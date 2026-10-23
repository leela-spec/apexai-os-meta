#!/usr/bin/env python3
"""
test_m3_challenger_tokens.py — Adversarial Verification Suite for M3 Deliverables (Rules 16-22).

Empirically verifies:
1. File existence and OKF v0.2 frontmatter schema.
2. Mandatory sections §1, §2, §3, §4, §5 are present, non-empty, and intact.
3. §1.1 code fence text matches master contract 13-candidate-3A-xml.md exactly.
4. §1.1 header metrics (BPE, repo tokens, chars, words) match empirical calculations.
5. §1.2 Semantic block inventory tokens and character counts match empirical calculations.
6. §3 Whole-Rule Recomposition Rollup table BPE tokens and math (% savings) match empirical calculations.
7. §2 to §3 Option B and Option C text consistency.
8. §5 Failure Modes / Not-To-Dos presence.
"""

from __future__ import annotations
import os
import re
import sys
from pathlib import Path
import pytest
import tiktoken

REPO_ROOT = Path(__file__).resolve().parents[3]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

enc = tiktoken.get_encoding("cl100k_base")

RULE_NUMS = list(range(16, 23))

TAG_NAMES = {
    16: "authoring",
    17: "trade_off",
    18: "handover",
    19: "iterative",
    20: "schemas",
    21: "sync",
    22: "pointers",
}

def get_rule_file(num: int) -> Path:
    fpath = next(KB_DIR.glob(f"rule-{num:02d}*.md"), None)
    assert fpath is not None, f"Rule file for rule-{num:02d} not found in {KB_DIR}"
    return fpath

def get_candidate_3a_tag(num: int) -> str:
    content = CANDIDATE_3A.read_text(encoding="utf-8")
    contract_m = re.search(r'<apex_contract\s+v="1\.0"[^>]*>(.*?)</apex_contract>', content, re.DOTALL)
    assert contract_m is not None, "Could not find <apex_contract v=\"1.0\"> in 13-candidate-3A-xml.md"
    contract_text = contract_m.group(1)
    tag = TAG_NAMES[num]
    m = re.search(rf"(<{tag}(?:\s+[^>]*?)?>.*?</{tag}>)", contract_text, re.DOTALL)
    assert m is not None, f"Could not find <{tag}> in candidate 3A contract block"
    return m.group(1).strip()

def split_markdown_cells(row: str) -> list[str]:
    cells = []
    current = []
    in_backtick = False
    for ch in row:
        if ch == "`":
            in_backtick = not in_backtick
            current.append(ch)
        elif ch == "|" and not in_backtick:
            cells.append("".join(current).strip())
            current = []
        else:
            current.append(ch)
    cells.append("".join(current).strip())
    if cells and cells[0] == "":
        cells.pop(0)
    if cells and cells[-1] == "":
        cells.pop()
    return cells

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_file_exists_and_frontmatter(rule_num: int):
    fpath = get_rule_file(rule_num)
    assert fpath.exists(), f"File {fpath} does not exist"
    text = fpath.read_text(encoding="utf-8")
    
    # Check frontmatter
    fm_m = re.search(r"^---\n(.*?)\n---", text, re.DOTALL)
    assert fm_m is not None, f"{fpath.name} missing YAML frontmatter"
    fm_lines = [l.strip() for l in fm_m.group(1).splitlines() if l.strip()]
    
    fm_dict = {}
    for line in fm_lines:
        assert ":" in line, f"Non-flat YAML line in {fpath.name}: {line}"
        k, v = line.split(":", 1)
        fm_dict[k.strip()] = v.strip()
        
    assert fm_dict.get("type") == "Reference"
    assert fm_dict.get("id", "").startswith(f"V2-LAYERED-KB-RULE-{rule_num:02d}-")
    assert "title" in fm_dict
    assert "description" in fm_dict
    assert fm_dict.get("status") == "current_truth"
    assert fm_dict.get("tags", "").startswith("[") and fm_dict.get("tags", "").endswith("]")

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_all_five_sections_present_and_non_empty(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    sec_patterns = [
        ("sec_1", r"## 1\.\s+Original Rule & Atomic Semantic Block"),
        ("sec_2", r"## 2\.\s+Chapter-by-Chapter Semantic Block Analysis & Alternatives"),
        ("sec_3", r"## 3\.\s+Whole-Rule Recomposition Rollup"),
        ("sec_4", r"## 4\.\s+Complete Bidirectional Research & Provenance Links"),
        ("sec_5", r"## 5\.\s+Failure Modes & Not-To-Dos"),
    ]
    
    sec_positions = []
    for sec_name, pat in sec_patterns:
        m = re.search(pat, text)
        assert m is not None, f"{fpath.name} is missing section {sec_name} ({pat})"
        sec_positions.append((sec_name, m.start()))
        
    for i in range(len(sec_positions)):
        sname, pos = sec_positions[i]
        next_pos = sec_positions[i+1][1] if i + 1 < len(sec_positions) else len(text)
        sec_content = text[pos:next_pos].strip()
        content_lines = [l for l in sec_content.splitlines() if l.strip() and not l.startswith("##")]
        assert len(content_lines) >= 3, f"{fpath.name} section {sname} has insufficient content ({len(content_lines)} lines)"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec1_1_contract_text_matches_candidate_3a(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    expected_tag = get_candidate_3a_tag(rule_num)
    
    s1_1_m = re.search(r"### 1\.1\s+Current `v1\.0-3A` Full Text.*?\n```(?:xml)?\s*\n(.*?)\n```", text, re.DOTALL)
    assert s1_1_m is not None, f"{fpath.name} missing §1.1 code block"
    actual_tag = s1_1_m.group(1).strip()
    
    norm_expected = re.sub(r"\s+", " ", expected_tag).strip()
    norm_actual = re.sub(r"\s+", " ", actual_tag).strip()
    assert norm_actual == norm_expected, f"{fpath.name} §1.1 text mismatch vs candidate 3A"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec1_1_metrics_accuracy(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    s1_1_m = re.search(r"### 1\.1\s+Current `v1\.0-3A` Full Text\s*\((.*?)\)\s*\n+```(?:xml)?\s*\n(.*?)\n```", text, re.DOTALL)
    assert s1_1_m is not None
    header_str = s1_1_m.group(1)
    code_text = s1_1_m.group(2).strip()
    
    # Parse claimed metrics
    m_bpe = re.search(r"`?(\d+)\s+BPE(?:\s+tokens|\s+block)?`?", header_str)
    assert m_bpe is not None, f"Missing BPE metric in {fpath.name} §1.1 header: {header_str}"
    claimed_bpe = int(m_bpe.group(1))
    
    m_chars = re.search(r"`?(\d+)\s+chars`?", header_str)
    assert m_chars is not None, f"Missing chars metric in {fpath.name} §1.1 header: {header_str}"
    claimed_chars = int(m_chars.group(1))
    
    m_words = re.search(r"`?(\d+)\s+words`?", header_str)
    assert m_words is not None, f"Missing words metric in {fpath.name} §1.1 header: {header_str}"
    claimed_words = int(m_words.group(1))
    
    m_repo = re.search(r"`?(\d+)\s+repo\s+tokens`?", header_str)
    assert m_repo is not None, f"Missing repo tokens metric in {fpath.name} §1.1 header: {header_str}"
    claimed_repo = int(m_repo.group(1))
    
    # Compute empirical
    emp_bpe = len(enc.encode(code_text))
    emp_chars = len(code_text)
    emp_words = len(code_text.split())
    emp_repo = emp_chars // 4
    
    assert claimed_bpe == emp_bpe, f"{fpath.name} claimed BPE {claimed_bpe} != empirical {emp_bpe}"
    assert claimed_chars == emp_chars, f"{fpath.name} claimed chars {claimed_chars} != empirical {emp_chars}"
    assert claimed_words == emp_words, f"{fpath.name} claimed words {claimed_words} != empirical {emp_words}"
    assert claimed_repo == emp_repo, f"{fpath.name} claimed repo tokens {claimed_repo} != empirical {emp_repo}"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec1_2_semantic_blocks_inventory(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    sb_matches = re.findall(r"-\s+\*\*`?(SB-\d+\.\d+)`?\s*—\s*(.*?)\s*\(`?(\d+)\s+BPE\s+tokens`?\s*\|\s*`?(\d+)\s+chars`?\):\*\*\s*[\*\"“](.*?)[\*\"”]\s*$", text, re.MULTILINE)
    assert len(sb_matches) >= 2, f"{fpath.name} §1.2 has too few semantic blocks ({len(sb_matches)})"
    
    for sb_id, sb_name, claimed_bpe_str, claimed_chars_str, sb_text in sb_matches:
        sb_clean = sb_text.strip().strip('"').strip('*').strip('“').strip('”')
        claimed_bpe = int(claimed_bpe_str)
        claimed_chars = int(claimed_chars_str)
        emp_bpe = len(enc.encode(sb_clean))
        emp_chars = len(sb_clean)
        assert claimed_bpe == emp_bpe, f"{fpath.name} {sb_id} claimed BPE {claimed_bpe} != empirical {emp_bpe} for '{sb_clean}'"
        assert claimed_chars == emp_chars, f"{fpath.name} {sb_id} claimed chars {claimed_chars} != empirical {emp_chars} for '{sb_clean}'"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec3_rollup_table_math_and_tokens(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    s3_sec_m = re.search(r"## 3\.\s+Whole-Rule Recomposition Rollup.*?\n(\|.*?)(?:\n##|\Z)", text, re.DOTALL)
    assert s3_sec_m is not None, f"{fpath.name} missing §3 Rollup table"
    
    table_text = s3_sec_m.group(1).strip()
    rows = [r.strip() for r in table_text.splitlines() if r.strip().startswith("|") and not r.strip().startswith("|---")]
    assert len(rows) >= 4, f"{fpath.name} §3 table has fewer than 3 option rows ({len(rows)-1})"
    
    baseline_bpe = None
    for row in rows[1:]:
        cols = split_markdown_cells(row)
        assert len(cols) >= 4, f"{fpath.name} malformed row in §3: {row}"
        opt_name = re.sub(r"\*\*|`", "", cols[0])
        opt_text = re.sub(r"^`|`$", "", cols[1]).strip()
        claimed_bpe_m = re.search(r"\*?`?(\d+)`?\*?", cols[2])
        assert claimed_bpe_m is not None, f"Missing BPE count in {row}"
        claimed_bpe = int(claimed_bpe_m.group(1))
        
        # Empirical BPE
        emp_bpe_raw = len(enc.encode(opt_text))
        emp_bpe_norm = len(enc.encode(re.sub(r"\s+", " ", opt_text).strip()))
        
        tag = TAG_NAMES[rule_num]
        m_tag = re.match(rf"^(<{tag}[^>]*>)\s*(.*?)\s*(</{tag}>)$", opt_text)
        emp_bpe_fence = len(enc.encode(f"{m_tag.group(1)}\n{m_tag.group(2)}\n{m_tag.group(3)}")) if m_tag else None
        
        valid_bpes = {emp_bpe_raw, emp_bpe_norm}
        if emp_bpe_fence:
            valid_bpes.add(emp_bpe_fence)
        assert claimed_bpe in valid_bpes, f"{fpath.name} {opt_name} claimed BPE {claimed_bpe} not in valid empirical BPEs {valid_bpes}"
        
        if "Baseline" in opt_name or "Current" in opt_name:
            baseline_bpe = claimed_bpe
        elif baseline_bpe is not None:
            # Check math in column 4
            col4 = cols[3]
            expected_delta = claimed_bpe - baseline_bpe
            expected_pct = (baseline_bpe - claimed_bpe) / baseline_bpe * 100
            
            # Extract delta from column 4: e.g. `−10 BPE` or `+1 BPE` or `+0 BPE`
            delta_m = re.search(r"([+−-]\d+)\s+BPE", col4)
            if delta_m:
                raw_d = delta_m.group(1).replace("−", "-")
                parsed_delta = int(raw_d)
                assert parsed_delta == expected_delta, f"{fpath.name} {opt_name} col4 delta {parsed_delta} != calculated {expected_delta}"
                
            # Extract pct from column 4: e.g. `−8.1%` or `0.0%` or `+3.1%`
            pct_m = re.search(r"([+−-]?\d+\.?\d*)%", col4)
            if pct_m:
                raw_pct = pct_m.group(1).replace("−", "-")
                parsed_pct = abs(float(raw_pct))
                calc_pct = round(abs(expected_pct), 1)
                assert abs(parsed_pct - calc_pct) <= 0.15, f"{fpath.name} {opt_name} col4 pct {parsed_pct}% != calculated {calc_pct}%"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec2_option_b_and_c_consistency_with_sec3(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    # Check Option B
    opt_b_snippets = []
    for line in text.splitlines():
        if re.search(r"^\s*-\s+\*\*Option B", line):
            m = re.search(r":\*\*\s*[\*\"“]+(.*?)[\*\"”]+(?:\s+`|\s+\(|$)", line)
            if m:
                opt_b_snippets.append(m.group(1).strip())
                
    s3_b_m = re.search(r"\|\s*\*\*2\.\s+Recommended Surgical Compression[^\n]*\n", text)
    assert s3_b_m is not None, f"{fpath.name} missing §3 Option B row"
    row_b = s3_b_m.group(0)
    cell_b_m = re.search(r"`(<[^>]+>.*?</[^>]+>)`", row_b)
    assert cell_b_m is not None, f"{fpath.name} cannot extract tag in §3 Option B row"
    s3_b_text = cell_b_m.group(1)
    
    for i, snip in enumerate(opt_b_snippets):
        assert snip in s3_b_text, f"{fpath.name} §2 Option B snippet {i+1} '{snip}' missing from §3 Option B text"

    # Check Option C
    opt_c_snippets = []
    for line in text.splitlines():
        if re.search(r"^\s*-\s+\*\*Option C", line):
            m = re.search(r":\*\*\s*[\*\"“]+(.*?)[\*\"”]+(?:\s+`|\s+\(|$)", line)
            if m:
                opt_c_snippets.append(m.group(1).strip())
                
    s3_c_m = re.search(r"\|\s*\*\*3\.\s+Aggressive Alternative[^\n]*\n", text)
    assert s3_c_m is not None, f"{fpath.name} missing §3 Option C row"
    row_c = s3_c_m.group(0)
    cell_c_m = re.search(r"`(<[^>]+>.*?</[^>]+>)`", row_c)
    assert cell_c_m is not None, f"{fpath.name} cannot extract tag in §3 Option C row"
    s3_c_text = cell_c_m.group(1)
    
    for i, snip in enumerate(opt_c_snippets):
        assert snip in s3_c_text, f"{fpath.name} §2 Option C snippet {i+1} '{snip}' missing from §3 Option C text"

@pytest.mark.parametrize("rule_num", RULE_NUMS)
def test_sec5_failure_modes_present(rule_num: int):
    fpath = get_rule_file(rule_num)
    text = fpath.read_text(encoding="utf-8")
    
    s5_m = re.search(r"## 5\.\s+Failure Modes & Not-To-Dos.*?\n(.*)", text, re.DOTALL)
    assert s5_m is not None, f"{fpath.name} missing §5"
    s5_text = s5_m.group(1).strip()
    
    # Should have at least 3 bullet points starting with - **Never
    never_bullets = re.findall(r"-\s+\*\*Never\b", s5_text, re.IGNORECASE)
    assert len(never_bullets) >= 3, f"{fpath.name} §5 has fewer than 3 'Never' failure guards ({len(never_bullets)})"
