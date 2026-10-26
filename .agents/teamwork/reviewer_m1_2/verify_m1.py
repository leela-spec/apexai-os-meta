import re
import urllib.parse
from pathlib import Path
import tiktoken

enc = tiktoken.get_encoding('cl100k_base')
kb_dir = Path('apex-meta/informatics/final/research/06-layered-rule-kb')
files = [
    'rule-02-product-first.md',
    'rule-03-scope.md',
    'rule-04-communication.md',
    'rule-05-hold-position.md',
    'rule-06-ground.md',
    'rule-07-reuse.md',
    'rule-08-context.md'
]

print("=== AUDIT 1: RESEARCH PACKETS & PLANE 4 RULES IN SECTION 4 ===")
for fname in files:
    content = (kb_dir / fname).read_text(encoding='utf-8')
    s4_match = re.search(r'## 4\. Complete Bidirectional Research & Provenance Links.*?\n(.*?)(?=\n## 5\.|\Z)', content, re.DOTALL)
    if not s4_match:
        print(f"{fname}: Section 4 NOT FOUND")
        continue
    s4_text = s4_match.group(1)
    
    # Extract RESULTS-XX, RP-XX, Plane 4 rules
    results = re.findall(r'RESULTS-\d+(?:-[a-z0-9-]+)?', s4_text)
    rps = re.findall(r'RP-\d+', s4_text)
    ad_rules = re.findall(r'AD-\d+', s4_text)
    wp_rules = re.findall(r'WP-\d+', s4_text)
    em_rules = re.findall(r'EM-\d+', s4_text)
    fa_rules = re.findall(r'FA-\d+', s4_text)
    gs_rules = re.findall(r'GS-\d+', s4_text)
    
    # Extract markdown links in s4
    links = re.findall(r'\[([^\]]+)\]\(([^)]+)\)', s4_text)
    broken_links = []
    valid_links = []
    for lt, url in links:
        if url.startswith('http://') or url.startswith('https://'):
            valid_links.append((lt, url, 'external'))
            continue
        unquoted = urllib.parse.unquote(url.split('#')[0])
        resolved = (kb_dir / unquoted).resolve()
        if resolved.exists():
            valid_links.append((lt, url, 'local_ok'))
        else:
            broken_links.append((lt, url, str(resolved)))

    print(f"\n--- {fname} ---")
    print(f"  Research Packets: {sorted(set(rps))} | Results: {sorted(set(results))}")
    print(f"  Plane 4 Rules: AD={sorted(set(ad_rules))} WP={sorted(set(wp_rules))} EM={sorted(set(em_rules))} FA={sorted(set(fa_rules))} GS={sorted(set(gs_rules))}")
    print(f"  Links: {len(valid_links)} valid, {len(broken_links)} broken")
    if broken_links:
        for lt, url, res in broken_links:
            print(f"    BROKEN: [{lt}]({url})")

print("\n=== AUDIT 2: SECTION 5 FAILURE MODES & NOT-TO-DOS (WP-25) ===")
for fname in files:
    content = (kb_dir / fname).read_text(encoding='utf-8')
    s5_match = re.search(r'## 5\. Failure Modes & Not-To-Dos \(`WP-25`\)\n\n(.*?)(?=\n## |\Z)', content, re.DOTALL)
    if not s5_match:
        print(f"{fname}: Section 5 NOT FOUND")
        continue
    s5_text = s5_match.group(1).strip()
    bullets = [b.strip() for b in s5_text.splitlines() if b.strip().startswith('-')]
    print(f"\n--- {fname} ({len(bullets)} failure modes) ---")
    for b in bullets:
        # Check non-default emphasis
        print(f"  * {b[:90]}...")

print("\n=== AUDIT 3: FRONTMATTER & METADATA ===")
for fname in files:
    content = (kb_dir / fname).read_text(encoding='utf-8')
    fm_match = re.match(r'^---\n(.*?)\n---', content, re.DOTALL)
    if not fm_match:
        print(f"{fname}: FRONTMATTER MISSING")
        continue
    fm = fm_match.group(1)
    durable_id = re.search(r'id:\s*(\S+)', fm).group(1) if re.search(r'id:\s*(\S+)', fm) else 'NONE'
    doc_type = re.search(r'type:\s*(\S+)', fm).group(1) if re.search(r'type:\s*(\S+)', fm) else 'NONE'
    status = re.search(r'status:\s*(\S+)', fm).group(1) if re.search(r'status:\s*(\S+)', fm) else 'NONE'
    print(f"{fname:28} | id={durable_id:32} | type={doc_type:10} | status={status}")

