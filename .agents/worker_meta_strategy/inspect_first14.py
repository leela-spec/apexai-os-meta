import json
import os

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', encoding='utf-8') as f:
    matrix = json.load(f)

strategy_files = [x for x in matrix if x.get('agent') == 'Meta Strategy']
print(f"Total Meta Strategy files: {len(strategy_files)}")

for i in range(14):
    f = strategy_files[i]
    p = f['absolute_path']
    exists = os.path.exists(p)
    sz = os.path.getsize(p) if exists else -1
    print(f"{i+1:2d}. {f['file_name']} | Status: {f['status']} | Comp: {f['composite_score']} | Exists: {exists} | Size: {sz} | Lines: {f['line_count']}")
    print(f"    Path: {p}")
