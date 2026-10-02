import json

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_categorized_91.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

for cat in sorted(set(f['category'] for f in files)):
    cat_files = [f for f in files if f['category'] == cat]
    print(f"=== {cat} ({len(cat_files)} files) ===")
    for f in cat_files:
        print(f"  [{f['score']:.2f}] {f['file_name']} ({f['actual_size']} B, {f['actual_lines']} L, {f['status']}) -> {f['path']}")
    print()
