import json
from collections import Counter, defaultdict
import os

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

print(f"Total KB files: {len(kb_files)}")
status_counts = Counter(f['status'] for f in kb_files)
for s, c in status_counts.items():
    print(f"  {s}: {c}")

folders = defaultdict(list)
for f in kb_files:
    p = f['absolute_path']
    if 'apexai-os-meta' in p.lower():
        sub = p.lower().split('apexai-os-meta\\')[1]
        top = sub.split('\\')[0]
        if top.startswith('.'):
            top = '\\'.join(sub.split('\\')[:2])
        folders['GitDev: ' + top].append(f)
    elif 'ai_preperationuntil_06-26' in p.lower():
        sub = p.lower().split('ai_preperationuntil_06-26\\')[1]
        top = sub.split('\\')[0]
        folders['Quasi: ' + top].append(f)
    else:
        folders['Other'].append(f)

print('\nFolder distribution:')
for fold, flist in sorted(folders.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {fold}: {len(flist)} files")

print('\nTop 25 by composite score:')
sorted_kb = sorted(kb_files, key=lambda x: x['composite_score'], reverse=True)
for i, f in enumerate(sorted_kb[:25], 1):
    print(f"{i:2d}. {f['composite_score']:.2f} | Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']} | {f['byte_size']} B, {f['line_count']} L | {f['file_name']} | {f['status']}")
    print(f"    Path: {f['absolute_path']}")

print('\nQuarantined / Empty Scaffold Stubs:')
stubs = [f for f in kb_files if f['status'] == 'Empty Scaffold / Stub' or 'EMPTY_STATE' in f.get('rationale', '') or 'EMPTY_STATE' in f.get('lineage_notes', '')]
for s in stubs:
    print(f"  {s['file_name']} | {s['byte_size']} B, {s['line_count']} L | {s['composite_score']} | {s['absolute_path']}")
    print(f"    Rationale: {s.get('rationale')}")

print('\nAll Distinct Categories or Types:')
# Let's inspect other files in the top 50
print('\nRank 26-50:')
for i, f in enumerate(sorted_kb[25:50], 26):
    print(f"{i:2d}. {f['composite_score']:.2f} | Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']} | {f['byte_size']} B, {f['line_count']} L | {f['file_name']} | {f['status']}")
    print(f"    Path: {f['absolute_path']}")
