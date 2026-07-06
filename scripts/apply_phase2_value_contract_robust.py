#!/usr/bin/env python3
"""
Deterministic Apex KB Phase 2 value-contract patch applier.

This script is intentionally conservative:
- It never uses an LLM patch/edit primitive.
- It first tries git apply with validation.
- If git apply fails, it uses a deterministic line-based unified-diff fallback.
- It only allows the nine declared Apex KB contract/template files to change.
- It verifies required/forbidden value-contract markers before commit.
"""

from __future__ import annotations

import argparse
import collections
import datetime as _dt
import fnmatch
from pathlib import Path
import re
import shutil
import subprocess
from typing import List, Dict, Tuple, Optional


EXPECTED = collections.OrderedDict([
    ("001-wiki-page-templates.patch", ".claude/skills/apex-kb/templates/wiki-page-templates.md"),
    ("002-ingest-analysis-template.patch", ".claude/skills/apex-kb/templates/ingest-analysis-template.md"),
    ("003-kb-contract.patch", ".claude/skills/apex-kb/references/kb-contract.md"),
    ("004-ingest-query-lint-audit-rules.patch", ".claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md"),
    ("005-acceptance-tests.patch", ".claude/skills/apex-kb/references/acceptance-tests.md"),
    ("006-skill.patch", ".claude/skills/apex-kb/SKILL.md"),
    ("007-lifecycle-state-machine.patch", ".claude/skills/apex-kb/references/lifecycle-state-machine.md"),
    ("008-knowledge-promotion-rules.patch", ".claude/skills/apex-kb/references/knowledge-promotion-rules.md"),
    ("009-kb-schema-template.patch", ".claude/skills/apex-kb/templates/kb-schema-template.md"),
])

REQUIRED_STRINGS = [
    "Adaptive Ranked Source Set",
    "Macro / Meso / Micro",
    "Routes Here",
    "Uncertainty / Raw Source Triggers",
]

FORBIDDEN_STRINGS = [
    "page_value_score",
    "source_cluster_map",
]

FORBIDDEN_CHANGED_PATTERNS = [
    ".claude/skills/apex-kb2/*",
    "apex-meta/kb/*/wiki/*",
    "apex-meta/kb/*/ingest-analysis/*",
    "apex-meta/scripts/*",
    "derived/*",
    "outputs/*",
    "raw/*",
    "sources/*",
]

HUNK_RE = re.compile(r"^@@ -(\d+)(?:,(\d+))? \+(\d+)(?:,(\d+))? @@")
INDEX_RE = re.compile(r"^index ([0-9a-f]+)\.\.([0-9a-f]+)(?: [0-7]+)?$")
DIFF_RE = re.compile(r"^diff --git a/(.*?) b/(.*?)$")


class PatchError(RuntimeError):
    pass


def log(msg: str) -> None:
    print(msg, flush=True)


def norm_path(p: str) -> str:
    return p.replace("\\", "/").strip()


def run(cmd: List[str], cwd: Path, check: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(cmd, cwd=str(cwd), text=True, stdout=subprocess.PIPE, stderr=subprocess.STDOUT)
    if check and proc.returncode != 0:
        raise PatchError("Command failed: {}\n{}".format(" ".join(cmd), proc.stdout))
    return proc


def git(cwd: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess:
    return run(["git", *args], cwd, check=check)


def split_git_lines(text: str) -> List[str]:
    if not text:
        return []
    return [line.strip() for line in text.splitlines() if line.strip()]


def decode_text(raw: bytes) -> Tuple[str, str]:
    newline = "\r\n" if raw.count(b"\r\n") > 0 and raw.count(b"\r\n") >= raw.count(b"\n") / 2 else "\n"
    text = raw.decode("utf-8-sig")
    text = text.replace("\r\n", "\n").replace("\r", "\n")
    return text, newline


def encode_text(text: str, newline: str) -> bytes:
    if newline != "\n":
        text = text.replace("\n", newline)
    return text.encode("utf-8")


def read_normalized(path: Path) -> Tuple[str, str]:
    return decode_text(path.read_bytes())


def write_normalized(path: Path, text: str, newline: str) -> None:
    path.write_bytes(encode_text(text, newline))


def parse_patch(patch_path: Path) -> Dict:
    raw = patch_path.read_bytes()
    text, _newline = decode_text(raw)
    lines = text.splitlines(True)

    diff_headers = [line.rstrip("\n") for line in lines if line.startswith("diff --git ")]
    if len(diff_headers) != 1:
        raise PatchError(f"{patch_path.name}: expected exactly one diff header, found {len(diff_headers)}")

    m = DIFF_RE.match(diff_headers[0])
    if not m:
        raise PatchError(f"{patch_path.name}: invalid diff header: {diff_headers[0]}")
    a_path, b_path = norm_path(m.group(1)), norm_path(m.group(2))
    if a_path != b_path:
        raise PatchError(f"{patch_path.name}: rename/copy patches are not allowed: {a_path} -> {b_path}")

    index_lines = [line.rstrip("\n") for line in lines if line.startswith("index ")]
    if len(index_lines) != 1:
        raise PatchError(f"{patch_path.name}: expected exactly one index line, found {len(index_lines)}")
    im = INDEX_RE.match(index_lines[0])
    if not im:
        raise PatchError(f"{patch_path.name}: invalid index line: {index_lines[0]}")
    old_blob, new_blob = im.group(1), im.group(2)

    hunks = []
    i = 0
    while i < len(lines):
        header = lines[i].rstrip("\n")
        hm = HUNK_RE.match(header)
        if not hm:
            i += 1
            continue

        old_start = int(hm.group(1))
        old_count = int(hm.group(2) or "1")
        new_start = int(hm.group(3))
        new_count = int(hm.group(4) or "1")
        i += 1
        body = []
        while i < len(lines):
            if lines[i].startswith("@@ ") or lines[i].startswith("diff --git "):
                break
            body.append(lines[i])
            i += 1

        counted_old = sum(1 for line in body if line.startswith((" ", "-")))
        counted_new = sum(1 for line in body if line.startswith((" ", "+")))
        if counted_old != old_count or counted_new != new_count:
            raise PatchError(
                f"{patch_path.name}: hunk count mismatch at {header}: "
                f"old header/count {old_count}/{counted_old}, new header/count {new_count}/{counted_new}"
            )
        hunks.append({
            "header": header,
            "old_start": old_start,
            "old_count": old_count,
            "new_start": new_start,
            "new_count": new_count,
            "body": body,
        })

    if not hunks:
        raise PatchError(f"{patch_path.name}: no hunks found")

    return {
        "patch_name": patch_path.name,
        "path": a_path,
        "old_blob": old_blob,
        "new_blob": new_blob,
        "hunks": hunks,
    }


def seq_equal(a: List[str], b: List[str]) -> bool:
    return a == b


def seq_equal_ws(a: List[str], b: List[str]) -> bool:
    return [x.rstrip() for x in a] == [x.rstrip() for x in b]


def find_sequence(lines: List[str], seq: List[str], expected_idx: int) -> Tuple[Optional[int], str]:
    if not seq:
        return max(0, min(expected_idx, len(lines))), "empty"

    max_start = len(lines) - len(seq)
    if max_start < 0:
        return None, "too_short"

    candidates = []
    for c in [expected_idx, expected_idx - 1, expected_idx + 1]:
        if 0 <= c <= max_start and c not in candidates:
            candidates.append(c)

    for c in candidates:
        if seq_equal(lines[c:c + len(seq)], seq):
            return c, "expected_exact"

    lo = max(0, expected_idx - 50)
    hi = min(max_start, expected_idx + 50)
    for c in range(lo, hi + 1):
        if seq_equal(lines[c:c + len(seq)], seq):
            return c, "near_exact"

    for c in range(0, max_start + 1):
        if seq_equal(lines[c:c + len(seq)], seq):
            return c, "global_exact"

    for c in candidates:
        if seq_equal_ws(lines[c:c + len(seq)], seq):
            return c, "expected_ws"

    for c in range(lo, hi + 1):
        if seq_equal_ws(lines[c:c + len(seq)], seq):
            return c, "near_ws"

    for c in range(0, max_start + 1):
        if seq_equal_ws(lines[c:c + len(seq)], seq):
            return c, "global_ws"

    return None, "not_found"


def hunk_old_new_lines(hunk: Dict) -> Tuple[List[str], List[str]]:
    old_lines: List[str] = []
    new_lines: List[str] = []
    for raw_line in hunk["body"]:
        if raw_line.startswith(" "):
            old_lines.append(raw_line[1:])
            new_lines.append(raw_line[1:])
        elif raw_line.startswith("-"):
            old_lines.append(raw_line[1:])
        elif raw_line.startswith("+"):
            new_lines.append(raw_line[1:])
        elif raw_line.startswith("\\"):
            continue
        else:
            raise PatchError(f"Invalid hunk line: {raw_line!r}")
    return old_lines, new_lines


def backup_file(repo: Path, target: Path, backup_root: Path) -> None:
    rel = target.relative_to(repo)
    dest = backup_root / rel
    dest.parent.mkdir(parents=True, exist_ok=True)
    shutil.copy2(target, dest)


def apply_patch_fallback(repo: Path, patch: Dict, backup_root: Path) -> None:
    target = repo / patch["path"]
    if not target.exists():
        raise PatchError(f"Target file does not exist: {patch['path']}")

    backup_file(repo, target, backup_root)

    text, newline = read_normalized(target)
    lines = text.splitlines(True)
    offset = 0

    for hunk in patch["hunks"]:
        old_lines, new_lines = hunk_old_new_lines(hunk)
        expected = max(0, hunk["old_start"] - 1 + offset)
        idx, mode = find_sequence(lines, old_lines, expected)

        if idx is None:
            already_idx, already_mode = find_sequence(lines, new_lines, expected)
            if already_idx is not None:
                log(f"  hunk already present: {patch['patch_name']} {hunk['header']} ({already_mode})")
                continue

            context_preview = "".join(old_lines[:8])
            raise PatchError(
                f"Fallback failed for {patch['patch_name']} {hunk['header']} in {patch['path']}\n"
                f"Could not locate old block. First old/context lines:\n{context_preview}"
            )

        lines[idx:idx + len(old_lines)] = new_lines
        offset += len(new_lines) - len(old_lines)
        log(f"  fallback applied hunk: {patch['patch_name']} {hunk['header']} at line {idx + 1} ({mode})")

    write_normalized(target, "".join(lines), newline)


def package_text(repo: Path) -> str:
    root = repo / ".claude" / "skills" / "apex-kb"
    out = []
    for path in sorted(root.rglob("*")):
        if path.is_file():
            out.append(path.read_text(encoding="utf-8", errors="replace"))
    return "\n".join(out)


def verify_value_contract(repo: Path) -> None:
    text = package_text(repo)
    missing = [s for s in REQUIRED_STRINGS if s not in text]
    present_forbidden = [s for s in FORBIDDEN_STRINGS if s in text]
    if missing:
        raise PatchError("Required strings missing: " + ", ".join(missing))
    if present_forbidden:
        raise PatchError("Forbidden strings present: " + ", ".join(present_forbidden))


def changed_files(repo: Path) -> List[str]:
    proc = git(repo, "diff", "--name-only")
    return [norm_path(x) for x in split_git_lines(proc.stdout)]


def verify_scope(repo: Path) -> None:
    changed = changed_files(repo)
    expected = [norm_path(p) for p in EXPECTED.values()]
    unexpected = [p for p in changed if p not in expected]
    missing = [p for p in expected if p not in changed]

    forbidden = []
    for p in changed:
        for pattern in FORBIDDEN_CHANGED_PATTERNS:
            if fnmatch.fnmatch(p, pattern):
                forbidden.append(p)
                break

    if unexpected:
        raise PatchError("Unexpected changed files: " + ", ".join(unexpected))
    if missing:
        raise PatchError("Expected target files not changed: " + ", ".join(missing))
    if forbidden:
        raise PatchError("Forbidden changed paths: " + ", ".join(forbidden))


def current_blob(repo: Path, path: str) -> str:
    proc = git(repo, "hash-object", "--", path)
    return proc.stdout.strip()


def patch_precheck(repo: Path, patches: List[Dict]) -> None:
    log("== Patch precheck ==")
    for patch in patches:
        expected_path = norm_path(EXPECTED[patch["patch_name"]])
        if patch["path"] != expected_path:
            raise PatchError(f"{patch['patch_name']}: expected target {expected_path}, got {patch['path']}")
        live = current_blob(repo, patch["path"])
        old = patch["old_blob"]
        verdict = "MATCH" if live.startswith(old) else "MISMATCH"
        log(f"{patch['patch_name']}: target={patch['path']} old_blob={old} live_blob={live[:len(old)]} verdict={verdict}")


def git_apply_all(repo: Path, patch_dir: Path, mode: str) -> bool:
    args_by_mode = {
        "plain": ["apply", "--whitespace=nowarn", "--recount"],
        "ignore-space": ["apply", "--whitespace=nowarn", "--recount", "--ignore-space-change", "--ignore-whitespace"],
        "3way": ["apply", "--3way", "--whitespace=nowarn", "--recount"],
    }
    args = args_by_mode[mode]
    log(f"== Trying git apply mode: {mode} ==")

    for patch_name in EXPECTED.keys():
        patch_path = str(patch_dir / patch_name)
        check_args = args.copy()
        check_args.insert(1, "--check")
        proc = git(repo, *check_args, patch_path, check=False)
        if proc.returncode != 0:
            log(f"git apply --check failed in mode {mode} for {patch_name}:\n{proc.stdout}")
            return False

    for patch_name in EXPECTED.keys():
        patch_path = str(patch_dir / patch_name)
        proc = git(repo, *args, patch_path, check=False)
        if proc.returncode != 0:
            log(f"git apply failed in mode {mode} for {patch_name}:\n{proc.stdout}")
            return False

    return True


def hard_reset(repo: Path) -> None:
    git(repo, "reset", "--hard", "HEAD")


def ensure_clean(repo: Path) -> None:
    proc = git(repo, "status", "--porcelain")
    dirty = split_git_lines(proc.stdout)
    if dirty:
        raise PatchError("Worktree is dirty before patching:\n" + "\n".join(dirty))


def origin_check(repo: Path) -> None:
    proc = git(repo, "remote", "get-url", "origin")
    origin = proc.stdout.strip()
    if not re.search(r"leela-spec[/\\]apexai-os-meta(?:\.git)?$", origin):
        raise PatchError(f"Unexpected origin URL: {origin}")
    log(f"origin: {origin}")


def commit_and_push(repo: Path, no_push: bool) -> None:
    expected = [norm_path(p) for p in EXPECTED.values()]
    git(repo, "add", "--", *expected)
    git(repo, "commit", "-m", "Strengthen Apex KB Phase 2 value contract")
    if not no_push:
        git(repo, "push", "origin", "main")


def main() -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument("--repo-root", default=r"C:\GitDev\apexai-os-meta")
    parser.add_argument("--patch-dir", default=r"apex-meta\handoff\Apex-Kb_Lifecycle_Analysis\phase2-value-contract")
    parser.add_argument("--no-push", action="store_true")
    parser.add_argument("--force-fallback", action="store_true")
    args = parser.parse_args()

    repo = Path(args.repo_root).resolve()
    patch_dir = Path(args.patch_dir)
    if not patch_dir.is_absolute():
        patch_dir = repo / patch_dir
    patch_dir = patch_dir.resolve()

    try:
        if not repo.exists():
            raise PatchError(f"Repo root not found: {repo}")
        if not patch_dir.exists():
            raise PatchError(f"Patch directory not found: {patch_dir}")

        inside = git(repo, "rev-parse", "--is-inside-work-tree").stdout.strip()
        if inside != "true":
            raise PatchError("Not inside a git worktree")

        top = Path(git(repo, "rev-parse", "--show-toplevel").stdout.strip()).resolve()
        if top != repo:
            log(f"Using git top-level repo: {top}")
            repo = top

        origin_check(repo)
        git(repo, "checkout", "main")
        git(repo, "pull", "--ff-only", "origin", "main")
        ensure_clean(repo)

        patches = []
        for patch_name in EXPECTED.keys():
            patch_path = patch_dir / patch_name
            if not patch_path.exists():
                raise PatchError(f"Missing patch file: {patch_path}")
            patches.append(parse_patch(patch_path))

        patch_precheck(repo, patches)

        applied = False
        if not args.force_fallback:
            for mode in ["plain", "ignore-space", "3way"]:
                hard_reset(repo)
                if git_apply_all(repo, patch_dir, mode):
                    applied = True
                    log(f"git apply succeeded with mode: {mode}")
                    break

        if not applied:
            hard_reset(repo)
            log("== Falling back to deterministic Python hunk applier ==")
            stamp = _dt.datetime.utcnow().strftime("%Y%m%dT%H%M%SZ")
            backup_root = repo / ".phase2-value-contract-backups" / stamp
            for patch in patches:
                apply_patch_fallback(repo, patch, backup_root)
            log(f"Backups written under: {backup_root}")

        verify_scope(repo)
        verify_value_contract(repo)
        commit_and_push(repo, args.no_push)

        final = git(repo, "status", "--porcelain").stdout.strip()
        if final:
            raise PatchError("Final worktree is not clean:\n" + final)

        log("FINAL_REPORT:")
        log("  verdict: PASS")
        log("  repo: leela-spec/apexai-os-meta")
        log("  branch: main")
        log(f"  pushed: {str(not args.no_push).lower()}")
        log("  changed_files:")
        for p in EXPECTED.values():
            log(f"    - {norm_path(p)}")
        return 0

    except Exception as exc:
        log("FINAL_REPORT:")
        log("  verdict: FAIL")
        log("  reason: |")
        for line in str(exc).splitlines():
            log("    " + line)
        try:
            log("  git_status:")
            status = git(repo, "status", "--short", check=False).stdout
            for line in status.splitlines():
                log("    " + line)
        except Exception:
            pass
        return 1


if __name__ == "__main__":
    raise SystemExit(main())
