import re
from pathlib import Path

def get_links(p):
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
            raw_target = m.group(2)
            target = raw_target.split('#')[0]
            if not target:
                continue
            if target.startswith('http://') or target.startswith('https://'):
                continue
            resolved = (base_dir / target).resolve()
            links.append((line_idx, link_text, raw_target, resolved, resolved.exists()))
    return links

files_to_check = [
    Path('apex-meta/informatics/final/index.md'),
    Path('apex-meta/informatics/final/research/06-layered-rule-kb/index.md'),
    Path('apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md'),
] + list(Path('apex-meta/informatics/final/research/06-layered-rule-kb').glob('*.md'))

total_links = 0
total_broken = 0

for f in files_to_check:
    links = get_links(f)
    broken = [l for l in links if not l[4]]
    total_links += len(links)
    total_broken += len(broken)
    if broken:
        print(f"File {f}: {len(links)} links, {len(broken)} BROKEN:")
        for line_idx, text, raw, resolved, exists in broken:
            print(f"  Line {line_idx}: [{text}]({raw}) -> {resolved}")
    else:
        # print(f"File {f.name}: {len(links)} links OK")
        pass

print(f"\nChecked {len(files_to_check)} files.")
print(f"Total relative markdown links evaluated: {total_links}")
print(f"Total broken links found: {total_broken}")
