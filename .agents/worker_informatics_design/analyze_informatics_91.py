import json
import os

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_verified_91.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

print(f"Total files: {len(files)}")

# Group by directory cluster
clusters = {}
status_map = {}
for f in files:
    p = f['path']
    st = f['status']
    status_map[st] = status_map.get(st, 0) + 1
    
    # cluster
    if '.claude\\skills' in p:
        skill_name = p.split('.claude\\skills\\')[1].split('\\')[0]
        cname = f"GitDev: .claude\\skills\\{skill_name}"
    elif 'apex-meta\\informatics' in p:
        cname = "GitDev: apex-meta\\informatics"
    elif 'apex-meta\\orchestration\\agents\\informatics-design' in p:
        cname = "GitDev: apex-meta\\orchestration\\agents\\informatics-design"
    elif 'apex-meta\\orchestration\\schemas' in p:
        cname = "GitDev: apex-meta\\orchestration\\schemas"
    elif '.claude\\agents' in p:
        cname = "GitDev: .claude\\agents"
    elif 'managed\\agent_kb\\special_ops__informatics_design' in p:
        cname = "QuasiDesktop: managed\\agent_kb\\special_ops__informatics_design"
    elif 'openclaw_setup' in p:
        cname = "QuasiDesktop: openclaw_setup"
    elif 'managed\\agents' in p:
        cname = "QuasiDesktop: managed\\agents"
    elif 'agent_kb_source_indexes' in p:
        cname = "QuasiDesktop: agent_kb_source_indexes"
    else:
        cname = "Other: " + os.path.dirname(p)
    clusters[cname] = clusters.get(cname, 0) + 1

print("\nStatus distribution:")
for k, v in status_map.items():
    print(f"  {k}: {v}")

print("\nCluster distribution:")
for k, v in sorted(clusters.items(), key=lambda x: x[1], reverse=True):
    print(f"  {k}: {v}")

print("\nTop 15 files by score:")
for i, f in enumerate(files[:15], 1):
    print(f"{i:2d}. [{f['score']:.2f}] {f['file_name']} ({f['actual_size']:,} B, {f['actual_lines']} L, {f['status']}) - {f['path']}")

# Check stubs
print("\nEmpty scaffolds / stubs:")
stubs = [f for f in files if f['status'] == 'Empty Scaffold / Stub' or f['score'] < 5.0 or 'empty' in f['file_name'].lower()]
for s in stubs:
    print(f"  - {s['file_name']} ({s['actual_size']} B, {s['actual_lines']} L, score {s['score']}) -> {s['path']}")
