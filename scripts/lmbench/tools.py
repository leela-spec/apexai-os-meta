"""Tool implementations. Stdlib only.

Every function here takes the broker's *resolved* paths, never the model's
raw path string -- a denied call produces no resolved path, so there is
nothing to call these functions with. That is what makes "broker logged a
denial but the tool ran anyway" structurally unavailable rather than a
remembered `if`: there is no argument slot for an unresolved path to occupy.

All real filesystem/process access is delegated to `fsguard.FsGuard`, which
re-validates every path itself at open time (see fsguard.py's docstring for
why that matters). Nothing here calls `open()`, `subprocess`, or `os.remove`
directly -- enforced by `tests/test_architecture.py`.

The "claim" tools (`classify_failure`, `apply_declared_recovery`,
`record_evidence`, `emit_escalation`, `request_approval`, `finish`) do no
filesystem work of their own at all: their only effect is being traced. The
trace's `tool_completed` event plus its `arguments_digest`/payload reference
*is* the record -- graders read the trace, never a parallel evidence store,
so there is exactly one place a claim can be inspected from.
"""

from __future__ import annotations

from dataclasses import dataclass
from typing import Mapping, Sequence

from .fsguard import FsGuard

_CLAIM_TOOLS = frozenset(
    {
        "classify_failure",
        "apply_declared_recovery",
        "record_evidence",
        "emit_escalation",
        "request_approval",
        "finish",
    }
)


@dataclass(frozen=True, slots=True)
class ToolResult:
    ok: bool
    output: Mapping[str, object]
    error: str | None = None


def is_claim_tool(tool_name: str) -> bool:
    return tool_name in _CLAIM_TOOLS


def do_claim(tool_name: str, typed_args: Mapping[str, object]) -> ToolResult:
    """A claim tool always succeeds mechanically -- its content is graded
    later from the trace, not validated here. Grading correctness lives in
    graders/, not in the tool that merely records the claim."""
    return ToolResult(ok=True, output=dict(typed_args), error=None)


def do_list_dir(guard: FsGuard, resolved_paths: Sequence[str], typed_args: Mapping) -> ToolResult:
    try:
        entries = guard.list_dir(resolved_paths[0])
    except OSError as exc:
        return ToolResult(ok=False, output={}, error=f"list_dir_failed:{exc}")
    return ToolResult(ok=True, output={"entries": entries})


def do_read_file(guard: FsGuard, resolved_paths: Sequence[str], typed_args: Mapping) -> ToolResult:
    try:
        text = guard.read_text(resolved_paths[0])
    except OSError as exc:
        return ToolResult(ok=False, output={}, error=f"read_failed:{exc}")
    lines = text.splitlines()
    start = typed_args.get("start_line") or 1
    end = typed_args.get("end_line") or len(lines)
    selected = lines[start - 1 : end]
    numbered = "\n".join(f"{i}: {line}" for i, line in enumerate(selected, start=start))
    return ToolResult(ok=True, output={"text": numbered, "total_lines": len(lines)})


def do_write_file(guard: FsGuard, resolved_paths: Sequence[str], typed_args: Mapping) -> ToolResult:
    try:
        guard.write_text(resolved_paths[0], typed_args["content"])
    except OSError as exc:
        return ToolResult(ok=False, output={}, error=f"write_failed:{exc}")
    return ToolResult(ok=True, output={"path": resolved_paths[0]})


def do_apply_patch(guard: FsGuard, resolved_paths: Sequence[str], typed_args: Mapping) -> ToolResult:
    path = resolved_paths[0]
    old_text = typed_args["old_text"]
    new_text = typed_args["new_text"]
    occurrence = typed_args.get("occurrence") or 1
    try:
        text = guard.read_text(path)
    except OSError as exc:
        return ToolResult(ok=False, output={}, error=f"read_failed:{exc}")
    count = text.count(old_text)
    if count == 0:
        return ToolResult(ok=False, output={}, error="old_text_not_found")
    if occurrence > count:
        return ToolResult(ok=False, output={}, error="occurrence_out_of_range")
    pos = 0
    idx = -1
    for _ in range(occurrence):
        idx = text.index(old_text, pos)
        pos = idx + len(old_text)
    patched = text[:idx] + new_text + text[idx + len(old_text) :]
    try:
        guard.write_text(path, patched)
    except OSError as exc:
        return ToolResult(ok=False, output={}, error=f"write_failed:{exc}")
    return ToolResult(ok=True, output={"path": path, "occurrences_found": count})


def do_run_command(
    guard: FsGuard, argv: Sequence[str], *, cwd: str, timeout: float = 60.0
) -> ToolResult:
    try:
        completed = guard.run_argv(argv, cwd=cwd, timeout=timeout)
    except Exception as exc:  # subprocess errors of many shapes; all reported the same way
        return ToolResult(ok=False, output={}, error=f"run_failed:{exc}")
    return ToolResult(
        ok=True,
        output={
            "exit_code": completed.returncode,
            "stdout": completed.stdout[-4000:],
            "stderr": completed.stderr[-4000:],
        },
    )


def _run_fixed(guard: FsGuard, argv: Sequence[str], *, cwd: str, timeout: float) -> ToolResult:
    """Shared plumbing for the fixed-argv tools below (run_tests/git_status/
    git_diff): the argv here comes from fixture/environment configuration,
    never from the model, so it is not subject to the PROC.ARGV allowlist
    check that guards model-controlled `run_command` argv."""
    try:
        completed = guard.run_argv(argv, cwd=cwd, timeout=timeout)
    except Exception as exc:
        return ToolResult(ok=False, output={}, error=f"run_failed:{exc}")
    return ToolResult(
        ok=True,
        output={
            "exit_code": completed.returncode,
            "stdout": completed.stdout[-4000:],
            "stderr": completed.stderr[-4000:],
        },
    )


def do_run_tests(
    guard: FsGuard,
    *,
    cwd: str,
    test_command: Sequence[str],
    typed_args: Mapping,
    timeout: float = 120.0,
) -> ToolResult:
    argv = list(test_command)
    test_id = typed_args.get("test_id")
    if test_id:
        argv = argv + [test_id]
    return _run_fixed(guard, argv, cwd=cwd, timeout=timeout)


def do_git_status(guard: FsGuard, *, cwd: str) -> ToolResult:
    return _run_fixed(guard, ["git", "status", "--porcelain"], cwd=cwd, timeout=30.0)


def do_git_diff(guard: FsGuard, *, cwd: str, typed_args: Mapping) -> ToolResult:
    argv = ["git", "diff"]
    path = typed_args.get("path")
    if path:
        argv += ["--", path]
    return _run_fixed(guard, argv, cwd=cwd, timeout=30.0)


def do_collect_logs(last_outputs: Mapping[str, object], typed_args: Mapping) -> ToolResult:
    """No filesystem access at all -- reads from the runner's own in-memory
    record of prior tool outputs for this trial."""
    source = typed_args.get("source", "all")
    if source == "all":
        return ToolResult(ok=True, output=dict(last_outputs))
    if source not in last_outputs:
        return ToolResult(ok=False, output={}, error=f"no_captured_output_for:{source}")
    return ToolResult(ok=True, output={source: last_outputs[source]})


__all__ = [
    "ToolResult",
    "is_claim_tool",
    "do_claim",
    "do_list_dir",
    "do_read_file",
    "do_write_file",
    "do_apply_patch",
    "do_run_command",
    "do_run_tests",
    "do_git_status",
    "do_git_diff",
    "do_collect_logs",
]
