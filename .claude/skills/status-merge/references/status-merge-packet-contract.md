# Status Merge Packet Contract

## Contract Role

```yaml
status_merge_packet_contract:
  artifact_name: status_merge_packet
  file_role: status_merge_reference_contract
  package: status-merge
  purpose: >
    Define the minimal operator-gated interface for reconciling validated
    FlowRecap candidate deltas, usage summaries, and previous state references
    into merge proposals, conflict notes, proposed project-kb-manager updates,
    an updated all-project status packet proposal/view, and the next PreCapNextDay input
    context. This contract does not create runtime execution, bypass
    project-kb-manager, or perform automatic durable state overwrite.

  ownership:
    owns:
      - status_merge_packet
      - merge_proposal
      - accepted_delta_register_view
      - conflict_notes
      - consumed_recap_candidate_list
      - next_PreCapNextDay_input_context
      - operator_conflict_review_gate
    must_not_own:
      - project_kb_durable_schema
      - direct_project_record_mutation_without_project_kb_manager
      - current_project_status_overview_schema
      - flow_recap_packet_schema
      - model_usage_delta_schema
      - usage_summary_schema
      - apex_orchestration_state_packet_schema
      - weekly_plan_packet_schema
      - next_day_plan_schema
      - calendar_write_schema
      - runtime_execution
      - automatic_status_overwrite

  upstream_inputs:
    required:
      - source_flow_recap_refs
      - source_usage_summary_refs
      - previous_state_refs
    optional:
      - apex_orchestration_state_packet_ref
      - current_project_status_overview_ref
      - project_kb_record_refs
      - operator_merge_notes

  downstream_consumers:
    primary:
      - operator_review
      - project-kb-manager
      - PreCapNextDay
    secondary:
      - ProjectStatus
      - PreCapWeek

  global_rules:
    interface_only: true
    runtime_not_created: true
    scheduler_not_created: true
    agent_not_created: true
    durable_writes_are_operator_gated: true
    durable_writes_must_route_through_project_kb_manager: true
    conflicts_are_surfaced_before_acceptance: true
    accepted_deltas_remain_proposals_until_confirmed: true
    next_PreCapNextDay_input_context_is_compact_seed_only: true
```

## Source Authority Inspection

```yaml
source_authority:
  inspected_sources:
    - path: .claude/Claude.md
      status: inspected
      relevant_finding: StatusMerge was formerly indexed as missing; its status output is proposal/view only behind operator gate G5, and repo rules forbid automatic state overwrite and batch writes without confirmation.
    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevant_finding: project-kb-manager owns durable project KB updates and next PreCap context when updates occur.
    - path: .claude/skills/project-kb-manager/references/project-schema.md
      status: inspected
      relevant_finding: project schema is the sole field/type authority for durable project records.
    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevant_finding: apex_orchestration_state_packet is a compact state handoff view, not a schema to redefine inside status-merge.
    - path: .claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md
      status: inspected
      relevant_finding: state handoff templates use refs, short digests, confidence notes, and operator review flags instead of full database exposure.
    - path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
      status: inspected
      relevant_finding: ProjectStatus owns current_project_status_overview and explicitly must not create status merges or detailed databases.
    - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      status: inspected
      relevant_finding: FlowRecap produces candidate_project_status_delta and model_usage_delta_candidate only; status-merge consumes them without mutating project KB directly.
    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/status-merge-packet.md
      status: inspected
      relevant_finding: status merge accepts validated recap deltas, previous status, conflict notes, and next-context seed; conflicts are exposed before acceptance.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md
      status: inspected
      relevant_finding: final skill packages should contain concise SKILL.md, references, optional templates/examples, and no runtime, scheduler, task board, or deployment files.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md
      status: inspected
      relevant_finding: YAML must remain 2-space indented, parseable, and non-duplicative; procedures should remain coarse-grained.

  source_gap_register:
    - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
      status: present
      handling: Treat project_status_delta content as candidate refs from flow_recap_packet without redefining schema.
    - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
      status: present
      handling: Treat source_usage_summary_refs as reference-only; usage_summary schema remains externally owned.
```

## Schema: status_merge_packet

```yaml
status_merge_packet:
  type: object
  required:
    - merge_packet_id
    - artifact_name
    - created_or_updated_at
    - source_flow_recap_refs
    - source_usage_summary_refs
    - previous_state_refs
    - merge_scope
    - accepted_delta_candidates
    - rejected_or_deferred_delta_candidates
    - conflict_notes
    - proposed_project_kb_update
    - updated_all_project_status_packet_proposal
    - next_PreCapNextDay_input_context
    - operator_review_flags
    - validation_status

  fields:
    merge_packet_id:
      type: string
      format: status_merge_packet_<YYYY_MM_DD>_<short_slug>
      required: true

    artifact_name:
      type: string
      const: status_merge_packet
      required: true

    created_or_updated_at:
      type: string
      format: YYYY-MM-DD
      required: true

    source_flow_recap_refs:
      type: list
      item_ref: flow_recap_packet
      min_items: 1
      required: true
      note: Reference only. flow_recap_packet_schema is owned by flow-recap.

    source_usage_summary_refs:
      type: list
      item_ref: usage_summary
      min_items: 0
      required: true
      note: Reference only. usage_summary_schema is owned outside status-merge.

    previous_state_refs:
      type: list
      item_ref: previous_state_ref
      min_items: 1
      required: true
      allowed_sources:
        - apex_orchestration_state_packet
        - current_project_status_overview
        - project_kb_record
        - consumed_recap_registry
      note: Previous state is referenced, not overwritten.

    merge_scope:
      type: string
      allowed:
        - single_flow
        - execution_day
        - multi_day_backlog
        - conflict_review_only
      required: true

    accepted_delta_candidates:
      type: list
      item_ref: accepted_delta_candidate
      min_items: 0
      required: true
      note: Candidate accepted for proposal only; durable acceptance requires operator/project-kb-manager confirmation.

    rejected_or_deferred_delta_candidates:
      type: list
      item_ref: rejected_or_deferred_delta_candidate
      min_items: 0
      required: true
      note: Preserve rejected and deferred deltas for auditability without mutating durable state.

    conflict_notes:
      type: list
      item_ref: conflict_note
      min_items: 0
      required: true
      note: Conflicts must be surfaced before acceptance.

    proposed_project_kb_update:
      type: object_ref
      ref: proposed_project_kb_update
      required: true
      owner: status-merge
      durable_write_owner: project-kb-manager
      note: Proposal only. Direct project record mutation is forbidden here.

    updated_all_project_status_packet_proposal:
      type: object_ref
      ref: updated_all_project_status_packet_view
      required: true
      owner: status-merge
      note: View/proposal only. current_project_status_overview_schema remains owned by ProjectStatus and durable project state remains owned by project-kb-manager.

    next_PreCapNextDay_input_context:
      type: object_ref
      ref: next_PreCapNextDay_input_context
      required: true
      owner: status-merge
      contract: references/next-precaphandoff-context-contract.md
      note: Compact seed for next daily planning, not a next_day_plan.

    operator_review_flags:
      type: list
      item_ref: operator_review_flag
      min_items: 0
      max_items: 24
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - blocked_by_conflict
        - blocked_by_missing_state_owner
      required: true
```

## Minimal Supporting Object Sketches

```yaml
accepted_delta_candidate:
  type: object
  required:
    - candidate_id
    - source_ref
    - delta_summary
    - proposed_destination
    - acceptance_basis
    - operator_confirmation_status
  fields:
    proposed_destination:
      allowed:
        - project_kb_manager_update_proposal
        - ProjectStatus_view_update_proposal
        - next_PreCapNextDay_context_seed
        - consumed_recap_register_view
    operator_confirmation_status:
      allowed:
        - confirmed
        - not_confirmed
        - not_required_for_low_risk_view_only

rejected_or_deferred_delta_candidate:
  type: object
  required:
    - candidate_id
    - source_ref
    - delta_summary
    - disposition
    - reason
  fields:
    disposition:
      allowed:
        - rejected
        - deferred
        - duplicate
        - superseded
        - insufficient_evidence

conflict_note:
  type: object
  required:
    - conflict_id
    - source_refs
    - conflict_type
    - conflict_summary
    - required_operator_decision
  fields:
    conflict_type:
      allowed:
        - state_owner_unclear
        - competing_status_values
        - stale_vs_newer_evidence
        - duplicate_recap_candidate
        - project_identity_ambiguous
        - usage_summary_incomplete
        - next_action_conflict

proposed_project_kb_update:
  type: object
  required:
    - proposal_id
    - durable_write_owner
    - target_project_refs
    - proposed_changes_summary
    - blocked_changes
    - operator_gate_status
  fields:
    durable_write_owner:
      const: project-kb-manager
    operator_gate_status:
      allowed:
        - ready_for_operator_review
        - confirmed_for_project_kb_manager
        - blocked_by_conflict
        - blocked_by_missing_state_owner

updated_all_project_status_packet_view:
  type: object
  required:
    - view_id
    - source_status_merge_packet_ref
    - accepted_delta_register_view
    - consumed_recap_candidate_list
    - project_status_summary
    - unresolved_conflicts
  note: This is a status-merge view/proposal, not durable project KB state.
```

## Boundary Validation

```yaml
boundary_validation:
  project_kb_manager_boundary_preserved: true
  direct_project_record_mutation_forbidden: true
  ProjectStatus_schema_not_redefined: true
  flow_recap_schema_not_redefined: true
  usage_summary_schema_not_redefined: true
  apex_orchestration_state_packet_schema_not_redefined: true
  next_day_plan_not_created: true
  weekly_plan_not_created: true
  calendar_events_not_created: true
  runtime_not_created: true
  automatic_status_overwrite_not_created: true
  conflicts_surfaced_before_acceptance: true
```
