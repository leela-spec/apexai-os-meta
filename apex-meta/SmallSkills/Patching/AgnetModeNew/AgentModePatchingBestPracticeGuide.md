# Agent Mode Patching Best-Practice Guide

```okf
okf_document:
  id: agent_mode_patching_best_practice_guide_v1
  title: Agent Mode Patching Best-Practice Guide
  status: neutral_general_process_standard
  purpose: >
    General reusable guide for Agent Mode, patch-pack, and repo-edit workflows.
    Historical runs are evidence only. They are not defaults.
```

## 1. Executive Verdict

```okf
executive_verdict:
  root_issue: run_specific_instruction_contamination
  definition: >
    Concrete details from one patching run were promoted into global process
    doctrine: old patch counts, target maps, repo-access assumptions, validation
    commands, and marker strings.
  durable_fix: >
    Separate invariant principles, environment modes, run parameters, and
    historical examples in every guide, handover, and reusable prompt.
  pass_condition: >
    A patching workflow can only pass when it reports its environment mode,
    source-access evidence, output artifacts, mechanical validation, persistence
    state, and limitations.
```

## 2. Core Distinction: Invariants vs Environment Modes vs Run Parameters

| class | definition | examples | prompt handling | contamination risk |
|---|---|---|---|---|
| `invariant_principle` | Always true across patching workflows. | no fabricated files; mechanical validation; honest final report | copy unchanged | vague PASS, pseudo-artifacts |
| `environment_mode` | Depends on available execution surface. | `live_git_worktree`, `api_mirror`, `blocked` | detect or declare | API snapshots mislabeled as Git-native |
| `run_parameter` | Must be rewritten per run. | repo, branch, patch root, source plan, target files, validation commands | fill fresh | stale patch counts and targets |
| `historical_example` | Evidence from a prior run. | working prompt, failed transcript, old patch pack | mark example-only or anti-pattern | old repair wave becomes doctrine |

```okf
separation_policy:
  invariant_principles:
    - anti_fabrication
    - source_access_verification
    - mechanical_validation
    - scope_control
    - honest_final_report
  environment_modes:
    - live_git_worktree
    - api_mirror
    - blocked
  run_parameters:
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
  historical_examples:
    allowed_use:
      - evidence
      - example_only
      - anti_pattern
    forbidden_use:
      - default patch count
      - default target file list
      - default environment assumption
```

## 3. Ranked Principles and Checks

| rank | principle | category | why_it_matters | failure_prevented | invariant_or_mode_specific | simple_rule | machine_check | evidence_files | risk_if_overapplied |
|---:|---|---|---|---|---|---|---|---|---|
| 1 | Do not fabricate placeholders. | anti_fabrication | Fake artifacts create false progress. | empty patches, pseudo-files, invented baselines | invariant | no placeholder implementation artifacts | `test -s`, reject TODO-only outputs | `AgentModePatchGuide_v4.md`, `NoLocalGitWorktree.md` | allow placeholders only in templates |
| 2 | Do not trust unverified large-file or connector reads. | source_access | Snippets can omit baseline context. | bad diffs, stale baselines | invariant | full file or explicit partial ledger | read ledger with method and range | `FailureAgentModeNew_ThinkingProcess.md`, `NoLocalGitWorktree.md` | can over-block authorized API mirror mode |
| 3 | Separate invariants from run parameters. | prompt_design | Prevents old run details becoming doctrine. | stale patch counts and targets | invariant | global guide contains no old task defaults | scan for fixed counts/old roots outside examples | `ChatHistory_ConstantFailurePrompts.md` | too abstract if placeholders are not filled |
| 4 | Make environment mode explicit. | environment_mode | Same commands mean different things by surface. | false Git-native success | mode_specific | declare one mode before work | final report `environment_mode` | `AgentModePatchGuide_v4.md` | overlong mode taxonomies distract workers |
| 5 | Validate mechanically, not rhetorically. | validation | Confidence is not evidence. | invalid hunks, marker-only success | invariant | require command output or explicit NA | `git apply --check`, compile, smoke tests | `AgentModePatchGuide_v4.md` | marker checks alone are insufficient |
| 6 | Use live worktree only for Git-native patch claims. | patch_integrity | Synthetic repos validate fake baselines. | fake Git-native patches | mode_specific | no worktree, no Git-native PASS | `git rev-parse`, `git remote get-url origin` | `NoLocalGitWorktree.md` | API mirror may still be useful if labeled |
| 7 | API mirror mode requires explicit authorization. | environment_mode | Connector fetches can help but are weaker. | silent baseline reconstruction | mode_specific | use only when operator authorizes | report stale-baseline warning | `MirrorMode.md`, `NoLocalGitWorktree.md` | may be too conservative for docs-only writes |
| 8 | Source access is a hard gate. | source_access | Missing sources make synthesis unreliable. | invented source index | invariant | stop or mark missing | missing-file ledger | current handover | can block useful partial output; label partial honestly |
| 9 | One patch per target file for patch packs. | patch_integrity | Easier validation and rollback. | multi-file hunk confusion | mode_specific | 1 target file per patch unless exception declared | count `diff --git` headers | `AgentModePatchGuide_v4.md` | some script files may need multiple feature patches |
| 10 | Builder final state must leave targets clean. | artifact_delivery | Patch-pack builder is not final applier. | direct mutation in builder run | mode_specific | commit/export artifacts only | `git status --porcelain -- <targets>` | `AgentModePatchGuide_v4.md` | not applicable to direct-edit mode |
| 11 | Dirty-tree policy must be scoped. | scope_control | Unrelated dirty files should not block safe work. | unnecessary blockers or overwrites | invariant | block only overlapping dirty paths | path overlap check | execution audits | too lax if generated outputs overlap |
| 12 | Behavior checks outrank marker checks. | validation | Strings can hide stubs. | stub-only implementation | invariant | scripts require compile/smoke tests | `py_compile`, help, sample command | failure audits | docs-only changes may not need behavior tests |
| 13 | Prompt should be execution contract, not failure anthology. | prompt_design | Failure history contaminates execution. | defensive, stale prompts | invariant | mission/source/scope/method/validation/report | prompt lint | `ChatHistory_ConstantFailurePrompts.md` | remove only history, not constraints |
| 14 | Historical examples are examples only. | handover_design | Working prompts include task specifics. | copied old patch lists | example_only | copy skeleton, not values | source index recommended_use | `WorkingPromptExample.md` | do not ignore proven structure |
| 15 | Persistence claims require evidence. | artifact_delivery | local/export/commit/push are distinct. | claiming pushed state falsely | invariant | cite SHA or archive path | commit SHA, pushed flag, archive path | process guide | verbose reports; keep schema compact |
| 16 | Forbidden paths are run parameters. | scope_control | Blast radius differs by task. | universal false blockers | run_parameter | fill fresh per task | changed-file scope check | current handover | some project-wide forbiddens may remain policy |
| 17 | Validation commands are run parameters. | validation | Old commands may not apply. | irrelevant validation | run_parameter | require task-specific commands | `<VALIDATION_COMMANDS>` populated | current handover | keep generic access checks |
| 18 | Report partial completion honestly. | artifact_delivery | Useful partial work must not become PASS. | hidden failures | invariant | PASS only when all gates pass | verdict plus blockers | process guide | avoid normalizing incomplete work |

## 4. Environment Mode Matrix

| mode | meaning | allowed | forbidden | required warnings/reporting |
|---|---|---|---|---|
| `live_git_worktree` | Agent has a real checked-out repo and can run Git against it. | `git diff` patches; `git apply --check`; cumulative validation; commit patch artifacts | API snippet baseline reconstruction; synthetic `git init` repo | repo root, branch, remote, dirty-tree state, validation results, commit SHA |
| `api_mirror` | Agent lacks live worktree but can fetch reliable full files through connector/API. | only if explicitly authorized: mirror from full files; archive/export draft artifacts; connector-written docs | claiming Git-native success; claiming pushed state unless connector write actually committed | stale-baseline warning; live repo revalidation required |
| `blocked` | Neither live worktree nor reliable source access exists. | stop and report access failure | patch generation; invented file contents; placeholder artifacts | missing files and action needed |

## 5. Source Access and Read Verification

```okf
read_verification:
  required_fields:
    - path
    - access_method
    - read_status
    - full_file_or_line_range
    - relevance
    - limitation
  rules:
    - search snippets are not full-file proof
    - connector metadata is not freshness proof
    - old source lists are not current repo state
    - missing sources must be explicit
```

## 6. Patch Generation and Validation

```okf
patch_generation:
  live_git_worktree:
    required:
      - read source plan
      - read current target files
      - modify one target file at a time
      - generate patch with git diff
      - verify non-empty patch when change expected
      - run git apply --check per patch
      - run cumulative git apply --check
      - run compile/smoke tests for code changes
      - revert target files in builder mode
    forbidden:
      - hand-written hunk headers
      - synthetic repo baselines
      - snippet-assembled patches
      - PASS_WITH_WORKAROUNDS when git apply fails
  api_mirror:
    required:
      - explicit authorization
      - full-file fetch verification
      - stale-baseline warning
      - no Git-native success claim
```

## 7. Anti-Fabrication and Partial Completion Rules

```okf
anti_fabrication:
  fail_if:
    - source plan unreadable and no authorized fallback
    - target file missing and patch depends on it
    - patch is empty but reported as implementation
    - final report claims push without commit evidence
  partial_if:
    - valid artifacts created but not persisted
    - API mirror artifacts need live validation
    - some sources are missing but ledger is explicit
  pass_only_if:
    - claimed mode gates passed
    - requested outputs exist
    - source index/ranking/template exist when required
    - old run-specific details are not defaults
```

## 8. Artifact Packaging and Delivery

```okf
artifact_delivery:
  patch_pack_builder:
    outputs:
      - manifest
      - patch files
      - validation report
      - apply handoff
    final_state:
      target_files_modified: false
      artifacts_persisted: true
  direct_repo_edit:
    outputs:
      - changed target files
      - validation report
      - commit SHA
  documentation_output:
    outputs:
      - guide
      - template
      - source index
      - final report
```

## 9. Prompt Design Rules

```okf
prompt_design:
  include:
    - role
    - mission
    - environment_mode_selection
    - invariant_rules
    - run_parameters
    - source_access_gate
    - target_scope
    - required_changes
    - validation_commands
    - output_artifacts
    - final_report_schema
  exclude:
    - old failure transcripts
    - old patch counts
    - old target maps as defaults
    - architecture rediscovery
    - fallback maze
    - speculative blockers
```

## 10. Common Anti-Patterns

| anti_pattern | why_bad | correction |
|---|---|---|
| Run-specific instruction contamination | Converts one repair wave into false doctrine. | Label every item as invariant, mode-specific, run parameter, or example. |
| Synthetic repo as live Git | Validates a fake baseline. | Claim Git-native only with real worktree. |
| Connector snippet baseline | Snippets are partial. | Use full-file fetch or stop. |
| Prompt as failure anthology | Causes stale defensive behavior. | Use compact execution contract. |
| Marker-only validation | Stubs pass string checks. | Add compile/smoke tests. |
| Placeholder patches | Looks complete, cannot apply. | Require non-empty Git-generated patch. |
| Universal forbidden paths | Blocks valid future workflows. | Make forbidden paths run parameters. |
| Unrelated dirty-tree hard stop | Wastes execution cycles. | Stop only on overlapping dirty paths. |

## 11. Minimal Final Report Schema

```yaml
FINAL_REPORT:
  verdict: "PASS | PARTIAL | FAIL"
  environment_mode: "live_git_worktree | api_mirror | blocked"
  files_read:
    count: 0
    files:
      - path: "<path>"
        status: "read | partial | missing"
        use: "authority | evidence | example_only | anti_pattern"
  outputs_created:
    - "<path>"
  source_index_created: true
  ranking_created: true
  prompt_template_created: true
  old_run_specific_details_removed: true
  validation:
    mechanical_validation: "PASS | FAIL | NA"
    anti_drift_check: "PASS | FAIL"
  persistence:
    committed: true
    sha: "<sha-or-NA>"
    pushed: true
  blockers: []
```

## 12. Source File Index

| file | source_type | value | durable_learning | run_specific_details_to_ignore | risk_if_overcopied | recommended_use | confidence |
|---|---|---|---|---|---|---|---|
| `Pasted markdown.md` | handover | Current task contract. | Remove old run-specific defaults. | None; current instruction source. | N/A | core_authority | high |
| `AgentModePatchGuide_v4.md` | process_standard | Defines Git-native builder contract and role split. | Git-native claims require real worktree and Git-generated patches. | repo names, branch names, old patch roots, old target sets | turns specific Apex patch process into universal defaults | core_authority | high |
| `AgentMode-GitNative-PatchPack-Process.okf.md` | process_standard | Machine-readable process doctrine. | Artifact-only builder state; final applier separate. | Apex-specific paths | over-forces Git-native mode where API mirror is authorized | core_authority | high |
| `WorkingPromptExample.md` | working_example | Compact positive execution skeleton. | Copy structure, not values. | patch filenames, feature names, target files | stale patch counts leak into new prompts | example_only | high |
| `ChatHistory_ConstantFailurePrompts.md` | failure_analysis | Shows prompt drift into failure-prevention sprawl. | Do not include long failure history in execution prompts. | user frustration text, old patch lists | makes future prompts defensive and stale | supporting_evidence | high |
| `FailureAgentModeNew_ThinkingProcess.md` | failure_analysis | Shows absent live repo preflight and segmented read drift. | Environment gates must be real. | old repo paths and line-read loops | normalizes API read loops as patch baselines | anti_pattern | high |
| `NoLocalGitWorktree.md` | environment_mode_note | Distinguishes no live repo, synthetic repo, and API mirror. | Do not label synthetic repo as Git-native. | container paths, expired URLs, tmp repo names | overgeneralizes one runtime into all Agent Mode runtimes | supporting_evidence | medium |
| `GitAccessMistake.md` | environment_mode_note | Documents wrong Git-access assumptions. | Verify access surface before execution. | specific failed commands | makes one access failure universal | supporting_evidence | medium |
| `MirrorMode.md` | environment_mode_note | Documents API/mirror mode. | Mirror mode is conditional and weaker than live Git. | old mirror paths | treats API mirror as always valid or always invalid | supporting_evidence | medium |
| `IterativeProcess.md` | process_standard | Iteration discipline. | Iterate through gates, not vibes. | old cadence | too many unnecessary loops | supporting_evidence | medium |
| `MASTER_HANDOVER_learnings_and_rankings.md` | handover | Consolidated lessons and rankings. | Evidence map, not execution prompt. | old ranks tied to incident | imports stale priorities | supporting_evidence | medium |
| `Create a learning for the failure modes. research.md` | root_cause_research | Root-cause evidence. | Learn failure classes, not old fixes. | old failure names | converts history into prompt bloat | supporting_evidence | medium |
| `create a solid version with all the best pracitce.md` | prompt_draft | Draft guide/prompt. | Mine wording only. | draft assumptions | contaminated draft supersedes neutral guide | example_only | low |
| `so teh checking or a live git work tree he does ev.md` | environment_mode_note | Live-worktree check discussion. | Preflight must distinguish real worktree from fake git repo. | typo title and old run context | over-focuses on one check | supporting_evidence | low |

```okf
source_index_map:
  core_authority:
    - Pasted markdown.md
    - AgentModePatchGuide_v4.md
    - AgentMode-GitNative-PatchPack-Process.okf.md
  example_only:
    - WorkingPromptExample.md
    - create a solid version with all the best pracitce.md
  anti_pattern:
    - FailureAgentModeNew_ThinkingProcess.md
  supporting_evidence:
    - ChatHistory_ConstantFailurePrompts.md
    - NoLocalGitWorktree.md
    - GitAccessMistake.md
    - MirrorMode.md
    - IterativeProcess.md
    - MASTER_HANDOVER_learnings_and_rankings.md
    - Create a learning for the failure modes. research.md
    - so teh checking or a live git work tree he does ev.md
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
  source_index_marks_examples_and_antipatterns: PASS
  result: PASS
```
