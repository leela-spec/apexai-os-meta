#!/usr/bin/env python3
"""Deterministic validator/applier for the exact-match patch-pack class.

See apex-meta/SmallSkills/Patching/instructions/PatchPackGenerationSOP.md for the
artifact format this tool consumes: a pack directory containing
`package-manifest.json`, `patches/*.exact-match.md` (each holding one or more
`<file>/<old>/<new>` blocks), and a `new-files/<repo-relative-path>` mirror tree
for brand-new files.

Stdlib only. Newline handling: matching is done on newline-normalized content
(CRLF and LF compare equal), but every write preserves the target file's own
existing newline style rather than imposing one.

Known limitation: a block's <old>/<new> body must not itself contain a line
that is exactly "</old>" or "</new>", since the parser terminates on the first
such line. This mirrors the format already in production use in this repo.

Subcommands:
  check           Dry run. Verifies baseline commit, and that every block's
                  <old> text occurs in its live target exactly once.
  apply           Applies the pack. Refuses unless a fresh `check` is clean.
  verify-manifest Recomputes SHA-256 of every artifact in the pack and compares
                  to package-manifest.json's artifact_sha256 map (pack integrity,
                  not target-repo state).
  new-baseline    Prints current HEAD plus per-target-file hashes, to stamp a
                  new pack's inspected_commit and starting point.
"""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import re
import subprocess
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional

MANIFEST_NAME = "package-manifest.json"

BLOCK_RE = re.compile(
    r"<file>(?P<file>[^\n]+?)</file>\s*\n"
    r"<old>\n(?P<old>.*?)\n</old>\s*\n"
    r"<new>\n(?P<new>.*?)\n</new>",
    re.DOTALL,
)


def normalize_newlines(text: str) -> str:
    return text.replace("\r\n", "\n").replace("\r", "\n")


def detect_newline_style(raw: bytes) -> str:
    return "\r\n" if b"\r\n" in raw else "\n"


def sha256_bytes(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()


def sha256_file(path: Path) -> str:
    return sha256_bytes(path.read_bytes())


def load_manifest(pack_dir: Path) -> Dict[str, Any]:
    path = pack_dir / MANIFEST_NAME
    if not path.exists():
        raise SystemExit(f"Missing manifest: {path}")
    return json.loads(path.read_text(encoding="utf-8"))


def parse_patch_file(path: Path) -> List[Dict[str, str]]:
    text = path.read_text(encoding="utf-8-sig")
    blocks = []
    for match in BLOCK_RE.finditer(text):
        blocks.append(
            {
                "file": match.group("file").strip(),
                "old": match.group("old"),
                "new": match.group("new"),
            }
        )
    if not blocks:
        raise SystemExit(f"No <file>/<old>/<new> blocks found in {path}")
    return blocks


def git_head(repo_root: Path) -> Optional[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(repo_root), "rev-parse", "HEAD"],
            capture_output=True,
            text=True,
            check=True,
        )
        return result.stdout.strip()
    except Exception:
        return None


def resolve_target(repo_root: Path, file_field: str) -> Path:
    candidate = Path(file_field)
    if candidate.is_absolute():
        return candidate
    return (repo_root / file_field).resolve()


def atomic_write(path: Path, data: bytes) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    tmp = path.with_name(f".{path.name}.{os.getpid()}.tmp")
    try:
        with open(tmp, "wb") as handle:
            handle.write(data)
            handle.flush()
            os.fsync(handle.fileno())
        os.replace(tmp, path)
    finally:
        if tmp.exists():
            tmp.unlink()


def check_pack(pack_dir: Path, repo_root: Path) -> Dict[str, Any]:
    manifest = load_manifest(pack_dir)
    report: Dict[str, Any] = {
        "pack": str(pack_dir),
        "repo": str(repo_root),
        "baseline_ok": None,
        "blocks": [],
        "new_files": [],
        "status": "ok",
    }

    inspected = manifest.get("inspected_commit")
    head = git_head(repo_root)
    if inspected and head:
        report["baseline_ok"] = inspected == head
        if inspected != head:
            report["status"] = "blocked"
            report["baseline_mismatch"] = {"inspected_commit": inspected, "current_head": head}

    all_ok = report["baseline_ok"] is not False
    for rel_patch in manifest.get("patch_order", []):
        patch_path = pack_dir / rel_patch
        if not patch_path.exists():
            report["blocks"].append({"patch": rel_patch, "status": "missing_patch_file"})
            all_ok = False
            continue
        for index, block in enumerate(parse_patch_file(patch_path)):
            target = resolve_target(repo_root, block["file"])
            entry: Dict[str, Any] = {"patch": rel_patch, "index": index, "target": str(target)}
            if not target.exists():
                entry["status"] = "target_missing"
                all_ok = False
            else:
                text = target.read_bytes().decode("utf-8-sig")
                norm_text = normalize_newlines(text)
                norm_old = normalize_newlines(block["old"])
                count = norm_text.count(norm_old)
                if count == 0:
                    entry["status"] = "zero_match"
                    all_ok = False
                elif count > 1:
                    entry["status"] = "multi_match"
                    entry["match_count"] = count
                    all_ok = False
                else:
                    entry["status"] = "ok"
            report["blocks"].append(entry)

    for rel_new in manifest.get("new_files", []):
        src = pack_dir / "new-files" / rel_new
        dest = resolve_target(repo_root, rel_new)
        entry = {"path": rel_new}
        if not src.exists():
            entry["status"] = "missing_source_in_pack"
            all_ok = False
        elif dest.exists():
            if sha256_file(src) == sha256_file(dest):
                entry["status"] = "identical_already_present"
            else:
                entry["status"] = "conflict_exists_different"
                all_ok = False
        else:
            entry["status"] = "ok_will_create"
        report["new_files"].append(entry)

    if not all_ok:
        report["status"] = "blocked"
    return report


def apply_pack(pack_dir: Path, repo_root: Path) -> Dict[str, Any]:
    report = check_pack(pack_dir, repo_root)
    if report["status"] != "ok":
        report["applied"] = False
        return report

    manifest = load_manifest(pack_dir)
    applied_blocks = []
    for rel_patch in manifest.get("patch_order", []):
        patch_path = pack_dir / rel_patch
        for index, block in enumerate(parse_patch_file(patch_path)):
            target = resolve_target(repo_root, block["file"])
            raw = target.read_bytes()
            newline = detect_newline_style(raw)
            text = raw.decode("utf-8-sig")
            norm_text = normalize_newlines(text)
            norm_old = normalize_newlines(block["old"])
            norm_new = normalize_newlines(block["new"])
            if norm_text.count(norm_old) != 1:
                raise SystemExit(
                    f"Aborting apply: block became non-unique since check "
                    f"({rel_patch}#{index} -> {target}); target changed mid-run"
                )
            replaced = norm_text.replace(norm_old, norm_new, 1)
            out_text = replaced.replace("\n", newline)
            atomic_write(target, out_text.encode("utf-8"))
            applied_blocks.append({"patch": rel_patch, "index": index, "target": str(target)})

    created_files = []
    for rel_new in manifest.get("new_files", []):
        src = pack_dir / "new-files" / rel_new
        dest = resolve_target(repo_root, rel_new)
        if dest.exists():
            continue
        atomic_write(dest, src.read_bytes())
        created_files.append(str(dest))

    report["applied"] = True
    report["applied_blocks"] = applied_blocks
    report["created_files"] = created_files
    return report


def verify_manifest(pack_dir: Path) -> Dict[str, Any]:
    manifest = load_manifest(pack_dir)
    hashes = manifest.get("artifact_sha256", {})
    results = []
    ok = True

    for rel, expected in hashes.items():
        path = pack_dir / rel
        if not path.exists():
            results.append({"path": rel, "status": "missing"})
            ok = False
            continue
        actual = sha256_file(path)
        status = "ok" if actual == expected else "mismatch"
        if status != "ok":
            ok = False
        results.append({"path": rel, "status": status, "expected": expected, "actual": actual})

    for sub in ("patches", "new-files"):
        base = pack_dir / sub
        if base.exists():
            for candidate in sorted(base.rglob("*")):
                if candidate.is_file():
                    rel = candidate.relative_to(pack_dir).as_posix()
                    if rel not in hashes:
                        results.append({"path": rel, "status": "unhashed_in_manifest"})
                        ok = False

    return {"pack": str(pack_dir), "status": "ok" if ok else "mismatch", "artifacts": results}


def new_baseline(repo_root: Path, targets: List[str]) -> Dict[str, Any]:
    head = git_head(repo_root)
    hashes = {}
    for target in targets:
        path = resolve_target(repo_root, target)
        if path.exists():
            hashes[target] = sha256_file(path)
    return {"repo": str(repo_root), "inspected_commit": head, "target_hashes": hashes}


def main(argv: Optional[List[str]] = None) -> int:
    parser = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    sub = parser.add_subparsers(dest="command", required=True)

    check_cmd = sub.add_parser("check", help="Dry-run validate every block matches exactly once")
    check_cmd.add_argument("--pack", required=True)
    check_cmd.add_argument("--repo", required=True)

    apply_cmd = sub.add_parser("apply", help="Apply the pack; refuses unless check is clean")
    apply_cmd.add_argument("--pack", required=True)
    apply_cmd.add_argument("--repo", required=True)

    verify_cmd = sub.add_parser("verify-manifest", help="Verify pack-internal artifact hashes")
    verify_cmd.add_argument("--pack", required=True)

    baseline_cmd = sub.add_parser("new-baseline", help="Print current HEAD and target-file hashes for a new pack")
    baseline_cmd.add_argument("--repo", required=True)
    baseline_cmd.add_argument("--targets", nargs="+", required=True)

    args = parser.parse_args(argv)

    if args.command == "check":
        report = check_pack(Path(args.pack), Path(args.repo).resolve())
    elif args.command == "apply":
        report = apply_pack(Path(args.pack), Path(args.repo).resolve())
    elif args.command == "verify-manifest":
        report = verify_manifest(Path(args.pack))
    elif args.command == "new-baseline":
        report = new_baseline(Path(args.repo).resolve(), args.targets)
    else:  # pragma: no cover - argparse enforces choices
        raise SystemExit(2)

    print(json.dumps(report, indent=2, ensure_ascii=False, sort_keys=True))
    return 0 if report.get("status", "ok") == "ok" else 1


if __name__ == "__main__":
    raise SystemExit(main())
