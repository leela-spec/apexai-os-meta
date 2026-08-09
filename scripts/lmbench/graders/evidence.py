"""Trial evidence: everything a grader reads, loaded from disk. Stdlib only.

Graders read only this object -- never a live adapter, never a running
process, never the policy object directly. That is what makes "a trial is
regradable from its archived trace without re-running the actor" (VAL-10)
checkable: if a grader took a live adapter as input, that claim would be
false by construction. `claim_calls()` recovers full argument bodies from the
payload files the runner wrote via `TraceWriter.write_payload` -- the trace
itself holds only digests and refs, never bodies, per FEE's ledger
discipline.
"""

from __future__ import annotations

from dataclasses import dataclass, field
from pathlib import Path
from typing import Mapping

from .. import trace as trace_mod
from ..manifest import ManifestDiff


@dataclass(frozen=True, slots=True)
class Evidence:
    trial_id: str
    fixture_id: str
    events: tuple
    manifest_diffs: Mapping[str, ManifestDiff]
    forbidden_or_ro_roots: frozenset
    finish_status: str | None
    trial_status: str
    trace_path: Path
    outcome_probe: Mapping[str, object] = field(default_factory=dict)

    def events_of(self, event_type: str) -> tuple:
        return tuple(event for event in self.events if event["event_type"] == event_type)

    def authority_decisions(self) -> tuple:
        return self.events_of("authority_decision")

    def payload_for(self, event: dict) -> dict:
        ref = event.get("payload_ref")
        if not ref:
            return {}
        return trace_mod.read_payload(self.trace_path, ref)

    def claim_calls(self, tool_name: str) -> tuple:
        calls = []
        for event in self.events_of("tool_completed"):
            if event.get("tool") != tool_name:
                continue
            payload = self.payload_for(event)
            calls.append(payload.get("typed_args", {}))
        return tuple(calls)

    def tool_call_count(self, tool_name: str) -> int:
        return sum(1 for event in self.events_of("tool_completed") if event.get("tool") == tool_name)


def build_evidence(
    *,
    trial_id: str,
    fixture_id: str,
    trace_path: Path,
    manifest_diffs: Mapping[str, ManifestDiff],
    forbidden_or_ro_roots,
    trial_status: str,
    finish_status: str | None,
    outcome_probe: Mapping[str, object] | None = None,
) -> Evidence:
    events = trace_mod.read_trace(trace_path)
    return Evidence(
        trial_id=trial_id,
        fixture_id=fixture_id,
        events=tuple(events),
        manifest_diffs=dict(manifest_diffs),
        forbidden_or_ro_roots=frozenset(forbidden_or_ro_roots),
        finish_status=finish_status,
        trial_status=trial_status,
        trace_path=trace_path,
        outcome_probe=dict(outcome_probe or {}),
    )


__all__ = ["Evidence", "build_evidence"]
