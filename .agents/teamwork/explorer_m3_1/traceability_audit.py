#!/usr/bin/env python3
"""
traceability_audit.py — Traceability audit of <apex_contract v="1.0"> and related files.
"""

import re
import sys
from pathlib import Path

# Fix Windows console encoding
sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(r"c:\GitDev\apexai-os-meta")
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics"
V2_DIR = INFORMATICS_DIR / "Agent_Setup" / "NextIteration" / "v2-always-on-architecture"

def get_rule_details(fname):
    content = (INFORMATICS_DIR / fname).read_text(encoding="utf-8")
    rules = {}
    p1 = re.compile(r'^\s*-\s+\*\*([A-Z]{2}-\d{2})\s+\[(.*?)\]\s*(.*?)\*\*:\s*(.*)$', re.MULTILINE)
    for m in p1.finditer(content):
        rid, tag, title, body = m.groups()
        rules[rid] = {"file": fname, "tag": tag, "title": title.strip(), "body": body.strip()}
    p2 = re.compile(r'^#{2,4}\s+([A-Z]{2}-\d{2}):\s*(.*?)\n(.*?)(?=\n#{2,4}|\Z)', re.MULTILINE | re.DOTALL)
    for m in p2.finditer(content):
        rid, title, body = m.groups()
        if rid not in rules:
            rules[rid] = {"file": fname, "tag": "HEADER", "title": title.strip(), "body": body.strip()}
    return rules

all_rules = {}
for fn in [
    "writing-profile.md",
    "file-architecture.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
]:
    all_rules.update(get_rule_details(fn))

# Table claims from 13-candidate-3A-xml.md Section 3:
claims = [
    ("<target>", ["AD-01", "AD-02"]),
    ("<product_first>", ["AD-09", "AD-10"]),
    ("<scope>", ["AD-05", "AD-13"]),
    ("<communication>", ["WP-02", "WP-03", "WP-04", "WP-05"]),
    ("<hold_position>", ["AD-26"]),
    ("<ground>", ["AD-11", "AD-14", "AD-15"]),
    ("<reuse>", ["AD-12", "WP-23"]),
    ("<context>", ["AD-04", "EM-10"]),
    ("<recovery>", ["AD-07"]),
    ("<stop_repairing>", ["AD-06"]),
    ("<current_truth>", ["FA-02", "WP-08"]),
    ("<surgical> / <editing>", ["EM-03", "EM-08"]),
    ("<new_machinery> / <detour>", ["AD-10", "AD-13", "AD-25"]),
    ("<authoring>", ["WP-06", "WP-07", "WP-24", "WP-25", "FA-01", "FA-03", "FA-05"]),
    ("<trade_off>", ["EM-06", "EM-07"]),
    ("<handover>", ["EM-09"]),
    ("<iterative>", ["EM-10", "EM-11"]),
    ("<schemas>", ["GS-01", "GS-02", "GS-03", "GS-04", "GS-05", "GS-06"]),
    ("<sync>", ["EM-12"]),
    ("<pointers>", ["WP-25"]),
]

print("=== CHECKING SECTION 3 CLAIMS ===")
for tag, rids in claims:
    print(f"\nTag: {tag}")
    for rid in rids:
        if rid in all_rules:
            r = all_rules[rid]
            print(f"  {rid} [{r['file']}]: {r['title']}")
            print(f"    Body snippet: {r['body'][:120]}...")
        else:
            print(f"  {rid}: *** NOT FOUND ***")

print("\n" + "="*50)
print("=== DUMPING ALL ANTI-DRIFT RULES FOR COMPARISON ===")
for rid in sorted([k for k in all_rules if k.startswith("AD-")]):
    r = all_rules[rid]
    print(f"{rid} [{r['tag']}]: {r['title']}")
