import os
import re
import tiktoken

base_dir = r"c:\GitDev\apexai-os-meta\apex-meta\informatics\final\research\06-layered-rule-kb"
files = [
    "rule-09-recovery.md",
    "rule-10-stop-repairing.md",
    "rule-11-current-truth.md",
    "rule-12-surgical.md",
    "rule-13-editing.md",
    "rule-14-new-machinery.md",
    "rule-15-detour.md",
]

enc = tiktoken.get_encoding("cl100k_base")

print("Checking Section 1.2 Semantic Block token counts:")
all_sb_match = True
for fname in files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    # Pattern: - **`SB-XX.Y` — Name (`ZZ BPE tokens` | `WW chars`):** *"..."*
    matches = re.findall(r"- \*\*`(SB-\d+\.\d+)`[^\(]*\(`(\d+) BPE tokens`\s*\|\s*`(\d+) chars`\):\*\*\s*\*\"([^\"]+)\"\*", content)
    for sb_id, claimed_bpe, claimed_chars, text in matches:
        actual_bpe = len(enc.encode(text))
        actual_chars = len(text)
        match_bpe = (int(claimed_bpe) == actual_bpe)
        match_chars = (int(claimed_chars) == actual_chars)
        if not (match_bpe and match_chars):
            all_sb_match = False
            print(f"[{fname}] {sb_id} MISMATCH:")
            print(f"  Claimed: {claimed_bpe} BPE, {claimed_chars} chars")
            print(f"  Actual:  {actual_bpe} BPE, {actual_chars} chars")
        else:
            print(f"[{fname}] {sb_id}: {claimed_bpe} BPE, {claimed_chars} chars -> OK")

print(f"All Semantic Blocks Verified: {all_sb_match}")
