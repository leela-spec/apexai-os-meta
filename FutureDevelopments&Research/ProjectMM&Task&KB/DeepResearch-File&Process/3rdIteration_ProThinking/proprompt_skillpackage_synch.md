```
# GPT-5.5 Pro Thinking Prompt — Final Canonical Creation of `apex-sync` Skill PackageYou are GPT-5.5 Pro Thinking working in the Apex2Claude2 project and/or the connected repo:```txtleela-spec/apexai-os-meta
```

Your task is to create the **final canonical, fully harmonized, repo-ready `apex-sync` skill package** as complete canonical file contents.

This is not a proposal.  
This is not a draft.  
This is not a research pass.  
This is not a package-readiness audit.  
This is not architecture rediscovery.  
This is not broad repo exploration.  
This is not public web browsing.  
This is not `apex-plan`.  
This is not `apex-session`.  
This is not a repo-write task.

You are creating the final version that should replace the current rough `apex-sync` scaffold after the operator backs up the old files.

Do **not** generate `.final.md` variants.  
Do **not** write to the repo.  
Do **not** output patch hunks.  
Output the complete final contents for the canonical target files.

---

## 0. Execution mode lock

```
execution_mode:  mode: FINAL_PACKAGE_CONTENT_OUTPUT_ONLY  repo_writes: false  create_branch: false  create_pr: false  update_files: false  generate_complete_final_files: true  output_canonical_target_paths: true  output_backup_application_plan: true  do_not_call_output_proposal: true
```

The operator will later move old files into backup and place these final files into the canonical paths. Your job is to generate the final canonical contents only.

---

## 1. Sync Safety Capsule

This capsule is binding. Use it to prevent known `apex-sync` failure modes.

```
sync_safety_capsule:  package_name: apex-sync  package_status: final_canonical_v1  package_path: .claude/skills/apex-sync/  canonical_script_path: scripts/apex_sync.py  prior_script_path_to_migrate_from:    - apex-meta/scripts/apex_sync.py  path_drift_do_not_copy:    - apex-meta/scripts/    - apex-meta/scripts/apex_sync.py  final_target_paths:    - .claude/skills/apex-sync/SKILL.md    - .claude/skills/apex-sync/references/sync-cluster-contract.md    - .claude/skills/apex-sync/references/script-command-contract.md    - .claude/skills/apex-sync/references/registry-and-drift-rules.md    - .claude/skills/apex-sync/references/scoring-and-focus-rules.md    - .claude/skills/apex-sync/package-manifest.md    - scripts/apex_sync.py  backup_policy:    create_backup_before_application: true    backup_location_recommendation: apex-meta/harmonization/backups/apex-sync-pre-final-YYYY-MM-DD/    this_run_creates_backup: false
```

### 1.1 Package role

```
B_SYNC_role:  cluster: B_SYNC  role: deterministic_read_side_synchronization  execution_model: skill_entrypoint_plus_standard_library_python_script
```

`apex-sync` owns:

```
apex_sync_owns:  - PM4_compute_next_action  - PM5_detect_blockers  - PM7_detect_stall  - PM8_generate_work_registry  - KB4_rebuild_index  - KB5_detect_drift  - PD1_compute_priority_score  - PD2_compute_urgency_score  - PD3_compute_unlock_depth  - PD4_compute_focus_candidates
```

`apex-sync` must not own:

```
apex_sync_must_not_own:  - PM1_project_capture  - PM2_human_decomposition  - PM6_status_mutation  - KB1_session_narrative  - KB2_state_delta_interpretation  - KB3_entity_synthesis  - KB6_next_session_authoring  - PD5_operator_validation  - PD6_planning_feed_authoring
```

### 1.2 Script policy

```
script_policy:  python_only: true  standard_library_only: true  bash_forbidden: true  typescript_forbidden: true  javascript_forbidden: true  shell_out_forbidden: true  external_dependencies_forbidden: true
```

### 1.3 Write policy

```
write_policy:  default_mode: dry_run  task_file_mutation: forbidden  handoff_file_mutation: forbidden  skill_file_mutation: forbidden  registry_write_allowed_only_for: apex-meta/registry/index.md  registry_write_requires:    - registry_subcommand    - explicit_non_dry_run_false
```

### 1.4 Missing-source policy

The following sources were previously referenced but are not available at the expected paths. Do not treat them as source-backed implementation files.

```
unavailable_or_unverified_sources:  llm_wiki_update_index_py:    expected_old_path: source-knowledge/ProjectRepos/llm-wiki-main/scripts/update-index.py    status: unavailable_at_expected_path    allowed_use: none    replacement_basis:      - llm-wiki SKILL.md conceptual raw/index/audit discipline      - custom Apex Python implementation    forbidden_claim: copied_llm_wiki_update_index_py  kanban_show_blocked_script:    expected_old_path: source-knowledge/ProjectRepos/kanban-skill-master/skills/kanban-ai/scripts/show_blocked.sh    status: unavailable_at_expected_path    allowed_use: none    replacement_basis:      - H1/H3 Apex dependency/status rules      - CCPM script-first tracking concept      - existing Apex apex_sync.py behavior      - custom Apex Python implementation    forbidden_claim: copied_kanban_blocker_script
```

Custom Apex Python is required for:

```
custom_Apex_Python_required_for:  - blocker_report  - stall_report  - registry_report  - drift_report  - unlock_depth
```

Forbidden claims:

```
forbidden_claims:  - copied_llm_wiki_update_index_py  - copied_kanban_blocker_script  - copied_OpenClaw_TaskFlow  - fully_source_backed_B_SYNC_without_custom_python  - copied_bash_script_behavior_as_python_without_adaptation
```

---

## 2. Locked Apex decisions

Use H1–H7 exactly.

```
H1_status_enum:  - open  - in-progress  - blocked  - done  - deferredH2_paths:  state_root: apex-meta/  harmonization_root: apex-meta/harmonization/  epics_root: apex-meta/epics/  handoff_root: apex-meta/handoff/  registry_root: apex-meta/registry/  scripts_root: scripts/  skills_root: .claude/skills/H3_dependency_field:  name: depends_on  type: int_array  rule: all_depends_on_items_must_be_done_before_actionableH4_script_language:  language: Python onlyH5_B_SYNC_cluster:  owns:    - PM4_compute_next_action    - PM5_detect_blockers    - PM7_detect_stall    - PM8_generate_work_registry    - KB4_rebuild_index    - KB5_detect_drift    - PD1_compute_priority_score    - PD2_compute_urgency_score    - PD3_compute_unlock_depth    - PD4_compute_focus_candidatesH6_handoff_format:  files:    - task_plan.md    - findings.md    - progress.md    - next-session.md  apex_sync_rule: may_read_context_if needed but must_not_author_or_mutate_handoffH7_priority_urgency:  priority:    high: 3    medium: 2    low: 1  urgency: due_date_days_until_due_or_999
```

---

## 3. Mandatory source touch gate

Before generating final files, open/read or explicitly mark unavailable:

```
required_sources:  repo_locks_and_scaffold:    - apex-meta/harmonization/decisions.md    - .claude/skills/apex-sync/SKILL.md    - .claude/skills/apex-sync/package-manifest.md    - apex-meta/scripts/apex_sync.py  concrete_blueprint_sources:    - source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/SKILL.md    - source-knowledge/ProjectRepos/ccpm-main/skill/ccpm/references/track.md    - source-knowledge/ProjectRepos/claude-task-master-main/scripts/modules/task-manager/find-next-task.js    - source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts    - source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/markdown/parser.ts    - source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md  skill_format_guidance:    - Apex_Alfred_Skill_Definition_Guide.md
```

If a required path differs, search only inside project resources or the connected repo. Do not browse public web.

If a source is unavailable, mark it unavailable and apply the missing-source policy. Do not silently treat unavailable sources as source-backed.

---

## 4. Source treatment map

Use this exact source treatment map.

```
source_treatment_map:  apex_meta_scripts_apex_sync_py:    treatment: MIGRATE_AND_REWRITE    use_for:      - existing Apex CLI behavior      - parser behavior      - H1 status validation      - report subcommands      - dry_run behavior      - registry write restriction    required_change:      - move canonical final script path to scripts/apex_sync.py      - remove apex-meta/scripts as final script root  ccpm_SKILL_md_and_track_md:    treatment: ADAPT    use_for:      - script-first deterministic reporting principle      - tracking command categories      - failure behavior when script output needs interpretation    required_change:      - adapt bash scripts to Python-only Apex script  task_master_find_next_task_js:    treatment: ADAPT    use_for:      - dependency-satisfied candidate filtering      - priority weighting      - dependency-count tie break      - deterministic next action logic    required_change:      - adapt JavaScript to Python      - normalize statuses to H1 only      - normalize dependency field to depends_on  backlog_types_and_parser:    treatment: ADAPT    use_for:      - task fields      - dependencies      - priority      - parent/subtask concepts      - raw content preservation      - Markdown/frontmatter parsing concepts    required_change:      - adapt to Apex file layout and H1/H3 locks  llm_wiki_SKILL_md:    treatment: CONCEPT_ONLY    use_for:      - index discipline      - raw/source/audit discipline      - do-not-silently-ignore audit or drift concept    forbidden_use:      - do not claim copied update-index.py behavior  unavailable_kanban_blocker_script:    treatment: OMIT_AS_SOURCE    replacement:      - custom Apex Python blocker logic      - H1/H3 dependency/status semantics
```

---

## 5. Final target tree

Generate exactly these final canonical files:

```
.claude/skills/apex-sync/  SKILL.md  references/    sync-cluster-contract.md    script-command-contract.md    registry-and-drift-rules.md    scoring-and-focus-rules.md  package-manifest.mdscripts/  apex_sync.py
```

Do not generate:

```
.claude/skills/apex-plan/.claude/skills/apex-session/.claude/skills/apex-sync/*.final.mdapex-meta/scripts/apex_sync.pytests/evals/schemas/extra guidance files
```

---

## 6. Required file responsibilities

### 6.1 `.claude/skills/apex-sync/SKILL.md`

Must contain:

```
required_content:  - valid YAML frontmatter  - concise routing description  - objective  - accepted inputs  - required outputs  - supporting file navigation  - numbered procedure  - validation rules  - failure modes  - completion gate  - canonical command policy pointing to python scripts/apex_sync.py
```

Final frontmatter must use this shape:

```
---name: apex-syncdescription: >  Use this skill when the operator asks to compute deterministic Apex read-side  synchronization reports: next actions, blockers, stale tasks, registry  rebuild previews, drift checks, dependency validation, priority, urgency,  unlock depth, or focus candidates. Uses `scripts/apex_sync.py`. Does not  capture projects, decompose work, mutate task status, author handoff files,  validate operator decisions, or write session narrative.---
```

### 6.2 `references/sync-cluster-contract.md`

Must define:

```
required_sections:  - package_role  - B_SYNC_process_scope  - owned_processes  - excluded_processes  - cross_package_routing  - read_side_only_policy  - registry_write_exception  - custom_python_caveats  - final_acceptance_invariants
```

### 6.3 `references/script-command-contract.md`

Must define:

```
required_sections:  - canonical_command  - global_flags  - subcommands  - next_command_contract  - blockers_command_contract  - registry_command_contract  - stall_command_contract  - drift_command_contract  - score_command_contract  - exit_code_policy  - json_output_policy  - dry_run_policy  - no_shell_out_policy
```

Canonical command:

```
python scripts/apex_sync.py <subcommand> --root . --json --dry-run true
```

Required subcommands:

```
subcommands:  - next  - blockers  - registry  - stall  - drift  - score
```

### 6.4 `references/registry-and-drift-rules.md`

Must define:

```
required_sections:  - purpose  - task_file_discovery  - task_frontmatter_validation  - registry_schema  - registry_rebuild_rules  - drift_detection_rules  - malformed_task_file_policy  - dry_run_default  - explicit_non_dry_run_write_gate  - only_allowed_write_path  - final_registry_report_contract
```

Only allowed write path:

```
apex-meta/registry/index.md
```

### 6.5 `references/scoring-and-focus-rules.md`

Must define:

```
required_sections:  - purpose  - H7_priority_score  - H7_urgency_score  - dependency_satisfied_actionability  - blocker_semantics  - stale_task_semantics  - unlock_depth_policy  - focus_candidate_sort_policy  - score_report_schema  - focus_candidate_report_schema  - no_planning_recommendation_boundary
```

### 6.6 `package-manifest.md`

Must define:

```
required_sections:  - package_name  - package_path  - package_status  - exact_file_index  - file_purpose_map  - source_basis_map  - read_order  - package_invariants  - validation_checklist  - forbidden_claims  - backup_and_application_notes
```

Package status:

```
package_status: final_canonical_v1
```

### 6.7 `scripts/apex_sync.py`

Must be a complete Python script.

Requirements:

```
script_requirements:  language: Python  standard_library_only: true  no_shell_out: true  no_external_dependencies: true  canonical_path: scripts/apex_sync.py  reads:    - apex-meta/epics/*/[0-9][0-9][0-9].md  may_write_only:    - apex-meta/registry/index.md  write_requires:    - subcommand == registry    - explicit --dry-run false  must_parse:    - YAML-like frontmatter    - Markdown body    - task id    - task title    - status    - priority    - due_date    - depends_on    - blocked_by    - updated_date or created_date when available  must_validate:    - H1 status enum    - duplicate task ids    - missing task ids    - missing dependency targets    - circular dependency risk    - blocked tasks without blocker reason    - malformed frontmatter  must_compute:    - next_action_report    - blocker_report    - registry_report    - stall_report    - drift_report    - score_report    - focus_candidate_report    - dependency_validation_report  output_modes:    - human readable default    - JSON with --json  required_review_flags:    - malformed_frontmatter    - missing_task_id    - duplicate_task_id    - unsupported_status    - missing_dependency_target    - circular_dependency_risk    - blocked_without_reason    - stale_task_candidate    - registry_out_of_date    - drift_detected    - script_failed
```

---

## 7. Canonical report contracts

Use these report names exactly:

```
required_reports:  - next_action_report  - blocker_report  - registry_report  - stall_report  - drift_report  - score_report  - focus_candidate_report  - dependency_validation_report
```

Every JSON report must include:

```
required_report_fields:  - report_name  - generated_at  - dry_run  - root  - script_exit_code  - review_flags
```

---

## 8. Formatting gates

All generated Markdown files must be valid Markdown with real line breaks.

```
format_hard_gates:  SKILL_md_valid_frontmatter: true  no_single_line_collapsed_yaml: true  no_single_line_collapsed_markdown: true  headings_have_blank_lines: true  code_fences_are_balanced: true  no_source_citation_markup_inside_generated_files: true  no_unresolved_template_placeholders_except_USER_INPUT_REQUIRED: true
```

The final package must not repeat collapsed YAML or one-line Markdown failures.

---

## 9. Backup and application plan

Do not perform repo writes. But include this plan in the final output:

```
backup_application_plan:  before_overwrite:    backup_current_files_to: apex-meta/harmonization/backups/apex-sync-pre-final-YYYY-MM-DD/  backup_these_if_present:    - .claude/skills/apex-sync/SKILL.md    - .claude/skills/apex-sync/package-manifest.md    - .claude/skills/apex-sync/references/sync-cluster-contract.md    - .claude/skills/apex-sync/references/script-command-contract.md    - .claude/skills/apex-sync/references/registry-and-drift-rules.md    - .claude/skills/apex-sync/references/scoring-and-focus-rules.md    - apex-meta/scripts/apex_sync.py  then_write:    - .claude/skills/apex-sync/SKILL.md    - .claude/skills/apex-sync/references/sync-cluster-contract.md    - .claude/skills/apex-sync/references/script-command-contract.md    - .claude/skills/apex-sync/references/registry-and-drift-rules.md    - .claude/skills/apex-sync/references/scoring-and-focus-rules.md    - .claude/skills/apex-sync/package-manifest.md    - scripts/apex_sync.py  after_write:    - fetch back every written file    - validate no collapsed YAML or Markdown    - validate script path is scripts/apex_sync.py    - validate no active references to apex-meta/scripts/apex_sync.py remain except backup notes    - optionally delete old apex-meta/scripts/apex_sync.py after successful migration
```

---

## 10. Final validation gates

After generation, visibly self-validate:

```
final_validation_gates:  exact_file_count:    expected: 7    must_match: true  package_tree:    must_match_exact_tree: true  script_path:    canonical_path_is_scripts_apex_sync_py: true    no_final_script_under_apex_meta_scripts: true  H1_status_enum:    exact_values_present: true    no_extra_status_values: true  H3_dependency_field:    depends_on_used: true    dependencies_alias_not_used_as_canonical: true  boundaries:    no_apex_plan_behavior: true    no_apex_session_behavior: true    no_task_status_mutation: true    no_handoff_authoring: true    no_operator_validation_claim: true  source_claims:    no_llm_wiki_update_index_py_copy_claim: true    no_kanban_blocker_script_copy_claim: true    custom_Apex_Python_caveats_present: true  formatting:    no_collapsed_files: true    valid_frontmatter: true  script:    standard_library_only: true    no_shell_out: true    dry_run_default: true    registry_write_gate_present: true
```

If any gate fails, fix the final files before ending. Do not present a known-invalid final package.

---

## 11. Required final output structure

Output exactly this structure:

# Final `apex-sync` Skill Package

## 1. Source Verification

|Source file|Opened/read?|Used for final files|Source treatment|Notes|
|---|---|---|---|---|

## 2. Final Package Tree

```
.claude/skills/apex-sync/  SKILL.md  references/    sync-cluster-contract.md    script-command-contract.md    registry-and-drift-rules.md    scoring-and-focus-rules.md  package-manifest.mdscripts/  apex_sync.py
```

## 3. Backup and Application Plan

```
<complete backup and application plan>
```

## 4. Final Files

### 4.1 `.claude/skills/apex-sync/SKILL.md`

```
<complete final file content>
```

### 4.2 `.claude/skills/apex-sync/references/sync-cluster-contract.md`

```
<complete final file content>
```

### 4.3 `.claude/skills/apex-sync/references/script-command-contract.md`

```
<complete final file content>
```

### 4.4 `.claude/skills/apex-sync/references/registry-and-drift-rules.md`

```
<complete final file content>
```

### 4.5 `.claude/skills/apex-sync/references/scoring-and-focus-rules.md`

```
<complete final file content>
```

### 4.6 `.claude/skills/apex-sync/package-manifest.md`

```
<complete final file content>
```

### 4.7 `scripts/apex_sync.py`

```
<complete final file content>
```

## 5. Final Validation

```
validation:  package_status: final_canonical_v1  exact_file_count: 7  exact_tree_match: true  canonical_script_path: scripts/apex_sync.py  no_final_md_variants: true  no_apex_meta_scripts_final_path: true  H1_status_enum_preserved: true  H3_depends_on_preserved: true  no_apex_plan_scope_drift: true  no_apex_session_scope_drift: true  no_task_status_mutation: true  no_handoff_authoring: true  no_operator_validation_claim: true  no_llm_wiki_update_index_copy_claim: true  no_kanban_blocker_script_copy_claim: true  custom_Apex_Python_caveats_present: true  no_collapsed_markdown_or_yaml: true  source_touch_gate_passed: true
```

## 6. Remaining Risks

Only list real unresolved risks. If none, write:

```
No known unresolved package risks after validation.
```

---

## 12. Forbidden final-answer behavior

Do not end with:

- “This is a proposal”
- “This is a draft”
- “You may want to…”
- “Further design is needed”
- “I assumed the schema”
- “I could not verify sources but generated anyway”

If blocked, say exactly what is blocked.  
If not blocked, deliver the final package.

---

## 13. Begin

Start with source verification.

Then create the final canonical `apex-sync` package contents.