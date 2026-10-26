import re
import sys
from pathlib import Path
import tiktoken

enc = tiktoken.get_encoding('cl100k_base')

cand_path = Path('apex-meta/informatics/final/candidates/16-candidate-3A-ultra.md')
cand_text = cand_path.read_text(encoding='utf-8')

m = re.search(r'```xml\s*\n(.*?)\n```', cand_text, re.DOTALL)
if not m:
    print("FAILED: XML block not found in candidate 16")
    sys.exit(1)

block = m.group(1)
chars = len(block)
repo = chars // 4
bpe = len(enc.encode(block))
words = len(block.split())
lines = len(block.splitlines())

print(f"Candidate 16 XML Block Metrics:")
print(f"  Chars: {chars}")
print(f"  Repo: {repo}")
print(f"  BPE: {bpe}")
print(f"  Words: {words}")
print(f"  Lines: {lines}")

expected_chars = 5917
expected_repo = 1479
expected_bpe = 1225
expected_words = 769
expected_lines = 65

metrics_match = (
    chars == expected_chars and
    repo == expected_repo and
    bpe == expected_bpe and
    words == expected_words and
    lines == expected_lines
)
print(f"  Matches documented metrics exactly: {metrics_match}")
if not metrics_match:
    print(f"  MISMATCH! Documented: chars={expected_chars}, repo={expected_repo}, bpe={expected_bpe}, words={expected_words}, lines={expected_lines}")

# Check all 22 tags
expected_tags = [
    "target", "product_first", "scope", "communication", "hold_position",
    "ground", "reuse", "context", "recovery", "stop_repairing",
    "current_truth", "surgical", "editing", "new_machinery", "detour",
    "authoring", "trade_off", "handover", "iterative", "schemas",
    "sync", "pointers"
]

print(f"\nChecking 22 tags in candidate 16:")
tag_matches = re.findall(r'<([a-z_]+)(?:\s+[^>]*?)?>', block)
# filter out root tag apex_contract
tag_matches = [t for t in tag_matches if t != "apex_contract"]
print(f"  Found {len(tag_matches)} tags: {tag_matches}")
if tag_matches == expected_tags:
    print("  Tags match expected 22 tags in exact order!")
else:
    print(f"  Tag mismatch! Diff: {set(expected_tags) ^ set(tag_matches)}")

# Verify each tag matches Option B in rule-01 to rule-22
print("\nVerifying Candidate 16 text against Option B in Layered Rule KB:")
mismatches = []
for idx, tag in enumerate(expected_tags, 1):
    rule_file = Path(f'apex-meta/informatics/final/research/06-layered-rule-kb/rule-{idx:02d}-{tag.replace("_", "-")}.md')
    if not rule_file.exists():
        # try finding by prefix
        candidates = list(Path('apex-meta/informatics/final/research/06-layered-rule-kb').glob(f'rule-{idx:02d}-*.md'))
        if candidates:
            rule_file = candidates[0]
        else:
            print(f"  Missing rule file for idx {idx} tag {tag}")
            continue
    rf_text = rule_file.read_text(encoding='utf-8')
    # find Option B block in Chapter 3
    # Look for Option B row in the rollup table or code block
    # In Chapter 3, Option B has a row or block
    # Let's extract Option B text from Candidate 16
    tag_pattern = rf'<{tag}(?:\s+[^>]*?)?>(.*?)</{tag}>'
    tag_m = re.search(tag_pattern, block, re.DOTALL)
    if not tag_m:
        print(f"  Could not find tag <{tag}> in Candidate 16")
        mismatches.append(tag)
        continue
    cand_body = tag_m.group(1).strip()
    # Check if cand_body appears in rule_file
    # Normalize whitespace for comparison
    cand_body_norm = ' '.join(cand_body.split())
    rf_text_norm = ' '.join(rf_text.split())
    if cand_body_norm in rf_text_norm:
        print(f"  Rule {idx:02d} <{tag}>: Option B matched in {rule_file.name}")
    else:
        print(f"  Rule {idx:02d} <{tag}>: WARNING - body not found verbatim in {rule_file.name}")
        mismatches.append(tag)

if not mismatches:
    print("ALL 22 RULES MATCH OPTION B SOURCE TEXT!")
else:
    print(f"Mismatches count: {len(mismatches)}")
