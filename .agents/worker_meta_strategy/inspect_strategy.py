import json
import os

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', encoding='utf-8') as f:
    matrix = json.load(f)

strategy_files = [x for x in matrix if x.get('agent') == 'Meta Strategy']
print(f"Total Meta Strategy files: {len(strategy_files)}")

for i, f in enumerate(strategy_files, 1):
    path = f['absolute_path']
    exists = os.path.exists(path)
    actual_size = os.path.getsize(path) if exists else -1
    lines = -1
    if exists:
        try:
            with open(path, 'r', encoding='utf-8', errors='ignore') as pf:
                lines = sum(1 for _ in pf)
        except Exception as e:
            lines = f"Error: {e}"
    print(f"{i:2d}. {f['file_name']} | Status: {f['status']} | Comp: {f['composite_score']} | Exists: {exists} | Size: {actual_size} (rep: {f.get('byte_size')}) | Lines: {lines} (rep: {f.get('line_count')})")
    print(f"    Path: {path}")
