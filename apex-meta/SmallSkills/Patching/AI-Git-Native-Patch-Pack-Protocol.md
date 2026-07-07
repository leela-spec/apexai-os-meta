# AI Git-Native Patch Pack Protocol

## Read This First

This is the authoritative protocol for future AI/Codex patch-pack work.

The reliable pattern is not "make something that looks like a patch."

The reliable pattern is:

```text
Use Git itself to create, verify, repair, apply, and validate patch packs.
```

If an AI cannot use a real local Git clone for patch creation and validation, it must not claim the patch pack is ready.

## The Smooth Success Pattern

The smooth run worked because the patch pack was created like this:

```text
1. Start from the exact current repo state.
2. Edit real target files in a local Git worktree.
3. Generate patches with `git diff`.
4. Revert target files after generating each patch.
5. Validate each patch with `git apply --check`.
6. Validate the full patch sequence in a disposable apply pass.
7. Verify changed-file scope and semantic markers.
8. Hand Codex a Git-native patch pack that already works.
```

That made Codex an executor, not a patch author or emergency repair agent.

## The Failure Pattern

The later messy runs failed because they copied the appearance of the smooth process without preserving the operational core.

Bad patch packs had one or more of these traits:

```yaml
failure_patterns:
  patch_created_from_memory_or_connector_excerpt: true
  patch_files_git_generated: false
  diff_git_headers_missing: true
  index_old_new_blob_lines_missing: true
  git_apply_check_not_run_against_real_clone: true
  synthetic_dry_run_claimed_as_validation: true
  patch_context_stale_against_current_main: true
  smoke_test_contract_not_validated_before_handoff: true
```

These artifacts may look like patches, but they are not reliable patch packs.

## Non-Negotiable Rule

```text
Patch packs must be created and validated with real Git operations against exact baseline file contents.
```

The Git workspace can be:

```yaml
valid_git_workspaces:
  local_user_clone:
    example: C:\GitDev\apexai-os-meta
    best_for: final apply, commit, push

  remote_agent_scratch_repo:
    example: ChatGPT Agent Mode sandbox
    requirements:
      - fetch exact live target file contents
      - preserve exact repo-relative paths
      - initialize a temporary Git repository
      - commit the baseline files
      - edit files in that Git repository
      - generate patches with git diff
      - validate patches with git apply --check in that scratch repository
      - record live blob hashes or baseline hashes
    best_for: creating downloadable patch packs when direct push is unavailable
```

Do not use copied snippets, memory, connector excerpts alone, or synthetic patch simulation as the final source of truth.

Those can help plan the change, but they cannot certify a patch pack.

## Environment Gate

Before doing anything else, identify what kind of AI environment is running.

```yaml
environment_gate:
  local_codex_with_user_repo:
    has_real_filesystem_path_to_user_repo: true
    can_run_git: true
    can_read_and_write_repo_files: true
    allowed_work:
      - create_patch_pack
      - validate_patch_pack
      - repair_patch_pack
      - apply_commit_push

  remote_agent_with_scratch_git:
    has_user_repo_path: false
    can_run_git_in_sandbox: true
    can_fetch_exact_live_files: true
    can_create_temp_git_repo: true
    allowed_work:
      - create_patch_pack
      - validate_patch_pack_in_scratch_repo
      - export_patch_pack_archive
    forbidden_claims:
      - "applied to user's local clone"
      - "pushed to origin/main"

  plain_remote_chat_or_connector_only:
    has_user_repo_path: false
    can_run_git_in_sandbox: false
    allowed_work:
      - explain_process
      - draft_operator_handoff
      - inspect_provided_text
    forbidden_claims:
      - "patch pack is ready"
      - "git apply check passed"
      - "old blobs match local repo"
      - "safe to apply"
```

If the AI is not running inside the local clone, it must stop before patch creation or validation and say:

```text
I cannot certify this patch pack unless I can either:
1. run in the real local clone, or
2. create a scratch Git repository from exact live target files and validate there.
```

This is not optional. The smooth process can be reproduced by remote Agent Mode, but not by a plain chat that only sees pasted text or connector excerpts.

## Roles

There are two different AI jobs. Do not mix them up.

```yaml
roles:
  patch_creator:
    job: create a Git-native patch pack
    required_environment:
      - local_codex_with_user_repo
      - remote_agent_with_scratch_git
    must_use:
      - real Git workspace
      - exact baseline file contents
      - git diff
      - git apply --check
      - disposable apply validation

  patch_executor:
    job: apply an already validated patch pack
    required_environment: local_codex_with_user_repo
    must_use:
      - git apply --check
      - git apply
      - scope checks
      - semantic/smoke checks
```

If the patch executor discovers the pack was not properly created, the executor must stop or switch to an explicit repair workflow. It must not pretend the pack is executor-ready.

## What The Working Process Actually Was

The working process was not merely a natural-language prompt. It also was not necessarily your physical local clone.

The successful ChatGPT Agent Mode run appears to have worked because it had an execution sandbox and used exact live files plus Git-style validation to produce a patch archive.

It had these concrete ingredients:

```yaml
working_process:
  git_workspace_available: true
  exact_live_target_files_available: true
  actual_patch_files_available: true
  patch_to_target_map_checked: true
  old_blob_or_live_file_match_checked: true
  deterministic_script_created_or_used: true
  script_attempt_order:
    - git_apply_check_and_apply
    - git_apply_whitespace_tolerant_modes
    - git_apply_3way_when_blob_data_available
    - deterministic_python_hunk_fallback
  scope_checks_after_apply: true
  marker_checks_after_apply: true
  commit_push_only_after_validation: true
```

The working process cannot be reproduced by asking a non-local AI to "do the same thing" unless that AI can actually run Git in a sandbox and build patches from exact live file contents.

## Common Reproduction Failure

This is the most common failed reproduction pattern:

```yaml
failed_reproduction:
  user_intent: "do it the same way"
  ai_environment: plain_remote_chat_or_connector_only
  ai_action: writes_more_instructions
  missing_step: no_local_git_validation
  result: not_the_same_process
```

Correct response:

```text
Do not create another theoretical handoff as if validation happened.
Either run in local Codex, or use Agent Mode to create a scratch Git repo from exact live files and validate there.
```

## Required Patch Pack Creation Process

Use this process when creating a patch pack.

### 1. Prepare A Clean Patch Worktree

```bash
git checkout main
git pull --ff-only origin main
BASE_SHA="$(git rev-parse HEAD)"
git status --short
```

If the worktree is dirty, create a separate worktree or clone for patch creation:

```bash
git worktree add ../apexai-os-meta-patchbuild "$BASE_SHA"
cd ../apexai-os-meta-patchbuild
```

Do not create patches from a dirty main worktree unless every dirty file is unrelated and explicitly accounted for.

### 2. Define The Patch Manifest First

Create a manifest with:

```yaml
patch_manifest:
  repo: leela-spec/apexai-os-meta
  base_branch: main
  base_sha: "<git rev-parse HEAD>"
  purpose: "<short purpose>"
  non_goals:
    - "<what this must not do>"
  patch_to_target_map:
    "001-example.patch": "path/to/target.md"
  expected_changed_files:
    - "path/to/target.md"
  required_markers:
    - "<string that must exist after apply>"
  forbidden_markers:
    - "<string that must not exist after apply>"
```

One patch should normally touch one target file.

### 3. Edit One Target File At A Time

For each target:

```bash
# edit one target file
git diff --check
git diff --no-ext-diff -- path/to/target.md > patches/001-example.patch
test -s patches/001-example.patch
git checkout -- path/to/target.md
git apply --check patches/001-example.patch
```

Required:

```yaml
patch_requirements:
  generated_by_git_diff: true
  has_diff_git_header: true
  has_index_old_new_blob_line: true
  has_correct_target_path: true
  applies_cleanly_after_target_restore: true
```

If the patch lacks this shape, it is not a valid Git-native patch:

```diff
diff --git a/path/to/file b/path/to/file
index <old_blob>..<new_blob> 100644
--- a/path/to/file
+++ b/path/to/file
@@ ...
```

### 4. Validate The Full Sequence

Use a disposable validation pass:

```bash
git checkout -- .

for p in $(find patches -maxdepth 1 -name '*.patch' -type f | sort); do
  echo "CHECK $p"
  git apply --check "$p"
done

for p in $(find patches -maxdepth 1 -name '*.patch' -type f | sort); do
  echo "APPLY $p"
  git apply "$p"
done

git diff --check
git diff --name-only | sort
```

The changed files must match `expected_changed_files`.

### 5. Run Semantic Or Smoke Checks

Every patch pack must prove more than "Git applied it."

Examples:

```bash
grep -R "required marker" path/to/package
! grep -R "forbidden marker" path/to/package
python -m py_compile path/to/script.py
python path/to/script.py --help
```

If the patch pack changes behavior, include a smoke test.

### 6. Restore The Worktree Before Export

After validation:

```bash
git checkout -- .
git clean -fd -- <only-generated-test-fixtures-if-needed>
git status --short
```

The patch creator must export patch artifacts, not leave target files edited.

### 7. Write The Validation Report Honestly

The validation report must say:

```yaml
validation_report:
  patch_files_git_generated: true
  git_apply_check_each_patch: pass
  git_apply_check_cumulative: pass
  disposable_apply_validation: pass
  changed_files_exactly_expected: pass
  semantic_or_smoke_checks: pass
```

If any of those are not true, write `false` or `not_run`.

Never describe a pack as ready if full `git apply --check` was not run against a real clone.

## Required Patch Pack Execution Process

Use this process when applying a patch pack.

### 1. Sync Main

```bash
git checkout main
git pull --ff-only origin main
git rev-parse HEAD
git status --short
```

### 2. Inspect Pack Quality

Before applying, check:

```yaml
executor_checks:
  manifest_exists: true
  patch_to_target_map_exists: true
  each_patch_touches_expected_target_only: true
  patches_have_diff_git_headers: true
  patches_have_index_old_new_blob_lines: true
  git_apply_check_passes: true
```

### 3. Classify The Pack

```yaml
class_A_executor_ready:
  all_executor_checks_pass: true
  action: apply normally

class_B_repair_first:
  git_apply_check_fails: true
  or_patch_lacks_blob_headers: true
  but_manifest_and_single_targets_exist: true
  action: repair patch artifacts first

class_C_reject:
  no_manifest: true
  or_ambiguous_targets: true
  or_dirty_target_overlap: true
  or_intent_requires_design_choices: true
  action: stop and request regeneration
```

### 4. Apply Class A Packs

```bash
for p in $(find patches -maxdepth 1 -name '*.patch' -type f | sort); do
  git apply --check "$p"
done

for p in $(find patches -maxdepth 1 -name '*.patch' -type f | sort); do
  git apply "$p"
done

git diff --check
# run pack-specific smoke/marker checks
```

### 5. Repair Class B Packs Before Final Apply

Do not apply partial patches to final targets.

Repair patch artifacts in a temporary branch/worktree:

```bash
BASE_SHA="$(git rev-parse HEAD)"
git checkout -B tmp/patch-pack-repair "$BASE_SHA"

# For each stale patch:
# 1. apply intended change to the one target
# 2. generate repaired patch with git diff -- target
# 3. restore target from BASE_SHA

git checkout main
```

Then prove the repaired pack:

```bash
for p in $(find patches -maxdepth 1 -name '*.patch' -type f | sort); do
  git apply --check "$p"
done
```

Run a disposable apply validation before final apply.

### 6. Reject Class C Packs

Stop with:

```yaml
FINAL_REPORT:
  verdict: FAIL
  reason: "patch pack is not safely repairable"
  action_needed: "regenerate patch pack from current origin/main using AI-Git-Native-Patch-Pack-Protocol.md"
```

## Explicit Failure Patterns And Required Response

### Failure: Patch Has No `diff --git`

Meaning:

```text
Patch was probably hand-authored or generated from excerpts.
```

Response:

```text
Do not call it executor-ready. Class B or C.
```

### Failure: Patch Has No `index <old>..<new>`

Meaning:

```text
No old-blob anchor exists. Git cannot prove baseline identity.
```

Response:

```text
Repair/regenerate with git diff in local clone.
```

### Failure: Validation Says `git_apply_check: not_run`

Meaning:

```text
The pack was not proven in a real clone.
```

Response:

```text
Do not trust readiness claims. Run local git apply --check.
```

### Failure: First Patch Fails At Line 1

Meaning:

```text
Patch hunk context likely came from an excerpt, not the real file position.
```

Response:

```text
Repair patch artifact or regenerate pack.
```

### Failure: Smoke Test Fails After Patches Apply

Meaning:

```text
Git syntax was valid, but the behavioral contract was wrong.
```

Response:

```text
Restore targets. Fix patch artifact. Re-run full check/apply/smoke.
```

## What To Tell The Operator

Be precise:

```text
This did not fail because your instruction changed.
It failed because the patch pack was not created and validated with the same Git-native process.
```

Do not hide behind generic "patch drift" if the real issue is:

```text
the AI-created patch pack was not Git-native or was not validated in a real clone.
```

## Short Version

```text
Create patches with Git.
Validate patches with Git.
Apply patches with Git.
If Git was not used during creation, the pack is not executor-ready.
```

