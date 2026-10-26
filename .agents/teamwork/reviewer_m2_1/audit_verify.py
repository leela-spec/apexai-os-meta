import sys
import os
import re
import json
from pathlib import Path

repo_root = Path('c:/GitDev/apexai-os-meta')
info_dir = repo_root / 'apex-meta' / 'informatics'

files_to_audit = [
    'anti-drift-rules.md',
    'governance-schemas.md',
    'general-informatics-router.md',
    'index.md'
]

print('=== 1. AUDITING M2 DELIVERABLE FILES EXISTENCE & SIZES ===')
for f in files_to_audit:
    p = info_dir / f
    assert p.exists(), f'Missing file {f}'
    content = p.read_text(encoding='utf-8')
    lines = len(content.splitlines())
    chars = len(content)
    tokens = chars // 4
    print(f'{f:32} | lines: {lines:3} | chars: {chars:5} | ~tokens: {tokens:4}')

print('\n=== 2. AUDITING XML ROUTER REFS EXISTENCE ===')
router_content = (info_dir / 'general-informatics-router.md').read_text(encoding='utf-8')
xml_refs = re.findall(r'<informatics[^>]*ref="([^"]+)"', router_content)
print(f'General router XML refs: {xml_refs}')
for ref in xml_refs:
    target = (info_dir / ref).resolve()
    assert target.exists(), f'Broken router ref: {ref}'
    print(f'  [OK] Ref resolves: {ref} -> {target.name}')

index_content = (info_dir / 'index.md').read_text(encoding='utf-8')
index_xml_refs = re.findall(r'<informatics[^>]*ref="([^"]+)"', index_content)
print(f'Index XML refs: {index_xml_refs}')
for ref in index_xml_refs:
    target = (info_dir / ref).resolve()
    assert target.exists(), f'Broken index XML ref: {ref}'
    print(f'  [OK] Index ref resolves: {ref} -> {target.name}')

print('\n=== 3. AUDITING INDEX.MD ALL MARKDOWN LINKS ===')
md_links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', index_content)
print(f'Found {len(md_links)} markdown links in index.md')
for text, link in md_links:
    target = (info_dir / link).resolve()
    assert target.exists(), f'Broken markdown link in index: {link}'
    print(f'  [OK] Link resolves: [{text}] -> {link}')

print('\n=== 4. AUDITING PRIMACY (P0 TOKENS) ===')
tag_pattern = re.compile(r'\[(P[0-3])\s*\|\s*I(\d+)/E(\d+)/R(\d+)\]')
for f in files_to_audit:
    content = (info_dir / f).read_text(encoding='utf-8')
    match = tag_pattern.search(content)
    if match:
        first_p0_pos = match.start()
        first_p0_token = first_p0_pos // 4
        print(f'{f:32} | First tag at token ~{first_p0_token:3} ({match.group(0)})')
        assert first_p0_token <= 500, f'Primacy violation in {f}: first tag at token {first_p0_token}'

print('\n=== 5. AUDITING 8 ANTI-DRIFT LAWS IN ANTI-DRIFT-RULES.MD ===')
adr = (info_dir / 'anti-drift-rules.md').read_text(encoding='utf-8')
laws = [
    ('Law 1: TARGET dominates', 'TARGET dominates everything'),
    ('Law 2: Two-strike rule', 'Two-Strike Subsystem Rule'),
    ('Law 3: No whole-file rewrites', 'Whole-File Rewrite Prohibition'),
    ('Law 4: Operator challenge', 'Does this need to be fixed before we can test the actual product?'),
    ('Law 5: Checkable ambiguity', 'Verify checkable facts immediately with available tools'),
    ('Law 6: Sunk-cost prohibition', 'No sunk-cost reasoning'),
    ('Law 7: Substance over ceremony', 'Substance Over Ceremony'),
    ('Law 8: Stop on drift', 'Stop on drift')
]
for name, needle in laws:
    found = needle in adr
    print(f'  {name:30}: {"[OK] FOUND" if found else "[FAIL] MISSING"}')
    assert found, f'Missing {name}'

print('\n=== 6. AUDITING TASK MINIMALISM & CONTEXT HYGIENE IN ANTI-DRIFT-RULES.MD ===')
minimalism_topics = [
    ("Gall's Law", "Gall's Law"),
    ('Minto BLUF', 'Minto BLUF'),
    ('Zero-Speculation Scope', 'Zero-Speculation Scope Ceiling'),
    ('Simplest Viable Path', 'Simplest Viable Path'),
    ('Conscious JIT Context', 'Conscious JIT Context Loading'),
    ('Residual Name Eradication', 'Residual Name Eradication'),
    ('Pre-existing Red vs Regress', 'Pre-Existing Red vs Regression'),
    ('Primary Grounding', 'Primary Grounding vs Secondary Citation'),
    ('Command-Carrying Claims', 'Command-Carrying Claims'),
    ('Surgical Edits', 'Surgical Edits Invariant'),
    ('Asset Preservation', 'Asset Preservation Practice'),
    ('Two-Strike Tracker Mechanics', 'Two-Strike Subsystem Tracker Mechanics'),
    ('Model Directive Ceilings', 'Model-Specific Directive Ceilings')
]
for name, needle in minimalism_topics:
    found = needle in adr
    print(f'  {name:30}: {"[OK] FOUND" if found else "[FAIL] MISSING"}')
    assert found, f'Missing {name}'

print('\n=== 7. AUDITING GOVERNANCE SCHEMAS ===')
gov = (info_dir / 'governance-schemas.md').read_text(encoding='utf-8')
gov_items = [
    ('OKF Root Frontmatter Contract', 'okf_version: "0.2"'),
    ('OKF Concept Contract', 'type: Specification'),
    ('patch_intent.v1 Schema', 'patch_intent.v1'),
    ('require_unique_match: true', '"require_unique_match": { "type": "boolean", "const": true }'),
    ('fail_on_ambiguity: true', '"fail_on_ambiguity": { "type": "boolean", "const": true }'),
    ('allow_full_file_rewrite: false', '"allow_full_file_rewrite": { "type": "boolean", "const": false }'),
    ('max_files_touched default: 1', '"max_files_touched": { "type": "integer", "minimum": 1, "maximum": 50, "default": 1 }'),
    ('Prohibited Brittle Identifiers', 'line_number'),
    ('Decision Matrix Data Dict', 'Q&A Decision Matrix Data Dictionary'),
    ('Bake-Off Phases', 'Phase 1: Gating Hard Filters'),
    ('Model Ceilings Table', 'GPT-4o'),
    ('Diagnostic Rule Catalog', 'OKF-ROOT-INDEX-EXISTS')
]
for name, needle in gov_items:
    found = needle in gov
    print(f'  {name:32}: {"[OK] FOUND" if found else "[FAIL] MISSING"}')
    assert found, f'Missing {name}'


print('\n=== 8. AUDITING DESCENDING SORT OF SIGNIFICANCE TAGS ===')
for f in files_to_audit:
    content = (info_dir / f).read_text(encoding='utf-8')
    tags = tag_pattern.findall(content)
    tiers = [t[0] for t in tags]
    ranks = [{'P0': 0, 'P1': 1, 'P2': 2, 'P3': 3}[t] for t in tiers]
    is_sorted = ranks == sorted(ranks)
    print(f'{f:32} | {len(tags)} tags | strictly descending: {is_sorted}')
    assert is_sorted, f'Tags not descending in {f}'

print('\nALL INDEPENDENT AUDIT CHECKS PASSED WITH 100% SUCCESS!')
