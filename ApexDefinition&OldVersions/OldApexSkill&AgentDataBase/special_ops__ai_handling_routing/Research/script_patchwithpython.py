content = r'''# GPT_PATCH_WORKFLOW.md
# Machine-readable process for GPT + search-replace-py local patching.
# TOKEN-EFFICIENT — follow exactly, no deviation.

---

## ROLE: GPT OUTPUT RULES (apply to every file modification)

NEVER: unified diffs, @@ hunks, +/- lines, full file rewrites
ALWAYS: SEARCH/REPLACE blocks in this exact format:

```
path/to/filename.ext
<<<<<<< SEARCH
[verbatim lines from current file, 3-5 context lines included]
=======
[replacement lines]
>>>>>>> REPLACE
```

Rules:
- SEARCH = exact copy from live file, not memory
- Block must match EXACTLY ONCE in file
- One block per logical change; multiple blocks allowed per file
- Write all blocks for one session to: patch.txt in repo root

---

## SETUP (one-time, local machine)

```bash
pip install search-replace-py
```

Save apply_patch.py once to repo root:

```python
from pathlib import Path
from search_replace import parse_edit_blocks, apply_edits
from search_replace.errors import ApplyError

llm_response = Path("patch.txt").read_text()
blocks = parse_edit_blocks(llm_response)

try:
    apply_edits(blocks.edits, root=Path("."), dry_run=True)
    print("Dry run OK — applying...")
except ApplyError as e:
    print(f"FAILED (nothing changed): {e}")
    print("Paste error + current file back to GPT. Retry.")
    exit(1)

apply_edits(blocks.edits, root=Path("."))
print("Done. Run: git diff")
```

---

## WORKFLOW (every patch session)

```
STEP 1  GPT reads target file from GitHub (live GET, not memory)
STEP 2  GPT outputs SEARCH/REPLACE blocks → saved as patch.txt in repo
STEP 3  Local: git pull origin <branch>
STEP 4  Local: python apply_patch.py
           → dry run validates ALL blocks before touching any file
           → on fail: nothing changes, error message shown
STEP 5  Local: git diff              # review changes
STEP 6  Local: git add . && git commit -m "patch: <description>" && git push
```

---

## ON FAILURE

ApplyError = SEARCH block did not match. Nothing was written.

Fix loop:
1. Copy full error message
2. Copy current file content
3. Send to GPT: "SEARCH block failed. Error: [paste]. Current file: [paste]."
4. GPT regenerates corrected block
5. Update patch.txt → re-run apply_patch.py

Matching order (auto, no config needed):
  exact match → whitespace-tolerant → ellipsis-segmented (...)
Only fails on genuine content mismatch — not indentation differences.

---

## PROHIBITIONS

- Never skip dry_run=True
- Never edit patch.txt manually to "fix" a mismatch — regenerate via GPT
- Never apply patches across multiple files in one unreviewed run
  without checking git diff per file
'''

with open("GPT_PATCH_WORKFLOW.md", "w") as f:
    f.write(content)

print("Written.")