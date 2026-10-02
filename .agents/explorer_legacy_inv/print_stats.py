import json
from collections import Counter

with open('legacy_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print(f'Total records: {len(data)}')

scopes = Counter(d['scope'] for d in data)
print('\n=== Breakdown by Scope ===')
for s, c in sorted(scopes.items()):
    print(f'{s:55}: {c}')

domains = Counter(d['domain'] for d in data)
print('\n=== Breakdown by Domain ===')
for dm, c in sorted(domains.items()):
    print(f'{dm:30}: {c}')

statuses = Counter(d['status'] for d in data)
print('\n=== Breakdown by Lifecycle Status ===')
for st, c in sorted(statuses.items()):
    print(f'{st:30}: {c}')

print('\n=== Top 15 Files by Composite Score ===')
top15 = sorted(data, key=lambda x: x['composite'], reverse=True)[:15]
for t in top15:
    print(f"{t['composite']:4.2f} | Q:{t['quality']} Qty:{t['quantity']} R:{t['readability']} V:{t['value']} | {t['domain']:20} | {t['file_name']}")

print('\n=== Empty Scaffold / Stub Files ===')
stubs = [d for d in data if d['status'] == 'Empty Scaffold / Stub']
print(f'Total Stubs: {len(stubs)}')
for s in stubs:
    print(f"  {s['file_name']:40} | size: {s['size_bytes']:5} | lines: {s['line_count']:3} | {s['rel_path']}")
