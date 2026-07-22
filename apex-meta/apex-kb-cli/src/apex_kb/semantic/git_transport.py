from __future__ import annotations

import subprocess
from pathlib import Path
from typing import Any

from ..errors import ApexKBError


_GIT_TIMEOUT_SECONDS = 120


def _git(root: Path, *args: str, check: bool = True) -> subprocess.CompletedProcess[str]:
    try:
        result = subprocess.run(
            ["git", "-C", str(root), *args],
            check=False,
            text=True,
            capture_output=True,
            timeout=_GIT_TIMEOUT_SECONDS,
        )
    except (OSError, subprocess.SubprocessError) as exc:
        raise ApexKBError(
            "destination_git_unavailable",
            f"Git could not execute in the destination repository: {root}",
            {"command": ["git", "-C", str(root), *args], "error": str(exc)},
        ) from exc
    if check and result.returncode != 0:
        raise ApexKBError(
            "destination_git_command_failed",
            f"Git command failed in the destination repository: {' '.join(args)}",
            {
                "command": ["git", "-C", str(root), *args],
                "exit_code": result.returncode,
                "stdout": result.stdout.strip(),
                "stderr": result.stderr.strip(),
            },
        )
    return result


def repository_relative(path: Path, repository_root: Path) -> str:
    try:
        return path.resolve().relative_to(repository_root.resolve()).as_posix()
    except ValueError as exc:
        raise ApexKBError(
            "destination_path_outside_repository",
            f"Path is outside the configured destination repository: {path}",
            {"repository_root": str(repository_root)},
        ) from exc


def current_head(repository_root: Path) -> str:
    return _git(repository_root, "rev-parse", "HEAD").stdout.strip()


def _current_branch(repository_root: Path) -> str:
    return _git(repository_root, "branch", "--show-current").stdout.strip()


def _fetch_main(repository_root: Path) -> None:
    _git(repository_root, "fetch", "origin", "main")


def _origin_main(repository_root: Path) -> str:
    return _git(repository_root, "rev-parse", "origin/main").stdout.strip()


def _is_ancestor(repository_root: Path, ancestor: str, descendant: str) -> bool:
    result = _git(repository_root, "merge-base", "--is-ancestor", ancestor, descendant, check=False)
    return result.returncode == 0


def _require_main(repository_root: Path) -> None:
    branch = _current_branch(repository_root)
    if branch != "main":
        raise ApexKBError(
            "destination_branch_not_main",
            "Generated KB artifacts must be published from the destination repository main branch.",
            {"actual_branch": branch or None, "expected_branch": "main"},
        )


def publish_run_artifacts(
    repository_root: Path,
    run_root: Path,
    commit_message: str,
) -> str:
    """Commit the deterministic run tree and push it directly to origin/main."""
    repository_root = repository_root.resolve()
    run_root = run_root.resolve()
    _require_main(repository_root)
    _fetch_main(repository_root)
    local_head = current_head(repository_root)
    remote_head = _origin_main(repository_root)
    if local_head != remote_head:
        raise ApexKBError(
            "destination_main_not_current",
            "Destination main must be fast-forward current before deterministic artifacts are published.",
            {
                "local_head": local_head,
                "origin_main": remote_head,
                "required_action": f'git -C "{repository_root}" pull --ff-only origin main',
            },
        )

    run_path = repository_relative(run_root, repository_root)
    status = _git(repository_root, "status", "--porcelain", "--", run_path).stdout.strip()
    if status:
        _git(repository_root, "add", "--", run_path)
        _git(repository_root, "commit", "--only", "-m", commit_message, "--", run_path)

    base_commit = current_head(repository_root)
    _git(repository_root, "push", "origin", "HEAD:main")
    _fetch_main(repository_root)
    pushed_head = _origin_main(repository_root)
    if pushed_head != base_commit:
        raise ApexKBError(
            "deterministic_publication_mismatch",
            "The pushed destination main commit does not equal the deterministic publication commit.",
            {"local_commit": base_commit, "origin_main": pushed_head},
        )
    return base_commit


def local_prompt_path(repository_root: Path, run_id: str, task_id: str) -> Path:
    git_dir_raw = _git(repository_root, "rev-parse", "--git-dir").stdout.strip()
    git_dir = Path(git_dir_raw)
    if not git_dir.is_absolute():
        git_dir = repository_root / git_dir
    path = git_dir.resolve() / "apex-kb" / "prompts" / run_id / f"{task_id}.md"
    path.parent.mkdir(parents=True, exist_ok=True)
    return path


def reconcile_direct_main(
    repository_root: Path,
    base_commit: str,
    expected_changed_paths: list[str],
) -> dict[str, Any]:
    """Fast-forward local main and prove the browser semantic commit contract."""
    repository_root = repository_root.resolve()
    _require_main(repository_root)
    _fetch_main(repository_root)
    remote_head = _origin_main(repository_root)
    local_head = current_head(repository_root)

    if local_head == base_commit:
        if remote_head == base_commit:
            raise ApexKBError(
                "semantic_result_pending",
                "Destination main has not advanced beyond the Phase 2A base commit.",
                {"base_commit": base_commit},
            )
        _git(repository_root, "pull", "--ff-only", "origin", "main")
        local_head = current_head(repository_root)
    elif local_head == remote_head and _is_ancestor(repository_root, base_commit, local_head):
        # Supports a local test or an operator checkout that already contains the landed browser commit.
        pass
    else:
        raise ApexKBError(
            "destination_local_head_moved",
            "Local destination main is not at the recorded base commit and cannot be reconciled as the landed semantic result.",
            {"base_commit": base_commit, "local_head": local_head, "origin_main": remote_head},
        )

    result_commit = current_head(repository_root)
    if result_commit == base_commit:
        raise ApexKBError(
            "semantic_result_pending",
            "Destination main has not advanced beyond the Phase 2A base commit.",
            {"base_commit": base_commit},
        )
    if not _is_ancestor(repository_root, base_commit, result_commit):
        raise ApexKBError(
            "main_moved",
            "Destination main is not a descendant of the Phase 2A base commit.",
            {"base_commit": base_commit, "result_commit": result_commit},
        )

    changed = sorted(
        line.strip()
        for line in _git(repository_root, "diff", "--name-only", f"{base_commit}..{result_commit}").stdout.splitlines()
        if line.strip()
    )
    expected = sorted(dict.fromkeys(expected_changed_paths))
    if changed != expected:
        raise ApexKBError(
            "semantic_changed_paths_invalid",
            "The Phase 2A semantic commit did not change exactly the declared output paths.",
            {
                "base_commit": base_commit,
                "result_commit": result_commit,
                "expected_paths": expected,
                "actual_paths": changed,
                "missing": sorted(set(expected) - set(changed)),
                "unexpected": sorted(set(changed) - set(expected)),
            },
        )
    return {
        "base_commit": base_commit,
        "result_commit": result_commit,
        "changed_paths": changed,
    }
