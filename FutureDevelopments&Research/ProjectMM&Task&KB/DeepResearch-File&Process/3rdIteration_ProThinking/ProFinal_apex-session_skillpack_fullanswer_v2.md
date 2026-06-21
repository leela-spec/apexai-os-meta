# Final `apex-session` Skill Package

## 1. Source Verification

|Source file|Opened/read?|Used for final files|Notes|
|---|--:|---|---|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/00_Apex_Phase_Pack_Meta_Index.md`|Yes|`package-manifest.md`, `handoff-and-next-session-contract.md`|Confirmed phase chain, evidence-gated generation model, and target packages.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 1 — Authority Extraction.md`|Yes|All files|Confirmed H1–H7 locks, C_SESSION cluster ownership, and source selections.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 2 — URL orLabel to Local Repo Path Map v01.md`|Yes|`package-manifest.md`, source labeling rules|Confirmed corrected local blueprint paths and substitute labels.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 3 — File-Read Ledger v0.1.md`|Yes|`source_basis_map`, all reference files|Confirmed resolved source families and carried missing sources.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 4 — Mechanism Ledger by Source v0.1.md`|Yes|All reference files|Confirmed planning-with-files, Backlog, llm-wiki, and CrewAI substitute mechanisms.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 5 — Process Coverage Gate v0.1.md`|Yes|`session-cluster-contract.md`, `mutation-gate-rules.md`, `state-delta-and-entity-rules.md`|Confirmed PM6, KB1, KB2, KB3, KB6, PD5, and PD6 coverage; confirmed C_SESSION readiness with one custom PD3 boundary.|
|`FutureDevelopments&Research/ProjectMM&Task&KB/DeepResearch-File&Process/3rdIteration_ProThinking/Preps/Phase 6 — PM2 Control Audit v0.1.md`|Yes|`mutation-gate-rules.md`, source labeling|Confirmed CrewAI `task.py` substitute and Backlog mutation model evidence.|
|`Phase 7 Package Readiness.txt` and repo `Phase 7 — Package Readiness Gate v0.1.md`|Yes|All files, especially scope exclusions|Opened local exact uploaded file and repo gate. Confirmed `apex-session` is safe for handoff/session/mutation-gate generation and must not overclaim graph logic.|
|`.claude/skills/apex-session/SKILL.md`|Yes|`SKILL.md`, `session-cluster-contract.md`, `package-manifest.md`|Existing scaffold used as continuity evidence only; stronger final contract replaces it.|
|`.claude/skills/apex-session/package-manifest.md`|Yes|`package-manifest.md`, file index|Existing manifest confirms current rough file index and boundaries.|
|`source-knowledge/ProjectRepos/planning-with-files-master/.kiro/skills/planning-with-files/SKILL.md`|Yes|`SKILL.md`, `handoff-and-next-session-contract.md`, templates|Confirmed task plan/findings/progress pattern, read-before-decide, and update-after-act rules.|
|`source-knowledge/ProjectRepos/planning-with-files-master/docs/quickstart.md`|Yes|`handoff-and-next-session-contract.md`, templates|Confirmed three planning files and handoff pattern for long-running topics.|
|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/types/index.ts`|Yes|`mutation-gate-rules.md`, `state-delta-and-entity-rules.md`|Confirmed task fields, update input, dependencies, priority, raw content, AC, DoD, and comments.|
|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/src/markdown/parser.ts`|Yes|`mutation-gate-rules.md`, `state-delta-and-entity-rules.md`|Confirmed frontmatter/body parsing, priority validation, raw content preservation, and dependency mapping.|
|`source-knowledge/ProjectRepos/backlog-main/Backlog.md-main/backlog/tasks/back-200 - Add-Claude-Code-integration-with-workflow-commands-during-init.md`|Yes|`mutation-gate-rules.md`, task evidence pattern|Confirmed concrete Markdown task record with frontmatter, dependencies, priority, description, and acceptance criteria.|
|`source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`|Yes|`state-delta-and-entity-rules.md`, `package-manifest.md`|Confirmed raw/source/entity/audit discipline; not used as exact `update-index.py` evidence.|
|`source-knowledge/ProjectRepos/crewAI-main/lib/crewai/src/crewai/task.py`|Yes|`mutation-gate-rules.md`, `state-delta-and-entity-rules.md`|Confirmed substitute evidence for description, expected output, output file, context, guardrails, input files, and human review.|
|`Apex_Alfred_Skill_Definition_Guide.md`|Yes|`SKILL.md`, `package-manifest.md`|Opened/read from mounted project files; used for valid skill frontmatter, compact entrypoint, objective/procedure split, and supporting-reference structure.|
|`chatgpt_extended_thinking_skill_process_file_flow.md`|Yes|`package-manifest.md`, generation boundaries|Opened/read from mounted project files; used for Claude-only skill/process file boundaries and no-runtime-output discipline.|
|`chatgpt_extended_thinking_skill_process_source_index.md`|Yes|`package-manifest.md`, source translation policy|Opened/read from mounted project files; used for source-routing and no source-citation markup inside generated files.|

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

# Apex Session

## Objective

`apex-session` converts current task/session evidence into final H6 handoff artifacts, gated status mutation records, state delta summaries, entity update records, and clean next-session context. It reads operator instructions, task evidence, handoff notes, raw source references, prior session material, and unresolved context. It validates all status movement against the H1 status enum and records operator validation before treating consequential mutations as confirmed. It preserves raw source references and unresolved context instead of silently rewriting or resolving them. It does not rank tasks, scan blockers, rebuild registries, compute scores, run scripts, perform calendar work, or decompose new work.

## Skill Contract

~~~yaml
skill_contract:
  package_name: apex-session
  cluster: C_SESSION
  package_path: ".claude/skills/apex-session/"
  primary_role: session_artifact_creation_and_gated_mutation_records

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

  final_handoff_files:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md

  allowed_status_values:
    - open
    - in-progress
    - blocked
    - done
    - deferred

  operator_validation_values:
    - confirmed
    - rejected
    - needs_revision
    - not_requested

  review_flag_values:
    - missing_input
    - invalid_status
    - source_conflict
    - duplicate_entity_risk
    - unresolved_dependency
    - scope_drift
    - operator_confirmation_missing
    - raw_source_missing
~~~

## Accepted Inputs

~~~yaml
accepted_inputs:
  task_evidence:
    - task_id
    - task_title
    - status_before
    - status_after
    - status_change_reason
    - depends_on
    - raw_source_ref
    - raw_source_path

  session_evidence:
    - operator_instructions
    - handoff_notes
    - prior_task_plan
    - prior_findings
    - prior_progress
    - prior_next_session_context
    - raw_sources
    - unresolved_context

  mutation_inputs:
    - requested_status_change
    - requested_entity_update
    - operator_validation
    - validation_timestamp

  planning_feed_inputs:
    - current_step
    - open_items
    - risks
    - decisions_made
    - next_actions
~~~

## Final Outputs

~~~yaml
final_outputs:
  mutation_records:
    - status_mutation_record
    - before_after_preview
    - operator_validation_record

  session_records:
    - state_delta_summary
    - entity_update_record
    - planning_feed
    - next_session_context

  H6_handoff_artifacts:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
~~~

## Supporting File Navigation

Read these supporting files only when their rules are needed:

~~~yaml
supporting_files:
  references/session-cluster-contract.md:
    read_when:
      - validating_C_SESSION_scope
      - routing_apex_plan_or_apex_sync_requests
      - checking_final_acceptance_invariants

  references/mutation-gate-rules.md:
    read_when:
      - validating_status_after
      - creating_status_mutation_record
      - creating_before_after_preview
      - creating_operator_validation_record

  references/state-delta-and-entity-rules.md:
    read_when:
      - extracting_state_delta_summary
      - maintaining_entity_update_records
      - preserving_raw_source_ref
      - flagging_source_conflict_or_duplicate_entity_risk

  references/handoff-and-next-session-contract.md:
    read_when:
      - producing_task_plan_md
      - producing_findings_md
      - producing_progress_md
      - producing_next_session_md
      - creating_planning_feed

  templates/task_plan.md:
    read_when:
      - creating_or_refreshing_task_plan_md

  templates/findings.md:
    read_when:
      - creating_or_refreshing_findings_md

  templates/progress.md:
    read_when:
      - creating_or_refreshing_progress_md

  templates/next-session.md:
    read_when:
      - creating_or_refreshing_next_session_md

  package-manifest.md:
    read_when:
      - validating_package_inventory
      - checking_source_basis_map
      - checking_package_invariants
~~~

## Procedure

1. **Classify the request.** Decide whether the operator is asking for session update, handoff creation, state delta extraction, entity update records, status mutation validation, or next-session context. If the request asks for new decomposition, route to `apex-plan`. If it asks for ranking, blocker scan, registry rebuild, drift detection, stale detection, or score computation, route to `apex-sync`.

2. **Read before deciding.** Inspect the provided task/session evidence, prior H6 files, raw source references, handoff notes, and operator instructions before drafting any final artifact. Preserve missing or unresolved context as explicit review flags instead of filling gaps from memory.

3. **Preserve source basis.** Carry every available `raw_source_ref` and `raw_source_path` into the relevant state delta, entity update, findings, or progress entry. If raw source evidence is expected but absent, set `review_flags` to include `raw_source_missing`.

4. **Validate status values.** For every requested status change, check `status_before` and `status_after` against the exact H1 enum: `open`, `in-progress`, `blocked`, `done`, `deferred`. Reject any other task status value with `review_flags: [invalid_status]`.

5. **Create mutation records.** For each valid status change, create a `status_mutation_record` and a `before_after_preview` using the schemas in `references/mutation-gate-rules.md`. Include `status_change_reason`, `operator_validation`, `validation_status`, and `validation_timestamp`.

6. **Apply the operator validation gate.** Consequential mutations must have `operator_validation: confirmed` before they are treated as confirmed records. If validation is missing, rejected, or needs revision, keep the record visible but not confirmed and add the appropriate review flag.

7. **Extract state deltas.** Convert session evidence into `state_delta_summary` records. Capture what changed, what remained unresolved, which raw sources support the change, and whether any `source_conflict` exists.

8. **Maintain entity update records.** Create `entity_update_record` entries when the session reveals durable changes to projects, tasks, artifacts, concepts, people, tools, or source references. Flag `duplicate_entity_risk` or `source_conflict` instead of silently merging uncertain entities.

9. **Produce H6 handoff artifacts.** Generate or refresh the final artifact set: `task_plan.md`, `findings.md`, `progress.md`, and `next-session.md`. Ensure `next-session.md` contains exactly these sections: Current Step, Open Items, Risks, Decisions Made, Next Actions.

10. **Create planning feed.** Produce `planning_feed` as clean input for the planning layer. Include next-session context, durable findings, open items, risks, decisions made, raw source references, and review flags. Do not compute final rank or exact focus candidate.

11. **Validate completion.** Check the final outputs against the validation rules below and the package manifest. If any gate fails, revise the affected file content before returning the result.

## Validation Rules

~~~yaml
validation_rules:
  status_validation:
    allowed_status_values_exact:
      - open
      - in-progress
      - blocked
      - done
      - deferred
    reject_extra_status_values: true

  handoff_validation:
    required_files:
      - task_plan.md
      - findings.md
      - progress.md
      - next-session.md
    next_session_sections_exact:
      - Current Step
      - Open Items
      - Risks
      - Decisions Made
      - Next Actions

  mutation_validation:
    before_after_preview_required: true
    operator_validation_record_required: true
    status_change_reason_required: true
    silent_repo_mutation_allowed: false

  source_validation:
    raw_source_ref_preserved_when_available: true
    raw_source_path_preserved_when_available: true
    unresolved_context_preserved: true
    source_conflict_flagged_not_silently_resolved: true

  boundary_validation:
    no_new_project_decomposition: true
    no_dependency_graph_scoring: true
    no_exact_next_task_ranking: true
    no_blocker_scan: true
    no_stale_detection: true
    no_registry_rebuild: true
    no_drift_detection: true
    no_priority_score_computation: true
    no_urgency_score_computation: true
    no_unlock_depth_computation: true
    no_script_execution: true
    no_calendar_operations: true
    no_public_web_research: true
~~~

## Failure Modes

~~~yaml
failure_modes:
  missing_input:
    trigger: required task/session evidence is absent
    response: add missing_input to review_flags and preserve the gap in Open Items

  invalid_status:
    trigger: status_before or status_after is outside H1
    response: reject the status mutation record and list allowed_status_values

  source_conflict:
    trigger: two or more sources disagree on a state delta or entity update
    response: preserve both raw_source_ref values and add source_conflict to review_flags

  duplicate_entity_risk:
    trigger: an entity update may duplicate an existing entity_id
    response: create an entity_update_record with duplicate_entity_risk and require operator validation

  unresolved_dependency:
    trigger: depends_on contains unresolved or not-done dependencies relevant to actionability
    response: record the dependency issue but do not compute ranking or unlock depth

  scope_drift:
    trigger: request enters apex-plan or apex-sync responsibility
    response: route the scoped part to the correct package and continue only with apex-session work

  operator_confirmation_missing:
    trigger: consequential mutation lacks operator_validation confirmed
    response: keep the mutation record unconfirmed and add operator_confirmation_missing

  raw_source_missing:
    trigger: state delta or entity update lacks raw_source_ref or raw_source_path where expected
    response: keep the record visible and add raw_source_missing
~~~

## Completion Gate

~~~yaml
completion_gate:
  package_scope_is_C_SESSION_only: true
  status_values_match_H1_exactly: true
  mutation_records_include_before_after_preview: true
  operator_validation_record_present_for_consequential_mutations: true
  raw_source_ref_and_raw_source_path_preserved_when_available: true
  state_delta_summary_present_when_session_evidence_changes_state: true
  entity_update_records_present_when_durable_entities_change: true
  H6_handoff_files_present: true
  next_session_sections_exact: true
  planning_feed_present_when_requested: true
  apex_plan_behavior_absent: true
  apex_sync_behavior_absent: true
  scripts_absent: true
  repo_writes_not_silently_performed: true
~~~
```

### 3.2 `.claude/skills/apex-session/references/session-cluster-contract.md`

```markdown
# Session Cluster Contract

## package_role

~~~yaml
package_role:
  package_name: apex-session
  package_path: ".claude/skills/apex-session/"
  cluster: C_SESSION
  role: >
    Produce final Apex session artifacts, gated mutation records, state deltas,
    entity update records, and planning-layer handoff context from current
    task/session evidence.

  primary_outputs:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
    - status_mutation_record
    - before_after_preview
    - operator_validation_record
    - state_delta_summary
    - entity_update_record
    - planning_feed

  storage_roots:
    state_root: apex-meta/
    harmonization_root: apex-meta/harmonization/
    epics_root: apex-meta/epics/
    handoff_root: apex-meta/handoff/
    registry_root: apex-meta/registry/
    scripts_root: scripts/
    skills_root: .claude/skills/
~~~

`apex-session` is the C_SESSION package. It converts active session evidence into final handoff material and validated mutation records. It does not create new project plans, compute exact next actions, rebuild registries, or execute scripts.

## C_SESSION_process_scope

~~~yaml
C_SESSION_process_scope:
  cluster_name: C_SESSION
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

  status_enum_H1:
    - open
    - in-progress
    - blocked
    - done
    - deferred

  handoff_format_H6:
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
~~~

## owned_processes

~~~yaml
owned_processes:
  PM6_update_status:
    responsibility: >
      Validate and record requested status changes using H1 status values,
      before_after_preview, and operator_validation_record.
    required_outputs:
      - status_mutation_record
      - before_after_preview
      - operator_validation_record

  KB1_write_session_progress:
    responsibility: >
      Produce or update progress-oriented session artifacts that log actions
      taken, status mutations, state deltas, errors, and review flags.
    required_outputs:
      - progress.md

  KB2_extract_state_deltas:
    responsibility: >
      Extract durable changes from session evidence, preserve raw source basis,
      and flag unresolved context or source conflicts.
    required_outputs:
      - state_delta_summary

  KB3_maintain_entity_files:
    responsibility: >
      Create entity update records for durable changes to tasks, projects,
      artifacts, concepts, people, tools, or sources.
    required_outputs:
      - entity_update_record

  KB6_produce_next_session_context:
    responsibility: >
      Produce next-session context that preserves Current Step, Open Items,
      Risks, Decisions Made, and Next Actions.
    required_outputs:
      - next-session.md
      - next_session_context

  PD5_operator_validation_for_mutation:
    responsibility: >
      Require operator validation for consequential status or entity changes
      before treating mutation records as confirmed.
    required_outputs:
      - operator_validation_record

  PD6_feed_planning_layer:
    responsibility: >
      Prepare clean planning_feed material for apex-plan without computing
      ranking, blocker state, registry state, scores, or new decomposition.
    required_outputs:
      - planning_feed
~~~

## excluded_processes

~~~yaml
excluded_processes:
  new_project_capture:
    route_to: apex-plan
  new_project_decomposition:
    route_to: apex-plan
  dependency_graph_scoring:
    route_to: apex-sync
  exact_next_task_ranking:
    route_to: apex-sync
  blocker_scan:
    route_to: apex-sync
  stale_detection:
    route_to: apex-sync
  registry_rebuild:
    route_to: apex-sync
  drift_detection:
    route_to: apex-sync
  priority_score_computation:
    route_to: apex-sync
  urgency_score_computation:
    route_to: apex-sync
  unlock_depth_computation:
    route_to: apex-sync_or_later_custom_helper
  script_execution:
    route_to: apex-sync_or_external_application_flow
  calendar_operations:
    route_to: out_of_scope
  public_web_research:
    route_to: out_of_scope
~~~

## cross_package_routing

~~~yaml
cross_package_routing:
  apex-plan:
    owns:
      - project_task_capture
      - project_decomposition
      - dependency_proposals
      - planning_packet_creation
    apex-session_may_send:
      - planning_feed
      - next_session_context
      - durable_findings
      - review_flags
      - unresolved_context

  apex-sync:
    owns:
      - next_action_computation
      - blocker_detection
      - registry_rebuild
      - drift_detection
      - scoring
      - exact_focus_candidate_reports
      - deterministic_Python_reports
    apex-session_may_send:
      - status_mutation_record
      - state_delta_summary
      - depends_on_context
      - raw_source_ref
      - raw_source_path
      - review_flags

  apex-session:
    owns:
      - session_artifact_creation
      - gated_status_mutation
      - before_after_preview
      - handoff_and_next_session_context
      - state_deltas
      - operator_validation
~~~

## PD3_unlock_depth_boundary

~~~yaml
PD3_unlock_depth_boundary:
  H5_owner: C_SESSION
  package_rule: >
    apex-session may record dependency context and unresolved dependency review
    flags, but it must not compute reverse unlock depth, dependency graph
    scores, final next-task ranking, or exact focus candidate reports.

  allowed:
    - preserve_depends_on_values
    - record_unresolved_dependency
    - record_dependency_context_from_operator
    - include_dependency_context_in_planning_feed

  forbidden:
    - compute_unlock_depth
    - rank_tasks_by_unlock_depth
    - scan_entire_dependency_graph
    - compute_final_focus_score
    - claim_apex_sync_outputs
~~~

## script_and_write_exclusions

~~~yaml
script_and_write_exclusions:
  no_scripts_in_this_package: true
  no_script_execution: true
  no_public_web_research: true
  no_calendar_operations: true
  no_silent_repo_writes: true

  mutation_policy: >
    The package creates final mutation records and handoff artifacts. It does
    not silently mutate repo files. Actual repo writes, if any, belong to a
    later explicit file-application flow.

  allowed_this_package:
    - produce_copy_paste_ready_file_contents
    - produce_status_mutation_record
    - produce_before_after_preview
    - produce_operator_validation_record
    - produce_state_delta_summary
    - produce_entity_update_record
    - produce_H6_handoff_artifacts

  forbidden_this_package:
    - create_scripts
    - run_scripts
    - update_repo_files_without_explicit_application_flow
    - create_branch
    - create_pull_request
    - mutate_registry
~~~

## final_acceptance_invariants

~~~yaml
final_acceptance_invariants:
  package_is_C_SESSION_only: true
  H1_status_enum_preserved:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H6_handoff_file_set_preserved:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  source_references_preserved: true
  unresolved_context_preserved: true
  operator_validation_required_for_consequential_mutation: true
  apex_plan_scope_absent: true
  apex_sync_scope_absent: true
  scripts_absent: true
  malformed_frontmatter_absent: true
~~~
```

### 3.3 `.claude/skills/apex-session/references/mutation-gate-rules.md`

```markdown
# Mutation Gate Rules

## purpose

~~~yaml
purpose:
  file_role: status_mutation_and_operator_validation_contract
  package_name: apex-session
  goal: >
    Define how apex-session validates H1 status changes, creates mutation
    records, previews before/after state, records operator validation, and
    rejects invalid or unconfirmed mutations.

mutation_policy:
  final_package_behavior: >
    The skill creates final mutation records and handoff artifacts. It does not
    silently mutate repo files. Actual repo writes, if any, belong to a later
    explicit file-application flow.

CrewAI_task_py_SUBSTITUTE:
  allowed_claim: >
    substitute task-contract, human review, expected_output, guardrail,
    and output_file evidence
  forbidden_claim: original CrewAI getting-started skill source
~~~

## H1_status_validation

~~~yaml
H1_status_validation:
  allowed_status_values:
    - open
    - in-progress
    - blocked
    - done
    - deferred

  required_checks:
    - status_before_must_be_allowed_or_USER_INPUT_REQUIRED
    - status_after_must_be_allowed
    - status_after_must_not_use_extra_values
    - status_change_reason_must_be_present_for_consequential_mutation
    - depends_on_must_be_preserved_when_available

  invalid_status_response:
    validation_status: rejected
    review_flags:
      - invalid_status
    action: >
      Reject the mutation record as invalid, show allowed_status_values, and
      preserve the rejected request in progress.md or review flags.
~~~

## status_mutation_record_schema

~~~yaml
status_mutation_record_schema:
  required_fields:
    task_id: string
    task_title: string
    status_before:
      type: enum_or_USER_INPUT_REQUIRED
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_after:
      type: enum
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_change_reason: string
    operator_validation:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_status:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_timestamp: string_or_USER_INPUT_REQUIRED
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    review_flags:
      type: array
      allowed_values:
        - missing_input
        - invalid_status
        - source_conflict
        - duplicate_entity_risk
        - unresolved_dependency
        - scope_drift
        - operator_confirmation_missing
        - raw_source_missing

  optional_fields:
    depends_on:
      type: int_array
      rule: all_depends_on_items_must_be_done_before_actionable
    source_conflict: boolean
~~~

## before_after_preview_schema

~~~yaml
before_after_preview_schema:
  required_fields:
    task_id: string
    task_title: string
    status_before:
      type: enum_or_USER_INPUT_REQUIRED
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_after:
      type: enum
      allowed_status_values:
        - open
        - in-progress
        - blocked
        - done
        - deferred
    status_change_reason: string
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    review_flags: array

  preview_rules:
    - show_exact_field_before_and_after
    - include_raw_source_basis
    - include_unresolved_dependency_when_depends_on_blocks_actionability
    - include_operator_validation_requirement
    - do_not_apply_repo_write
~~~

## operator_validation_record_schema

~~~yaml
operator_validation_record_schema:
  required_fields:
    task_id: string
    task_title: string
    operator_validation:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_status:
      type: enum
      allowed_values:
        - confirmed
        - rejected
        - needs_revision
        - not_requested
    validation_timestamp: string_or_USER_INPUT_REQUIRED
    status_change_reason: string
    review_flags: array

  validation_rules:
    confirmed:
      effect: mutation_record_can_be_treated_as_confirmed
    rejected:
      effect: mutation_record_must_not_be_treated_as_confirmed
    needs_revision:
      effect: mutation_record_requires_revised_status_or_reason
    not_requested:
      effect: mutation_record_is_visible_but_not_confirmed
~~~

## create_vs_update_distinction

~~~yaml
create_vs_update_distinction:
  create_record:
    use_when:
      - task_id_is_new_or_unknown
      - entity_id_is_new_or_unknown
      - session_evidence_creates_new_state_delta_id
    required_action:
      - preserve_raw_source_ref
      - preserve_raw_source_path
      - mark_missing_input_if_identity_is_incomplete

  update_record:
    use_when:
      - task_id_exists
      - entity_id_exists
      - status_before_is_known_or_explicitly_marked_USER_INPUT_REQUIRED
    required_action:
      - preserve_status_before
      - preserve_status_after
      - include_before_after_preview
      - include_operator_validation_record

  shared_rule: >
    Create and update records are final records in the handoff package, but they
    are not silent repo mutations. A later explicit file-application flow may
    apply them to files after validation.
~~~

## confirmation_gate

~~~yaml
confirmation_gate:
  consequential_mutation_requires_operator_validation: true
  confirmed_value: confirmed

  consequential_mutation_examples:
    - status_after_changes_task_state
    - entity_update_record_changes_durable_entity_meaning
    - source_conflict_resolution_is_requested
    - duplicate_entity_risk_would_be_merged
    - raw_source_missing_would_be_ignored

  if_operator_validation_is_confirmed:
    validation_status: confirmed
    allowed_result: confirmed_mutation_record

  if_operator_validation_is_rejected:
    validation_status: rejected
    required_review_flags:
      - operator_confirmation_missing

  if_operator_validation_is_needs_revision:
    validation_status: needs_revision
    required_review_flags:
      - operator_confirmation_missing

  if_operator_validation_is_not_requested:
    validation_status: not_requested
    required_review_flags:
      - operator_confirmation_missing
~~~

## invalid_mutation_rejection

~~~yaml
invalid_mutation_rejection:
  reject_when:
    - status_after_not_in_H1
    - status_before_not_in_H1_and_not_marked_USER_INPUT_REQUIRED
    - task_id_missing
    - task_title_missing
    - status_change_reason_missing_for_consequential_mutation
    - raw_source_ref_missing_when_required
    - raw_source_path_missing_when_required
    - operator_validation_missing_for_consequential_mutation
    - requested_behavior_belongs_to_apex_plan
    - requested_behavior_belongs_to_apex_sync

  rejection_output:
    - rejected_status_mutation_record
    - before_after_preview_when_possible
    - review_flags
    - safest_valid_next_action_for_operator
~~~

## final_mutation_output_contract

~~~yaml
final_mutation_output_contract:
  required_outputs_when_status_change_requested:
    - status_mutation_record
    - before_after_preview
    - operator_validation_record

  required_outputs_when_mutation_is_confirmed:
    - validation_status_confirmed
    - validation_timestamp
    - raw_source_ref_or_raw_source_missing_flag
    - raw_source_path_or_raw_source_missing_flag

  required_outputs_when_mutation_is_not_confirmed:
    - validation_status_not_confirmed_value
    - review_flags
    - before_after_preview
    - reason_not_confirmed

  never_do:
    - silently_mutate_repo_files
    - invent_status_values
    - invent_operator_validation
    - suppress_source_conflict
    - suppress_duplicate_entity_risk
    - compute_final_task_rank
    - compute_blocker_report
    - rebuild_registry
~~~
```

### 3.4 `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`

```markdown
# State Delta and Entity Rules

## purpose

~~~yaml
purpose:
  file_role: state_delta_and_entity_update_contract
  package_name: apex-session
  goal: >
    Define how apex-session extracts state deltas from current session evidence,
    preserves raw source references, creates entity update records, flags source
    conflicts and duplicate entity risks, and prepares clean planning_feed
    material without computing final ranking or rebuilding indexes.

llm_wiki:
  allowed_claim: conceptual/adapted source for raw/source/entity/index/audit discipline
  forbidden_claim: copied exact update-index.py behavior
~~~

## state_delta_summary_schema

~~~yaml
state_delta_summary_schema:
  required_fields:
    state_delta_id: string
    task_id: string_or_USER_INPUT_REQUIRED
    task_title: string_or_USER_INPUT_REQUIRED
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    delta_summary: string
    affected_fields:
      type: array
      examples:
        - status_before
        - status_after
        - status_change_reason
        - depends_on
        - next_session_context
        - planning_feed
    source_conflict: boolean
    review_flags:
      type: array
      allowed_values:
        - missing_input
        - invalid_status
        - source_conflict
        - duplicate_entity_risk
        - unresolved_dependency
        - scope_drift
        - operator_confirmation_missing
        - raw_source_missing

  required_behavior:
    - preserve_raw_source_ref_when_available
    - preserve_raw_source_path_when_available
    - flag_missing_raw_source_instead_of_inventing
    - flag_source_conflict_instead_of_resolving_silently
    - preserve_unresolved_context_for_next_session
~~~

## entity_update_record_schema

~~~yaml
entity_update_record_schema:
  required_fields:
    entity_id: string_or_USER_INPUT_REQUIRED
    entity_update_type:
      type: enum_string
      allowed_examples:
        - create
        - update
        - split
        - merge_candidate
        - archive_candidate
        - reference_only
    entity_summary: string
    raw_source_ref: string_or_USER_INPUT_REQUIRED
    raw_source_path: string_or_USER_INPUT_REQUIRED
    source_conflict: boolean
    review_flags:
      type: array
      allowed_values:
        - missing_input
        - invalid_status
        - source_conflict
        - duplicate_entity_risk
        - unresolved_dependency
        - scope_drift
        - operator_confirmation_missing
        - raw_source_missing

  optional_fields:
    task_id: string
    task_title: string
    state_delta_id: string
    depends_on:
      type: int_array
      rule: all_depends_on_items_must_be_done_before_actionable
    planning_feed: string
    next_session_context: string
~~~

## raw_source_preservation_policy

~~~yaml
raw_source_preservation_policy:
  preserve_exact_references: true
  preserve_exact_paths: true
  never_rewrite_raw_source_content: true
  never_treat_missing_source_as_verified: true

  required_when_available:
    - raw_source_ref
    - raw_source_path

  when_missing:
    raw_source_ref: USER_INPUT_REQUIRED
    raw_source_path: USER_INPUT_REQUIRED
    review_flags:
      - raw_source_missing

  output_locations:
    - findings.md
    - progress.md
    - next-session.md
    - state_delta_summary
    - entity_update_record
    - planning_feed
~~~

## raw_source_path_policy

~~~yaml
raw_source_path_policy:
  accepted_path_forms:
    - repo_relative_path
    - local_project_path
    - operator_supplied_path
    - prior_handoff_path

  path_rules:
    - keep_original_spelling_and_spacing
    - do_not_normalize_without_recording_original
    - do_not_infer_file_existence_without_read_or_operator_basis
    - include_path_drift_or_missing_path_in_review_flags

  large_or_unavailable_source_behavior:
    - preserve_pointer_or_reference
    - summarize_available_evidence_only
    - mark_missing_input_if_required_content_is_unavailable
~~~

## source_conflict_policy

~~~yaml
source_conflict_policy:
  conflict_definition: >
    A source_conflict exists when two or more task/session/raw sources support
    incompatible state deltas, entity meanings, status values, or next actions.

  required_behavior:
    - preserve_each_conflicting_raw_source_ref
    - preserve_each_conflicting_raw_source_path_when_available
    - set_source_conflict_true
    - add_source_conflict_to_review_flags
    - record_conflict_in_findings_md
    - carry_conflict_into_next_session_md_open_items

  forbidden_behavior:
    - silently_choose_one_source
    - erase_conflicting_source
    - mark_conflict_resolved_without_operator_validation
    - compute_final_rank_to_break_conflict
~~~

## duplicate_entity_risk_policy

~~~yaml
duplicate_entity_risk_policy:
  risk_definition: >
    duplicate_entity_risk exists when the session evidence may describe an
    entity that already has a durable record under another entity_id or path.

  required_behavior:
    - set_duplicate_entity_risk_review_flag
    - preserve_possible_existing_entity_id_when_known
    - create_merge_candidate_or_reference_only_record
    - require_operator_validation_before_merge

  forbidden_behavior:
    - silently_merge_entities
    - silently_create_duplicate_entity
    - delete_entity_record
    - rewrite_raw_source_path_to_match_guess
~~~

## durable_findings_policy

~~~yaml
durable_findings_policy:
  durable_finding_definition: >
    A durable finding is a session observation that should influence future
    planning, validation, status mutation, entity maintenance, or handoff.

  write_to_findings_when:
    - decision_made
    - source_conflict_detected
    - durable_state_delta_extracted
    - raw_source_ref_or_path_is_important
    - operator_validation_record_changes_future_behavior
    - unresolved_context_should_survive_session

  findings_must_include:
    - concise_finding
    - raw_source_ref_or_raw_source_missing_flag
    - raw_source_path_or_raw_source_missing_flag
    - review_flags_when_relevant
~~~

## planning_feed_policy

~~~yaml
planning_feed_policy:
  planning_feed_role: >
    Provide apex-plan with clean next-session context, durable findings, open
    items, risks, decisions made, raw source references, and review flags.

  include:
    - next_session_context
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
    - durable_findings
    - raw_source_ref
    - raw_source_path
    - review_flags
    - unresolved_context

  exclude:
    - exact_next_task_ranking
    - blocker_scan_result
    - registry_rebuild_result
    - drift_detection_result
    - priority_score_computation
    - urgency_score_computation
    - unlock_depth_computation
~~~

## failure_modes

~~~yaml
failure_modes:
  missing_input:
    response: create_record_with_USER_INPUT_REQUIRED_and_review_flag
  raw_source_missing:
    response: preserve_delta_or_entity_update_but_mark_raw_source_missing
  source_conflict:
    response: preserve_all_sides_and_carry_to_next_session_open_items
  duplicate_entity_risk:
    response: create_merge_candidate_or_reference_only_record
  unresolved_dependency:
    response: preserve_depends_on_and_do_not_compute_unlock_depth
  scope_drift:
    response: route_exact_ranking_or_registry_or_decomposition_to_correct_package
~~~
```

### 3.5 `.claude/skills/apex-session/references/handoff-and-next-session-contract.md`

```markdown
# Handoff and Next Session Contract

## H6_file_set

~~~yaml
H6_file_set:
  handoff_root: apex-meta/handoff/
  required_files:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md

  next_session_required_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
~~~

The H6 handoff format is the final artifact contract for `apex-session`. The files capture the plan, durable findings, progress log, and clean continuation context needed by the next session or planning layer.

## task_plan_contract

~~~yaml
task_plan_contract:
  file_name: task_plan.md
  purpose: >
    Preserve the session goal, current step, phase structure, decisions, open
    items, risks, and next actions so the next session can resume without
    relying on chat memory.

  exact_sections:
    - Goal
    - Current Step
    - Phases
    - Decisions
    - Open Items
    - Risks
    - Next Actions

  required_behavior:
    - state_goal_in_operator_language
    - identify_current_step
    - preserve_phases_without_over_planning
    - record_decisions_made
    - carry_open_items_forward
    - carry_risks_forward
    - avoid_exact_rank_or_score_computation
~~~

## findings_contract

~~~yaml
findings_contract:
  file_name: findings.md
  purpose: >
    Preserve durable findings, decisions made, source notes, open questions,
    and operator validations that should survive the current session.

  exact_sections:
    - Durable Findings
    - Decisions Made
    - Source Notes
    - Open Questions
    - Operator Validations

  required_behavior:
    - include_durable_findings_only
    - preserve_raw_source_ref
    - preserve_raw_source_path
    - record_source_conflict_when_present
    - record_operator_validation_when_present
    - avoid_unverified_claims
~~~

## progress_contract

~~~yaml
progress_contract:
  file_name: progress.md
  purpose: >
    Preserve the session log, actions taken, status mutations, state deltas,
    errors, review flags, and next step for continuity.

  exact_sections:
    - Session Log
    - Actions Taken
    - Status Mutations
    - State Deltas
    - Errors or Review Flags
    - Next Step

  required_behavior:
    - log_actions_taken
    - log_status_mutation_records
    - log_state_delta_summary
    - log_errors_and_review_flags
    - preserve_operator_validation_record
    - record_next_step_without_computing_final_rank
~~~

## next_session_contract

~~~yaml
next_session_contract:
  file_name: next-session.md
  purpose: >
    Provide the smallest clean context packet that lets the next session resume
    safely and lets apex-plan consume current context without reconstructing
    chat history.

  exact_sections:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions

  required_behavior:
    - summarize_current_step
    - list_open_items
    - list_risks
    - list_decisions_made
    - list_next_actions
    - include_review_flags_when_relevant
    - include_raw_source_ref_and_raw_source_path_when_needed
~~~

## required_next_session_sections

~~~yaml
required_next_session_sections:
  exact_order:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions

  section_rules:
    Current Step:
      must_capture: current operative session position
    Open Items:
      must_capture: unresolved context, missing inputs, source conflicts, unfinished validation
    Risks:
      must_capture: scope drift, invalid status risk, duplicate entity risk, raw source gaps
    Decisions Made:
      must_capture: confirmed operator validations and durable decisions
    Next Actions:
      must_capture: actions for the next session or planning layer without final ranking
~~~

## read_before_decide_rule

~~~yaml
read_before_decide_rule:
  principle: >
    Before producing final handoff or mutation records, read the available plan,
    findings, progress, next-session context, raw sources, and operator
    instructions.

  required_reads_when_available:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
    - raw_source_ref
    - raw_source_path
    - operator_instructions

  missing_context_behavior:
    - mark_missing_input
    - preserve_missing_path
    - continue_with_available_evidence_if_safe
    - do_not_invent_source_basis
~~~

## planning_layer_feed_contract

~~~yaml
planning_layer_feed_contract:
  artifact_name: planning_feed
  primary_consumer: apex-plan
  purpose: >
    Provide the planning layer with clean next-session context, durable
    findings, unresolved context, risks, decisions made, and source references.

  include:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
    - state_delta_summary
    - entity_update_record
    - raw_source_ref
    - raw_source_path
    - review_flags

  exclude:
    - exact_next_task_ranking
    - blocker_scan
    - registry_rebuild
    - drift_detection
    - priority_score_computation
    - urgency_score_computation
    - unlock_depth_computation
    - new_project_decomposition
~~~

## missing_context_behavior

~~~yaml
missing_context_behavior:
  when_required_input_missing:
    add_review_flags:
      - missing_input
    write_to:
      - Open Items
      - Errors or Review Flags
    use_marker: USER_INPUT_REQUIRED

  when_raw_source_missing:
    add_review_flags:
      - raw_source_missing
    preserve_available_raw_source_ref: true
    preserve_available_raw_source_path: true

  when_scope_drift_detected:
    add_review_flags:
      - scope_drift
    route_to_apex_plan_or_apex_sync: true
~~~

## final_handoff_acceptance_checks

~~~yaml
final_handoff_acceptance_checks:
  required_file_count: 4
  required_files_present:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  task_plan_sections_exact:
    - Goal
    - Current Step
    - Phases
    - Decisions
    - Open Items
    - Risks
    - Next Actions
  findings_sections_exact:
    - Durable Findings
    - Decisions Made
    - Source Notes
    - Open Questions
    - Operator Validations
  progress_sections_exact:
    - Session Log
    - Actions Taken
    - Status Mutations
    - State Deltas
    - Errors or Review Flags
    - Next Step
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  no_forbidden_sync_or_plan_behavior: true
  raw_source_basis_preserved_when_available: true
  unresolved_context_visible: true
~~~
```

### 3.6 `.claude/skills/apex-session/templates/task_plan.md`

```markdown
# Goal

USER_INPUT_REQUIRED

# Current Step

USER_INPUT_REQUIRED

# Phases

- USER_INPUT_REQUIRED

# Decisions

- USER_INPUT_REQUIRED

# Open Items

- USER_INPUT_REQUIRED

# Risks

- USER_INPUT_REQUIRED

# Next Actions

- USER_INPUT_REQUIRED
```

### 3.7 `.claude/skills/apex-session/templates/findings.md`

```markdown
# Durable Findings

- USER_INPUT_REQUIRED

# Decisions Made

- USER_INPUT_REQUIRED

# Source Notes

- raw_source_ref: USER_INPUT_REQUIRED
- raw_source_path: USER_INPUT_REQUIRED

# Open Questions

- USER_INPUT_REQUIRED

# Operator Validations

- operator_validation: USER_INPUT_REQUIRED
- validation_timestamp: USER_INPUT_REQUIRED
```

### 3.8 `.claude/skills/apex-session/templates/progress.md`

```markdown
# Session Log

- USER_INPUT_REQUIRED

# Actions Taken

- USER_INPUT_REQUIRED

# Status Mutations

- task_id: USER_INPUT_REQUIRED
- task_title: USER_INPUT_REQUIRED
- status_before: USER_INPUT_REQUIRED
- status_after: USER_INPUT_REQUIRED
- status_change_reason: USER_INPUT_REQUIRED
- operator_validation: USER_INPUT_REQUIRED
- validation_status: USER_INPUT_REQUIRED
- validation_timestamp: USER_INPUT_REQUIRED

# State Deltas

- state_delta_id: USER_INPUT_REQUIRED
- raw_source_ref: USER_INPUT_REQUIRED
- raw_source_path: USER_INPUT_REQUIRED

# Errors or Review Flags

- review_flags: USER_INPUT_REQUIRED

# Next Step

USER_INPUT_REQUIRED
```

### 3.9 `.claude/skills/apex-session/templates/next-session.md`

```markdown
# Current Step

USER_INPUT_REQUIRED

# Open Items

- USER_INPUT_REQUIRED

# Risks

- USER_INPUT_REQUIRED

# Decisions Made

- USER_INPUT_REQUIRED

# Next Actions

- USER_INPUT_REQUIRED
```

### 3.10 `.claude/skills/apex-session/package-manifest.md`

```markdown
# Apex Session Package Manifest

## package_name

~~~yaml
package_name: apex-session
~~~

## package_path

~~~yaml
package_path: ".claude/skills/apex-session/"
~~~

## package_status

~~~yaml
package_status: final_canonical_v1
~~~

## exact_file_index

~~~yaml
exact_file_index:
  package_root: ".claude/skills/apex-session/"
  files:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - references/state-delta-and-entity-rules.md
    - references/handoff-and-next-session-contract.md
    - templates/task_plan.md
    - templates/findings.md
    - templates/progress.md
    - templates/next-session.md
    - package-manifest.md

  exact_file_count: 10

  excluded_directories:
    - scripts/
    - evals/
    - tests/
    - schemas/
    - examples/
    - assets/
    - agents/
~~~

## file_purpose_map

~~~yaml
file_purpose_map:
  SKILL.md:
    role: compact_skill_entrypoint
    purpose: >
      Defines invocation scope, objective, accepted inputs, final outputs,
      supporting file navigation, procedure, validation rules, failure modes,
      and completion gate.

  references/session-cluster-contract.md:
    role: C_SESSION_scope_contract
    purpose: >
      Defines package role, owned processes, excluded processes,
      cross-package routing, PD3 boundary, script/write exclusions, and final
      acceptance invariants.

  references/mutation-gate-rules.md:
    role: mutation_validation_contract
    purpose: >
      Defines H1 status validation, status_mutation_record schema,
      before_after_preview schema, operator_validation_record schema,
      confirmation gate, invalid mutation rejection, and final mutation output
      contract.

  references/state-delta-and-entity-rules.md:
    role: state_delta_and_entity_contract
    purpose: >
      Defines state_delta_summary schema, entity_update_record schema, raw
      source preservation, source conflict policy, duplicate entity risk policy,
      durable findings policy, and planning_feed policy.

  references/handoff-and-next-session-contract.md:
    role: H6_handoff_contract
    purpose: >
      Defines task_plan.md, findings.md, progress.md, next-session.md,
      required next-session sections, read-before-decide rule, planning feed,
      missing-context behavior, and final handoff checks.

  templates/task_plan.md:
    role: H6_template
    purpose: task plan artifact template with exact sections.

  templates/findings.md:
    role: H6_template
    purpose: findings artifact template with exact sections.

  templates/progress.md:
    role: H6_template
    purpose: progress artifact template with exact sections.

  templates/next-session.md:
    role: H6_template
    purpose: next-session artifact template with exact sections.

  package-manifest.md:
    role: package_index_and_validation_summary
    purpose: >
      Defines package status, exact file index, file purpose map, source basis,
      read order, package invariants, validation checklist, and forbidden
      claims.
~~~

## source_basis_map

~~~yaml
source_basis_map:
  SKILL.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt
      - .claude/skills/apex-session/SKILL.md
      - planning-with-files SKILL.md
      - Backlog types/index.ts
      - CrewAI task.py SUBSTITUTE
      - Apex_Alfred_Skill_Definition_Guide.md

  references/session-cluster-contract.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt
      - .claude/skills/apex-session/SKILL.md
      - .claude/skills/apex-session/package-manifest.md

  references/mutation-gate-rules.md:
    sources:
      - Backlog types/index.ts
      - Backlog parser.ts
      - CrewAI task.py SUBSTITUTE
      - Phase 5 — Process Coverage Gate v0.1.md
      - Phase 7 Package Readiness.txt

  references/state-delta-and-entity-rules.md:
    sources:
      - Backlog types/index.ts
      - Backlog parser.ts
      - llm-wiki SKILL.md
      - Phase 4 — Mechanism Ledger by Source v0.1.md
      - Phase 5 — Process Coverage Gate v0.1.md

  references/handoff-and-next-session-contract.md:
    sources:
      - Phase 1 — Authority Extraction.md
      - 00_Apex_Phase_Pack_Meta_Index.md
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/task_plan.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/findings.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/progress.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  templates/next-session.md:
    sources:
      - H6_handoff_format
      - planning-with-files SKILL.md
      - planning-with-files docs/quickstart.md

  package-manifest.md:
    sources:
      - .claude/skills/apex-session/package-manifest.md
      - generated final package files
      - Phase 7 Package Readiness.txt
~~~

## read_order

~~~yaml
read_order:
  normal_invocation:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - references/state-delta-and-entity-rules.md
    - references/handoff-and-next-session-contract.md
    - relevant_template
    - package-manifest.md

  status_mutation_request:
    - SKILL.md
    - references/session-cluster-contract.md
    - references/mutation-gate-rules.md
    - templates/progress.md
    - references/handoff-and-next-session-contract.md

  handoff_request:
    - SKILL.md
    - references/handoff-and-next-session-contract.md
    - templates/task_plan.md
    - templates/findings.md
    - templates/progress.md
    - templates/next-session.md

  state_delta_or_entity_request:
    - SKILL.md
    - references/state-delta-and-entity-rules.md
    - references/mutation-gate-rules.md
    - references/handoff-and-next-session-contract.md
~~~

## package_invariants

~~~yaml
package_invariants:
  package_status: final_canonical_v1
  exact_file_count: 10
  C_SESSION_only: true
  H1_status_enum_exact:
    - open
    - in-progress
    - blocked
    - done
    - deferred
  H6_handoff_files_exact:
    - task_plan.md
    - findings.md
    - progress.md
    - next-session.md
  next_session_sections_exact:
    - Current Step
    - Open Items
    - Risks
    - Decisions Made
    - Next Actions
  no_scripts_in_package: true
  no_repo_write_claim: true
  no_apex_plan_scope: true
  no_apex_sync_scope: true
  no_public_web_research: true
  raw_source_reference_preservation_required: true
  operator_validation_required_for_consequential_mutation: true
  CrewAI_task_py_labeled_SUBSTITUTE: true
  llm_wiki_not_claimed_as_update_index_source: true
~~~

## validation_checklist

~~~yaml
validation_checklist:
  file_inventory:
    exact_file_count_is_10: true
    exact_tree_match: true
    no_extra_generated_directories: true

  SKILL_md:
    valid_frontmatter: true
    frontmatter_name_is_apex_session: true
    description_matches_final_contract: true
    objective_present: true
    skill_contract_present: true
    accepted_inputs_present: true
    final_outputs_present: true
    procedure_present: true
    validation_rules_present: true
    failure_modes_present: true
    completion_gate_present: true

  status_and_mutation:
    H1_status_enum_exact: true
    no_extra_task_status_values: true
    status_mutation_record_schema_present: true
    before_after_preview_schema_present: true
    operator_validation_record_schema_present: true
    invalid_mutation_rejection_present: true

  handoff:
    H6_files_present: true
    next_session_sections_exact: true
    templates_have_exact_required_sections: true

  boundaries:
    no_ranking_behavior: true
    no_blocker_scan_behavior: true
    no_registry_rebuild_behavior: true
    no_score_computation: true
    no_unlock_depth_computation: true
    no_new_project_decomposition: true
    no_script_execution: true
    no_calendar_operations: true

  formatting:
    no_collapsed_yaml: true
    no_collapsed_markdown: true
    headings_have_blank_lines: true
    code_fences_balanced: true
    no_source_citation_markup_inside_generated_files: true
    no_unresolved_placeholders_except_USER_INPUT_REQUIRED: true
~~~

## forbidden_claims

~~~yaml
forbidden_claims:
  - copied_CrewAI_getting_started_skill_source
  - copied_llm_wiki_update_index_behavior
  - copied_OpenClaw_TaskFlow_behavior
  - copied_Kanban_blocker_script_behavior
  - exact_next_task_ranking_inside_apex_session
  - blocker_scan_inside_apex_session
  - registry_rebuild_inside_apex_session
  - drift_detection_inside_apex_session
  - priority_score_computation_inside_apex_session
  - urgency_score_computation_inside_apex_session
  - unlock_depth_computation_inside_apex_session
  - silent_repo_mutation
  - scripts_generated_for_apex_session
~~~
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

```txt
No known unresolved package risks after validation.
```