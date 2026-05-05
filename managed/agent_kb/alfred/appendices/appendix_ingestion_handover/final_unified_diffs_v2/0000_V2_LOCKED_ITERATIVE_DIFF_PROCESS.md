# V2 Locked Iterative Diff Process

## Why this V2 exists

The prior `final_unified_diffs/` package is invalid as an executable patch package. It used manually written hunk headers such as bare `@@`, which Git cannot apply. `git apply --recount -C0` can repair hunk count/context problems, but it cannot repair structurally invalid unified diff syntax.

This V2 process supersedes the broken package without deleting it.

## V2 output locations

Corrected artifacts live under:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/
```

Template group files are created directly under:

```text
managed/agent_kb/alfred/templates/
```

## Hard target lock

Only these scaffold targets may be changed by V2 diffs:

```text
managed/agent_kb/alfred/ESSENCE.md
managed/agent_kb/alfred/BEST_PRACTICES.md
managed/agent_kb/alfred/MISTAKES.md
managed/agent_kb/alfred/TEMPLATES.md
managed/agent_kb/alfred/LEARNING_QUEUE.md
managed/agent_kb/alfred/SOURCE_MANIFEST.md
managed/agent_kb/alfred/COVERAGE_AUDIT.md
managed/agent_kb/alfred/README.md
```

Only these template group files may be created directly:

```text
managed/agent_kb/alfred/templates/routing_templates.md
managed/agent_kb/alfred/templates/daily_board_templates.md
managed/agent_kb/alfred/templates/project_packet_templates.md
managed/agent_kb/alfred/templates/trace_state_tracking_templates.md
managed/agent_kb/alfred/templates/pattern_learning_templates.md
```

No cleanup deletion happens in this V2 generation pass.

## Non-drift rules

Do not:

- rewrite whole scaffold files from memory
- create duplicate IDs
- preserve the broken V1 package as reusable patch authority
- add new Alfred doctrine beyond the validated plan intent
- harden detailed Leela / Rhythm / Sequencing mechanics into Alfred doctrine
- treat cleanup/proposal/control folders as permanent scaffold content
- add permanent README navigation to cleanup-bound folders
- reintroduce non-final metric fields or mappings

Use only:

- `EVD`
- `IMP`
- `RSK`
- scoped `URG` for process handovers, Daily Command Board routing, and time-sensitive handoff priority

Weekly Preview and Monthly Direction Map remain deferred / candidate-only.

## Required generation method for corrected unified diffs

A corrected V2 `.diff` file must be generated from an actual before/after file state, not hand-authored as a diff-looking text block.

Preferred local method in Codex:

```bash
git checkout -b alfred-final-diffs-v2
# edit exactly one target file
mkdir -p managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2
git diff -- managed/agent_kb/alfred/<TARGET>.md > managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/<NNNN_NAME>.diff
git apply --check managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/<NNNN_NAME>.diff
```

A valid V2 diff must contain real hunk headers like:

```diff
@@ -120,6 +120,14 @@
```

A V2 diff is invalid if it contains a bare hunk header:

```diff
@@
```

## Iterative generation order

Each iteration has the same loop:

1. Fetch/read the current target file.
2. Make only the locked intended change for that file.
3. Generate the diff using `git diff` or another real unified-diff generator.
4. Validate patch syntax with `git apply --check`.
5. Validate target lock.
6. Validate content-drift guardrails.
7. Record validation result before moving to the next file.

Order:

```text
0001_ESSENCE_FINAL.diff
0002_BEST_PRACTICES_FINAL.diff
0003_MISTAKES_FINAL.diff
TEMPLATE_GROUP_FILES_DIRECT_WRITE
0004_TEMPLATES_INDEX_FINAL.diff
0005_LEARNING_QUEUE_FINAL.diff
0006_SOURCE_MANIFEST_FINAL.diff
0007_COVERAGE_AUDIT_FINAL.diff
0008_README_FINAL.diff
0009_CLEANUP_EXECUTOR_NOTE.md
```

## Template-specific V2 decision

Template group files are created directly first. They are not generated as patch files.

After all group files exist and validate, generate `0004_TEMPLATES_INDEX_FINAL.diff` against `TEMPLATES.md` so the index can point to real existing files.

This avoids the V1 problem where an index diff pointed to grouped files that did not yet exist and partially rewrote old template sections unsafely.

## Per-iteration validation checklist

For every generated diff:

```bash
git apply --check <diff-file>
! grep -n '^@@$' <diff-file>
grep -n '^@@ -[0-9]' <diff-file>
```

Then check target lock:

```bash
git diff --name-only
```

Expected: only the active target file plus the newly created V2 diff artifact, or only the permitted template group file during direct template creation.

Content guardrails:

```bash
grep -Rni "value / urgency / leverage / fit\|old metric\|superseded metric\|mapping table" managed/agent_kb/alfred || true
grep -Rni "Weekly Preview\|Monthly Direction Map" managed/agent_kb/alfred/TEMPLATES.md managed/agent_kb/alfred/templates || true
grep -Rni "Weekly Preview\|Monthly Direction Map" managed/agent_kb/alfred/LEARNING_QUEUE.md || true
grep -Rni "cleanup_patch_proposals\|appendix_ingestion_handover" managed/agent_kb/alfred/README.md managed/agent_kb/alfred/SOURCE_MANIFEST.md managed/agent_kb/alfred/COVERAGE_AUDIT.md || true
```

Expected:

- Metric drift absent from scaffold doctrine.
- Weekly Preview and Monthly Direction Map absent from accepted template content.
- Weekly Preview and Monthly Direction Map present only as deferred/candidate items if present.
- Cleanup-bound folders not permanent README navigation or doctrine source.

## Validation record format

After each iteration, append a record under:

```text
managed/agent_kb/alfred/appendices/appendix_ingestion_handover/final_unified_diffs_v2/V2_VALIDATION_LOG.md
```

Template:

```md
## Iteration <N> — <target>

- Artifact: `<path>`
- Target: `<path>`
- Generation method: real diff from actual before/after | direct file creation
- Patch syntax check: pass | fail | not_applicable_direct_file
- Bare `@@` scan: pass | fail | not_applicable_direct_file
- Target lock: pass | fail
- Content drift scan: pass | fail
- Deferred item status: pass | fail | not_applicable
- Cleanup-bound reference status: pass | fail | not_applicable
- Result: accepted_for_next_iteration | blocked
- Notes:
```

## Failure handling

If any iteration fails validation, stop and do not generate the next artifact.

Do not use `--recount -C0` unless the diff has valid hunk headers and fails only because of hunk counts or context looseness.

If the diff has bare `@@`, `patch with only garbage`, or `corrupt patch`, regenerate the diff from actual file state. Do not patch around it.
