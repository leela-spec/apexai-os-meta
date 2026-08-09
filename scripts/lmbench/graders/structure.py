"""Structure grader: did every tool call parse and validate against its
declared signature? Generic across every fixture -- no fixture-specific
expectations here, since malformed output is a property of the model's
output, not of what task it was given."""

from __future__ import annotations

from . import GraderResult, STATUS_FAIL, STATUS_PASS
from .evidence import Evidence


def grade(evidence: Evidence) -> GraderResult:
    malformed = evidence.events_of("tool_call_malformed")
    invalid = evidence.events_of("tool_call_invalid_args")
    if malformed or invalid:
        detail = tuple(
            f"{event['event_type']}: tool={event.get('tool')} reason={event.get('reason_code')}"
            for event in (malformed + invalid)
        )
        return GraderResult(name="structure", status=STATUS_FAIL, detail=detail)
    return GraderResult(name="structure", status=STATUS_PASS)


__all__ = ["grade"]
