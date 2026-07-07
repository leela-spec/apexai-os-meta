---
okf_schema: "apex.agent_mode.git_native_patch_plan.v1"
plan_id: "2026-07-07-step1-prompt-blocker-cleanup"
status: "ready_for_agent_mode_patch_pack_builder"
repo: "leela-spec/apexai-os-meta"
branch: "main"
created_for: "APEX Step 1 prompt-blocker cleanup before operator-output Deep Research"
source_plan_inputs:
  - "Blockers.md"
  - "AgentMode-GitNative-PatchPack-Process.okf.md"
future_patch_pack_path: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/"
---

# APEX Step 1 Prompt-Blocker Cleanup — Patch-Pack Source Plan

```yaml
mission:
  create: "Git-native patch pack only"
  implementation_now: false
  pr_now: false
  final_builder_state: "patch artifacts only; target files reverted"
  purpose: >
    Fix prompt blockers that would confuse later Deep Research, patch planning,
    or operator-facing template design.

non_goals:
  - "Do not run APEX project work or any loop skill."
  - "Do not mutate project state, .claude/kb, calendars, runtime, cron, schedulers, or agents."
  - "Do not move or rename whole skill folders in this pass."
  - "Do not design the final operator-facing template family."
  - "Do not edit source-knowledge or ApexDefinition&OldVersions; read only if needed."
```

## 1. Authority Read Order

```yaml
read_first:
  - path: "AgentMode-GitNative-PatchPack-Process.okf.md"
    role: "Git-native patch-pack method"
  - path: "Blockers.md"
    role: "primary blocker register"
  - path: "apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md"
    role: "this execution plan"

read_live_targets_before_editing:
  - ".claude/Claude.md"
  - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
  - ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
  - ".claude/skills/PrecapWeek/package-manifest.md"
  - ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
  - ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
  - ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
  - ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
  - ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
  - ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
  - ".claude/skills/ProjectStatus/package-manifest.md"
  - ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
  - ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
  - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
  - ".claude/skills/status-merge/SKILL.md"
  - ".claude/skills/project-kb-manager/SKILL.md"
  - ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"

read_only_evidence_if_needed:
  - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/PrecapWeek/"
    use_for: "recovering missing PreCapWeek reference intent"
  - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/ProjectStatus/"
    use_for: "checking ProjectStatus path drift"
  - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/AIRouting/"
    use_for: "checking AIRouting path drift"
```

## 2. Discovery Instructions

```yaml
discovery:
  inventory_checks:
    - "List files under each targeted .claude/skills package."
    - "Confirm missing PreCapWeek references before creating them."
    - "Search target files for build residue, collapsed blocks, and path drift."
  search_terms:
    build_residue:
      - "NEXT PROMPT"
      - "VALIDATION"
      - "package_path_created"
      - "package_manifest_created"
      - "files_created"
      - "build-stage"
    collapsed_blocks:
      - "core_loop:  1:"
      - "operator_gates:  G1:"
      - "artifact_paths:  apex_project_status:"
      - "skill_contract:  skill_name:"
      - "supporting_files:  - path:"
    path_drift:
      - ".claude/skills/precap-week"
      - ".claude/skills/project-status-overview"
      - ".claude/skills/ai-routing-and-usage-tracking"
      - ".claude/skills/prompt-engineering"
      - ".claude/skills/workflow-process-design"
    output_design:
      - "result card"
      - "success card"
      - "Operator Review First"
      - "Route Reuse / Avoid Signal"
```

## 3. Future Patch-Pack Rules

```yaml
patch_pack_rules:
  one_patch_per_target_file: true
  use_git_diff_only: true
  no_handwritten_hunks: true
  validate_each_patch_with_git_apply_check: true
  cumulative_validation_required: true
  target_files_reverted_after_patch_generation: true
  final_builder_state: "only patch-pack artifacts changed"
  allowed_outputs:
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-*.patch"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-apply-patches.md"
  forbidden_live_edit_paths:
    - "state/"
    - ".claude/kb/"
    - "source-knowledge/"
    - "ApexDefinition&OldVersions/"
    - ".github/workflows/"
    - "scripts/"
```

## 4. Target File and Patch Map

```yaml
target_files:
  - id: "001"
    blockers: [PB001, PB004]
    target: ".claude/Claude.md"
    patch: "001-root-claude-loop-source-authority.patch"
    change_type: "modify"
  - id: "002"
    blockers: [PB002]
    target: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    patch: "002-precap-next-day-entrypoint-unfence.patch"
    change_type: "modify"
  - id: "003"
    blockers: [PB003, PB004]
    target: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    patch: "003-precap-week-entrypoint-readable.patch"
    change_type: "modify"
  - id: "004"
    blockers: [PB001, PB003]
    target: ".claude/skills/PrecapWeek/package-manifest.md"
    patch: "004-precap-week-manifest-actual-paths.patch"
    change_type: "modify"
  - id: "005"
    blockers: [PB003]
    target: ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md"
    patch: "005-precap-week-calendar-guidance.patch"
    change_type: "create_if_missing"
  - id: "006"
    blockers: [PB003]
    target: ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md"
    patch: "006-precap-week-output-contract.patch"
    change_type: "create_if_missing"
  - id: "007"
    blockers: [PB003]
    target: ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md"
    patch: "007-precap-week-blueprint-standard.patch"
    change_type: "create_if_missing"
  - id: "008"
    blockers: [PB003]
    target: ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md"
    patch: "008-precap-week-meeting-example.patch"
    change_type: "create_if_missing"
  - id: "009"
    blockers: [PB003]
    target: ".claude/skills/PrecapWeek/references/validation-checklist.md"
    patch: "009-precap-week-validation-checklist.patch"
    change_type: "create_if_missing"
  - id: "010"
    blockers: [PB001]
    target: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
    patch: "010-precap-next-day-path-policy.patch"
    change_type: "modify"
  - id: "011"
    blockers: [PB006]
    target: ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
    patch: "011-operator-output-design-result-card-policy.patch"
    change_type: "modify"
  - id: "012"
    blockers: [PB006]
    target: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
    patch: "012-next-day-plan-result-card.patch"
    change_type: "modify"
  - id: "013"
    blockers: [PB008]
    target: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
    patch: "013-prompt-engineering-path-bridge.patch"
    change_type: "modify"
  - id: "014"
    blockers: [PB008]
    target: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
    patch: "014-usage-tracking-path-bridge.patch"
    change_type: "modify"
  - id: "015"
    blockers: [PB008]
    target: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
    patch: "015-workflow-process-path-bridge.patch"
    change_type: "modify"
  - id: "016"
    blockers: [PB001]
    target: ".claude/skills/ProjectStatus/package-manifest.md"
    patch: "016-projectstatus-manifest-actual-paths.patch"
    change_type: "modify"
  - id: "017"
    blockers: [PB001, PB005]
    target: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
    patch: "017-airouting-entrypoint-residue-removal.patch"
    change_type: "modify"
  - id: "018"
    blockers: [PB001, PB005]
    target: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
    patch: "018-airouting-manifest-residue-and-paths.patch"
    change_type: "modify"
  - id: "019"
    blockers: [PB005]
    target: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    patch: "019-raw-flow-run-completion-gate.patch"
    change_type: "modify"
  - id: "020"
    blockers: [PB005]
    target: ".claude/skills/status-merge/SKILL.md"
    patch: "020-status-merge-run-completion-gate.patch"
    change_type: "modify"
  - id: "021"
    blockers: [PB007]
    target: ".claude/skills/project-kb-manager/SKILL.md"
    patch: "021-project-kb-manager-state-handoff-exposure.patch"
    change_type: "modify"
  - id: "022"
    blockers: [PB009]
    target: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    patch: "022-model-usage-learning-card.patch"
    change_type: "modify"
```

## 5. Improvement Matrix

```yaml
improvement_matrix:
  B1_root_loop_and_source_authority:
    patch_ids: ["001"]
    desired_state:
      - "core_loop, operator_gates, artifact_paths are readable YAML blocks"
      - "root path_policy distinguishes actual_live_path from canonical_target_path"
      - "actual live paths remain authoritative until normalization pass"
    forbidden:
      - "folder moves"
      - "canonical target paths presented as live"

  B2_PreCapWeek_handoff_integrity:
    patch_ids: ["003", "004", "005", "006", "007", "008", "009"]
    desired_state:
      - "PreCapWeek entrypoint readable, not one-line YAML-like blocks"
      - "supporting files listed by entrypoint actually exist"
      - "weekly-to-daily first_precap_next_day_seed is inspectable"
    evidence_sources:
      - "live PreCapWeek skill and manifest"
      - "old PreCapWeek final files, read-only, only if useful"
    forbidden:
      - "next_day_plan schema in PreCapWeek"
      - "prompt packet generation"
      - "calendar event creation"

  B3_manifest_and_dependency_path_alignment:
    patch_ids: ["010", "013", "014", "015", "016", "018"]
    desired_state:
      - "manifests and dependency contracts expose actual_live_path and canonical_target_path"
      - "path_resolution_policy says use actual_live_path until package-normalization pass"
    forbidden:
      - "repo-wide renames"
      - "schema rewrites"

  B4_remove_build_residue:
    patch_ids: ["017", "018", "019", "020"]
    desired_state:
      - "no NEXT PROMPT in live AIRouting files"
      - "no package-build completion gates in raw-flow or status-merge SKILL entrypoints"
      - "completion gates validate invocation outputs"
    forbidden:
      - "removing real boundary checks"

  B5_output_success_signal_placeholders:
    patch_ids: ["011", "012", "022"]
    desired_state:
      - "minimal result card policy exists"
      - "next-day plan template has Result Card before tables"
      - "model usage template has Operator Learning Card before detailed usage fields"
    forbidden:
      - "final UI/template-family design"
      - "removing machine-readable YAML"

  B6_state_handoff_visibility:
    patch_ids: ["021"]
    desired_state:
      - "project-kb-manager SKILL exposes apex_orchestration_state_packet support files"
      - "handoff mode is visible without replacing query/update/intake"
    forbidden:
      - "project KB schema replacement"
      - "direct PreCapWeek or PreCapNextDay execution"
```

## 6. Required and Forbidden Markers

```yaml
marker_matrix:
  ".claude/Claude.md":
    required: ["path_policy:", "actual_live_path", "canonical_target_path", "core_loop:", "operator_gates:", "artifact_paths:"]
    forbidden: ["core_loop:  1:", "operator_gates:  G1:", "artifact_paths:  apex_project_status:"]

  ".claude/skills/PrecapNextDay/Skill_precap-next-day.md":
    required: ["---\nname: precap-next-day", "## Skill Contract", "## Completion Gate"]
    forbidden: ["```markdown", "```markdown id="]

  ".claude/skills/PrecapWeek/Skill_Precap-Week.md":
    required: ["skill_contract:", "supporting_files:", "failure_modes:", "completion_gate:", "first_precap_next_day_seed"]
    forbidden: ["skill_contract:  skill_name:", "supporting_files:  - path:", "completion_gate:  target_path_valid:"]

  ".claude/skills/PrecapWeek/package-manifest.md":
    required: ["package_path_actual: .claude/skills/PrecapWeek/", "entrypoint_file_actual: Skill_Precap-Week.md", "normalization_status: pending"]
    forbidden: ["package_path: .claude/skills/precap-week/"]

  ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md":
    required: ["# Calendar Planning Guidance", "calendar_behavior:", "create_calendar_events: false", "calendar_block_proposals_only: true"]
    forbidden: ["create_calendar_events: true"]

  ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md":
    required: ["# Weekly Plan Output Contract", "precap_week_output", "first_precap_next_day_seed", "operator_validation"]
    forbidden: ["flow_prompt_pack:"]

  ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md":
    required: ["# Weekly Blueprint Standard", "Monday_to_Friday", "Sunday_weekly_precap_session"]
    forbidden: ["Saturday_regular_planning", "Sunday_regular_day_planning"]

  ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md":
    required: ["# Weekly Blueprint Meeting Example", "meeting_week_deformation_rules", "partial_flow_rules"]
    forbidden: ["calendar_event_creation"]

  ".claude/skills/PrecapWeek/references/validation-checklist.md":
    required: ["# Validation Checklist", "validation_checks:", "operator_review_flags:", "missing_input_behavior:"]
    forbidden: ["NEXT PROMPT", "package_path_created"]

  ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md":
    required: ["package_path_actual: \".claude/skills/PrecapNextDay/\"", "package_path_canonical_target: \".claude/skills/precap-next-day/\"", "normalization_status: pending", "actual_path_is_authoritative_until_normalization: true"]
    forbidden: []

  ".claude/skills/PrecapNextDay/references/operator-output-format-design.md":
    required: ["result_card_policy:", "tables_are_secondary_detail_views", "operator_value_signal_first"]
    forbidden: []

  ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md":
    required: ["## 2. Result Card", "operator_value_signal", "what_changed_for_operator", "next_action_for_operator"]
    forbidden: []

  ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md":
    required: ["path_resolution_policy:", "actual_live_path: \".claude/skills/PromptEngineer/SKILL_prompt-engineering.md\"", "canonical_target_path: \".claude/skills/prompt-engineering/\""]
    forbidden: []

  ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md":
    required: ["path_resolution_policy:", "actual_live_path: \".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md\"", "canonical_target_path: \".claude/skills/ai-routing-and-usage-tracking/\""]
    forbidden: []

  ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md":
    required: ["path_resolution_policy:", "actual_live_path: \".claude/skills/Workflow&Processes/workflow-process-design-SKILL.md\"", "canonical_target_path: \".claude/skills/workflow-process-design/\""]
    forbidden: []

  ".claude/skills/ProjectStatus/package-manifest.md":
    required: ["package_path_actual: \".claude/skills/ProjectStatus/\"", "entrypoint_file_actual: \"project-status-overview_SKILL_v3.md\"", "normalization_status: pending"]
    forbidden: ["path: \".claude/skills/project-status-overview/SKILL.md\""]

  ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md":
    required: ["## Completion Gate", "routing_decision_present: true"]
    forbidden: ["# VALIDATION", "# NEXT PROMPT", "Paste this next"]

  ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md":
    required: ["package_path_actual: \".claude/skills/AIRouting/\"", "entrypoint_file_actual: \"ai-routing-and-usage-tracking-SKILL.md\"", "normalization_status: pending"]
    forbidden: ["```markdown id=", "# NEXT PROMPT", "Paste this next"]

  ".claude/skills/raw-flow-dump-normalize/SKILL.md":
    required: ["raw_flow_dump_output_completion_gate:", "normalized_raw_flow_dump_or_skipped_flow_marker_present: true", "no_FlowRecap_or_status_merge_output_created: true"]
    forbidden: ["package_path_created: true", "raw_flow_dump_contract_created: true", "manifest_created: true", "SKILL_md_created_with_valid_frontmatter: true"]

  ".claude/skills/status-merge/SKILL.md":
    required: ["status_merge_output_completion_gate:", "status_merge_packet_present: true", "next_PreCapNextDay_input_context_is_seed_only: true"]
    forbidden: ["package_path_created: true", "template_created: true", "manifest_created: true", "SKILL_md_created_with_valid_frontmatter: true"]

  ".claude/skills/project-kb-manager/SKILL.md":
    required: ["handoff_mode", "references/apex-orchestration-state-packet-contract.md", "templates/apex-orchestration-state-packet-template.md", "apex_orchestration_state_packet"]
    forbidden: []

  ".claude/skills/model-usage-log/templates/model-usage-delta-template.md":
    required: ["## 2. Operator Learning Card", "operator_learning_card:", "route_reuse_or_avoid_signal", "next_PreCapNextDay_hint"]
    forbidden: []
```

## 7. Future Patch Manifest Requirements

```yaml
patch_manifest_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/000-patch-manifest.md"
include:
  - "repo, branch, timestamp"
  - "source plan path"
  - "Blockers.md read status"
  - "AgentMode Git-native guide read status"
  - "patch order"
  - "target-to-patch map"
  - "per-patch git apply --check result"
  - "cumulative validation result"
  - "changed-file scope result"
  - "required and forbidden marker check result"
  - "dirty-state notes"

apply_handoff_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/999-apply-patches.md"
include:
  - "start from clean main"
  - "apply-check each patch before apply"
  - "apply patches in numeric order"
  - "verify changed-file scope"
  - "verify markers"
  - "commit implementation changes separately"
```

## 8. Done Criteria

```yaml
done_when:
  - "all listed patch artifacts are created"
  - "each patch touches exactly one target file"
  - "each patch is generated from git diff"
  - "each patch passes git apply --check"
  - "cumulative apply passes"
  - "changed file scope equals target_files exactly"
  - "required markers are present"
  - "forbidden markers are absent"
  - "target files are reverted in builder final state"
  - "000-patch-manifest.md and 999-apply-patches.md exist and are complete"

not_done_if:
  - "any target file remains directly modified in builder final state"
  - "any old-version/source-knowledge file is modified"
  - "any runtime/state/calendar/project execution behavior is introduced"
  - "any patch is hand-written instead of git diff generated"
```
