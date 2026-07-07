# Failure Report: Apex Loop Skill Audit Fixes Patch Pack

Date: 2026-07-07

## Summary

The patch pack at:

```text
C:\Users\gehm7\Downloads\apex-loop-skill-audit-fixes-patch-pack\patches\apex-loop-skill-audit-fixes
```

does not behave like the earlier smooth patch pack documented in this folder. The earlier successful process depended on Git-generated, blob-anchored patch files that had been verified with `git apply --check` against a real local clone. This patch pack was generated from connector-read file excerpts, not from a local Git worktree, and its own validation report says full `git apply --check` was not run.

This report also corrects an earlier incomplete diagnosis: the Apex KB v3 finalization run that eventually passed was not actually a smooth repeatable process. It took about 16 minutes because Codex performed iterative patch repair during execution, hit multiple stale patches, hit a smoke-test contract mismatch after applying the repaired pack, then restored targets and corrected patch `001` before retrying. That was a recovery, not evidence that the process was healthy.

## What Failed

Running a direct Git check against the current local clone fails immediately:

```text
CHECK .../001-root-claude-skill-index.patch
error: patch failed: .claude/Claude.md:1
error: .claude/Claude.md: patch does not apply
```

The first patch starts with:

```diff
--- a/.claude/Claude.md
+++ b/.claude/Claude.md
@@ -1,28 +1,28 @@
```

but the edited `FlowRecap`, `StatusMerge`, `RawFlowDumpNormalize`, and `ModelUsageLog` block is not at line 1 in the current local file. The patch also has no `diff --git` line and no `index <old>..<new>` blob line, so Git cannot verify that the patch was generated from the exact live file blob.

## Prior Run Process Failure

The prior Apex KB v3 finalization run had two distinct failures:

```yaml
prior_run_failures:
  initial_apply:
    failed_step: git_apply_check
    failed_patch: apex-meta/patches/apex-kb-v3-finalization/patches/001-apex-kb-py-source-payload-manifest.patch
    failed_target: apex-meta/scripts/apex_kb.py
    reason: stale patch context after origin/main advanced
  repair_execution:
    duration: about_16_minutes_53_seconds
    repair_style: iterative_ad_hoc_patch_rebase
    stale_patches_found: multiple
    smoke_failure_after_apply: true
    smoke_failure_reason: generated manifest did not contain required "source_payload_manifest" term
    final_pass_required: restore_targets_then_modify_repaired_patch_001_and_retry
```

The final commit passed validation, but the path there was too manual and too long. The correct lesson is not "this process worked." The correct lesson is:

```text
If the first git apply --check fails, do not improvise patch repair in the main execution path.
Stop and run a dedicated patch-pack repair workflow that:
1. repairs all stale patches as patch artifacts first,
2. proves all repaired patches apply,
3. runs smoke validation in a disposable apply pass,
4. only then performs final apply/commit/push.
```

## Why The Same Instructions Did Not Produce The Same Result

The operator instructions were similar, but the artifact quality was not.

The successful folder describes this required pattern:

```yaml
git_generated_unified_diffs: true
old_blob_anchoring: true
git_apply_check_against_real_clone: true
one_patch_per_target_file: true
```

This patch pack reports:

```yaml
patch_files_git_generated: false
git_apply_check_each_patch: not_run_against_full_clone
git_apply_check_cumulative: not_run_against_full_clone
old_blob_validation: not_applicable
ready_for_later_application: review_required
```

So the failure was not caused by a different operator intent. It was caused by a different patch-generation process. A synthetic patch dry-run is not equivalent to Git applying a patch in the real repository.

There was also an execution problem: Codex treated a stale patch pack as something to repair live under deadline pressure. That created a long chain of local scripts and one-off repair decisions. Even though the final result passed, it violated the spirit of the "smooth process" folder, where the whole point was to make fallback unnecessary by generating validated Git-native patches before handoff.

## Additional Local Risk

The local worktree is also dirty with unrelated deleted files under:

```text
apex-meta/kb/apex-kb-skill-test/
apex-meta/kb/apex-plan-sync-session-workflow/
scripts/Patch/
```

Those deletions do not overlap this patch pack's targets, but a robust applier must explicitly allow unrelated dirt while blocking dirty overlap with patch targets.

## Required Fix For The Next Run

Do not run plain `git apply` directly on this downloaded patch pack.

Do not run a long manual rebase loop directly inside the final apply task either.

Use a repair-first workflow:

1. Copy the downloaded patch pack into a repo-local patch artifact folder.
2. Parse `000-patch-manifest.md` for the patch-to-target map.
3. Check that no dirty file overlaps a patch target.
4. Try `git apply --check`.
5. If it fails, create a temporary repair branch from current `origin/main`.
6. Apply each stale patch to its single target with deterministic hunk matching.
7. Regenerate each repaired patch with `git diff -- <target> > <patch>`.
8. Restore target files and return to `main`.
9. Re-run `git apply --check` for the full repaired pack.
10. Run a disposable apply validation and all smoke/marker checks.
11. Restore targets to baseline.
12. Only then apply the repaired Git-native patches for the final state.

Use:

```text
apex-meta/SmallSkills/Patching/CODEX-Robust-ApexLoopSkillAuditFixes-Handoff.md
apex-meta/SmallSkills/Patching/apply_apex_loop_skill_audit_fixes_robust.py
```

for the next run.

## Updated Rule

For future patch packs, Codex should classify the pack before applying it:

```yaml
pack_classification:
  class_A_smooth:
    requirements:
      - git_generated_diffs
      - index_old_new_blob_lines_present
      - full_git_apply_check_passed_against_real_clone
      - target_scope_manifest_present
    action: run deterministic applier

  class_B_repairable:
    requirements:
      - one_patch_per_target
      - target_manifest_present
      - no_dirty_target_overlap
    action: repair patch artifacts first, then run deterministic applier

  class_C_reject:
    examples:
      - multi_target_ambiguous_patch
      - no_target_manifest
      - patch_targets_overlap_dirty_files
      - smoke_contract_unknown
    action: stop and request regeneration from current origin/main
```

The Apex loop-skill audit fixes pack is Class B at best. It must be repaired before application.
