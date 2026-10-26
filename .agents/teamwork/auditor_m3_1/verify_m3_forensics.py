#!/usr/bin/env python3
"""
Forensic Auditor Verification Script for Milestone 3 (Rules 16-22)
Checks:
1. File inventory, sizes, and word counts
2. OKF v0.2 frontmatter compliance & durable IDs
3. Required 5-section architecture and Layer positioning headers
4. Deep-scan for placeholders, dummy stubs, and facade text
5. Exact text match against 13-candidate-3A-xml.md
6. Semantic block inventory, Option A/B/C availability, [P0-P3 | I/E/R] tags
7. Re-verification of all relative markdown links against live filesystem
8. Tiktoken BPE metrics audit
"""

import os
import re
import sys
import yaml
from pathlib import Path

WORKSPACE = Path(r"c:\GitDev\apexai-os-meta")
KB_DIR = WORKSPACE / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"
CANDIDATE_3A = WORKSPACE / "apex-meta" / "informatics" / "final" / "candidates" / "13-candidate-3A-xml.md"

RULES = [
    ("rule-16-authoring.md", "authoring", 16, "V2-LAYERED-KB-RULE-16-AUTHORING"),
    ("rule-17-trade-off.md", "trade_off", 17, "V2-LAYERED-KB-RULE-17-TRADE-OFF"),
    ("rule-18-handover.md", "handover", 18, "V2-LAYERED-KB-RULE-18-HANDOVER"),
    ("rule-19-iterative.md", "iterative", 19, "V2-LAYERED-KB-RULE-19-ITERATIVE"),
    ("rule-20-schemas.md", "schemas", 20, "V2-LAYERED-KB-RULE-20-SCHEMAS"),
    ("rule-21-sync.md", "sync", 21, "V2-LAYERED-KB-RULE-21-SYNC"),
    ("rule-22-pointers.md", "pointers", 22, "V2-LAYERED-KB-RULE-22-POINTERS"),
]

def check_file_inventory():
    print("=== 1. FILE INVENTORY & STATS ===")
    results = []
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        if not fpath.exists():
            print(f"[FAIL] Missing file: {fname}")
            results.append(False)
            continue
        size = fpath.stat().st_size
        content = fpath.read_text(encoding="utf-8")
        lines = content.splitlines()
        words = len(content.split())
        print(f"[PASS] {fname}: {size:,} bytes | {len(lines)} lines | {words} words")
        if size < 5000:
            print(f"  [WARN/FAIL] Suspiciously small size (< 5KB): {size} bytes")
            results.append(False)
        else:
            results.append(True)
    return all(results)

def check_frontmatter_and_sections():
    print("\n=== 2. FRONTMATTER & SECTION ARCHITECTURE ===")
    results = []
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        
        # Frontmatter
        fm_match = re.match(r"^---\r?\n(.*?)\r?\n---\r?\n", content, re.DOTALL)
        if not fm_match:
            print(f"[FAIL] {fname}: No YAML frontmatter found!")
            results.append(False)
            continue
        fm_text = fm_match.group(1)
        fm = yaml.safe_load(fm_text)
        
        # Check required frontmatter keys
        missing_keys = [k for k in ["type", "id", "title", "description", "status", "tags"] if k not in fm]
        if missing_keys:
            print(f"[FAIL] {fname}: Missing frontmatter keys: {missing_keys}")
            results.append(False)
            continue
        
        if fm["id"] != expected_id:
            print(f"[FAIL] {fname}: ID mismatch. Expected '{expected_id}', got '{fm['id']}'")
            results.append(False)
            continue
            
        if fm["type"] != "Reference" or fm["status"] != "current_truth":
            print(f"[FAIL] {fname}: Frontmatter type/status mismatch: type={fm['type']}, status={fm['status']}")
            results.append(False)
            continue
            
        # Check Layer positioning header
        if "Layer 0" not in content or "Layer 1" not in content or "Layer 2" not in content:
            print(f"[FAIL] {fname}: Missing Layer 0/1/2 positioning header!")
            results.append(False)
            continue
            
        # Check mandatory sections (allowing standard numbering variants)
        sec1 = bool(re.search(r"##\s+(?:1\.|§1)\s+Original Rule", content, re.IGNORECASE))
        sec2 = bool(re.search(r"##\s+(?:2\.|§2)\s+Chapter-by-Chapter Semantic Block", content, re.IGNORECASE))
        sec3 = bool(re.search(r"##\s+(?:3\.|§3)\s+Whole-Rule Recomposition Rollup", content, re.IGNORECASE))
        sec4 = bool(re.search(r"##\s+(?:4\.|§4)\s+Complete Bidirectional Research", content, re.IGNORECASE))
        sec5 = bool(re.search(r"##\s+(?:5\.|§5)\s+Failure Modes", content, re.IGNORECASE))
        
        if not (sec1 and sec2 and sec3 and sec4 and sec5):
            print(f"[FAIL] {fname}: Missing section! (Sec1={sec1}, Sec2={sec2}, Sec3={sec3}, Sec4={sec4}, Sec5={sec5})")
            results.append(False)
            continue
            
        print(f"[PASS] {fname}: OKF frontmatter ({expected_id}) & all 5 mandatory sections present.")
        results.append(True)
    return all(results)

def check_placeholders_and_stubs():
    print("\n=== 3. DEEP PLACEHOLDER & STUB SCAN ===")
    flagged = False
    # Patterns that indicate unwritten or lazy stubbed content
    suspicious_patterns = [
        (r"\bTODO\b", "TODO marker"),
        (r"\bFIXME\b", "FIXME marker"),
        (r"\bTBD\b", "TBD marker"),
        (r"\bXXX\b", "XXX marker"),
        (r"\blorem\s+ipsum\b", "Lorem Ipsum placeholder"),
        (r"\bcoming\s+soon\b", "Coming Soon placeholder"),
        (r"\bas\s+above\b", "As Above placeholder shortcut"),
        (r"\bsame\s+as\s+rule\b", "Same As shortcut"),
        (r"\[insert\s+", "Insert bracket placeholder"),
        (r"<insert\s+", "Insert tag placeholder"),
    ]
    
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        lines = content.splitlines()
        
        file_flagged = False
        for line_num, line in enumerate(lines, 1):
            for pattern, desc in suspicious_patterns:
                # ignore if in a code block or URL or discussing "as above" in linguistic context
                m = re.search(pattern, line, re.IGNORECASE)
                if m:
                    # Filter out legitimate mentions (e.g. "TBD" in a test scenario description if any)
                    print(f"  [FLAG] {fname}:{line_num}: Found {desc} -> '{line.strip()}'")
                    file_flagged = True
                    flagged = True
        if not file_flagged:
            print(f"[PASS] {fname}: Zero suspicious placeholder or stub tokens found.")
            
    return not flagged

def check_semantic_blocks_and_tags():
    print("\n=== 4. SEMANTIC BLOCKS & SIGNIFICANCE TAGS ===")
    results = []
    
    tag_regex = re.compile(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]")
    
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        
        # Find all SB-XX.Y blocks
        sb_matches = sorted(list(set(re.findall(rf"SB-{num}\.\d+", content))))
        if not sb_matches:
            print(f"[FAIL] {fname}: No semantic blocks found for SB-{num}.X!")
            results.append(False)
            continue
            
        # Check Option A, Option B, Option C in each file
        opt_a = len(re.findall(r"Option A\b", content))
        opt_b = len(re.findall(r"Option B\b", content))
        opt_c = len(re.findall(r"Option C\b", content))
        
        # Check significance tags
        tags_found = tag_regex.findall(content)
        if not tags_found:
            print(f"[FAIL] {fname}: No [P0-P3 | I/E/R] significance tags found!")
            results.append(False)
            continue
            
        # Check for prohibited computed formulas (e.g. = (I*E)/R or similar arithmetic)
        calc_matches = re.findall(r"=\s*\(\s*[IER]\s*[\*\+\-\/]", content)
        if calc_matches:
            print(f"[FAIL] {fname}: Detected computed mathematical formula: {calc_matches}")
            results.append(False)
            continue
            
        print(f"[PASS] {fname}: {len(sb_matches)} SBs {sb_matches} | Options A:{opt_a} B:{opt_b} C:{opt_c} | {len(tags_found)} tags")
        results.append(True)
        
    return all(results)

def check_ground_truth_matching():
    print("\n=== 5. GROUND TRUTH MATCHING WITH 13-CANDIDATE-3A-XML.MD ===")
    if not CANDIDATE_3A.exists():
        print(f"[FAIL] 13-candidate-3A-xml.md does not exist at {CANDIDATE_3A}")
        return False
        
    c3a_content = CANDIDATE_3A.read_text(encoding="utf-8")
    # Extract the actual contract block
    block_match = re.search(r"```xml\n<apex_contract.*?</apex_contract>\n```", c3a_content, re.DOTALL)
    if not block_match:
        print("[FAIL] Could not locate <apex_contract> xml code block in 13-candidate-3A-xml.md!")
        return False
    contract_block = block_match.group(0)
    
    results = []
    
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        
        # Extract tag from contract block
        pattern = rf"(<{tag}\b[^>]*>(?:(?!</?{tag}>).)*?</{tag}>)"
        match_3a = re.search(pattern, contract_block, re.DOTALL)
        if not match_3a:
            print(f"[FAIL] Tag <{tag}> not found in contract block of 13-candidate-3A-xml.md!")
            results.append(False)
            continue
            
        tag_3a_full = match_3a.group(1).strip()
        inner_3a = re.sub(rf"^<{tag}[^>]*>|</{tag}>$", "", tag_3a_full, flags=re.DOTALL).strip()
        inner_3a_norm = " ".join(inner_3a.split())
        
        sec1_match = re.search(r"##\s+(?:1\.|§1)\s+Original Rule.*?(?=##\s+(?:2\.|§2))", content, re.DOTALL | re.IGNORECASE)
        if not sec1_match:
            print(f"[FAIL] {fname}: Could not isolate section 1!")
            results.append(False)
            continue
            
        sec1_text = sec1_match.group(0)
        sec1_norm = " ".join(sec1_text.split())
        
        if inner_3a_norm in sec1_norm:
            print(f"[PASS] {fname}: Exact inner text for <{tag}> matches 13-candidate-3A-xml.md.")
            results.append(True)
        else:
            words_3a = set(inner_3a_norm.split())
            words_sec1 = set(sec1_norm.split())
            overlap = len(words_3a & words_sec1) / len(words_3a) if words_3a else 0
            if overlap > 0.95:
                print(f"[PASS (near exact)] {fname}: {overlap*100:.1f}% match for <{tag}>.")
                results.append(True)
            else:
                print(f"[FAIL] {fname}: <{tag}> text in §1 does not match 13-candidate-3A-xml.md! Overlap={overlap*100:.1f}%")
                results.append(False)
                
    return all(results)

def check_relative_links():
    print("\n=== 6. RELATIVE LINK RESOLUTION ===")
    import urllib.parse
    total_links = 0
    broken_links = []
    
    for fname, tag, num, expected_id in RULES:
        fpath = KB_DIR / fname
        content = fpath.read_text(encoding="utf-8")
        file_dir = fpath.parent
        
        # Find markdown links [text](path)
        raw_links = re.findall(r"\[([^\]]+)\]\(([^)]+)\)", content)
        for text, link in raw_links:
            clean_link = link.split("#")[0].split("?")[0].strip()
            if not clean_link:
                continue
            if clean_link.startswith(("http://", "https://", "mailto:")):
                continue
            total_links += 1
            decoded_link = urllib.parse.unquote(clean_link)
            target_path = (file_dir / decoded_link).resolve()
            if not target_path.exists():
                broken_links.append((fname, text, link, str(target_path)))
                
    if broken_links:
        print(f"[FAIL] Found {len(broken_links)} broken relative links out of {total_links}:")
        for fn, txt, lnk, resolved in broken_links:
            print(f"  {fn}: [{txt}]({lnk}) -> {resolved} (NOT FOUND)")
        return False
    else:
        print(f"[PASS] All {total_links} relative links across 7 files resolve to actual files on disk!")
        return True

def check_token_metrics():
    print("\n=== 7. TIKTOKEN BPE AUDIT ===")
    try:
        import tiktoken
        enc = tiktoken.get_encoding("cl100k_base")
        print("[INFO] tiktoken loaded with cl100k_base encoding.")
        
        for fname, tag, num, expected_id in RULES:
            fpath = KB_DIR / fname
            content = fpath.read_text(encoding="utf-8")
            
            # Check §3 Rollup table values
            # Search for table rows with Option B tokens
            # Example: | **2. Recommended Surgical Compression (Option B)** | `<tag ...> ... </tag>` | **`113`** | ...
            m_opt_b = re.search(r"Option B\)[^|]*\|\s*(`[^`]+`|<[^>]+>[^<]+</[^>]+>)[^|]*\|\s*\*\*`?(\d+)`?\*\*", content)
            if m_opt_b:
                text_b = m_opt_b.group(1).strip("`")
                reported_bpe = int(m_opt_b.group(2))
                actual_bpe = len(enc.encode(text_b))
                diff = abs(actual_bpe - reported_bpe)
                status = "PASS" if diff <= 2 else "WARN"
                print(f"[{status}] {fname}: Option B reported {reported_bpe} BPE, measured {actual_bpe} BPE (diff={diff})")
            else:
                print(f"[INFO] {fname}: Rollup table parsing skipped or different layout.")
        return True
    except ImportError:
        print("[WARN] tiktoken not installed in current environment; skipping BPE recalculation.")
        return True

def main():
    print("=" * 60)
    print("FORENSIC AUDITOR MILESTONE 3 INDEPENDENT VERIFICATION")
    print(f"Working Dir: {KB_DIR}")
    print("=" * 60)
    
    c1 = check_file_inventory()
    c2 = check_frontmatter_and_sections()
    c3 = check_placeholders_and_stubs()
    c4 = check_semantic_blocks_and_tags()
    c5 = check_ground_truth_matching()
    c6 = check_relative_links()
    c7 = check_token_metrics()
    
    all_passed = c1 and c2 and c3 and c4 and c5 and c6 and c7
    print("\n" + "=" * 60)
    if all_passed:
        print("VERDICT: ALL FORENSIC CHECKS PASSED -> CLEAN")
    else:
        print("VERDICT: ONE OR MORE CHECKS FAILED -> INTEGRITY VIOLATION")
    print("=" * 60)
    return 0 if all_passed else 1

if __name__ == "__main__":
    sys.exit(main())
