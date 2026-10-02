import json
import os
import sys

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

hc = data['Hygiene Clean']
print('Keys in Hygiene Clean:', list(hc.keys()))
for k in hc:
    if k != 'files':
        print(f'{k}: {hc[k]}')

files = hc.get('files', [])
print(f'Total files in dossier: {len(files)}')

with open(r'c:\GitDev\apexai-os-meta\.agents\worker_hygiene_clean\all_45_files.txt', 'w', encoding='utf-8') as out:
    for i, f in enumerate(files):
        p = f.get('path', '')
        exists = os.path.exists(p)
        actual_size = os.path.getsize(p) if exists else -1
        actual_lines = 0
        if exists:
            try:
                with open(p, 'rb') as pf:
                    actual_lines = len(pf.readlines())
            except Exception as e:
                actual_lines = -1
        
        line = f"[{i+1:02d}] {f.get('name')} | exists: {exists} | size: {f.get('size')} (actual: {actual_size}) | lines: {f.get('lines')} (actual: {actual_lines}) | score: {f.get('composite_score')} | status: {f.get('status')} | path: {p}\n"
        out.write(line)

print("Saved all 45 files info to all_45_files.txt")
