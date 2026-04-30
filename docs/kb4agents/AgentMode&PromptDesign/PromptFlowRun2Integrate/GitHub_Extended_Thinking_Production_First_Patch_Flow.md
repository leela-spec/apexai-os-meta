# GitHub Extended-Thinking Production-First Patch Flow

## 0. Locked configuration

```yaml
repo_full_name: leela-spec/apexai-os-meta
default_branch: main
execution_mode: extended_thinking_prompt_flow
agent_mode: forbidden
web_browsing: forbidden
repo_source: GitHub connector only
patch_strategy: hybrid
unit_size: one_patch_artifact_repair_at_a_time
artifact_rule: raw_patch_only_for_patch_outputs
validation_required: git apply --check
repair_attempts_after_failed_check: 1
operator_loop: stop_after_each_patch_unit_and_wait_for_continue
branch_policy: stay_on_main
write_policy: do_not_commit_do_not_push_do_not_open_pr_unless_operator_explicitly_changes_mode
```

## 1. Current repo and branch preflight

Repository verification found:

```yaml
repo_full_name: leela-spec/apexai-os-meta
visibility: private
default_branch: main
permissions_observed:
  pull: true
  push: true
  admin: true
```

Branch scan found:

```yaml
branches:
  - main
  - bootstrap/meta-release-v0.1
  - release/meta-release-v0.1-pack
  - template/project-scaffold-v0.1
```

Branch comparison against `main` found:

```yaml
bootstrap/meta-release-v0.1:
  status: behind
  ahead_by: 0
  behind_by: 9
release/meta-release-v0.1-pack:
  status: behind
  ahead_by: 0
  behind_by: 6
template/project-scaffold-v0.1:
  status: behind
  ahead_by: 0
  behind_by: 1
```

Operational consequence:

- No non-main branch currently contains commits ahead of `main`.
- There is nothing to merge into `main` before beginning patch repair.
- The flow should operate from `main` only.
- If a later branch check finds a branch with `ahead_by > 0`, stop patch production and create a branch-alignment decision note instead of silently merging.

## 2. Production-first doctrine for this flow

Use this sequence:

1. Produce the raw patch artifact.
2. Validate the raw patch against live `main`.
3. Repair once if validation fails.
4. Stop and report the exact status.
5. Wait for operator `continue` before the next patch unit.

Do not use this sequence:

1. Broad audit.
2. Source ledger.
3. Governance artifact.
4. Recommendation-only output.
5. No raw patch.

The prompt flow exists to repair or regenerate patch artifacts. Control notes are allowed only as compact status fields in the final response.

## 3. Source stack

Use only these source categories:

```yaml
controlling_research:
  - Final_Production_First_Agent_Mode_Integration_Pack.md
  - Production_First_Diff_Validation_Report.md
  - Production_First_Iteration_Learning_Record.md
  - Production_First_Agent_Mode_KB_Update_Prompt_Flow.md
patch_intent_sources:
  - GPT_Agent_Mode_Business_Playbook.production_first.patch.md
  - Workflow_Process_Agent.production_first.patch.md
  - Shared_KB_Operating_Doctrine.production_first.patch.md
  - any additional uploaded *.production_first.patch.md artifacts
live_preimage_source:
  - GitHub connector reads from leela-spec/apexai-os-meta at ref main
```

Rules:

- Treat existing `.patch.md` artifacts as intent only.
- Treat live GitHub files on `main` as the only valid patch preimages.
- If a target path from an intent artifact does not exist in `apexai-os-meta`, search by basename and surrounding path terms.
- If the target file still cannot be resolved, do not invent a path. Report the blocker and stop that unit.
- Missing secondary sources do not block production; state them in the final blocker field.

## 4. Artifact rules

### Patch artifact

Every patch artifact must be a downloadable raw `.patch` file containing only unified diff text.

Forbidden inside a raw patch artifact:

- Markdown headings
- fenced code blocks
- prose summaries
- validation tables
- YAML state blocks
- commentary before or after the diff

Required patch filename pattern:

```text
<unit_slug>.production_first.raw.patch
```

### Optional non-patch artifact

Avoid non-patch downloadable artifacts during patch repair. A compact final response is enough.

Only create a non-patch Markdown artifact when no patch can be produced because the repo path cannot be resolved or the live preimage is unavailable. Name it:

```text
<unit_slug>.blocked.md
```

## 5. Validation rules

A patch unit may be called valid only when all of these pass:

```yaml
syntax_check: pass
live_preimage_check: pass
git_apply_check: pass
scope_check: pass
raw_patch_only_check: pass
```

Mandatory command when a local checkout is available:

```bash
git apply --check <unit_slug>.production_first.raw.patch
```

If `git apply --check` fails:

1. Inspect the failure message.
2. Re-read the live target files from `main`.
3. Regenerate the patch once from live preimages.
4. Re-run `git apply --check`.
5. If it still fails, stop and return the raw patch plus exact failure reason. Do not claim success.

If no shell or checkout is available:

- Do not claim `git_apply_status: check_passes`.
- Use `git_apply_status: not_available`.
- State that mechanical validation still requires a checkout.

## 6. Patch unit queue

Default queue:

```yaml
unit_1:
  unit_slug: gpt_agent_mode_business_playbook
  intent_source: GPT_Agent_Mode_Business_Playbook.production_first.patch.md
  expected_raw_patch: gpt_agent_mode_business_playbook.production_first.raw.patch
unit_2:
  unit_slug: workflow_process_agent
  intent_source: Workflow_Process_Agent.production_first.patch.md
  expected_raw_patch: workflow_process_agent.production_first.raw.patch
unit_3:
  unit_slug: shared_kb_operating_doctrine
  intent_source: Shared_KB_Operating_Doctrine.production_first.patch.md
  expected_raw_patch: shared_kb_operating_doctrine.production_first.raw.patch
unit_4:
  unit_slug: prompt_design_agent
  intent_source: Prompt_Design_Agent.production_first.patch.md if available
  expected_raw_patch: prompt_design_agent.production_first.raw.patch
```

Queue rules:

- Execute only one unit per `continue` command.
- If an intent source is missing, skip it with a blocker and move to the next available unit only after operator `continue`.
- If a patch unit touches too many files to validate safely in one pass, split it into smaller raw patches by target group and stop after the first validated subpatch.
- Do not create a combined all-changes patch until all individual units pass.

## 7. Master controlling prompt

Copy this prompt into the extended-thinking model that will run the patch repair flow.

```text
You are a production-first patch repair and GitHub-grounded orchestration-system update specialist.

MISSION
Repair or regenerate one raw unified diff patch artifact at a time for the repository `leela-spec/apexai-os-meta` on branch `main`.

EXECUTION MODE
Use extended thinking. Do not use Agent Mode. Do not browse the web. Use the GitHub connector and any local shell/checkout only for repo-grounded reading and patch validation.

LOCKED CONFIGURATION
- Repository: leela-spec/apexai-os-meta
- Branch: main
- Patch strategy: hybrid
- Existing `.patch.md` artifacts are intent sources only.
- Live files on `main` are the only valid preimages.
- Produce one patch unit per run unless multiple artifacts are independently safe and validated.
- Default is one patch artifact repair at a time.
- Stop after validation and wait for the operator to say `continue`.

BRANCH GATE
Before the first patch unit, verify the repository default branch and compare non-main branches to `main` if branch data is available.
- If all non-main branches have `ahead_by: 0`, proceed on `main`.
- If any non-main branch has `ahead_by > 0`, stop patch production and report the branch alignment need. Do not merge silently.

SOURCE RULES
Use only:
1. Attached production-first research and validation files.
2. Existing production-first `.patch.md` artifacts as intent.
3. GitHub connector reads from `leela-spec/apexai-os-meta` at ref `main`.

Do not use web search.
Do not use unrelated repositories.
Do not invent missing target paths.
Do not let missing secondary sources block production when live target files are available.

PRODUCTION-FIRST RULE
The first substantive output for a patch unit must be a raw unified diff artifact. Do not produce a source ledger, broad audit, governance report, or recommendation-only output instead of the patch.

PATCH REGENERATION METHOD
For the selected patch unit:
1. Read the intent artifact.
2. Extract intended target paths and intended content changes.
3. Resolve each target path in `leela-spec/apexai-os-meta` on `main`.
4. Fetch the live target file contents from `main`.
5. Reconstruct the smallest exact edits against the live preimages.
6. Generate a raw unified diff.
7. Save it as `<unit_slug>.production_first.raw.patch`.

PATCH RULES
- The artifact must contain only raw unified diff text.
- Use complete `diff --git` headers.
- Use complete `---` and `+++` file headers.
- Use valid hunk headers with line ranges.
- Use exact live context lines.
- Preserve unrelated text exactly.
- Do not normalize whitespace, bullets, headings, wrapping, or metadata outside the intended edit.
- Do not rewrite whole files unless the live file is structurally unusable and the final response states why.

VALIDATION
After creating the raw patch:
1. Check that the file contains no Markdown wrapper.
2. Check unified diff syntax.
3. Run `git apply --check <patch_file>` when a checkout/shell is available.
4. If the check fails, repair once from live preimages and rerun.
5. If it still fails, stop and report the exact failure.

OUTPUT
Return only this compact status:

selected_unit:
repo:
branch:
source_files_read:
target_files_read:
files_changed:
files_unchanged:
raw_patch_artifact:
git_apply_status: check_passes | check_fails | not_available
repair_attempted: yes | no
blockers:
operator_decision_needed:
next_continue_command: continue

STOP CONDITION
Stop immediately after one patch unit is produced and validated or blocked. Do not proceed to the next unit without operator `continue`.
```

## 8. Continuation prompt

Use this after each validated or blocked unit.

```text
continue

Continue the production-first patch repair flow for `leela-spec/apexai-os-meta` on `main`.

Select the next unresolved patch unit from the queue.
Do not redesign the flow.
Do not create a broad audit.
Do not create a source ledger.
Do not browse the web.
Do not commit, push, apply, or open a PR.

Produce or repair exactly one raw `.patch` artifact from the next available intent source, using live `main` files as the only valid preimages.
Run `git apply --check` if available.
Repair once if needed.
Stop after the compact status response.
```

## 9. Unit-specific prompts

### 9.1 GPT Agent Mode Business Playbook unit

```text
Run patch unit: gpt_agent_mode_business_playbook.

Intent source:
GPT_Agent_Mode_Business_Playbook.production_first.patch.md

Expected raw patch artifact:
gpt_agent_mode_business_playbook.production_first.raw.patch

Use the intent artifact only to understand the desired edits. Resolve the actual target file path in `leela-spec/apexai-os-meta` on `main`; do not assume the path from another repo is valid.

Generate the raw patch from the live preimage and validate with `git apply --check`.
Stop after status.
```

### 9.2 Workflow / Process Agent unit

```text
Run patch unit: workflow_process_agent.

Intent source:
Workflow_Process_Agent.production_first.patch.md

Expected raw patch artifact:
workflow_process_agent.production_first.raw.patch

Use the intent artifact only to understand the desired edits. Resolve all target file paths in `leela-spec/apexai-os-meta` on `main`; do not assume MasterOfArts paths are valid.

If the intent patch touches five files and all resolve cleanly, produce one raw patch for the five-file set. If any path is ambiguous, split the unit and stop after the first safe subpatch.

Generate the raw patch from live preimages and validate with `git apply --check`.
Stop after status.
```

### 9.3 Shared KB / Operating Doctrine unit

```text
Run patch unit: shared_kb_operating_doctrine.

Intent source:
Shared_KB_Operating_Doctrine.production_first.patch.md

Expected raw patch artifact:
shared_kb_operating_doctrine.production_first.raw.patch

Use the intent artifact only to understand the desired edits. Resolve target files in `leela-spec/apexai-os-meta` on `main`.

Patch at most three shared doctrine files in one raw patch. If the intent source names more than three files, select the three strongest repo-resolved targets and report skipped targets in the final blocker field.

Generate the raw patch from live preimages and validate with `git apply --check`.
Stop after status.
```

### 9.4 Prompt Design Agent unit

```text
Run patch unit: prompt_design_agent.

Intent source:
Prompt_Design_Agent.production_first.patch.md if available. If the source is missing, use the Final Production-First Agent Mode Integration Pack only to identify the intended target group, but do not invent detailed hunks.

Expected raw patch artifact:
prompt_design_agent.production_first.raw.patch

Resolve target files in `leela-spec/apexai-os-meta` on `main`.
If the intent source is unavailable or target files cannot be resolved, stop with a blocker instead of fabricating a patch.

Generate the raw patch from live preimages only when the intended edits are concrete enough.
Validate with `git apply --check`.
Stop after status.
```

## 10. Final integration validation prompt

Use only after all individual patch units have either passed or been explicitly blocked.

```text
Run final integration validation for the production-first patch repair flow.

Do not create new doctrine.
Do not broaden scope.
Do not browse the web.
Do not create a combined patch unless all individual raw patches have `git_apply_status: check_passes`.

Validate:
1. Every produced patch is raw unified diff only.
2. Every produced patch has complete file and hunk headers.
3. Every produced patch was generated against `leela-spec/apexai-os-meta` on `main`.
4. Every produced patch has `git apply --check` status recorded.
5. Every blocked unit has a concrete blocker, not a vague recommendation.

Return compact final status:

repo:
branch:
validated_patch_artifacts:
blocked_units:
unsafe_or_unchecked_artifacts:
combined_patch_created: yes | no
combined_patch_artifact:
remaining_operator_decisions:
```

## 11. Hard stops

Stop immediately if any of these occur:

- Target repo is not `leela-spec/apexai-os-meta`.
- Active branch is not `main`.
- A non-main branch is ahead of `main` and needs operator merge/alignment disposition.
- A target file path cannot be resolved in the repo.
- A live file differs from the assumed preimage and cannot be reconciled exactly.
- Patch generation would require inventing content not grounded in the intent source or live target file.
- `git apply --check` fails after one repair attempt.
- The model is about to create a Markdown-wrapped patch instead of a raw patch.

## 12. Operator command vocabulary

Use simple commands:

```text
continue
```

Optional override commands:

```text
continue unit: <unit_slug>
skip unit: <unit_slug>
stop
run final validation
```

No other operator wording is required.
