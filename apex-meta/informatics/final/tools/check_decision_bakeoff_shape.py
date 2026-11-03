#!/usr/bin/env python3
"""Structural shape checks for GS-12 (decision matrix) and GS-13 (bake-off rubric).

Both rules were declared in specs/governance-schemas.md as "reject a record that omits X" /
"reject a bake-off that skips or reorders phases" with no validator anywhere in this corpus
enforcing them (confirmed by reading tools/okf_validator.py in full before writing this --
it implements frontmatter/link/sentence-length checks only). This closes that specific gap.

Deliberately checks SHAPE only (are the required elements present, in the right places), not
substance (is the recommendation actually correct) -- substance is Class C, see
operations/15-PROSE-TO-DETERMINISTIC-TRANSLATION-FINDINGS.md.

Standalone by design, not merged into okf_validator.py this session -- lower risk than editing a
production validator without having read every one of its call sites. Reuses its Finding
severity vocabulary (APEX_PROFILE_ERROR) for consistency, not its code.

Usage:
    python tools/check_decision_bakeoff_shape.py <file.md> [<file.md> ...]
    python tools/check_decision_bakeoff_shape.py --selftest
"""

from __future__ import annotations

import re
import sys
from dataclasses import dataclass
from pathlib import Path


@dataclass
class Finding:
    severity: str  # 'APEX_PROFILE_ERROR'
    path: str
    rule: str
    message: str


# GS-13: 4-Phase Comparison Bake-Off Rubric (execution-modes.md §3.1 / bake-off.md §3)
BAKEOFF_PHASE_MARKERS = [
    r"(?i)phase\s*1.*discovery|candidate discovery",
    r"(?i)phase\s*2.*evaluation|multi-metric evaluation",
    r"(?i)phase\s*3.*verdict|ranked verdict",
    r"(?i)phase\s*4.*prototype|functional prototype",
]
BAKEOFF_TABLE_COLUMNS = ["Primary Failure Mode"]

# GS-12: Structured Decision Matrix Protocol (execution-modes.md §2.1)
DECISION_MATRIX_FIELDS = ["Question", "Grounding", "Recommendation", "Reasoning"]
IER_TAG_RE = re.compile(r"\(I\d{1,3}/E\d{1,3}/R\d{1,3}\)")


def looks_like_bakeoff(text: str) -> bool:
    return bool(re.search(r"(?i)bake-?off|comparison matrix", text))


def looks_like_decision_matrix(text: str) -> bool:
    return bool(re.search(r"(?i)decision matrix|\|\s*question\s*\|", text, re.IGNORECASE))


def check_bakeoff_shape(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    missing_phases = [m for m in BAKEOFF_PHASE_MARKERS if not re.search(m, text)]
    if missing_phases:
        findings.append(
            Finding(
                "APEX_PROFILE_ERROR",
                path,
                "GS-13",
                f"bake-off is missing {len(missing_phases)}/4 required phase markers "
                "(discovery, evaluation matrix, ranked verdicts, prototypes) -- reject per GS-13",
            )
        )
    for col in BAKEOFF_TABLE_COLUMNS:
        if col not in text:
            findings.append(
                Finding(
                    "APEX_PROFILE_ERROR",
                    path,
                    "GS-13",
                    f"bake-off comparison table is missing required column '{col}'",
                )
            )
    return findings


def check_decision_matrix_shape(path: str, text: str) -> list[Finding]:
    findings: list[Finding] = []
    for field in DECISION_MATRIX_FIELDS:
        if field.lower() not in text.lower():
            findings.append(
                Finding(
                    "APEX_PROFILE_ERROR",
                    path,
                    "GS-12",
                    f"decision matrix is missing required field '{field}'",
                )
            )
    if not IER_TAG_RE.search(text):
        findings.append(
            Finding(
                "APEX_PROFILE_ERROR",
                path,
                "GS-12",
                "decision matrix has no raw (I/E/R) tag on any option -- required by GS-12",
            )
        )
    option_count = len(re.findall(r"(?i)^\s*-?\s*\*?\*?option\b", text, re.MULTILINE))
    if option_count < 2:
        findings.append(
            Finding(
                "APEX_PROFILE_ERROR",
                path,
                "GS-12",
                f"decision matrix names {option_count} option(s); GS-12 requires >=2",
            )
        )
    return findings


def check_file(path: Path) -> list[Finding]:
    text = path.read_text(encoding="utf-8")
    findings: list[Finding] = []
    if looks_like_bakeoff(text):
        findings += check_bakeoff_shape(str(path), text)
    if looks_like_decision_matrix(text):
        findings += check_decision_matrix_shape(str(path), text)
    return findings


_SELFTEST_GOOD_BAKEOFF = """
# A bake-off
We ran a bake-off comparison matrix.
Phase 1: Candidate Discovery & Hard Gating
Phase 2: Multi-Metric Evaluation Matrix
Phase 3: Ranked Verdicts
Phase 4: Functional Prototypes & Decision Triggers
| Candidate | Primary Failure Mode |
|---|---|
| A | flaky |
"""

_SELFTEST_BAD_BAKEOFF = """
# A bake-off
We ran a bake-off comparison matrix and picked Candidate A because it felt right.
"""

_SELFTEST_GOOD_DECISION = """
## Decision matrix
Question: which DB?
Option A: Postgres. Grounding: used elsewhere. (I80/E70/R20)
Option B: SQLite. Grounding: simpler. (I60/E50/R10)
Recommendation: A. Reasoning: scale.
"""

_SELFTEST_BAD_DECISION = """
## Decision matrix
Question: which DB? We picked Postgres.
"""


def selftest() -> int:
    cases = [
        ("good bakeoff", _SELFTEST_GOOD_BAKEOFF, 0),
        ("bad bakeoff", _SELFTEST_BAD_BAKEOFF, 1),
        ("good decision matrix", _SELFTEST_GOOD_DECISION, 0),
        ("bad decision matrix", _SELFTEST_BAD_DECISION, 1),
    ]
    ok = True
    for name, text, expect_findings in cases:
        findings = []
        if looks_like_bakeoff(text):
            findings += check_bakeoff_shape("<selftest>", text)
        if looks_like_decision_matrix(text):
            findings += check_decision_matrix_shape("<selftest>", text)
        has_findings = 1 if findings else 0
        status = "PASS" if has_findings == expect_findings else "FAIL"
        if status == "FAIL":
            ok = False
        print(f"{status}: {name} -> {len(findings)} finding(s)")
        for f in findings:
            print(f"    {f.rule}: {f.message}")
    print("ALL PASS" if ok else "SOME FAILED")
    return 0 if ok else 1


def main(argv: list[str]) -> int:
    if not argv or argv[0] == "--selftest":
        return selftest()
    total = 0
    for arg in argv:
        path = Path(arg)
        findings = check_file(path)
        for f in findings:
            print(f"{f.severity}: {f.path}: {f.rule}: {f.message}")
        total += len(findings)
    return 1 if total else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
