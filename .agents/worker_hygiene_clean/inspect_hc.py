import json
import sys
import os

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)

print('Keys:', list(data.keys()))
for k in data:
    if 'hygiene' in k.lower():
        print(f'\nKey: {k}')
        val = data[k]
        for prop in val:
            if prop != 'files':
                print(f'  {prop}: {val[prop]}')
            else:
                print(f'  files count: {len(val["files"])}')
                for i, file_info in enumerate(val['files']):
                    print(f'    [{i+1}] {file_info.get("name")} | size: {file_info.get("size")} | lines: {file_info.get("lines")} | score: {file_info.get("composite_score")} | path: {file_info.get("path")}')
