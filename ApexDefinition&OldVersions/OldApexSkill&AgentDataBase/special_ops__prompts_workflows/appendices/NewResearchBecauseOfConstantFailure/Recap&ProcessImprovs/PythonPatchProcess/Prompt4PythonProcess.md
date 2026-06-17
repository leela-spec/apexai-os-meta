# Role
You are a senior Python engineer and DevOps specialist with hands-on
experience deploying LLM-based patching pipelines on local machines.
You give practical, tested, step-by-step operator guidance — no theory,
no hand-waving, no unverified steps.

# Operator context (read carefully before answering anything)
The operator:
  - Uses GPT 5.5 in the browser (subscription, not API)
  - GPT has read/write access to a GitHub repo via the GitHub connector
  - The repo is also cloned to a local HDD
  - Operating system: [OPERATOR: fill in — Windows / macOS / Linux]
  - Python experience level: [OPERATOR: fill in — beginner / intermediate]
  - Goal: Use search-replace-py (PyPI: search-replace-py v0.0.2) as the
    local patch execution engine

# Intended workflow (operator's current understanding)
  STEP A — GPT (browser) reads a file in the GitHub repo, produces
           SEARCH/REPLACE patch blocks, and writes them as a .patch.md
           file into the repo via the GitHub connector.
  STEP B — Operator does: git pull  (pulls the .patch.md files locally)
  STEP C — Operator runs a local Python script that reads the .patch.md
           files, applies the SEARCH/REPLACE blocks to the target files,
           and writes the updated files back locally.
  STEP D — Operator does: git add / commit / push  (pushes results back)

# Your task
Answer the following questions IN ORDER. Do not skip any.
For each answer, be concrete and OS-specific where relevant.

---

## Q1 — Workflow validation
Is the operator's A→B→C→D workflow above the best available option
for their setup (browser GPT + GitHub connector + local clone)?

Evaluate against these alternatives:
  - Alt 1: GPT applies patches directly to repo via connector (no local step)
  - Alt 2: GPT writes patch intent, operator uses Aider CLI locally
  - Alt 3: Current A→B→C→D workflow with search-replace-py
  - Alt 4: GPT writes full file rewrites directly (no patch format)

For each alternative score:
  - Reliability (1–100): how resistant to drift / data loss
  - Simplicity (1–100): operator effort and tooling overhead
  - Speed (1–100): time from GPT output to committed result
  - Risk (1–100): chance of silent error going undetected

Give a final ranked recommendation with one sentence of reasoning per option.

---

## Q2 — Prerequisites check
What does the operator need installed before using search-replace-py?
List only the things that are genuinely required, not nice-to-have.
Format as a checklist the operator can run through in under 5 minutes.
Include the exact terminal command to verify each prerequisite is met.

---

## Q3 — Installation
Provide the exact installation commands for:
  a) macOS
  b) Windows (PowerShell)
  c) Linux (Ubuntu/Debian)

Use a virtual environment. Show each step. Keep it minimal — do not
install anything not required for this specific use case.

---

## Q4 — Patch file format contract
What exact format must the .patch.md files follow so that
search-replace-py can parse them without errors?

Provide:
  - The canonical block format (copy-pasteable example)
  - Rules for what makes a SEARCH block valid vs invalid
  - What happens on parse failure (error type, behavior)
  - How to handle multi-block patches (multiple changes to one file)
  - How to handle patches that touch multiple files

---

## Q5 — The runner script
Write a minimal, production-ready Python script the operator can save
as  run_patches.py  in their repo root.

The script must:
  - Accept a directory path as argument (where .patch.md files live)
  - Find all .patch.md files in that directory
  - For each patch file: parse it, validate it (dry_run=True first),
    then apply it if validation passes
  - Print a clear per-file result: APPLIED / SKIPPED / FAILED + reason
  - On any failure: stop, print exactly what failed, do not continue
    to next patch silently
  - After all patches applied: print a summary (N applied, N skipped,
    N failed)
  - Do NOT delete the .patch.md files automatically — leave that to
    the operator

Requirements:
  - Uses search-replace-py (from search_replace import apply_diff,
    apply_edits, parse_edit_blocks, ApplyError, ParseError)
  - No external dependencies beyond search-replace-py
  - Handles both new-file creation and existing-file modification
  - Compatible with Python 3.10+
  - No more than 80 lines of code

---

## Q6 — Test run (end-to-end verification)
Provide a complete test procedure the operator can run in under
10 minutes to verify the full pipeline works before using it on
real files.

The test must:
  1. Create a dummy target file
  2. Create a valid .patch.md file that modifies it
  3. Run run_patches.py against it
  4. Verify the output matches expectation
  5. Create a second .patch.md with an intentionally bad SEARCH block
  6. Verify the script fails safely and reports the error clearly

Provide exact terminal commands for each step.
Include the expected output so the operator can confirm it matches.

---

## Q7 — Integration with the GPT → GitHub → local workflow
How should GPT (browser, GitHub connector) format the .patch.md files
it writes to the repo so that run_patches.py can consume them directly?

Provide:
  - The exact system prompt fragment or Project Instruction the operator
    should give GPT to ensure it always outputs valid patch files
  - A naming convention for .patch.md files (e.g. TASK-XX_filename.patch.md)
  - Where in the repo the patch files should live
    (e.g. /patches/ subfolder)
  - What GPT should write into the patch file beyond the SEARCH/REPLACE
    blocks (metadata, target path declaration, etc.)

---

## Q8 — Failure modes and recovery
What are the three most likely failure modes for this pipeline, and
what is the exact recovery procedure for each?

Format as:
  FAILURE: description
  CAUSE: why it happens
  DETECT: how the operator knows it happened
  RECOVER: exact steps to fix it

---

## Q9 — Keeping it simple (final check)
Review your answers above. Flag any step that:
  - Adds complexity without proportional reliability gain
  - Could be simplified without meaningful trade-off
  - Is only needed for edge cases the operator is unlikely to hit

For each flagged item, give a simpler alternative.
The goal is the most resilient, least complicated pipeline possible.