# GPT-5.5 Pro Thinking Prompt — Final Canonical Creation of `apex-session` Skill Package

You are GPT-5.5 Pro Thinking working in the Apex2Claude2 project and/or the connected repo:

```txt
leela-spec/apexai-os-meta
```

Your task is to create the **final canonical, fully harmonized, repo-ready `apex-session` skill package** as complete file contents.

This is not a proposal.  
This is not a draft.  
This is not a research pass.  
This is not a package-readiness audit.  
This is not architecture rediscovery.  
This is not broad repo exploration.  
This is not `apex-plan`.  
This is not `apex-sync`.  
This is not a repo-write task.

You are creating the final version that should replace the current rough `apex-session` scaffold, using the accumulated Apex harmonization context, verified blueprint files, Claude skill best practices, and locked H1–H7 decisions.

---

## 0. Execution mode lock

```yaml
execution_mode:
  mode: FINAL_PACKAGE_CONTENT_OUTPUT_ONLY
  reason: >
    This expensive Pro Thinking run should create the final canonical package
    coherently in one logic pass. Repo writing is delegated to a later
    extended-thinking application flow that writes one file at a time, fetches
    back each file, and validates the final repo state.

repo_write_policy_for_this_run:
  write_repo_files: false
  create_branch: false
  create_pr: false
  update_files: false
  generate_complete_final_files: true
  output_copy_paste_ready_files: true
  do_not_call_output_proposal: true
```

Do not write to the repo in this run even if repo write tools are available.  
Do not include patch hunks.  
Do not include partial file fragments.  
Output the complete final contents for every target file.

---

## 1. Formatting warning

Do not copy malformed formatting examples from prior prompts or project resources.

All generated files must use valid multiline Markdown and YAML.

Especially avoid this invalid pattern:

```txt
---name: apex-sessiondescription: > ...
```

The correct `SKILL.md` frontmatter pattern is:

```yaml
---
name: apex-session
description: >
  Multiline description here.
---
```

All YAML blocks must use real line breaks and indentation.  
All Markdown headings must be separated by blank lines.  
All code fences must be balanced.

---

## 2. Final mission

Create the final package contents for:

```txt
.claude/skills/apex-session/
```

The package must fully implement the `C_SESSION` cluster as a Claude-native skill package.

`apex-session` must:

1. Consume Apex task/session evidence, handoff notes, raw sources, prior handoff files, and operator instructions.
2. Produce final H6 handoff/session artifacts:
   - `task_plan.md`
   - `findings.md`
   - `progress.md`
   - `next-session.md`
3. Extract state deltas from the current session.
4. Maintain entity update records at the instruction/contract level.
5. Perform gated status mutation logic using H1 status values.
6. Preserve raw source references and unresolved context.
7. Feed the planning layer with clean next-session context.
8. Keep deterministic scoring, registry rebuild, blocker scan, drift detection, and next-task ranking out of scope.

The result must be internally consistent enough to be used as the final package version without another generation pass.

---

## 3. Mandatory anti-regression rule

Do not “verschlimmbessern.”

Preserve all safeguards from the prior prompt design:

```yaml
must_preserve:
  - final package creation framing
  - exact blueprint source touch gate
  - exact local repo paths for blueprint files
  - no public web browsing
  - no architecture rediscovery
  - no apex-plan generation
  - no apex-sync generation
  - no scripts generated for apex-session
  - no ranking behavior inside apex-session
  - no blocker scan behavior inside apex-session
  - no registry rebuild behavior inside apex-session
  - no score computation inside apex-session
  - no malformed frontmatter
  - no collapsed single-line markdown or YAML
  - no missing source-basis map
  - no CrewAI overclaiming
  - no llm-wiki update-index overclaiming
  - no vague variable names
  - no handoff field drift
  - no direct repo writing in this run
```

---

## 4. Mandatory Blueprint Source Touch Gate

Before generating final files, open/read the exact required sources.

Do not compose the package from memory, prior summaries, or generic skill best practices alone.

```yaml
blueprint_source_touch_gate:
  required: true
  pass_condition:
    - each required phase/control file is opened or explicitly marked unavailable
    - each required blueprint repo file is opened or explicitly marked unavailable
    - every generated package file maps to concrete source files
  fail_condition:
    - package content is created without opening blueprint files
    - source summaries are used instead of actual blueprint files
    - unavailable sources are silently treated as source-backed
    - generic Claude skill advice replaces Apex-specific contracts
  failure_output:
    status: SOURCE_ACCESS_BLOCKED
    include:
      - missing_path
      - why_required
      - package_files_blocked
      - safest_next_action
```

If a required source cannot be opened, do not silently continue.  
Either stop with `SOURCE_ACCESS_BLOCKED`, or explicitly downgrade the affected source to unavailable and explain which final package files remain safe.

---

## 5. Authority hierarchy

Use this authority order:

```yaml
authority_hierarchy:
  tier_0_current_operator_instruction:
    role: highest_authority
    binding_update: >
      This is final package creation, not a proposal. The output must be the
      final package content, not a plan to generate it later.

  tier_1_phase_pack_and_locks:
    role: binding_generation_constraints
    files:
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/00_Apex_Phase_Pack_Meta_Index.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 1 — Authority Extraction.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 2 — URL orLabel to Local Repo Path Map v01.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 3 — File-Read Ledger v0.1.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 4 — Mechanism Ledger by Source v0.1.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 5 — Process Coverage Gate v0.1.md
      - FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 6 — PM2 Control Audit v0.1.md
      - Phase 7 Package Readiness.txt

  tier_2_existing_repo_scaffold:
    role: rough_existing_package_to_replace_or_upgrade
    files:
      - .claude/skills/apex-session/SKILL.md
      - .claude/skills/apex-session/package-manifest.md
    rule: >
      Use these only as repo-state context and continuity evidence. Do not
      preserve weak wording or scaffold gaps if stronger harmonized package
      logic is available.

  tier_3_blueprint_repo_files:
    role: concrete_mechanism_sources
    files:
      - source-knowledge/ProjectRepos/planning-with-files-master/.kiro/skills/planning-with-files/SKILL.md
      - source-knowledge/ProjectRepos/planning-with-files-master/docs/quickstart.md
      - source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts
      - source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/markdown/parser.ts
      - source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/backlog/tasks/back-200 - Add-Claude-Code-integration-with-workflow-commands-during-init.md
      - source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md
      - source-knowledge/ProjectRepos/crewAI-main/lib/crewai/src/crewai/task.py

  tier_4_claude_skill_best_practices:
    role: package_format_and_description_quality
    files:
      - Apex_Alfred_Skill_Definition_Guide.md
      - chatgpt_extended_thinking_skill_process_file_flow.md
      - chatgpt_extended_thinking_skill_process_source_index.md
```

If a path differs, search inside project resources or the connected repo only.  
Do not browse public web.  
Do not use public GitHub.  
Do not infer a file exists until opened/read.

---

## 6. Locked Apex decisions

Preserve these exactly.

```yaml
H1_status_enum:
  - open
  - in-progress
  - blocked
  - done
  - deferred

H2_paths:
  state_root: apex-meta/
  harmonization_root: apex-meta/harmonization/
  epics_root: apex-meta/epics/
  handoff_root: apex-meta/handoff/
  registry_root: apex-meta/registry/
  scripts_root: scripts/
  skills_root: .claude/skills/

H3_dependency_field:
  name: depends_on
  type: int_array
  rule: all_depends_on_items_must_be_done_before_actionable

H4_script_language:
  language: Python only
  apex_session_package_rule: no_scripts_in_this_package

H5_C_SESSION_cluster:
  owns:
    - PM6_update_status
    - KB1_write_session_progress
    - KB2_extract_state_deltas
    - KB3_maintain_entity_files
    - KB6_produce_next_session_context
    - PD5_operator_validation_for_mutation
    - PD6_feed_planning_layer
  boundary_note:
    - PD3_unlock_depth_context_can_be_recorded_but_not_computed

H6_handoff_format:
  files:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  next_session_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions

H7_priority_urgency:
  priority:
    high: 3
    medium: 2
    low: 1
  urgency: due_date_days_until_due_or_999
  apex_session_rule: may_record_inputs_but_must_not_compute_final_rank
```

---

## 7. Package responsibility contract

`apex-session` owns:

```yaml
apex_session_owns:
  - session_progress_artifacts
  - status_mutation_gate
  - status_change_validation_against_H1
  - before_after_change_preview
  - operator_validation_record
  - state_delta_extraction
  - entity_update_records
  - raw_source_reference_preservation
  - handoff_packet_generation
  - next_session_context_generation
  - planning_layer_feed
```

`apex-session` must not own:

```yaml
apex_session_must_not_own:
  - new_project_capture
  - new_project_decomposition
  - dependency_graph_scoring
  - exact_next_task_ranking
  - blocker_scan
  - stale_detection
  - registry_rebuild
  - drift_detection
  - priority_score_computation
  - urgency_score_computation
  - unlock_depth_computation
  - script_execution
  - calendar_operations
  - public_web_research
```

Cross-package routing:

```yaml
cross_package_routing:
  apex-plan:
    owns:
      - project/task capture
      - decomposition
      - dependency proposals
      - planning packet creation

  apex-sync:
    owns:
      - next action computation
      - blocker detection
      - registry rebuild
      - drift detection
      - scoring
      - exact focus candidate reports
      - deterministic Python reports

  apex-session:
    owns:
      - session artifact creation
      - gated status mutation
      - before/after preview
      - handoff and next-session context
      - state deltas
      - operator validation
```

---

## 8. Exact final package file tree

Generate exactly these package files:

```txt
.claude/skills/apex-session/
  SKILL.md
  references/
    session-cluster-contract.md
    mutation-gate-rules.md
    state-delta-and-entity-rules.md
    handoff-and-next-session-contract.md
  templates/
    task_plan.md
    findings.md
    progress.md
    next-session.md
  package-manifest.md
```

Do not generate:

```txt
.claude/skills/apex-plan/
.claude/skills/apex-sync/
scripts/
apex-meta/scripts/
apex-meta/registry/
apex-meta/epics/
evals/
tests/
schemas/
```

Unless an existing `apex-session` package already contains extra files, report them in validation as extra repo-state files, but do not expand scope unless the operator explicitly asks.

---

## 9. Source-to-file construction map

Use this map. Do not rediscover the file set.

### 9.1 `SKILL.md`

Use:

```yaml
sources:
  - Phase 1 — Authority Extraction.md
  - Phase 5 — Process Coverage Gate v0.1.md
  - Phase 7 Package Readiness.txt
  - .claude/skills/apex-session/SKILL.md
  - planning-with-files SKILL.md
  - Backlog types/index.ts
  - CrewAI task.py substitute
  - Apex_Alfred_Skill_Definition_Guide.md
```

Must define:

```yaml
SKILL_md_required_content:
  - valid YAML frontmatter
  - concise routing description
  - objective
  - skill contract
  - accepted inputs
  - final outputs
  - supporting file navigation
  - numbered procedure
  - validation rules
  - failure modes
  - completion gate
```

Final frontmatter must be exactly this shape:

```yaml
---
name: apex-session
description: >
  Use this skill when the operator asks to update Apex session state, validate
  status changes, produce handoff files, extract state deltas, preserve raw
  source references, or prepare next-session context from task/session evidence.
  Produces final H6 session artifacts and gated mutation records. Does not rank
  tasks, scan blockers, rebuild registries, compute scores, run scripts, or
  decompose new work.
---
```

### 9.2 `references/session-cluster-contract.md`

Use:

```yaml
sources:
  - Phase 1 — Authority Extraction.md
  - Phase 5 — Process Coverage Gate v0.1.md
  - Phase 7 Package Readiness.txt
  - .claude/skills/apex-session/SKILL.md
  - .claude/skills/apex-session/package-manifest.md
```

Must define:

```yaml
required_sections:
  - package_role
  - C_SESSION_process_scope
  - owned_processes
  - excluded_processes
  - cross_package_routing
  - PD3_unlock_depth_boundary
  - script_and_write_exclusions
  - final_acceptance_invariants
```

### 9.3 `references/mutation-gate-rules.md`

Use:

```yaml
sources:
  - Backlog types/index.ts
  - Backlog parser.ts
  - CrewAI task.py
  - Phase 5 — Process Coverage Gate v0.1.md
  - Phase 7 Package Readiness.txt
```

Must define:

```yaml
required_sections:
  - purpose
  - H1_status_validation
  - status_mutation_record_schema
  - before_after_preview_schema
  - operator_validation_record_schema
  - create_vs_update_distinction
  - confirmation_gate
  - invalid_mutation_rejection
  - final_mutation_output_contract
```

Required mutation wording:

```yaml
mutation_policy:
  final_package_behavior: >
    The skill creates final mutation records and handoff artifacts. It does not
    silently mutate repo files. Actual repo writes, if any, belong to a later
    explicit file-application flow.
```

CrewAI source label:

```yaml
CrewAI_task_py_SUBSTITUTE:
  allowed_claim: >
    substitute task-contract, human review, expected_output, guardrail,
    and output_file evidence
  forbidden_claim: original CrewAI getting-started skill source
```

### 9.4 `references/state-delta-and-entity-rules.md`

Use:

```yaml
sources:
  - Backlog types/index.ts
  - Backlog parser.ts
  - llm-wiki SKILL.md
  - Phase 4 — Mechanism Ledger by Source v0.1.md
  - Phase 5 — Process Coverage Gate v0.1.md
```

Must define:

```yaml
required_sections:
  - purpose
  - state_delta_summary_schema
  - entity_update_record_schema
  - raw_source_preservation_policy
  - raw_source_path_policy
  - source_conflict_policy
  - duplicate_entity_risk_policy
  - durable_findings_policy
  - planning_feed_policy
  - failure_modes
```

llm-wiki source label:

```yaml
llm_wiki:
  allowed_claim: conceptual/adapted source for raw/source/entity/index/audit discipline
  forbidden_claim: copied exact update-index.py behavior
```

### 9.5 `references/handoff-and-next-session-contract.md`

Use:

```yaml
sources:
  - Phase 1 — Authority Extraction.md
  - 00_Apex_Phase_Pack_Meta_Index.md
  - planning-with-files SKILL.md
  - planning-with-files docs/quickstart.md
```

Must define:

```yaml
required_sections:
  - H6_file_set
  - task_plan_contract
  - findings_contract
  - progress_contract
  - next_session_contract
  - required_next_session_sections
  - read_before_decide_rule
  - planning_layer_feed_contract
  - missing_context_behavior
  - final_handoff_acceptance_checks
```

### 9.6 Templates

Use:

```yaml
template_sources:
  - H6_handoff_format
  - planning-with-files SKILL.md
  - planning-with-files quickstart.md
```

Template requirements:

```yaml
templates:
  task_plan.md:
    exact_sections:
      - Goal
      - Current Step
      - Phases
      - Decisions
      - Open Items
      - Risks
      - Next Actions

  findings.md:
    exact_sections:
      - Durable Findings
      - Decisions Made
      - Source Notes
      - Open Questions
      - Operator Validations

  progress.md:
    exact_sections:
      - Session Log
      - Actions Taken
      - Status Mutations
      - State Deltas
      - Errors or Review Flags
      - Next Step

  next-session.md:
    exact_sections:
      - Current Step
      - Open Items
      - Risks
      - Decisions Made
      - Next Actions
```

### 9.7 `package-manifest.md`

Use:

```yaml
sources:
  - .claude/skills/apex-session/package-manifest.md
  - generated final package files
  - Phase 7 Package Readiness.txt
```

Must define:

```yaml
required_sections:
  - package_name
  - package_path
  - package_status
  - exact_file_index
  - file_purpose_map
  - source_basis_map
  - read_order
  - package_invariants
  - validation_checklist
  - forbidden_claims
```

Package status must be:

```yaml
package_status: final_canonical_v1
```

---

## 10. Variable and schema lock

Use these canonical names consistently.

```yaml
canonical_variables:
  task_id: task_id
  task_title: task_title
  status_before: status_before
  status_after: status_after
  allowed_status_values: allowed_status_values
  status_change_reason: status_change_reason
  operator_validation: operator_validation
  validation_status: validation_status
  validation_timestamp: validation_timestamp
  raw_source_ref: raw_source_ref
  raw_source_path: raw_source_path
  state_delta_id: state_delta_id
  entity_id: entity_id
  entity_update_type: entity_update_type
  source_conflict: source_conflict
  review_flags: review_flags
  next_session_context: next_session_context
  planning_feed: planning_feed
  depends_on: depends_on
```

Allowed status values:

```yaml
allowed_status_values:
  - open
  - in-progress
  - blocked
  - done
  - deferred
```

Operator validation values:

```yaml
operator_validation_values:
  - confirmed
  - rejected
  - needs_revision
  - not_requested
```

Review flag values:

```yaml
review_flag_values:
  - missing_input
  - invalid_status
  - source_conflict
  - duplicate_entity_risk
  - unresolved_dependency
  - scope_drift
  - operator_confirmation_missing
  - raw_source_missing
```

Do not invent alternate names such as:

```yaml
forbidden_variable_aliases:
  - previous_status
  - new_status
  - approval_state
  - source_pointer
  - next_context
  - task_dependencies
```

---

## 11. Final package behavior

The final package must behave like this:

```yaml
runtime_behavior:
  when_user_requests_session_update:
    - read provided task/session evidence
    - validate status values against H1
    - produce status_mutation_record
    - produce before_after_preview
    - produce operator_validation_record when mutation is consequential
    - generate H6 handoff artifacts

  when_user_requests_handoff:
    - produce task_plan.md
    - produce findings.md
    - produce progress.md
    - produce next-session.md
    - ensure next-session.md contains exact H6 sections

  when_user_provides_raw_sources:
    - preserve raw_source_ref
    - preserve raw_source_path when available
    - extract durable findings
    - create state_delta_summary
    - create entity_update_records if needed
    - flag conflicts instead of silently resolving them

  when_user_asks_for_ranking_or_sync:
    - route to apex-sync
    - do not compute ranking locally

  when_user_asks_for_new_decomposition:
    - route to apex-plan
```

---

## 12. Formatting gates

All final files must be valid Markdown with real line breaks.

```yaml
format_hard_gates:
  SKILL_md_valid_frontmatter: true
  frontmatter_opening_delimiter: "---"
  frontmatter_closing_delimiter: "---"
  no_single_line_collapsed_yaml: true
  no_single_line_collapsed_markdown: true
  headings_have_blank_lines: true
  code_fences_are_balanced: true
  no_source_citation_markup_inside_generated_files: true
  no_unresolved_template_placeholders_except_USER_INPUT_REQUIRED: true
```

The package must not repeat the previous malformed Pro-output failure where frontmatter collapsed into one line.

---

## 13. Final validation gates

After generation, run this self-validation visibly.

```yaml
final_validation_gates:
  file_count:
    expected: 10
    must_match: true

  package_tree:
    must_match_exact_tree: true

  H1_status_enum:
    exact_values_present: true
    no_extra_status_values: true

  H6_handoff:
    exact_file_names_present: true
    next_session_sections_exact: true

  boundaries:
    no_apex_plan_behavior: true
    no_apex_sync_behavior: true
    no_scripts: true
    no_ranking: true
    no_blocker_scan: true
    no_registry_rebuild: true
    no_score_computation: true
    no_repo_writes_claimed: true

  source_claims:
    no_CrewAI_getting_started_claim: true
    no_llm_wiki_update_index_claim: true
    no_OpenClaw_TaskFlow_claim: true
    no_Kanban_blocker_script_claim: true

  formatting:
    no_collapsed_files: true
    valid_frontmatter: true
```

If any gate fails, fix the final files before ending. Do not present a known-invalid final package.

---

## 14. Required final output structure

Output exactly this structure:

# Final `apex-session` Skill Package

## 1. Source Verification

| Source file | Opened/read? | Used for final files | Notes |
|---|---:|---|---|

## 2. Final Package Tree

```txt
.claude/skills/apex-session/
  SKILL.md
  references/
    session-cluster-contract.md
    mutation-gate-rules.md
    state-delta-and-entity-rules.md
    handoff-and-next-session-contract.md
  templates/
    task_plan.md
    findings.md
    progress.md
    next-session.md
  package-manifest.md
```

## 3. Final Files

### 3.1 `.claude/skills/apex-session/SKILL.md`

```markdown
<complete final file content>
```

### 3.2 `.claude/skills/apex-session/references/session-cluster-contract.md`

```markdown
<complete final file content>
```

### 3.3 `.claude/skills/apex-session/references/mutation-gate-rules.md`

```markdown
<complete final file content>
```

### 3.4 `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`

```markdown
<complete final file content>
```

### 3.5 `.claude/skills/apex-session/references/handoff-and-next-session-contract.md`

```markdown
<complete final file content>
```

### 3.6 `.claude/skills/apex-session/templates/task_plan.md`

```markdown
<complete final file content>
```

### 3.7 `.claude/skills/apex-session/templates/findings.md`

```markdown
<complete final file content>
```

### 3.8 `.claude/skills/apex-session/templates/progress.md`

```markdown
<complete final file content>
```

### 3.9 `.claude/skills/apex-session/templates/next-session.md`

```markdown
<complete final file content>
```

### 3.10 `.claude/skills/apex-session/package-manifest.md`

```markdown
<complete final file content>
```

## 4. Final Validation

```yaml
validation:
  package_status: final_canonical_v1
  exact_file_count: 10
  exact_tree_match: true
  H1_status_enum_preserved: true
  H6_handoff_format_preserved: true
  no_apex_sync_scope_drift: true
  no_apex_plan_scope_drift: true
  no_scripts_generated: true
  no_repo_writes_claimed: true
  no_collapsed_markdown_or_yaml: true
  source_touch_gate_passed: true
```

## 5. Remaining Risks

Only list real unresolved risks. If none, write:

```txt
No known unresolved package risks after validation.
```

---

## 15. Forbidden final-answer behavior

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

## 16. Begin

Start with source verification.

Then create the final canonical `apex-session` package contents.