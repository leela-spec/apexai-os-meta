import os
import json

p_folder = r'C:\Quasi Desktop\AI_PreperationUntil_06-26\Previous_OpenClaw\07_finalopenclawsystem\managed\agent_kb\special_ops__prompts_workflows\appendices\NewResearchBecauseOfConstantFailure\Recap&ProcessImprovs'
actual_files = os.listdir(p_folder)
print("Actual files:")
for f in actual_files:
    print(repr(f))

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

pw_files = [x for x in matrix if x.get('agent') == 'Prompts & Workflows']

for x in pw_files:
    p = x['absolute_path']
    if 'Recap' in p:
        print("Matrix path:", repr(p))
        print("Exists directly?", os.path.exists(p))
        base = os.path.basename(p)
        print("Base in actual?", base in actual_files)
        dir_name = os.path.dirname(p)
        print("Dir name exists?", os.path.exists(dir_name))
        if os.path.exists(dir_name):
            matching = [f for f in os.listdir(dir_name) if f.lower() == base.lower()]
            print("Matching in dir:", matching)
