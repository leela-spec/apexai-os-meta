```
# APEX PM/KB/PD — Generate Canonical `apex-sync` Skill Package v2# Model target: GPT-5.5 Pro Thinking# Mode: accepted-mapping application, not research# Output mode: chat-output file blocks only---## 0. MissionYou are a Claude-native skill package author and deterministic Python script designer.Generate the complete canonical `.claude/skills/apex-sync/` package and one consolidated deterministic Python script file block.You are not researching architecture.You are not redesigning Apex.You are not writing to GitHub.You are not cloning repositories.You are not using web search.You are not reading public GitHub source repos.You are not generating Bash, TypeScript, JavaScript, CI, GitHub Actions, calendar logic, AI routing, or PreCapNextDay logic.`apex-sync` is the deterministic synchronization package. It owns read-side checks and exact computations: next-action detection, blocker scan, stall detection, registry/index rebuild, drift detection, priority/urgency/unlock/focus scoring, and dependency validation.---## 1. Execution modeThis prompt supports two environments.```yamlexecution_modes:  local_repo_mode:    description: >      The model has access to the local repo, likely at      C:\GitDev\apexai-os-meta or an equivalent current working directory.    preferred_optional_files:      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\decisions.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\field-schema.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\task-template.md  upload_only_mode:    description: >      The model only has uploaded/project files such as      ProThinkingGPT_Harmonization_v1.md and skill best-practice guides.    behavior: >      Continue from ProThinking extracted evidence and available guidance.      Do not treat missing local repo files as blockers.  output_mode:    repo_write_mode: disabled    git_commit_mode: disabled    confirm_gate_mode_for_prompt_execution: not_applicable    output: complete_file_blocks_only
```

Operator confirmation gates must be represented inside generated skill/script behavior where relevant, not used as this prompt’s execution workflow.

---

## 2. Authority hierarchy

Use this hierarchy.

```
authority_order:  required:    - ProThinkingGPT_Harmonization_v1.md  preferred_if_available:    - apex-meta/harmonization/decisions.md    - APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md    - Apex_Harmonization_NextChat_Handover_and_ProPrompts.md    - Claude_Skill_Package_BestPractice_Handover.md    - Claude_Skill_PromptFlow_Design_Guidance_v1.md  optional_do_not_search_for_if_missing:    - apex-meta/harmonization/field-schema.md    - apex-meta/harmonization/task-template.md  do_not_read_by_default:    - source-knowledge/ProjectRepos/    - .claude/skills/AIRouting/    - .claude/skills/Workflow&Processes/    - .claude/skills/PrecapNextDay/    - .claude/skills/project-kb-manager/    - ApexDefinition&OldVersions/  reason_for_not_reading_source_repos: >    ProThinkingGPT_Harmonization_v1.md already extracted and validated the    implementation evidence for Task Master next-task logic, CCPM tracking,    kanban blocker scans, llm-wiki indexing, and planning-with-files persistence.    Rereading source repos is token waste unless the operator requests an audit.
```

If `ProThinkingGPT_Harmonization_v1.md` is missing, stop and ask for it.

If `decisions.md` is missing, continue using H1–H7 from ProThinking and the init/handover documents. Missing `decisions.md` is not a blocker in upload-only mode.

---

## 3. Minimal preflight

Perform only this preflight.

```
minimal_preflight:  required_check:    - locate_and_read: ProThinkingGPT_Harmonization_v1.md  optional_checks:    - locate_if_available: apex-meta/harmonization/decisions.md    - locate_if_available: Claude_Skill_Package_BestPractice_Handover.md    - locate_if_available: Claude_Skill_PromptFlow_Design_Guidance_v1.md  do_not_do:    - do_not_web_search    - do_not_fetch_public_GitHub    - do_not_scan_entire_repo    - do_not_read_source-knowledge_ProjectRepos    - do_not_validate_existing_live_skill_folders
```

Then produce a compact source availability ledger with maximum 6 rows:

```
source_ledger_columns:  - source  - available  - used_for
```

Do not produce a long evidence matrix.

---

## 4. Binding decisions

Apply these decisions exactly.

```
binding_decisions:  target_package:    name: apex-sync    path: .claude/skills/apex-sync/  durable_paths:    base: apex-meta/    epics: apex-meta/epics/    registry: apex-meta/registry/index.md    handoff: apex-meta/handoff/    scripts: apex-meta/scripts/  status_enum:    - open    - in-progress    - blocked    - done    - deferred  dependency_field:    name: depends_on    type: integer_array    rule: all_depended_task_ids_must_have_status_done_before_task_is_actionable  script_policy:    python_allowed: true    bash_allowed: false    typescript_allowed: false    javascript_allowed: false    shell_out_allowed: false    external_dependencies_allowed: false    standard_library_only: true  package_process_scope:    owns:      - PM4_compute_next_action      - PM5_detect_blockers      - PM7_detect_stall      - PM8_generate_work_registry      - KB4_rebuild_index      - KB5_detect_drift      - PD1_compute_priority_score      - PD2_compute_urgency_score      - PD3_compute_unlock_depth      - PD4_compute_focus_candidates    must_not_own:      - PM1_project_capture      - PM2_human_decomposition      - PM6_status_mutation      - KB1_session_narrative      - KB2_state_delta_interpretation      - KB3_entity_synthesis      - KB6_next_session_authoring      - PD5_operator_validation      - PD6_planning_feed_authoring  priority_policy:    values:      high: 3      medium: 2      low: 1  urgency_policy:    field: due_date    computation: days_until_due_or_999
```

---

## 5. ProThinking mapping to preserve

Use the report mapping. Do not invent new clusters.

```
mapping_to_preserve:  natural_clusters:    decomposition_and_dependency_engine:      primary_home: apex-plan      secondary_home: apex-sync      package_role:        - dependency_validation        - actionable_task_detection        - exact_next_action_computation    session_memory_and_handoff:      primary_home: apex-session      secondary_home: apex-sync      package_role:        - stale_state_detection        - drift_detection        - registry_rebuild    knowledge_entity_maintenance:      primary_home: apex-session      secondary_home: apex-sync      package_role:        - index_rebuild        - orphan_or_drift_scan        - registry_generation    product_scoring_and_recommendation:      primary_home: apex-plan      secondary_home: apex-sync      package_role:        - exact_priority_score        - exact_urgency_score        - unlock_depth_score        - focus_candidate_ordering
```

---

## 6. Files to generate

Generate exactly these files.

```
files_to_generate:  - .claude/skills/apex-sync/SKILL.md  - .claude/skills/apex-sync/references/sync-cluster-contract.md  - .claude/skills/apex-sync/references/script-command-contract.md  - .claude/skills/apex-sync/references/registry-and-drift-rules.md  - .claude/skills/apex-sync/references/scoring-and-focus-rules.md  - .claude/skills/apex-sync/package-manifest.md  - apex-meta/scripts/apex_sync.py
```

Use one consolidated Python script with subcommands instead of many separate scripts to reduce token waste and maintenance surface.

---

## 7. Python script requirements

`apex-meta/scripts/apex_sync.py` must be standard-library-only and implement subcommands:

```
apex_sync_py:  subcommands:    next:      purpose: compute actionable next task candidates    blockers:      purpose: list blocked tasks and missing dependency targets    registry:      purpose: rebuild or print compact registry index    stall:      purpose: detect stale tasks    drift:      purpose: detect registry/source mismatch    score:      purpose: compute priority urgency unlock focus scores  global_flags:    - --root    - --json    - --dry-run  safety:    no_network: true    no_external_dependencies: true    no_shell_out: true    read_only_by_default: true    only_write_allowed: registry_subcommand_with_explicit_non_dry_run    invalid_files_report_and_continue: true  parsing:    input_glob: apex-meta/epics/*/[0-9][0-9][0-9].md    frontmatter: minimal_yaml_like_parser_using_standard_library    body: preserve_as_text
```

The script must not mutate task files, handoff files, entity files, or skill files.

---

## 8. SKILL.md requirements

`SKILL.md` must follow this section order:

```
skill_md_sections:  1: yaml_frontmatter  2: "# Apex Sync"  3: "## Skill Contract"  4: "## Supporting Files"  5: "## Procedure"  6: "## Failure Modes"  7: "## Output Requirements"  8: "## Completion Gate"
```

Frontmatter:

```
frontmatter:  allowed_fields_only:    - name    - description  name: apex-sync  description_must_begin_with: "Use this skill when"  max_words: 80
```

Supporting files must be a YAML block with `path` and `read_when`. Failure modes must be a YAML block where each mode has exactly `trigger` and `correction`.

---

## 9. Package content requirements

The package must include:

```
required_outputs:  - next_action_report  - blocker_report  - registry_report  - stall_report  - drift_report  - score_report  - focus_candidate_reportscript_boundary:  apex_sync_owns_exact_computation: true  apex_plan_owns_rationale_and_policy: true  apex_session_owns_mutation_and_handoff: truereview_flags:  - malformed_frontmatter  - missing_task_id  - unsupported_status  - missing_dependency_target  - circular_dependency_risk  - blocked_without_reason  - stale_task_candidate  - registry_out_of_date  - drift_detected  - script_failed
```

---

## 10. Output format

Return exactly:

```
# SOURCE AVAILABILITY LEDGER| source | available | used_for ||---|---:|---|# FILE: .claude/skills/apex-sync/SKILL.md```markdown<complete file content>
```

# FILE: .claude/skills/apex-sync/references/sync-cluster-contract.md

```
<complete file content>
```

...repeat for every package file...

# FILE: apex-meta/scripts/apex_sync.py

```
<complete file content>
```

# VALIDATION REPORT

```
validation:  required_mapping_source_used: true  decisions_md_used_if_available: true  no_web_search: true  no_repo_write: true  consolidated_python_script_generated: true  no_bash_or_typescript_or_javascript_generated: true  standard_library_only_python: true  status_enum_preserved: true  depends_on_preserved: true  script_read_only_by_default: true  registry_is_only_allowed_write: true  apex_plan_boundary_preserved: true  apex_session_boundary_preserved: true  skill_best_practice_structure_followed: true
```

```
No commentary before the source ledger.No commentary after the validation report.
```