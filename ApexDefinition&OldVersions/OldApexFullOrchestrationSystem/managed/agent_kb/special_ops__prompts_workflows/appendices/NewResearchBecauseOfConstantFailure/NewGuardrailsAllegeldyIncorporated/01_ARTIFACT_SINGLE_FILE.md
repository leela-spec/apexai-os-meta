[ARTIFACT_BLOCK v1.0]
TRIGGER: task requires writing one file

FORMAT:
```
# FILE: {FILENAME.ext}
# SCOPE: {one-line task description}
# GATE: move-only | no-expand | locked
---
{file content here — nothing else}
```

RULES:
- Code block opens with # FILE: line — no exceptions
- No text before opening ```
- No text after closing ```
- File content begins immediately after ---
- No inline comments unless file type requires them
- If content exceeds response limit: output SPLIT_SIGNAL (see TEMPLATE_05)
