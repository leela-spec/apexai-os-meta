---
learning_id: hygiene_clean_promptflow_execution_2026_05_04
source_chat_file: Chathistroyproomptflowhygiene.md
repo: leela-spec/MasterOfArts
target_root: OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/
status: captured
format: machine_readable_markdown_yaml
---

# LEARNINGS_PROMPTFLOW_HYGIENE_CLEAN_EXECUTION

```yaml
incident:
  summary: assistant repeatedly expanded scope during a bounded promptflow execution and skipped required manufacturing gates before being constrained by explicit execution-mode prompts.
  user_impact: high_frustration_context_loss_rework
  final_recovery: bounded per-file diff artifacts, patchset validation report, and zero-freedom Codex apply plan created in repo

root_causes:
  - id: RC-001
    name: scope_expansion_as_diligence
    pattern: assistant reread or searched for broader governance/context instead of executing the current bounded artifact step
  - id: RC-002
    name: phase_reopen_after_approval
    pattern: approved matrices were treated as inputs for renewed reasoning instead of closed decisions
  - id: RC-003
    name: output_location_mismatch
    pattern: assistant produced unified diff in chat when user intended repo-stored diff artifact
  - id: RC-004
    name: manufacturing_vs_design_confusion
    pattern: assistant treated artifact creation as design/governance work instead of deterministic manufacturing
  - id: RC-005
    name: helpful_improvement_drift
    pattern: assistant and anticipated Codex risk adding improvements, repairs, or inspiration not requested

failures:
  - id: F-001
    stage: phase_3
    failure: skipped candidate decision matrix gate before first patch-pack attempt
    correction: produce ranked decision matrix and wait for operator approval
  - id: F-002
    stage: phase_4_5
    failure: generated premature patch-pack and Codex prompt before approved per-file artifact workflow
    correction: require update design table, changed-file set, then one diff artifact per file
  - id: F-003
    stage: artifact_output
    failure: returned first unified diff in chat instead of writing it to repo appendix folder
    correction: create PATCH_001...PATCH_007 .diff files directly under appendices
  - id: F-004
    stage: continuation
    failure: context loss across iterations
    correction: create PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md as local rereference anchor

controls_that_worked:
  - id: C-001
    control: explicit EXECUTION MODE bounded artifact manufacturing
    effect: stopped broad reasoning and forced exact current-phase output
  - id: C-002
    control: one file per iteration
    effect: reduced context load and prevented mixed diffs
  - id: C-003
    control: repo-stored promptflow anchor
    effect: allowed continuation by next_pending_artifact instead of memory
  - id: C-004
    control: per-artifact validation yaml
    effect: made scope, path, and approval mapping explicit after each step
  - id: C-005
    control: zero-freedom Codex plan
    effect: blocks Codex content generation, repair, 3-way merge, reject mode, branch creation, and scope widening

future_rules:
  - id: R-001
    rule: once operator approves a decision matrix, do not reopen discovery/design unless explicitly requested
  - id: R-002
    rule: for MANUFACTURE tasks, produce only the named artifact and stop
  - id: R-003
    rule: if user says write/create directly in repo, do not output artifact only in chat
  - id: R-004
    rule: every multi-file patch workflow needs a repo-local promptflow anchor with next_pending_artifact
  - id: R-005
    rule: every diff artifact must be one target file only and validated before continuing
  - id: R-006
    rule: Codex plans must define executor-only role, exact patch list, git apply --check, changed-file allowlist, forbidden paths, and stop-on-failure
  - id: R-007
    rule: no hand edits, no inferred improvements, no missing-content generation during APPLY phase

recommended_command_labels:
  DISCOVER: broad research allowed
  DESIGN: tradeoffs allowed
  DECIDE: matrix/options for approval
  MANUFACTURE: no broad reasoning; create exact artifact
  VERIFY: check only listed criteria
  APPLY: execute approved diffs/commands only

canonical_manufacture_prompt:
  mode: bounded_artifact_manufacturing
  required_fields:
    - current_phase
    - exact_input_files
    - exact_output_artifact
    - allowed_actions
    - forbidden_actions
    - validation_checks
    - stop_condition
  forbidden_defaults:
    - source_expansion
    - broad_governance_reread
    - phase_reopen
    - extra_files
    - explanatory_recaps

created_repo_artifacts:
  - appendices/ChangesHygiene.md
  - appendices/ChangesHygiene2.md
  - appendices/PROMPTFLOW_HYGIENE_CLEAN_UNIFIED_DIFF_ARTIFACT_MANUFACTURING.md
  - appendices/PATCH_001_APP_KB_QA_AND_NEXT_RESEARCH_PLAN.diff
  - appendices/PATCH_002_ESSENCE.diff
  - appendices/PATCH_003_BEST_PRACTICES.diff
  - appendices/PATCH_004_TEMPLATES.diff
  - appendices/PATCH_005_LEARNING_QUEUE.diff
  - appendices/PATCH_006_APP_KB_CANDIDATE_LEDGER.diff
  - appendices/PATCH_007_APP_KB_SOURCE_MANIFEST.diff
  - appendices/PATCHSET_VALIDATION_REPORT.md
  - appendices/CODEX_APPLY_PLAN_HYGIENE_CLEAN_PATCHSET.md

success_condition_for_next_runs:
  - assistant reads only the named repo-local promptflow and current required artifact inputs
  - assistant performs exactly one current-phase action
  - assistant writes requested artifact to requested repo path
  - assistant validates only the declared checks
  - assistant stops without adjacent reasoning or extra deliverables
```
