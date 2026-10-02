import json

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
sorted_kb = sorted(kb_files, key=lambda x: x['composite_score'], reverse=True)

print("Top 15 files:")
for i, f in enumerate(sorted_kb[:15], 1):
    print(f"{i:2d}. {f['composite_score']:.2f} | Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']} | {f['byte_size']} B, {f['line_count']} L | {f['file_name']} | {f['status']}")
    print(f"    Path: {f['absolute_path']}")
