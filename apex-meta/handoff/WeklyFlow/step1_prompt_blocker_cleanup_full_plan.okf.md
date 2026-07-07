---
okf_schema: "apex.agent_mode.git_native_patch_plan.v1"
plan_id: "2026-07-07-step1-prompt-blocker-cleanup-full"
status: "ready_for_agent_mode_patch_pack_builder"
created_for: "APEX Step 1 prompt-blocker cleanup before operator-output Deep Research"
repo: "leela-spec/apexai-os-meta"
branch: "main"
source_of_truth: "live terminal Git repository"
primary_blocker_source: "Blockers.md"
process_guide: "AgentMode-GitNative-PatchPack-Process.okf.md"
future_patch_pack_path: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/"
plan_update_policy: "This file is the authoritative semantic source plan for the later Agent Mode patch-pack builder."
---

# APEX Step 1 Prompt-Blocker Cleanup — Full Git-Native Patch-Pack Source Plan

## 0. Purpose

```yaml
purpose:
  one_line: >
    Provide the later Agent Mode run with a full, machine-readable, source-grounded
    plan for creating validated Git-native patch artifacts for all identified
    Step 1 prompt blockers.
  why_this_exists: >
    The later Deep Research run for operator-facing output design must not inspect
    stale path maps, fenced skill entrypoints, missing support files, build residue,
    or table-first templates as if they were stable architecture.
  expected_use: >
    Agent Mode reads this plan first, reads Blockers.md and the Git-native patch
    guide, inspects the live repo, then creates one Git-generated patch per target
    file plus a patch manifest and apply handoff.
```

---

## 1. Mission Contract

```yaml
mission_contract:
  mission: "Create a validated Git-native patch pack."
  output_type: "patch artifacts only"
  implementation_commit_now: false
  create_pull_request_now: false
  final_builder_repo_state:
    target_files_modified: false
    patch_pack_artifacts_present: true
    only_patch_pack_artifacts_changed: true
  patch_generation_rule: "Use git diff from live repo modifications; do not hand-write hunks."
  patch_scope_rule: "Exactly one patch per target file."
  validation_rule: "Every patch and the cumulative patch sequence must pass git apply --check."

strict_non_goals:
  - "Do not run PreCapWeek."
  - "Do not run PreCapNextDay."
  - "Do not run FlowRecap."
  - "Do not run raw-flow-dump-normalize."
  - "Do not run model-usage-log."
  - "Do not run status-merge."
  - "Do not run APEX project work."
  - "Do not merge canonical project status."
  - "Do not mutate durable project state."
  - "Do not edit .claude/kb data."
  - "Do not create calendar events."
  - "Do not create runtime automation, cron jobs, schedulers, or agents."
  - "Do not redesign the final operator-facing output template family."
  - "Do not normalize repository casing by moving folders in this pass."
  - "Do not patch source-knowledge or ApexDefinition&OldVersions."
```

---

## 2. Required Read Order

```yaml
read_order:
  phase_0_process_authority:
    - path: "AgentMode-GitNative-PatchPack-Process.okf.md"
      role: >
        Defines the process doctrine: source-grounded semantic plan, exact target
        files, one Git-generated patch per target file, git apply --check,
        cumulative validation, and artifact-only final state.
      required: true

  phase_1_blocker_authority:
    - path: "Blockers.md"
      role: >
        Primary blocker register. Contains executive verdict, source inventory,
        PB001-PB009 blocker definitions, fix-first batches B1-B6, Deep Research
        readiness checklist, and patch protocol note.
      required: true

  phase_2_this_plan:
    - path: "apex-meta/patch-plans/2026-07-07-step1-prompt-blocker-cleanup-plan.okf.md"
      role: "This machine-readable full source plan."
      required: true

  phase_3_live_source_files:
    root:
      - ".claude/Claude.md"
    skill_entrypoints_and_manifests:
      - ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
      - ".claude/skills/PrecapWeek/package-manifest.md"
      - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
      - ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
      - ".claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md"
      - ".claude/skills/ProjectStatus/package-manifest.md"
      - ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
      - ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      - ".claude/skills/project-kb-manager/SKILL.md"
      - ".claude/skills/project-kb-manager/package-manifest.md"
      - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
      - ".claude/skills/flow-recap/SKILL.md"
      - ".claude/skills/model-usage-log/SKILL.md"
      - ".claude/skills/status-merge/SKILL.md"
    operator_templates_and_dependency_contracts:
      - ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
      - ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
      - ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
      - ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
      - ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
      - ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    state_handoff_sources:
      - ".claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md"
      - ".claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md"

  phase_4_read_only_recovery_sources:
    use_only_if_live_reference_is_missing_or_ambiguous:
      - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/PrecapWeek/"
        role: "Recover intent for missing PreCapWeek references."
      - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/ProjectStatus/"
        role: "Verify old/current ProjectStatus path drift."
      - path: "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/AIRouting/"
        role: "Verify old/current AIRouting path drift."
    rule: "Read-only evidence only. Do not patch these paths."
```

---

## 3. Evidence-Discovery Plan

```yaml
evidence_discovery:
  preflight_commands:
    - command: "git rev-parse --show-toplevel"
      purpose: "Confirm repo root."
    - command: "git rev-parse --is-inside-work-tree"
      purpose: "Confirm Git worktree."
    - command: "git remote get-url origin"
      purpose: "Confirm remote repository identity."
    - command: "git fetch origin main"
      purpose: "Ensure main is current."
    - command: "git checkout main"
      purpose: "Use requested branch."
    - command: "git pull --ff-only origin main"
      purpose: "Start from current main."
    - command: "git branch --show-current"
      purpose: "Confirm branch."
    - command: "git status --porcelain"
      purpose: "Record dirty state before building patch pack."

  inventory_checks:
    - command: "git ls-files '.claude/skills/PrecapWeek/**'"
      purpose: "Confirm actual PreCapWeek files and missing references."
    - command: "git ls-files '.claude/skills/PrecapNextDay/**'"
      purpose: "Confirm PreCapNextDay entrypoint, references, templates."
    - command: "git ls-files '.claude/skills/ProjectStatus/**'"
      purpose: "Confirm ProjectStatus actual files and old FirstIteration layout."
    - command: "git ls-files '.claude/skills/AIRouting/**'"
      purpose: "Confirm AIRouting actual files and reference placement."
    - command: "git ls-files '.claude/skills/project-kb-manager/**'"
      purpose: "Confirm state packet contract/template exists."
    - command: "git ls-files '.claude/skills/raw-flow-dump-normalize/**'"
      purpose: "Confirm raw-flow files."
    - command: "git ls-files '.claude/skills/status-merge/**'"
      purpose: "Confirm status-merge files."
    - command: "git ls-files '.claude/skills/model-usage-log/**'"
      purpose: "Confirm model-usage files."

  high_evidence_searches:
    build_residue:
      patterns:
        - "NEXT PROMPT"
        - "VALIDATION"
        - "package_path_created"
        - "package_manifest_created"
        - "files_created"
        - "SKILL_md_created_with_valid_frontmatter"
        - "template_created"
        - "manifest_created"
      search_scope:
        - ".claude/skills/AIRouting"
        - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
        - ".claude/skills/status-merge/SKILL.md"
        - ".claude/skills/flow-recap"
      action_rule: >
        Remove build residue from live invocation files. In manifests, preserve
        package-build metadata only if clearly labeled as historical/build status,
        not invocation completion criteria.

    collapsed_or_fenced_blocks:
      patterns:
        - "core_loop:  1:"
        - "operator_gates:  G1:"
        - "artifact_paths:  apex_project_status:"
        - "skill_contract:  skill_name:"
        - "supporting_files:  - path:"
        - "failure_modes:  missing_required_inputs:"
        - "completion_gate:  target_path_valid:"
        - "```markdown"
        - "```markdown id="
      search_scope:
        - ".claude/Claude.md"
        - ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
        - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
        - ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
      action_rule: "Expand collapsed blocks and remove wrapper fences from live entrypoints/manifests."

    path_drift:
      patterns:
        - ".claude/skills/precap-week"
        - ".claude/skills/project-status-overview"
        - ".claude/skills/ai-routing-and-usage-tracking"
        - ".claude/skills/prompt-engineering"
        - ".claude/skills/workflow-process-design"
      search_scope:
        - ".claude/Claude.md"
        - ".claude/skills/PrecapWeek"
        - ".claude/skills/PrecapNextDay"
        - ".claude/skills/ProjectStatus"
        - ".claude/skills/AIRouting"
      action_rule: >
        Do not rename folders. Add actual_live_path and canonical_target_path
        bridges where needed. Use actual live path as authoritative until a
        separate package-normalization pass.

    output_design_signal:
      patterns:
        - "result card"
        - "success card"
        - "Operator Review First"
        - "Route Reuse / Avoid Signal"
        - "learning signal"
        - "next_PreCapNextDay_hint"
      search_scope:
        - ".claude/skills/PrecapNextDay"
        - ".claude/skills/model-usage-log"
      action_rule: >
        Add minimal top-level operator value cards. Do not redesign the final
        output system.

    missing_precapweek_references:
      filenames:
        - "calendar-planning-guidance.md"
        - "weekly-plan-output-contract.md"
        - "weekly-blueprint-standard.md"
        - "weekly-blueprint-meeting-example.md"
        - "validation-checklist.md"
      search_scope:
        - ".claude/skills/PrecapWeek"
        - "ApexDefinition&OldVersions/ApexWithClaude/FinalFiles/PrecapWeek"
      action_rule: >
        If live references are missing, create minimal live reference files.
        Prefer recovered old-version intent where high-confidence; otherwise
        create narrow interface stubs that satisfy the entrypoint and manifest
        without expanding scope.
```

---

## 4. Source Inventory Expected by Plan

```yaml
source_inventory_expected:
  root_control:
    actual_path: ".claude/Claude.md"
    known_issue:
      - "core_loop, operator_gates, artifact_paths are collapsed one-line machine blocks"
    intended_resolution:
      - "make readable YAML blocks"
      - "add actual/canonical path policy"

  PreCapWeek:
    actual_package: ".claude/skills/PrecapWeek/"
    actual_entrypoint: "Skill_Precap-Week.md"
    manifest: "package-manifest.md"
    known_issue:
      - "manifest names lowercase canonical path and SKILL.md, not live path/file"
      - "support files declared but live references are not discoverable"
      - "entrypoint contains collapsed YAML-like blocks"
    intended_resolution:
      - "preserve live path"
      - "label canonical path as future target"
      - "create missing references or align manifest to live files"
      - "expand collapsed blocks"

  PreCapNextDay:
    actual_package: ".claude/skills/PrecapNextDay/"
    actual_entrypoint: "Skill_precap-next-day.md"
    manifest: "precap-next-day-package-manifest.md"
    known_issue:
      - "entrypoint wrapped in markdown code fence"
      - "manifest has actual/canonical policy but can be clearer"
      - "operator template is table-first"
      - "dependency contracts point to lowercase non-live upstream paths"
    intended_resolution:
      - "remove wrapper fence"
      - "make path policy machine-checkable"
      - "add result card policy and template section"
      - "add actual_live_path bridges in dependency contracts"

  ProjectStatus:
    actual_package: ".claude/skills/ProjectStatus/"
    actual_entrypoint: "project-status-overview_SKILL_v3.md"
    manifest: "package-manifest.md"
    known_issue:
      - "manifest declares .claude/skills/project-status-overview/SKILL.md"
    intended_resolution:
      - "manifest exposes actual path and future canonical target distinctly"

  AIRouting:
    actual_package: ".claude/skills/AIRouting/"
    actual_entrypoint: "ai-routing-and-usage-tracking-SKILL.md"
    manifest: "ai-routing-and-usage-tracking-package-manifest.md"
    known_issue:
      - "entrypoint and manifest contain build-handoff residue"
      - "manifest names lowercase canonical path"
      - "support path placement may differ from declared references path"
    intended_resolution:
      - "remove invocation-surface build residue"
      - "add actual/canonical path bridge"
      - "do not move files"

  project_kb_manager:
    actual_package: ".claude/skills/project-kb-manager/"
    actual_entrypoint: "SKILL.md"
    known_issue:
      - "state packet contract/template in manifest but omitted from SKILL support map"
    intended_resolution:
      - "add handoff mode and support-file references"

  raw_flow_dump_normalize:
    actual_package: ".claude/skills/raw-flow-dump-normalize/"
    actual_entrypoint: "SKILL.md"
    known_issue:
      - "completion gate checks package creation rather than invocation output"
    intended_resolution:
      - "replace with run-level completion gate"

  status_merge:
    actual_package: ".claude/skills/status-merge/"
    actual_entrypoint: "SKILL.md"
    known_issue:
      - "completion gate includes package-build checks"
    intended_resolution:
      - "replace with run-level merge proposal completion gate"

  model_usage_log:
    actual_package: ".claude/skills/model-usage-log/"
    known_issue:
      - "route signal exists but learning takeaway is not top-level"
    intended_resolution:
      - "add operator learning card near top of template"
```

---

## 5. Target File and Patch Map

```yaml
target_files:
  - id: "001"
    blocker_ids: [PB001, PB004]
    batch_ids: [B1]
    target_file: ".claude/Claude.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/001-root-claude-loop-source-authority.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "002"
    blocker_ids: [PB002]
    batch_ids: [B3]
    target_file: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/002-precap-next-day-entrypoint-unfence.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "003"
    blocker_ids: [PB003, PB004]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/003-precap-week-entrypoint-readable.patch"
    patch_type: "modify_existing"
    risk: "medium"

  - id: "004"
    blocker_ids: [PB001, PB003]
    batch_ids: [B2, B3]
    target_file: ".claude/skills/PrecapWeek/package-manifest.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/004-precap-week-manifest-actual-paths.patch"
    patch_type: "modify_existing"
    risk: "medium"

  - id: "005"
    blocker_ids: [PB003]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/005-precap-week-calendar-guidance.patch"
    patch_type: "create_if_missing"
    risk: "medium"

  - id: "006"
    blocker_ids: [PB003]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/006-precap-week-output-contract.patch"
    patch_type: "create_if_missing"
    risk: "medium"

  - id: "007"
    blocker_ids: [PB003]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/007-precap-week-blueprint-standard.patch"
    patch_type: "create_if_missing"
    risk: "medium"

  - id: "008"
    blocker_ids: [PB003]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/008-precap-week-meeting-example.patch"
    patch_type: "create_if_missing"
    risk: "medium"

  - id: "009"
    blocker_ids: [PB003]
    batch_ids: [B2]
    target_file: ".claude/skills/PrecapWeek/references/validation-checklist.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/009-precap-week-validation-checklist.patch"
    patch_type: "create_if_missing"
    risk: "medium"

  - id: "010"
    blocker_ids: [PB001]
    batch_ids: [B3]
    target_file: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/010-precap-next-day-path-policy.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "011"
    blocker_ids: [PB006]
    batch_ids: [B5]
    target_file: ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/011-operator-output-design-result-card-policy.patch"
    patch_type: "modify_existing"
    risk: "medium"

  - id: "012"
    blocker_ids: [PB006]
    batch_ids: [B5]
    target_file: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/012-next-day-plan-result-card.patch"
    patch_type: "modify_existing"
    risk: "medium"

  - id: "013"
    blocker_ids: [PB008]
    batch_ids: [B3]
    target_file: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/013-prompt-engineering-path-bridge.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "014"
    blocker_ids: [PB008]
    batch_ids: [B3]
    target_file: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/014-usage-tracking-path-bridge.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "015"
    blocker_ids: [PB008]
    batch_ids: [B3]
    target_file: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/015-workflow-process-path-bridge.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "016"
    blocker_ids: [PB001]
    batch_ids: [B3]
    target_file: ".claude/skills/ProjectStatus/package-manifest.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/016-projectstatus-manifest-actual-paths.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "017"
    blocker_ids: [PB001, PB005]
    batch_ids: [B3, B4]
    target_file: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/017-airouting-entrypoint-residue-removal.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "018"
    blocker_ids: [PB001, PB005]
    batch_ids: [B3, B4]
    target_file: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/018-airouting-manifest-residue-and-paths.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "019"
    blocker_ids: [PB005]
    batch_ids: [B4]
    target_file: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/019-raw-flow-run-completion-gate.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "020"
    blocker_ids: [PB005]
    batch_ids: [B4]
    target_file: ".claude/skills/status-merge/SKILL.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/020-status-merge-run-completion-gate.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "021"
    blocker_ids: [PB007]
    batch_ids: [B6]
    target_file: ".claude/skills/project-kb-manager/SKILL.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/021-project-kb-manager-state-handoff-exposure.patch"
    patch_type: "modify_existing"
    risk: "low"

  - id: "022"
    blocker_ids: [PB009]
    batch_ids: [B5]
    target_file: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    patch_file: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/022-model-usage-learning-card.patch"
    patch_type: "modify_existing"
    risk: "low"
```

---

## 6. Improvement Matrix

```yaml
improvement_matrix:
  B1_root_loop_and_source_authority:
    blocker_ids: [PB001, PB004]
    patch_ids: ["001"]
    impact_0_100: 96
    evidence_confidence_0_100: 98
    goal: "Make root control source readable and path-realistic."
    desired_state:
      - "core_loop is a readable YAML block."
      - "operator_gates is a readable YAML block."
      - "artifact_paths is a readable YAML block."
      - "root skill index remains actual-live-path authoritative."
      - "path_policy distinguishes actual_live_path from canonical_target_path."
      - "canonical paths are future normalization targets, not current file claims."
    high_impact_extra_checks:
      - "Check if root index omits any new loop packages created after Claude.md was last edited."
      - "Check if root forbidden actions still include no scheduler, no calendar, no auto state overwrite."
    forbidden:
      - "Do not create new package names."
      - "Do not move folders."
      - "Do not claim canonical paths already exist."

  B2_PreCapWeek_handoff_integrity:
    blocker_ids: [PB003, PB004]
    patch_ids: ["003", "004", "005", "006", "007", "008", "009"]
    impact_0_100: 94
    evidence_confidence_0_100: 94
    goal: "Make PreCapWeek readable and make weekly-to-daily handoff support files inspectable."
    desired_state:
      - "Skill_Precap-Week.md is readable and not collapsed."
      - "package-manifest.md reflects actual live package path and entrypoint."
      - "All declared support references exist or are explicitly marked missing; preferred fix is to create minimal references."
      - "weekly-plan-output-contract defines first_precap_next_day_seed boundary."
      - "calendar-planning-guidance makes calendar output proposal-only."
      - "validation-checklist validates weekly output and seed, not package creation."
    high_impact_extra_checks:
      - "Search old PreCapWeek final files for stronger names/fields before writing minimal stubs."
      - "Ensure PreCapWeek does not own next_day_plan, flow_prompt_pack, or calendar writes."
    forbidden:
      - "Do not define daily plan output schema in PreCapWeek."
      - "Do not create FlowRecap or PromptEngineer outputs."
      - "Do not perform calendar writes."

  B3_manifest_and_path_alignment:
    blocker_ids: [PB001, PB008]
    patch_ids: ["010", "013", "014", "015", "016", "018"]
    impact_0_100: 90
    evidence_confidence_0_100: 93
    goal: "Make actual vs canonical path policy explicit across dependent packages."
    desired_state:
      - "Affected manifests expose package_path_actual and package_path_canonical_target."
      - "Affected dependency contracts expose actual_live_path and canonical_target_path."
      - "path_resolution_policy says actual_live_path is authoritative until package-normalization pass."
    high_impact_extra_checks:
      - "Compare every manifest-declared file path with git ls-files."
      - "Mark future canonical targets as pending, not missing errors."
    forbidden:
      - "Do not move package directories."
      - "Do not patch generated old versions."
      - "Do not update references to nonexistent live paths."

  B4_remove_build_residue:
    blocker_ids: [PB005]
    patch_ids: ["017", "018", "019", "020"]
    impact_0_100: 88
    evidence_confidence_0_100: 98
    goal: "Remove package-construction residue from live invocation surfaces."
    desired_state:
      - "AIRouting entrypoint has no NEXT PROMPT or package-build validation section."
      - "AIRouting manifest has no next-package prompt residue."
      - "raw-flow-dump-normalize completion gate validates invocation output."
      - "status-merge completion gate validates merge proposal output."
    high_impact_extra_checks:
      - "Search all live SKILL.md and *_SKILL*.md files for package_path_created."
      - "Do not remove real runtime boundary safety checks while removing build residue."
    forbidden:
      - "Do not remove no-runtime/no-calendar/no-state-overwrite boundaries."

  B5_output_success_signal_placeholders:
    blocker_ids: [PB006, PB009]
    patch_ids: ["011", "012", "022"]
    impact_0_100: 82
    evidence_confidence_0_100: 90
    goal: "Add minimal operator value anchors before later output-design Deep Research."
    desired_state:
      - "operator-output-format-design includes result_card_policy."
      - "next-day-plan operator template has a compact Result Card before detail tables."
      - "tables are explicitly secondary/detail views."
      - "model-usage template has Operator Learning Card before detailed usage evidence."
    high_impact_extra_checks:
      - "Preserve all machine-readable output fields."
      - "Do not attempt full information design overhaul."
    forbidden:
      - "Do not remove tables entirely."
      - "Do not create final UI specification."

  B6_state_handoff_visibility:
    blocker_ids: [PB007]
    patch_ids: ["021"]
    impact_0_100: 78
    evidence_confidence_0_100: 96
    goal: "Expose apex_orchestration_state_packet through project-kb-manager live entrypoint."
    desired_state:
      - "project-kb-manager SKILL supporting_files include state packet contract and template."
      - "handoff_mode is visible as a mode or submode."
      - "durable writes remain operator-gated and project-kb-manager-boundary-safe."
    high_impact_extra_checks:
      - "Read manifest state packet entries before editing SKILL.md."
      - "Keep query/update/intake modes intact."
    forbidden:
      - "Do not replace project schema."
      - "Do not trigger PreCapWeek or PreCapNextDay."
```

---

## 7. Per-Target Contracts

```yaml
per_target_contracts:
  "001":
    target_file: ".claude/Claude.md"
    blocker_ids: [PB001, PB004]
    read_before_edit:
      - "Blockers.md PB001/PB004"
      - ".claude/Claude.md"
    required_changes:
      - "Expand core_loop collapsed block into multi-line YAML."
      - "Expand operator_gates collapsed block into multi-line YAML."
      - "Expand artifact_paths collapsed block into multi-line YAML."
      - "Add path_policy section."
      - "For each mixed-case package in root skill index, preserve actual path and optionally add canonical_target_path note."
    required_markers:
      - "path_policy:"
      - "actual_live_path"
      - "canonical_target_path"
      - "core_loop:"
      - "operator_gates:"
      - "artifact_paths:"
    forbidden_markers:
      - "core_loop:  1:"
      - "operator_gates:  G1:"
      - "artifact_paths:  apex_project_status:"
    acceptance:
      - "Root file is easier to read and less likely to misroute Agent Mode."
      - "No new runtime behavior introduced."

  "002":
    target_file: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    blocker_ids: [PB002]
    read_before_edit:
      - "Blockers.md PB002"
      - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    required_changes:
      - "Remove the opening markdown code fence before frontmatter."
      - "Remove final closing code fence if it only closes the wrapper."
      - "Keep substantive skill content unchanged except necessary heading cleanup."
    required_markers:
      - "---\nname: precap-next-day"
      - "## Skill Contract"
      - "## Completion Gate"
    forbidden_markers:
      - "```markdown"
      - "```markdown id="
    acceptance:
      - "YAML frontmatter begins at raw file start."

  "003":
    target_file: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    blocker_ids: [PB003, PB004]
    required_changes:
      - "Convert collapsed skill_contract/supporting_files/failure_modes/completion_gate blocks into readable YAML."
      - "Keep scope limited to weekly planning and first PreCapNextDay seed."
      - "Point supporting_files to live references under .claude/skills/PrecapWeek/references/."
    required_markers:
      - "skill_contract:"
      - "supporting_files:"
      - "failure_modes:"
      - "completion_gate:"
      - "first_precap_next_day_seed"
    forbidden_markers:
      - "skill_contract:  skill_name:"
      - "supporting_files:  - path:"
      - "failure_modes:  missing_required_inputs:"
      - "completion_gate:  target_path_valid:"
    acceptance:
      - "Entrypoint is readable and support-file references are resolvable after patches 005-009."

  "004":
    target_file: ".claude/skills/PrecapWeek/package-manifest.md"
    blocker_ids: [PB001, PB003]
    required_changes:
      - "Add or update package_path_actual as .claude/skills/PrecapWeek/."
      - "Add or update entrypoint_file_actual as Skill_Precap-Week.md."
      - "Preserve lowercase path only as package_path_canonical_target."
      - "Set normalization_status to pending."
      - "Make exact_files match live entrypoint and created reference files."
    required_markers:
      - "package_path_actual: .claude/skills/PrecapWeek/"
      - "entrypoint_file_actual: Skill_Precap-Week.md"
      - "package_path_canonical_target: .claude/skills/precap-week/"
      - "normalization_status: pending"
    forbidden_markers:
      - "package_path: .claude/skills/precap-week/"
    acceptance:
      - "Manifest no longer implies current live package is lowercase SKILL.md."

  "005":
    target_file: ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md"
    blocker_ids: [PB003]
    patch_type: "create_if_missing"
    required_changes:
      - "Create minimal guidance for calendar-aware weekly planning."
      - "State that PreCapWeek may propose planning blocks but must not write calendar events."
      - "State calendar inputs are operator-provided context, not direct calendar mutation authority."
    required_markers:
      - "# Calendar Planning Guidance"
      - "calendar_behavior:"
      - "create_calendar_events: false"
      - "calendar_block_proposals_only: true"
    forbidden_markers:
      - "create_calendar_events: true"
      - "actual_calendar_write"
    acceptance:
      - "Calendar behavior is safe and inspectable."

  "006":
    target_file: ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md"
    blocker_ids: [PB003]
    patch_type: "create_if_missing"
    required_changes:
      - "Define PreCapWeek output contract."
      - "Include weekly intent, constraints, project focus, day-shape overview, and first_precap_next_day_seed."
      - "Make first_precap_next_day_seed explicitly seed-only and operator-reviewed."
    required_markers:
      - "# Weekly Plan Output Contract"
      - "precap_week_output"
      - "first_precap_next_day_seed"
      - "operator_validation"
    forbidden_markers:
      - "flow_prompt_pack:"
      - "accepted_project_status_delta"
    acceptance:
      - "Weekly-to-daily handoff is defined without owning daily plan execution."

  "007":
    target_file: ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md"
    blocker_ids: [PB003]
    patch_type: "create_if_missing"
    required_changes:
      - "Define normal weekly blueprint pattern."
      - "Use Monday_to_Friday and Sunday_weekly_precap_session markers."
      - "Keep Saturday/Sunday nonstandard assumptions explicit."
    required_markers:
      - "# Weekly Blueprint Standard"
      - "Monday_to_Friday"
      - "Sunday_weekly_precap_session"
    forbidden_markers:
      - "Saturday_regular_planning"
      - "Sunday_regular_day_planning"
    acceptance:
      - "Standard weekly pattern is available as reference."

  "008":
    target_file: ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md"
    blocker_ids: [PB003]
    patch_type: "create_if_missing"
    required_changes:
      - "Define how meeting-heavy or constrained weeks deform the standard blueprint."
      - "Include partial_flow_rules and meeting_week_deformation_rules."
      - "Keep all examples proposal-only."
    required_markers:
      - "# Weekly Blueprint Meeting Example"
      - "meeting_week_deformation_rules"
      - "partial_flow_rules"
    forbidden_markers:
      - "calendar_event_creation"
    acceptance:
      - "Meeting-week example exists without creating calendar behavior."

  "009":
    target_file: ".claude/skills/PrecapWeek/references/validation-checklist.md"
    blocker_ids: [PB003]
    patch_type: "create_if_missing"
    required_changes:
      - "Validate PreCapWeek outputs and first daily seed."
      - "Include missing_input_behavior and operator_review_flags."
      - "No package-build checks."
    required_markers:
      - "# Validation Checklist"
      - "validation_checks:"
      - "operator_review_flags:"
      - "missing_input_behavior:"
    forbidden_markers:
      - "NEXT PROMPT"
      - "package_path_created"
    acceptance:
      - "Validation is invocation/output oriented."

  "010":
    target_file: ".claude/skills/PrecapNextDay/precap-next-day-package-manifest.md"
    blocker_ids: [PB001]
    required_changes:
      - "Make current actual path and future canonical target machine-readable."
      - "State actual path is authoritative until package normalization."
    required_markers:
      - "package_path_actual: \".claude/skills/PrecapNextDay/\""
      - "package_path_canonical_target: \".claude/skills/precap-next-day/\""
      - "normalization_status: pending"
      - "actual_path_is_authoritative_until_normalization: true"
    forbidden_markers: []
    acceptance:
      - "Path policy is explicit."

  "011":
    target_file: ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
    blocker_ids: [PB006]
    required_changes:
      - "Add result_card_policy."
      - "State operator value signal should appear before detail tables."
      - "State tables are secondary detail/navigation views."
    required_markers:
      - "result_card_policy:"
      - "tables_are_secondary_detail_views"
      - "operator_value_signal_first"
    forbidden_markers: []
    acceptance:
      - "Deep Research will not simply optimize table-first artifact design."

  "012":
    target_file: ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
    blocker_ids: [PB006]
    required_changes:
      - "Insert compact Result Card near top, before wide tables."
      - "Include operator_value_signal, what_changed_for_operator, next_action_for_operator."
      - "Preserve existing tables as detail sections."
    required_markers:
      - "## 2. Result Card"
      - "operator_value_signal"
      - "what_changed_for_operator"
      - "next_action_for_operator"
    forbidden_markers: []
    acceptance:
      - "Operator sees result/success signal before dense tables."

  "013":
    target_file: ".claude/skills/PrecapNextDay/references/prompt-engineering-dependency-contract.md"
    blocker_ids: [PB008]
    required_changes:
      - "Add path_resolution_policy."
      - "Add actual_live_path for PromptEngineer current file."
      - "Preserve lowercase path as canonical_target_path only."
    required_markers:
      - "path_resolution_policy:"
      - "actual_live_path: \".claude/skills/PromptEngineer/SKILL_prompt-engineering.md\""
      - "canonical_target_path: \".claude/skills/prompt-engineering/\""
    forbidden_markers: []
    acceptance:
      - "Dependency inspection opens correct live PromptEngineer file."

  "014":
    target_file: ".claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md"
    blocker_ids: [PB008]
    required_changes:
      - "Add path_resolution_policy."
      - "Add actual_live_path for AIRouting current entrypoint."
      - "Preserve lowercase path as canonical_target_path only."
    required_markers:
      - "path_resolution_policy:"
      - "actual_live_path: \".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md\""
      - "canonical_target_path: \".claude/skills/ai-routing-and-usage-tracking/\""
    forbidden_markers: []
    acceptance:
      - "Dependency inspection opens correct live AIRouting file."

  "015":
    target_file: ".claude/skills/PrecapNextDay/references/workflow-process-validation-contract.md"
    blocker_ids: [PB008]
    required_changes:
      - "Add path_resolution_policy."
      - "Add actual_live_path for Workflow&Processes current entrypoint."
      - "Preserve lowercase path as canonical_target_path only."
    required_markers:
      - "path_resolution_policy:"
      - "actual_live_path: \".claude/skills/Workflow&Processes/workflow-process-design-SKILL.md\""
      - "canonical_target_path: \".claude/skills/workflow-process-design/\""
    forbidden_markers: []
    acceptance:
      - "Dependency inspection opens correct live Workflow&Processes file."

  "016":
    target_file: ".claude/skills/ProjectStatus/package-manifest.md"
    blocker_ids: [PB001]
    required_changes:
      - "Add package_path_actual as .claude/skills/ProjectStatus/."
      - "Add entrypoint_file_actual as project-status-overview_SKILL_v3.md."
      - "Preserve lowercase package as canonical target only."
      - "Set normalization_status pending."
    required_markers:
      - "package_path_actual: \".claude/skills/ProjectStatus/\""
      - "entrypoint_file_actual: \"project-status-overview_SKILL_v3.md\""
      - "package_path_canonical_target: \".claude/skills/project-status-overview/\""
      - "normalization_status: pending"
    forbidden_markers:
      - "path: \".claude/skills/project-status-overview/SKILL.md\""
    acceptance:
      - "ProjectStatus manifest no longer points patcher to non-live path as current."

  "017":
    target_file: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
    blocker_ids: [PB001, PB005]
    required_changes:
      - "Remove NEXT PROMPT section."
      - "Remove package-build validation residue if present."
      - "Preserve actual routing procedure, output requirements, failure modes, and completion gate."
      - "If frontmatter is not at raw file start because of a file-header line, either fix minimally or explicitly leave if outside blocker scope; record decision in manifest."
    required_markers:
      - "## Completion Gate"
      - "routing_decision_present: true"
    forbidden_markers:
      - "# VALIDATION"
      - "# NEXT PROMPT"
      - "Paste this next"
    acceptance:
      - "AIRouting entrypoint is invocation-oriented."

  "018":
    target_file: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-package-manifest.md"
    blocker_ids: [PB001, PB005]
    required_changes:
      - "Remove wrapper markdown code fence if present."
      - "Remove NEXT PROMPT section."
      - "Add package_path_actual and entrypoint_file_actual."
      - "Preserve lowercase path as canonical target only."
      - "Set normalization_status pending."
    required_markers:
      - "package_path_actual: \".claude/skills/AIRouting/\""
      - "entrypoint_file_actual: \"ai-routing-and-usage-tracking-SKILL.md\""
      - "package_path_canonical_target: \".claude/skills/ai-routing-and-usage-tracking/\""
      - "normalization_status: pending"
    forbidden_markers:
      - "```markdown id="
      - "# NEXT PROMPT"
      - "Paste this next"
    acceptance:
      - "AIRouting manifest is path-realistic and no longer a build-handoff prompt."

  "019":
    target_file: ".claude/skills/raw-flow-dump-normalize/SKILL.md"
    blocker_ids: [PB005]
    required_changes:
      - "Replace package-build completion gate with raw_flow_dump_output_completion_gate."
      - "Gate must validate normalized raw dump OR skipped-flow marker."
      - "Gate must confirm no FlowRecap/status-merge/model-usage output was created."
    required_markers:
      - "raw_flow_dump_output_completion_gate:"
      - "normalized_raw_flow_dump_or_skipped_flow_marker_present: true"
      - "no_FlowRecap_or_status_merge_output_created: true"
    forbidden_markers:
      - "package_path_created: true"
      - "raw_flow_dump_contract_created: true"
      - "manifest_created: true"
      - "SKILL_md_created_with_valid_frontmatter: true"
    acceptance:
      - "Completion gate validates live skill invocation output only."

  "020":
    target_file: ".claude/skills/status-merge/SKILL.md"
    blocker_ids: [PB005]
    required_changes:
      - "Replace package-build completion gate with status_merge_output_completion_gate."
      - "Gate must validate status merge packet/proposal, conflict notes, and next PreCap context seed."
      - "Gate must preserve no durable state overwrite boundary."
    required_markers:
      - "status_merge_output_completion_gate:"
      - "status_merge_packet_present: true"
      - "next_PreCapNextDay_input_context_is_seed_only: true"
    forbidden_markers:
      - "package_path_created: true"
      - "template_created: true"
      - "manifest_created: true"
      - "SKILL_md_created_with_valid_frontmatter: true"
    acceptance:
      - "Completion gate validates merge proposal output only."

  "021":
    target_file: ".claude/skills/project-kb-manager/SKILL.md"
    blocker_ids: [PB007]
    required_changes:
      - "Add handoff_mode or orchestration_state_handoff_mode to supported modes."
      - "Add state packet contract to supporting files."
      - "Add state packet template to supporting files."
      - "Mention apex_orchestration_state_packet output when handoff mode is requested."
      - "Preserve update/query/intake boundaries."
    required_markers:
      - "handoff_mode"
      - "references/apex-orchestration-state-packet-contract.md"
      - "templates/apex-orchestration-state-packet-template.md"
      - "apex_orchestration_state_packet"
    forbidden_markers: []
    acceptance:
      - "State handoff layer is visible at invocation time."
      - "Durable writes remain operator-gated."

  "022":
    target_file: ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
    blocker_ids: [PB009]
    required_changes:
      - "Add Operator Learning Card near top."
      - "Include route_reuse_or_avoid_signal and next_PreCapNextDay_hint."
      - "Preserve existing detailed usage delta fields."
    required_markers:
      - "## 2. Operator Learning Card"
      - "operator_learning_card:"
      - "route_reuse_or_avoid_signal"
      - "next_PreCapNextDay_hint"
    forbidden_markers: []
    acceptance:
      - "Learning signal is visible before detailed usage evidence."
```

---

## 8. Cross-File Consistency Requirements

```yaml
cross_file_consistency:
  path_policy:
    actual_live_paths_must_match_root_index:
      PreCapWeek: ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
      PreCapNextDay: ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
      ProjectStatus: ".claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md"
      AIRouting: ".claude/skills/AIRouting/ai-routing-and-usage-tracking-SKILL.md"
      PromptEngineer: ".claude/skills/PromptEngineer/SKILL_prompt-engineering.md"
      WorkflowProcesses: ".claude/skills/Workflow&Processes/workflow-process-design-SKILL.md"
    canonical_targets_are_future_only:
      - ".claude/skills/precap-week/"
      - ".claude/skills/precap-next-day/"
      - ".claude/skills/project-status-overview/"
      - ".claude/skills/ai-routing-and-usage-tracking/"
      - ".claude/skills/prompt-engineering/"
      - ".claude/skills/workflow-process-design/"

  PreCapWeek_to_PreCapNextDay_boundary:
    PreCapWeek_may_output:
      - "weekly plan"
      - "weekly blueprint"
      - "first_precap_next_day_seed"
      - "operator review flags"
    PreCapWeek_must_not_output:
      - "next_day_plan"
      - "flow_prompt_pack"
      - "calendar event writes"
      - "accepted project status delta"

  live_skill_completion_gates:
    must_be_invocation_level: true
    must_not_be_package_build_level: true
    affected_files:
      - ".claude/skills/raw-flow-dump-normalize/SKILL.md"
      - ".claude/skills/status-merge/SKILL.md"

  output_design_placeholder_policy:
    must_add_value_signal: true
    must_not_finalize_design: true
    cards_before_tables: true
    affected_files:
      - ".claude/skills/PrecapNextDay/references/operator-output-format-design.md"
      - ".claude/skills/PrecapNextDay/templates/next-day-plan-operator-template.md"
      - ".claude/skills/model-usage-log/templates/model-usage-delta-template.md"
```

---

## 9. Forbidden Paths and Mutation Guard

```yaml
forbidden_paths_for_patch_pack:
  never_modify:
    - "state/**"
    - ".claude/kb/**"
    - "source-knowledge/**"
    - "ApexDefinition&OldVersions/**"
    - ".github/workflows/**"
    - "scripts/**"
    - "**/*.py"
    - "**/*.json"
    - "**/*.yaml"
    - "**/*.yml"
  allowed_new_paths:
    - ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md"
    - ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md"
    - ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md"
    - ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md"
    - ".claude/skills/PrecapWeek/references/validation-checklist.md"
    - "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/**"

forbidden_behavior:
  - "No direct target-file final commit in builder run."
  - "No broad formatter run."
  - "No line-ending normalization across whole repo."
  - "No schema rewrite outside named target files."
  - "No final output design research during patch-pack creation."
```

---

## 10. Patch-Pack Artifact Contract

```yaml
patch_pack_artifacts:
  directory: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/"
  required_files:
    manifest: "000-patch-manifest.md"
    patches:
      - "001-root-claude-loop-source-authority.patch"
      - "002-precap-next-day-entrypoint-unfence.patch"
      - "003-precap-week-entrypoint-readable.patch"
      - "004-precap-week-manifest-actual-paths.patch"
      - "005-precap-week-calendar-guidance.patch"
      - "006-precap-week-output-contract.patch"
      - "007-precap-week-blueprint-standard.patch"
      - "008-precap-week-meeting-example.patch"
      - "009-precap-week-validation-checklist.patch"
      - "010-precap-next-day-path-policy.patch"
      - "011-operator-output-design-result-card-policy.patch"
      - "012-next-day-plan-result-card.patch"
      - "013-prompt-engineering-path-bridge.patch"
      - "014-usage-tracking-path-bridge.patch"
      - "015-workflow-process-path-bridge.patch"
      - "016-projectstatus-manifest-actual-paths.patch"
      - "017-airouting-entrypoint-residue-removal.patch"
      - "018-airouting-manifest-residue-and-paths.patch"
      - "019-raw-flow-run-completion-gate.patch"
      - "020-status-merge-run-completion-gate.patch"
      - "021-project-kb-manager-state-handoff-exposure.patch"
      - "022-model-usage-learning-card.patch"
    apply_handoff: "999-apply-patches.md"

  manifest_must_include:
    - "repo and branch"
    - "source plan path"
    - "Blockers.md read status"
    - "Git-native patch process guide read status"
    - "dirty-state notes"
    - "patch order"
    - "target-to-patch map"
    - "per-patch single-file scope result"
    - "per-patch git apply --check result"
    - "cumulative apply-check result"
    - "cumulative apply result"
    - "changed-file scope result"
    - "required marker results"
    - "forbidden marker results"
    - "final builder state"

  apply_handoff_must_include:
    - "start from clean main"
    - "git apply --check each patch before applying"
    - "apply patches in numeric order"
    - "verify changed-file scope equals target_files"
    - "verify required markers"
    - "verify forbidden markers"
    - "commit implementation changes separately from patch-pack creation"
    - "do not manually edit target files during apply"
```

---

## 11. Validation Matrix

```yaml
validation_matrix:
  per_patch:
    - check: "patch_non_empty"
      pass_condition: "patch file contains a diff"
    - check: "single_file_scope"
      pass_condition: "patch contains exactly one diff target and it equals target_file"
    - check: "apply_check"
      pass_condition: "git apply --check succeeds from clean base"

  cumulative:
    - check: "apply_check_all_in_order"
      pass_condition: "all patches can be checked in numeric order"
    - check: "apply_all_in_order"
      pass_condition: "all patches apply in numeric order"
    - check: "changed_file_scope"
      pass_condition: "changed files equal the target file list exactly"
    - check: "required_markers"
      pass_condition: "all required markers in this plan are present after cumulative apply"
    - check: "forbidden_markers"
      pass_condition: "all forbidden markers in this plan are absent after cumulative apply"
    - check: "forbidden_paths"
      pass_condition: "no forbidden path is changed"

  target_file_scope_must_equal:
    - ".claude/Claude.md"
    - ".claude/skills/PrecapNextDay/Skill_precap-next-day.md"
    - ".claude/skills/PrecapWeek/Skill_Precap-Week.md"
    - ".claude/skills/PrecapWeek/package-manifest.md"
    - ".claude/skills/PrecapWeek/references/calendar-planning-guidance.md"
    - ".claude/skills/PrecapWeek/references/weekly-plan-output-contract.md"
    - ".claude/skills/PrecapWeek/references/weekly-blueprint-standard.md"
    - ".claude/skills/PrecapWeek/references/weekly-blueprint-meeting-example.md"
    - ".claude/skills/PrecapWeek/references/validation-checklist.md"
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
```

---

## 12. Agent Mode Final Report Schema

```yaml
final_report_schema:
  verdict: "PASS | PARTIAL_ARTIFACT_EXPORT | FAIL"
  repo: "leela-spec/apexai-os-meta"
  branch: "main"
  patch_plan_read: true
  blocker_source_read: "true | false | embedded_only"
  git_native_process_read: "true | false | embedded_only"
  patch_pack_path: "apex-meta/patch-packs/2026-07-07-step1-prompt-blocker-cleanup/"
  source_files_read:
    - "<path>"
  patches_created:
    - patch_id: "001"
      patch_file: "<path>"
      target_file: "<path>"
      git_diff_generated: "PASS | FAIL"
      single_file_scope: "PASS | FAIL"
      git_apply_check: "PASS | FAIL"
      marker_check: "PASS | FAIL"
  cumulative_validation:
    git_apply_check_all: "PASS | FAIL"
    git_apply_all: "PASS | FAIL"
    changed_file_scope: "PASS | FAIL"
    required_markers: "PASS | FAIL"
    forbidden_markers: "PASS | FAIL"
    forbidden_paths_unchanged: "PASS | FAIL"
  builder_final_state:
    target_files_reverted: true
    only_patch_artifacts_changed: true
  patch_pack_committed_or_exported: "committed | exported | not_done"
  unresolved_notes:
    - "Only include if blocking or genuinely relevant."
```

---

## 13. Done Criteria

```yaml
done_when:
  - "All required patch-pack artifacts exist."
  - "There is exactly one Git-generated patch per target file."
  - "Every patch touches exactly one target file."
  - "Every patch passes git apply --check."
  - "The cumulative patch sequence passes apply-check and apply validation."
  - "Changed-file scope equals target_file_scope_must_equal exactly."
  - "Required markers are present after cumulative apply."
  - "Forbidden markers are absent after cumulative apply."
  - "No forbidden path is changed."
  - "The builder final state contains patch artifacts only."
  - "000-patch-manifest.md is complete."
  - "999-apply-patches.md is complete."

not_done_if:
  - "Any target file remains modified in the builder final state."
  - "Any patch was hand-written instead of generated from git diff."
  - "Any patch touches more than one target file."
  - "Any old-version or source-knowledge file is modified."
  - "Any runtime, state, calendar, scheduler, or project execution behavior is introduced."
  - "Deep Research is started before this cleanup patch pack exists."
```
