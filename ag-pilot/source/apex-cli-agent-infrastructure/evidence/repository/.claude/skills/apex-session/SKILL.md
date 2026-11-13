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

## APEX OS Backbone Role

`apex-session` is the confirmed-mutation and closure capability in the shared Plan-Sync-Session Backbone. Multi-Agent Orchestration uses it for gated mutation and run closure; Weekly Orchestrator routes approved project or task changes through it and reads its confirmed planning feed. Session artifacts do not auto-activate either orchestration system.

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