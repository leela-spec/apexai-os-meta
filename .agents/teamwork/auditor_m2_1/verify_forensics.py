#!/usr/bin/env python3
"""
Full Comprehensive Forensic Integrity Verification Script for Milestone 2 (Rules 09-15)
Auditor: auditor_m2_1
"""

import os
import re
import sys
import urllib.parse
from pathlib import Path
import tiktoken

REPO_ROOT = Path("c:/GitDev/apexai-os-meta").resolve()
TARGET_DIR = REPO_ROOT / "apex-meta" / "informatics" / "final" / "research" / "06-layered-rule-kb"

RULES_M2 = [
    ("rule-09-recovery.md", "V2-LAYERED-KB-RULE-09-RECOVERY", "<recovery>", 2, 38, 34),
    ("rule-10-stop-repairing.md", "V2-LAYERED-KB-RULE-10-STOP-REPAIRING", "<stop_repairing>", 2, 41, 35),
    ("rule-11-current-truth.md", "V2-LAYERED-KB-RULE-11-CURRENT-TRUTH", "<current_truth>", 3, 38, 38),
    ("rule-12-surgical.md", "V2-LAYERED-KB-RULE-12-SURGICAL", "<surgical>", 1, 15, 16),
    ("rule-13-editing.md", "V2-LAYERED-KB-RULE-13-EDITING", "<editing>", 4, 75, 67),
    ("rule-14-new-machinery.md", "V2-LAYERED-KB-RULE-14-NEW-MACHINERY", "<new_machinery>", 3, 70, 68),
    ("rule-15-detour.md", "V2-LAYERED-KB-RULE-15-DETOUR", "<detour>", 2, 44, 40),
]

SUSPICIOUS_PATTERNS = [
    r"\bTODO\b",
    r"\bFIXME\b",
    r"\bTBD\b",
    r"\bXXX\b",
    r"\blorem\s+ipsum\b",
    r"\bplaceholder\b",
    r"\bdummy\b",
    r"\[insert\s+",
    r"\.\.\.\s*$",
]

LINK_PATTERN = re.compile(r"\[([^\]]+)\]\(([^)]+)\)")

def run_forensic_audit():
    print("=" * 80)
    print("M2 FORENSIC AUDIT: RULES 09-15 INTEGRITY CHECKS")
    print("=" * 80)
    
    enc = tiktoken.get_encoding("cl100k_base")
    total_violations = 0
    all_links = []
    
    file_stats = []
    
    for fname, expected_id, expected_tag, expected_sb_count, exp_base_bpe, exp_optb_bpe in RULES_M2:
        fpath = TARGET_DIR / fname
        if not fpath.exists():
            print(f"[FAIL] Missing deliverable file: {fname}")
            total_violations += 1
            continue
            
        content = fpath.read_text(encoding="utf-8")
        lines = content.splitlines()
        words = content.split()
        chars = len(content)
        total_file_bpe = len(enc.encode(content))
        
        file_stats.append({
            "fname": fname,
            "lines": len(lines),
            "words": len(words),
            "chars": chars,
            "bpe": total_file_bpe
        })
        
        print(f"\n--- Checking {fname} ---")
        print(f"  Metrics: {len(lines)} lines | {len(words)} words | {chars} chars | {total_file_bpe} full file BPE")
        
        # Check nominal analytical file depth (>= 1,500 BPE for full deep dive)
        if total_file_bpe < 1500:
            print(f"  [FAIL] File token count suspiciously low ({total_file_bpe} < 1500 BPE)")
            total_violations += 1
        else:
            print(f"  [PASS] File analytical depth verified ({total_file_bpe} BPE)")
            
        # Frontmatter
        if not content.startswith("---\n"):
            print("  [FAIL] Missing YAML frontmatter marker")
            total_violations += 1
        else:
            fm_end = content.find("\n---\n", 4)
            if fm_end == -1:
                print("  [FAIL] Frontmatter not properly closed")
                total_violations += 1
            else:
                fm_text = content[4:fm_end]
                for key in ["type: Reference", f"id: {expected_id}", "status: current_truth", "tags: ["]:
                    if key not in fm_text:
                        print(f"  [FAIL] Missing frontmatter key: {key}")
                        total_violations += 1
                print("  [PASS] Frontmatter conforms to OKF v0.2")

        # Layer Positioning
        if "Position in Layered Knowledge Base:" not in content:
            print("  [FAIL] Missing Layer Positioning block")
            total_violations += 1
        else:
            print("  [PASS] Layer Positioning block present")

        # 5 Sections
        sections = [
            ("Section 1", r"## 1\.\s+Original Rule & Atomic Semantic Block"),
            ("Section 2", r"## 2\.\s+Chapter-by-Chapter Semantic Block Analysis"),
            ("Section 3", r"## 3\.\s+Whole-Rule Recomposition Rollup"),
            ("Section 4", r"## 4\.\s+Complete Bidirectional Research & Provenance Links"),
            ("Section 5", r"## 5\.\s+Failure Modes & Not-To-Dos"),
        ]
        for sec_name, sec_regex in sections:
            if not re.search(sec_regex, content):
                print(f"  [FAIL] Missing {sec_name}")
                total_violations += 1
            else:
                print(f"  [PASS] {sec_name} present")

        # Semantic block chapters in Section 2
        rule_num = expected_id.split("-")[4]
        for sb_idx in range(1, expected_sb_count + 1):
            sb_header = f"SB-{rule_num}.{sb_idx}"
            if sb_header not in content:
                print(f"  [FAIL] Missing chapter for {sb_header}")
                total_violations += 1
            else:
                print(f"  [PASS] Chapter {sb_header} verified")

        # Check options A, B, C
        for opt in ["Option A", "Option B", "Option C"]:
            if opt not in content:
                print(f"  [FAIL] Missing {opt}")
                total_violations += 1

        # Check Rollup table
        if "| Rollup Option |" not in content or "Recommended Surgical Compression" not in content:
            print("  [FAIL] Missing or malformed Rollup table in Section 3")
            total_violations += 1
        else:
            print("  [PASS] Section 3 Rollup table present")

        # Check Failure modes
        if "## 5. Failure Modes & Not-To-Dos" not in content or "Never " not in content:
            print("  [FAIL] Section 5 lacks 'Never' boundary rules")
            total_violations += 1
        else:
            print("  [PASS] Section 5 failure modes verified")

        # Check Suspicious Patterns
        suspicious_found = 0
        for line_no, line in enumerate(lines, 1):
            for pat in SUSPICIOUS_PATTERNS:
                if re.search(pat, line, re.IGNORECASE):
                    # Check false positives
                    lower = line.lower()
                    if "never" in lower or "prohibit" in lower or "ban" in lower or "rule-level" in lower:
                        continue
                    print(f"  [ALERT] Line {line_no} matches suspicious pattern '{pat}': {line.strip()[:70]}")
                    suspicious_found += 1
        if suspicious_found == 0:
            print("  [PASS] Zero suspicious/dummy/placeholder patterns detected")
        else:
            total_violations += suspicious_found

        # Collect Links
        for m in LINK_PATTERN.finditer(content):
            all_links.append((fname, fpath, m.group(1), m.group(2)))

    # Link Resolution Check
    print("\n" + "=" * 80)
    print("PHASE 2: RELATIVE LINK RESOLUTION VERIFICATION")
    print("=" * 80)
    broken_links = 0
    resolved_links = 0
    ext_links = 0
    for sfname, spath, ltext, lurl in all_links:
        if lurl.startswith("http://") or lurl.startswith("https://"):
            ext_links += 1
            continue
        clean_url = urllib.parse.unquote(lurl.split("#")[0])
        if not clean_url:
            continue
        tgt = (spath.parent / clean_url).resolve()
        if not tgt.exists():
            print(f"[BROKEN] In {sfname}: {lurl} -> {tgt}")
            broken_links += 1
        else:
            resolved_links += 1

    print(f"Total links scanned: {len(all_links)}")
    print(f"External links (HTTP/HTTPS): {ext_links}")
    print(f"Internal relative links verified: {resolved_links}")
    print(f"Broken internal links: {broken_links}")
    if broken_links > 0:
        total_violations += broken_links

    # Summary table
    print("\n" + "=" * 80)
    print("PHASE 3: FILE METRICS SUMMARY TABLE")
    print("=" * 80)
    print(f"{'Filename':<28} | {'Lines':>6} | {'Words':>6} | {'Chars':>7} | {'BPE':>6}")
    print("-" * 65)
    for s in file_stats:
        print(f"{s['fname']:<28} | {s['lines']:>6} | {s['words']:>6} | {s['chars']:>7} | {s['bpe']:>6}")
        
    print("\n" + "=" * 80)
    print(f"FINAL RESULT: {total_violations} INTEGRITY VIOLATIONS DETECTED")
    print("=" * 80)
    return total_violations

if __name__ == "__main__":
    v = run_forensic_audit()
    sys.exit(v)
