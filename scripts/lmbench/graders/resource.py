"""Resource grader: reports elapsed time / memory metrics. Measured and
reported in round 1, never gated -- inventing a resource threshold now would
fabricate the evidence this benchmark exists to produce (portfolio Section 4
gate 6 has no numeric threshold until baseline runs establish one)."""

from __future__ import annotations

from . import GraderResult, STATUS_PASS
from .evidence import Evidence


def grade(evidence: Evidence) -> GraderResult:
    metrics = evidence.outcome_probe.get("resource_metrics", {})
    detail = tuple(f"{key}={value}" for key, value in sorted(metrics.items()))
    if not detail:
        detail = ("no resource metrics captured",)
    return GraderResult(name="resource", status=STATUS_PASS, detail=detail)


__all__ = ["grade"]
