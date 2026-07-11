# CODEX_APPLY_PLAN_HYGIENE_CLEAN_PATCHSET

## Purpose

This is the zero-freedom Codex execution plan for applying the approved Special Ops Hygiene Clean KB patchset.

Codex must apply only the seven already-manufactured unified-diff artifacts in this appendix folder.

Codex must not generate, improve, reinterpret, rewrite, normalize, repair, or broaden content.

## Source basis

This plan follows the repo's deterministic Codex execution doctrine:

- Codex is an executor, not a content author.
- Exact unified diffs are the change artifact.
- `git apply --check` is mandatory before `git apply`.
- All checks must pass before apply, commit, or push.
- If any check fails, Codex stops and reports instead of hand-editing.
- Changed paths must exactly match the approved changed-file set.

## Repo lock

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
artifact_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/
operation_class: PATCH_PATHS
branch_creation_required: false
branch_creation_forbidden: true
codex_may_generate_content: false
codex_may_repair_failed_diff: false
codex_may_create_extra_files: false
codex_may_modify_config: false
codex_may_touch_source_or_staging: false
```

## Approved patch artifacts

Apply these exact artifacts, in this order:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_002_ESSENCE.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_003_BEST_PRACTICES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_004_TEMPLATES.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_005_LEARNING_QUEUE.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_007_APP_KB_SOURCE_MANIFEST.diff
```

## Approved changed-file set

After applying the seven patches, `git diff --name-only` must equal exactly:

```text
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
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
any sibling folder under OpenClaw/07_finalopenclawsystem/managed/agent_kb/ other than special_ops__hygiene_clean/
```

## Codex execution prompt

Copy this whole section into Codex.

````md
# CODEX EXECUTION PROMPT - SPECIAL OPS HYGIENE CLEAN KB PATCHSET

## Role

You are Codex operating on a real local checkout of `leela-spec/MasterOfArts`.

You are a deterministic patch executor and verifier only.

You are not a content author.
You are not a reviewer.
You are not an improver.
You are not allowed to generate missing content.

## Non-negotiable constraint

Apply only the exact seven unified-diff artifacts already present in the repo under:

`OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/`

Do not invent, improve, rewrite, reformat, normalize, repair, or broaden content.

If any diff fails `git apply --check`, STOP and report. Do not hand-edit.

If any target file has drifted, STOP and report. Do not adapt the patch.

If any validation command fails, STOP and report. Do not continue.

## Repo lock

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
branch_creation_required: false
branch_creation_forbidden: true
operation_class: PATCH_PATHS
codex_may_generate_content: false
codex_may_repair_failed_diff: false
codex_may_create_extra_files: false
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
PATCH_DIR="OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices"
PATCHES=(
  "$PATCH_DIR/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff"
  "$PATCH_DIR/PATCH_002_ESSENCE.diff"
  "$PATCH_DIR/PATCH_003_BEST_PRACTICES.diff"
  "$PATCH_DIR/PATCH_004_TEMPLATES.diff"
  "$PATCH_DIR/PATCH_005_LEARNING_QUEUE.diff"
  "$PATCH_DIR/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff"
  "$PATCH_DIR/PATCH_007_APP_KB_SOURCE_MANIFEST.diff"
)
```

## Copy patch artifacts to temp

Run:

```bash
mkdir -p /tmp/openclaw_hygiene_patches
cp "$PATCH_DIR/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff" /tmp/openclaw_hygiene_patches/001_app_kb_qa_and_next_research_plan.diff
cp "$PATCH_DIR/PATCH_002_ESSENCE.diff" /tmp/openclaw_hygiene_patches/002_essence.diff
cp "$PATCH_DIR/PATCH_003_BEST_PRACTICES.diff" /tmp/openclaw_hygiene_patches/003_best_practices.diff
cp "$PATCH_DIR/PATCH_004_TEMPLATES.diff" /tmp/openclaw_hygiene_patches/004_templates.diff
cp "$PATCH_DIR/PATCH_005_LEARNING_QUEUE.diff" /tmp/openclaw_hygiene_patches/005_learning_queue.diff
cp "$PATCH_DIR/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff" /tmp/openclaw_hygiene_patches/006_app_kb_candidate_ledger.diff
cp "$PATCH_DIR/PATCH_007_APP_KB_SOURCE_MANIFEST.diff" /tmp/openclaw_hygiene_patches/007_app_kb_source_manifest.diff
```

Do not edit these files after copying them.

## Structural patch validation before apply

Run:

```bash
for f in /tmp/openclaw_hygiene_patches/*.diff; do
  echo "CHECKING $f"
  test "$(grep -c '^diff --git ' "$f")" = "1" || { echo "bad diff header count: $f"; exit 1; }
  grep -q '^diff --git a/OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/' "$f" || { echo "target outside Hygiene Clean KB: $f"; exit 1; }
  ! grep -E '^diff --git a/(OpenClaw/07_finalopenclawsystem/managed/config/|OpenClaw/04_final-system-setup/|OpenClaw/02_research-kb/|agent_kb_source_indexes/|AllAIBestPractice/|Apex|apexai-os-meta)' "$f" || { echo "forbidden path in patch: $f"; exit 1; }
done
```

## Apply check: all patches before any apply

Run every check before applying anything:

```bash
git apply --check /tmp/openclaw_hygiene_patches/001_app_kb_qa_and_next_research_plan.diff
git apply --check /tmp/openclaw_hygiene_patches/002_essence.diff
git apply --check /tmp/openclaw_hygiene_patches/003_best_practices.diff
git apply --check /tmp/openclaw_hygiene_patches/004_templates.diff
git apply --check /tmp/openclaw_hygiene_patches/005_learning_queue.diff
git apply --check /tmp/openclaw_hygiene_patches/006_app_kb_candidate_ledger.diff
git apply --check /tmp/openclaw_hygiene_patches/007_app_kb_source_manifest.diff
```

If any `git apply --check` fails, STOP. Report:

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

## Apply patches only after all checks pass

Run:

```bash
git apply /tmp/openclaw_hygiene_patches/001_app_kb_qa_and_next_research_plan.diff
git apply /tmp/openclaw_hygiene_patches/002_essence.diff
git apply /tmp/openclaw_hygiene_patches/003_best_practices.diff
git apply /tmp/openclaw_hygiene_patches/004_templates.diff
git apply /tmp/openclaw_hygiene_patches/005_learning_queue.diff
git apply /tmp/openclaw_hygiene_patches/006_app_kb_candidate_ledger.diff
git apply /tmp/openclaw_hygiene_patches/007_app_kb_source_manifest.diff
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
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
```

If it differs, STOP and report. Do not commit.

## Forbidden-path validation

Run:

```bash
git diff --name-only | grep -E '^(OpenClaw/07_finalopenclawsystem/managed/config/|OpenClaw/04_final-system-setup/|OpenClaw/02_research-kb/|agent_kb_source_indexes/|AllAIBestPractice/|Apex|apexai-os-meta)' && { echo "forbidden path changed"; exit 1; } || true

git diff --name-only | grep -E '^OpenClaw/07_finalopenclawsystem/managed/agent_kb/' | grep -v '^OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/' && { echo "sibling agent KB changed"; exit 1; } || true
```

## Readback validation

Run:

```bash
grep -q 'APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md
grep -q '## Status vocabulary' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md
grep -q 'BP-HC-008' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md
grep -q '## Template chooser' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md
grep -q '## Realization trace boundary' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md
grep -q '## Realization trace fields' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md
grep -q '## Source Notes register' OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_SOURCE_MANIFEST.md
```

If any readback check fails, STOP and report. Do not commit.

## Commit and push only after all checks pass

Run:

```bash
git add \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/ESSENCE.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/BEST_PRACTICES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/TEMPLATES.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/LEARNING_QUEUE.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_CANDIDATE_LEDGER.md \
  OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/APPENDIX_KB_SOURCE_MANIFEST.md

git commit -m "Apply Hygiene Clean KB scaffold patchset"
git push origin main
```

Do not add the patch artifact files. They should already be present on `main` and unchanged.

## Final report schema

Report exactly this schema:

```yaml
repo: leela-spec/MasterOfArts
branch: main
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
patch_artifacts_used:
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_002_ESSENCE.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_003_BEST_PRACTICES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_004_TEMPLATES.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_005_LEARNING_QUEUE.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff
  - OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/appendices/PATCH_007_APP_KB_SOURCE_MANIFEST.diff
git_apply_check_passed: true | false
git_apply_passed: true | false
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
I approve this Special Ops Hygiene Clean KB patchset for Codex execution. Codex is authorized to apply only the seven exact unified diff artifacts listed in CODEX_APPLY_PLAN_HYGIENE_CLEAN_PATCHSET.md, using git apply --check first for every diff. Codex may not generate content, repair failed diffs, widen scope, modify config, touch source/staging folders, create a branch, or touch any sibling agent KB folder. If any check fails, Codex must stop and report instead of hand-editing.
```

## Planning proof

```yaml
codex_apply_plan_created: true
patchset_validation_report_exists: true
expected_patch_artifacts: 7
expected_changed_files: 7
codex_generation_allowed: false
codex_hand_edit_allowed: false
branch_creation_forbidden: true
target_branch: main
status: ready_for_operator_codex_execution
```
