#!/usr/bin/env python3
"""Deterministic scaffolding for LLM-assisted stub-function repair patch packs.

Division of labor this script enforces:
  LLM does:      identify the stub, write the replacement function body text.
  Script does:   worktree mgmt, checkout/diff/revert cycles, git apply --check
                 (individual + cumulative), py_compile, fixture construction,
                 CLI execution, JSON-path assertion checking, scope checks,
                 manifest assembly, and the final apply/commit/push to main.

Python stdlib only. No network. No shell-out beyond `git` and `python`.

Subcommands:
  worktree-add      create a disposable detached worktree
  worktree-remove   remove it
  gen-patch         diff target file(s) against clean HEAD, revert, validate
  validate          git apply --check (individual + cumulative) + py_compile
  run-fixture       build a fixture dir from a JSON spec, run commands, assert
  finalize          apply pack to a real repo/branch, verify scope, commit, push
"""
from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
import tempfile
from pathlib import Path
from typing import Any, Dict, List, Sequence


def run(cmd: Sequence[str], cwd: Path, check: bool = True, capture: bool = True) -> subprocess.CompletedProcess:
    proc = subprocess.run(list(cmd), cwd=str(cwd), text=True, capture_output=capture)
    if check and proc.returncode != 0:
        detail = (proc.stdout or "") + (proc.stderr or "")
        raise SystemExit(f"command failed ({proc.returncode}): {' '.join(cmd)}\n{detail}")
    return proc


def py_compile_no_cache(repo: Path, rel_path: str) -> subprocess.CompletedProcess:
    """Compile-check a file without writing into the tracked __pycache__/.
    `-m py_compile` always writes its .pyc (PYTHONDONTWRITEBYTECODE does not
    suppress it — that only affects import-time caching), so cfile is
    redirected to a throwaway path outside the repo instead."""
    with tempfile.TemporaryDirectory() as tmp:
        cfile = str(Path(tmp) / "compile_check.pyc")
        code = (
            "import py_compile, sys; "
            f"py_compile.compile(sys.argv[1], cfile={cfile!r}, doraise=True)"
        )
        return run([sys.executable, "-c", code, rel_path], repo, check=False)


def git_status_paths(repo: Path) -> List[str]:
    out = run(["git", "status", "--porcelain"], repo).stdout
    paths = []
    for raw in out.splitlines():
        p = raw[3:] if len(raw) > 3 else ""
        p = p.split(" -> ", 1)[1] if " -> " in p else p
        paths.append(p.replace("\\", "/"))
    return paths


def patch_targets(patch: Path) -> List[str]:
    targets = []
    for line in patch.read_text(encoding="utf-8", errors="replace").splitlines():
        if line.startswith("+++ b/"):
            targets.append(line[6:])
    return sorted(set(targets))


# ---------------------------------------------------------------- worktree

def cmd_worktree_add(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    run(["git", "worktree", "add", "--detach", str(Path(args.at).resolve()), args.ref], repo, capture=False)
    print(f"worktree ready: {args.at} @ {args.ref}")
    return 0


def cmd_worktree_remove(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    run(["git", "worktree", "remove", str(Path(args.at).resolve()), "--force"], repo)
    print(f"worktree removed: {args.at}")
    return 0


# ---------------------------------------------------------------- gen-patch

def cmd_gen_patch(args: argparse.Namespace) -> int:
    """Assumes the LLM already edited args.targets in place inside args.repo
    (a worktree). Diffs, verifies non-empty + expected scope, reverts the
    working tree, then validates the patch applies to the now-clean tree."""
    repo = Path(args.repo).resolve()
    patch_out = Path(args.out).resolve()
    targets = args.targets
    overlap = sorted(set(git_status_paths(repo)) & set(t for t in targets))
    dirty_before = set(git_status_paths(repo)) - set(targets)
    if dirty_before:
        print("WARN unrelated dirty files present (left untouched):", dirty_before, file=sys.stderr)

    diff = run(["git", "diff", "--no-ext-diff", "--"] + targets, repo).stdout
    if not diff.strip():
        raise SystemExit(f"no diff produced for {targets} — did you edit the file(s) in {repo} first?")
    patch_out.parent.mkdir(parents=True, exist_ok=True)
    patch_out.write_text(diff, encoding="utf-8", newline="\n")

    header_count = diff.count("\ndiff --git ") + (1 if diff.startswith("diff --git ") else 0)
    if header_count != len(targets):
        raise SystemExit(f"expected {len(targets)} diff --git header(s), got {header_count} — targets list may be wrong")

    run(["git", "checkout", "--"] + targets, repo)
    check = run(["git", "apply", "--check", str(patch_out)], repo, check=False)
    if check.returncode != 0:
        raise SystemExit(f"git apply --check failed for freshly-generated patch:\n{check.stdout}{check.stderr}")

    print(f"PATCH_OK: {patch_out} ({header_count} file(s): {', '.join(targets)})")
    return 0


# ---------------------------------------------------------------- validate

def cmd_validate(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    patch_dir = Path(args.patches).resolve()
    patches = sorted(p for p in patch_dir.glob("*.patch"))
    if not patches:
        raise SystemExit(f"no *.patch files under {patch_dir}")

    print("=== individual checks ===")
    for p in patches:
        r = run(["git", "apply", "--check", str(p)], repo, check=False)
        status = "OK" if r.returncode == 0 else "FAIL"
        print(f"{status}: {p.name}")
        if r.returncode != 0:
            raise SystemExit(r.stdout + r.stderr)

    print("=== cumulative check ===")
    run(["git", "apply", "--check"] + [str(p) for p in patches], repo)
    print("CUMULATIVE_CHECK_OK")

    print("=== cumulative apply + py_compile + scope + revert ===")
    run(["git", "apply"] + [str(p) for p in patches], repo)
    all_targets = sorted({t for p in patches for t in patch_targets(p)})
    changed = sorted(p for p in git_status_paths(repo) if p in set(all_targets))
    unexpected = sorted(set(git_status_paths(repo)) - set(all_targets) - {str(patch_dir.relative_to(repo)).replace("\\", "/") + "/"})
    if sorted(changed) != sorted(all_targets):
        raise SystemExit(f"scope mismatch: expected {all_targets}, got {changed}")
    for py_file in args.py_compile or []:
        r = py_compile_no_cache(repo, py_file)
        print(f"py_compile {py_file}: {'OK' if r.returncode == 0 else 'FAIL'}")
        if r.returncode != 0:
            run(["git", "checkout", "--"] + all_targets, repo)
            raise SystemExit(r.stdout + r.stderr)
    run(["git", "checkout", "--"] + all_targets, repo)
    print("REVERTED_CLEAN")
    if unexpected:
        print("NOTE unrelated pre-existing dirty paths (untouched):", unexpected, file=sys.stderr)
    return 0


# ---------------------------------------------------------------- fixture

def _get_path(obj: Any, dotted: str) -> Any:
    cur = obj
    for part in dotted.split("."):
        if isinstance(cur, list):
            cur = cur[int(part)]
        elif isinstance(cur, dict):
            cur = cur.get(part)
        else:
            return None
    return cur


def _check_assertion(value: Any, assertion: Dict[str, Any]) -> bool:
    if "equals" in assertion:
        return value == assertion["equals"]
    if "not_equals" in assertion:
        return value != assertion["not_equals"]
    if "gt" in assertion:
        return value is not None and value > assertion["gt"]
    if "lt" in assertion:
        return value is not None and value < assertion["lt"]
    if "contains" in assertion:
        return isinstance(value, (list, dict, str)) and assertion["contains"] in value
    if "not_empty" in assertion:
        return bool(value)
    if "is_empty" in assertion:
        return not value
    raise SystemExit(f"unrecognized assertion shape: {assertion}")


def cmd_run_fixture(args: argparse.Namespace) -> int:
    spec = json.loads(Path(args.spec).read_text(encoding="utf-8"))
    kb_root = Path(spec["kb_root"]).resolve()
    if kb_root.exists() and spec.get("reset", True):
        import shutil

        shutil.rmtree(kb_root)
    for rel, content in spec.get("files", {}).items():
        target = kb_root / rel
        target.parent.mkdir(parents=True, exist_ok=True)
        target.write_text(content, encoding="utf-8", newline="\n")

    failures = 0
    for command in spec.get("commands", []):
        argv = [a.replace("<kb_root>", str(kb_root)) for a in command["argv"]]
        proc = subprocess.run(argv, text=True, capture_output=True)
        result: Any = None
        parse_error = None
        try:
            result = json.loads(proc.stdout)
        except Exception as exc:
            parse_error = str(exc)
        print(f"--- {command.get('id', argv)} ---")
        if parse_error:
            print(f"  STDOUT_NOT_JSON: {parse_error}")
            print(f"  raw stdout: {proc.stdout[:400]}")
            print(f"  raw stderr: {proc.stderr[:400]}")
            failures += 1
            continue
        for assertion in command.get("assert", []):
            value = _get_path(result, assertion["path"])
            ok = _check_assertion(value, assertion)
            print(f"  {'PASS' if ok else 'FAIL'} {assertion['path']} = {value!r} vs {assertion}")
            if not ok:
                failures += 1

    print(f"=== {'ALL PASS' if failures == 0 else f'{failures} FAILURE(S)'} ===")
    return 1 if failures else 0


# ---------------------------------------------------------------- finalize

def cmd_finalize(args: argparse.Namespace) -> int:
    repo = Path(args.repo).resolve()
    patch_dir = Path(args.patches).resolve()
    patches = sorted(p for p in patch_dir.glob("*.patch"))
    all_targets = sorted({t for p in patches for t in patch_targets(p)})

    run(["git", "checkout", args.branch], repo)
    run(["git", "pull", "--ff-only", "origin", args.branch], repo)

    overlap = sorted(set(git_status_paths(repo)) & set(all_targets))
    if overlap:
        raise SystemExit(f"dirty files overlap patch targets, aborting: {overlap}")

    run(["git", "apply", "--check"] + [str(p) for p in patches], repo)
    run(["git", "apply"] + [str(p) for p in patches], repo)

    changed = sorted(p for p in git_status_paths(repo) if p in set(all_targets))
    if changed != all_targets:
        raise SystemExit(f"post-apply scope mismatch: expected {all_targets}, got {changed}")

    for py_file in [t for t in all_targets if t.endswith(".py")]:
        r = py_compile_no_cache(repo, py_file)
        if r.returncode != 0:
            raise SystemExit(r.stdout + r.stderr)

    if args.commit_message:
        rel_patch_dir = str(patch_dir.relative_to(repo)).replace("\\", "/")
        run(["git", "add"] + all_targets + [rel_patch_dir], repo, capture=False)
        run(["git", "commit", "-m", args.commit_message], repo, capture=False)
        if args.push:
            run(["git", "push", "origin", args.branch], repo, capture=False)

    print("FINAL_REPORT:")
    print("  changed_file_scope: PASS")
    print("  py_compile: PASS")
    print("  committed:", bool(args.commit_message))
    print("  pushed:", bool(args.push and args.commit_message))
    return 0


# ---------------------------------------------------------------- CLI

def build_parser() -> argparse.ArgumentParser:
    p = argparse.ArgumentParser(description=__doc__)
    sub = p.add_subparsers(dest="command", required=True)

    wa = sub.add_parser("worktree-add")
    wa.add_argument("--repo", required=True)
    wa.add_argument("--at", required=True)
    wa.add_argument("--ref", default="main")
    wa.set_defaults(func=cmd_worktree_add)

    wr = sub.add_parser("worktree-remove")
    wr.add_argument("--repo", required=True)
    wr.add_argument("--at", required=True)
    wr.set_defaults(func=cmd_worktree_remove)

    gp = sub.add_parser("gen-patch")
    gp.add_argument("--repo", required=True)
    gp.add_argument("--out", required=True)
    gp.add_argument("targets", nargs="+")
    gp.set_defaults(func=cmd_gen_patch)

    va = sub.add_parser("validate")
    va.add_argument("--repo", required=True)
    va.add_argument("--patches", required=True)
    va.add_argument("--py-compile", nargs="*", default=[])
    va.set_defaults(func=cmd_validate)

    rf = sub.add_parser("run-fixture")
    rf.add_argument("--spec", required=True)
    rf.set_defaults(func=cmd_run_fixture)

    fz = sub.add_parser("finalize")
    fz.add_argument("--repo", required=True)
    fz.add_argument("--patches", required=True)
    fz.add_argument("--branch", default="main")
    fz.add_argument("--commit-message")
    fz.add_argument("--push", action="store_true")
    fz.set_defaults(func=cmd_finalize)

    return p


def main(argv: Sequence[str] | None = None) -> int:
    args = build_parser().parse_args(argv)
    return args.func(args)


if __name__ == "__main__":
    raise SystemExit(main())
