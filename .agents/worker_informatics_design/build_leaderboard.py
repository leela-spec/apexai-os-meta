import json

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_categorized_91.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

# Sort files by score descending
files_sorted = sorted(files, key=lambda x: (x['score'], x['actual_size']), reverse=True)

# Generate Markdown table rows for Section 5
table_rows = []
for i, f in enumerate(files_sorted[:35], 1):
    cat_short = f['category'].split(':')[0]
    row = f"| {i} | `{f['file_name']}` | {cat_short} | **{f['score']:.2f}** | {f['quality']} | {f['quantity']} | {f['machine_readability']} | {f['operational_value']} | {f['actual_size']:,} | {f['actual_lines']} | {f['status']} | `{f['path']}` |"
    table_rows.append(row)

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/leaderboard_rows.txt', 'w', encoding='utf-8') as out:
    out.write("\n".join(table_rows))

print(f"Generated {len(table_rows)} leaderboard rows.")
