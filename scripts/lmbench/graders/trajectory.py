"""Trajectory grader: runs the fixture's declared `forbidden_event_assertions`
-- the non-occurrence / event-ordering rules -- through the checks registry.
Distinct from the outcome grader: trajectory grades *how* the actor got
there (the event sequence), outcome grades *where it ended up* (final
environment state). Both can independently pass or fail -- a correct
escalation should pass trajectory while the environment stays untouched."""

from __future__ import annotations

from . import GraderResult
from .checks import run_assertion_list
from .evidence import Evidence


def grade(evidence: Evidence, forbidden_assertions: list) -> GraderResult:
    status, detail = run_assertion_list(evidence, forbidden_assertions, grader_name="trajectory")
    return GraderResult(name="trajectory", status=status, detail=detail)


__all__ = ["grade"]
