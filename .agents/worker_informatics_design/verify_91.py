import json
import os

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

def get_agent_key(item):
    p = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    ag = item.get('agent', '')
    if 'hygiene' in p.lower() or 'hygiene' in fn.lower():
        return 'Hygiene Clean'
    if ag == 'AI Routing / Special Ops':
        return 'AI Handling & Routing'
    return ag

info_items = [m for m in matrix if get_agent_key(m) == 'Informatics Design']
print(f"Total Informatics Design items: {len(info_items)}")

verified_files = []
missing_files = []

for item in info_items:
    path = item.get('absolute_path', '')
    exists = os.path.exists(path)
    if exists:
        sz = os.path.getsize(path)
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as f:
                lines = sum(1 for _ in f)
        except Exception as e:
            lines = 0
        verified_files.append({
            'file_name': item.get('file_name'),
            'path': path,
            'matrix_size': item.get('byte_size'),
            'actual_size': sz,
            'matrix_lines': item.get('line_count'),
            'actual_lines': lines,
            'score': item.get('composite_score'),
            'quality': item.get('quality'),
            'quantity': item.get('quantity'),
            'machine_readability': item.get('machine_readability'),
            'operational_value': item.get('operational_value'),
            'status': item.get('status'),
            'rationale': item.get('rationale'),
            'lineage_notes': item.get('lineage_notes')
        })
    else:
        missing_files.append((item.get('file_name'), path))

print(f"Verified files count: {len(verified_files)}")
print(f"Missing files count: {len(missing_files)}")
if missing_files:
    print("Missing files:", missing_files)

# Sort verified_files by score descending
verified_files.sort(key=lambda x: x['score'], reverse=True)

# Save to json for further analysis
with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_verified_91.json', 'w', encoding='utf-8') as f:
    json.dump(verified_files, f, indent=2)

print("Saved informatics_verified_91.json successfully.")
