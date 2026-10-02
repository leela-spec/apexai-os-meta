import json
from collections import Counter

with open('evaluated_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f"Total evaluated files: {len(data)}")

print("\n--- By Lifecycle Status ---")
for s, c in Counter(d['status'] for d in data).most_common():
    print(f"  {s}: {c}")

print("\n--- By Domain ---")
for s, c in Counter(d['domain'] for d in data).most_common():
    print(f"  {s}: {c}")

print("\n--- By Scope ---")
for s, c in Counter(d['scope'] for d in data).most_common():
    print(f"  {s}: {c}")

print("\n--- Top 15 Highest Scoring Files ---")
top_sorted = sorted(data, key=lambda x: (x['composite_score'], x['quality'], x['operational_value']), reverse=True)
for x in top_sorted[:15]:
    print(f"  {x['composite_score']} | {x['domain']} | {x['file_name']} | {x['status']} | {x['rel_path']}")

print("\n--- Lowest Scoring Files ---")
for x in top_sorted[-10:]:
    print(f"  {x['composite_score']} | {x['domain']} | {x['file_name']} | {x['status']} | {x['rel_path']}")
