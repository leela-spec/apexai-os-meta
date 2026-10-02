import json
import os

with open('c:/GitDev/apexai-os-meta/.agents/worker_informatics_design/informatics_categorized_91.json', 'r', encoding='utf-8') as f:
    files = json.load(f)

print(f"Total files: {len(files)}")
total_bytes = sum(f['actual_size'] for f in files)
total_lines = sum(f['actual_lines'] for f in files)
print(f"Total actual bytes: {total_bytes:,}")
print(f"Total actual lines: {total_lines:,}")

# Status counts
status_counts = {}
for f in files:
    s = f['status']
    status_counts[s] = status_counts.get(s, 0) + 1
print("Status counts:", status_counts)

# Repo distribution
repo_counts = {'GitDev': 0, 'Quasi': 0}
for f in files:
    if 'apexai-os-meta' in f['path']:
        repo_counts['GitDev'] += 1
    else:
        repo_counts['Quasi'] += 1
print("Repo counts:", repo_counts)

# Score tiers
tiers = {'Tier S (9.0+)': 0, 'Tier A (8.0-8.99)': 0, 'Tier B (7.0-7.99)': 0, 'Tier C (5.0-6.99)': 0, 'Tier D (<5.0)': 0}
for f in files:
    sc = f['score']
    if sc >= 9.0:
        tiers['Tier S (9.0+)'] += 1
    elif sc >= 8.0:
        tiers['Tier A (8.0-8.99)'] += 1
    elif sc >= 7.0:
        tiers['Tier B (7.0-7.99)'] += 1
    elif sc >= 5.0:
        tiers['Tier C (5.0-6.99)'] += 1
    else:
        tiers['Tier D (<5.0)'] += 1
print("Tiers:", tiers)

# Top 25 files
print("\nTop 25 files:")
files_sorted = sorted(files, key=lambda x: x['score'], reverse=True)
for i, f in enumerate(files_sorted[:25], 1):
    print(f"{i:2d}. {f['file_name']} | Comp: {f['score']:.2f} | Q:{f['quality']} Qt:{f['quantity']} MR:{f['machine_readability']} OV:{f['operational_value']} | {f['actual_size']:,} B | {f['actual_lines']} L | {f['status']} | {f['category']}")

# Stubs
print("\nStubs count:")
stubs = [f for f in files if f['status'] == 'Empty Scaffold / Stub']
print(f"Total stubs: {len(stubs)}")
for s in stubs:
    print(f"  {s['file_name']} | {s['actual_size']} B | {s['actual_lines']} L | {s['path']}")
