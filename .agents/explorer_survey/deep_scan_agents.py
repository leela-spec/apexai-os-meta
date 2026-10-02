import json
from collections import Counter, defaultdict
import os

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Classification logic for 8 agents + Alfred
def get_canonical_agent(item):
    p = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    ag = item.get('agent', '')
    
    # Hygiene Clean detection
    if 'hygiene' in p.lower() or 'hygiene' in fn.lower():
        return 'Hygiene Clean'
    
    if ag == 'AI Routing / Special Ops':
        return 'AI Handling & Routing'
    
    return ag

agent_files = defaultdict(list)
for item in matrix:
    ca = get_canonical_agent(item)
    agent_files[ca].append(item)

print("Canonical agent distribution:")
for ca, files in sorted(agent_files.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"  {ca}: {len(files)} files")

target_agents = [
    "Meta Ops",
    "Meta Detective",
    "Meta Strategy",
    "Prompts & Workflows",
    "Informatics Design",
    "Knowledge Bank",
    "AI Handling & Routing",
    "Hygiene Clean"
]

detailed_agent_dossiers = {}

for name in target_agents:
    items = agent_files.get(name, [])
    # Sort by composite score desc
    items_sorted = sorted(items, key=lambda x: x.get('composite_score', 0), reverse=True)
    
    # Statuses
    statuses = Counter(x.get('status') for x in items)
    
    # Check physical existence of top 10 files
    top_10 = items_sorted[:10]
    top_10_verified = []
    for it in top_10:
        p = it.get('absolute_path', '')
        exists = os.path.exists(p)
        actual_size = os.path.getsize(p) if exists else None
        top_10_verified.append({
            'file_name': it.get('file_name'),
            'path': p,
            'exists': exists,
            'reported_size': it.get('byte_size'),
            'actual_size': actual_size,
            'score': it.get('composite_score'),
            'quality': it.get('quality'),
            'quantity': it.get('quantity'),
            'machine_readability': it.get('machine_readability'),
            'operational_value': it.get('operational_value'),
            'status': it.get('status'),
            'rationale': it.get('rationale'),
            'lineage_notes': it.get('lineage_notes')
        })
        
    # Check all empty scaffolds / stubs
    stubs = [x for x in items if x.get('status') == 'Empty Scaffold / Stub' or 'EMPTY_STATE' in x.get('rationale', '') or 'EMPTY_STATE' in x.get('lineage_notes', '')]
    stub_files = [{
        'file_name': s.get('file_name'),
        'path': s.get('absolute_path'),
        'exists': os.path.exists(s.get('absolute_path', '')),
        'score': s.get('composite_score'),
        'rationale': s.get('rationale')
    } for s in stubs]
    
    # Path clustering
    path_clusters = Counter()
    for it in items:
        p = it.get('absolute_path', '')
        if 'c:\\gitdev\\apexai-os-meta' in p.lower():
            # cluster within gitdev
            rel = p.lower().split('apexai-os-meta\\')[1]
            top_dir = rel.split('\\')[0]
            if top_dir.startswith('.'):
                top_dir = '\\'.join(rel.split('\\')[:2])
            path_clusters['GitDev: ' + top_dir] += 1
        elif 'quasi desktop' in p.lower():
            rel = p.lower().split('ai_preperationuntil_06-26\\')[1]
            top_dir = rel.split('\\')[0]
            if top_dir == 'previous_openclaw':
                top_dir = '\\'.join(rel.split('\\')[:2])
            path_clusters['QuasiDesktop: ' + top_dir] += 1
        else:
            path_clusters['Other'] += 1
            
    detailed_agent_dossiers[name] = {
        'total_files': len(items),
        'status_breakdown': dict(statuses),
        'path_clusters': dict(path_clusters.most_common(8)),
        'stub_count': len(stubs),
        'stubs': stub_files,
        'top_10': top_10_verified
    }

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', 'w', encoding='utf-8') as f:
    json.dump(detailed_agent_dossiers, f, indent=2)

print("\nSaved detailed_agent_dossiers.json")
