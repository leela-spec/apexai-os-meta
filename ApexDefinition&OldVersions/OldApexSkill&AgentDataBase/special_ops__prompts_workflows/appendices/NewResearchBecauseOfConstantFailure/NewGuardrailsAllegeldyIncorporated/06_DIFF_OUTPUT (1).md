[DIFF_OUTPUT v1.0]
TRIGGER: task is a targeted edit to existing file (not full rewrite)

FORMAT:
```diff
# DIFF: {FILENAME.ext}
# SCOPE: {one-line description of change only}
# MODE: patch-only | no-restructure
---
--- a/{FILENAME.ext}
+++ b/{FILENAME.ext}
@@ -{line_start},{line_count} +{line_start},{line_count} @@
 {unchanged context line}
-{removed line}
+{added line}
 {unchanged context line}
```
AFTER_BLOCK:
DIFF_COMPLETE. LINES_CHANGED: {n}. NO_OTHER_MODIFICATIONS.

RULES:
- Max 3 lines of unchanged context per hunk
- Never output full file when diff is possible
- One hunk per logical change
- Apply via: git apply {filename}.diff
