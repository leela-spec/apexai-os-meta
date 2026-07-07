#!/usr/bin/env python3
"""Repair and apply the Apex loop-skill audit fixes patch pack.

This script exists because the downloaded patch files were not Git-generated
against a local clone. It repairs patch artifacts in a temporary branch, then
uses Git-native apply for the final target-file state.
"""
from __future__ import annotations

import argparse
import re
import shutil
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Sequence, Tuple


def run(cmd: Sequence[str], cwd: Path, check: bool = True, capture: bool = False) -> subprocess.CompletedProcess[str]:
    proc = subprocess.run(cmd, cwd=cwd, text=True, capture_output=capture)
    if check and proc.returncode != 0:
        detail = (proc.stdout or "") + (proc.stderr or "")
        raise SystemExit(f"command failed: {' '.join(cmd)}\n{detail}")
    return proc


def rel(path: Path) -> str:
    return path.as_posix()


def parse_manifest_map(path: Path) -> Dict[str, str]:
    text = path.read_text(encoding="utf-8", errors="replace")
    block_match = re.search(r"patch_to_target_map:\n(?P<body>.*?)(?:\n\n|\n  expected_changed_files:)", text, re.S)
    if not block_match:
        raise SystemExit(f"patch_to_target_map not found in {path}")
    mapping: Dict[str, str] = {}
    for line in block_match.group("body").splitlines():
        m = re.match(r'\s+"([^"]+\.patch)":\s+"([^"]+)"\s*$', line)
        if m:
            mapping[m.group(1)] = m.group(2)
    if not mapping:
        raise SystemExit(f"no patch mappings parsed from {path}")
    return mapping


def patch_targets(patch: Path) -> List[str]:
    targets: List[str] = []
    for line in patch.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("+++ b/"):
            targets.append(line[6:])
    return sorted(set(targets))


def copy_patch_pack(src: Path, dest: Path) -> None:
    if not src.exists():
        raise SystemExit(f"download patch dir missing: {src}")
    dest.mkdir(parents=True, exist_ok=True)
    for item in src.iterdir():
        target = dest / item.name
        if item.is_dir():
            if target.exists():
                shutil.rmtree(target)
            shutil.copytree(item, target)
        else:
            shutil.copy2(item, target)


def git_status_paths(repo: Path) -> List[str]:
    out = run(["git", "status", "--porcelain"], repo, capture=True).stdout
    paths: List[str] = []
    for raw in out.splitlines():
        path = raw[3:] if len(raw) > 3 else ""
        if " -> " in path:
            path = path.split(" -> ", 1)[1]
        paths.append(path.replace("\\", "/"))
    return paths


def ensure_no_dirty_target_overlap(repo: Path, targets: Iterable[str]) -> None:
    target_set = set(targets)
    overlap = sorted(path for path in git_status_paths(repo) if path in target_set)
    if overlap:
        raise SystemExit("dirty files overlap patch targets:\n" + "\n".join(overlap))


def check_patch_map(patch_dir: Path, mapping: Dict[str, str]) -> None:
    for patch_name, target in mapping.items():
        patch = patch_dir / patch_name
        if not patch.exists():
            raise SystemExit(f"missing patch: {patch}")
        targets = patch_targets(patch)
        if targets != [target]:
            raise SystemExit(f"target mismatch for {patch_name}: expected {target}, got {targets}")


def patch_files(patch_dir: Path) -> List[Path]:
    return sorted(p for p in patch_dir.glob("*.patch") if p.name[0].isdigit())


def git_apply_check_all(repo: Path, patches: Sequence[Path]) -> Tuple[bool, str]:
    output: List[str] = []
    for patch in patches:
        proc = run(["git", "apply", "--check", str(patch)], repo, check=False, capture=True)
        output.append(f"CHECK {patch}")
        output.append((proc.stdout or "") + (proc.stderr or ""))
        if proc.returncode != 0:
            return False, "\n".join(output)
    return True, "\n".join(output)


def split_hunks(patch_text: str) -> List[List[str]]:
    hunks: List[List[str]] = []
    current: List[str] | None = None
    for line in patch_text.splitlines():
        if line.startswith("@@"):
            if current:
                hunks.append(current)
            current = []
            continue
        if current is not None and line[:1] in {" ", "+", "-"} and not line.startswith(("---", "+++")):
            current.append(line)
    if current:
        hunks.append(current)
    return hunks


def seq_from_hunk(hunk: List[str], tags: set[str]) -> List[str]:
    return [line[1:] + "\n" for line in hunk if line[:1] in tags]


def find_seq(lines: List[str], needle: List[str], start: int = 0) -> int:
    if not needle:
        return -1
    limit = len(lines) - len(needle)
    for i in range(start, limit + 1):
        if lines[i : i + len(needle)] == needle:
            return i
    return -1


def fuzzy_apply_patch_to_target(patch: Path, target: Path) -> None:
    patch_text = patch.read_text(encoding="utf-8", errors="replace")
    lines = target.read_text(encoding="utf-8", errors="replace").splitlines(keepends=True)
    for hunk in split_hunks(patch_text):
        old_seq = seq_from_hunk(hunk, {" ", "-"})
        new_seq = seq_from_hunk(hunk, {" ", "+"})
        idx = find_seq(lines, old_seq)
        if idx >= 0:
            lines[idx : idx + len(old_seq)] = new_seq
            continue
        search_pos = 0
        changed = False
        i = 0
        while i < len(hunk):
            tag = hunk[i][:1]
            if tag == "-":
                old_block: List[str] = []
                while i < len(hunk) and hunk[i].startswith("-"):
                    old_block.append(hunk[i][1:] + "\n")
                    i += 1
                new_block: List[str] = []
                while i < len(hunk) and hunk[i].startswith("+"):
                    new_block.append(hunk[i][1:] + "\n")
                    i += 1
                idx = find_seq(lines, old_block, search_pos)
                if idx < 0:
                    raise SystemExit(f"could not find removal block in {target}: {old_block!r}")
                lines[idx : idx + len(old_block)] = new_block
                search_pos = idx + len(new_block)
                changed = True
                continue
            if tag == "+":
                add_block: List[str] = []
                while i < len(hunk) and hunk[i].startswith("+"):
                    add_block.append(hunk[i][1:] + "\n")
                    i += 1
                if find_seq(lines, add_block) >= 0:
                    changed = True
                    continue
                previous_context = None
                for j in range(i - len(add_block) - 1, -1, -1):
                    if hunk[j].startswith(" "):
                        previous_context = hunk[j][1:] + "\n"
                        break
                next_context = None
                for j in range(i, len(hunk)):
                    if hunk[j].startswith(" "):
                        next_context = hunk[j][1:] + "\n"
                        break
                if previous_context and previous_context in lines:
                    insert_at = max(k for k, value in enumerate(lines) if value == previous_context) + 1
                    lines[insert_at:insert_at] = add_block
                    changed = True
                elif next_context and next_context in lines:
                    insert_at = lines.index(next_context)
                    lines[insert_at:insert_at] = add_block
                    changed = True
                else:
                    raise SystemExit(f"could not place addition in {target}: {add_block!r}")
                continue
            i += 1
        if not changed:
            raise SystemExit(f"hunk was not applied in {target}")
    target.write_text("".join(lines), encoding="utf-8", newline="\n")


def repair_patches(repo: Path, patch_dir: Path, mapping: Dict[str, str]) -> None:
    base = run(["git", "rev-parse", "HEAD"], repo, capture=True).stdout.strip()
    run(["git", "checkout", "-B", "tmp/apex-loop-skill-audit-fixes-repair", base], repo)
    try:
        for patch in patch_files(patch_dir):
            target_rel = mapping[patch.name]
            target = repo / target_rel
            run(["git", "checkout", base, "--", target_rel], repo)
            fuzzy_apply_patch_to_target(patch, target)
            diff = run(["git", "diff", "--", target_rel], repo, capture=True).stdout
            if not diff.strip():
                raise SystemExit(f"repair produced empty patch for {patch.name}")
            patch.write_text(diff, encoding="utf-8", newline="\n")
            run(["git", "checkout", base, "--", target_rel], repo)
    finally:
        run(["git", "checkout", "main"], repo)


def apply_patches(repo: Path, patches: Sequence[Path]) -> None:
    for patch in patches:
        run(["git", "apply", str(patch)], repo)


def changed_files(repo: Path) -> List[str]:
    return sorted(run(["git", "diff", "--name-only"], repo, capture=True).stdout.splitlines())


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", type=Path, required=True)
    parser.add_argument("--download-patch-dir", type=Path, required=True)
    parser.add_argument("--repo-patch-dir", type=Path, required=True)
    parser.add_argument("--repair", action="store_true")
    parser.add_argument("--apply", action="store_true")
    parser.add_argument("--commit", action="store_true")
    parser.add_argument("--push", action="store_true")
    args = parser.parse_args()

    repo = args.repo_root.resolve()
    repo_patch_dir = (repo / args.repo_patch_dir).resolve()
    copy_patch_pack(args.download_patch_dir.resolve(), repo_patch_dir)

    mapping = parse_manifest_map(repo_patch_dir / "000-patch-manifest.md")
    check_patch_map(repo_patch_dir, mapping)
    ensure_no_dirty_target_overlap(repo, mapping.values())
    baseline_changed = set(changed_files(repo))

    patches = patch_files(repo_patch_dir)
    ok, output = git_apply_check_all(repo, patches)
    print(output)
    if not ok:
        if not args.repair:
            raise SystemExit("git apply --check failed; rerun with --repair")
        repair_patches(repo, repo_patch_dir, mapping)
        ok, output = git_apply_check_all(repo, patches)
        print(output)
        if not ok:
            raise SystemExit("git apply --check still failed after repair")

    if args.apply:
        apply_patches(repo, patches)
        actual = changed_files(repo)
        new_changes = [path for path in actual if path not in baseline_changed]
        repo_patch_prefix = rel(repo_patch_dir.relative_to(repo)) + "/"
        allowed = set(mapping.values())
        unexpected = [
            path
            for path in new_changes
            if path not in allowed and not path.startswith(repo_patch_prefix)
        ]
        if unexpected:
            raise SystemExit("unexpected changed files:\n" + "\n".join(unexpected))
        run(["git", "diff", "--check"], repo)

    if args.commit:
        run(["git", "add", str(repo_patch_dir.relative_to(repo))], repo)
        for target in mapping.values():
            run(["git", "add", target], repo)
        run(["git", "commit", "-m", "Apply Apex loop skill audit fixes"], repo)

    if args.push:
        run(["git", "push", "origin", "main"], repo)

    print("FINAL_REPORT:")
    print("  verdict: PASS")
    print("  repaired_patch_pack:", "true" if args.repair else "false")
    print("  applied:", "true" if args.apply else "false")
    print("  committed:", "true" if args.commit else "false")
    print("  pushed:", "true" if args.push else "false")
    return 0


if __name__ == "__main__":
    sys.exit(main())
