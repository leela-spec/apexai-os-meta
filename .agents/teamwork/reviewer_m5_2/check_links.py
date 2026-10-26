import re
import sys
from pathlib import Path

def check_links(file_path):
    p = Path(file_path)
    base_dir = p.parent
    text = p.read_text(encoding='utf-8')
    lines = text.splitlines()
    in_fence = False
    links = []
    for line_idx, line in enumerate(lines, 1):
        if line.strip().startswith('```'):
            in_fence = not in_fence
            continue
        if in_fence:
            continue
        for m in re.finditer(r'\[([^\]]+)\]\(([^)]+)\)', line):
            link_text = m.group(1)
            target = m.group(2).split('#')[0]
            if not target:
                continue
            links.append((line_idx, link_text, m.group(2), target))
    
    results = []
    for line_idx, link_text, raw_target, target in links:
        resolved = (base_dir / target).resolve()
        exists = resolved.exists()
        is_file = resolved.is_file()
        is_dir = resolved.is_dir()
        results.append({
            'line': line_idx,
            'text': link_text,
            'raw_target': raw_target,
            'resolved': str(resolved),
            'exists': exists,
            'is_file': is_file,
            'is_dir': is_dir
        })
    return results

f1 = 'apex-meta/informatics/final/index.md'
f2 = 'apex-meta/informatics/final/research/06-layered-rule-kb/index.md'

print(f"=== Checking {f1} ===")
r1 = check_links(f1)
failed1 = [x for x in r1 if not x['exists']]
print(f"Total links: {len(r1)}, Missing: {len(failed1)}")
for x in failed1:
    print(f"  Line {x['line']}: [{x['text']}]({x['raw_target']}) -> NOT FOUND at {x['resolved']}")
if not failed1:
    print("  ALL LINKS RESOLVED SUCCESSFULLY!")

print(f"\n=== Checking {f2} ===")
r2 = check_links(f2)
failed2 = [x for x in r2 if not x['exists']]
print(f"Total links: {len(r2)}, Missing: {len(failed2)}")
for x in failed2:
    print(f"  Line {x['line']}: [{x['text']}]({x['raw_target']}) -> NOT FOUND at {x['resolved']}")
if not failed2:
    print("  ALL LINKS RESOLVED SUCCESSFULLY!")

if failed1 or failed2:
    sys.exit(1)
else:
    sys.exit(0)
