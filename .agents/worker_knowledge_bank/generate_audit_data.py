import json
from collections import Counter, defaultdict

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

def get_canonical_agent(item):
    p = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    ag = item.get('agent', '')
    if 'hygiene' in p.lower() or 'hygiene' in fn.lower():
        return 'Hygiene Clean'
    if ag == 'AI Routing / Special Ops':
        return 'AI Handling & Routing'
    return ag

kb_files = [item for item in matrix if get_canonical_agent(item) == 'Knowledge Bank']

# Tier distribution
tiers = Counter()
for f in kb_files:
    score = f['composite_score']
    if score >= 9.0:
        tiers['Tier S (9.00 - 10.00)'] += 1
    elif score >= 8.0:
        tiers['Tier A (8.00 - 8.99)'] += 1
    elif score >= 7.0:
        tiers['Tier B (7.00 - 7.99)'] += 1
    elif score >= 5.0:
        tiers['Tier C (5.00 - 6.99)'] += 1
    else:
        tiers['Tier D (< 5.00)'] += 1

print("Tier Breakdown:")
for t, c in sorted(tiers.items()):
    print(f"  {t}: {c} ({c/len(kb_files)*100:.1f}%)")

# Path clusters
path_clusters = Counter()
for f in kb_files:
    p = f['absolute_path']
    if 'apexai-os-meta' in p.lower():
        sub = p.lower().split('apexai-os-meta\\')[1]
        top = sub.split('\\')[0]
        if top.startswith('.'):
            top = '\\'.join(sub.split('\\')[:2])
        path_clusters['GitDev: ' + top] += 1
    elif 'ai_preperationuntil_06-26' in p.lower():
        sub = p.lower().split('ai_preperationuntil_06-26\\')[1]
        top = sub.split('\\')[0]
        path_clusters['Quasi: ' + top] += 1

print("\nPath Clusters:")
for pc, c in sorted(path_clusters.items(), key=lambda x: x[1], reverse=True):
    print(f"  {pc}: {c} ({c/len(kb_files)*100:.1f}%)")

sorted_kb = sorted(kb_files, key=lambda x: x['composite_score'], reverse=True)
print("\nTop 30 files for leaderboard:")
for i, f in enumerate(sorted_kb[:30], 1):
    print(f"{i:2d} | {f['file_name']} | Comp: {f['composite_score']} | Q: {f['quality']} | Qt: {f['quantity']} | MR: {f['machine_readability']} | OV: {f['operational_value']} | {f['byte_size']} B | {f['line_count']} L | {f['status']} | {f['absolute_path']}")
