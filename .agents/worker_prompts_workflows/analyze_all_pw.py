import json
import os

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

pw_files = [x for x in matrix if x.get('agent') == 'Prompts & Workflows']
print(f"Total PW files: {len(pw_files)}")

# Check repos
gitdev_files = [x for x in pw_files if 'GitDev' in x['absolute_path'] or 'apexai-os-meta' in x['absolute_path']]
quasi_files = [x for x in pw_files if 'Quasi Desktop' in x['absolute_path']]
print(f"GitDev count: {len(gitdev_files)}, Quasi count: {len(quasi_files)}")

# Status breakdown
status_counts = {}
for x in pw_files:
    s = x['status']
    status_counts[s] = status_counts.get(s, 0) + 1
print("Status breakdown:", status_counts)

# Score stats
scores = [x['composite_score'] for x in pw_files]
print(f"Min score: {min(scores)}, Max score: {max(scores)}, Avg: {sum(scores)/len(scores):.2f}")

# Sort by composite_score desc
sorted_files = sorted(pw_files, key=lambda x: (x['composite_score'], x['quality'], x['quantity']), reverse=True)

print("\n--- TOP 25 FILES ---")
for i, f in enumerate(sorted_files[:25], 1):
    print(f"{i:2d}. {f['file_name']} | Comp: {f['composite_score']} | Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']} | Size: {f['byte_size']} B | Lines: {f['line_count']} | Status: {f['status']}")
    print(f"    Path: {f['absolute_path']}")

# Check stubs
stubs = [x for x in pw_files if x['status'] == 'Empty Scaffold / Stub' or x['composite_score'] < 4.0 or x['byte_size'] == 0]
print(f"\nPotential stubs count: {len(stubs)}")
for s in stubs:
    print(f"Stub: {s['file_name']} | Size: {s['byte_size']} | Score: {s['composite_score']} | Path: {s['absolute_path']}")
