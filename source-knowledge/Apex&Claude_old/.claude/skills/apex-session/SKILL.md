---
name: apex-session
description: >
  Use this skill when the operator asks to propose status mutations, preview before/after changes, log session progress, extract state deltas, propose entity updates, validate writes, prepare next-session context, or feed the planning layer. Accepts Apex task files, handoff notes, raw sources, and operator instructions. Produces gated session artifacts. Does not rank next tasks, scan blockers, rebuild registries, compute scores, or decompose new work.
---

# Apex Session

## Skill Contract

~~~yaml
skill_contract:
  primary_output: next_session_context
  output_role: operator_gated_session_mutation_and_handoff
  package_path: ".claude/skills/apex-session/"
  chat_output_only: true

  canonical_source:
    session_cluster_contract: "references/session-cluster-contract.md"
    mutation_gate_rules: "references/mutation-gate-rules.md"
    state_delta_and_entity_rules: "references/state-delta-and-entity-rules.md"
    handoff_and_next_session_contract: "references/handoff-and-next-session-contract.md"

  required_outputs:
    - status_mutation_proposal
    - before_after_mutation_preview
    - session_progress_log
    - state_delta_summary
    - entity_update_proposal
    - next_session_context
    - planning_layer_feed
    - operator_validation_result

  mutation_gate:
    canonical_source: "references/mutation-gate-rules.md"
    rule: "All mutations remain proposals until the operator supplies an accepted confirmation_token."

  accepted_confirm_tokens:
    canonical_source: "references/mutation-gate-rules.md"

  boundaries:
    canonical_source: "references/session-cluster-contract.md"
~~~

## Supporting Files

~~~yaml
supporting_files:
  - path: "references/session-cluster-contract.md"
    read_when:
      - validating_package_boundary
      - checking_process_scope
      - coordinating_with_apex_plan_or_apex_sync

  - path: "references/mutation-gate-rules.md"
    read_when:
      - proposing_status_mutation
      - preparing_before_after_mutation_preview
      - validating_operator_confirmation

  - path: "references/state-delta-and-entity-rules.md"
    read_when:
      - extracting_state_delta_summary
      - proposing_entity_update
      - preserving_raw_source

  - path: "references/handoff-and-next-session-contract.md"
    read_when:
      - writing_handoff_files
      - producing_next_session_context
      - producing_planning_layer_feed

  - path: "templates/task_plan.md"
    read_when:
      - creating_task_plan
      - refreshing_handoff_template
      - preparing_session_plan

  - path: "templates/findings.md"
    read_when:
      - creating_findings
      - recording_decisions_made
      - extracting_durable_findings

  - path: "templates/progress.md"
    read_when:
      - creating_progress
      - appending_session_progress_log
      - recording_session_activity

  - path: "templates/next-session.md"
    read_when:
      - creating_next_session
      - preparing_context_bootstrap
      - summarizing_open_items

  - path: "package-manifest.md"
    read_when:
      - operator_inspects_package_structure
      - validating_file_inventory
~~~

## Procedure

1. **Load session context.** Read the operator request, relevant task files, handoff files, entity files, and raw_source_path references; if required context is missing, apply the matching failure mode.

2. **Draft mutation proposals.** For requested status or entity changes, produce status_mutation_proposal or entity_update_proposal only, and include before_after_mutation_preview for every proposed mutation.

3. **Apply the mutation gate.** Require confirmation_token to equal CONFIRM, CONFIRM WRITE, or CONFIRM MUTATION before any mutation is considered confirmed; otherwise keep all outputs as proposals.

4. **Record session progress.** Produce session_progress_log entries for actions, decisions, unresolved items, review_flags, and handoff_requests without computing next-task ranking or registry state.

5. **Extract state deltas.** Convert session evidence into state_delta_summary and entity_update_proposal while preserving raw_source and raw_source_path exactly.

6. **Prepare handoff.** Produce task_plan, findings, progress, next_session_context, and planning_layer_feed using the canonical handoff contract.

7. **Validate completion.** Check all outputs against the supporting files and apply Failure Modes before returning the final operator-facing result.

## Failure Modes

~~~yaml
failure_modes:
  missing_confirmation:
    trigger: "A mutation is requested but confirmation_token is absent or not accepted."
    correction: "Keep the change as a proposal, include before_after_mutation_preview, and request CONFIRM, CONFIRM WRITE, or CONFIRM MUTATION."

  ambiguous_status_delta:
    trigger: "The requested status change is unclear or not supported by session evidence."
    correction: "Return status_mutation_proposal with review_flags and do not mark the mutation confirmed."

  unsupported_status_value:
    trigger: "The requested status is not open, in-progress, blocked, done, or deferred."
    correction: "Reject the status value and ask the operator to choose a supported status."

  raw_source_missing:
    trigger: "An entity update or state delta lacks raw_source or raw_source_path."
    correction: "Flag raw_source_missing and preserve the proposal without rewriting source material."

  entity_update_uncertain:
    trigger: "The entity update cannot be confidently tied to one entity_id or entity_path."
    correction: "Return entity_update_proposal with review_flags and request operator validation."

  duplicate_entity_risk:
    trigger: "The proposed entity update may duplicate an existing entity file."
    correction: "Flag duplicate_entity_risk and require operator confirmation before writing."

  planning_feed_incomplete:
    trigger: "The planning_layer_feed lacks Current Step, Open Items, Risks, Decisions Made, or Next Actions."
    correction: "Return the incomplete feed with review_flags and do not treat handoff as complete."

  boundary_violation:
    trigger: "The request asks apex-session to rank tasks, scan blockers, rebuild registries, compute scores, or decompose new work."
    correction: "Stop that part of the request and route the responsibility to apex-sync or apex-plan."
~~~

## Output Requirements

~~~yaml
output_requirements:
  required_outputs:
    - status_mutation_proposal
    - before_after_mutation_preview
    - session_progress_log
    - state_delta_summary
    - entity_update_proposal
    - next_session_context
    - planning_layer_feed
    - operator_validation_result

  mutation_outputs:
    proposal_until_confirmed: true
    before_after_mutation_preview_required: true
    confirmation_token_required: true

  handoff_files:
    - task_plan
    - findings
    - progress
    - next_session

  review_flags:
    include_only_when_relevant: true
    canonical_source: "references/mutation-gate-rules.md"

  raw_source:
    preserve_raw_source: true
    canonical_source: "references/state-delta-and-entity-rules.md"
~~~

## Completion Gate

~~~yaml
completion_gate:
  status_mutation_proposal_is_proposal_until_confirmed: true
  before_after_mutation_preview_present_for_mutations: true
  mutation_gate_uses_accepted_confirm_tokens: true
  operator_validation_result_present: true
  raw_source_path_preserved_for_entity_updates: true
  next_session_context_has_required_sections: true
  planning_layer_feed_present_when_requested: true
  no_next_task_ranking_computed: true
  no_blocker_scan_performed: true
  no_registry_rebuild_performed: true
  failure_modes_checked: true
~~~