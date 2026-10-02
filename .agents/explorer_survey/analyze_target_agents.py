import json
from collections import Counter, defaultdict
import os

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

# Let's inspect the exact mapping.
# The user specified 8 target agents:
# 1. Meta Ops (Meta Ops Head)
# 2. Meta Detective (Meta Detective Head)
# 3. Meta Strategy (Meta Strategy Head)
# 4. Prompts & Workflows / Prompt Engineer
# 5. Informatics Design
# 6. Knowledge Bank
# 7. AI Handling & Routing
# 8. Hygiene Clean

# Notice in the matrix, the 'agent' field has:
# 'Meta Ops', 'Meta Detective', 'Meta Strategy', 'Prompts & Workflows', 'Informatics Design', 'Knowledge Bank', 'AI Routing / Special Ops', 'Alfred'.
# Let's see how 'AI Handling & Routing' and 'Hygiene Clean' are divided within 'AI Routing / Special Ops' (and any cross-agent mentions).

def classify_agent(item):
    agent = item.get('agent', '')
    path = item.get('absolute_path', '')
    fn = item.get('file_name', '')
    
    # Check hygiene clean specific items
    if 'hygiene' in path.lower() or 'hygiene' in fn.lower():
        return 'Hygiene Clean'
    
    if agent == 'AI Routing / Special Ops':
        # If not hygiene clean, it's AI Handling & Routing
        return 'AI Handling & Routing'
    
    if agent == 'Meta Ops':
        return 'Meta Ops'
    elif agent == 'Meta Detective':
        return 'Meta Detective'
    elif agent == 'Meta Strategy':
        return 'Meta Strategy'
    elif agent == 'Prompts & Workflows':
        return 'Prompts & Workflows'
    elif agent == 'Informatics Design':
        return 'Informatics Design'
    elif agent == 'Knowledge Bank':
        return 'Knowledge Bank'
    elif agent == 'Alfred':
        return 'Alfred'
    return agent

# Let's classify all items
categorized = defaultdict(list)
for item in matrix:
    target = classify_agent(item)
    categorized[target].append(item)

print("=== AGENT FILE COUNTS (with Hygiene Clean separated) ===")
for target, items in sorted(categorized.items(), key=lambda x: len(x[1]), reverse=True):
    print(f"{target}: {len(items)} files")

# Detailed per-agent analysis
print("\n" + "="*80)
print("DETAILED PER-AGENT SUMMARY")
print("="*80)

target_order = [
    "Meta Ops",
    "Meta Detective",
    "Meta Strategy",
    "Prompts & Workflows",
    "Informatics Design",
    "Knowledge Bank",
    "AI Handling & Routing",
    "Hygiene Clean"
]

results = {}

for agent_name in target_order:
    items = categorized.get(agent_name, [])
    # status breakdown
    status_counts = Counter(item.get('status') for item in items)
    # top scoring files
    sorted_items = sorted(items, key=lambda x: x.get('composite_score', 0), reverse=True)
    
    # Path locations / repositories
    repo_counts = Counter()
    for item in items:
        p = item.get('absolute_path', '')
        if 'c:\\GitDev\\apexai-os-meta' in p.lower():
            repo_counts['GitDev/apexai-os-meta'] += 1
        elif 'quasi desktop\\ai_preperationuntil_06-26' in p.lower():
            repo_counts['Quasi Desktop/AI_PreperationUntil_06-26'] += 1
        else:
            repo_counts['Other'] += 1
            
    # Stubs check
    stubs = [it for it in items if it.get('status') == 'Empty Scaffold / Stub' or 'EMPTY_STATE' in it.get('rationale', '')]
    
    # Top 5 files
    top_5 = sorted_items[:5]
    
    results[agent_name] = {
        'total': len(items),
        'status_counts': dict(status_counts),
        'repo_counts': dict(repo_counts),
        'stub_count': len(stubs),
        'stubs': [s.get('file_name') for s in stubs],
        'top_5': [{
            'file_name': t.get('file_name'),
            'composite_score': t.get('composite_score'),
            'quality': t.get('quality'),
            'quantity': t.get('quantity'),
            'machine_readability': t.get('machine_readability'),
            'operational_value': t.get('operational_value'),
            'byte_size': t.get('byte_size'),
            'line_count': t.get('line_count'),
            'path': t.get('absolute_path'),
            'status': t.get('status'),
            'rationale': t.get('rationale')
        } for t in top_5]
    }
    
    print(f"\n### {agent_name} (Total: {len(items)})")
    print(f"  Statuses: {dict(status_counts)}")
    print(f"  Repos: {dict(repo_counts)}")
    print(f"  Stubs: {len(stubs)} ({[s.get('file_name') for s in stubs[:5]]})")
    print("  Top 5 files:")
    for t in top_5:
        print(f"    - {t.get('file_name')} | Score: {t.get('composite_score')} | Q:{t.get('quality')} Qt:{t.get('quantity')} MR:{t.get('machine_readability')} OV:{t.get('operational_value')} | Path: {t.get('absolute_path')}")

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\agent_recon_data.json', 'w', encoding='utf-8') as out:
    json.dump(results, out, indent=2)
print("\nWrote agent_recon_data.json successfully.")
