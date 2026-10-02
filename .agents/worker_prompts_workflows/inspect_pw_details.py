import json
import os

with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', 'r', encoding='utf-8') as f:
    dossiers = json.load(f)

pw_dossier = dossiers['Prompts & Workflows']
print("=== DOSSIER INFO ===")
for k in pw_dossier:
    if k not in ['top_10', 'stubs', 'files']:
        print(f"{k}: {pw_dossier[k]}")

print("\n=== STUBS (count: {}) ===".format(len(pw_dossier.get('stubs', []))))
for s in pw_dossier.get('stubs', []):
    print(s)

print("\n=== TOP 10 ===")
for item in pw_dossier.get('top_10', []):
    print(f"Rank {item.get('rank')}: {item.get('file_name')} - Score {item.get('composite_score')} (Path: {item.get('absolute_path')})")

with open(r'c:\GitDev\apexai-os-meta\artifacts\agent_knowledge_audit\agent_knowledge_matrix.json', 'r', encoding='utf-8') as f:
    matrix = json.load(f)

pw_files = [x for x in matrix if x.get('agent') == 'Prompts & Workflows']
print(f"\nTotal PW files in matrix: {len(pw_files)}")

# Check physical existence of all 186 files
missing_files = []
for x in pw_files:
    p = x['absolute_path']
    if not os.path.exists(p):
        missing_files.append(p)

print(f"Missing physical files on disk: {len(missing_files)}")
if missing_files:
    for m in missing_files[:10]:
        print("Missing:", m)
