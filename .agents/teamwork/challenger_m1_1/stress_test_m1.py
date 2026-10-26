#!/usr/bin/env python3
"""
stress_test_m1.py — Empirical Adversarial Stress Test Suite for Milestone 1.

Authored by M1 Challenger 1 (critic, specialist).
Performs white-box and black-box stress tests on:
- apex-meta/informatics/Agent_Setup/index.md
- apex-meta/informatics/file-architecture.md
- apex-meta/informatics/writing-profile.md
- apex-meta/informatics/execution-modes.md
"""

from __future__ import annotations

import os
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

REPO_ROOT = Path("c:/GitDev/apexai-os-meta").resolve()
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics"
SCRIPTS_DIR = REPO_ROOT / "apex-meta" / "scripts"

if str(SCRIPTS_DIR) not in sys.path:
    sys.path.insert(0, str(SCRIPTS_DIR))

import okf_validator

TARGET_FILES = {
    "agent_setup": INFORMATICS_DIR / "Agent_Setup" / "index.md",
    "file_arch": INFORMATICS_DIR / "file-architecture.md",
    "writing_profile": INFORMATICS_DIR / "writing-profile.md",
    "execution_modes": INFORMATICS_DIR / "execution-modes.md",
}


def estimate_tokens(text: str) -> int:
    """Standard token estimation heuristic (~4 chars per token)."""
    return max(1, len(text) // 4) if text else 0


def test_yaml_frontmatter_resilience():
    print("=== TEST 1: YAML Frontmatter Parser Resilience ===")
    results = {}
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            results[key] = {"status": "FAIL", "error": "File does not exist"}
            continue
        content = path.read_text(encoding="utf-8")
        
        # 1. Check opening delimiter
        if not content.startswith("---"):
            results[key] = {"status": "FAIL", "error": "No opening '---'"}
            continue
            
        # 2. Check closing delimiter
        parts = content.split("---", 2)
        if len(parts) < 3:
            results[key] = {"status": "FAIL", "error": "Unterminated frontmatter"}
            continue
            
        fm_raw = parts[1]
        lines = fm_raw.splitlines()
        line_errors = []
        for idx, line in enumerate(lines, start=2):
            line_str = line.strip()
            if not line_str or line_str.startswith("#"):
                continue
            if ":" not in line_str:
                line_errors.append(f"Line {idx} missing colon: '{line_str}'")
            if line_str.startswith("-"):
                line_errors.append(f"Line {idx} uses multiline list syntax: '{line_str}'")
                
        fm_dict, body, err = okf_validator.parse_frontmatter(content)
        
        results[key] = {
            "status": "PASS" if not err and not line_errors else "FAIL",
            "err": err,
            "line_errors": line_errors,
            "parsed_keys": list(fm_dict.keys()) if fm_dict else [],
            "fm_dict": fm_dict,
        }
        print(f"[{'PASS' if not err and not line_errors else 'FAIL'}] {rel}")
        if err or line_errors:
            print(f"   Parser Error: {err}")
            print(f"   Line Errors: {line_errors}")
        else:
            print(f"   Parsed Keys: {list(fm_dict.keys())}")
            if "type" in fm_dict:
                print(f"   Type: {fm_dict.get('type')}")
            if "okf_version" in fm_dict:
                print(f"   OKF Version: {fm_dict.get('okf_version')}")
    return results


def test_significance_tag_syntax_and_ranking():
    print("\n=== TEST 2: Significance Tag Syntax & Ranking Compliance ===")
    # Exact strict regex
    STRICT_TAG_REGEX = re.compile(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]")
    
    # Loose regex to catch malformed tags
    LOOSE_TAG_REGEX = re.compile(r"\[([pP]?\d|[a-zA-Z0-9]+)\s*\|?\s*([^\]]+)\]")
    
    # Mathematical formula check
    FORMULA_PATTERNS = [
        re.compile(r"\bScore\s*="),
        re.compile(r"\bE\[V\]"),
        re.compile(r"\(I\s*[*+]\s*E\)\s*/\s*R"),
        re.compile(r"I\s*\*\s*E"),
        re.compile(r"=\s*\d+\.\d+"),
    ]
    
    rank_order = {"P0": 0, "P1": 1, "P2": 2, "P3": 3}
    
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        
        # Exclude code blocks from tag counting
        content_no_code = re.sub(r"```[\s\S]*?```", "", content)
        
        strict_matches = list(STRICT_TAG_REGEX.finditer(content_no_code))
        
        print(f"\nChecking: {rel}")
        print(f"Found {len(strict_matches)} strict significance tags.")
        
        tier_counts = {"P0": 0, "P1": 0, "P2": 0, "P3": 0}
        parsed_tags = []
        
        for m in strict_matches:
            tier, i_str, e_str, r_str = m.groups()
            i_val, e_val, r_val = int(i_str), int(e_str), int(r_str)
            tier_counts[tier] += 1
            parsed_tags.append((tier, i_val, e_val, r_val, m.group(0), m.start()))
            
            # Check range
            if not (1 <= i_val <= 100):
                print(f"   [BUG] Impact out of range (1-100): {i_val} in {m.group(0)}")
            if not (1 <= e_val <= 100):
                print(f"   [BUG] Evidence out of range (1-100): {e_val} in {m.group(0)}")
            if not (1 <= r_val <= 100):
                print(f"   [BUG] Risk out of range (1-100): {r_val} in {m.group(0)}")
                
        print(f"Tier Breakdown: {tier_counts}")
        
        # Check priority order
        inversions = []
        for i in range(len(parsed_tags) - 1):
            curr_tier = parsed_tags[i][0]
            next_tier = parsed_tags[i+1][0]
            if rank_order[curr_tier] > rank_order[next_tier]:
                inversions.append((parsed_tags[i], parsed_tags[i+1]))
                
        if inversions:
            print(f"   [FAIL] Inverted priority order detected:")
            for inv in inversions:
                print(f"      {inv[0][0]} ({inv[0][4]}) appears BEFORE {inv[1][0]} ({inv[1][4]})")
        else:
            print(f"   [PASS] Strictly non-decreasing rank order (P0 -> P1 -> P2 -> P3)")
            
        # Check for formula patterns
        formula_hits = []
        for pat in FORMULA_PATTERNS:
            hits = pat.findall(content_no_code)
            if hits:
                formula_hits.extend(hits)
        if formula_hits:
            print(f"   [WARNING/BUG] Possible mathematical formula detected: {formula_hits}")
        else:
            print(f"   [PASS] Zero calculated formulas detected in body text.")


def test_first_500_tokens_primacy():
    print("\n=== TEST 3: Attention Primacy (First 500 Tokens) ===")
    STRICT_TAG_REGEX = re.compile(r"\[(P[0-3])\s*\|\s*I(\d{1,3})/E(\d{1,3})/R(\d{1,3})\]")
    
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        total_tokens = estimate_tokens(content)
        
        # Find all P0 tags
        p0_matches = [m for m in STRICT_TAG_REGEX.finditer(content) if m.group(1) == "P0"]
        
        print(f"\nFile: {rel} (Total tokens: ~{total_tokens})")
        if not p0_matches:
            print("   No P0 invariants in this file.")
            continue
            
        first_p0 = p0_matches[0]
        first_p0_token = estimate_tokens(content[:first_p0.start()])
        last_p0 = p0_matches[-1]
        last_p0_token = estimate_tokens(content[:last_p0.start()])
        
        print(f"   First P0 tag: '{first_p0.group(0)}' at character {first_p0.start()} (~token {first_p0_token})")
        print(f"   Last P0 tag:  '{last_p0.group(0)}' at character {last_p0.start()} (~token {last_p0_token})")
        
        if first_p0_token <= 500:
            print(f"   [PASS] First P0 is well within first 500 tokens ({first_p0_token} <= 500).")
        else:
            print(f"   [FAIL] First P0 is delayed beyond 500 tokens ({first_p0_token} > 500).")
            
        # Check all P0 tags positions
        for idx, m in enumerate(p0_matches):
            t_pos = estimate_tokens(content[:m.start()])
            status = "PASS" if t_pos <= 500 else "BEYOND_500"
            print(f"      P0 #{idx+1}: {m.group(0)} at ~token {t_pos} [{status}]")


def test_markdown_ast_and_prose_ergonomics():
    print("\n=== TEST 4: Markdown AST & Prose Ergonomics ===")
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        
        # 1. Heading depth analysis
        headings = []
        for line_num, line in enumerate(content.splitlines(), start=1):
            if line.strip().startswith("#"):
                clean = line.strip()
                depth = len(clean) - len(clean.lstrip("#"))
                title = clean.lstrip("#").strip()
                headings.append((line_num, depth, title))
                
        h4_plus = [h for h in headings if h[1] > 3]
        print(f"\nFile: {rel}")
        print(f"   Total headings: {len(headings)}")
        print(f"   Heading distribution: H1={len([h for h in headings if h[1]==1])}, H2={len([h for h in headings if h[1]==2])}, H3={len([h for h in headings if h[1]==3])}, H4+={len(h4_plus)}")
        if h4_plus:
            print(f"   [INFO] Found {len(h4_plus)} H4+ headings (Advisory / WP-P2-02 guideline):")
            for h in h4_plus[:5]:
                print(f"      Line {h[0]}: {'#'*h[1]} {h[2]}")
            if len(h4_plus) > 5:
                print(f"      ... and {len(h4_plus)-5} more.")
        else:
            print(f"   [PASS] All headings <= H3 (depth <= 3)")

        # 2. Sentence length checks
        long_sentences = okf_validator.check_writing_style(rel, content)
        if long_sentences:
            print(f"   [ADVISORY] {len(long_sentences)} sentences exceed recommended 30 words:")
            for s in long_sentences[:3]:
                print(f"      {s.message}")
        else:
            print(f"   [PASS] 0 sentences exceed 30 words.")


def test_link_integrity():
    print("\n=== TEST 5: Link Integrity Across Files ===")
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        links = okf_validator.extract_links(content)
        print(f"\nFile: {rel}")
        print(f"   Found {len(links)} relative markdown links.")
        broken = []
        for l in links:
            # Resolve relative to parent dir
            target = (path.parent / l).resolve()
            if not target.exists():
                broken.append((l, str(target)))
        if broken:
            print(f"   [FAIL] {len(broken)} broken link(s) found:")
            for b in broken:
                print(f"      Link '{b[0]}' -> Unresolved '{b[1]}'")
        else:
            print(f"   [PASS] All {len(links)} links resolve successfully.")


def test_durable_id_uniqueness():
    print("\n=== TEST 6: Durable ID Uniqueness & Existence ===")
    durable_ids = {}
    for key, path in TARGET_FILES.items():
        rel = path.relative_to(REPO_ROOT).as_posix()
        if not path.exists():
            continue
        content = path.read_text(encoding="utf-8")
        fm, _, _ = okf_validator.parse_frontmatter(content)
        if fm and "id" in fm:
            doc_id = str(fm["id"]).strip()
            if doc_id in durable_ids:
                print(f"   [FAIL] Duplicate ID '{doc_id}' in {rel} (already in {durable_ids[doc_id]})")
            else:
                durable_ids[doc_id] = rel
                print(f"   [PASS] {rel} defines unique ID '{doc_id}'")
        else:
            print(f"   [INFO] {rel} does not define 'id' field in frontmatter (optional in root/index)")


def test_adversarial_parser_injection():
    print("\n=== TEST 7: Adversarial Parser Stress & Edge Case Mutations ===")
    # Stress-test okf_validator.parse_frontmatter on tricky syntaxes
    cases = [
        ("Trailing space after ---", "---  \ntype: Profile\n---\nBody", True),
        ("Colon in value string", '---\ntype: Profile\ndescription: "Foo: Bar: Baz"\n---\nBody', True),
        ("Inline array with spaces", "---\ntype: Profile\ntags: [ a , b , c ]\n---\nBody", True),
        ("Inline dictionary mapping", "---\ntype: Profile\nmeta: { foo: bar }\n---\nBody", True),
        ("Unclosed quote in value", '---\ntype: "Profile\n---\nBody', True),
        ("Empty value", "---\ntype:\n---\nBody", True),
        ("Multiline YAML list (forbidden)", "---\ntype: Profile\ntags:\n  - a\n  - b\n---\nBody", False),
        ("CRLF Windows line endings", "---\r\ntype: Profile\r\ntitle: Windows File\r\n---\r\nBody", True),
    ]
    
    passed_cases = 0
    for name, content, expected_success in cases:
        fm, body, err = okf_validator.parse_frontmatter(content)
        success = (err is None)
        if success == expected_success:
            print(f"   [PASS] {name} -> success={success} (expected {expected_success})")
            passed_cases += 1
        else:
            print(f"   [FAIL] {name} -> success={success} (expected {expected_success}, err={err})")


if __name__ == "__main__":
    test_yaml_frontmatter_resilience()
    test_significance_tag_syntax_and_ranking()
    test_first_500_tokens_primacy()
    test_markdown_ast_and_prose_ergonomics()
    test_link_integrity()
    test_durable_id_uniqueness()
    test_adversarial_parser_injection()
