#!/usr/bin/env python3
"""
test_m5_challenger_verification.py — Adversarial Empirical Verification Suite for Milestone 5:
Candidate 16-candidate-3A-ultra.md vs 13-candidate-3A-xml.md and Layered Rule KB (01-22).

Empirically verifies:
1. Candidate 16-ultra file existence and OKF v0.2 frontmatter conformance.
2. XML block extraction from 16-candidate-3A-ultra.md and 100% exact metric reproduction:
   - Lines, words, chars, repo tokens (chars // 4), BPE tokens (cl100k_base).
3. Header callout claims and section 1 claims match measured values.
4. Baseline 13-candidate-3A-xml.md metric verification and claimed delta verification.
5. Exact 100% match of all 22 rule snippets against Option B in rule-01 through rule-22 §3 rollup tables.
6. Section 3 Delta Table arithmetic, per-rule BPE metrics, and percentage savings verification.
7. Total row arithmetic and whole-block token reconciliation.
8. Preservation of exact 22 semantic tags in canonical order and root wrapper attributes.
9. Immutability of live carrier files (AGENTS.md, CLAUDE.md, GEMINI.md).
"""

from __future__ import annotations
import os
import re
import subprocess
from pathlib import Path
import pytest
import tiktoken

REPO_ROOT = Path(__file__).resolve().parents[5]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_16 = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "16-candidate-3A-ultra.md"
CANDIDATE_13 = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

enc = tiktoken.get_encoding("cl100k_base")

CANONICAL_TAGS = [
    "target", "product_first", "scope", "communication", "hold_position",
    "ground", "reuse", "context", "recovery", "stop_repairing",
    "current_truth", "surgical", "editing", "new_machinery", "detour",
    "authoring", "trade_off", "handover", "iterative", "schemas",
    "sync", "pointers"
]


def extract_xml_block(file_path: Path) -> str:
    content = file_path.read_text(encoding="utf-8")
    m = re.search(r"```xml\s*\n(.*?)\n```", content, re.DOTALL)
    assert m is not None, f"Could not find ```xml ... ``` block in {file_path}"
    return m.group(1)


def get_rule_file(num: int) -> Path:
    matches = list(KB_DIR.glob(f"rule-{num:02d}*.md"))
    assert len(matches) == 1, f"Expected 1 file for rule-{num:02d}, found {len(matches)}"
    return matches[0]


def test_candidate_16_file_exists_and_frontmatter():
    assert CANDIDATE_16.exists(), f"File {CANDIDATE_16} does not exist"
    content = CANDIDATE_16.read_text(encoding="utf-8")
    fm_m = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    assert fm_m is not None, "16-candidate-3A-ultra.md missing YAML frontmatter"
    
    fm_dict = {}
    for line in fm_m.group(1).splitlines():
        if line.strip() and ":" in line:
            k, v = line.split(":", 1)
            fm_dict[k.strip()] = v.strip()
            
    assert fm_dict.get("type") == "Reference"
    assert fm_dict.get("id") == "V2-CANDIDATE-3A-ULTRA-v1.0"
    assert "title" in fm_dict
    assert "description" in fm_dict
    assert fm_dict.get("status") == "current_candidate"
    assert fm_dict.get("tags", "").startswith("[") and fm_dict.get("tags", "").endswith("]")


def test_candidate_16_measured_metrics():
    xml_block = extract_xml_block(CANDIDATE_16)
    
    measured_lines = len(xml_block.splitlines())
    measured_words = len(xml_block.split())
    measured_chars = len(xml_block)
    measured_repo = measured_chars // 4
    measured_bpe = len(enc.encode(xml_block))
    
    # Assert against ground truth
    assert measured_lines == 65, f"Expected 65 lines, got {measured_lines}"
    assert measured_words == 769, f"Expected 769 words, got {measured_words}"
    assert measured_chars == 5917, f"Expected 5,917 chars, got {measured_chars}"
    assert measured_repo == 1479, f"Expected 1,479 repo tokens, got {measured_repo}"
    assert measured_bpe == 1225, f"Expected 1,225 BPE tokens, got {measured_bpe}"
    
    # Assert against header callout claims in line 14
    content = CANDIDATE_16.read_text(encoding="utf-8")
    assert "`5,917` chars" in content
    assert "`1,479` repo tokens (`chars // 4`)" in content
    assert "`1,225` BPE tokens (`cl100k_base`)" in content
    assert "`769` words" in content
    assert "`65` lines" in content


def test_candidate_13_baseline_metrics():
    xml_block = extract_xml_block(CANDIDATE_13)
    
    measured_lines = len(xml_block.splitlines())
    measured_words = len(xml_block.split())
    measured_chars = len(xml_block)
    measured_repo = measured_chars // 4
    measured_bpe = len(enc.encode(xml_block))
    
    assert measured_lines == 65
    assert measured_words == 899
    assert measured_chars == 6529
    assert measured_repo == 1632
    assert measured_bpe == 1350


def test_metric_deltas_and_percentages():
    xml16 = extract_xml_block(CANDIDATE_16)
    xml13 = extract_xml_block(CANDIDATE_13)
    
    delta_chars = len(xml16) - len(xml13)
    delta_repo = (len(xml16) // 4) - (len(xml13) // 4)
    delta_bpe = len(enc.encode(xml16)) - len(enc.encode(xml13))
    delta_words = len(xml16.split()) - len(xml13.split())
    
    assert delta_chars == -612
    assert delta_repo == -153
    assert delta_bpe == -125
    assert delta_words == -130
    
    pct_bpe = delta_bpe / len(enc.encode(xml13)) * 100.0
    pct_repo = delta_repo / (len(xml13) // 4) * 100.0
    pct_chars = delta_chars / len(xml13) * 100.0
    pct_words = delta_words / len(xml13.split()) * 100.0
    
    assert round(pct_bpe, 1) == -9.3
    assert round(pct_repo, 1) == -9.4
    assert round(pct_chars, 1) == -9.4
    assert round(pct_words, 1) == -14.5


@pytest.mark.parametrize("idx, tag", list(enumerate(CANONICAL_TAGS, 1)))
def test_each_rule_matches_option_b_exact(idx: int, tag: str):
    xml16 = extract_xml_block(CANDIDATE_16)
    t16_m = re.search(rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)", xml16, re.DOTALL)
    assert t16_m is not None, f"Tag <{tag}> not found in 16-candidate-3A-ultra.md"
    cand_snippet = t16_m.group(1).strip()
    
    rf = get_rule_file(idx)
    rf_text = rf.read_text(encoding="utf-8")
    
    s3_m = re.search(r"## 3\.\s+Whole-Rule Recomposition Rollup.*?\n(\|.*?)(?:\n##|\Z)", rf_text, re.DOTALL)
    assert s3_m is not None, f"Rollup table not found in {rf.name}"
    tbl = s3_m.group(1).strip()
    rows = [r.strip() for r in tbl.splitlines() if r.strip().startswith("|") and not r.strip().startswith("|---")]
    
    # Row index 2 is Option B row (0: header, 1: baseline, 2: option B)
    opt_b_row = rows[2]
    opt_b_m = re.search(rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)", opt_b_row, re.DOTALL)
    assert opt_b_m is not None, f"Could not extract <{tag}> snippet from Option B row of {rf.name}"
    opt_b_snippet = opt_b_m.group(1).strip()
    
    norm_cand = re.sub(r"\s+", " ", cand_snippet).strip()
    norm_optb = re.sub(r"\s+", " ", opt_b_snippet).strip()
    
    assert norm_cand == norm_optb, f"Mismatch for rule {idx:02d} <{tag}>:\nCandidate:\n{norm_cand}\nOption B:\n{norm_optb}"


def test_delta_table_in_section_3():
    content = CANDIDATE_16.read_text(encoding="utf-8")
    s3_table_m = re.search(r"## 3\.\s+Rule-by-Rule Delta Table Against.*?\n(\|.*?)(?:\n---|\Z)", content, re.DOTALL)
    assert s3_table_m is not None, "Delta table not found in section 3 of candidate 16"
    
    xml16 = extract_xml_block(CANDIDATE_16)
    xml13 = extract_xml_block(CANDIDATE_13)
    
    tbl_lines = [l.strip() for l in s3_table_m.group(1).strip().splitlines() if l.strip().startswith("|") and not l.strip().startswith("|---")]
    rows = tbl_lines[1:]
    assert len(rows) == 23, f"Expected 22 rules + 1 total row = 23 rows, got {len(rows)}"
    
    for row in rows[:22]:
        cols = [c.strip() for c in row.split("|")[1:-1]]
        num = int(cols[0].replace("**", "").strip())
        tag = CANONICAL_TAGS[num - 1]
        
        claimed_base_bpe = int(cols[3].replace("**", "").replace(",", ""))
        claimed_ultra_bpe = int(cols[4].replace("**", "").replace(",", ""))
        claimed_delta = int(cols[5].replace("**", "").strip().replace("−", "-"))
        claimed_pct = float(cols[6].replace("**", "").strip().replace("−", "-").replace("%", ""))
        
        # Verify snippet BPEs
        t13_m = re.search(rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)", xml13, re.DOTALL)
        t16_m = re.search(rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)", xml16, re.DOTALL)
        
        emp_base_bpe = len(enc.encode(t13_m.group(1).strip()))
        emp_ultra_bpe = len(enc.encode(t16_m.group(1).strip()))
        
        assert claimed_base_bpe == emp_base_bpe, f"Rule {num:02d} <{tag}> base BPE mismatch"
        assert claimed_ultra_bpe == emp_ultra_bpe, f"Rule {num:02d} <{tag}> ultra BPE mismatch"
        
        calc_delta = claimed_ultra_bpe - claimed_base_bpe
        assert claimed_delta == calc_delta, f"Rule {num:02d} <{tag}> delta arithmetic error: {claimed_delta} != {calc_delta}"
        
        calc_pct = round((calc_delta / claimed_base_bpe) * 100.0, 1)
        assert abs(claimed_pct - calc_pct) <= 0.1, f"Rule {num:02d} <{tag}> pct savings error: {claimed_pct} != {calc_pct}"
        
    # Total row
    total_cols = [c.strip() for c in rows[22].split("|")[1:-1]]
    tot_base = int(total_cols[3].replace("**", "").replace(",", ""))
    tot_ultra = int(total_cols[4].replace("**", "").replace(",", ""))
    tot_delta = int(total_cols[5].replace("**", "").strip().replace("−", "-"))
    tot_pct = float(total_cols[6].replace("**", "").strip().replace("−", "-").replace("%", ""))
    
    assert tot_base == 1350
    assert tot_ultra == 1225
    assert tot_delta == -125
    assert round((tot_delta / tot_base) * 100.0, 1) == -9.3
    assert tot_pct == -9.3


def test_all_22_tags_present_and_in_order():
    xml16 = extract_xml_block(CANDIDATE_16)
    
    # Root tag check
    assert xml16.startswith('<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">')
    assert xml16.endswith('</apex_contract>')
    
    # Check that each tag occurs in strict sequential order
    last_pos = 0
    for tag in CANONICAL_TAGS:
        pattern = rf"<{tag}(?:\s+[^>]*?)?>.*?</{tag}>"
        m = re.search(pattern, xml16[last_pos:], re.DOTALL)
        assert m is not None, f"Tag <{tag}> not found in order after position {last_pos}"
        last_pos += m.end()


def test_carrier_immutability():
    """Confirm zero informatics contract injection into live carrier files."""
    carriers = ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]
    for cname in carriers:
        cpath = REPO_ROOT / cname
        assert cpath.is_file(), f"Carrier file missing: {cpath}"
        content = cpath.read_text(encoding="utf-8")
        assert "<apex_contract" not in content, f"Live carrier {cname} contains injected <apex_contract>"
        assert "06-layered-rule-kb" not in content, f"Live carrier {cname} contains layered rule kb references"
        assert "16-candidate-3A-ultra" not in content, f"Live carrier {cname} contains 16-candidate-3A-ultra references"
