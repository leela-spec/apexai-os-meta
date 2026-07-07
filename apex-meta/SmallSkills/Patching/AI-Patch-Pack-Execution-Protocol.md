# AI Patch Pack Execution Protocol

## Purpose

This is the document that should guide future AI/Codex runs for patch packs.

The key lesson from the recent failures is:

```text
"Use the same process" only works when the patch pack is the same class of artifact.
```

The earlier smooth run worked because the patch pack was already Git-native and validated. Later runs failed because the patch packs looked similar to humans but were technically different: stale, not Git-generated, not blob-anchored, or not validated against the real local repository.

## What Actually Happened

### Smooth run

The smooth process worked because the patch pack had these properties:

```yaml
smooth_patch_pack:
  generated_from_live_repo_files: true
  one_patch_per_target_file: true
  git_generated_diffs: true
  diff_has_index_old_new_blob_lines: true
  git_apply_check_was_run_against_real_clone: true
  target_scope_was_verified: true
  semantic_marker_checks_existed: true
```

That means Codex could act as an executor:

```text
check -> apply -> validate -> commit
```

No judgment-heavy repair was needed.

### Later messy Apex KB v3 finalization run

That pack was stale relative to current `origin/main`.

The first failure was:

```yaml
failed_patch: 001-apex-kb-py-source-payload-manifest.patch
failed_target: apex-meta/scripts/apex_kb.py
reason: patch context no longer matched current main
```

Codex eventually made it pass, but only by doing a long live repair loop:

```yaml
what_went_wrong:
  repair_happened_during_final_apply_task: true
  multiple_stale_patches_found_one_after_another: true
  final_smoke_test_failed_once: true
  patch_001_needed_late_contract_fix: true
  process_duration_was_too_long: true
```

Final PASS did not mean the process was good. It meant the recovery succeeded.

### Apex loop-skill audit fixes pack

That pack was not equivalent to the smooth pack. Its own validation report said:

```yaml
patch_files_git_generated: false
git_apply_check_each_patch: not_run_against_full_clone
git_apply_check_cumulative: not_run_against_full_clone
old_blob_validation: not_applicable
ready_for_later_application: review_required
```

The first patch failed immediately:

```text
001-root-claude-skill-index.patch
error: patch failed: .claude/Claude.md:1
```

It also lacked Git-native headers:

```text
diff --git ...        missing
index <old>..<new>   missing
```

So it was a patch-shaped text artifact, not a fully Git-native patch pack.

## Why Same Instructions Failed

The operator instruction was similar, but the inputs were not.

This is the central distinction:

```text
Same execution instructions + different patch artifact class = different behavior.
```

An AI cannot make a stale or non-Git-generated patch pack behave like a validated Git-native patch pack by following the same apply commands. If the patch was created against an old file shape, or without real `git apply --check`, then the first real local apply may be the first time the patch is actually tested.

## Required Patch Pack Classification

Before applying any patch pack, classify it.

### Class A: Executor-Ready

Use the simple smooth process only if all are true:

```yaml
class_A_executor_ready:
  one_patch_per_target_file: true
  manifest_maps_patch_to_target: true
  patches_have_diff_git_headers: true
  patches_have_index_old_new_blob_lines: true
  old_blob_ids_match_current_local_targets: true
  git_apply_check_passes_against_current_local_clone: true
  semantic_or_smoke_checks_are_defined: true
```

Action:

```text
Run deterministic applier. Do not repair. Do not improvise.
```

### Class B: Repair-First

Use repair-first if any of these are true:

```yaml
class_B_repair_first:
  patch_context_stale: true
  git_apply_check_fails: true
  patch_has_manifest_but_no_blob_anchors: true
  validation_report_says_full_git_apply_not_run: true
  one_patch_per_target_file: true
```

Action:

```text
Do not apply final targets yet.
Repair patch artifacts first in a temporary branch/worktree.
Regenerate Git-native diffs.
Run git apply --check on the full repaired pack.
Run disposable apply validation and smoke checks.
Restore targets.
Only then do final apply/commit/push if requested.
```

### Class C: Reject / Regenerate

Stop if any are true:

```yaml
class_C_reject:
  no_patch_to_target_manifest: true
  patches_touch_multiple_unrelated_targets: true
  dirty_worktree_overlaps_patch_targets: true
  patch_intent_requires_design_choices: true
  smoke_contract_unknown: true
```

Action:

```text
Stop and request regeneration from current origin/main.
```

## Mandatory Execution Flow

### Step 1: Baseline

```bash
git checkout main
git pull --ff-only origin main
git rev-parse HEAD
git status --short
```

Unrelated dirty files are allowed only if they do not overlap patch targets.

### Step 2: Copy Patch Pack Into Repo

Copy downloaded artifacts into a repo-local patch directory, for example:

```text
apex-meta/patches/<patch-pack-name>/
```

### Step 3: Parse Manifest

The manifest must provide:

```yaml
patch_to_target_map: required
expected_changed_files: required
non_goals: required
required_markers_or_smoke_tests: strongly_required
```

### Step 4: Verify Patch Shape

For each patch:

```yaml
checks:
  touches_exactly_one_expected_target: required
  diff_git_header_present: required_for_class_A
  index_old_new_blob_present: required_for_class_A
  old_blob_matches_local_file: required_for_class_A
```

### Step 5: Run Git Check

```bash
for p in patches/*.patch; do
  git apply --check "$p"
done
```

If this fails, the pack is not executor-ready. Move to repair-first or reject.

### Step 6: Repair-First Flow For Class B

Do not apply partial patches.

For each failing patch:

```text
1. create temporary repair branch/worktree from current main
2. apply the intended change to the single target in the repair branch
3. generate a new patch with git diff -- <target>
4. restore target file
5. return to main
6. re-run git apply --check for the full pack
```

Do not do final target edits manually.

### Step 7: Disposable Validation Apply

Before final commit/push, validate in a disposable pass:

```text
apply all repaired patches
run compile/tests/smoke/marker checks
verify changed-file scope
restore targets to baseline
```

This prevents late failures like:

```text
patches apply, but smoke contract fails
```

### Step 8: Final Apply

Only after disposable validation passes:

```text
apply all patches with git apply
run validation again
stage only expected files and patch-pack artifacts
commit if requested
push if requested
```

## What The Next AI Should Read

For any future patch pack, the AI should read this file first:

```text
apex-meta/SmallSkills/Patching/AI-Patch-Pack-Execution-Protocol.md
```

Then read a pack-specific handoff if one exists, for example:

```text
apex-meta/SmallSkills/Patching/CODEX-Robust-ApexLoopSkillAuditFixes-Handoff.md
```

The earlier file is still useful as a success case:

```text
apex-meta/SmallSkills/Patching/BestPracticeGitPatchWorkflow.md
```

But it should not be used alone, because it describes Class A executor-ready packs. It does not adequately instruct the AI what to do with Class B stale or non-Git-generated packs.

## Short Rule

```text
First classify the patch pack.
Class A: execute.
Class B: repair patch artifacts first, validate in disposable apply, then execute.
Class C: stop and regenerate.
```

