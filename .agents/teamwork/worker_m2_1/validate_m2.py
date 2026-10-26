import os
import re

base = r'c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb'
files = [
    'rule-09-recovery.md',
    'rule-10-stop-repairing.md',
    'rule-11-current-truth.md',
    'rule-12-surgical.md',
    'rule-13-editing.md',
    'rule-14-new-machinery.md',
    'rule-15-detour.md'
]

total_links = 0
broken_links = 0

for f in files:
    fpath = os.path.join(base, f)
    assert os.path.exists(fpath), f'Missing {f}'
    with open(fpath, encoding='utf-8') as fp:
        content = fp.read()
    
    # Check frontmatter
    assert content.startswith('---'), f'{f}: missing frontmatter start'
    assert 'type: Reference' in content, f'{f}: missing type Reference'
    assert 'status: current_truth' in content, f'{f}: missing status current_truth'
    
    # Check 5 sections
    assert 'Position in Layered Knowledge Base:' in content, f'{f}: missing Layer Positioning'
    assert '## 1. Original Rule & Atomic Semantic Block Inventory' in content, f'{f}: missing Section 1'
    assert '## 2. Chapter-by-Chapter Semantic Block Analysis & Alternatives' in content, f'{f}: missing Section 2'
    assert '## 3. Whole-Rule Recomposition Rollup' in content, f'{f}: missing Section 3'
    assert '## 4. Complete Bidirectional Research & Provenance Links' in content, f'{f}: missing Section 4'
    assert '## 5. Failure Modes & Not-To-Dos' in content, f'{f}: missing Section 5'
    
    # Check links
    links = re.findall(r'\[.*?\]\((.*?)\)', content)
    for l in links:
        if l.startswith('http'):
            continue
        total_links += 1
        unquoted = l.replace('%20', ' ')
        target = os.path.normpath(os.path.join(base, unquoted))
        if not os.path.exists(target):
            print(f'BROKEN in {f}: {l} -> {target}')
            broken_links += 1

print(f'Checked {len(files)} files.')
print(f'Total relative links verified: {total_links}')
print(f'Broken relative links: {broken_links}')
assert broken_links == 0, 'Found broken links!'
print('ALL M2 FILES PASSED INTEGRITY AND LINK VALIDATION!')
