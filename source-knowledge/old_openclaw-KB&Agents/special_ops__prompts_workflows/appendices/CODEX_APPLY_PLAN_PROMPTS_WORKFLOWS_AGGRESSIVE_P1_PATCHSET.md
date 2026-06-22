# CODEX_APPLY_PLAN_PROMPTS_WORKFLOWS_AGGRESSIVE_P1_PATCHSET

## Purpose

This is the zero-freedom Codex execution plan for applying the approved Special Ops Prompts Workflows aggressive P1 patchset.

Codex must apply only the six already-manufactured unified-diff artifacts in this appendix folder.

Codex must not generate, improve, reinterpret, rewrite, normalize, repair, or broaden content.

## Source basis

This plan follows the repo's deterministic Codex execution doctrine, with one explicit operator-approved workaround for this patchset:

- Codex is an executor, not a content author.
- Exact unified diffs are the change artifact.
- These patch artifacts are known to be potentially malformed for strict `git apply --check` because hunk metadata may not be pristine.
- For this patchset only, Codex must use the operator-approved `--recount -C0` workaround rather than stopping on strict patch metadata failure.
- The applied result must still validate by changed-file allowlist, forbidden-path check, readback checks, and `git diff --check`.
- The patch artifacts must not be treated as pristine reusable patches after this workaround path is used.
- If `git apply --check --recount -C0` or `git apply --recount -C0` fails, Codex stops and reports instead of hand-editing.
- Changed paths must exactly match the approved changed-file set.

## Repo lock

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
artifact_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/
operation_class: PATCH_PATHS
branch_creation_required: false
branch_creation_forbidden: true
codex_may_generate_content: false
codex_may_repair_failed_diff: false
codex_may_create_extra_files: false
codex_may_modify_config: false
codex_may_touch_source_or_staging: false
patch_metadata_pristine: false
operator_approved_apply_workaround: git_apply_recount_C0
```

## Approved patch artifacts

Apply these exact artifacts, in this order:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_001_APP_KB_EXAMPLES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_002_APP_KB_SOURCE_NOTES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_003_TEMPLATES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_004_MISTAKES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_005_BEST_PRACTICES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_006_ESSENCE.diff
```

## Approved changed-file set

After applying the six patches, `git diff --name-only` must equal exactly:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXAMPLES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_NOTES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
```

No other path may be modified.

## Forbidden paths

Codex must stop if any pending or applied diff touches:

```text
OpenClaw/07_finalopenclawsystem/managed/config/
OpenClaw/04_final-system-setup/
OpenClaw/02_research-kb/
agent_kb_source_indexes/
AllAIBestPractice/
Apex
apexai-os-meta
any sibling folder under OpenClaw/07_finalopenclawsystem/managed/agent_kb/ other than special_ops__prompts_workflows/
```

## Codex execution prompt

Copy this whole section into Codex.

````md
# CODEX EXECUTION PROMPT - SPECIAL OPS PROMPTS WORKFLOWS AGGRESSIVE P1 PATCHSET

## Role

You are Codex operating on a real local checkout of `leela-spec/MasterOfArts`.

You are a deterministic patch executor and verifier only.

You are not a content author.
You are not a reviewer.
You are not an improver.
You are not allowed to generate missing content.

## Non-negotiable constraint

Apply only the exact six unified-diff artifacts already present in the repo under:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/`

Do not invent, improve, rewrite, reformat, normalize, repair, or broaden content.

Known condition for this patchset: the patch artifact metadata may be malformed for strict `git apply --check`. This has operator approval for the `--recount -C0` workaround.

Use `git apply --check --recount -C0` as the apply-check gate and `git apply --recount -C0` as the apply command. Do not use strict `git apply --check` as the stop gate for this patchset.

If any `git apply --check --recount -C0` or `git apply --recount -C0` command fails, STOP and report. Do not hand-edit.

If any target file has drifted enough that `--recount -C0` cannot apply, STOP and report. Do not adapt the patch.

If any validation command fails after apply, STOP and report. Do not continue.

The applied result may be trusted only after validation passes. The patch artifacts themselves must be reported as non-pristine reusable patches.

## Repo lock

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
artifact_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/
branch_creation_required: false
branch_creation_forbidden: true
operation_class: PATCH_PATHS
codex_may_generate_content: false
codex_may_repair_failed_diff: false
codex_may_create_extra_files: false
codex_may_modify_config: false
codex_may_touch_source_or_staging: false
patch_metadata_pristine: false
operator_approved_apply_workaround: git_apply_recount_C0
```

## Required preflight

Run:

```bash
git status --short
git branch --show-current
git log --oneline -5
git fetch origin
git switch main
git pull --ff-only origin main
git status --short
```

Stop if:

- branch is not `main`
- tracked files are dirty before applying patches
- `git pull --ff-only` fails
- repo is not `leela-spec/MasterOfArts`

Untracked files may be reported, but must not be deleted or modified unless they are part of this exact plan. They are not part of this plan.

## Patch artifact list

Use exactly these source artifacts:

```bash
PATCH_DIR="OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices"
PATCHES=(
  "$PATCH_DIR/PATCH_001_APP_KB_EXAMPLES.diff"
  "$PATCH_DIR/PATCH_002_APP_KB_SOURCE_NOTES.diff"
  "$PATCH_DIR/PATCH_003_TEMPLATES.diff"
  "$PATCH_DIR/PATCH_004_MISTAKES.diff"
  "$PATCH_DIR/PATCH_005_BEST_PRACTICES.diff"
  "$PATCH_DIR/PATCH_006_ESSENCE.diff"
)
```

## Copy patch artifacts to temp

Run:

```bash
mkdir -p /tmp/openclaw_prompts_workflows_patches
cp "$PATCH_DIR/PATCH_001_APP_KB_EXAMPLES.diff" /tmp/openclaw_prompts_workflows_patches/001_app_kb_examples.diff
cp "$PATCH_DIR/PATCH_002_APP_KB_SOURCE_NOTES.diff" /tmp/openclaw_prompts_workflows_patches/002_app_kb_source_notes.diff
cp "$PATCH_DIR/PATCH_003_TEMPLATES.diff" /tmp/openclaw_prompts_workflows_patches/003_templates.diff
cp "$PATCH_DIR/PATCH_004_MISTAKES.diff" /tmp/openclaw_prompts_workflows_patches/004_mistakes.diff
cp "$PATCH_DIR/PATCH_005_BEST_PRACTICES.diff" /tmp/openclaw_prompts_workflows_patches/005_best_practices.diff
cp "$PATCH_DIR/PATCH_006_ESSENCE.diff" /tmp/openclaw_prompts_workflows_patches/006_essence.diff
```

Do not edit these files after copying them.

## Structural patch validation before apply

Run:

```bash
for f in /tmp/openclaw_prompts_workflows_patches/*.diff; do
  echo "CHECKING $f"
  test "$(grep -c '^diff --git ' "$f")" = "1" || { echo "bad diff header count: $f"; exit 1; }
  grep -q '^diff --git a/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/' "$f" || { echo "target outside Prompts Workflows KB: $f"; exit 1; }
  ! grep -E '^diff --git a/(OpenClaw/07_finalopenclawsystem/managed/config/|OpenClaw/04_final-system-setup/|OpenClaw/02_research-kb/|agent_kb_source_indexes/|AllAIBestPractice/|Apex|apexai-os-meta)' "$f" || { echo "forbidden path in patch: $f"; exit 1; }
done
```

## Operator-approved malformed-patch workaround

This patchset is expected to require the workaround below because the patch artifacts may have malformed hunk metadata. Do not run strict `git apply --check` as the decision gate.

The artifact itself is not pristine. The validation target is the applied result.

## Apply check: use recount workaround before any apply

Run every recount check before applying anything:

```bash
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/001_app_kb_examples.diff
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/002_app_kb_source_notes.diff
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/003_templates.diff
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/004_mistakes.diff
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/005_best_practices.diff
git apply --check --recount -C0 /tmp/openclaw_prompts_workflows_patches/006_essence.diff
```

If any recount check fails, STOP. Report:

```yaml
status: stopped
failed_patch:
failure_output:
likely_cause:
current_branch:
tracked_dirty_state:
recommended_next_action: regenerate that one diff against current main
```

Do not hand-edit.
Do not use `--reject`.
Do not use `--3way`.
Do not manually merge.

## Apply patches only after all recount checks pass

Run:

```bash
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/001_app_kb_examples.diff
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/002_app_kb_source_notes.diff
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/003_templates.diff
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/004_mistakes.diff
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/005_best_practices.diff
git apply --recount -C0 /tmp/openclaw_prompts_workflows_patches/006_essence.diff
```

Do not make any other edits.

## Required validation after apply

Run:

```bash
git diff --check
git status --short
git diff --name-only
```

The output of `git diff --name-only` must equal exactly:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXAMPLES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_NOTES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
```

If it differs, STOP and report. Do not commit.

## Forbidden-path validation

Run:

```bash
git diff --name-only | grep -E '^(OpenClaw/07_finalopenclawsystem/managed/config/|OpenClaw/04_final-system-setup/|OpenClaw/02_research-kb/|agent_kb_source_indexes/|AllAIBestPractice/|Apex|apexai-os-meta)' && { echo "forbidden path changed"; exit 1; } || true

git diff --name-only | grep -E '^OpenClaw/07_finalopenclawsystem/managed/agent_kb/' | grep -v '^OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/' && { echo "sibling agent KB changed"; exit 1; } || true
```

## Readback validation

Run:

```bash
grep -q 'APPENDIX_KB_EXAMPLES' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXAMPLES.md
grep -q 'APPENDIX_KB_SOURCE_NOTES' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_NOTES.md
grep -q 'PW-TPL-006' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
grep -q 'PW-TPL-007' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md
grep -q 'PW-MK-007' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
grep -q 'PW-MK-008' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md
grep -q 'PW-BP-007' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
grep -q 'PW-BP-008' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md
grep -q 'Examples are regression tests' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md
```

If any readback check fails, STOP and report. Do not commit.

## Commit and push only after all checks pass

Run:

```bash
git add \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_EXAMPLES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/APPENDIX_KB_SOURCE_NOTES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/TEMPLATES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/MISTAKES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/BEST_PRACTICES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/ESSENCE.md

git commit -m "Apply Prompts Workflows aggressive P1 patchset"
git push origin main
```

Do not add the patch artifact files. They should already be present on `main` and unchanged.

## Final report schema

Report exactly this schema:

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/
patch_artifacts_used:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_001_APP_KB_EXAMPLES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_002_APP_KB_SOURCE_NOTES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_003_TEMPLATES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_004_MISTAKES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_005_BEST_PRACTICES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/appendices/PATCH_006_ESSENCE.diff
strict_git_apply_check_used: false
operator_approved_apply_workaround: git_apply_recount_C0
patch_metadata_pristine: false
git_apply_check_recount_C0_passed: true | false
git_apply_recount_C0_passed: true | false
git_diff_check_passed: true | false
changed_file_set_actual: []
changed_file_set_matches_expected: true | false
forbidden_paths_changed: []
readback_verified: true | false
commit_created: true | false
commit_sha:
pushed_to_origin_main: true | false
status: applied_and_pushed | stopped
```
````

## Operator approval note

Use this exact approval text when handing this plan to Codex:

```text
I approve this Special Ops Prompts Workflows aggressive P1 patchset for Codex execution. Codex is authorized to apply only the six exact unified diff artifacts listed in CODEX_APPLY_PLAN_PROMPTS_WORKFLOWS_AGGRESSIVE_P1_PATCHSET.md. The patch artifacts are known to be potentially malformed for strict git apply --check because hunk metadata may not be pristine, so Codex must use the operator-approved git apply --check --recount -C0 and git apply --recount -C0 path directly for this patchset. Codex may not generate content, repair failed diffs, widen scope, modify config, touch source/staging folders, create a branch, use --reject, use --3way, or touch any sibling agent KB folder. If recount validation or post-apply validation fails, Codex must stop and report instead of hand-editing. The applied result must validate, but the patch artifacts themselves must not be treated as pristine reusable patches.
```

## Planning proof

```yaml
codex_apply_plan_created: true
expected_patch_artifacts: 6
expected_changed_files: 6
codex_generation_allowed: false
codex_hand_edit_allowed: false
branch_creation_forbidden: true
target_branch: main
strict_git_apply_check_used: false
operator_approved_apply_workaround: git_apply_recount_C0
patch_metadata_pristine: false
status: ready_for_operator_codex_execution
```
