"""FEE module M6 -- the evidence ledger. Stdlib only, per D-I2.

Append-only JSONL, one writer, never rewritten and never compacted mid-run (D-S7).
It is the single source of truth for what happened, and the basis of resume
idempotence: a turn already marked `turn_captured` is never re-sent.

The ledger never contains captured response bodies -- hashes and paths only
(D-S10). That keeps expensive reasoning output out of every metered context and
keeps the file greppable and small.
"""

from __future__ import annotations

import json
import os
from datetime import datetime, timezone
from pathlib import Path

# Closed set, per 02-meso-module-design M6. An unknown event type is a bug, not
# an extension point -- callers get a hard error rather than a silently novel log.
EVENT_TYPES = frozenset(
    {
        "run_started",
        "plan_frozen",
        "turn_started",
        "turn_captured",
        "turn_failed",
        "turn_skipped",
        "adjudicated",
        "follow_up_fired",
        "provider_degraded",
        "circuit_opened",
        "needs_operator",
        "halted",
        "run_completed",
    }
)

_FIELDS = (
    "ts",
    "run_id",
    "plan_hash",
    "event_type",
    "sprint_id",
    "prompt_ref",
    "provider",
    "payload_hash",
    "note",
)


class LedgerError(Exception):
    """Raised on an unknown event type or a malformed ledger line."""


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


class Ledger:
    """Append-only event log for a single flow's execution directory."""

    def __init__(self, path: Path, run_id: str, plan_hash: str | None = None):
        self.path = path
        self.run_id = run_id
        self.plan_hash = plan_hash

    def append(
        self,
        event_type: str,
        *,
        sprint_id: str | None = None,
        prompt_ref: str | None = None,
        provider: str | None = None,
        payload_hash: str | None = None,
        note: str | None = None,
        plan_hash: str | None = None,
    ) -> dict:
        if event_type not in EVENT_TYPES:
            raise LedgerError(
                f"unknown event_type {event_type!r}; allowed: {sorted(EVENT_TYPES)}"
            )
        event = {
            "ts": _now(),
            "run_id": self.run_id,
            "plan_hash": plan_hash if plan_hash is not None else self.plan_hash,
            "event_type": event_type,
            "sprint_id": sprint_id,
            "prompt_ref": prompt_ref,
            "provider": provider,
            "payload_hash": payload_hash,
            "note": note,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps({k: event[k] for k in _FIELDS}, ensure_ascii=False)
        # Append, flush, and fsync: a crash mid-run must not lose the last event,
        # because resume correctness depends on it.
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return event

    # Reading ---------------------------------------------------------------

    def events(self) -> list[dict]:
        return read_events(self.path)

    def captured_steps(self) -> set[str]:
        """Step ids already captured -- the resume skip-set (V4)."""
        return {
            event["prompt_ref"]
            for event in self.events()
            if event.get("event_type") == "turn_captured" and event.get("prompt_ref")
        }


def read_events(path: Path) -> list[dict]:
    """Read a ledger, surfacing a corrupt line with its number rather than skipping."""
    if not path.exists():
        return []
    events: list[dict] = []
    with path.open("r", encoding="utf-8") as handle:
        for lineno, raw in enumerate(handle, start=1):
            stripped = raw.strip()
            if not stripped:
                continue
            try:
                events.append(json.loads(stripped))
            except json.JSONDecodeError as exc:
                raise LedgerError(f"{path.name}:{lineno}: corrupt ledger line: {exc}") from exc
    return events


def last_event(path: Path, event_type: str | None = None) -> dict | None:
    for event in reversed(read_events(path)):
        if event_type is None or event.get("event_type") == event_type:
            return event
    return None
