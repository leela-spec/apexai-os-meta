import json

with open('legacy_inventory.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('=== Top 25 Overall Legacy Files ===')
top25 = sorted(data, key=lambda x: (x['composite'], x['size_bytes']), reverse=True)[:25]
for i, t in enumerate(top25, 1):
    print(f"{i:2}. [{t['composite']:4.2f}] Q:{t['quality']} Qty:{t['quantity']} R:{t['readability']} V:{t['value']} | {t['domain']:22} | {t['file_name']:45} | {t['status']}")
