import urllib.parse
from pathlib import Path
import re

REPO_ROOT = Path('.').resolve()

def check_file(p):
    content = p.read_text(encoding='utf-8')
    without_fences = re.sub(r'```[\s\S]*?```', '', content)
    stripped = re.sub(r'`[^`\n]*`', '', without_fences)
    broken = []
    total = 0
    for anchor, raw_link in re.findall(r'\[([^\]]*)\]\(([^)\s]+)\)', stripped):
        if raw_link.startswith(('http://', 'https://', 'mailto:', '#')):
            continue
        clean_target = raw_link.split('#')[0]
        if not clean_target:
            continue
        total += 1
        unquoted = urllib.parse.unquote(clean_target)
        if unquoted.startswith('/'):
            resolved = (REPO_ROOT / unquoted.lstrip('/')).resolve()
        else:
            resolved = (p.parent / unquoted).resolve()
        if not resolved.exists():
            broken.append((anchor, raw_link, str(resolved)))
    return total, broken

targets = [
    Path('apex-meta/informatics/final/index.md'),
    Path('apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md'),
] + sorted(list(Path('apex-meta/informatics/final/research/06-layered-rule-kb').glob('*.md')))

all_broken = {}
grand_total = 0
for t in targets:
    tot, brk = check_file(t)
    grand_total += tot
    if brk:
        all_broken[t.name] = brk

print(f'Total links checked across {len(targets)} files: {grand_total}')
print(f'Files with broken links: {len(all_broken)}')
for fname, brk in all_broken.items():
    print(f'\n{fname}:')
    for a, r, res in brk:
        print(f'  [{a}]({r}) -> {res}')
