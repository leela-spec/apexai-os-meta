"""Mechanical Git/state helper for the Transcript-to-Knowledge V3 OpenClaw relay.

This helper deliberately has no Git commit, rebase, reset, or push operation.
Antigravity owns module result commits; ChatGPT owns review-gate authority commits.
"""

from __future__ import annotations

import argparse
import json
import os
import re
import subprocess
import sys
from dataclasses import dataclass
from pathlib import Path
from typing import Any, Sequence


CURRENT_WORK = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/CURRENT-WORK.md"
)
M00_RESULT = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/results/M00-RESULT.md"
)
M00_SEED = Path(
    "SourceTranscriptionAnalysisPipeline_Research/v3-proven-infrastructure/results/M00-PROVEN-SYSTEMS-SEED.md"
)
STATE_SCHEMA = "ttk.relay-state/v1"
CURRENT_WORK_SCHEMA = "ttk.current-work/v1"
STATE_PATTERN = re.compile(r"<!-- ttk-relay-state\s*\n(.*?)\n-->", re.DOTALL)
FULL_SHA_PATTERN = re.compile(r"^[0-9a-f]{40}$")


class RelayError(RuntimeError):
    def __init__(self, code: str, message: str):
        super().__init__(message)
        self.code = code


@dataclass(frozen=True)
class Context:
    repo: Path
    state_path: Path
    expected_remote: str | None


def emit(payload: dict[str, Any], *, stream: Any = sys.stdout) -> None:
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), file=stream, flush=True)


def run_git(
    repo: Path,
    *args: str,
    check: bool = True,
) -> subprocess.CompletedProcess[str]:
    environment = os.environ.copy()
    for name in list(environment):
        if name.upper().startswith("GIT_"):
            environment.pop(name, None)
    command = [
        "git",
        "--no-optional-locks",
        "-c",
        "core.hooksPath=NUL" if os.name == "nt" else "core.hooksPath=/dev/null",
        "-c",
        "core.fsmonitor=false",
        "-c",
        "protocol.allow=never",
        "-c",
        "protocol.file.allow=always",
        "-c",
        "protocol.https.allow=always",
        "-C",
        str(repo),
        *args,
    ]
    result = subprocess.run(command, text=True, capture_output=True, check=False, env=environment)
    if check and result.returncode != 0:
        detail = (result.stderr or result.stdout).strip()
        raise RelayError("GIT_FAILED", f"git {' '.join(args)} failed: {detail}")
    return result


def assert_repo(ctx: Context) -> None:
    if not ctx.repo.is_dir():
        raise RelayError("REPO_MISSING", f"Repository does not exist: {ctx.repo}")
    top = run_git(ctx.repo, "rev-parse", "--show-toplevel").stdout.strip()
    if Path(top).resolve() != ctx.repo:
        raise RelayError("REPO_ROOT_MISMATCH", f"Expected exact repository root: {ctx.repo}")
    branch = run_git(ctx.repo, "branch", "--show-current").stdout.strip()
    if branch != "main":
        raise RelayError("BRANCH_NOT_MAIN", f"Current branch is {branch!r}, not 'main'")
    remotes = [line for line in run_git(ctx.repo, "remote", "get-url", "--all", "origin").stdout.splitlines() if line]
    push_remotes = [
        line for line in run_git(ctx.repo, "remote", "get-url", "--push", "--all", "origin").stdout.splitlines() if line
    ]
    if len(remotes) != 1 or len(push_remotes) != 1 or remotes[0] != push_remotes[0]:
        raise RelayError("REMOTE_INVALID", "origin must have one identical fetch and push URL")
    if ctx.expected_remote is not None and remotes[0] != ctx.expected_remote:
        raise RelayError("REMOTE_MISMATCH", f"origin is {remotes[0]!r}, expected {ctx.expected_remote!r}")


def assert_clean(ctx: Context) -> None:
    dirty = run_git(ctx.repo, "status", "--porcelain=v1", "--untracked-files=all").stdout
    if dirty:
        paths = [line[3:] for line in dirty.splitlines()[:10]]
        raise RelayError("DIRTY_WORKTREE", f"Working tree is dirty: {paths}")


def is_ancestor(ctx: Context, ancestor: str, descendant: str) -> bool:
    result = run_git(ctx.repo, "merge-base", "--is-ancestor", ancestor, descendant, check=False)
    if result.returncode not in (0, 1):
        raise RelayError("GIT_FAILED", result.stderr.strip() or "merge-base failed")
    return result.returncode == 0


def fetch_main(ctx: Context) -> str:
    run_git(ctx.repo, "fetch", "--no-tags", "origin", "refs/heads/main:refs/remotes/origin/main")
    return run_git(ctx.repo, "rev-parse", "refs/remotes/origin/main").stdout.strip()


def read_current_work_text(ctx: Context, *, revision: str | None = None) -> str:
    if revision is None:
        path = ctx.repo / CURRENT_WORK
        if not path.is_file():
            raise RelayError("CURRENT_WORK_MISSING", f"Missing {CURRENT_WORK.as_posix()}")
        return path.read_text(encoding="utf-8")
    result = run_git(ctx.repo, "show", f"{revision}:{CURRENT_WORK.as_posix()}", check=False)
    if result.returncode != 0:
        raise RelayError("CURRENT_WORK_MISSING", f"Missing {CURRENT_WORK.as_posix()} at {revision}")
    return result.stdout


def parse_current_work(text: str) -> dict[str, Any]:
    match = STATE_PATTERN.search(text)
    if match is None:
        raise RelayError("CURRENT_WORK_STATE_MISSING", "CURRENT-WORK lacks ttk-relay-state metadata")
    try:
        state = json.loads(match.group(1))
    except json.JSONDecodeError as exc:
        raise RelayError("CURRENT_WORK_STATE_INVALID", f"Invalid relay-state JSON: {exc}") from exc
    if not isinstance(state, dict) or state.get("schema_version") != CURRENT_WORK_SCHEMA:
        raise RelayError("CURRENT_WORK_STATE_INVALID", "Unsupported current-work state schema")
    required = {"status", "active_module", "on_pass", "review_gate", "stop_marker"}
    if not required.issubset(state):
        raise RelayError("CURRENT_WORK_STATE_INVALID", "Current-work state is missing required fields")
    active_module = state.get("active_module")
    if active_module is not None:
        module_path = Path(str(active_module))
        if module_path.is_absolute() or ".." in module_path.parts or module_path.parts[:1] != ("execution-modules",):
            raise RelayError("CURRENT_WORK_STATE_INVALID", "active_module is outside execution-modules")
    return state


def save_state(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    temporary.write_text(json.dumps(payload, indent=2, sort_keys=True) + "\n", encoding="utf-8", newline="\n")
    os.replace(temporary, path)


def load_state(path: Path) -> dict[str, Any]:
    if not path.is_file():
        return {"schema_version": STATE_SCHEMA}
    try:
        state = json.loads(path.read_text(encoding="utf-8"))
    except json.JSONDecodeError as exc:
        raise RelayError("RELAY_STATE_INVALID", f"Invalid relay state: {exc}") from exc
    if not isinstance(state, dict) or state.get("schema_version") != STATE_SCHEMA:
        raise RelayError("RELAY_STATE_INVALID", "Unsupported relay-state schema")
    return state


def validate_sha(value: str, name: str) -> None:
    if FULL_SHA_PATTERN.fullmatch(value) is None:
        raise RelayError("SHA_INVALID", f"{name} must be a full lowercase Git SHA")


def command_sync(ctx: Context, _: argparse.Namespace) -> dict[str, Any]:
    assert_repo(ctx)
    assert_clean(ctx)
    local_head = run_git(ctx.repo, "rev-parse", "HEAD").stdout.strip()
    remote_head = fetch_main(ctx)
    if local_head == remote_head:
        disposition = "already_current"
    elif is_ancestor(ctx, local_head, remote_head):
        run_git(ctx.repo, "merge", "--ff-only", "refs/remotes/origin/main")
        disposition = "fast_forwarded"
    elif is_ancestor(ctx, remote_head, local_head):
        raise RelayError("LOCAL_AHEAD", "Local main contains commits not present on origin/main")
    else:
        raise RelayError("DIVERGED_MAIN", "Local main and origin/main have diverged")
    state = parse_current_work(read_current_work_text(ctx))
    active_module = state.get("active_module")
    if active_module is not None and not (ctx.repo / CURRENT_WORK.parent / active_module).is_file():
        raise RelayError("ACTIVE_MODULE_MISSING", f"Active module does not exist: {active_module}")
    return {"status": "synced", "disposition": disposition, "head": remote_head, "current_work": state}


def changed_paths(ctx: Context, start: str, end: str) -> set[str]:
    output = run_git(ctx.repo, "diff", "--name-only", "--no-renames", f"{start}..{end}", "--").stdout
    return {line.strip().replace("\\", "/") for line in output.splitlines() if line.strip()}


def command_verify_result(ctx: Context, args: argparse.Namespace) -> dict[str, Any]:
    assert_repo(ctx)
    assert_clean(ctx)
    validate_sha(args.before_sha, "before-sha")
    if args.module != "M00":
        raise RelayError("MODULE_UNSUPPORTED", "The live pilot verifier currently permits M00 only")
    local_head = run_git(ctx.repo, "rev-parse", "HEAD").stdout.strip()
    remote_head = fetch_main(ctx)
    if local_head != remote_head:
        raise RelayError("RESULT_NOT_ON_REMOTE", "Local HEAD is not the actual origin/main HEAD")
    if local_head == args.before_sha or not is_ancestor(ctx, args.before_sha, local_head):
        raise RelayError("RESULT_ANCESTRY_INVALID", "M00 result is not a descendant of the launch SHA")
    allowed = {CURRENT_WORK.as_posix(), M00_RESULT.as_posix(), M00_SEED.as_posix()}
    unexpected = sorted(changed_paths(ctx, args.before_sha, local_head) - allowed)
    if unexpected:
        raise RelayError("UNEXPECTED_RESULT_PATH", f"M00 committed unexpected paths: {unexpected}")
    missing = [path for path in (CURRENT_WORK, M00_RESULT, M00_SEED) if not (ctx.repo / path).is_file()]
    if missing:
        raise RelayError("RESULT_FILE_MISSING", f"M00 result files are missing: {[p.as_posix() for p in missing]}")
    result_text = (ctx.repo / M00_RESULT).read_text(encoding="utf-8")
    if re.search(r"(?m)^PASS\s*$", result_text) is None:
        raise RelayError("RESULT_NOT_PASS", "M00-RESULT.md does not contain an exact PASS status line")
    seed_text = (ctx.repo / M00_SEED).read_text(encoding="utf-8")
    if len(re.findall(r"https?://[^\s)>]+", seed_text)) < 3:
        raise RelayError("SEED_INCOMPLETE", "M00 seed contains fewer than three URLs")
    current = parse_current_work(read_current_work_text(ctx))
    expected_module = "execution-modules/M01-PROVEN-SYSTEMS-LANDSCAPE-AND-BASELINES.md"
    if current.get("status") != "READY_FOR_M01" or current.get("active_module") != expected_module:
        raise RelayError("CURRENT_WORK_NOT_ADVANCED", "M00 did not advance CURRENT-WORK to READY_FOR_M01")
    saved = load_state(ctx.state_path)
    saved.update({"module": "M00", "result_sha": local_head, "status": "M00_VERIFIED"})
    save_state(ctx.state_path, saved)
    return {"status": "verified", "module": "M00", "result_sha": local_head, "current_work": current}


def gate_message(gate: str, result_sha: str) -> str:
    event_id = f"{gate}:{result_sha}"
    return (
        f"[TTK_RELAY_GATE event_id={event_id}] Review {gate} from GitHub main using the V3 authority and "
        f"the executor result ending at commit {result_sha}. ChatGPT must create and push its own resulting "
        "authority/work-package commit to main. Reply with the new full commit SHA only after that push succeeds."
    )


def command_prepare_gate(ctx: Context, args: argparse.Namespace) -> dict[str, Any]:
    validate_sha(args.result_sha, "result-sha")
    event_id = f"{args.gate}:{args.result_sha}"
    state = load_state(ctx.state_path)
    if state.get("gate_event_id") == event_id:
        return {"status": "duplicate", "event_id": event_id, "gate_status": state.get("gate_status")}
    if state.get("gate_status") in {"prepared", "submitted"}:
        raise RelayError("GATE_EVENT_IN_FLIGHT", "A different gate event is already in flight")
    message = gate_message(args.gate, args.result_sha)
    state.update(
        {
            "gate": args.gate,
            "gate_event_id": event_id,
            "gate_result_sha": args.result_sha,
            "gate_status": "prepared",
            "gate_message": message,
        }
    )
    save_state(ctx.state_path, state)
    return {"status": "prepared", "event_id": event_id, "message": message}


def command_mark_gate_submitted(ctx: Context, args: argparse.Namespace) -> dict[str, Any]:
    state = load_state(ctx.state_path)
    if state.get("gate_event_id") != args.event_id:
        raise RelayError("GATE_EVENT_MISMATCH", "Submitted event does not match the prepared gate event")
    if state.get("gate_status") == "submitted":
        return {"status": "duplicate", "event_id": args.event_id}
    if state.get("gate_status") != "prepared":
        raise RelayError("GATE_NOT_PREPARED", "Gate event is not prepared")
    state["gate_status"] = "submitted"
    save_state(ctx.state_path, state)
    return {"status": "submitted", "event_id": args.event_id}


def validate_authority_state(ctx: Context, revision: str, gate: str) -> dict[str, Any]:
    state = parse_current_work(read_current_work_text(ctx, revision=revision))
    if state.get("status") == f"WAITING_FOR_{gate}":
        raise RelayError("AUTHORITY_NOT_ADVANCED", f"CURRENT-WORK still waits for {gate}")
    active_module = state.get("active_module")
    if active_module is not None:
        result = run_git(
            ctx.repo,
            "cat-file",
            "-e",
            f"{revision}:{(CURRENT_WORK.parent / active_module).as_posix()}",
            check=False,
        )
        if result.returncode != 0:
            raise RelayError("ACTIVE_MODULE_MISSING", f"Authority selects a missing module: {active_module}")
    return state


def command_verify_authority(ctx: Context, args: argparse.Namespace) -> dict[str, Any]:
    assert_repo(ctx)
    assert_clean(ctx)
    validate_sha(args.after_sha, "after-sha")
    local_head = run_git(ctx.repo, "rev-parse", "HEAD").stdout.strip()
    remote_head = fetch_main(ctx)
    if not is_ancestor(ctx, local_head, remote_head):
        raise RelayError("DIVERGED_MAIN", "Remote authority cannot fast-forward local main")
    if args.after_sha == remote_head or not is_ancestor(ctx, args.after_sha, remote_head):
        raise RelayError("AUTHORITY_COMMIT_MISSING", "No descendant remote commit is available after the result SHA")
    commits = [
        line
        for line in run_git(ctx.repo, "rev-list", "--reverse", f"{args.after_sha}..{remote_head}").stdout.splitlines()
        if line
    ]
    authority_sha: str | None = None
    authority_state: dict[str, Any] | None = None
    for commit in commits:
        paths = changed_paths(ctx, f"{commit}^", commit)
        if CURRENT_WORK.as_posix() not in paths:
            continue
        try:
            candidate = validate_authority_state(ctx, commit, args.gate)
        except RelayError:
            continue
        authority_sha = commit
        authority_state = candidate
    if authority_sha is None or authority_state is None:
        raise RelayError("AUTHORITY_COMMIT_MISSING", "No valid V3 authority transition was found in the remote range")
    run_git(ctx.repo, "merge", "--ff-only", "refs/remotes/origin/main")
    state = load_state(ctx.state_path)
    state.update({"gate": args.gate, "gate_status": "verified", "authority_sha": authority_sha})
    save_state(ctx.state_path, state)
    return {
        "status": "authority_verified",
        "gate": args.gate,
        "authority_sha": authority_sha,
        "head": remote_head,
        "current_work": authority_state,
    }


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--repo", required=True, type=Path)
    parser.add_argument("--state-path", required=True, type=Path)
    parser.add_argument("--expected-remote")
    commands = parser.add_subparsers(dest="command", required=True)
    commands.add_parser("sync")
    verify = commands.add_parser("verify-result")
    verify.add_argument("--module", required=True, choices=("M00",))
    verify.add_argument("--before-sha", required=True)
    prepare = commands.add_parser("prepare-gate")
    prepare.add_argument("--gate", required=True, choices=("R1", "R2", "R3"))
    prepare.add_argument("--result-sha", required=True)
    submitted = commands.add_parser("mark-gate-submitted")
    submitted.add_argument("--event-id", required=True)
    authority = commands.add_parser("verify-authority")
    authority.add_argument("--gate", required=True, choices=("R1", "R2", "R3"))
    authority.add_argument("--after-sha", required=True)
    return parser


def main() -> int:
    parser = build_parser()
    args = parser.parse_args()
    ctx = Context(args.repo.resolve(), args.state_path.resolve(), args.expected_remote)
    handlers = {
        "sync": command_sync,
        "verify-result": command_verify_result,
        "prepare-gate": command_prepare_gate,
        "mark-gate-submitted": command_mark_gate_submitted,
        "verify-authority": command_verify_authority,
    }
    try:
        payload = handlers[args.command](ctx, args)
    except RelayError as exc:
        emit({"status": "error", "error_code": exc.code, "error": str(exc)}, stream=sys.stderr)
        return 2
    except Exception as exc:
        emit(
            {"status": "error", "error_code": "INTERNAL_ERROR", "error_type": type(exc).__name__, "error": str(exc)},
            stream=sys.stderr,
        )
        return 3
    emit(payload)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
