import json
from collections import defaultdict, Counter

with open('artifacts/agent_knowledge_audit/agent_knowledge_matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

meta_ops = []
for item in matrix:
    p = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    if 'hygiene' in p.lower() or 'hygiene' in fn.lower():
        continue
    if item.get('agent') == 'Meta Ops':
        meta_ops.append(item)

print(f"Total Meta Ops files: {len(meta_ops)}")

meta_ops.sort(key=lambda x: x.get('composite_score', 0), reverse=True)

print("\n--- TOP 35 META OPS FILES ---")
for idx, it in enumerate(meta_ops[:35], 1):
    comp = it['composite_score']
    q = it['quality']
    qt = it['quantity']
    mr = it['machine_readability']
    ov = it['operational_value']
    fn = it['file_name']
    bs = it['byte_size']
    lc = it['line_count']
    st = it['status']
    path = it['absolute_path']
    print(f"{idx:2d} | {comp:.2f} | Q:{q} Qt:{qt} MR:{mr} OV:{ov} | {fn:32s} | {bs:6d} B | {lc:4d} L | {st:25s} | {path}")

# Tier distribution
tiers = Counter()
for it in meta_ops:
    c = it.get('composite_score', 0)
    if c >= 9.0:
        tiers['Tier S (9.0-10.0)'] += 1
    elif c >= 8.0:
        tiers['Tier A (8.0-8.99)'] += 1
    elif c >= 7.0:
        tiers['Tier B (7.0-7.99)'] += 1
    elif c >= 5.0:
        tiers['Tier C (5.0-6.99)'] += 1
    else:
        tiers['Tier D (<5.0)'] += 1

print("\n--- TIER DISTRIBUTION ---")
for t, cnt in sorted(tiers.items()):
    print(f"{t}: {cnt}")
