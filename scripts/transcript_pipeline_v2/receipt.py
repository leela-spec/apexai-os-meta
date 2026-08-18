"""Atomic receipt helper for Transcript Pipeline V2."""
from __future__ import annotations

import json
import os
import tempfile
import time
from datetime import datetime, timezone
from pathlib import Path
from typing import Any


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).isoformat()


def sanitize_no_secrets(data: Any) -> Any:
    """Recursively ensure no secret values are leaked in receipt dicts."""
    forbidden_keys = {
        "api_key", "token", "auth_token", "password", "secret", "cookie",
        "anthropic_api_key", "openai_api_key", "gemini_api_key", "google_api_key"
    }
    if isinstance(data, dict):
        cleaned = {}
        for k, v in data.items():
            if str(k).lower() in forbidden_keys:
                cleaned[k] = "[REDACTED_SECRET]"
            else:
                cleaned[k] = sanitize_no_secrets(v)
        return cleaned
    elif isinstance(data, list):
        return [sanitize_no_secrets(x) for x in data]
    return data


def write_atomic_receipt(path: Path, data: dict[str, Any]) -> None:
    """Atomically write sanitized JSON receipt."""
    path = Path(path).resolve()
    path.parent.mkdir(parents=True, exist_ok=True)
    sanitized = sanitize_no_secrets(data)
    
    # Write to a temp file in the same directory for atomic replace
    temp_file = tempfile.NamedTemporaryFile(
        mode="w",
        encoding="utf-8",
        dir=str(path.parent),
        delete=False,
        suffix=".tmp"
    )
    try:
        json.dump(sanitized, temp_file, indent=2, ensure_ascii=False)
        temp_file.write("\n")
        temp_file.flush()
        temp_file.close()
        os.replace(temp_file.name, str(path))
    except Exception:
        if os.path.exists(temp_file.name):
            try:
                os.remove(temp_file.name)
            except OSError:
                pass
        raise


class ExecutionReceipt:
    """Context manager / builder for task and invocation receipts."""

    def __init__(self, receipt_path: Path, task_id: str, config: dict[str, Any] | None = None):
        self.receipt_path = Path(receipt_path)
        self.task_id = task_id
        self.config = config or {}
        self.started_at: str = utc_now_iso()
        self.start_time: float = time.time()
        self.finished_at: str | None = None
        self.wall_time_seconds: float = 0.0
        self.exit_code: int = 0
        self.input_hash: str | None = None
        self.output_hash: str | None = None
        self.status: str = "IN_PROGRESS"
        self.extra: dict[str, Any] = {}

    def complete(
        self,
        exit_code: int = 0,
        input_hash: str | None = None,
        output_hash: str | None = None,
        status: str = "PASS",
        **kwargs: Any
    ) -> dict[str, Any]:
        self.finished_at = utc_now_iso()
        self.wall_time_seconds = round(time.time() - self.start_time, 4)
        self.exit_code = exit_code
        self.input_hash = input_hash
        self.output_hash = output_hash
        self.status = status
        self.extra.update(kwargs)
        receipt_data = self.to_dict()
        write_atomic_receipt(self.receipt_path, receipt_data)
        return receipt_data

    def fail(self, error: str, exit_code: int = 1, **kwargs: Any) -> dict[str, Any]:
        return self.complete(exit_code=exit_code, status="FAIL", error=error, **kwargs)

    def to_dict(self) -> dict[str, Any]:
        return {
            "schema": "transcript-pipeline-receipt.v2",
            "task_id": self.task_id,
            "status": self.status,
            "started_at": self.started_at,
            "finished_at": self.finished_at or utc_now_iso(),
            "wall_time_seconds": self.wall_time_seconds,
            "exit_code": self.exit_code,
            "input_hash": self.input_hash,
            "output_hash": self.output_hash,
            "config": self.config,
            **self.extra
        }
