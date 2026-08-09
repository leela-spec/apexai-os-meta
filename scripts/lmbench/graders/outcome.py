"""Outcome grader: compares the frozen post-actor environment (manifest
diffs, recomputed test/holdout results in `evidence.outcome_probe`) against
the fixture's declared final-state assertions. Never trusts the actor's own
claim of success -- `finish(status=completed)` is a claim tool call like any
other; only this grader (via the checks it runs) decides whether the
environment actually agrees."""

from __future__ import annotations

from . import GraderResult
from .checks import run_assertion_list
from .evidence import Evidence


def grade(evidence: Evidence, final_state_assertions: list) -> GraderResult:
    status, detail = run_assertion_list(evidence, final_state_assertions, grader_name="outcome")
    return GraderResult(name="outcome", status=status, detail=detail)


__all__ = ["grade"]
