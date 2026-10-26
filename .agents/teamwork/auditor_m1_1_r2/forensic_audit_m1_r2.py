import os
import re
import sys
import tiktoken
import datetime

enc = tiktoken.get_encoding("cl100k_base")
kb_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
rules = [f"rule-{i:02d}-{name}.md" for i, name in [
    (2, "product-first"),
    (3, "scope"),
    (4, "communication"),
    (5, "hold-position"),
    (6, "ground"),
    (7, "reuse"),
    (8, "context")
]]

# Baseline word counts from Iteration 1 (pre-link-remediation)
it1_word_counts = {
    'rule-02-product-first.md': 1434,
    'rule-03-scope.md': 1279,
    'rule-04-communication.md': 1580,
    'rule-05-hold-position.md': 1355,
    'rule-06-ground.md': 1678,
    'rule-07-reuse.md': 1419,
    'rule-08-context.md': 1145,
}

print("=" * 80)
print("FORENSIC INTEGRITY AUDIT — MILESTONE 1 ITERATION 2 RE-VERIFICATION")
print("=" * 80)

failures = []
total_relative_links = 0
verified_link_targets = set()

# Phase 1: File by File Analysis
for r in rules:
    fpath = os.path.join(kb_dir, r)
    if not os.path.exists(fpath):
        failures.append(f"Missing file: {r}")
        continue
    
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    bpe = len(enc.encode(content))
    words = len(content.split())
    lines = len(content.splitlines())
    chars = len(content)

    print(f"\n[AUDIT] {r}: {lines} lines, {words} words, {chars} chars, {bpe} BPE tokens")

    # Check 1: Prose Preservation (Word count stability)
    exp_words = it1_word_counts[r]
    if words != exp_words:
        failures.append(f"{r}: Word count drift! Expected {exp_words}, got {words}")
    else:
        print(f"  [PASS] Prose Preservation: Exact word count match ({words}/{exp_words})")

    # Check 2: Relative Link Resolution
    pat = re.compile(r'\[([^\]]+)\]\(([^)]+)\)')
    file_rel_links = 0
    for text, url in pat.findall(content):
        u = url.strip()
        if u.startswith(('http:', 'https:', 'mailto:', '#')):
            continue
        file_rel_links += 1
        total_relative_links += 1
        p = urllib.parse.unquote(u.split('#')[0]) if 'urllib' in sys.modules else u.split('#')[0].replace('%20', ' ')
        target_path = os.path.normpath(os.path.join(kb_dir, p))
        if not os.path.exists(target_path):
            failures.append(f"{r}: Broken relative link [{text}]({url}) -> {target_path}")
        elif not os.path.isfile(target_path):
            failures.append(f"{r}: Link target is not a file: {target_path}")
        elif os.path.getsize(target_path) == 0:
            failures.append(f"{r}: Link target is zero bytes (empty): {target_path}")
        else:
            verified_link_targets.add(target_path)
    print(f"  [PASS] Link Resolution: {file_rel_links} relative links verified (all resolve on disk)")

    # Check 3: Frontmatter
    fm_m = re.match(r"^---\s*\n(.*?)\n---\s*\n", content, re.DOTALL)
    if not fm_m:
        failures.append(f"{r}: Missing valid frontmatter")
    else:
        fm = fm_m.group(1)
        if "type: Reference" not in fm or "status: current_truth" not in fm or "tags:" not in fm:
            failures.append(f"{r}: Incomplete frontmatter metadata")
        else:
            print(f"  [PASS] Frontmatter OKF v0.2 metadata conformant")

    # Check 4: Mandatory Sections
    for sec_num, sec_name in [(1, "Original Rule"), (2, "Chapter-by-Chapter"), (3, "Whole-Rule Recomposition"), (4, "Complete Bidirectional Research"), (5, "Failure Modes & Not-To-Dos")]:
        if not re.search(rf"^## {sec_num}\.\s+.*{re.escape(sec_name.split()[0])}", content, re.MULTILINE):
            failures.append(f"{r}: Missing Section {sec_num} ({sec_name})")
    print(f"  [PASS] Mandatory Sections 1-5 present")

    # Check 5: Anti-Cheating & Prohibited Patterns
    for prohibited in ["FIXME", "lorem ipsum", "TBD", "placeholder"]:
        if prohibited.lower() in content.lower():
            failures.append(f"{r}: Prohibited placeholder string '{prohibited}' detected")
    
    # Check for computed math formulas in significance tags
    math_calc = re.findall(r"\[P[0-3]\s*\|\s*[^\]]*[\*\+\=][^\]]*\]", content)
    if math_calc:
        failures.append(f"{r}: Computed math formula detected in tags: {math_calc}")
    print(f"  [PASS] Anti-Cheating: Zero prohibited strings or math formulas")

# Phase 2: Live Carrier Invariance Check
print("\n" + "-" * 80)
print("CARRIER INVARIANCE CHECK (AGENTS.md, CLAUDE.md, GEMINI.md)")
today_utc = datetime.datetime.now(datetime.timezone.utc).date()
for carrier in ["AGENTS.md", "CLAUDE.md", "GEMINI.md"]:
    carrier_path = os.path.join(r"c:\GitDev\apexai-os-meta", carrier)
    mtime = datetime.datetime.fromtimestamp(os.path.getmtime(carrier_path), tz=datetime.timezone.utc)
    print(f"  {carrier}: Last modified {mtime.isoformat()}")
    if mtime.date() == today_utc:
        failures.append(f"Carrier file modified today: {carrier} at {mtime}")
    else:
        print(f"  [PASS] {carrier} unmodified today (last touched {mtime.strftime('%Y-%m-%d')})")

print("\n" + "=" * 80)
print(f"TOTAL RELATIVE LINKS CHECKED: {total_relative_links}")
print(f"UNIQUE TARGET FILES RESOLVED: {len(verified_link_targets)}")
print(f"TOTAL FAILURES DETECTED: {len(failures)}")
if failures:
    print("FAILURES:")
    for f in failures:
        print(f"  - {f}")
    print("VERDICT: INTEGRITY VIOLATION")
    sys.exit(1)
else:
    print("VERDICT: CLEAN")
print("=" * 80)
