"""Forensic verification script for Milestone 5 deliverables.
Independently verifies:
1. Carrier immutability and frozen research preservation.
2. Candidate 16-3A-ultra composition, formatting, and exact metrics.
3. 22 Option B block provenance between Layered Rule KB and Candidate 16.
4. Layered KB index and final/index.md link integrity and matrix coverage.
5. Detection of facades, dummy strings, placeholders, or hardcoded cheating.
"""

import os
import re
import sys
from pathlib import Path
from datetime import datetime

REPO_ROOT = Path(__file__).resolve().parents[3]
print(f"REPO_ROOT: {REPO_ROOT}")

try:
    import tiktoken
    ENC = tiktoken.get_encoding("cl100k_base")
except ImportError:
    print("WARNING: tiktoken not installed in this environment, falling back to None")
    ENC = None


def check_carrier_immutability():
    print("\n--- CHECK 1: Carrier Immutability ---")
    carriers = ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]
    today_start = datetime(2026, 10, 22, 0, 0, 0).timestamp()
    results = {}
    for c in carriers:
        p = REPO_ROOT / c
        assert p.is_file(), f"Carrier missing: {p}"
        mtime = p.stat().st_mtime
        mtime_dt = datetime.fromtimestamp(mtime)
        content = p.read_text(encoding="utf-8")
        
        # Check forbidden injections
        assert "<apex_contract" not in content, f"Injected <apex_contract> in {c}"
        assert "06-layered-rule-kb" not in content, f"Injected layered KB ref in {c}"
        assert "16-candidate-3A-ultra" not in content, f"Injected ultra ref in {c}"
        
        # Check modification time
        modified_today = mtime >= today_start
        results[c] = {
            "mtime": mtime_dt.isoformat(),
            "modified_today": modified_today,
            "size": p.stat().st_size,
        }
        print(f"  {c}: mtime={mtime_dt.isoformat()} | modified_today={modified_today} | size={p.stat().st_size} bytes")
        assert not modified_today, f"{c} was modified today ({mtime_dt.isoformat()})"
    print("PASS: Zero live carrier mutations today; no injected contracts.")
    return results


def check_frozen_research():
    print("\n--- CHECK 2: Frozen Research Directories ---")
    rdirs = [
        REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "01-universal-instruction-research",
        REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "03-research-of-file-10",
    ]
    today_start = datetime(2026, 10, 22, 0, 0, 0).timestamp()
    for rdir in rdirs:
        assert rdir.is_dir(), f"Research dir missing: {rdir}"
        files = [f for f in rdir.rglob("*") if f.is_file()]
        assert len(files) > 0, f"No files in {rdir}"
        latest_mtime = max(f.stat().st_mtime for f in files)
        latest_dt = datetime.fromtimestamp(latest_mtime)
        print(f"  {rdir.name}: {len(files)} files, latest mtime={latest_dt.isoformat()}")
        assert latest_mtime < today_start, f"File in {rdir.name} modified today: {latest_dt.isoformat()}"
    print("PASS: Frozen research directories 100% preserved (zero modifications).")


def check_candidate_16_metrics():
    print("\n--- CHECK 3: Candidate 16-3A-Ultra Metrics & Code Block ---")
    c16_path = REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "16-candidate-3A-ultra.md"
    assert c16_path.is_file(), f"16-candidate-3A-ultra.md missing: {c16_path}"
    raw = c16_path.read_text(encoding="utf-8")
    
    # Check frontmatter
    assert raw.startswith("---"), "Missing frontmatter start"
    fm_match = re.search(r"^---\n(.*?)\n---", raw, re.DOTALL)
    assert fm_match, "Failed to parse frontmatter"
    fm = fm_match.group(1)
    assert "id: V2-CANDIDATE-3A-ULTRA-v1.0" in fm, "Frontmatter ID mismatch"
    assert "type: Reference" in fm, "Frontmatter type mismatch"
    assert "status: current_candidate" in fm, "Frontmatter status mismatch"

    # Extract XML code block
    m = re.search(r"```xml\s*\n(.*?)\n```", raw, re.DOTALL)
    assert m, "No ```xml code block found in 16-candidate-3A-ultra.md"
    xml_block = m.group(1)

    # Recompute metrics on xml_block
    char_count = len(xml_block)
    word_count = len(xml_block.split())
    line_count = len(xml_block.splitlines())
    repo_tokens = char_count // 4
    bpe_tokens = len(ENC.encode(xml_block)) if ENC else None

    print(f"  Computed XML block metrics:")
    print(f"    Chars:       {char_count}")
    print(f"    Words:       {word_count}")
    print(f"    Lines:       {line_count}")
    print(f"    Repo tokens: {repo_tokens}")
    print(f"    BPE tokens:  {bpe_tokens}")

    # Verify against documented metrics
    assert char_count == 5917, f"Char count mismatch: {char_count} != 5917"
    assert word_count == 769, f"Word count mismatch: {word_count} != 769"
    assert line_count == 65, f"Line count mismatch: {line_count} != 65"
    assert repo_tokens == 1479, f"Repo token mismatch: {repo_tokens} != 1479"
    if bpe_tokens is not None:
        assert bpe_tokens == 1225, f"BPE token mismatch: {bpe_tokens} != 1225"

    print("PASS: Exact metric reproduction matches documented numbers 100%.")
    return xml_block, raw


def check_candidate_16_composition_and_provenance(xml_block):
    print("\n--- CHECK 4: Candidate 16 Composition & 22 Option B Blocks Provenance ---")
    kb_dir = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
    assert kb_dir.is_dir(), f"KB dir missing: {kb_dir}"

    expected_rules = [
        (1, "target"),
        (2, "product_first"),
        (3, "scope"),
        (4, "communication"),
        (5, "hold_position"),
        (6, "ground"),
        (7, "reuse"),
        (8, "context"),
        (9, "recovery"),
        (10, "stop_repairing"),
        (11, "current_truth"),
        (12, "surgical"),
        (13, "editing"),
        (14, "new_machinery"),
        (15, "detour"),
        (16, "authoring"),
        (17, "trade_off"),
        (18, "handover"),
        (19, "iterative"),
        (20, "schemas"),
        (21, "sync"),
        (22, "pointers"),
    ]

    # Check root tags
    assert xml_block.startswith('<apex_contract v="1.0-ultra" base_ref="apex-meta/informatics/">\n')
    assert xml_block.endswith('</apex_contract>')

    # Extract all tags in xml_block
    tag_matches = list(re.finditer(r'<([a-z_0-9]+)(?:\s+[^>]+)?>', xml_block))
    non_contract_tags = [m.group(1) for m in tag_matches if m.group(1) != "apex_contract"]
    expected_tag_names = [name for _, name in expected_rules]
    assert non_contract_tags == expected_tag_names, f"Tag sequence mismatch: {non_contract_tags} != {expected_tag_names}"
    print(f"  Verified all {len(expected_tag_names)} tags present in strict canonical order.")

    # Now verify each rule's Option B against its KB deep-dive file
    mismatches = []
    for num, tag_name in expected_rules:
        # Find corresponding file in kb_dir
        pattern = f"rule-{num:02d}-*.md"
        matches = list(kb_dir.glob(pattern))
        assert len(matches) == 1, f"Expected 1 match for {pattern}, found {len(matches)}"
        rf_path = matches[0]
        rf_text = rf_path.read_text(encoding="utf-8")

        # Find Option B text in Section 3 rollup table (Row 2)
        # Format is typically: | **2. Recommended Surgical Compression...** | `<tag>...</tag>` | ...
        opt_b_match = re.search(r"\|\s*\*\*2\.[^*]+\*\*\s*\|\s*`([^`]+)`", rf_text)
        if not opt_b_match:
            opt_b_match = re.search(r"\|\s*\*\*Option B[^*]*\*\*\s*\|\s*`([^`]+)`", rf_text)
        if not opt_b_match:
            opt_b_match = re.search(r"\|\s*\*\*2\.[^*]+\*\*\s*\|\s*```(?:xml)?\s*\n(.*?)\n```", rf_text, re.DOTALL)
        
        # Also extract tag block from candidate 16
        # Find <tag_name ...>...</tag_name>
        cand_tag_pattern = re.compile(rf'(<{tag_name}(?:\s+[^>]+)?>.*?</{tag_name}>)', re.DOTALL)
        cand_tag_match = cand_tag_pattern.search(xml_block)
        assert cand_tag_match, f"Could not find tag <{tag_name}> in 16-candidate-3A-ultra.md"
        cand_tag_content = cand_tag_match.group(1)

        # Normalize whitespace for comparison
        cand_clean = " ".join(cand_tag_content.split())

        assert opt_b_match, f"Could not find Option B rollup in {rf_path.name}"
        kb_opt_b = opt_b_match.group(1)
        kb_clean = " ".join(kb_opt_b.split())
        if cand_clean == kb_clean:
            print(f"  Rule {num:02d} ({tag_name}): EXACT match with Rollup Table Option B.")
        else:
            print(f"  Rule {num:02d} ({tag_name}): Normalized diff:")
            print(f"    cand: {cand_clean}")
            print(f"    kb:   {kb_clean}")
            assert cand_clean == kb_clean, f"Content mismatch in Rule {num:02d} ({tag_name})"

    print("PASS: All 22 rules traceable directly to Layered Rule KB deep dives.")


def check_indices_and_cross_references():
    print("\n--- CHECK 5: Index Files & Cross-References ---")
    kb_index = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb" / "index.md"
    final_index = REPO_ROOT / "apex-meta" / "informatics" / "final" / "index.md"

    assert kb_index.is_file(), f"KB index missing: {kb_index}"
    assert final_index.is_file(), f"Final index missing: {final_index}"

    kb_raw = kb_index.read_text(encoding="utf-8")
    final_raw = final_index.read_text(encoding="utf-8")

    # Verify kb_index links to all 22 rules
    for i in range(1, 23):
        assert f"rule-{i:02d}-" in kb_raw, f"KB index missing link to rule {i:02d}"
    print("  KB index links to all 22 rule files.")

    # Verify kb_index links to all 5 module audits
    for i in range(1, 6):
        assert f"audit-module-{i:02d}-" in kb_raw, f"KB index missing link to audit module {i:02d}"
    print("  KB index links to all 5 audit module files.")

    # Verify final_index references 16-candidate-3A-ultra.md and 06-layered-rule-kb
    assert "16-candidate-3A-ultra.md" in final_raw, "final/index.md missing 16-candidate-3A-ultra.md"
    assert "06-layered-rule-kb" in final_raw, "final/index.md missing 06-layered-rule-kb"
    assert "research/06-layered-rule-kb/index.md" in final_raw, "final/index.md missing link to KB index"

    # Verify all 22 rules hyperlinked in Section 3 matrix
    for i in range(1, 23):
        pattern = f"research/06-layered-rule-kb/rule-{i:02d}-"
        assert pattern in final_raw, f"final/index.md Section 3 matrix missing hyperlink for rule {i:02d}"
    print("  final/index.md Section 3 matrix hyperlinked to all 22 rule deep dives.")

    print("PASS: Index files and cross-references complete and verified.")


def check_anti_cheating_and_facades():
    print("\n--- CHECK 6: Anti-Cheating, Facade & Placeholder Scan ---")
    suspicious_patterns = [
        r"\bTODO\b", r"\bFIXME\b", r"\bTBD\b", r"\bXXX\b",
        r"\blorem ipsum\b", r"\bplaceholder\b", r"\bdummy\b",
        r"\bcoming soon\b", r"\[insert\s+"
    ]
    
    files_to_scan = [
        REPO_ROOT / "apex-meta" / "informatics" / "final" / "candidates" / "16-candidate-3A-ultra.md",
        REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb" / "index.md",
        REPO_ROOT / "apex-meta" / "informatics" / "final" / "index.md",
    ]

    for fpath in files_to_scan:
        content = fpath.read_text(encoding="utf-8")
        for pat in suspicious_patterns:
            matches = list(re.finditer(pat, content, re.IGNORECASE))
            if matches:
                # Check context to see if it's legit discussion (e.g. testing for dummy)
                for m in matches:
                    start = max(0, m.start() - 40)
                    end = min(len(content), m.end() + 40)
                    snippet = content[start:end].replace('\n', ' ')
                    print(f"  FLAG in {fpath.name}: '{m.group(0)}' at context: ...{snippet}...")
                    # Fail on actual unfinished placeholder
                    assert False, f"Unfinished placeholder detected: {m.group(0)} in {fpath.name}"
        print(f"  {fpath.name}: 0 placeholders or shortcut markers found.")

    print("PASS: No facade implementations or unfinished placeholders detected.")


if __name__ == "__main__":
    check_carrier_immutability()
    check_frozen_research()
    xml_block, c16_raw = check_candidate_16_metrics()
    check_candidate_16_composition_and_provenance(xml_block)
    check_indices_and_cross_references()
    check_anti_cheating_and_facades()
    print("\n=== ALL FORENSIC CHECKS PASSED: VERDICT = CLEAN ===")
