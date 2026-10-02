import json
import os

base_dir = os.path.dirname(__file__)
json_path = os.path.join(base_dir, 'legacy_inventory.json')
md_path = os.path.join(base_dir, 'legacy_inventory.md')

# 1. Verify JSON and disk paths
with open(json_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Loaded {len(data)} records from legacy_inventory.json")

missing = []
for d in data:
    p = d['absolute_path']
    if not os.path.exists('\\\\?\\' + p):
        missing.append(p)

assert len(missing) == 0, f"Found {len(missing)} missing files: {missing}"
print(f"VERIFIED: 100% of all {len(data)} physical files exist on disk with zero phantom paths!")

# 2. Verify Markdown report sections
with open(md_path, 'r', encoding='utf-8') as f:
    text = f.read()

sections = text.split('## ')
scope_counts = {}
for s in sections[1:]:
    header = s.split('\n')[0]
    lines = s.split('\n')
    table_lines = [l for l in lines if l.startswith('|') and not l.startswith('| #') and not l.startswith('|:') and not l.startswith('| Scope') and not l.startswith('| Functional') and not l.startswith('| Lifecycle') and not l.startswith('| Rank') and not l.startswith('| **')]
    if 'Scope 1' in header: scope_counts['Scope 1'] = len(table_lines)
    elif 'Scope 2' in header: scope_counts['Scope 2'] = len(table_lines)
    elif 'Scope 3' in header: scope_counts['Scope 3'] = len(table_lines)
    elif 'Scope 4' in header: scope_counts['Scope 4'] = len(table_lines)
    elif 'Scope 5' in header: scope_counts['Scope 5'] = len(table_lines)
    elif 'Leaderboard' in header: scope_counts['Leaderboard'] = len(table_lines)

print("\nMarkdown Table Verification:")
print(f"  Scope 1 (Managed Agent KB): {scope_counts['Scope 1']} (expected 216)")
print(f"  Scope 2 (Source Indexes): {scope_counts['Scope 2']} (expected 4)")
print(f"  Scope 3 (Managed Companion Systems): {scope_counts['Scope 3']} (expected 33)")
print(f"  Scope 4 (Modernization & Factory): {scope_counts['Scope 4']} (expected 62)")
print(f"  Scope 5 (Uncurated Operational Corpora): {scope_counts['Scope 5']} (expected 222)")
print(f"  Leaderboard: {scope_counts['Leaderboard']} (expected 30)")

total_cataloged = sum(scope_counts[k] for k in ['Scope 1', 'Scope 2', 'Scope 3', 'Scope 4', 'Scope 5'])
print(f"\nTotal unique cataloged rows in inventory tables: {total_cataloged}")
assert total_cataloged == 537, f"Expected 537 cataloged rows, got {total_cataloged}"
assert scope_counts['Scope 1'] == 216
assert scope_counts['Scope 2'] == 4
assert scope_counts['Scope 3'] == 33
assert scope_counts['Scope 4'] == 62
assert scope_counts['Scope 5'] == 222
assert scope_counts['Leaderboard'] == 30

print("\nALL SYSTEM VERIFICATIONS PASSED WITH 100% DISK GROUNDING AND STRUCTURAL FIDELITY!")
