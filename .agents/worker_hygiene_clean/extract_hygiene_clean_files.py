import json
import os

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

def is_hygiene_clean(item):
    p = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    ag = item.get('agent', '')
    return ('hygiene' in p.lower() or 'hygiene' in fn.lower())

hc_items = [x for x in matrix if is_hygiene_clean(x)]
print(f"Total Hygiene Clean items in matrix: {len(hc_items)}")

# Sort by composite_score desc
hc_items.sort(key=lambda x: (x.get('composite_score', 0), x.get('byte_size', 0)), reverse=True)

verified_items = []
missing_items = []

for i, it in enumerate(hc_items):
    p = it.get('absolute_path', '')
    fn = it.get('file_name', '')
    exists = os.path.exists(p)
    actual_size = os.path.getsize(p) if exists else None
    actual_lines = 0
    if exists:
        try:
            with open(p, 'rb') as pf:
                actual_lines = len(pf.readlines())
        except Exception:
            actual_lines = -1
    else:
        missing_items.append((fn, p))
    
    item_data = {
        'rank': i + 1,
        'file_name': fn,
        'absolute_path': p,
        'exists': exists,
        'matrix_size': it.get('byte_size'),
        'actual_size': actual_size,
        'matrix_lines': it.get('line_count'),
        'actual_lines': actual_lines,
        'quality': it.get('quality'),
        'quantity': it.get('quantity'),
        'machine_readability': it.get('machine_readability'),
        'operational_value': it.get('operational_value'),
        'composite_score': it.get('composite_score'),
        'status': it.get('status'),
        'agent': it.get('agent'),
        'lineage_notes': it.get('lineage_notes'),
        'rationale': it.get('rationale')
    }
    verified_items.append(item_data)

print(f"Verified exists count: {sum(1 for x in verified_items if x['exists'])} / {len(verified_items)}")
if missing_items:
    print(f"Missing files ({len(missing_items)}):")
    for fn, p in missing_items:
        print(f"  {fn} -> {p}")

with open(r'c:\GitDev\apexai-os-meta\.agents\worker_hygiene_clean\hygiene_clean_verified_census.json', 'w', encoding='utf-8') as out_f:
    json.dump(verified_items, out_f, indent=2)

print("Saved hygiene_clean_verified_census.json")
