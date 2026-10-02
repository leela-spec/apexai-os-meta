import json

with open(r'c:\GitDev\apexai-os-meta\.agents\worker_hygiene_clean\hygiene_clean_verified_census.json', 'r', encoding='utf-8') as f:
    census = json.load(f)

for x in census:
    print(f"#{x['rank']:02d} | Comp: {x['composite_score']:.2f} | Q:{x['quality']} Qt:{x['quantity']} MR:{x['machine_readability']} OV:{x['operational_value']} | {x['actual_size']} B | {x['actual_lines']} L | {x['status']} | {x['file_name']} | {x['absolute_path']}")
