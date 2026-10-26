import os
import re

base_kb = r'c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb'
informatics_dir = r'c:\GitDev\apexai-os-meta\apex-meta\informatics'

plane4_files = {
    'AD': os.path.join(informatics_dir, 'anti-drift-rules.md'),
    'WP': os.path.join(informatics_dir, 'writing-profile.md'),
    'EM': os.path.join(informatics_dir, 'execution-modes.md'),
    'FA': os.path.join(informatics_dir, 'file-architecture.md'),
    'GS': os.path.join(informatics_dir, 'governance-schemas.md'),
}

# Read plane 4 rule texts
plane4_rules = {}
for prefix, path in plane4_files.items():
    with open(path, encoding='utf-8') as f:
        text = f.read()
    # Find all IDs like AD-01, WP-25, etc.
    ids = set(re.findall(rf'{prefix}-\d{{2}}', text))
    plane4_rules[prefix] = ids
    print(f"Loaded {len(ids)} rule IDs for {prefix} from {os.path.basename(path)}")

rules_to_check = [
    'rule-09-recovery.md',
    'rule-10-stop-repairing.md',
    'rule-11-current-truth.md',
    'rule-12-surgical.md',
    'rule-13-editing.md',
    'rule-14-new-machinery.md',
    'rule-15-detour.md'
]

print("\n--- Verifying Plane 4 Rule IDs in M2 Files ---")
missing_ids = 0
for rfile in rules_to_check:
    fpath = os.path.join(base_kb, rfile)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    # Extract referenced rule IDs: AD-xx, WP-xx, EM-xx, FA-xx, GS-xx
    referenced_ids = set(re.findall(r'\b(AD|WP|EM|FA|GS)-(\d{2})\b', content))
    for pfx, num in referenced_ids:
        rule_id = f"{pfx}-{num}"
        if rule_id not in plane4_rules[pfx]:
            print(f"MISSING RULE ID: {rule_id} in {rfile}")
            missing_ids += 1
        else:
            # print(f"Found {rule_id} in {rfile}")
            pass

print(f"Total missing Plane 4 Rule IDs: {missing_ids}")

print("\n--- Verifying Relative File Links ---")
total_links = 0
broken_links = 0
for rfile in rules_to_check:
    fpath = os.path.join(base_kb, rfile)
    with open(fpath, encoding='utf-8') as f:
        content = f.read()
    
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    for l in links:
        if l.startswith('http') or l.startswith('#'):
            continue
        total_links += 1
        unquoted = l.split('#')[0].replace('%20', ' ')
        target = os.path.normpath(os.path.join(base_kb, unquoted))
        if not os.path.exists(target):
            print(f"BROKEN LINK in {rfile}: {l} -> {target}")
            broken_links += 1

print(f"Total checked relative links: {total_links}")
print(f"Total broken relative links: {broken_links}")
