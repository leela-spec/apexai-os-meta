import json

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

informatics_items = [m for m in matrix if get_agent_key(m) == 'Informatics Design']
print(f"Total Informatics Design items with get_agent_key: {len(informatics_items)}")

# Let's inspect the 3 reassigned files
reassigned = [m for m in matrix if m.get('agent') == 'Informatics Design' and get_agent_key(m) != 'Informatics Design']
print(f"Reassigned items count: {len(reassigned)}")
for r in reassigned:
    print(" -", r['file_name'], "->", r['absolute_path'])
