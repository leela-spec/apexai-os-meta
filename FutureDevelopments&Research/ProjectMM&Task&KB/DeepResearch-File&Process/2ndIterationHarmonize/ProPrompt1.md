```
# APEX PM/KB/PD — Generate Canonical `apex-plan` Skill Package v2# Model target: GPT-5.5 Pro Thinking# Mode: accepted-mapping application, not research# Output mode: chat-output file blocks only---## 0. MissionYou are a Claude-native skill package author.Generate the complete canonical `.claude/skills/apex-plan/` package from the accepted Apex PM/KB/PD ProThinking mapping.You are not researching architecture.You are not redesigning Apex.You are not writing to GitHub.You are not cloning repositories.You are not validating unrelated existing skill folders.You are not using web search.You are not reading public GitHub source repos.`apex-plan` is the no-script planning package. It owns project/task intake, decomposition, dependency proposal, priority/urgency/focus rationale, and operator-gated planning outputs. It does not compute deterministic next-task ranking, traverse dependency graphs, scan blockers, rebuild registries, or mutate session/KB state.---## 1. Execution modeThis prompt supports two environments.```yamlexecution_modes:  local_repo_mode:    description: >      The model has access to the local repo, likely at      C:\GitDev\apexai-os-meta or an equivalent current working directory.    preferred_optional_files:      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\decisions.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\field-schema.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\task-template.md  upload_only_mode:    description: >      The model only has uploaded/project files such as      ProThinkingGPT_Harmonization_v1.md and skill best-practice guides.    behavior: >      Continue from ProThinking extracted evidence and available guidance.      Do not treat missing local repo files as blockers.  output_mode:    repo_write_mode: disabled    git_commit_mode: disabled    confirm_gate_mode_for_prompt_execution: not_applicable    output: complete_file_blocks_only
```

Operator confirmation gates must be represented inside the generated skill content, not used as a step in this chat-output run.

---

## 2. Authority hierarchy

Use this hierarchy.

```
authority_order:  required:    - ProThinkingGPT_Harmonization_v1.md  preferred_if_available:    - apex-meta/harmonization/decisions.md    - APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md    - Apex_Harmonization_NextChat_Handover_and_ProPrompts.md    - Claude_Skill_Package_BestPractice_Handover.md    - Claude_Skill_PromptFlow_Design_Guidance_v1.md  optional_do_not_search_for_if_missing:    - apex-meta/harmonization/field-schema.md    - apex-meta/harmonization/task-template.md  do_not_read_by_default:    - source-knowledge/ProjectRepos/    - .claude/skills/AIRouting/    - .claude/skills/Workflow&Processes/    - .claude/skills/PrecapNextDay/    - .claude/skills/project-kb-manager/    - ApexDefinition&OldVersions/  reason_for_not_reading_source_repos: >    ProThinkingGPT_Harmonization_v1.md already extracted and validated the    public implementation evidence. Rereading repo-local source repos is token    waste unless the operator explicitly requests a second evidence audit.
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
binding_decisions:  target_package:    name: apex-plan    path: .claude/skills/apex-plan/  durable_paths:    base: apex-meta/    harmonization: apex-meta/harmonization/    epics: apex-meta/epics/    registry: apex-meta/registry/index.md    handoff: apex-meta/handoff/  status_enum:    - open    - in-progress    - blocked    - done    - deferred  dependency_field:    name: depends_on    type: integer_array    rule: all_depended_task_ids_must_have_status_done_before_task_is_actionable  script_policy:    scripts_allowed: false    bash_allowed: false    python_allowed: false  priority_policy:    values:      high: 3      medium: 2      low: 1  urgency_policy:    field: due_date    computation_owner: apex-sync    rule_for_apex_plan: >      Apex Plan records due_date and explains urgency qualitatively.      It must not perform deterministic urgency ranking.  package_process_scope:    owns:      - PM1_capture_project      - PM2_decompose_project      - PM3_assign_dependency_proposals      - PD1_priority_policy      - PD2_urgency_policy      - PD4_focus_recommendation_rationale    must_handoff_to_apex_sync:      - exact_next_task_computation      - dependency_graph_traversal      - blocker_scan      - registry_rebuild      - drift_detection      - exact_priority_urgency_unlock_sorting    must_handoff_to_apex_session:      - status_mutation      - entity_update      - session_progress_log      - next_session_context      - operator_confirmed_write
```

---

## 5. ProThinking mapping to preserve

Use the report mapping. Do not invent new clusters.

```
mapping_to_preserve:  natural_clusters:    intake_and_task_contract:      primary_home: apex-plan      package_role: project_capture_and_task_record_contracts    decomposition_and_dependency_engine:      primary_home: apex-plan      secondary_home: apex-sync      package_role: decomposition_and_dependency_proposal_only    product_scoring_and_recommendation:      primary_home: apex-plan      secondary_home: apex-sync      package_role: qualitative_rationale_and_policy_only    governance_and_validation:      primary_home: apex-session      package_role_in_apex_plan: review_flags_and_handoff_requests
```

---

## 6. Files to generate

Generate exactly these files.

```
files_to_generate:  - .claude/skills/apex-plan/SKILL.md  - .claude/skills/apex-plan/references/plan-cluster-contract.md  - .claude/skills/apex-plan/references/task-record-contract.md  - .claude/skills/apex-plan/references/decomposition-and-dependency-rules.md  - .claude/skills/apex-plan/references/priority-urgency-focus-policy.md  - .claude/skills/apex-plan/templates/epic-template.md  - .claude/skills/apex-plan/templates/task-template.md  - .claude/skills/apex-plan/package-manifest.md
```

Do not generate scripts. Do not generate repo-write instructions.

---

## 7. SKILL.md requirements

`SKILL.md` must follow this section order:

```
skill_md_sections:  1: yaml_frontmatter  2: "# Apex Plan"  3: "## Skill Contract"  4: "## Supporting Files"  5: "## Procedure"  6: "## Failure Modes"  7: "## Output Requirements"  8: "## Completion Gate"
```

Frontmatter:

```
frontmatter:  allowed_fields_only:    - name    - description  name: apex-plan  description_must_begin_with: "Use this skill when"  max_words: 80
```

Supporting files must be a YAML block with `path` and `read_when`. Failure modes must be a YAML block where each mode has exactly `trigger` and `correction`.

---

## 8. Package content requirements

The package must include:

```
required_contracts:  project_capture_record:    purpose: capture project goal, scope, constraints, source, and review flags  epic_record:    purpose: define a project-level work container under apex-meta/epics/<slug>/  task_record:    required_fields:      - id      - title      - status      - priority      - due_date      - depends_on      - blocked_by      - acceptance_criteria      - definition_of_done      - notes      - source  dependency_plan:    rules:      - use depends_on      - detect obvious circular_dependency_risk      - mark dependency uncertainty for apex-sync validation      - do not compute graph traversal  priority_urgency_focus_policy:    rules:      - priority is high_medium_low      - due_date is recorded for urgency      - exact urgency score belongs to apex-sync      - focus recommendation from apex-plan is provisional  handoff_requests:    to_apex_sync:      - validate_dependencies      - compute_next_action      - scan_blockers      - rebuild_registry      - compute_focus_candidates    to_apex_session:      - request_status_mutation      - request_operator_confirmed_write      - request_session_handoff_update
```

---

## 9. Output format

Return exactly:

```
# SOURCE AVAILABILITY LEDGER| source | available | used_for ||---|---:|---|# FILE: .claude/skills/apex-plan/SKILL.md```markdown<complete file content>
```

# FILE: .claude/skills/apex-plan/references/plan-cluster-contract.md

```
<complete file content>
```

...repeat for every file...

# VALIDATION REPORT

```
validation:  required_mapping_source_used: true  decisions_md_used_if_available: true  no_web_search: true  no_repo_write: true  no_scripts_generated: true  status_enum_preserved: true  depends_on_preserved: true  apex_plan_does_not_compute_deterministic_rankings: true  apex_sync_handoff_boundary_present: true  apex_session_handoff_boundary_present: true  skill_best_practice_structure_followed: true
```

```
No commentary before the source ledger.No commentary after the validation report.
```