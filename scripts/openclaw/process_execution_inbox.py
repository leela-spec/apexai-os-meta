"""Deterministically dispatch bounded execution requests from a repository inbox."""

from __future__ import annotations

import argparse
import hashlib
import json
import os
import subprocess
import sys
from contextlib import contextmanager
from datetime import datetime, timezone
from pathlib import Path
from typing import BinaryIO, Iterator


POWERSHELL = Path(r"C:\Windows\System32\WindowsPowerShell\v1.0\powershell.exe")
DEFAULT_DISPATCHER = Path(__file__).with_name("dispatch-execution-request.ps1")
RECEIPT_SCHEMA = "apex.execution-inbox-receipt/v1"


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--queue-root", required=True, type=Path)
    parser.add_argument("--dispatcher-path", type=Path, default=DEFAULT_DISPATCHER)
    parser.add_argument(
        "--executor-model",
        choices=("openai/gpt-4.1-nano", "apex-local/qwen3-8b-q4km"),
        default="openai/gpt-4.1-nano",
    )
    parser.add_argument("--max-requests", type=int, default=10)
    args = parser.parse_args()
    if not args.queue_root.is_absolute():
        parser.error("--queue-root must be an absolute path")
    if not 1 <= args.max_requests <= 100:
        parser.error("--max-requests must be between 1 and 100")
    return args


def emit(payload: dict[str, object], *, stream: object = sys.stdout) -> None:
    print(json.dumps(payload, sort_keys=True, separators=(",", ":")), file=stream, flush=True)


def utc_now() -> str:
    return datetime.now(timezone.utc).isoformat().replace("+00:00", "Z")


def receipt_path(directory: Path, request_name: str) -> Path:
    suffix = ".request.json"
    stem = request_name[: -len(suffix)] if request_name.endswith(suffix) else request_name
    return directory / f"{stem}.receipt.json"


def write_json_atomic(path: Path, payload: dict[str, object]) -> None:
    temporary = path.with_name(f"{path.name}.{os.getpid()}.tmp")
    temporary.write_text(
        json.dumps(payload, indent=2, sort_keys=True) + "\n",
        encoding="utf-8",
        newline="\n",
    )
    os.replace(temporary, path)


@contextmanager
def queue_lock(queue_root: Path) -> Iterator[bool]:
    lock_path = queue_root / ".execution-inbox.lock"
    handle: BinaryIO = lock_path.open("a+b")
    acquired = False
    try:
        handle.seek(0, os.SEEK_END)
        if handle.tell() == 0:
            handle.write(b"\0")
            handle.flush()
        handle.seek(0)
        if os.name == "nt":
            import msvcrt

            try:
                msvcrt.locking(handle.fileno(), msvcrt.LK_NBLCK, 1)
                acquired = True
            except OSError:
                acquired = False
        else:
            import fcntl

            try:
                fcntl.flock(handle.fileno(), fcntl.LOCK_EX | fcntl.LOCK_NB)
                acquired = True
            except BlockingIOError:
                acquired = False
        yield acquired
    finally:
        if acquired:
            handle.seek(0)
            if os.name == "nt":
                import msvcrt

                msvcrt.locking(handle.fileno(), msvcrt.LK_UNLCK, 1)
            else:
                import fcntl

                fcntl.flock(handle.fileno(), fcntl.LOCK_UN)
        handle.close()


def invoke_dispatcher(request_path: Path, dispatcher_path: Path, executor_model: str) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        [
            str(POWERSHELL),
            "-NoProfile",
            "-NonInteractive",
            "-ExecutionPolicy",
            "Bypass",
            "-File",
            str(dispatcher_path),
            "-RequestPath",
            str(request_path),
            "-ExecutorModel",
            executor_model,
        ],
        text=True,
        capture_output=True,
        check=False,
    )


def dispatch_one(request_path: Path, completed: Path, failed: Path, dispatcher: Path, model: str) -> bool:
    request_bytes = request_path.read_bytes()
    request_hash = hashlib.sha256(request_bytes).hexdigest()
    result = invoke_dispatcher(request_path, dispatcher, model)
    dispatcher_payload: object | None = None
    error_code: str | None = None

    if result.returncode == 0:
        try:
            dispatcher_payload = json.loads(result.stdout)
        except json.JSONDecodeError:
            error_code = "DISPATCH_OUTPUT_INVALID"
        else:
            if not isinstance(dispatcher_payload, dict) or dispatcher_payload.get("status") != "completed":
                error_code = "DISPATCH_NOT_COMPLETED"
    else:
        error_code = "DISPATCH_FAILED"

    succeeded = error_code is None
    terminal_directory = completed if succeeded else failed
    terminal_request = terminal_directory / request_path.name
    os.replace(request_path, terminal_request)
    receipt: dict[str, object] = {
        "schema_version": RECEIPT_SCHEMA,
        "status": "completed" if succeeded else "failed",
        "processed_at": utc_now(),
        "request_file": request_path.name,
        "request_sha256": request_hash,
        "dispatcher_exit_code": result.returncode,
        "dispatcher_stdout": result.stdout,
        "dispatcher_stderr": result.stderr,
    }
    if dispatcher_payload is not None:
        receipt["dispatcher_payload"] = dispatcher_payload
    if error_code is not None:
        receipt["error_code"] = error_code
    write_json_atomic(receipt_path(terminal_directory, request_path.name), receipt)
    return succeeded


def process(args: argparse.Namespace) -> int:
    queue_root = args.queue_root.resolve()
    dispatcher = args.dispatcher_path.resolve()
    if not dispatcher.is_file():
        raise FileNotFoundError(f"dispatcher does not exist: {dispatcher}")

    inbox = queue_root / "inbox"
    processing = queue_root / "processing"
    completed = queue_root / "completed"
    failed = queue_root / "failed"
    for directory in (inbox, processing, completed, failed):
        directory.mkdir(parents=True, exist_ok=True)

    with queue_lock(queue_root) as acquired:
        if not acquired:
            emit({"status": "busy", "claimed": 0, "completed": 0, "failed": 0})
            return 0

        claimed = 0
        completed_count = 0
        failed_count = 0
        pending = sorted(processing.glob("*.request.json"), key=lambda path: path.name)

        for inbox_path in sorted(inbox.glob("*.request.json"), key=lambda path: path.name):
            if len(pending) >= args.max_requests:
                break
            processing_path = processing / inbox_path.name
            os.replace(inbox_path, processing_path)
            pending.append(processing_path)
            claimed += 1

        for request_path in pending[: args.max_requests]:
            if dispatch_one(request_path, completed, failed, dispatcher, args.executor_model):
                completed_count += 1
            else:
                failed_count += 1

        emit(
            {
                "status": "ok",
                "claimed": claimed,
                "completed": completed_count,
                "failed": failed_count,
            }
        )
        return 0


def main() -> int:
    args = parse_args()
    try:
        return process(args)
    except Exception as exc:
        emit(
            {"status": "error", "error_type": type(exc).__name__, "error": str(exc)},
            stream=sys.stderr,
        )
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
