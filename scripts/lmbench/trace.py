"""Append-only trial event trace. Stdlib only.

Invariants copied deliberately from `scripts/fee/ledger.py` (not the code --
its 9 fields and 13-event enum are flow-shaped, and a benchmark event must
never be appendable to a production Weekly ledger): append-only, fsync-per-
append, a closed event enum where an unknown type is a hard error rather than
a silently novel log line, a corrupt line surfaces *with its line number*
rather than being skipped, and the trace never holds response bodies -- hashes
and refs only.

The event enum and field order are locked here deliberately early: later churn
would invalidate every stored trace and break VAL-10 (a trial must be
regradable from its archived trace without re-running the actor).
"""

from __future__ import annotations

import json
import os
import time
from datetime import datetime, timezone
from pathlib import Path

from .errors import BenchError

EVENT_TYPES = frozenset(
    {
        # lifecycle
        "trial_allocated",
        "fixture_materialized",
        "source_hashes_verified",
        "roots_instantiated",
        "state_seeded",
        "baseline_captured",
        "sampler_started",
        "actor_started",
        "actor_access_revoked",
        "final_captured",
        "children_terminated",
        "external_targets_verified",
        "evidence_archived",
        "workspace_destroyed",
        # actor turn
        "model_request",
        "model_response",
        "tool_call_malformed",
        "tool_call_invalid_args",
        "authority_decision",
        "tool_started",
        "tool_completed",
        "approval_requested",
        "approval_resolved",
        "escalation_emitted",
        "budget_exhausted",
        "actor_finished",
        # fault
        "runtime_error",
        "trial_invalidated",
    }
)

_FIELDS = (
    "event_id",
    "seq",
    "parent_event_id",
    "ts",
    "monotonic_ns",
    "trial_id",
    "run_id",
    "fixture_id",
    "fixture_version",
    "configuration_id",
    "policy_hash",
    "turn_index",
    "event_type",
    "actor",
    "tool",
    "action",
    "call_id",
    "authority_decision",
    "policy_rule_id",
    "reason_code",
    "arguments_digest",
    "result_digest",
    "payload_ref",
    "note",
)


class TraceError(BenchError):
    """Raised on an unknown event type or a malformed/corrupt trace line."""


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%S.%fZ")


class TraceWriter:
    """One writer per trial, one file per trial. Never shared with the
    telemetry sampler, which writes its own `resource.jsonl` -- two writers to
    one file is the easiest way to corrupt evidence."""

    def __init__(
        self,
        path: Path,
        *,
        trial_id: str,
        run_id: str,
        fixture_id: str,
        fixture_version: int,
        configuration_id: str,
        policy_hash: str,
    ):
        self.path = path
        self.trial_id = trial_id
        self.run_id = run_id
        self.fixture_id = fixture_id
        self.fixture_version = fixture_version
        self.configuration_id = configuration_id
        self.policy_hash = policy_hash
        self._seq = 0

    def emit(
        self,
        event_type: str,
        *,
        actor: str = "harness",
        parent_event_id: str | None = None,
        turn_index: int | None = None,
        tool: str | None = None,
        action: str | None = None,
        call_id: str | None = None,
        authority_decision: str | None = None,
        policy_rule_id: str | None = None,
        reason_code: str | None = None,
        arguments_digest: str | None = None,
        result_digest: str | None = None,
        payload_ref: str | None = None,
        note: str | None = None,
    ) -> str:
        if event_type not in EVENT_TYPES:
            raise TraceError(f"unknown event_type {event_type!r}; allowed: {sorted(EVENT_TYPES)}")
        self._seq += 1
        event_id = f"{self.trial_id}:{self._seq}"
        event = {
            "event_id": event_id,
            "seq": self._seq,
            "parent_event_id": parent_event_id,
            "ts": _now(),
            "monotonic_ns": time.monotonic_ns(),
            "trial_id": self.trial_id,
            "run_id": self.run_id,
            "fixture_id": self.fixture_id,
            "fixture_version": self.fixture_version,
            "configuration_id": self.configuration_id,
            "policy_hash": self.policy_hash,
            "turn_index": turn_index,
            "event_type": event_type,
            "actor": actor,
            "tool": tool,
            "action": action,
            "call_id": call_id,
            "authority_decision": authority_decision,
            "policy_rule_id": policy_rule_id,
            "reason_code": reason_code,
            "arguments_digest": arguments_digest,
            "result_digest": result_digest,
            "payload_ref": payload_ref,
            "note": note,
        }
        self.path.parent.mkdir(parents=True, exist_ok=True)
        line = json.dumps({key: event[key] for key in _FIELDS}, ensure_ascii=False)
        # Append, flush, and fsync -- a crash mid-trial must not lose the last
        # authority decision, since VAL-09/VAL-10 depend on the trace being the
        # ground truth for what actually happened.
        with self.path.open("a", encoding="utf-8", newline="\n") as handle:
            handle.write(line + "\n")
            handle.flush()
            os.fsync(handle.fileno())
        return event_id


    def write_payload(self, name: str, data: dict) -> str:
        """Writes a JSON payload alongside the trace for content that doesn't
        belong inline in the append-only log (full tool-call arguments and
        results) -- the trace keeps only a digest and this `payload_ref`,
        exactly like FEE's ledger keeps hashes-and-paths rather than bodies.
        Grading reads the referenced file, never the actor's live process, so
        a trial is regradable from disk alone (VAL-10). Same risk class as
        the trace file itself: the destination path is harness-decided (a
        fixed directory, a harness-controlled sequence number), never a
        model-supplied path -- exempted in test_architecture.py alongside
        trace.py's own JSONL append."""
        payloads_dir = self.path.parent / "payloads"
        payloads_dir.mkdir(parents=True, exist_ok=True)
        target = payloads_dir / f"{name}.json"
        target.write_text(json.dumps(data, sort_keys=True, default=str), encoding="utf-8")
        return f"payloads/{name}.json"


def read_payload(trace_path: Path, payload_ref: str) -> dict:
    target = trace_path.parent / payload_ref
    return json.loads(target.read_text(encoding="utf-8"))


def read_trace(path: Path) -> list[dict]:
    """Read a trace, surfacing a corrupt line with its number rather than
    skipping it -- a silently dropped event would make the authority replay
    (and therefore the authority grader) wrong without any visible symptom."""
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
                raise TraceError(f"{path.name}:{lineno}: corrupt trace line: {exc}") from exc
    return events


def replay_authority(events: list[dict]) -> list[dict]:
    """Every `authority_decision`-bearing event, in original order. This is the
    entire input to the authority grader -- authority grading is a *replay*
    over this list, never a re-derivation from the policy, so a grader bug
    can't silently re-decide something the broker already decided."""
    return [event for event in events if event.get("event_type") == "authority_decision"]


def event_counts(events: list[dict]) -> dict[str, int]:
    counts: dict[str, int] = {}
    for event in events:
        key = event.get("event_type")
        if key is not None:
            counts[key] = counts.get(key, 0) + 1
    return counts


__all__ = [
    "EVENT_TYPES",
    "TraceError",
    "TraceWriter",
    "read_trace",
    "read_payload",
    "replay_authority",
    "event_counts",
]
