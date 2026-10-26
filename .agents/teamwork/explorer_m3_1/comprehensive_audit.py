#!/usr/bin/env python3
"""
comprehensive_audit.py — Deep audit of rule IDs, references, links, and cross-file consistency.
"""

import re
import sys
from pathlib import Path

sys.stdout.reconfigure(encoding="utf-8")

REPO_ROOT = Path(r"c:\GitDev\apexai-os-meta")
INFORMATICS_DIR = REPO_ROOT / "apex-meta" / "informatics"
V2_DIR = INFORMATICS_DIR / "Agent_Setup" / "NextIteration" / "v2-always-on-architecture"
DOSSIER_DIR = V2_DIR / "FinalizationDossier"

RULE_PATTERNS = [
    re.compile(r'^\s*-\s+\*\*((?:WP|FA|EM|AD|GS)-\d{2})\s+\[', re.MULTILINE),
    re.compile(r'^#{2,4}\s+((?:WP|FA|EM|AD|GS)-\d{2}):', re.MULTILINE),
]

GOVERNED_FILES = [
    "writing-profile.md",
    "file-architecture.md",
    "execution-modes.md",
    "anti-drift-rules.md",
    "governance-schemas.md",
    "index.md",
    "general-informatics-router.md",
    "log.md",
]

def get_definitions():
    defs = {}
    for fname in GOVERNED_FILES:
        fpath = INFORMATICS_DIR / fname
        if not fpath.exists():
            continue
        content = fpath.read_text(encoding="utf-8")
        for p in RULE_PATTERNS:
            for rid in p.findall(content):
                defs[rid] = fname
    return defs

canonical_defs = get_definitions()
print(f"Total Canonical Rules Defined across Plane 4: {len(canonical_defs)}")
for prefix in ["WP", "FA", "EM", "AD", "GS"]:
    rules = sorted([r for r in canonical_defs if r.startswith(prefix)])
    print(f"  {prefix}: {len(rules)} rules ({rules[0]}..{rules[-1]})")

# Check all rule references across V2 and Dossier files
v2_files = list(V2_DIR.glob("*.md"))
dossier_files = list(DOSSIER_DIR.glob("*.md"))

all_target_files = v2_files + dossier_files
print(f"\nScanning {len(all_target_files)} target files for rule ID references...")

RULE_REF_PATTERN = re.compile(r'\b((?:WP|FA|EM|AD|GS)-\d{2})\b')

unknown_refs = {}
for f in all_target_files:
    content = f.read_text(encoding="utf-8")
    rel_path = f.relative_to(REPO_ROOT)
    refs = set(RULE_REF_PATTERN.findall(content))
    for r in refs:
        if r not in canonical_defs:
            unknown_refs.setdefault(r, []).append(str(rel_path))

if unknown_refs:
    print(f"\n[WARNING] Found references to UNKNOWN rule IDs:")
    for rid, flist in sorted(unknown_refs.items()):
        print(f"  {rid}: referenced in {flist}")
else:
    print("\n[OK] All rule ID references resolve to canonical definitions!")

# Check for absolute file:/// links
print("\nScanning for machine-specific 'file:///' absolute links...")
abs_link_pattern = re.compile(r'\[([^\]]*)\]\((file:///[^)]+)\)')

abs_links = {}
for f in all_target_files:
    content = f.read_text(encoding="utf-8")
    rel_path = f.relative_to(REPO_ROOT)
    matches = abs_link_pattern.findall(content)
    if matches:
        abs_links[str(rel_path)] = len(matches)

if abs_links:
    print(f"[NOTE] Found absolute file:/// links in {len(abs_links)} files:")
    for path, count in sorted(abs_links.items()):
        print(f"  {path}: {count} links")
else:
    print("[OK] No file:/// links found.")

# Check for stale v0.3/v0.4 tags in candidate/blueprint/protocol files
print("\nScanning for stale tags/attributes (<always>, <writing>, <files>, <dispatch>, deepen_when=)...")
stale_patterns = {
    "<always>": re.compile(r'<always\b'),
    "<writing>": re.compile(r'<writing\b'),
    "<files>": re.compile(r'<files\b'),
    "<dispatch>": re.compile(r'<dispatch\b'),
    "deepen_when=": re.compile(r'deepen_when='),
}

for name, pattern in stale_patterns.items():
    found_in = []
    for f in all_target_files:
        content = f.read_text(encoding="utf-8")
        rel_path = f.relative_to(REPO_ROOT)
        # We allow historical docs (02, 06, 07, 08, 09, ResearchOfFile10) to mention them if in past context,
        # but let's see which files contain them.
        matches = pattern.findall(content)
        if matches:
            found_in.append((str(rel_path), len(matches)))
    print(f"Pattern '{name}': found in {len(found_in)} files")
    for p, c in found_in:
        print(f"    {p}: {c} occurrences")
