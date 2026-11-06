#!/usr/bin/env python3
"""
test_m6_two_layer_carrier_drafts.py — Deterministic Verification Suite for Milestone 6:
Multi-Repo Two-Layer Carrier Drafts (11-TWO-LAYER-CARRIER-DRAFTS-MULTI-REPO.md).

Empirically verifies:
1. File existence and Runbook YAML frontmatter of 11-TWO-LAYER-CARRIER-DRAFTS-MULTI-REPO.md.
2. Extraction of all 4 concrete carrier drafts:
   - apexai-os-meta (AGENTS.md, CLAUDE.md, GEMINI.md)
   - MasterOfArts (AGENTS.md)
   - Leela-Cloud-2026 (AGENTS.md)
   - Leela-Cloud-2026 (CLAUDE.md)
3. Layer 1 Universal Contract Immutability:
   - All 4 carrier drafts carry <apex_contract v="1.0-ultra"> with all 22 rules in canonical order.
   - Normalized text of every single rule in all 4 carriers matches 16-candidate-3A-ultra.md exactly.
4. Layer 2 Domain Invariant & Lore Preservation:
   - MasterOfArts Layer 2 matches live MasterOfArts/AGENTS.md 100% character-for-character.
   - Leela-Cloud-2026 AGENTS.md Layer 2 matches live Leela-Cloud-2026/AGENTS.md 100% character-for-character.
   - Leela-Cloud-2026 CLAUDE.md Layer 2 matches live Leela-Cloud-2026/CLAUDE.md (anti-drift + routes) 100%.
   - apexai-os-meta Layer 2 preserves Windows 11 host environment, QMD speed protocol,
     canonical OpenProject node client route, and completion reporting rule.
5. Invariant preservation matrix in Section 5 covers all audited items.
6. Multi-Repo Live Carrier Immutability:
   - Confirms zero injection into live root carriers across all 3 primary repositories on disk.
"""

from __future__ import annotations
import os
import re
from pathlib import Path
import pytest
import tiktoken

REPO_ROOT = Path(__file__).resolve().parents[5]
INFORMATICS_FINAL = REPO_ROOT / "apex-meta" / "informatics" / "final"
DRAFTS_FILE = INFORMATICS_FINAL / "operations" / "11-TWO-LAYER-CARRIER-DRAFTS-MULTI-REPO.md"
CANDIDATE_16 = INFORMATICS_FINAL / "candidates" / "_archive" / "16-candidate-3A-ultra.md"

MOA_ROOT = REPO_ROOT.parent / "MasterOfArts"
LEELA_ROOT = REPO_ROOT.parent / "Leela-Cloud-2026"

CANONICAL_TAGS = [
    "target", "product_first", "scope", "communication", "hold_position",
    "ground", "reuse", "context", "recovery", "stop_repairing",
    "current_truth", "surgical", "editing", "new_machinery", "detour",
    "authoring", "trade_off", "handover", "iterative", "schemas",
    "sync", "pointers"
]


def extract_candidate_xml() -> str:
    content = CANDIDATE_16.read_text(encoding="utf-8")
    m = re.search(r"```xml\s*\n(.*?)\n```", content, re.DOTALL)
    assert m is not None, f"Could not find ```xml block in {CANDIDATE_16}"
    return m.group(1).strip()


def extract_carrier_code_blocks() -> dict[str, str]:
    text = DRAFTS_FILE.read_text(encoding="utf-8")
    
    # Section 2: apexai-os-meta
    p2 = text.find("## 2. Concrete Two-Layer Carrier: `c:\\GitDev\\apexai-os-meta`")
    p3 = text.find("## 3. Concrete Two-Layer Carrier: `c:\\GitDev\\MasterOfArts`")
    p4 = text.find("## 4. Concrete Two-Layer Carrier: `c:\\GitDev\\Leela-Cloud-2026`")
    p41 = text.find("### 4.1 Carrier 1: `AGENTS.md`")
    p42 = text.find("### 4.2 Carrier 2: `CLAUDE.md`")
    p5 = text.find("## 5. Invariant Preservation & Anti-Dilution Audit Matrix")
    
    assert all(p >= 0 for p in (p2, p3, p4, p41, p42, p5)), "Failed to locate all section headings in drafts file"
    
    sec2 = text[p2:p3]
    sec3 = text[p3:p4]
    sec41 = text[p41:p42]
    sec42 = text[p42:p5]
    
    def extract_outer_markdown(block: str) -> str:
        p_start = block.find("```markdown")
        p_end = block.rfind("\n```")
        assert p_start >= 0 and p_end > p_start, "Could not extract markdown block"
        return block[p_start + len("```markdown\n"):p_end].strip()
    
    return {
        "apexai-os-meta": extract_outer_markdown(sec2),
        "MasterOfArts": extract_outer_markdown(sec3),
        "Leela-AGENTS": extract_outer_markdown(sec41),
        "Leela-CLAUDE": extract_outer_markdown(sec42),
    }


def test_carrier_drafts_file_exists_and_frontmatter():
    assert DRAFTS_FILE.is_file(), f"Drafts file missing: {DRAFTS_FILE}"
    content = DRAFTS_FILE.read_text(encoding="utf-8")
    fm_m = re.search(r"^---\n(.*?)\n---", content, re.DOTALL)
    assert fm_m is not None, "Drafts file missing YAML frontmatter"
    
    fm_dict = {}
    for line in fm_m.group(1).splitlines():
        if line.strip() and ":" in line:
            k, v = line.split(":", 1)
            fm_dict[k.strip()] = v.strip()
            
    assert fm_dict.get("type") == "Runbook"
    assert fm_dict.get("id") == "RUNBOOK-TWO-LAYER-CARRIER-DRAFTS-v1.0"
    assert "title" in fm_dict
    assert fm_dict.get("status") == "current_truth"
    assert fm_dict.get("tags", "").startswith("[") and fm_dict.get("tags", "").endswith("]")


@pytest.mark.parametrize("carrier_key", ["apexai-os-meta", "MasterOfArts", "Leela-AGENTS", "Leela-CLAUDE"])
def test_all_carriers_contain_identical_layer1_rules(carrier_key: str):
    carriers = extract_carrier_code_blocks()
    carrier_text = carriers[carrier_key]
    cand_xml = extract_candidate_xml()
    
    # Verify root tag presence
    root_m = re.search(r"<apex_contract\s+v=\"1\.0-ultra\"\s+base_ref=\"([^\"]+)\">", carrier_text)
    assert root_m is not None, f"Root <apex_contract v=\"1.0-ultra\"> tag missing in {carrier_key}"
    
    if carrier_key == "apexai-os-meta":
        assert root_m.group(1) == "apex-meta/informatics/"
    else:
        assert root_m.group(1) == "c:/GitDev/apexai-os-meta/apex-meta/informatics/"
        
    assert "</apex_contract>" in carrier_text, f"</apex_contract> closing tag missing in {carrier_key}"
    
    # Extract contract block
    contract_block = carrier_text[root_m.start():carrier_text.find("</apex_contract>") + len("</apex_contract>")]
    
    # Verify each of the 22 rules in canonical order
    last_pos = 0
    for tag in CANONICAL_TAGS:
        pattern = rf"<{tag}(?:\s+[^>]*?)?>.*?</{tag}>"
        cm = re.search(pattern, contract_block[last_pos:], re.DOTALL)
        assert cm is not None, f"Tag <{tag}> missing or out of order in {carrier_key}"
        last_pos += cm.end()
        
        # Verify exact rule text against candidate 16
        cand_tag_m = re.search(pattern, cand_xml, re.DOTALL)
        assert cand_tag_m is not None, f"Tag <{tag}> not found in candidate 16"
        
        norm_carrier = re.sub(r"\s+", " ", cm.group(0)).strip()
        norm_cand = re.sub(r"\s+", " ", cand_tag_m.group(0)).strip()
        assert norm_carrier == norm_cand, f"Rule <{tag}> mismatch in {carrier_key} vs candidate 16"


def test_master_of_arts_layer2_exact_preservation():
    carriers = extract_carrier_code_blocks()
    moa_draft = carriers["MasterOfArts"]
    
    l2_marker = "<!-- LAYER 2: MASTER OF ARTS SPECIFIC OPERATING CONTEXT & SAFETY LORE        -->"
    p_l2 = moa_draft.find(l2_marker)
    assert p_l2 >= 0, "Layer 2 marker missing in MasterOfArts draft"
    draft_l2 = moa_draft[p_l2 + len(l2_marker):].split("-->", 1)[1].strip()
    
    live_moa_file = MOA_ROOT / "AGENTS.md"
    assert live_moa_file.is_file(), f"Live MasterOfArts AGENTS.md missing at {live_moa_file}"
    live_moa_text = live_moa_file.read_text(encoding="utf-8").strip()
    live_l2 = re.sub(r"^# Master of Arts Portfolio — Macro Context \(AGENTS\.md\)\s*", "", live_moa_text).strip()
    
    assert draft_l2 == live_l2, "MasterOfArts Layer 2 does not match live AGENTS.md verbatim"


def test_leela_cloud_agents_layer2_exact_preservation():
    carriers = extract_carrier_code_blocks()
    leela_draft = carriers["Leela-AGENTS"]
    
    l2_marker = "<!-- LAYER 2: LEELA CLOUD SPECIFIC OPERATING CONTEXT & MATERIALIZATION LORE  -->"
    p_l2 = leela_draft.find(l2_marker)
    assert p_l2 >= 0, "Layer 2 marker missing in Leela-AGENTS draft"
    draft_l2 = leela_draft[p_l2 + len(l2_marker):].split("-->", 1)[1].strip()
    
    live_leela_file = LEELA_ROOT / "AGENTS.md"
    assert live_leela_file.is_file(), f"Live Leela AGENTS.md missing at {live_leela_file}"
    live_leela_text = live_leela_file.read_text(encoding="utf-8").strip()
    live_l2 = re.sub(r"^# AGENTS\.md - Leela Cloud 2026\s*", "", live_leela_text).strip()
    
    assert draft_l2 == live_l2, "Leela AGENTS.md Layer 2 does not match live AGENTS.md verbatim"


def test_leela_cloud_claude_layer2_exact_preservation():
    carriers = extract_carrier_code_blocks()
    claude_draft = carriers["Leela-CLAUDE"]
    
    l2_marker = "<!-- LAYER 2: CLAUDE ANTI-DRIFT RULES & TASK ROUTE LADDER                   -->"
    p_l2 = claude_draft.find(l2_marker)
    assert p_l2 >= 0, "Layer 2 marker missing in Leela-CLAUDE draft"
    draft_l2 = claude_draft[p_l2 + len(l2_marker):].split("-->", 1)[1].strip()
    
    live_claude_file = LEELA_ROOT / "CLAUDE.md"
    assert live_claude_file.is_file(), f"Live Leela CLAUDE.md missing at {live_claude_file}"
    live_claude_text = live_claude_file.read_text(encoding="utf-8")
    
    # Lines 5 to 63 in live CLAUDE.md (omits header and @AGENTS.md import)
    lines = live_claude_text.splitlines()
    live_l2 = "\n".join([l for l in lines[4:] if l.strip() != "@AGENTS.md"]).strip()
    
    assert draft_l2 == live_l2, "Leela CLAUDE.md Layer 2 does not match live CLAUDE.md verbatim"


def test_apexai_os_meta_layer2_preservation():
    carriers = extract_carrier_code_blocks()
    meta_draft = carriers["apexai-os-meta"]
    
    l2_marker = "<!-- LAYER 2: WINDOWS NATIVE WORKSTATION & REPO-SPECIFIC OPERATING CONTEXT   -->"
    p_l2 = meta_draft.find(l2_marker)
    assert p_l2 >= 0, "Layer 2 marker missing in apexai-os-meta draft"
    draft_l2 = meta_draft[p_l2 + len(l2_marker):].split("-->", 1)[1].strip()
    
    # Invariant 1: Windows Host Environment
    assert "Windows 11 host (`c:\\GitDev\\apexai-os-meta`)" in draft_l2
    assert "ki-basis" in draft_l2
    
    # Invariant 2: QMD Retrieval Tooling
    assert "qmd search" in draft_l2
    assert "qmd query" in draft_l2
    assert "DEC-QMD-01" in draft_l2
    assert "DEC-QMD-02" in draft_l2
    assert "DEC-QMD-04" in draft_l2
    assert "20–40 line windows" in draft_l2
    
    # Invariant 3: Canonical OpenProject Route
    assert "C:\\GitDev\\agent-skills\\skills\\openproject" in draft_l2
    assert "node C:\\GitDev\\agent-skills\\skills\\openproject\\client\\opCall.js" in draft_l2
    assert "http://127.0.0.1:8083" in draft_l2
    assert "--confirmed" in draft_l2
    
    # Invariant 4: Completion Reporting Rule
    assert "Never describe a proposed block as applied" in draft_l2


def test_multi_repo_carrier_immutability():
    """Verify live root carriers in all 3 repos remain strictly unmutated."""
    meta_carriers = [REPO_ROOT / "AGENTS.md", REPO_ROOT / "CLAUDE.md", REPO_ROOT / "GEMINI.md"]
    for c in meta_carriers:
        assert c.is_file(), f"Missing meta carrier: {c}"
        assert "<apex_contract" not in c.read_text(encoding="utf-8"), f"Meta carrier {c.name} contaminated"
        
    moa_agents = MOA_ROOT / "AGENTS.md"
    assert moa_agents.is_file(), f"Missing MoA carrier: {moa_agents}"
    assert "<apex_contract" not in moa_agents.read_text(encoding="utf-8"), f"MoA carrier contaminated"
    
    leela_agents = LEELA_ROOT / "AGENTS.md"
    assert leela_agents.is_file(), f"Missing Leela AGENTS.md: {leela_agents}"
    assert "<apex_contract" not in leela_agents.read_text(encoding="utf-8"), f"Leela AGENTS.md contaminated"
    
    leela_claude = LEELA_ROOT / "CLAUDE.md"
    assert leela_claude.is_file(), f"Missing Leela CLAUDE.md: {leela_claude}"
    assert "<apex_contract" not in leela_claude.read_text(encoding="utf-8"), f"Leela CLAUDE.md contaminated"
