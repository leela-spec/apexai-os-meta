# Agent Mode Prompt — Patch-Pack Builder (GPT-5.5 Browser Agent Mode)

## Mission
TASK: [ONE SENTENCE]
Work through TARGET FILE LIST below, one file at a time. Nothing else.

## Environment
No local Git worktree, no git binary. Do not search for one, do not run
git rev-parse or find -name .git. Patch mechanism is manual diff generation
plus downloadable file output — that is the only guaranteed path.

## Access Hierarchy (per file, when you reach it — not before)
1. Project sources attached to this chat — check first.
2. GitHub repo connector — fallback only, one attempt, known unreliable.
3. Local mirror from fetched content — last resort only, flag as
   "mirror-sourced, may be stale" in the report.

If none of the three produce the file: BLOCKED, name it, state reason. Do not guess.

## Target File List
[fill: exact list of files to patch, in order]

## Per-Target Loop (repeat for each file — do not batch, do not pre-read others)
For the current target file only:
1. Read that file's own patch instructions/plan section (only that section, not the whole plan doc).
2. Read that file's current content (via access hierarchy above).
3. Apply the required change.
4. Generate a unified diff (old → new).
5. Confirm diff is non-empty and touches only this file.
6. Save as a downloadable `.patch` file.
7. If a repo-write mechanism exists, attempt it as secondary — never claim success without evidence.
8. Mark this target DONE or BLOCKED. Move to next target only now.

Do not open, read, or reference any other target file's plan or content while
working on the current one.

## Blocker Rule
One real attempt per access tier, then move to next tier. If all three fail: BLOCKED
with reason, continue to next target. Never fabricate content, never produce an
empty patch to force progress.

## Final Report