import json
from collections import Counter, defaultdict
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

target_order = [
    ("Meta Ops", "meta-ops", "META_OPS"),
    ("Meta Detective", "meta-detective", "META_DETECTIVE"),
    ("Meta Strategy", "meta-strategy", "META_STRATEGY"),
    ("Prompts & Workflows", "prompts-workflows", "PROMPTS_WORKFLOWS"),
    ("Informatics Design", "informatics-design", "INFORMATICS_DESIGN"),
    ("Knowledge Bank", "knowledge-bank", "KNOWLEDGE_BANK"),
    ("AI Handling & Routing", "ai-handling-routing", "AI_HANDLING_ROUTING"),
    ("Hygiene Clean", "hygiene-clean", "HYGIENE_CLEAN")
]

all_data = {}

for agent_label, slug, upper_slug in target_order:
    items = [x for x in matrix if get_agent_key(x) == agent_label]
    items_sorted = sorted(items, key=lambda x: x.get('composite_score', 0), reverse=True)
    
    status_counts = Counter(x.get('status') for x in items)
    
    gitdev_count = sum(1 for x in items if 'apexai-os-meta' in x.get('absolute_path', '').lower())
    quasidev_count = sum(1 for x in items if 'ai_preperation' in x.get('absolute_path', '').lower())
    
    stubs = [x for x in items if x.get('status') == 'Empty Scaffold / Stub' or 'EMPTY_STATE' in x.get('rationale', '') or 'EMPTY_STATE' in x.get('lineage_notes', '')]
    
    # top 10
    top_10 = []
    for it in items_sorted[:10]:
        p = it.get('absolute_path', '')
        exists = os.path.exists(p)
        top_10.append({
            'name': it.get('file_name'),
            'score': it.get('composite_score'),
            'q': it.get('quality'),
            'qt': it.get('quantity'),
            'mr': it.get('machine_readability'),
            'ov': it.get('operational_value'),
            'size': it.get('byte_size'),
            'lines': it.get('line_count'),
            'status': it.get('status'),
            'path': p,
            'exists': exists,
            'rationale': it.get('rationale')
        })
        
    all_data[agent_label] = {
        'slug': slug,
        'upper_slug': upper_slug,
        'total': len(items),
        'gitdev_count': gitdev_count,
        'quasidev_count': quasidev_count,
        'status_counts': dict(status_counts),
        'stub_count': len(stubs),
        'stubs': [{'name': s.get('file_name'), 'path': s.get('absolute_path'), 'score': s.get('composite_score')} for s in stubs],
        'top_10': top_10
    }

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\compiled_agent_data.json', 'w', encoding='utf-8') as f:
    json.dump(all_data, f, indent=2)

print("Saved compiled_agent_data.json successfully")
