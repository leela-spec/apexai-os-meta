import json

d = json.load(open(r'c:\GitDev\apexai-os-meta\.agents\explorer_survey\detailed_agent_dossiers.json', encoding='utf-8'))
for k, v in d.items():
    print(f"=== {k} (Total: {v['total_files']}, Stubs: {v['stub_count']}) ===")
    print("Status counts:", v['status_breakdown'])
    print("Path clusters:", v['path_clusters'])
    print("Top 3 files:")
    for i, t in enumerate(v['top_10'][:3]):
        print(f"  #{i+1}: {t['file_name']} (Comp: {t['score']}) [Exists: {t['exists']}, ActualSize: {t['actual_size']}]")
        print(f"      Path: {t['path']}")
    print()
