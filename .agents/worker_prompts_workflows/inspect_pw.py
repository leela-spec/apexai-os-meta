import json

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    matrix = json.load(f)

print("First item keys:", list(matrix[0].keys()) if matrix else "empty")
print("First item sample:", matrix[0] if matrix else "empty")

# Find how agents are identified
keys = list(matrix[0].keys())
agent_key = None
for k in keys:
    if 'agent' in k.lower():
        agent_key = k
        break

print("Agent key:", agent_key)
if agent_key:
    agents = set(x.get(agent_key) for x in matrix)
    print("Agents in matrix:", sorted(list(agents)))
