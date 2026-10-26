import os
import re
import tiktoken

enc = tiktoken.get_encoding("cl100k_base")
base_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"

rule_files = [
    "rule-16-authoring.md",
    "rule-17-trade-off.md",
    "rule-18-handover.md",
    "rule-19-iterative.md",
    "rule-20-schemas.md",
    "rule-21-sync.md",
    "rule-22-pointers.md"
]

print("=== RECOMPUTING BPE TOKEN COUNTS ===")
for rf in rule_files:
    path = os.path.join(base_dir, rf)
    with open(path, "r", encoding="utf-8") as f:
        lines = f.readlines()
    
    in_table = False
    print(f"\n--- {rf} ---")
    for line in lines:
        if line.startswith("## 3. Whole-Rule Recomposition Rollup"):
            in_table = True
            continue
        if in_table and line.startswith("## 4."):
            in_table = False
            break
        if in_table and line.startswith("| **"):
            # Line format: | **<Option>** | `<text>` | **`<bpe>`** | ...
            # Split by ` | ` but be careful about pipes inside code blocks
            # Find the backticked code:
            code_match = re.search(r"`(<[^>]+>.*?</[^>]+>|<pointers>.*?</pointers>)`", line)
            bpe_match = re.search(r"\*\*\s*`?(\d+)`?\s*\*\*", line[code_match.end():] if code_match else "")
            
            if code_match and bpe_match:
                code_text = code_match.group(1)
                reported_bpe = int(bpe_match.group(1))
                actual_bpe = len(enc.encode(code_text))
                option_name = line.split("|")[1].strip()
                match_status = "EXACT MATCH" if actual_bpe == reported_bpe else f"DELTA ({actual_bpe - reported_bpe:+d})"
                print(f"  {option_name:40s} | Reported: {reported_bpe:3d} | Actual: {actual_bpe:3d} | {match_status}")
            else:
                print(f"  Could not parse table row: {line.strip()}")
