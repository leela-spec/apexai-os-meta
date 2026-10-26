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

print("Checking Option C token counts in Section 3 of each file:")
for fname in files:
    fpath = os.path.join(base_dir, fname)
    with open(fpath, "r", encoding="utf-8") as f:
        content = f.read()

    m = re.search(r"\|\s*\*\*3\.\s*Aggressive Alternative[^\*]*\*\*\s*\|\s*`([^`]+)`\s*\|\s*\*\*`?(\d+)`?\*\*\s*\|", content)
    if m:
        text = m.group(1).strip()
        claimed_bpe = int(m.group(2))
        actual_bpe = len(enc.encode(text))
        print(f"{fname}: Claimed BPE = {claimed_bpe}, Actual BPE = {actual_bpe}, Match = {claimed_bpe == actual_bpe}")
        if claimed_bpe != actual_bpe:
            print(f"  MISMATCH in {fname}: claimed {claimed_bpe} != actual {actual_bpe}")
            print(f"  Text was: {text}")
    else:
        print(f"{fname}: Could not parse Option C row in Section 3!")
