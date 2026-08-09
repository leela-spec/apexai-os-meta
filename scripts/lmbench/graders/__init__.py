"""Six graders, one shared result type. Stdlib only.

`GraderResult.status` is tri-state (`pass`/`fail`/`unknown`), never a bare
boolean: `combine_status` treats `unknown` as sticky and never resolves it to
a pass. This corpus uses zero LLM graders, so `unknown` only arises from a
check whose inputs genuinely weren't captured (e.g. no manifest for a root
that was never declared) -- but the state exists precisely so a future
grader failure can never silently read as actor success (VAL-17).
"""

from __future__ import annotations

from dataclasses import dataclass

STATUS_PASS = "pass"
STATUS_FAIL = "fail"
STATUS_UNKNOWN = "unknown"

_STATUSES = frozenset({STATUS_PASS, STATUS_FAIL, STATUS_UNKNOWN})


@dataclass(frozen=True, slots=True)
class GraderResult:
    name: str
    status: str
    detail: tuple = ()

    def __post_init__(self) -> None:
        if self.status not in _STATUSES:
            raise ValueError(f"invalid grader status: {self.status!r}")

    @property
    def passed(self) -> bool | None:
        if self.status == STATUS_PASS:
            return True
        if self.status == STATUS_FAIL:
            return False
        return None


def combine_status(statuses) -> str:
    statuses = list(statuses)
    if any(status == STATUS_UNKNOWN for status in statuses):
        return STATUS_UNKNOWN
    if statuses and all(status == STATUS_PASS for status in statuses):
        return STATUS_PASS
    return STATUS_FAIL


__all__ = ["GraderResult", "STATUS_PASS", "STATUS_FAIL", "STATUS_UNKNOWN", "combine_status"]
