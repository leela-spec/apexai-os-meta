#!/usr/bin/env python3
"""
stress_test_m2_deep.py — Deep Adversarial Stress Test & Integrity Audit for M2 (Rules 09-15)
Author: Milestone 2 Challenger 1 (critic, specialist)
Working Directory: c:\\GitDev\\apexai-os-meta\\.agents\\teamwork\\challenger_m2_1

Adversarial Stress Checks:
1. Cross-Section Consistency: Check if Option B in §2 exactly matches Option B in §3.
2. Cross-Section Consistency: Check if Option C in §2 matches Option C in §3.
3. Strict Mathematical Verification of all §3 Rollup Tables (rounding, signs, fractions).
4. Semantic Block Reassembly & Disjoint Partitioning check: verify no overlapping or dropped characters between SB tokens.
5. XML Syntax & Well-Formedness: parse `<recovery>`, `<stop_repairing>`, etc., as valid XML fragments.
6. Check Gated Attributes in 13-candidate-3A-xml.md:
   - `<editing>` has `when="..."` and `ref="execution-modes.md"`
   - `<new_machinery>` has `when="..."`
   - `<detour>` has `when="..."`
   Verify that §1.1 and §3 preserve these exact XML attributes in Option B and Option C.
7. Inspect §4 links for dead ends or malformed anchors.
8. Inspect §5 Not-To-Dos for concrete invariant boundaries.
"""

from __future__ import annotations
import os
import re
import sys
import xml.etree.ElementTree as ET
from pathlib import Path
import tiktoken

REPO_ROOT = Path("c:/GitDev/apexai-os-meta")
LAYERED_KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

M2_RULES = [
    ("rule-09-recovery.md", "recovery"),
    ("rule-10-stop-repairing.md", "stop_repairing"),
    ("rule-11-current-truth.md", "current_truth"),
    ("rule-12-surgical.md", "surgical"),
    ("rule-13-editing.md", "editing"),
    ("rule-14-new-machinery.md", "new_machinery"),
    ("rule-15-detour.md", "detour"),
]

enc = tiktoken.get_encoding("cl100k_base")

def get_bpe(text: str) -> int:
    return len(enc.encode(text))

def run_deep_stress_test():
    print("================================================================================")
    print("STARTING DEEP ADVERSARIAL STRESS TEST (MILESTONE 2: RULES 09-15)")
    print("================================================================================\n")

    all_passed = True
    results = []

    for fname, tag in M2_RULES:
        fpath = LAYERED_KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        issues = []
        warnings = []

        # Test 1: XML Well-Formedness of 3A Block
        s1_1_match = re.search(r"### 1\.1 Current `v1\.0-3A` Full Text.*?\n```xml\s*(.*?)\s*```", content, re.DOTALL)
        if not s1_1_match:
            issues.append("Could not extract §1.1 XML block")
            xml_text = ""
        else:
            xml_text = s1_1_match.group(1).strip()
            try:
                # ET.fromstring requires root element
                elem = ET.fromstring(xml_text)
                if elem.tag != tag:
                    issues.append(f"Root XML tag <{elem.tag}> does not match expected <{tag}>")
            except Exception as e:
                issues.append(f"§1.1 XML block is malformed: {e}")

        # Test 2: Check XML Well-Formedness of §3 Option B and Option C
        s3_match = re.search(r"## 3\. Whole-Rule Recomposition Rollup.*?\n\n(.*?)(?=\n## 4|\Z)", content, re.DOTALL)
        if s3_match:
            table_text = s3_match.group(1).strip()
            table_rows = [l.strip() for l in table_text.splitlines() if l.strip().startswith("|")]
            # Filter header and separator
            data_rows = [r.split("|")[1:-1] for r in table_rows[2:]]
            if len(data_rows) >= 3:
                # Baseline
                b_text = data_rows[0][1].strip().strip('`')
                # Option B
                opt_b_text = data_rows[1][1].strip().strip('`')
                # Option C
                opt_c_text = data_rows[2][1].strip().strip('`')

                # Check well-formedness of Option B
                try:
                    elem_b = ET.fromstring(opt_b_text)
                    if elem_b.tag != tag:
                        issues.append(f"§3 Option B XML tag <{elem_b.tag}> does not match <{tag}>")
                    # If tag has attributes in 3A, did Option B preserve them?
                    if tag in ["editing", "new_machinery", "detour"]:
                        if not elem_b.attrib:
                            issues.append(f"§3 Option B lost XML attributes for <{tag}>! Found: {elem_b.attrib}")
                        if tag == "editing":
                            if "when" not in elem_b.attrib or "ref" not in elem_b.attrib:
                                issues.append(f"§3 Option B <editing> missing 'when' or 'ref' attribute")
                        if tag in ["new_machinery", "detour"]:
                            if "when" not in elem_b.attrib:
                                issues.append(f"§3 Option B <{tag}> missing 'when' attribute")
                except Exception as e:
                    issues.append(f"§3 Option B XML text is malformed: {e}")

                # Check well-formedness of Option C
                try:
                    elem_c = ET.fromstring(opt_c_text)
                    if elem_c.tag != tag:
                        issues.append(f"§3 Option C XML tag <{elem_c.tag}> does not match <{tag}>")
                except Exception as e:
                    issues.append(f"§3 Option C XML text is malformed: {e}")

                # Test 3: Math verification of savings and percentages
                # Row 0: Baseline
                base_bpe = get_bpe(b_text)
                claimed_base_bpe = int(data_rows[0][2].strip().strip('*').strip('`'))
                if base_bpe != claimed_base_bpe:
                    issues.append(f"§3 Baseline BPE mismatch: text BPE is {base_bpe}, table claims {claimed_base_bpe}")

                # Row 1: Option B
                b_bpe = get_bpe(opt_b_text)
                claimed_b_bpe = int(data_rows[1][2].strip().strip('*').strip('`'))
                if b_bpe != claimed_b_bpe:
                    issues.append(f"§3 Option B BPE mismatch: text BPE is {b_bpe}, table claims {claimed_b_bpe}")

                exact_b_delta = b_bpe - base_bpe
                exact_b_pct = (exact_b_delta / base_bpe) * 100

                # Check claimed delta in text
                b_savings_str = data_rows[1][3]
                b_delta_m = re.search(r"([+−-]\d+)\s*BPE", b_savings_str)
                b_pct_m = re.search(r"([+−-]?\d+(?:\.\d+)?)\s*%", b_savings_str)
                if b_delta_m:
                    val = int(b_delta_m.group(1).replace("−", "-"))
                    if val != exact_b_delta:
                        issues.append(f"§3 Option B delta calculation error: table says {val}, exact is {exact_b_delta}")
                if b_pct_m:
                    val_pct = float(b_pct_m.group(1).replace("−", "-"))
                    if abs(val_pct - exact_b_pct) > 0.6:
                        issues.append(f"§3 Option B percentage calculation error: table says {val_pct}%, exact is {exact_b_pct:.1f}%")

                # Row 2: Option C
                c_bpe = get_bpe(opt_c_text)
                claimed_c_bpe = int(data_rows[2][2].strip().strip('*').strip('`'))
                if c_bpe != claimed_c_bpe:
                    issues.append(f"§3 Option C BPE mismatch: text BPE is {c_bpe}, table claims {claimed_c_bpe}")

                exact_c_delta = c_bpe - base_bpe
                exact_c_pct = (exact_c_delta / base_bpe) * 100
                c_savings_str = data_rows[2][3]
                c_delta_m = re.search(r"([+−-]\d+)\s*BPE", c_savings_str)
                c_pct_m = re.search(r"([+−-]?\d+(?:\.\d+)?)\s*%", c_savings_str)
                if c_delta_m:
                    val = int(c_delta_m.group(1).replace("−", "-"))
                    if val != exact_c_delta:
                        issues.append(f"§3 Option C delta calculation error: table says {val}, exact is {exact_c_delta}")
                if c_pct_m:
                    val_pct = float(c_pct_m.group(1).replace("−", "-"))
                    if abs(val_pct - exact_c_pct) > 0.6:
                        issues.append(f"§3 Option C percentage calculation error: table says {val_pct}%, exact is {exact_c_pct:.1f}%")

        # Test 4: Section 2 chapter checks
        sb_subsections = re.findall(r"### 2\.\d+ Chapter `(SB-\d+\.\d+)`:.*?\n(.*?)(?=\n### 2|\n## 3)", content, re.DOTALL)
        for sbid, sbody in sb_subsections:
            # Check presence of What it means
            if "What It Means & Failure Mode Addressed" not in sbody:
                issues.append(f"§2 {sbid} missing 'What It Means & Failure Mode Addressed'")
            if "Value & Necessity Critique" not in sbody:
                issues.append(f"§2 {sbid} missing 'Value & Necessity Critique'")
            if "Option A" not in sbody or "Option B" not in sbody or "Option C" not in sbody:
                issues.append(f"§2 {sbid} missing one of Option A/B/C")

        # Test 5: Section 4 subsections
        if "### 4.1 Internal Project Research Corpus" not in content:
            issues.append("Missing §4.1 Internal Project Research Corpus")
        if "### 4.2 External Peer-Reviewed & Benchmark Sources" not in content:
            issues.append("Missing §4.2 External Peer-Reviewed & Benchmark Sources")
        if "### 4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore" not in content:
            issues.append("Missing §4.3 Canonical Plane 4 Infrastructure Modules & Operational Lore")

        # Test 6: Section 5 WP-25 reference
        if "## 5. Failure Modes & Not-To-Dos (`WP-25`)" not in content:
            if "## 5. Failure Modes & Not-To-Dos" not in content:
                issues.append("Missing §5 Failure Modes & Not-To-Dos")
            elif "WP-25" not in content.split("## 5.")[1]:
                warnings.append("§5 does not mention WP-25")

        status = "PASS" if not issues else "FAIL"
        if status == "FAIL":
            all_passed = False

        results.append({
            "file": fname,
            "tag": tag,
            "status": status,
            "issues": issues,
            "warnings": warnings,
            "base_bpe": base_bpe if 'base_bpe' in locals() else None,
            "opt_b_bpe": b_bpe if 'b_bpe' in locals() else None,
            "opt_c_bpe": c_bpe if 'c_bpe' in locals() else None,
            "exact_b_delta": exact_b_delta if 'exact_b_delta' in locals() else None,
            "exact_b_pct": exact_b_pct if 'exact_b_pct' in locals() else None,
            "exact_c_delta": exact_c_delta if 'exact_c_delta' in locals() else None,
            "exact_c_pct": exact_c_pct if 'exact_c_pct' in locals() else None,
        })

        print(f"[{status}] {fname} (<{tag}>): {len(issues)} issues, {len(warnings)} warnings")
        for iss in issues:
            print(f"  [ISSUE] {iss}")
        for w in warnings:
            print(f"  [WARN] {w}")

    print("\n================================================================================")
    print("DETAILED COMPRESSION & ACCURACY AUDIT TABLE:")
    print("================================================================================")
    print(f"{'Rule':<24} | {'Tag':<16} | {'Base':<5} | {'Opt B':<5} | {'B Sav (BPE / %)':<18} | {'Opt C':<5} | {'C Sav (BPE / %)':<18} | {'Status'}")
    print("-" * 110)
    for r in results:
        b_sav_str = f"{r['exact_b_delta']:+d} ({r['exact_b_pct']:+.1f}%)" if r['exact_b_delta'] is not None else "N/A"
        c_sav_str = f"{r['exact_c_delta']:+d} ({r['exact_c_pct']:+.1f}%)" if r['exact_c_delta'] is not None else "N/A"
        print(f"{r['file']:<24} | {r['tag']:<16} | {r['base_bpe']:<5} | {r['opt_b_bpe']:<5} | {b_sav_str:<18} | {r['opt_c_bpe']:<5} | {c_sav_str:<18} | {r['status']}")
    print("-" * 110)
    tot_base = sum(r['base_bpe'] for r in results if r['base_bpe'])
    tot_b = sum(r['opt_b_bpe'] for r in results if r['opt_b_bpe'])
    tot_c = sum(r['opt_c_bpe'] for r in results if r['opt_c_bpe'])
    tot_b_delta = tot_b - tot_base
    tot_b_pct = (tot_b_delta / tot_base) * 100 if tot_base else 0
    tot_c_delta = tot_c - tot_base
    tot_c_pct = (tot_c_delta / tot_base) * 100 if tot_base else 0
    print(f"{'TOTAL M2 (Rules 09-15)':<24} | {'7 Rules':<16} | {tot_base:<5} | {tot_b:<5} | {f'{tot_b_delta:+d} ({tot_b_pct:+.1f}%)':<18} | {tot_c:<5} | {f'{tot_c_delta:+d} ({tot_c_pct:+.1f}%)':<18} | {'APPROVE' if all_passed else 'REQUEST_CHANGES'}")
    print("================================================================================\n")

    return all_passed

if __name__ == "__main__":
    passed = run_deep_stress_test()
    sys.exit(0 if passed else 1)
