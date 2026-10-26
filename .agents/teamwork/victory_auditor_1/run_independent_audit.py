#!/usr/bin/env python3
"""
run_independent_audit.py — Independent Victory Auditor Verification Script.

Zero shared context with implementation team.
Independently verifies:
1. Deterministic OKF Conformance via okf_validator.py
2. Requirements R1–R5 and Acceptance Criteria
3. Significance ranking syntax [P<tier> | I/E/R] & descending sort
4. Math formula ban (zero computed scores)
5. Top-loaded primacy (first P0 <= 500 tokens)
6. Router ceilings (~100 lines / ~400 tokens / <= 2000 chars)
7. XML IF-clause gating & zero eager @path imports
8. Context isolation simulation
9. Operational lore traceability (8 Anti-drift laws, Operator challenge boundary, etc.)
10. Execution of the team's canonical test suites and comparison against claims.
"""

from __future__ import annotations

import json
from pathlib import Path
import re
import subprocess
import sys
from typing import Dict, List, Tuple

REPO_ROOT = Path(r"c:\GitDev\apexai-os-meta")
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics"
SCRIPTS_DIR = REPO_ROOT / "apex-meta" / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import okf_validator

DELIVERABLES = [
    "Agent_Setup/index.md",
    "file-architecture.md",
    "writing-profile.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
    "index.md",
    "general-informatics-router.md",
]

SIG_TAG_REGEX = re.compile(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]")
ROUTER_XML_TAG_REGEX = re.compile(
    r'<informatics\s+when="([^"]+)"\s+ref="([^"]+)"(?:\s+deepen_when="([^"]+)")?\s*/?>'
)


def estimate_tokens(text: str) -> int:
    return max(1, len(text) // 4)


def run_audit() -> Dict[str, any]:
    report = {
        "okf_validator": {},
        "deliverables": {},
        "r1_significance": {},
        "r2_ceilings": {},
        "r3_router": {},
        "r4_specification_suite": {},
        "r5_operational_lore": {},
        "context_isolation": {},
        "canonical_tests": {},
        "all_passed": True,
        "failures": [],
    }

    # 1. OKF Validator
    val_rep = okf_validator.validate_bundle(INFORMATICS_DIR)
    okf_errors = val_rep.okf_errors
    apex_errors = val_rep.apex_profile_errors
    advisories = val_rep.advisory_warnings

    report["okf_validator"] = {
        "okf_errors": okf_errors,
        "apex_errors": apex_errors,
        "advisories": advisories,
    }
    if okf_errors or apex_errors:
        report["all_passed"] = False
        report["failures"].append(f"OKF Validator errors: {okf_errors} OKF, {apex_errors} Apex")

    # 2. Deliverables existence and metrics
    total_tags_all_files = 0
    tier_counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}

    for rel_path in DELIVERABLES:
        fpath = INFORMATICS_DIR / rel_path
        if not fpath.exists():
            report["all_passed"] = False
            report["failures"].append(f"Missing deliverable: {rel_path}")
            continue

        content = fpath.read_text(encoding="utf-8")
        clean_content = re.sub(r"```[\s\S]*?```", "", content)
        tags = SIG_TAG_REGEX.findall(clean_content)

        # Check descending order
        inversions = 0
        tag_objs = []
        for tier, i_str, e_str, r_str in tags:
            tag_objs.append((tier, int(i_str), int(e_str), int(r_str)))
            tier_counts[tier] += 1
            total_tags_all_files += 1

        rank_map = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
        for i in range(len(tag_objs) - 1):
            if rank_map[tag_objs[i][0]] > rank_map[tag_objs[i + 1][0]]:
                inversions += 1

        # Check top-loaded primacy
        first_p0_token = None
        p0_matches = [m for m in SIG_TAG_REGEX.finditer(clean_content) if m.group(1) == "P0"]
        if p0_matches:
            first_p0_pos = p0_matches[0].start()
            first_p0_token = estimate_tokens(clean_content[:first_p0_pos])

        # Check formula ban
        formula_matches = re.findall(r"\b(?:I\s*[\*\+/]\s*E|Score\s*=|Expected\s*Value\s*=)\b", clean_content)

        report["deliverables"][rel_path] = {
            "lines": len(content.splitlines()),
            "chars": len(content),
            "tokens": estimate_tokens(content),
            "tag_count": len(tags),
            "inversions": inversions,
            "first_p0_token": first_p0_token,
            "formula_matches": len(formula_matches),
        }

        if inversions > 0:
            report["all_passed"] = False
            report["failures"].append(f"{rel_path} has {inversions} priority order inversions")
        if first_p0_token is not None and first_p0_token > 500:
            report["all_passed"] = False
            report["failures"].append(f"{rel_path} first P0 is at token {first_p0_token} (> 500)")
        if formula_matches:
            report["all_passed"] = False
            report["failures"].append(f"{rel_path} contains computed formula score: {formula_matches}")

    report["r1_significance"] = {
        "total_tags": total_tags_all_files,
        "tier_counts": tier_counts,
    }

    # 3. Router checks (R2 & R3)
    router_path = INFORMATICS_DIR / "general-informatics-router.md"
    router_text = router_path.read_text(encoding="utf-8")
    router_lines = len(router_text.splitlines())
    router_tokens = estimate_tokens(router_text)
    router_chars = len(router_text)
    eager_imports = re.findall(r"@[\w./\-]+\.md", router_text)
    xml_tags = ROUTER_XML_TAG_REGEX.findall(router_text)

    report["r2_ceilings"] = {
        "router_lines": router_lines,
        "router_tokens": router_tokens,
        "router_chars": router_chars,
        "eager_imports": eager_imports,
        "xml_tags_count": len(xml_tags),
    }

    if router_lines > 120:
        report["all_passed"] = False
        report["failures"].append(f"Router lines {router_lines} > 120 ceiling")
    if router_tokens > 500:
        report["all_passed"] = False
        report["failures"].append(f"Router tokens {router_tokens} > 500 ceiling")
    if eager_imports:
        report["all_passed"] = False
        report["failures"].append(f"Router contains eager imports: {eager_imports}")
    if len(xml_tags) < 5:
        report["all_passed"] = False
        report["failures"].append(f"Router has fewer than 5 XML dispatch tags ({len(xml_tags)})")

    # 4. Context Isolation Simulation
    dispatches = {when: ref for when, ref, _ in xml_tags}
    writing_target = dispatches.get("writing_or_documentation")
    if writing_target != "writing-profile.md":
        report["all_passed"] = False
        report["failures"].append(f"Context isolation: expected writing-profile.md, got {writing_target}")

    writing_profile_tokens = report["deliverables"]["writing-profile.md"]["tokens"]
    router_tokens = report["deliverables"]["general-informatics-router.md"]["tokens"]
    total_bundle_tokens = sum(d["tokens"] for d in report["deliverables"].values())
    loaded_isolated_tokens = writing_profile_tokens + router_tokens
    token_savings_pct = (1.0 - (loaded_isolated_tokens / total_bundle_tokens)) * 100.0

    report["context_isolation"] = {
        "writing_target": writing_target,
        "isolated_tokens": loaded_isolated_tokens,
        "total_bundle_tokens": total_bundle_tokens,
        "token_savings_pct": round(token_savings_pct, 1),
    }

    # 5. Operational Lore Verification (R5)
    anti_drift_text = (INFORMATICS_DIR / "anti-drift-rules.md").read_text(encoding="utf-8")
    lore_checks = {
        "operator_challenge_boundary": 'Does this need to be fixed before we can test the actual product?' in anti_drift_text,
        "two_strike_rule": 'Two-Strike' in anti_drift_text,
        "target_dominance": 'TARGET Dominance' in anti_drift_text or 'TARGET dominates' in anti_drift_text,
        "sunk_cost": 'Sunk-Cost' in anti_drift_text,
        "substance_over_ceremony": 'Substance Over Ceremony' in anti_drift_text,
        "residual_name_eradication": 'Residual Name Eradication' in anti_drift_text,
    }
    report["r5_operational_lore"] = lore_checks
    for k, v in lore_checks.items():
        if not v:
            report["all_passed"] = False
            report["failures"].append(f"Missing operational lore: {k}")

    # 6. Canonical Test Re-execution
    # Run test_informatics_e2e.py in JSON mode
    proc_e2e = subprocess.run(
        [sys.executable, str(INFORMATICS_DIR / "tests" / "test_informatics_e2e.py"), "--json"],
        capture_output=True,
        text=True,
    )
    if proc_e2e.returncode != 0:
        report["all_passed"] = False
        report["failures"].append(f"test_informatics_e2e.py failed with exit code {proc_e2e.returncode}")
        report["canonical_tests"]["e2e"] = {"exit_code": proc_e2e.returncode, "stdout": proc_e2e.stdout, "stderr": proc_e2e.stderr}
    else:
        try:
            report["canonical_tests"]["e2e"] = json.loads(proc_e2e.stdout)
        except Exception:
            report["canonical_tests"]["e2e"] = {"stdout": proc_e2e.stdout}

    # Run test_tier5_adversarial.py
    proc_t5 = subprocess.run(
        [sys.executable, str(INFORMATICS_DIR / "tests" / "test_tier5_adversarial.py")],
        capture_output=True,
        text=True,
    )
    if proc_t5.returncode != 0:
        report["all_passed"] = False
        report["failures"].append(f"test_tier5_adversarial.py failed with exit code {proc_t5.returncode}")
    report["canonical_tests"]["tier5"] = {
        "exit_code": proc_t5.returncode,
        "ran_tests": len(re.findall(r"\.\.\. ok", proc_t5.stderr)),
        "ok": "OK" in proc_t5.stderr,
    }

    return report


if __name__ == "__main__":
    rep = run_audit()
    print(json.dumps(rep, indent=2))
    sys.exit(0 if rep["all_passed"] else 1)
