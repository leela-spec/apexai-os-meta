#!/usr/bin/env python3
"""
download_selected_apex_claude_orchestration_repos.py

Download the selected Apex Claude orchestration repo set into the local Apex KB:

  C:\\GitDev\\apexai-os-meta\\apex-meta\\kb\\claude-orchestration-agents

This script is intentionally narrow. It only includes the repos from the locked
Apex Claude Repo Selection recommendation:

  first_batch_to_clone:
    - shanraisshan/claude-code-best-practice
    - bmad-code-org/BMAD-METHOD
    - amanaiproduct/personal-os
    - iannuttall/claude-agents

  first_batch_to_read_only:
    - hesreallyhim/awesome-claude-code
    - Aider-AI/aider
    - princeton-nlp/SWE-agent

Design principles:
  - Uses git for source verification and download.
  - Uses sparse checkout by default, following the prior Apex guidance.
  - Never runs any code from downloaded repos.
  - Writes a JSON manifest and a Markdown report.
  - Optionally strips nested .git folders after recording commit metadata so the
    downloaded sources can live safely inside the parent Apex repo as KB sources.

Examples from PowerShell:

  cd C:\\GitDev\\apexai-os-meta

  # Preview exact actions.
  python scripts\\download_selected_apex_claude_orchestration_repos.py --dry-run

  # Download selected repos into the KB folder, stripping nested .git folders.
  python scripts\\download_selected_apex_claude_orchestration_repos.py

  # Re-run and update existing live git clones. Only works if --keep-git was used.
  python scripts\\download_selected_apex_claude_orchestration_repos.py --update --keep-git

  # Force a fresh download by deleting existing target folders first.
  python scripts\\download_selected_apex_claude_orchestration_repos.py --force

No external Python packages are required. Git must be installed and available on PATH.
"""

from __future__ import annotations

import argparse
import dataclasses
import datetime as dt
import json
import os
import shutil
import stat
import subprocess
import sys
from pathlib import Path
from typing import Dict, Iterable, List, Optional, Sequence

DEFAULT_TARGET_ROOT = Path(r"C:\GitDev\apexai-os-meta\apex-meta\kb\claude-orchestration-agents")

FIRST_BATCH_TO_CLONE = "first_batch_to_clone"
FIRST_BATCH_TO_READ_ONLY = "first_batch_to_read_only"


@dataclasses.dataclass(frozen=True)
class RepoSpec:
    key: str
    owner: str
    repo: str
    decision_group: str
    decision: str
    priority: int
    why: str
    include_paths: Sequence[str]
    notes: str = ""

    @property
    def full_name(self) -> str:
        return f"{self.owner}/{self.repo}"

    @property
    def url(self) -> str:
        return f"https://github.com/{self.owner}/{self.repo}.git"

    @property
    def folder_name(self) -> str:
        return f"{self.owner}__{self.repo}"


REPOS: List[RepoSpec] = [
    RepoSpec(
        key="claude-code-best-practice",
        owner="shanraisshan",
        repo="claude-code-best-practice",
        decision_group=FIRST_BATCH_TO_CLONE,
        decision="must_clone_and_study",
        priority=1,
        why="Verified Claude Code .claude layout and command-agent-skill routing reference.",
        include_paths=(
            ".claude/",
            "CLAUDE.md",
            "README.md",
            "LICENSE",
            "best-practice/",
            "implementation/",
            "orchestration-workflow/",
        ),
        notes="Primary Claude-native layout source.",
    ),
    RepoSpec(
        key="BMAD-METHOD",
        owner="bmad-code-org",
        repo="BMAD-METHOD",
        decision_group=FIRST_BATCH_TO_CLONE,
        decision="must_clone_and_study",
        priority=1,
        why="Workflow/team/orchestrator grammar source; adapt surgically, do not blindly copy.",
        include_paths=(
            "README.md",
            "LICENSE",
            "AGENTS.md",
            "docs/",
            "src/",
            "tools/",
            "web-bundles/",
        ),
        notes="Old bmad-core path claims must be checked against the downloaded tree.",
    ),
    RepoSpec(
        key="personal-os",
        owner="amanaiproduct",
        repo="personal-os",
        decision_group=FIRST_BATCH_TO_CLONE,
        decision="clone_selectively",
        priority=2,
        why="Personal OS file grammar: GOALS.md, AGENTS.md, setup flow, templates, workspace.",
        include_paths=(
            "README.md",
            "LICENSE",
            "GOALS.md",
            "AGENTS.md",
            "setup.sh",
            "templates/",
            "workspace/",
        ),
        notes="Low-noise personal orchestration reference. Do not run setup.sh automatically.",
    ),
    RepoSpec(
        key="claude-agents",
        owner="iannuttall",
        repo="claude-agents",
        decision_group=FIRST_BATCH_TO_CLONE,
        decision="clone_selectively",
        priority=2,
        why="Small, low-noise Claude subagent template source.",
        include_paths=(
            "README.md",
            "LICENSE",
            "agents/",
        ),
        notes="Use as subagent formatting reference, not as a large permanent agent roster.",
    ),
    RepoSpec(
        key="awesome-claude-code",
        owner="hesreallyhim",
        repo="awesome-claude-code",
        decision_group=FIRST_BATCH_TO_READ_ONLY,
        decision="read_only_reference",
        priority=2,
        why="Discovery hub for Claude Code skills, hooks, commands, apps, plugins, and orchestrators.",
        include_paths=(
            "README.md",
            "LICENSE",
            "docs/",
        ),
        notes="Do not ingest linked repos from this index without separate verification.",
    ),
    RepoSpec(
        key="aider",
        owner="Aider-AI",
        repo="aider",
        decision_group=FIRST_BATCH_TO_READ_ONLY,
        decision="read_only_reference",
        priority=3,
        why="Repo-map and atomic Git workflow reference; not an Apex orchestration foundation.",
        include_paths=(
            "README.md",
            "LICENSE",
            "docs/",
            "aider/repomap.py",
        ),
        notes="Read for repo-map / git-state concepts only. Avoid full codebase ingestion.",
    ),
    RepoSpec(
        key="SWE-agent",
        owner="princeton-nlp",
        repo="SWE-agent",
        decision_group=FIRST_BATCH_TO_READ_ONLY,
        decision="read_only_reference",
        priority=3,
        why="Agent-computer-interface and issue-to-fix-to-validate reference.",
        include_paths=(
            "README.md",
            "LICENSE",
            "docs/",
        ),
        notes="Use conceptually. Original repo may be superseded by mini-SWE-agent for active development.",
    ),
]


@dataclasses.dataclass
class RepoResult:
    full_name: str
    decision_group: str
    decision: str
    priority: int
    url: str
    target_path: str
    status: str
    head: Optional[str] = None
    default_branch: Optional[str] = None
    sparse: bool = True
    git_dir_kept: bool = False
    file_count: Optional[int] = None
    bytes_total: Optional[int] = None
    include_paths: Sequence[str] = dataclasses.field(default_factory=list)
    missing_include_paths: Sequence[str] = dataclasses.field(default_factory=list)
    error: Optional[str] = None
    notes: str = ""


class CommandError(RuntimeError):
    pass


def utc_now() -> str:
    return dt.datetime.now(dt.timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def timestamp() -> str:
    return dt.datetime.now(dt.timezone.utc).strftime("%Y%m%d_%H%M%S")


def run_cmd(
    cmd: Sequence[str],
    cwd: Optional[Path] = None,
    check: bool = True,
    capture: bool = True,
) -> subprocess.CompletedProcess[str]:
    kwargs = {
        "cwd": str(cwd) if cwd else None,
        "text": True,
        "encoding": "utf-8",
        "errors": "replace",
    }
    if capture:
        kwargs.update({"stdout": subprocess.PIPE, "stderr": subprocess.PIPE})
    proc = subprocess.run(list(cmd), **kwargs)  # noqa: S603 - intended local git invocation
    if check and proc.returncode != 0:
        stderr = (proc.stderr or "").strip()
        stdout = (proc.stdout or "").strip()
        raise CommandError(f"command failed ({proc.returncode}): {' '.join(cmd)}\nSTDOUT:\n{stdout}\nSTDERR:\n{stderr}")
    return proc


def require_git() -> str:
    try:
        proc = run_cmd(["git", "--version"])
    except FileNotFoundError as exc:
        raise CommandError("git was not found on PATH. Install Git for Windows and re-run.") from exc
    return (proc.stdout or "").strip()


def find_parent_repo_root(target_root: Path) -> Optional[Path]:
    current = target_root.resolve()
    for candidate in [current, *current.parents]:
        if (candidate / ".git").exists():
            return candidate
    return None


def ensure_target_layout(target_root: Path) -> Dict[str, Path]:
    paths = {
        "raw_repos": target_root / "raw" / "repos",
        FIRST_BATCH_TO_CLONE: target_root / "raw" / "repos" / "first-batch-to-clone",
        FIRST_BATCH_TO_READ_ONLY: target_root / "raw" / "repos" / "first-batch-to-read-only",
        "manifests": target_root / "manifests" / "repo-downloads",
        "log": target_root / "log",
    }
    for path in paths.values():
        path.mkdir(parents=True, exist_ok=True)
    return paths


def repo_dest(paths: Dict[str, Path], spec: RepoSpec) -> Path:
    if spec.decision_group == FIRST_BATCH_TO_CLONE:
        return paths[FIRST_BATCH_TO_CLONE] / spec.folder_name
    return paths[FIRST_BATCH_TO_READ_ONLY] / spec.folder_name


def has_git_dir(path: Path) -> bool:
    return (path / ".git").exists() or (path / ".git").is_file()


def remove_git_metadata(path: Path) -> None:
    git_path = path / ".git"
    if git_path.is_dir():
        shutil.rmtree(git_path, onerror=handle_remove_readonly)
    elif git_path.exists():
        git_path.chmod(stat.S_IWRITE)
        git_path.unlink()


def handle_remove_readonly(func, path, _exc_info) -> None:
    os.chmod(path, stat.S_IWRITE)
    func(path)


def verify_remote_exists(spec: RepoSpec) -> str:
    proc = run_cmd(["git", "ls-remote", "--heads", spec.url], check=True)
    return (proc.stdout or "").strip()


def clone_sparse(spec: RepoSpec, dest: Path, depth: int, no_sparse: bool, log_lines: List[str]) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if no_sparse:
        cmd = ["git", "clone", "--depth", str(depth), spec.url, str(dest)] if depth else ["git", "clone", spec.url, str(dest)]
        log_lines.append("$ " + " ".join(cmd))
        run_cmd(cmd, capture=True)
        return

    clone_cmd = ["git", "clone", "--filter=blob:none", "--no-checkout"]
    if depth:
        clone_cmd.extend(["--depth", str(depth)])
    clone_cmd.extend([spec.url, str(dest)])
    log_lines.append("$ " + " ".join(clone_cmd))
    run_cmd(clone_cmd, capture=True)

    # Use no-cone mode so individual root files and selected files such as
    # aider/repomap.py can be included precisely.
    try:
        run_cmd(["git", "sparse-checkout", "init", "--no-cone"], cwd=dest)
        run_cmd(["git", "sparse-checkout", "set", "--no-cone", *spec.include_paths], cwd=dest)
        run_cmd(["git", "checkout"], cwd=dest)
    except CommandError as exc:
        # Fallback for older Git versions. Full checkout is safer than leaving an
        # empty repo, but the report will mark sparse=false.
        log_lines.append(f"sparse checkout failed for {spec.full_name}: {exc}")
        run_cmd(["git", "sparse-checkout", "disable"], cwd=dest, check=False)
        run_cmd(["git", "checkout"], cwd=dest)


def git_head(path: Path) -> Optional[str]:
    if not has_git_dir(path):
        meta = path / "repo-source-meta.json"
        if meta.exists():
            try:
                return json.loads(meta.read_text(encoding="utf-8")).get("head")
            except Exception:
                return None
        return None
    return (run_cmd(["git", "rev-parse", "HEAD"], cwd=path).stdout or "").strip() or None


def git_default_branch(path: Path) -> Optional[str]:
    if not has_git_dir(path):
        meta = path / "repo-source-meta.json"
        if meta.exists():
            try:
                return json.loads(meta.read_text(encoding="utf-8")).get("default_branch")
            except Exception:
                return None
        return None
    proc = run_cmd(["git", "rev-parse", "--abbrev-ref", "HEAD"], cwd=path, check=False)
    branch = (proc.stdout or "").strip()
    return branch or None


def update_repo(path: Path, log_lines: List[str]) -> None:
    if not has_git_dir(path):
        raise CommandError(f"cannot update {path}; nested .git was stripped. Re-run with --force or use --keep-git next time.")
    run_cmd(["git", "fetch", "--depth", "1", "origin"], cwd=path)
    branch = git_default_branch(path) or "HEAD"
    if branch == "HEAD":
        run_cmd(["git", "pull", "--ff-only"], cwd=path, check=False)
    else:
        run_cmd(["git", "pull", "--ff-only", "origin", branch], cwd=path)
    log_lines.append(f"updated {path}")


def count_files_and_bytes(path: Path) -> tuple[int, int]:
    count = 0
    total = 0
    for p in path.rglob("*"):
        # Do not count nested git internals as source content.
        if ".git" in p.parts:
            continue
        if p.is_file():
            count += 1
            try:
                total += p.stat().st_size
            except OSError:
                pass
    return count, total


def missing_includes(path: Path, include_paths: Sequence[str]) -> List[str]:
    missing: List[str] = []
    for rel in include_paths:
        # Git sparse patterns may include directories with trailing slash.
        clean = rel.rstrip("/")
        if not clean:
            continue
        if not (path / clean).exists():
            missing.append(rel)
    return missing


def write_repo_metadata(path: Path, spec: RepoSpec, head: Optional[str], default_branch: Optional[str], stripped_git: bool) -> None:
    payload = {
        "source_type": "github_repo",
        "downloaded_at": utc_now(),
        "repo": spec.full_name,
        "url": spec.url,
        "decision_group": spec.decision_group,
        "decision": spec.decision,
        "priority": spec.priority,
        "why": spec.why,
        "include_paths": list(spec.include_paths),
        "notes": spec.notes,
        "head": head,
        "default_branch": default_branch,
        "git_metadata_stripped": stripped_git,
        "warning": "Do not run scripts from this downloaded repo without separate review.",
    }
    (path / "repo-source-meta.json").write_text(json.dumps(payload, indent=2, ensure_ascii=False) + "\n", encoding="utf-8", newline="\n")


def process_repo(
    spec: RepoSpec,
    dest: Path,
    args: argparse.Namespace,
    log_lines: List[str],
) -> RepoResult:
    result = RepoResult(
        full_name=spec.full_name,
        decision_group=spec.decision_group,
        decision=spec.decision,
        priority=spec.priority,
        url=spec.url,
        target_path=str(dest),
        status="pending",
        sparse=not args.no_sparse,
        git_dir_kept=args.keep_git,
        include_paths=list(spec.include_paths),
        notes=spec.notes,
    )

    try:
        verify_remote_exists(spec)
        if args.dry_run:
            result.status = "dry_run"
            return result

        if dest.exists():
            if args.force:
                shutil.rmtree(dest, onerror=handle_remove_readonly)
            elif args.update:
                update_repo(dest, log_lines)
                result.status = "updated"
                result.head = git_head(dest)
                result.default_branch = git_default_branch(dest)
                result.missing_include_paths = missing_includes(dest, spec.include_paths)
                result.file_count, result.bytes_total = count_files_and_bytes(dest)
                return result
            else:
                result.status = "skipped_existing"
                result.head = git_head(dest)
                result.default_branch = git_default_branch(dest)
                result.missing_include_paths = missing_includes(dest, spec.include_paths)
                result.file_count, result.bytes_total = count_files_and_bytes(dest)
                return result

        clone_sparse(spec, dest, args.depth, args.no_sparse, log_lines)
        head = git_head(dest)
        branch = git_default_branch(dest)
        sparse_actual = not args.no_sparse and bool((dest / ".git" / "info" / "sparse-checkout").exists())
        missing = missing_includes(dest, spec.include_paths)

        stripped = False
        if not args.keep_git:
            remove_git_metadata(dest)
            stripped = True

        write_repo_metadata(dest, spec, head, branch, stripped)
        count, total = count_files_and_bytes(dest)
        result.status = "downloaded"
        result.head = head
        result.default_branch = branch
        result.sparse = sparse_actual
        result.git_dir_kept = not stripped
        result.file_count = count
        result.bytes_total = total
        result.missing_include_paths = missing
        return result
    except Exception as exc:  # noqa: BLE001 - report all per-repo failures and continue
        result.status = "failed"
        result.error = f"{type(exc).__name__}: {exc}"
        return result


def render_report(results: Sequence[RepoResult], target_root: Path, parent_repo_root: Optional[Path], git_version: str, parent_status: str, args: argparse.Namespace) -> str:
    counts: Dict[str, int] = {}
    for r in results:
        counts[r.status] = counts.get(r.status, 0) + 1
    lines = [
        "# Apex Claude Orchestration Repo Download Report",
        "",
        f"Generated: `{utc_now()}`",
        "",
        "## Scope",
        "",
        "Only the locked first-batch repos were included:",
        "",
        "```yaml",
        "first_batch_to_clone:",
        '  - "shanraisshan/claude-code-best-practice"',
        '  - "bmad-code-org/BMAD-METHOD"',
        '  - "amanaiproduct/personal-os"',
        '  - "iannuttall/claude-agents"',
        "",
        "first_batch_to_read_only:",
        '  - "hesreallyhim/awesome-claude-code"',
        '  - "Aider-AI/aider"',
        '  - "princeton-nlp/SWE-agent"',
        "```",
        "",
        "## Run Configuration",
        "",
        "```yaml",
        f"target_root: {str(target_root)!r}",
        f"parent_repo_root: {str(parent_repo_root) if parent_repo_root else 'not_found'!r}",
        f"git_version: {git_version!r}",
        f"dry_run: {bool(args.dry_run)}",
        f"force: {bool(args.force)}",
        f"update: {bool(args.update)}",
        f"sparse_checkout: {not bool(args.no_sparse)}",
        f"keep_nested_git_dirs: {bool(args.keep_git)}",
        f"depth: {args.depth}",
        "```",
        "",
        "## Parent Git Status Before Download",
        "",
        "```text",
        parent_status.strip() or "clean_or_not_available",
        "```",
        "",
        "## Status Counts",
        "",
        "| Status | Count |",
        "|---|---:|",
    ]
    for status, count in sorted(counts.items()):
        lines.append(f"| {status} | {count} |")
    lines.extend([
        "",
        "## Downloaded Tree",
        "",
        "```text",
        "apex-meta/kb/claude-orchestration-agents/",
        "  raw/",
        "    repos/",
        "      first-batch-to-clone/",
    ])
    for r in results:
        if r.decision_group == FIRST_BATCH_TO_CLONE:
            lines.append(f"        {Path(r.target_path).name}/")
    lines.extend([
        "      first-batch-to-read-only/",
    ])
    for r in results:
        if r.decision_group == FIRST_BATCH_TO_READ_ONLY:
            lines.append(f"        {Path(r.target_path).name}/")
    lines.extend([
        "  manifests/",
        "    repo-downloads/",
        "  log/",
        "```",
        "",
        "## Repo Results",
        "",
        "| Repo | Group | Decision | Status | Files | Bytes | Head | Missing requested paths | Target | Error |",
        "|---|---|---|---|---:|---:|---|---|---|---|",
    ])
    for r in results:
        missing = ", ".join(r.missing_include_paths or [])
        head = (r.head or "")[:12]
        err = (r.error or "").replace("\n", " ")[:180]
        lines.append(
            f"| `{r.full_name}` | `{r.decision_group}` | `{r.decision}` | `{r.status}` | "
            f"{r.file_count if r.file_count is not None else ''} | {r.bytes_total if r.bytes_total is not None else ''} | "
            f"`{head}` | `{missing}` | `{r.target_path}` | {err} |"
        )
    lines.extend([
        "",
        "## Safety Notes",
        "",
        "- The script does not run any scripts from downloaded repositories.",
        "- By default it strips nested `.git` folders after recording source metadata, avoiding accidental nested-repo/submodule behavior inside `apexai-os-meta`.",
        "- Use `--keep-git` only when you explicitly want live nested clones for later `--update` runs.",
        "- Any missing requested sparse paths are reported; they usually mean the upstream repo tree changed or the prior path claim was stale.",
        "",
    ])
    return "\n".join(lines)


def parent_git_status(parent_repo_root: Optional[Path]) -> str:
    if not parent_repo_root:
        return "parent git repo not found"
    proc = run_cmd(["git", "status", "--short"], cwd=parent_repo_root, check=False)
    return (proc.stdout or proc.stderr or "").strip()


def write_text(path: Path, text: str) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(text, encoding="utf-8", newline="\n")


def run(args: argparse.Namespace) -> int:
    git_version = require_git()
    target_root = Path(args.target_root).expanduser().resolve()
    paths = ensure_target_layout(target_root)
    parent_root = find_parent_repo_root(target_root)
    p_status = parent_git_status(parent_root)

    if args.strict_clean and p_status.strip():
        print("Parent repo has dirty/untracked files. Re-run without --strict-clean to continue.", file=sys.stderr)
        print(p_status, file=sys.stderr)
        return 2

    selected = [r for r in REPOS if args.only_group in {"all", r.decision_group}]
    log_lines = [f"started: {utc_now()}", f"git_version: {git_version}", f"target_root: {target_root}"]
    results: List[RepoResult] = []
    for spec in selected:
        dest = repo_dest(paths, spec)
        print(f"[{spec.decision_group}] {spec.full_name} -> {dest}")
        result = process_repo(spec, dest, args, log_lines)
        results.append(result)
        print(f"  {result.status}" + (f" ({result.error})" if result.error else ""))

    stamp = timestamp()
    manifest_path = paths["manifests"] / f"selected-repo-download-manifest_{stamp}.json"
    report_path = paths["manifests"] / f"selected-repo-download-report_{stamp}.md"
    log_path = paths["log"] / f"selected-repo-download_{stamp}.log"

    payload = {
        "generated_at": utc_now(),
        "target_root": str(target_root),
        "parent_repo_root": str(parent_root) if parent_root else None,
        "git_version": git_version,
        "settings": {
            "dry_run": args.dry_run,
            "force": args.force,
            "update": args.update,
            "sparse_checkout": not args.no_sparse,
            "keep_git": args.keep_git,
            "depth": args.depth,
            "only_group": args.only_group,
        },
        "results": [dataclasses.asdict(r) for r in results],
    }
    write_text(manifest_path, json.dumps(payload, indent=2, ensure_ascii=False) + "\n")
    write_text(report_path, render_report(results, target_root, parent_root, git_version, p_status, args))
    write_text(log_path, "\n".join(log_lines) + "\n")

    print(f"manifest: {manifest_path}")
    print(f"report:   {report_path}")
    print(f"log:      {log_path}")

    failed = [r for r in results if r.status == "failed"]
    return 1 if failed and args.fail_on_error else 0


def parse_args(argv: Optional[Sequence[str]] = None) -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Download selected Apex Claude orchestration GitHub repos into the claude-orchestration-agents KB.")
    parser.add_argument("--target-root", default=str(DEFAULT_TARGET_ROOT), help="Target KB root. Default: C:\\GitDev\\apexai-os-meta\\apex-meta\\kb\\claude-orchestration-agents")
    parser.add_argument("--dry-run", action="store_true", help="Verify remotes and write reports without cloning.")
    parser.add_argument("--force", action="store_true", help="Delete and re-download existing target repo folders.")
    parser.add_argument("--update", action="store_true", help="Update existing cloned repos. Requires nested .git dirs to exist; use with --keep-git.")
    parser.add_argument("--keep-git", action="store_true", help="Keep nested .git folders. Default strips them after recording source metadata.")
    parser.add_argument("--no-sparse", action="store_true", help="Clone full repos instead of sparse selected paths.")
    parser.add_argument("--depth", type=int, default=1, help="Git clone depth. Use 0 for full history. Default: 1.")
    parser.add_argument("--only-group", choices=["all", FIRST_BATCH_TO_CLONE, FIRST_BATCH_TO_READ_ONLY], default="all", help="Download only one decision group.")
    parser.add_argument("--strict-clean", action="store_true", help="Stop if parent Apex repo has any dirty/untracked files before download.")
    parser.add_argument("--fail-on-error", action="store_true", help="Return non-zero if any repo fails.")
    return parser.parse_args(argv)


def main(argv: Optional[Sequence[str]] = None) -> int:
    return run(parse_args(argv))


if __name__ == "__main__":
    raise SystemExit(main())
