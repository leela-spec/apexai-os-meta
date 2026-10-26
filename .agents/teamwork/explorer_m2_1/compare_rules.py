import re
from pathlib import Path
import tiktoken

enc = tiktoken.get_encoding('cl100k_base')

repo_root = Path(r"c:\GitDev\apexai-os-meta")
base = repo_root / "apex-meta" / "informatics" / "Agent_Setup" / "NextIteration" / "v2-always-on-architecture"

f3a_text = (base / "13-candidate-3A-xml.md").read_text(encoding="utf-8")
f3b_text = (base / "14-candidate-3B-hybrid.md").read_text(encoding="utf-8")
f03_text = (base / "03-BLUEPRINT-agents.md").read_text(encoding="utf-8")

# Extract the code blocks from 13 and 14
match_3a = re.search(r'```xml\s*(<apex_contract[\s\S]*?</apex_contract>)\s*```', f3a_text)
match_3b = re.search(r'```xml\s*(<apex_contract[\s\S]*?</apex_contract>)\s*```', f3b_text)

block_3a = match_3a.group(1)
block_3b = match_3b.group(1)

def split_markdown_cells(row: str):
    cells = re.split(r'(?<!\\)\|', row)
    clean = [c.strip().replace(r'\|', '|') for c in cells]
    if clean and clean[0] == '':
        clean.pop(0)
    if clean and clean[-1] == '':
        clean.pop()
    return clean

print("=" * 70)
print("1. RULE-BY-RULE EQUIVALENCE AUDIT (3A vs 3B)")
print("=" * 70)

unconditional_names = [
    "target", "product_first", "scope", "communication", "hold_position",
    "ground", "reuse", "context", "recovery", "stop_repairing",
    "current_truth", "surgical"
]

print("\n--- A. Unconditional Invariants (12 rules) ---")
for name in unconditional_names:
    pat = rf'<{name}>([\s\S]*?)</{name}>'
    m3a = re.search(pat, block_3a)
    m3b = re.search(pat, block_3b)
    if not m3a or not m3b:
        print(f"ERROR: missing tag <{name}> in 3A or 3B!")
        continue
    body_a = m3a.group(1).strip()
    body_b = m3b.group(1).strip()
    match = (body_a == body_b)
    print(f"  <{name}>: {'IDENTICAL' if match else 'DIFFERENT'}")
    if not match:
        print(f"    3A: {body_a}")
        print(f"    3B: {body_b}")

print("\n--- B. Conditional Gates (9 rules) ---")
conditional_3a_tags = [
    "editing", "new_machinery", "detour", "authoring",
    "trade_off", "handover", "iterative", "schemas", "sync"
]

table_match = re.search(r'<conditional_rules[^>]*>([\s\S]*?)</conditional_rules>', block_3b)
table_text = table_match.group(1).strip()
table_rows = []
for line in table_text.splitlines():
    sline = line.strip()
    if sline.startswith("|") and not sline.startswith("| When") and not sline.startswith("|---"):
        parts = split_markdown_cells(sline)
        table_rows.append(parts)

print(f"Parsed {len(conditional_3a_tags)} conditional tags in 3A and {len(table_rows)} table rows in 3B.")

diff_count = 0
for idx, tag_name in enumerate(conditional_3a_tags):
    pat = rf'<{tag_name}\s+([^>]*)>([\s\S]*?)</{tag_name}>'
    m3a = re.search(pat, block_3a)
    attrs_str = m3a.group(1)
    body_a = m3a.group(2).strip()

    when_match = re.search(r'when="([^"]*)"', attrs_str)
    ref_match = re.search(r'ref="([^"]*)"', attrs_str)

    when_a = when_match.group(1) if when_match else ""
    ref_a = ref_match.group(1) if ref_match else ""

    row_3b = table_rows[idx]
    when_b = row_3b[0]
    body_b = row_3b[1]
    ref_b = row_3b[2]

    # Normalize backticks and em-dash
    ref_b_clean = ref_b.replace("`", "").strip()
    if ref_b_clean in ["—", "-", "–", ""]:
        ref_b_clean = ""

    ref_equiv = (ref_a == ref_b_clean)

    body_b_nobackticks = body_b.replace("`", "")
    body_a_nobackticks = body_a.replace("`", "")
    body_equiv = (body_a_nobackticks == body_b_nobackticks)

    # When clause normalization (case and leading 'the' / 'about to')
    when_a_norm = when_a.lower().strip()
    when_b_norm = when_b.lower().strip()

    print(f"\nRule #{idx+1} [<{tag_name}> vs Table Row {idx+1}]:")
    print(f"  When condition:")
    print(f"    3A: \"{when_a}\"")
    print(f"    3B: \"{when_b}\"")
    print(f"  Ref pointer:")
    print(f"    3A: \"{ref_a}\"")
    print(f"    3B: \"{ref_b}\" (clean: \"{ref_b_clean}\") -> Ref Equiv: {ref_equiv}")
    print(f"  Operative body:")
    print(f"    3A: {body_a}")
    print(f"    3B: {body_b}")
    print(f"  Body text equivalence (ignoring markdown backticks): {body_equiv}")

    if not body_equiv or not ref_equiv:
        diff_count += 1

print(f"\nTotal semantic/operative body discrepancies: {diff_count}")

print("\n--- C. Terminal Guard / Scoping Note Equivalence ---")
pat_pointers = r'<pointers>([\s\S]*?)</pointers>'
m_ptr = re.search(pat_pointers, block_3a)
ptr_text = m_ptr.group(1).strip() if m_ptr else ""

m_cr_note = re.search(r'<conditional_rules\s+note="([^"]*)"', block_3b)
cr_note = m_cr_note.group(1) if m_cr_note else ""

print(f"3A <pointers>: \"{ptr_text}\"")
print(f"3B note attribute: \"{cr_note}\"")
