import json
import os
import sys

sys.stdout.reconfigure(encoding='utf-8')

matrix_path = r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json'
with open(matrix_path, 'r', encoding='utf-8') as f:
    data = json.load(f)

det = [f for f in data if f.get('agent') == 'Meta Detective']
print(f'Total Meta Detective entries: {len(det)}')

# verify physical existence, actual size, lines
for f in det:
    p = f.get('absolute_path')
    # handle extended path for > 260 chars
    check_p = p
    if len(check_p) >= 260 and not check_p.startswith('\\\\?\\'):
        check_p = '\\\\?\\' + check_p
    exists = os.path.exists(check_p)
    f['verified_exists'] = exists
    if exists:
        f['actual_size'] = os.path.getsize(check_p)
        try:
            with open(check_p, 'r', encoding='utf-8', errors='replace') as fp:
                f['actual_lines'] = sum(1 for _ in fp)
        except Exception as e:
            f['actual_lines'] = -1
    else:
        f['actual_size'] = 0
        f['actual_lines'] = 0

gitdev = [f for f in det if f['absolute_path'].lower().startswith('c:\\gitdev')]
quasi = [f for f in det if f['absolute_path'].lower().startswith('c:\\quasi desktop')]

print(f'GitDev count: {len(gitdev)}')
print(f'Quasi count: {len(quasi)}')

missing = [f for f in det if not f['verified_exists']]
print(f'Missing files count: {len(missing)}')

# Save enriched dataset for our audit report generation
with open(r'c:\GitDev\apexai-os-meta\.agents\worker_meta_detective\det_enriched.json', 'w', encoding='utf-8') as f:
    json.dump(det, f, indent=2)

print('Enriched dataset written.')
