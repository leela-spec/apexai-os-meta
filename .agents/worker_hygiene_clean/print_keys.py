import json
with open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', 'r', encoding='utf-8') as f:
    data = json.load(f)
for k in data.keys():
    print(repr(k))
