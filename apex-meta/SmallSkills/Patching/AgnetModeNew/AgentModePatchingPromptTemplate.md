# Agent Mode Patching Prompt Template

```okf
okf_document:
  id: agent_mode_patching_prompt_template_v2
  title: Agent Mode Patching Prompt Template v2
  status: reusable_template
  purpose: >
    Reusable neutral template for future Agent Mode, patch-pack, and repo-edit
    workflows without inheriting old patch counts, target maps, marker strings,
    or environment assumptions. Version 2 adds executor-gate, mission-preservation,
    repair-coverage, and patch-grouping fields so the worker cannot fix the last
    failure by forgetting the actual task.
```

## 0. Template Use Rules

```yaml
template_sections:
  invariant_rules:
    purpose: copied unchanged
  environment_mode_selection:
    purpose: filled based on actual run
  run_parameters:
    purpose: must be rewritten every run
  validation:
    purpose: must use task-specific commands
  final_report:
    purpose: must expose mode, limits, and evidence

rewrite_every_run:
  - <REPO>
  - <BRANCH>
  - <PATCH_PACK_ROOT>
  - <SOURCE_PLAN_PATH>
  - <TARGET_FILES>
  - <FORBIDDEN_PATHS>
  - <REQUIRED_CHANGES>
  - <REQUIRED_MARKERS>
  - <VALIDATION_COMMANDS>
  - <OUTPUT_ARTIFACTS>
  - <FINAL_REPORT_SCHEMA>
  - <EXECUTOR_GATE_REQUIREMENT>
  - <REPAIR_AREAS_OR_DELIVERABLE_COVERAGE>
  - <PATCH_GROUPING_RULE>
  - <INVALID_HISTORICAL_ARTIFACTS>
```

---

# Agent Mode Task — <TASK_NAME>

You are GPT-5.5 Agent Mode acting as `<ROLE>`.

## 1. Mission

```yaml
mission:
  task: "<ONE_SENTENCE_TASK>"
  repo: "<REPO>"
  branch: "<BRANCH>"
  output_mode: "<PATCH_PACK | DIRECT_REPO_EDIT | DOC_ONLY | ANALYSIS_ONLY>"
```

Do not build anything outside the declared output mode.

Do not let executor-access checks replace the declared mission.

Do not import target files, patch counts, marker checks, or failure details from previous runs.

## 1.1 Mission Preservation Lock

Fill this section whenever the task has multiple repair areas, deliverables, or source-plan targets.

```yaml
mission_preservation_lock:
  declared_deliverables:
<REPAIR_AREAS_OR_DELIVERABLE_COVERAGE>
  rule: >
    Every declared deliverable must be completed, explicitly omitted with a reason,
    or marked failed. Executor preflight is a gate, not a deliverable.
  forbidden_completion_patterns:
    - "PASS after access check only"
    - "dropping repair areas after adding a new guard"
    - "replacing the landed source plan with a newly invented plan"
```

## 1.2 Invalid Historical Artifacts

Fill this section when prior failed patch packs, transcripts, or examples exist.

```yaml
invalid_historical_artifacts:
<INVALID_HISTORICAL_ARTIFACTS>
handling_rules:
  - "read only if the source plan names them as evidence"
  - "do not copy patch hunks, target maps, or marker checks from them"
  - "never use failed patch files as implementation authority"
```

## 2. Invariant Rules

```yaml
invariant_rules:
  anti_fabrication:
    - "Do not fabricate missing source files."
    - "Do not create placeholder implementation artifacts."
    - "Do not claim PASS without mechanical evidence."
  source_grounding:
    - "Read the declared source plan before producing artifacts."
    - "Record missing or partial sources explicitly."
  validation:
    - "Use mechanical validation appropriate to the declared environment mode."
    - "Use behavior checks when scripts or executable workflows change."
  reporting:
    - "Report environment mode, limits, outputs, validation, commit/export state, and blockers."
```

## 3. Environment Mode Selection

Choose exactly one mode after preflight. If the task requires live Git and the
preflight fails, stop immediately with WRONG_EXECUTOR. Do not search for the repo
or switch into API reconstruction.

```yaml
executor_gate:
  required_when: "<EXECUTOR_GATE_REQUIREMENT>"
  live_git_one_shot_checks:
    - "git rev-parse --show-toplevel"
    - "git rev-parse --is-inside-work-tree"
    - "git remote get-url origin"
    - "git branch --show-current"
  required_result:
    inside_work_tree: true
    origin_contains: "<REPO>"
    branch: "<BRANCH>"
  if_failed:
    verdict: WRONG_EXECUTOR
    patch_generation_started: false
    pushed: false
  forbidden_recovery:
    - "find / -name <repo>"
    - "inspect /home/oai/share, /workspace, /mnt/data, or /tmp as fallback"
    - "git clone"
    - "git init"
    - "GitHub/API baseline reconstruction"
```

Use `api_mirror` only when the prompt explicitly authorizes mirror mode. Do not
automatically reinterpret a Git-native task as API mirror mode.

```yaml
environment_mode_selection:
  live_git_worktree:
    use_when: "A real checked-out repo is available and git commands operate against it."
    required_preflight:
      - "git rev-parse --show-toplevel"
      - "git rev-parse --is-inside-work-tree"
      - "git remote get-url origin"
      - "git branch --show-current"
      - "git status --porcelain"
    allowed:
      - "git diff generated patches"
      - "git apply --check"
      - "commit/push or local export"
    forbidden:
      - "API snippet baseline reconstruction"
      - "synthetic git init repo"

  api_mirror:
    use_when: "No live worktree exists, but full files can be fetched and this mode is explicitly authorized."
    allowed_only_if_explicitly_authorized:
      - "local mirror seeded from fetched full files"
      - "archive/export draft artifacts"
      - "connector-written documentation files"
    required_warnings:
      - "baseline may be stale"
      - "requires live repo revalidation before patch application"
    forbidden:
      - "claiming Git-native validation"
      - "claiming pushed repo state unless connector write actually committed"

  blocked:
    use_when: "Neither live worktree nor reliable full-source access exists."
    required_action:
      - "stop"
      - "report SOURCE_ACCESS_FAILED"
```

## 4. Run Parameters

Fill these fresh. Do not keep placeholder text in the final prompt.

```yaml
run_parameters:
  repo: "<REPO>"
  branch: "<BRANCH>"
  patch_pack_root: "<PATCH_PACK_ROOT>"
  source_plan_path: "<SOURCE_PLAN_PATH>"
  target_files:
<TARGET_FILES>
  forbidden_paths:
<FORBIDDEN_PATHS>
  patch_grouping_rule:
<PATCH_GROUPING_RULE>
  invalid_historical_artifacts:
<INVALID_HISTORICAL_ARTIFACTS>
  deliverable_coverage:
<REPAIR_AREAS_OR_DELIVERABLE_COVERAGE>
  required_changes:
<REQUIRED_CHANGES>
  required_markers:
<REQUIRED_MARKERS>
  validation_commands:
<VALIDATION_COMMANDS>
  output_artifacts:
<OUTPUT_ARTIFACTS>
```

## 5. Source Access Gate

Read first:

```text
<SOURCE_PLAN_PATH>
```

Then read every target file listed in `<TARGET_FILES>` if the task changes target files.

If a required source is missing, stop unless the run parameters define an authorized fallback.

```yaml
SOURCE_ACCESS_FAILED:
  folder_or_file: "<MISSING_SOURCE>"
  missing_files:
    - "<path>"
  action_needed: "Mount, upload, or authorize fallback source access."
```

## 6. Procedure

### 6.1 Patch-Pack Mode

```yaml
patch_pack_mode:
  procedure:
    - "start from declared environment mode"
    - "read source plan"
    - "read current target files"
    - "for each repo target path, modify only that path and include all same-file repair areas in one patch unless the source plan explicitly requires an ordered same-file patch stack"
    - "generate patch artifact with environment-appropriate method"
    - "validate each patch"
    - "validate cumulative application when live Git worktree exists"
    - "revert target files in builder final state"
    - "persist patch-pack artifacts only"
  live_git_required_checks:
    - "git diff --no-ext-diff -- <target-file> > <patch-file>"
    - "test -s <patch-file>"
    - "grep '^diff --git ' <patch-file>"
    - "git apply --check <patch-file>"
    - "git apply --check all patches in order"
  required_manifest_fields:
    - "patch_file"
    - "target_file"
    - "repair_areas_or_deliverables_covered"
    - "omitted_repair_areas_with_reason"
  forbidden:
    - "one patch per feature when multiple features modify the same file and the source plan does not require that split"
    - "PASS_WITH_WORKAROUNDS"
    - "marker-only behavior proof for executable changes"
```

### 6.2 Direct Repo Edit Mode

```yaml
direct_repo_edit_mode:
  procedure:
    - "read source plan"
    - "modify only allowed target files"
    - "run validation commands"
    - "verify changed-file scope"
    - "commit and push if requested and available"
  required_checks:
    - "changed-file scope equals allowed files"
    - "validation commands pass or fail explicitly"
```

### 6.3 Documentation-Only Mode

```yaml
doc_only_mode:
  procedure:
    - "read source files"
    - "create requested documentation artifacts"
    - "include source index if required"
    - "include anti-drift check if required"
    - "commit through available repo write surface if requested"
```

## 7. Validation

Use task-specific commands only.

```yaml
validation:
  commands:
<VALIDATION_COMMANDS>
  required_markers:
<REQUIRED_MARKERS>
  forbidden_markers:
    - "<FORBIDDEN_MARKER_IF_ANY>"
  changed_file_scope:
    allowed:
<TARGET_FILES>
```

Do not treat marker presence as behavior proof when executable code changes.

If the task has declared repair areas, validation must include a coverage ledger.

## 8. Output Artifacts

```yaml
output_artifacts:
<OUTPUT_ARTIFACTS>
```

Artifacts must be complete. No placeholder implementation artifacts.

## 9. Final Report

Use this schema unless the run defines a stricter one.

```yaml
FINAL_REPORT:
  verdict: "PASS | PARTIAL | FAIL | WRONG_EXECUTOR"
  environment_mode: "live_git_worktree | api_mirror | blocked"
  repo: "<REPO>"
  branch: "<BRANCH>"
  files_read:
    count: 0
    files:
      - "<path>"
  outputs_created:
    - "<path>"
  executor_gate:
    required: true|false
    result: "PASS | WRONG_EXECUTOR | NA"
  deliverable_coverage:
    declared:
      - "<deliverable_or_repair_area>"
    completed:
      - "<deliverable_or_repair_area>"
    omitted:
      - name: "<deliverable_or_repair_area>"
        reason: "<reason>"
  validation:
    mechanical_validation: "PASS | FAIL | NA"
    changed_file_scope: "PASS | FAIL | NA"
    required_markers: "PASS | FAIL | NA"
    forbidden_markers: "PASS | FAIL | NA"
    behavior_checks: "PASS | FAIL | NA"
  patch_grouping:
    rule: "<PATCH_GROUPING_RULE>"
    exceptions:
      - "<only-if-used>"
  persistence:
    committed: true|false
    sha: "<sha-or-NA>"
    pushed: true|false
    archive: "<path-or-NA>"
  limitations:
    - "<only if relevant>"
  blockers:
    - "<only if FAIL>"
```

## 10. Anti-Drift Self-Check

Before finalizing, verify:

```yaml
anti_drift_check:
  no_old_batch_count_is_default: true
  no_old_target_path_is_default: true
  no_old_patch_file_list_is_default: true
  no_old_environment_assumption_is_default: true
  all_run_parameters_rewritten: true
  examples_marked_example_only: true
  executor_gate_does_not_replace_mission: true
  deliverable_coverage_complete_or_explained: true
  same_target_repairs_grouped_unless_exception: true
  invalid_historical_artifacts_not_used_as_authority: true
  placeholders_present_only_in_template: true
```

## 11. Optional Example Section

```yaml
example_policy:
  status: example_only
  rule: >
    Any concrete repo path, file count, patch count, marker string, or validation
    command shown here must be replaced before execution.
```
