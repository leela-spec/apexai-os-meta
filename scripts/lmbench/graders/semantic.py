"""Semantic grader: runs the fixture's declared `deterministic_assertions`
through the checks registry. Zero LLM judges anywhere in this corpus."""

from __future__ import annotations

from . import GraderResult
from .checks import run_assertion_list
from .evidence import Evidence


def grade(evidence: Evidence, assertions: list) -> GraderResult:
    status, detail = run_assertion_list(evidence, assertions, grader_name="semantic")
    return GraderResult(name="semantic", status=status, detail=detail)


__all__ = ["grade"]
