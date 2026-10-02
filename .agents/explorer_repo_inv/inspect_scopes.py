import json

with open('raw_inventory.json', 'r', encoding='utf-8') as f:
    items = json.load(f)

for s in ['Scope 1: Active Agent Contracts', 'Scope 2: Orchestration Agent Doctrines & Manifests', 'Scope 3: System Core & Workflows']:
    print(f'=== {s} ===')
    for it in [x for x in items if x['scope'] == s][:5]:
        print(f"File: {it['file_name']} ({it['byte_size']} bytes, {it['line_count']} lines, yaml={it['has_yaml_frontmatter']})")
        print(f"  Keys: {it['yaml_keys']}")
        print(f"  Preview: {it['preview'][:2]}")
