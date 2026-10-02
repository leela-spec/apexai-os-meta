import json
from collections import Counter, defaultdict

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total entries in matrix: {len(data)}")

# 1. Agents in matrix
agents = Counter(d.get('agent') for d in data)
print("\nAgents breakdown:")
for a, cnt in agents.most_common():
    print(f"  {a}: {cnt}")

# 2. Statuses breakdown
statuses = Counter(d.get('status') for d in data)
print("\nStatus breakdown overall:")
for s, cnt in statuses.most_common():
    print(f"  {s}: {cnt}")

# 3. Target 8 agents mapping
# Target agents from request:
# 1. Meta Ops (Meta Ops Head)
# 2. Meta Detective (Meta Detective Head)
# 3. Meta Strategy (Meta Strategy Head)
# 4. Prompts & Workflows / Prompt Engineer
# 5. Informatics Design
# 6. Knowledge Bank
# 7. AI Handling & Routing
# 8. Hygiene Clean

# Let's inspect where "Hygiene Clean" files are currently assigned in matrix:
hygiene_items = [d for d in data if 'hygiene' in d.get('absolute_path', '').lower() or 'hygiene' in d.get('file_name', '').lower()]
print(f"\nTotal files matching 'hygiene' in path or file_name: {len(hygiene_items)}")
hygiene_by_agent = Counter(d.get('agent') for d in hygiene_items)
print("Hygiene files currently attributed to:")
for a, cnt in hygiene_by_agent.most_common():
    print(f"  {a}: {cnt}")

# Let's check AI Routing / Special Ops folder paths:
ai_routing_items = [d for d in data if d.get('agent') == 'AI Routing / Special Ops']
ai_routing_subdirs = Counter()
for d in ai_routing_items:
    path = d.get('absolute_path', '')
    if 'managed\\agent_kb\\' in path:
        sub = path.split('managed\\agent_kb\\')[1].split('\\')[0]
        ai_routing_subdirs[sub] += 1
    else:
        ai_routing_subdirs['other: ' + path.split('\\')[-2]] += 1
print("\nAI Routing / Special Ops breakdown by folder:")
for sub, cnt in ai_routing_subdirs.most_common():
    print(f"  {sub}: {cnt}")
