#!/usr/bin/env python3
"""
Comprehensive verification test script for Milestone 4: Plane 4 Infrastructure Module Audits.
Run by Reviewer 2.
"""

from __future__ import annotations
import re
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parents[3]
KB_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

AUDIT_FILES = [
    "audit-module-01-writing-profile.md",
    "audit-module-02-file-architecture.md",
    "audit-module-03-execution-modes.md",
    "audit-module-04-anti-drift-rules.md",
    "audit-module-05-governance-schemas.md",
]

EXPECTED_RULES = {
    "audit-module-01-writing-profile.md": 25,
    "audit-module-02-file-architecture.md": 13,
    "audit-module-03-execution-modes.md": 12,
    "audit-module-04-anti-drift-rules.md": 28,
    "audit-module-05-governance-schemas.md": 19, # active rules (plus 3 retired)
}

EXPECTED_PREFIXES = {
    "audit-module-01-writing-profile.md": "WP",
    "audit-module-02-file-architecture.md": "FA",
    "audit-module-03-execution-modes.md": "EM",
    "audit-module-04-anti-drift-rules.md": "AD",
    "audit-module-05-governance-schemas.md": "GS",
}

def test_file_existence_and_sizes():
    print("=== 1. Checking File Existence and Physical Sizes ===")
    for fname in AUDIT_FILES:
        path = KB_DIR / fname
        assert path.exists(), f"File does not exist: {fname}"
        size = path.stat().st_size
        lines = len(path.read_text(encoding="utf-8").splitlines())
        words = len(path.read_text(encoding="utf-8").split())
        print(f"  {fname}: {size:,} bytes | {lines} lines | {words:,} words")
        assert size > 20000, f"{fname} is under 20,000 bytes ({size} bytes)"
        assert lines > 200, f"{fname} is under 200 lines ({lines} lines)"
    print("  -> PASS: All 5 files exist with substantial physical depth (>20KB each).")

def test_chapter_structure_and_terminal_wp25():
    print("\n=== 2. Checking 5-Chapter Structure & Terminal WP-25 Position ===")
    for fname in AUDIT_FILES:
        path = KB_DIR / fname
        text = path.read_text(encoding="utf-8")
        lines = text.splitlines()
        
        # Check OKF frontmatter
        assert text.startswith("---\n"), f"{fname} missing frontmatter delimiter"
        assert "type: Reference" in text, f"{fname} missing type: Reference"
        assert "status: current_truth" in text, f"{fname} missing status: current_truth"
        assert f"id: V2-AUDIT-MODULE-" in text, f"{fname} missing valid durable ID"
        
        # Check all 5 chapters
        chapters = ["## 1.", "## 2.", "## 3.", "## 4.", "## 5."]
        for ch in chapters:
            assert ch in text, f"{fname} missing {ch}"
            
        # Verify Chapter 5 is strictly in terminal position (last H2 heading)
        h2_headings = [(i + 1, l) for i, l in enumerate(lines) if l.startswith("## ")]
        last_h2_line, last_h2_text = h2_headings[-1]
        assert "5." in last_h2_text and "Failure Modes" in last_h2_text and "WP-25" in last_h2_text, (
            f"{fname} Chapter 5 is not the last H2 heading: {last_h2_text}"
        )
        print(f"  {fname}: All 5 chapters present, Chapter 5 terminal at line {last_h2_line}.")
    print("  -> PASS: All 5 files strictly implement 5-chapter structure with WP-25 terminal.")

def test_single_ownership_and_governed_rules():
    print("\n=== 3. Checking Single-Ownership Discipline (WP-23) & Rule Counts ===")
    total_governed_rules = 0
    all_rule_ids = set()
    
    # Regex to match table rows defining rules
    # E.g.: | 1 | Prose Core | `WP-01` | `[P0 \| I98/E98/R05]` | Title | ...
    table_rule_re = re.compile(r"\|\s*\d+\s*\|\s*[^|]+\|\s*`((?:WP|FA|EM|AD|GS)-\d{2})`\s*\|\s*`?\[(P[0-3])\s*\\?\|\s*I(\d+)/E(\d+)/R(\d+)\]`?\s*\|")
    
    for fname in AUDIT_FILES:
        path = KB_DIR / fname
        text = path.read_text(encoding="utf-8")
        prefix = EXPECTED_PREFIXES[fname]
        
        matches = table_rule_re.findall(text)
        print(f"  {fname} (Prefix {prefix}): {len(matches)} rules extracted from rule inventory")
        assert len(matches) == EXPECTED_RULES[fname], (
            f"{fname} expected {EXPECTED_RULES[fname]} rules, got {len(matches)}"
        )
        
        for rid, tier, imp, ev, rsk in matches:
            assert rid.startswith(f"{prefix}-"), f"Rule {rid} does not match prefix {prefix}"
            assert rid not in all_rule_ids, f"Duplicate rule ID across suite: {rid}"
            all_rule_ids.add(rid)
            assert 1 <= int(imp) <= 100, f"Impact out of range in {rid}: {imp}"
            assert 1 <= int(ev) <= 100, f"Evidence out of range in {rid}: {ev}"
            assert 1 <= int(rsk) <= 100, f"Risk out of range in {rid}: {rsk}"
            
        total_governed_rules += len(matches)
        
    print(f"  Total Active Governed Rules across 5 files: {total_governed_rules}")
    assert total_governed_rules == 97, f"Expected 97 governed rules, got {total_governed_rules}"
    
    # Verify retired rules handling in audit-module-05
    gs_text = (KB_DIR / "audit-module-05-governance-schemas.md").read_text(encoding="utf-8")
    for retired_id in ["GS-16", "GS-18", "GS-19"]:
        assert retired_id in gs_text, f"Retired ID {retired_id} not documented in audit-module-05"
        assert f"`{retired_id}`" in gs_text, f"Retired ID {retired_id} not code-referenced"
        print(f"  Verified retired rule {retired_id} documented in audit-module-05 per WP-15.")
    print("  -> PASS: All 97 active governed rules uniquely defined with single ownership and retired rules documented.")

def test_cross_traceability_chapter_4():
    print("\n=== 4. Checking Cross-Traceability Matrices (Chapter 4) ===")
    # Extract contract tags from 13-candidate-3A-xml.md
    c3a_text = CANDIDATE_3A.read_text(encoding="utf-8")
    contract_match = re.search(r"<apex_contract[^>]*>([\s\S]*?)</apex_contract>", c3a_text)
    assert contract_match, "Failed to extract <apex_contract> from 13-candidate-3A-xml.md"
    
    tag_names = re.findall(r"<([a-z_]+)(?:\s+[^>]*)*>", contract_match.group(1))
    unique_contract_tags = sorted(list(set(tag_names)))
    print(f"  Extracted {len(unique_contract_tags)} unique contract tags from 13-candidate-3A-xml.md:")
    print(f"  {unique_contract_tags}")
    assert len(unique_contract_tags) == 22, f"Expected 22 tags, got {len(unique_contract_tags)}"
    
    # Check that each file's Chapter 4 contains a traceability table with mapping to contract tags
    mapped_tags_across_audits = set()
    for fname in AUDIT_FILES:
        path = KB_DIR / fname
        text = path.read_text(encoding="utf-8")
        
        # Find Chapter 4 section
        ch4_match = re.search(r"## 4\.\s+Cross-Traceability Matrix[\s\S]*?(?=## 5\.|$)", text)
        assert ch4_match, f"Missing Chapter 4 in {fname}"
        ch4_text = ch4_match.group(0)
        
        # Check for contract tags in Chapter 4
        file_mapped_tags = set()
        for tag in unique_contract_tags:
            tag_xml = f"<{tag}>"
            if tag_xml in ch4_text:
                file_mapped_tags.add(tag)
                mapped_tags_across_audits.add(tag)
        print(f"  {fname}: Mapped {len(file_mapped_tags)} contract tags in Chapter 4")
        assert len(file_mapped_tags) > 0, f"No contract tags mapped in {fname}"
        
        # Check unmapped rules ledger exists in Chapter 4
        assert "Unmapped" in ch4_text or "unmapped" in ch4_text, (
            f"{fname} missing unmapped rules ledger/analysis in Chapter 4"
        )
        
    print(f"  Total unique contract tags mapped across all 5 audits: {len(mapped_tags_across_audits)}/22")
    assert len(mapped_tags_across_audits) == 22, (
        f"Missing contract tags across audit files: {set(unique_contract_tags) - mapped_tags_across_audits}"
    )
    print("  -> PASS: All 22 contract clauses bi-directionally traced across the 5 module audits.")

def test_link_integrity_and_no_file_urls():
    print("\n=== 5. Checking Link Resolution and Zero Machine-Specific Paths ===")
    link_re = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")
    bt = chr(96)
    fence_pattern = bt * 3 + r"[\s\S]*?" + bt * 3
    inline_pattern = bt + r"[^" + bt + r"\n]*" + bt
    
    total_links = 0
    broken_links = []
    abs_links = []
    
    for fname in AUDIT_FILES:
        content = (KB_DIR / fname).read_text(encoding="utf-8")
        clean_content = re.sub(inline_pattern, "", re.sub(fence_pattern, "", content))
        links = link_re.findall(clean_content)
        total_links += len(links)
        
        for title, link in links:
            link = link.strip()
            if link.startswith("file://") or ":\\" in link or ":/" in link:
                abs_links.append((fname, link))
            if link.startswith(("http://", "https://", "mailto:", "#")):
                continue
            tgt = link.split("#")[0].replace("%20", " ")
            if not tgt:
                continue
            if tgt.startswith("/"):
                target_path = (REPO_ROOT / tgt.lstrip("/")).resolve()
            else:
                target_path = (KB_DIR / tgt).resolve()
            if not target_path.exists():
                broken_links.append((fname, link, str(target_path)))
                
    print(f"  Total relative links checked: {total_links}")
    print(f"  Broken links: {len(broken_links)}")
    print(f"  Absolute links: {len(abs_links)}")
    assert len(broken_links) == 0, f"Broken links found: {broken_links}"
    assert len(abs_links) == 0, f"Machine-specific absolute links found: {abs_links}"
    print("  -> PASS: Zero broken links and zero machine-specific absolute links.")

if __name__ == "__main__":
    test_file_existence_and_sizes()
    test_chapter_structure_and_terminal_wp25()
    test_single_ownership_and_governed_rules()
    test_cross_traceability_chapter_4()
    test_link_integrity_and_no_file_urls()
    print("\n============================================================")
    print("ALL MILESTONE 4 AUDIT VERIFICATIONS PASSED 100%!")
    print("============================================================")
