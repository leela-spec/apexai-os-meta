fff# Agent Mode Patching Best-Practice Guide

```okf
okf_document:
  id: agent_mode_patching_best_practice_guide_v2
  status: neutral_general_process_standard_with_failure_learning
  purpose: >
    reusable guide for Agent Mode patch-pack and repo-edit workflows that
    preserves accumulated failure findings without letting the last failure mode
    erase the mission, payload, or proven execution model
```

## 1. Executive Verdict

```okf
verdict:
  root_issue: run_specific_instruction_contamination
  definition: concrete details from one run became false global doctrine
  durable_fix: separate invariants, environment modes, run parameters, and examples
  pass_rule: no PASS without source access, complete outputs, validation evidence, and persistence evidence
  v2_correction: executor guards must prevent wrong-runtime waste without narrowing the mission
```

## 1.1 V2 Failure-Learning Addendum

```okf
v2_failure_learning:
  core_problem: >
    Previous prompts overcorrected to the most recent failure and forgot older
    accepted findings. A valid process guide must preserve the full finding set,
    not merely patch the last observed error.
  wrong_executor_guard:
    rule: >
      If a live terminal Git worktree is required, verify it once and stop with
      WRONG_EXECUTOR when absent. Do not search the filesystem, clone, initialize
      synthetic repos, or reconstruct baselines from connector/API snippets.
    prevents:
      - generic Agent Mode container wasting a run by searching /home/oai/share
      - API/connector reconstruction being mislabeled as Git-native
      - synthetic repo validation against fake baselines
  mission_preservation_guard:
    rule: >
      Executor checks are gates, not the task. After the gate passes, the worker
      must still implement every declared repair area or output an explicit
      omitted-repair ledger.
    prevents:
      - narrowing the prompt to git preflight
      - dropping repair payload after adding environment checks
      - treating access validation as progress
  source_plan_supremacy:
    rule: >
      A landed source-plan package overrides ad-hoc prompt memory. The prompt
      should wrap the plan with execution rules; it must not re-author the plan.
    prevents:
      - architecture rediscovery
      - stale prompt lists overriding the package manifest
      - repeated debate of already-accepted decisions
```

## 1.2 Best Incorporation Strategy

```okf
best_way_to_incorporate_findings:
  do_not_depend_on_chat_memory: true
  durable_carriers:
    - guide_file_v2
    - prompt_template_v2
    - patch_script_or_apply_handoff
    - source_plan_manifest
  required_mechanism:
    - encode findings as executable gates and report fields
    - require coverage ledgers for every declared repair area
    - classify old examples as example_only or anti_pattern
    - use scripts/patches where possible instead of prose-only correction
  operator_rule: >
    When the same failure repeats, patch the process artifacts first. Do not run
    another live execution prompt until the process artifacts encode the missing
    guard.
```

## 2. Core Distinction: Invariants vs Environment Modes vs Run Parameters

| class | meaning | examples | handling |
|---|---|---|---|
| invariant_principles | always true | no fabrication, source ledger, mechanical validation, honest report | copy unchanged |
| environment_modes | execution-surface specific | live_git_worktree, api_mirror, blocked | detect or declare |
| run_parameters | fresh per run | repo, branch, source plan, targets, forbidden paths, validation | rewrite every run |
| historical_examples | evidence only | working prompts, failed transcripts, old patch packs | mark example_only or anti_pattern |

```okf
run_parameters_must_be_fresh:
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
```

## 3. Ranked Principles and Checks

| rank | principle | category | why_it_matters | failure_prevented | type | simple_rule | machine_check | evidence_files | risk_if_overapplied |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | do not fabricate placeholders | anti_fabrication | fake artifacts create false progress | empty patches, invented files | invariant | no placeholder implementation | `test -s`, reject TODO-only outputs | AgentModePatchGuide_v4.md | templates may legitimately contain placeholders |
| 2 | do not trust unverified large-file or connector reads | source_access | snippets can omit baseline context | stale diffs | invariant | full-file or partial ledger | read ledger | FailureAgentModeNew, NoLocalGitWorktree | API mirror can still be authorized |
| 3 | separate invariants from run parameters | prompt_design | prevents stale target maps | run-specific contamination | invariant | no old defaults in guide | scan fixed counts/old paths | ChatHistory_ConstantFailurePrompts | too abstract if placeholders not filled |
| 4 | make environment mode explicit | environment_mode | same command has different meaning by surface | false Git-native claims | mode_specific | choose one mode | final report mode field | AgentModePatchGuide_v4 | avoid huge mode taxonomy |
| 5 | validate mechanically, not rhetorically | validation | confidence is not evidence | invalid hunks, marker-only PASS | invariant | require command evidence | git apply/compile/smoke | AgentModePatchGuide_v4 | marker checks alone are weak |
| 6 | live Git only for Git-native claims | patch_integrity | synthetic repo validates fake baseline | fake Git-native patch pack | mode_specific | no worktree, no Git-native PASS | git rev-parse/remote | NoLocalGitWorktree | label API mirror separately |
| 7 | API mirror requires explicit authorization | environment_mode | connector baselines are weaker | silent reconstruction | mode_specific | warn and require revalidation | mirror report | MirrorMode | too strict for docs-only writes |
| 8 | source access is a hard gate | source_access | unread sources cause invention | fake source index | invariant | stop or mark missing | missing ledger | current handover | partial output must be labeled |
| 9 | one patch per target file by default | patch_integrity | simplifies review and rollback | multi-file hunk confusion | mode_specific | 1 file per patch unless exception | count diff headers | AgentModePatchGuide_v4 | exceptions may be needed |
| 10 | builder final state keeps targets clean | artifact_delivery | builder produces artifacts, not final implementation | direct mutation | mode_specific | commit/export artifacts only | git status targets | AgentModePatchGuide_v4 | not for direct-edit mode |
| 11 | dirty-tree policy must be scoped | scope_control | unrelated dirt should not block | false blockers | invariant | block only overlapping paths | path overlap check | execution audits | generated files may overlap |
| 12 | behavior checks outrank marker checks | validation | strings can hide stubs | stub success | invariant | scripts need compile/smoke | py_compile/help/sample | failure audits | docs-only changes may not need smoke |
| 13 | prompt is execution contract, not failure anthology | prompt_design | history distracts worker | stale defensive prompt | invariant | mission/source/scope/method/report | prompt lint | ChatHistory | keep concise constraints |
| 14 | historical examples are examples only | handover_design | examples contain task values | copied old patch list | example_only | copy structure not values | source index use field | WorkingPromptExample | do not ignore proven skeleton |
| 15 | persistence claims require evidence | artifact_delivery | created/exported/pushed differ | false pushed state | invariant | SHA or archive path | commit SHA/archive exists | process guide | keep report compact |
| 16 | forbidden paths are run parameters | scope_control | blast radius changes by task | universal false blockers | run_parameter | fill fresh | diff scope | current handover | project-wide rules may still apply |
| 17 | validation commands are run parameters | validation | old commands may be irrelevant | fake validation | run_parameter | fill fresh | command log | current handover | keep generic access checks |
| 18 | report partial completion honestly | artifact_delivery | useful partial is not PASS | hidden failure | invariant | PASS only if all gates pass | final verdict/blockers | process guide | avoid normalizing incomplete work |

## 4. Environment Mode Matrix

| mode | meaning | allowed | forbidden | report requirement |
|---|---|---|---|---|
| live_git_worktree | real checked-out repo, Git works against it | git diff patches; git apply --check; cumulative validation; commit artifacts | API snippet baseline; synthetic git init repo | root, branch, remote, dirty state, validation, SHA |
| api_mirror | no worktree, but full files can be fetched and mode is authorized | full-file mirror; archive/export; connector-written docs | Git-native PASS; pushed claim without connector commit | stale-baseline warning; live revalidation needed |
| blocked | no reliable source access | stop and report | patch generation; invented files | SOURCE_ACCESS_FAILED |

```okf
wrong_executor_gate:
  use_when: "task explicitly requires live terminal Git worktree"
  one_shot_checks:
    - git rev-parse --show-toplevel
    - git rev-parse --is-inside-work-tree
    - git remote get-url origin
    - git branch --show-current
  if_failed:
    verdict: WRONG_EXECUTOR
    patch_generation_started: false
    allowed_next_actions: ["report only"]
  forbidden_recovery:
    - find / -name repo
    - inspect /home/oai/share or /workspace as a fallback
    - git clone
    - git init
    - GitHub/API baseline reconstruction
```

## 5. Source Access and Read Verification

```okf
read_ledger_required_fields:
  - path
  - access_method
  - status: read | partial | missing
  - use: authority | evidence | example_only | anti_pattern
  - limitation
rules:
  - search snippets are not full-file proof
  - connector metadata is not freshness proof
  - missing sources must be explicit
```

## 6. Patch Generation and Validation

```okf
live_git_patch_contract:
  required:
    - read source plan
    - read current targets
    - modify one target at a time
    - generate patch with git diff
    - verify non-empty patch when change expected
    - run git apply --check per patch and cumulatively
    - run compile/smoke tests for code changes
    - revert target files in builder mode
  forbidden:
    - hand-written hunk headers
    - synthetic repo baselines
    - snippet-assembled patches
    - PASS_WITH_WORKAROUNDS when git apply fails
```

## 6.1 Patch Grouping Rule

```okf
patch_grouping_rule:
  default: one_git_generated_patch_per_repo_target_path
  rationale: >
    A single target file may carry multiple repair areas. Splitting those into
    separate feature patches against the same baseline often creates cumulative
    hunk failures or ordering fragility.
  apply:
    - merge all changes for the same repo target path into one patch
    - list every repair area covered by that patch in the manifest
    - only split same-file patches when the source plan explicitly requires an ordered stack
  examples:
    good:
      apex-meta/scripts/apex_kb.py: [pointer_only_phase0, quality_coverage, query_eval, graph_process_flow, status_freshness_split]
    bad:
      - 003-pointer-only.patch against apex_kb.py
      - 005-quality.patch against the same original apex_kb.py baseline
      - 006-query-eval.patch against the same original apex_kb.py baseline
  manifest_required_fields:
    - patch_file
    - target_file
    - repair_areas_covered
```

## 7. Anti-Fabrication and Partial Completion Rules

```okf
fail_if:
  - source plan unreadable and no authorized fallback
  - target file missing and patch depends on it
  - patch is empty but reported as implementation
  - report claims push without commit evidence
partial_if:
  - valid artifacts created but not persisted
  - API mirror artifacts need live validation
  - some sources missing but ledger is explicit
pass_only_if:
  - claimed mode gates passed
  - requested outputs exist
  - required index/ranking/template exist
  - old run-specific details are not defaults
```

## 8. Artifact Packaging and Delivery

```okf
artifact_delivery:
  patch_pack_builder:
    outputs: [manifest, patch_files, validation_report, apply_handoff]
    final_state: {target_files_modified: false, artifacts_persisted: true}
  direct_repo_edit:
    outputs: [changed_files, validation_report, commit_sha]
  documentation_output:
    outputs: [guide, template, source_index, final_report]
```

## 9. Prompt Design Rules

```okf
include: [role, mission, environment_mode_selection, invariant_rules, run_parameters, source_access_gate, target_scope, required_changes, validation_commands, output_artifacts, final_report_schema]
exclude: [old_failure_transcripts, old_patch_counts, old_target_maps_as_defaults, architecture_rediscovery, fallback_maze, speculative_blockers]
```

## 10. Common Anti-Patterns

| anti_pattern | why_bad | correction |
|---|---|---|
| run-specific contamination | one repair wave becomes doctrine | classify every item |
| synthetic repo as live Git | validates fake baseline | claim Git-native only with real worktree |
| connector snippet baseline | partial source | use full-file fetch or stop |
| prompt as failure anthology | stale defensive behavior | compact execution contract |
| marker-only validation | stubs pass | compile/smoke tests |
| placeholder patches | cannot apply | Git-generated non-empty patches |
| universal forbidden paths | false blockers | make them run parameters |
| unrelated dirty-tree hard stop | wasted cycles | block overlapping paths only |

## 10.1 V2 Drift Guards

| drift | symptom | guard |
|---|---|---|
| last_failure_tunnel_vision | prompt only prevents latest failure | include mission/payload coverage ledger |
| executor_guard_replaces_task | final output is only WRONG_EXECUTOR logic | executor gate is section 0, not mission |
| plan_reauthoring | assistant rewrites accepted plan from memory | read and obey source-plan manifest |
| same-file_patch_fragmentation | many patches touch same file and collide | one patch per repo target path |
| stale_patch_artifact_reuse | old failed patches copied as source | mark historical patches invalid unless source plan says otherwise |
| dirty_tree_overblocking | unrelated local files stop run | block only overlapping target/forbidden paths |

```okf
v2_pass_rule:
  PASS_requires:
    - executor gate passed or non-git mode explicitly authorized
    - all declared repair areas PASS or have explicit omitted reason
    - patch grouping follows one-patch-per-target-path rule
    - final state contains only allowed artifacts in builder mode
```

## 11. Minimal Final Report Schema

```yaml
FINAL_REPORT:
  verdict: PASS | PARTIAL | FAIL
  environment_mode: live_git_worktree | api_mirror | blocked
  files_read:
    count: 0
    files:
      - path: <path>
        status: read | partial | missing
        use: authority | evidence | example_only | anti_pattern
  outputs_created:
    - <path>
  source_index_created: true
  ranking_created: true
  prompt_template_created: true
  old_run_specific_details_removed: true
  validation:
    mechanical_validation: PASS | FAIL | NA
    anti_drift_check: PASS | FAIL
  coverage:
    declared_repair_areas:
      - <repair_area>
    covered_repair_areas:
      - <repair_area>
    omitted_repair_areas:
      - repair: <repair_area>
        reason: <reason>
  executor_gate:
    required: true|false
    result: PASS | WRONG_EXECUTOR | NA
  patch_grouping:
    rule: one_patch_per_repo_target_path
    exceptions:
      - target: <path>
        reason: <only_if_needed>
  persistence:
    committed: true
    sha: <sha-or-NA>
    pushed: true
  blockers: []
```

## 12. Source File Index

| file | source_type | value | durable_learning | run_specific_details_to_ignore | risk_if_overcopied | recommended_use | confidence |
|---|---|---|---|---|---|---|---|
| Pasted markdown.md | handover | current task contract | remove old run-specific defaults | none | n/a | core_authority | high |
| AgentModePatchGuide_v4.md | process_standard | Git-native builder doctrine | real worktree and git diff required for Git-native PASS | repo/branch/old patch roots/targets | specific Apex defaults leak | core_authority | high |
| AgentMode-GitNative-PatchPack-Process.okf.md | process_standard | machine-readable process | artifact-only builder state | Apex-specific paths | over-forces Git mode | core_authority | high |
| WorkingPromptExample.md | working_example | compact skeleton | copy structure, not values | patch filenames/features/targets | stale patch list | example_only | high |
| ChatHistory_ConstantFailurePrompts.md | failure_analysis | prompt drift evidence | avoid failure anthology | user frustration, old patches | defensive stale prompts | supporting_evidence | high |
| FailureAgentModeNew_ThinkingProcess.md | failure_analysis | absent repo and read-loop drift | environment gates must be real | old paths/line reads | API loops as baseline | anti_pattern | high |
| NoLocalGitWorktree.md | environment_mode_note | no-worktree/synthetic/API distinction | do not call synthetic repo Git-native | container paths/tmp repo | one runtime becomes universal | supporting_evidence | medium |
| GitAccessMistake.md | environment_mode_note | wrong Git assumptions | verify access surface | old failed commands | one failure becomes universal | supporting_evidence | medium |
| MirrorMode.md | environment_mode_note | API mirror distinction | mirror is conditional and weaker | old mirror paths | API mirror always valid/invalid | supporting_evidence | medium |
| IterativeProcess.md | process_standard | iteration discipline | gates over vibes | old cadence | too many loops | supporting_evidence | medium |
| MASTER_HANDOVER_learnings_and_rankings.md | handover | consolidated lessons | evidence map only | old ranks | stale priorities | supporting_evidence | medium |
| Create a learning for the failure modes. research.md | root_cause_research | failure classes | learn classes, not old fixes | old failure names | prompt bloat | supporting_evidence | medium |
| create a solid version with all the best pracitce.md | prompt_draft | draft guide | mine wording only | draft assumptions | contaminated draft | example_only | low |
| so teh checking or a live git work tree he does ev.md | environment_mode_note | live-worktree checks | distinguish real from fake worktree | typo title/old context | over-focus on one check | supporting_evidence | low |

```okf
source_index_map:
  core_authority: [Pasted markdown.md, AgentModePatchGuide_v4.md, AgentMode-GitNative-PatchPack-Process.okf.md]
  example_only: [WorkingPromptExample.md, create a solid version with all the best pracitce.md]
  anti_pattern: [FailureAgentModeNew_ThinkingProcess.md]
  supporting_evidence: [ChatHistory_ConstantFailurePrompts.md, NoLocalGitWorktree.md, GitAccessMistake.md, MirrorMode.md, IterativeProcess.md, MASTER_HANDOVER_learnings_and_rankings.md, Create a learning for the failure modes. research.md, so teh checking or a live git work tree he does ev.md]
```

## Anti-Drift Check

```yaml
anti_drift_check:
  no_old_batch_count_as_universal: PASS
  no_old_target_path_as_universal: PASS
  no_old_patch_file_list_as_universal: PASS
  no_old_environment_assumption_as_universal: PASS
  every_principle_labeled: PASS
  prompt_template_uses_placeholders: PASS
  executor_gate_does_not_replace_mission: PASS
  declared_repair_areas_have_coverage: PASS
  same_target_repairs_grouped: PASS
  old_failed_patch_artifacts_marked_invalid: PASS
  source_index_marks_examples_and_antipatterns: PASS
  result: PASS
```
