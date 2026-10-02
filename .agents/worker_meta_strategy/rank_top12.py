import json
import os

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', encoding='utf-8') as f:
    matrix = json.load(f)

strategy = [x for x in matrix if x.get('agent') == 'Meta Strategy']
strategy.sort(key=lambda x: x.get('composite_score', 0), reverse=True)

for i in range(12):
    f = strategy[i]
    path = f['absolute_path']
    exists = os.path.exists(path)
    sz = os.path.getsize(path) if exists else -1
    lc = f.get('line_count')
    cs = f.get('composite_score')
    q = f.get('quality')
    qt = f.get('quantity')
    mr = f.get('machine_readability')
    ov = f.get('operational_value')
    st = f.get('status')
    name = f.get('file_name')
    print(f"{i+1:2d} | Comp: {cs:4.2f} | Q:{q:2d} Qt:{qt:2d} MR:{mr:2d} OV:{ov:2d} | Size:{sz:6d} Lines:{lc:4d} | {st[:15]} | {name}")
    print(f"    Path: {path}")
