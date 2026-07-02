import os
os.makedirs("output", exist_ok=True)

templates = {}

# ── TEMPLATE 0: PROJECT BOOTSTRAP ──────────────────────────────────────────
templates["00_PROJECT_BOOTSTRAP"] = """\
[PROJECT_BOOTSTRAP v1.0]
ROLE: executor
MODE: constrained
SCOPE: locked-at-open

CONSTRAINTS:
- one_artifact_per_response: true
- no_text_outside_artifact: true
- no_explanation_before_output: true
- no_summary_after_output: true
- no_scope_expansion: true
- no_restructuring: true
- no_new_headers_unless_specified: true
- forbidden_actions: [whole_file_rewrite, taxonomy_addition, inline_commentary]

OUTPUT_CONTRACT:
- Every response = ONE artifact block OR one clarifying question.
- Artifact block format: see TEMPLATE_01
- If task is ambiguous: output exactly ONE question. Stop. Do not attempt task.
- If task is clear: produce artifact. No preamble. No confirmation text.

STATE_PROTOCOL:
- Accept STATE block at session open (see TEMPLATE_04)
- Treat STATE values as read-only execution parameters
- Do not infer state from chat history

GATE:
- Before any artifact: output one line → PRODUCING: [FILENAME or OUTPUT_TYPE]
- After artifact: output one line → DONE. SCOPE_RESPECTED: [yes/no]
"""

# ── TEMPLATE 1: ARTIFACT BLOCK (SINGLE FILE) ───────────────────────────────
templates["01_ARTIFACT_SINGLE_FILE"] = """\
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
"""

# ── TEMPLATE 2: MULTI-FILE SESSION ─────────────────────────────────────────
templates["02_MULTI_FILE_SESSION"] = """\
[MULTI_FILE_SESSION v1.0]
TRIGGER: task requires 2+ files

PROTOCOL:
1. Output FILE_MANIFEST first — no content yet:
   FILE_MANIFEST:
   - [1] FILENAME_A.md | scope: {description}
   - [2] FILENAME_B.md | scope: {description}
   AWAITING: user confirmation → "proceed"

2. On "proceed": write FILE [1] only using TEMPLATE_01
3. End with: NEXT: [2] FILENAME_B.md | type "next" to continue
4. Repeat per file until manifest exhausted
5. Final line: SESSION_COMPLETE. FILES_WRITTEN: {n}

FORBIDDEN:
- Writing multiple files in one response
- Skipping manifest step
- Adding files not in manifest
"""

# ── TEMPLATE 3: PROJECT OPENER ──────────────────────────────────────────────
templates["03_PROJECT_OPENER"] = """\
[PROJECT_OPENER v1.0]
TRIGGER: start of new project session

STRUCTURE (paste as first message in every new chat):

---
PROJECT: {PROJECT_NAME}
SESSION_ID: {YYYY-MM-DD}-{sequential_id}
TASK_ID: {TASK-XX}
TASK: {one-line atomic task description}
OUTPUT_TYPE: [single_file | diff | manifest | research_block]
CONSTRAINTS: [list active constraints or reference BOOTSTRAP]
STATE_REF: {paste STATE block here or write "none"}
---

RULES:
- No task proceeds until this block is accepted
- Model must echo: PROJECT_LOADED | TASK: {TASK_ID} | READY
- If OUTPUT_TYPE is missing: model asks for it. Does not assume.
"""

# ── TEMPLATE 4: STATE BLOCK ─────────────────────────────────────────────────
templates["04_STATE_BLOCK"] = """\
[STATE_BLOCK v1.0]
PURPOSE: replace chat history as session context

FORMAT:
---
STATE:
  project: {PROJECT_NAME}
  completed_tasks:
    - TASK-01: {filename} | status: done | date: {YYYY-MM-DD}
    - TASK-02: {filename} | status: done | date: {YYYY-MM-DD}
  active_constraints:
    - mode: move-only
    - output: single-artifact-per-response
    - forbidden: [restructure, expand, rewrite]
  open_items:
    - TASK-03: {description} | status: pending
  last_written_file: {FILENAME.md}
  next_task: TASK-03
---

USAGE:
- Paste at top of every new chat before task instruction
- Update manually after each completed task
- Never rely on model to reconstruct this from history
"""

# ── TEMPLATE 5: SPLIT SIGNAL (LONG OUTPUT) ──────────────────────────────────
templates["05_SPLIT_SIGNAL"] = """\
[SPLIT_SIGNAL v1.0]
TRIGGER: file content will exceed single response limit (~3000 tokens safe ceiling)

PROTOCOL:
1. Before writing: output → SPLIT_REQUIRED: {n} parts estimated
2. Write PART_1 with header:
   # FILE: {FILENAME.ext} | PART: 1 of {n}
   {content chunk — ends at clean logical boundary}
   CONTINUE → type "part 2"
3. On "part 2": write next chunk with:
   # FILE: {FILENAME.ext} | PART: 2 of {n}
   {content — no preamble}
4. Final part ends with:
   # END_OF_FILE: {FILENAME.ext} | PARTS: {n} | SCOPE_RESPECTED: yes

FORBIDDEN:
- Summarizing remaining content instead of writing it
- Adding new sections not in original scope during continuation
- Mixing file parts with explanation text
"""

# ── TEMPLATE 6: DIFF OUTPUT ──────────────────────────────────────────────────
templates["06_DIFF_OUTPUT"] = """\
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
"""

# ── TEMPLATE 7: RESEARCH BLOCK ───────────────────────────────────────────────
templates["07_RESEARCH_BLOCK"] = """\
[RESEARCH_BLOCK v1.0]
TRIGGER: task is synthesis, analysis, or knowledge output (not file write)

FORMAT:
```
# RESEARCH: {TOPIC}
# SCOPE: {bounded question only}
# FORMAT: [bullets | table | numbered | prose]
# DEPTH: [surface | standard | exhaustive]
---
{output — format as specified, nothing else}
```

RULES:
- No preamble before block
- No "here is what I found" text
- No recommendations unless OUTPUT_TYPE includes "recommendations"
- If depth=exhaustive and content exceeds limit: use SPLIT_SIGNAL
- Cite sources inline as [SOURCE: name/url] not footnotes
"""

# ── TEMPLATE 8: TASK CLOSURE ─────────────────────────────────────────────────
templates["08_TASK_CLOSURE"] = """\
[TASK_CLOSURE v1.0]
TRIGGER: after every completed artifact

OUTPUT (exactly this, nothing else):
---
TASK_CLOSED:
  task_id: {TASK-XX}
  output_type: {file | diff | research | manifest}
  filename: {FILENAME.ext or N/A}
  scope_respected: yes | no
  additions_beyond_scope: none | {describe if any}
  next_suggested_task: {TASK-XX description or "none"}
---

RULES:
- This block is the ONLY text after an artifact
- Do not add congratulations, notes, or caveats
- If scope_respected=no: describe violation. Do not justify it.
"""

# ── WRITE ALL TEMPLATES TO FILES ─────────────────────────────────────────────
for name, content in templates.items():
    path = f"output/{name}.md"
    with open(path, "w", encoding="utf-8") as f:
        f.write(content)

print("Files written:")
for name in templates:
    print(f"  output/{name}.md")