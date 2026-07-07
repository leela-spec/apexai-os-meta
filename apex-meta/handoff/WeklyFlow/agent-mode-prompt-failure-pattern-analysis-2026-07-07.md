# Agent Mode Prompt Failure Pattern Analysis — 2026-07-07

## Purpose

This document records the repeated Agent Mode prompt failures around the APEX Step 1 Prompt-Blocker Cleanup patch-pack task.

It is not another patch prompt. It is a failure-pattern analysis intended to prevent repeating the same repair loop.

## Bottom-line assessment

The repeated failures were not caused by one isolated typo. They came from a repeated bad repair pattern:

> Each new prompt edit tried to fix the most recent failure directly, instead of preserving the working prompt's known-good structure and changing only the task-specific file map and semantic source plan.

The assistant repeatedly added new assumptions, guards, fallback behavior, clone behavior, local path behavior, or validation logic that was not present in the working example. Those additions created new failure modes.

## Failure timeline

| Run / stage | Intended improvement | Actual effect | Failure pattern |
|---|---|---|---|
| Initial prompt generation | Follow guide and working example | Prompt was structurally close but made source-plan patching authority too implicit | Copied shape, missed execution-critical semantic bridge |
| B1-B6 bridge patch | Make Sections 5-7 explicit authority | Improved semantic clarity | Useful fix; not the root runtime issue |
| AgentPrompt_v1 validation | Check for overengineering / new failure patterns | New-file patch generation risk was found | Valid critique, but not enough runtime validation |
| AgentPrompt_v3 validation | Avoid overthinking and approve realistic prompt | Marked prompt as safe enough | Overconfidence: runtime repo-access assumptions were not checked against Agent Mode launch behavior |
| First Agent Mode run | Generate fallback archive if push unavailable | Agent ran in local `patchwork`, did not read source plan, created placeholder patches | Fallback allowed artifact generation without proving real repo + source plan + target-file access |
| First postmortem | Identify placeholder/fallback problem | Correctly identified fake patches, but initially framed GitHub push status too prominently | Evaluated delivery status before artifact integrity |
| Clone patch | Force real repo by cloning | Failed because Agent Mode environment lacked network access | Added environment-acquisition behavior not present in working example |
| Local Windows path patch | Require `C:\GitDev\apexai-os-meta` | Failed because Agent Mode did not run inside that Windows path | Added user-local path assumption that Agent Mode could not satisfy |
| Script patch | Deterministically replace clone block | Risked reinforcing the wrong local-path fix | Automation of a bad correction |
| Generic preflight correction | Remove local path and clone, restore working-preflight logic | Correct direction, but came after multiple avoidable failures | Late return to working-pattern principle |

## Root causes

### 1. Repair-by-last-error instead of copy-the-working-prompt

The user explicitly requested that the working prompt be copied and only task-specific fields changed.

The assistant repeatedly drifted from that instruction by adding:

- custom fallback gates,
- clone instructions,
- local Windows path requirements,
- `/home/oai/share` assumptions,
- synthetic-repo bans patched in multiple different forms,
- extra report semantics,
- confidence scores that were not validated against the real Agent Mode environment.

The correct method should have been:

1. Take the working prompt as the locked skeleton.
2. Replace only:
   - title / role,
   - repo / branch if needed,
   - patch-pack path,
   - primary source plan path,
   - target-file and patch-file list,
   - task-specific required semantic markers,
   - task-specific forbidden paths.
3. Do not add environment setup logic that the working prompt did not use.

### 2. Confusing three different questions

The assistant repeatedly mixed these questions:

| Question | Correct check | Mistake made |
|---|---|---|
| Did Agent Mode deliver artifacts to GitHub main? | Check repo path / commits | Checked too early and overemphasized delivery |
| Are exported patches syntactically valid? | Inspect patch headers and `git apply --check` context | Accepted PASS too easily without source-plan access |
| Are patches semantically valid against real repo files? | Confirm source_plan_read, real target baselines, marker validation | Initially missed that `source_plan_read: false` is fatal |

The key invariant should have been:

```yaml
source_plan_read: true
real_git_worktree_used: true
real_target_files_read: true
placeholder_files_created: false
cumulative_marker_validation: PASS
```

Without these, the run cannot be called successful.

### 3. Fallback mode was not tightly gated

The first patch prompt allowed fallback behavior before proving that real patches existed.

That allowed Agent Mode to:

- run outside the real repository,
- create a local `patchwork` repo,
- create placeholder target files,
- generate syntactically valid but semantically useless patches,
- report `PARTIAL_ARTIFACT_EXPORT` instead of `FAIL`.

Correct invariant:

```text
Fallback archive mode is allowed only after real patches have already been generated from real repo files and the only failed step is push/export persistence.
```

Fallback must never be a path for missing repo, missing origin, missing source plan, missing target files, API reconstruction, or placeholder file generation.

### 4. Clone instruction introduced a new environment failure

The assistant then tried to fix the missing repo by adding:

```bash
git clone https://github.com/leela-spec/apexai-os-meta.git
```

This was wrong because:

- it was not in the working example,
- Agent Mode may not have network access,
- private repo auth may not be available,
- the working pattern expected an already mounted/live Git worktree.

Result:

```yaml
failure_reason: "Unable to clone the required repository due to network access restrictions"
```

This was a new failure introduced by the assistant.

### 5. Local Windows path requirement introduced another environment failure

The assistant then tried:

```text
This prompt must be run from inside:
C:\GitDev\apexai-os-meta
```

This was wrong because:

- Agent Mode may run in a Linux-like sandbox,
- the user-local Windows path is not necessarily visible to Agent Mode,
- the working prompt did not require this path,
- it converted a prompt meant for a mounted live repo into a local-machine-specific prompt.

Result:

```yaml
failure_reason: "Prompt was not run from inside the existing apexai-os-meta Git checkout."
```

This was another failure introduced by the assistant.

### 6. Confidence scores were used too casually

The assistant gave high confidence scores such as `91`, `94`, or `safe_to_use: true` while not validating the actual Agent Mode runtime assumption.

This created false assurance.

For this task, confidence should have been conditional:

```yaml
safe_if:
  - Agent Mode starts inside a real repo checkout with origin configured
  - source plan exists in that checkout
  - target files exist in that checkout
unsafe_if:
  - Agent Mode starts in a blank sandbox
  - Agent Mode has no mounted repo
  - Agent Mode must clone over network
```

### 7. Structural similarity was mistaken for behavioral equivalence

The prompt looked like the working example but diverged in behaviorally important places:

- fallback semantics,
- repo acquisition assumptions,
- new-file handling,
- source-plan authority,
- local path constraints.

A correct comparison against the working example should have produced a drift table before any run:

| Prompt section | Working example behavior | New prompt behavior | Allowed? |
|---|---|---|---|
| Repo access | Assume live terminal repo | Added clone / local path in later versions | No |
| Fallback | Export only when push unavailable | Initially allowed generation without real source | No |
| Source plan | Must read primary plan | Run reported source_plan_read:false | Fatal |
| Patch generation | Real git diff from real target files | Placeholder patches in failed run | Fatal |

## Correct stable rule going forward

Use this rule for all future Agent Mode patch-pack prompts:

```text
Copy the working prompt skeleton.
Only change the task-specific values.
Do not add clone logic.
Do not add local absolute paths.
Do not add synthetic repo creation.
Do not add API reconstruction.
Do not broaden fallback mode.
Do not convert missing repo/source/target into PARTIAL_ARTIFACT_EXPORT.
```

## Minimal allowed differences from the working prompt

Future prompts may change only:

| Allowed change | Example |
|---|---|
| Task title | `APEX Step 1 Prompt-Blocker Cleanup` |
| Patch-pack path | `apex-meta/patch-packs/...` |
| Source plan path | `apex-meta/patch-plans/...` |
| Optional repair/blocker file | `Blockers.md` |
| Target-file map | 001-022 target files |
| Patch-file map | 001-022 patch files |
| Required semantic markers | B1-B6 / Sections 5-7 references |
| Forbidden mutation paths | Task-specific forbidden files/folders |
| Final report fields | Only if copied from guide/source plan |

Everything else should remain as close as possible to the working prompt.

## Hard gates for future run evaluation

A run is successful only if all are true:

```yaml
normal_or_export_mode:
  source_plan_read: true
  real_git_worktree_used: true
  origin_verified: true_or_push_only_failure
  placeholder_files_created: false
  api_reconstruction_used: false
  patch_files_created: all_expected
  each_patch_git_apply_check: PASS
  cumulative_patch_check: PASS
  cumulative_marker_validation: PASS
  target_files_modified_by_patch_pack_commits: false
  forbidden_files_touched: false
```

A run must be classified as failed if any are true:

```yaml
fatal_flags:
  source_plan_read: false
  real_git_worktree_used: false
  placeholder_files_created: true
  cumulative_marker_validation: FAIL
  patch_files_created_from_fake_baseline: true
  clone_required_but_network_unavailable: true
  local_windows_path_required_inside_agent_mode: true
```

## Do-not-repeat list

Do not repeat these assistant behaviors:

1. Do not validate a prompt as safe based only on textual similarity.
2. Do not invent repo setup steps that the working prompt did not include.
3. Do not add `git clone` unless the operator explicitly says the Agent Mode environment supports network clone and auth.
4. Do not add `C:\GitDev\...` as an Agent Mode runtime requirement.
5. Do not allow fallback mode before real source-plan and target-file reads.
6. Do not accept `git apply --check: PASS` if the patch baseline may be synthetic.
7. Do not call `PARTIAL_ARTIFACT_EXPORT` acceptable when `source_plan_read:false`.
8. Do not generate or approve placeholder patches.
9. Do not create patch scripts for a correction before verifying the correction is directionally valid.
10. Do not keep patching from memory of the previous failure; compare against the working example every time.

## Correct next operational path

The next attempt should not be another creative prompt repair.

Use one of two options:

### Option A — Run Agent Mode only in the correct environment

Launch Agent Mode from a real live checkout of `leela-spec/apexai-os-meta` with origin configured and the source plan present.

Then use a prompt that is copied from the working example with only task-specific values changed.

### Option B — Stop using Agent Mode for this patch-pack build

Use Codex or a local terminal where the repo is already checked out at:

```text
C:\GitDev\apexai-os-meta
```

Then execute a deterministic local patch-pack script or manual Git-native process.

This avoids Agent Mode environment ambiguity entirely.

## Accountability note

The assistant's main reliability failure was not a single wrong command. It was the repeated pattern of making plausible-sounding prompt repairs without preserving the known-good prompt skeleton and without validating the actual runtime environment assumptions.

The user request was to copy the working prompt and only change task-specific details. The assistant repeatedly violated that by adding new environment behavior. That is the direct cause of several additional failed runs.