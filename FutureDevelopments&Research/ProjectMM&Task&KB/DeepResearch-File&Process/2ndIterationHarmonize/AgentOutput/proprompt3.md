```
# APEX PM/KB/PD — Generate Canonical `apex-session` Skill Package v2# Model target: GPT-5.5 Pro Thinking# Mode: accepted-mapping application, not research# Output mode: chat-output file blocks only---## 0. MissionYou are a Claude-native skill package author.Generate the complete canonical `.claude/skills/apex-session/` package from the accepted Apex PM/KB/PD ProThinking mapping.You are not researching architecture.You are not redesigning Apex.You are not writing to GitHub.You are not cloning repositories.You are not validating unrelated existing skill folders.You are not using web search.You are not reading public GitHub source repos.You are not generating scripts.`apex-session` is the session, mutation, KB/entity, operator-validation, and handoff package. It owns status mutation proposals, explicit write gates, progress logging, state-delta extraction, entity maintenance, next-session context, and planning-layer feed.---## 1. Execution modeThis prompt supports two environments.```yamlexecution_modes:  local_repo_mode:    description: >      The model has access to the local repo, likely at      C:\GitDev\apexai-os-meta or an equivalent current working directory.    preferred_optional_files:      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\decisions.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\field-schema.md      - C:\GitDev\apexai-os-meta\apex-meta\harmonization\task-template.md  upload_only_mode:    description: >      The model only has uploaded/project files such as      ProThinkingGPT_Harmonization_v1.md and skill best-practice guides.    behavior: >      Continue from ProThinking extracted evidence and available guidance.      Do not treat missing local repo files as blockers.  output_mode:    repo_write_mode: disabled    git_commit_mode: disabled    confirm_gate_mode_for_prompt_execution: not_applicable    output: complete_file_blocks_only
```

Operator confirmation gates must be represented inside the generated skill content, not used as this prompt’s execution workflow.

---

## 2. Authority hierarchy

Use this hierarchy.

```
authority_order:  required:    - ProThinkingGPT_Harmonization_v1.md  preferred_if_available:    - apex-meta/harmonization/decisions.md    - APEX HARMONIZATION — AGENT MODE INIT DOCUMENT_v2.md    - Apex_Harmonization_NextChat_Handover_and_ProPrompts.md    - Claude_Skill_Package_BestPractice_Handover.md    - Claude_Skill_PromptFlow_Design_Guidance_v1.md  optional_do_not_search_for_if_missing:    - apex-meta/harmonization/field-schema.md    - apex-meta/harmonization/task-template.md  do_not_read_by_default:    - source-knowledge/ProjectRepos/    - .claude/skills/AIRouting/    - .claude/skills/Workflow&Processes/    - .claude/skills/PrecapNextDay/    - .claude/skills/project-kb-manager/    - ApexDefinition&OldVersions/  reason_for_not_reading_source_repos: >    ProThinkingGPT_Harmonization_v1.md already extracted and validated the    evidence for planning-with-files, llm-wiki, Backlog.md, CrewAI guardrails,    and Task Master dependency logic. Rereading source repos is token waste    unless the operator requests an audit.
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
binding_decisions:  target_package:    name: apex-session    path: .claude/skills/apex-session/  durable_paths:    base: apex-meta/    epics: apex-meta/epics/    registry: apex-meta/registry/index.md    handoff: apex-meta/handoff/    entities: apex-meta/entities/    raw: apex-meta/raw/  status_enum:    - open    - in-progress    - blocked    - done    - deferred  dependency_field:    name: depends_on    type: integer_array    rule: all_depended_task_ids_must_have_status_done_before_task_is_actionable  script_policy:    scripts_generated_by_this_prompt: false    deterministic_script_requests_go_to: apex-sync  handoff_format:    files:      - task_plan.md      - findings.md      - progress.md      - next-session.md    next_session_sections:      - Current Step      - Open Items      - Risks      - Decisions Made      - Next Actions  mutation_gate:    all_mutations_require_explicit_operator_confirmation: true    accepted_confirm_tokens:      - CONFIRM      - CONFIRM WRITE      - CONFIRM MUTATION  package_process_scope:    owns:      - PM6_update_status      - KB1_write_session_progress      - KB2_extract_state_deltas      - KB3_maintain_entity_files      - KB6_produce_next_session_context      - PD5_validate_with_operator      - PD6_feed_planning_layer    coordinates_with_apex_sync:      - PM7_stall_flags      - KB4_index_rebuild      - KB5_drift_flags      - PD3_unlock_depth    coordinates_with_apex_plan:      - PM1_project_capture      - PM2_decomposition      - PM3_dependency_proposals      - PD4_focus_rationale
```

---

## 5. ProThinking mapping to preserve

Use the report mapping. Do not invent new clusters.

```
mapping_to_preserve:  natural_clusters:    session_memory_and_handoff:      primary_home: apex-session      secondary_home: apex-sync      package_role:        - task_plan        - findings        - progress        - next_session_context        - session_recovery_surface    knowledge_entity_maintenance:      primary_home: apex-session      secondary_home: apex-sync      package_role:        - raw_source_preservation        - entity_file_update_proposal        - concept_or_project_record_update        - index_rebuild_request    governance_and_validation:      primary_home: apex-session      package_role:        - explicit_operator_gate        - before_after_mutation_preview        - review_flags        - mutation_audit_note    intake_and_task_contract:      primary_home: apex-plan      secondary_home: apex-session      package_role:        - operator_confirmed_status_update        - state_delta_capture
```

---

## 6. Files to generate

Generate exactly these files.

```
files_to_generate:  - .claude/skills/apex-session/SKILL.md  - .claude/skills/apex-session/references/session-cluster-contract.md  - .claude/skills/apex-session/references/mutation-gate-rules.md  - .claude/skills/apex-session/references/state-delta-and-entity-rules.md  - .claude/skills/apex-session/references/handoff-and-next-session-contract.md  - .claude/skills/apex-session/templates/task_plan.md  - .claude/skills/apex-session/templates/findings.md  - .claude/skills/apex-session/templates/progress.md  - .claude/skills/apex-session/templates/next-session.md  - .claude/skills/apex-session/package-manifest.md
```

Do not generate scripts. Do not generate repo-write instructions.

---

## 7. SKILL.md requirements

`SKILL.md` must follow this section order:

```
skill_md_sections:  1: yaml_frontmatter  2: "# Apex Session"  3: "## Skill Contract"  4: "## Supporting Files"  5: "## Procedure"  6: "## Failure Modes"  7: "## Output Requirements"  8: "## Completion Gate"
```

Frontmatter:

```
frontmatter:  allowed_fields_only:    - name    - description  name: apex-session  description_must_begin_with: "Use this skill when"  max_words: 80
```

Supporting files must be a YAML block with `path` and `read_when`. Failure modes must be a YAML block where each mode has exactly `trigger` and `correction`.

---

## 8. Package content requirements

The package must include:

```
required_outputs:  - status_mutation_proposal  - before_after_mutation_preview  - session_progress_log  - state_delta_summary  - entity_update_proposal  - next_session_context  - planning_layer_feed  - operator_validation_resulthandoff_files:  task_plan.md:    role: current_session_plan_and_phase_tracking  findings.md:    role: durable_discoveries_and_decisions  progress.md:    role: append_only_session_activity_log  next-session.md:    role: context_bootstrap_for_next_sessionnext_session_required_sections:  - Current Step  - Open Items  - Risks  - Decisions Made  - Next Actionsmutation_targets:  - apex-meta/epics/<slug>/<NNN>.md  - apex-meta/entities/*.md  - apex-meta/handoff/task_plan.md  - apex-meta/handoff/findings.md  - apex-meta/handoff/progress.md  - apex-meta/handoff/next-session.mdentity_policy:  raw_sources_path: apex-meta/raw/  raw_sources_rule: preserve_raw_sources_do_not_rewrite  entity_files_path: apex-meta/entities/  entity_update_rule: update_only_after_operator_confirmation  index_rebuild_owner: apex-syncoperator_review_flags:  - missing_confirmation  - ambiguous_status_delta  - unsupported_status_value  - entity_update_uncertain  - duplicate_entity_risk  - raw_source_missing  - planning_feed_incomplete  - sync_required_before_final_context  - conflict_between_sources
```

---

## 9. Output format

Return exactly:

```
# SOURCE AVAILABILITY LEDGER| source | available | used_for ||---|---:|---|# FILE: .claude/skills/apex-session/SKILL.md```markdown<complete file content>
```

# FILE: .claude/skills/apex-session/references/session-cluster-contract.md

```
<complete file content>
```

...repeat for every file...

# VALIDATION REPORT

```
validation:  required_mapping_source_used: true  decisions_md_used_if_available: true  no_web_search: true  no_repo_write: true  no_scripts_generated: true  status_enum_preserved: true  depends_on_preserved: true  handoff_format_preserved: true  mutation_gate_required: true  raw_source_preservation_policy_present: true  apex_plan_boundary_preserved: true  apex_sync_boundary_preserved: true  skill_best_practice_structure_followed: true
```

```
No commentary before the source ledger.No commentary after the validation report.
```