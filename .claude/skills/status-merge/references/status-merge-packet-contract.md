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
    an updated all-project status packet view, and the next PreCapNextDay input
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
      - previous_state_refs
    optional:
      - source_usage_summary_refs
      - apex_orchestration_state_packet_ref
      - current_project_status_overview_ref
      - project_kb_record_refs
      - operator_merge_notes

  downstream_consumers:
    primary:
      - operator_review
      - project-kb-manager
      - ProjectStatus
      - PreCapNextDay
    secondary:
      - PreCapWeek
      - model-usage-log

  global_rules:
    one_status_merge_packet_per_merge_scope: true
    accepted_deltas_are_proposals_until_operator_review: true
    project_kb_manager_performs_or_gates_durable_writes: true
    conflicts_are_surfaced_before_acceptance: true
    consumed_recap_tracking_is_candidate_until_project_kb_manager_acceptance: true
    updated_all_project_status_packet_is_a_reviewable_view_not_direct_state: true
    next_PreCapNextDay_input_context_is_compact_seed_only: true
    no_runtime_execution: true
    no_calendar_write: true
    no_automatic_status_overwrite: true
```

## Source Authority Inspection

```yaml
source_authority:
  inspected_sources:
    - path: .claude/Claude.md
      status: inspected
      relevant_finding: >
        The repo loop declares StatusMerge as missing, positioned after
        FlowRecap, writing updated_all_project_status_packet behind operator
        gate G5; repo behavior forbids unconfirmed state overwrites.
    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevant_finding: >
        project-kb-manager maintains the durable Apex project KB and owns update
        and intake modes while forbidding project execution, planning, FlowRecap,
        calendar mutation, and schema fields outside project-schema.
    - path: .claude/skills/project-kb-manager/references/project-schema.md
      status: inspected
      relevant_finding: >
        project-schema is the sole field type and allowed-value authority for
        durable project records, milestones, progress logs, registry entries,
        and consumed recap entries.
    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevant_finding: >
        apex_orchestration_state_packet is a compact planning handoff view; it
        must not redefine project schema, ProjectStatus, apex-plan, session,
        sync, weekly, next-day, FlowRecap, or status-merge outputs.
    - path: .claude/skills/project-kb-manager/templates/apex-orchestration-state-packet-template.md
      status: inspected
      relevant_finding: >
        Operator-facing state handoffs should expose source package status,
        review flags, compact planning views, and missing or weak input markers
        rather than the full project database.
    - path: .claude/skills/ProjectStatus/project-status-overview_SKILL_v3.md
      status: inspected
      relevant_finding: >
        ProjectStatus owns current_project_status_overview and explicitly does
        not create weekly plans, next-day plans, status merges, execution,
        decision registries, artifact registries, or detailed project databases.
    - path: .claude/skills/flow-recap/references/flow-recap-packet-contract.md
      status: inspected
      relevant_finding: >
        FlowRecap outputs candidate_project_status_delta and
        model_usage_delta_candidate only; durable status acceptance belongs
        downstream to status-merge or project-kb-manager.
    - path: .claude/skills/model-usage-log/references/model-usage-delta-contract.md
      status: inspected
      relevant_finding: >
        model-usage-log owns model_usage_delta and treats usage outputs as
        advisory and non-blocking for FlowRecap and StatusMerge, with no runtime
        metering or automation.
    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/status-merge-packet.md
      status: inspected
      relevant_finding: >
        The concept page defines status merge as accepting validated recap
        deltas into canonical project state, reading accepted recaps and previous
        status, writing updated status, conflict notes, and next-context seed,
        with conflicts exposed before acceptance.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md
      status: inspected
      relevant_finding: >
        Skill packages should keep schema authority in references, avoid runtime
        files and scheduler files, and keep SKILL.md compact with required
        frontmatter and section order.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md
      status: inspected
      relevant_finding: >
        YAML must remain parseable with 2-space indentation; procedures should
        remain coarse-grained; failure modes and completion gates should be
        machine-readable.

  source_gap_register:
    - path: .claude/skills/flow-recap/references/project-status-delta-contract.md
      status: missing
      handling: >
        Treat project status deltas inside source_flow_recap_refs as opaque
        candidate deltas. Do not infer a separate project_status_delta schema.
    - path: .claude/skills/model-usage-log/references/usage-summary-contract.md
      status: missing
      handling: >
        Treat source_usage_summary_refs as optional opaque references. Do not
        define usage_summary schema inside status-merge.
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
    - updated_all_project_status_packet
    - next_PreCapNextDay_input_context
    - operator_review_flags
    - validation_status

  fields:
    merge_packet_id:
      type: string
      format: status_merge_packet_<YYYY_MM_DD>_<scope_or_short_slug>
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
      item_type: object_ref
      required: true
      min_items: 0
      note: >
        References to flow_recap_packet artifacts only. flow_recap_packet_schema
        is owned by flow-recap.

    source_usage_summary_refs:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      note: >
        Optional/empty when usage summary is missing. usage_summary_schema is
        not owned by status-merge.

    previous_state_refs:
      type: list
      item_type: object_ref
      required: true
      min_items: 0
      allowed_ref_examples:
        - apex_orchestration_state_packet
        - current_project_status_overview
        - project_kb_record
        - consumed_recap_registry
        - prior_status_merge_packet
      note: Reference previous state artifacts; do not mutate them here.

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
      required: true
      min_items: 0
      note: >
        Accepted for proposal only until operator/project-kb-manager acceptance
        confirms the durable write.

    rejected_or_deferred_delta_candidates:
      type: list
      item_ref: rejected_or_deferred_delta_candidate
      required: true
      min_items: 0

    conflict_notes:
      type: list
      item_ref: conflict_note
      required: true
      min_items: 0

    proposed_project_kb_update:
      type: object_ref
      ref: proposed_project_kb_update
      required: true
      note: >
        Proposal only. project-kb-manager owns durable project schema and write
        handling.

    updated_all_project_status_packet:
      type: object_ref
      ref: updated_all_project_status_packet_view
      required: true
      note: >
        Reviewable status view produced by status-merge. Durable state overwrite
        requires operator/project-kb-manager confirmation.

    next_PreCapNextDay_input_context:
      type: object_ref
      ref: next_PreCapNextDay_input_context
      required: true
      note: >
        Compact planning seed only. PreCapNextDay owns next_day_plan and flow
        planning outputs.

    operator_review_flags:
      type: list
      item_type: string
      required: true
      min_items: 0
      max_items: 24

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

## Supporting Object Sketches

```yaml
accepted_delta_candidate:
  type: object
  required:
    - candidate_id
    - source_flow_recap_ref
    - delta_summary
    - target_owner
    - acceptance_basis
    - write_status
    - evidence_refs
  fields:
    target_owner:
      type: string
      allowed:
        - project-kb-manager
        - ProjectStatus
        - model-usage-log
        - PreCapNextDay
        - operator
        - unknown
    write_status:
      type: string
      allowed:
        - proposal_only
        - operator_accepted_pending_project_kb_manager
        - project_kb_manager_confirmed
        - not_a_durable_write

rejected_or_deferred_delta_candidate:
  type: object
  required:
    - candidate_id
    - source_flow_recap_ref
    - disposition
    - reason
    - revisit_condition
  fields:
    disposition:
      type: string
      allowed:
        - rejected
        - deferred
        - duplicate
        - insufficient_evidence
        - blocked_by_conflict

conflict_note:
  type: object
  required:
    - conflict_id
    - conflict_type
    - conflicting_refs
    - impact
    - operator_decision_needed
    - proposed_resolution
  fields:
    conflict_type:
      type: string
      allowed:
        - state_conflict
        - recap_conflict
        - duplicate_delta
        - stale_previous_state
        - missing_state_owner
        - usage_evidence_conflict
        - scope_boundary_conflict
    operator_decision_needed:
      type: boolean

proposed_project_kb_update:
  type: object
  required:
    - update_status
    - target_project_refs
    - proposed_changes_summary
    - project_kb_manager_required
    - durable_write_allowed_here
  fields:
    update_status:
      type: string
      allowed:
        - no_update_needed
        - proposal_ready
        - operator_review_needed
        - blocked_by_conflict
        - blocked_by_missing_project_kb_owner
    project_kb_manager_required:
      type: boolean
      const: true
    durable_write_allowed_here:
      type: boolean
      const: false

updated_all_project_status_packet_view:
  type: object
  required:
    - view_status
    - source_status
    - compact_status_changes
    - unresolved_conflicts
    - durable_state_write_status
  fields:
    view_status:
      type: string
      allowed:
        - proposal_view
        - operator_review_view
        - conflict_only_view
        - blocked
    durable_state_write_status:
      type: string
      allowed:
        - none_performed
        - pending_project_kb_manager
        - confirmed_externally_by_project_kb_manager
```

## Validation Rules

```yaml
status_merge_packet_validation_rules:
  source_requirements:
    source_flow_recap_refs_present: true
    previous_state_refs_present_or_gap_flagged: true
    usage_summary_refs_present_or_empty_with_gap_flag: true

  boundary_requirements:
    flow_recap_schema_not_redefined: true
    project_kb_schema_not_redefined: true
    project_status_overview_schema_not_redefined: true
    usage_summary_schema_not_redefined: true
    apex_orchestration_state_packet_schema_not_redefined: true
    weekly_plan_packet_not_created: true
    next_day_plan_not_created: true
    calendar_write_not_created: true
    runtime_not_created: true

  operator_gate_requirements:
    conflicts_are_listed_before_acceptance: true
    accepted_deltas_remain_proposal_until_confirmed: true
    proposed_project_kb_update_marks_project_kb_manager_required: true
    durable_write_allowed_here_is_false: true
    operator_review_flags_present: true

  validation_status_selection:
    valid: all_required_fields_present_no_conflict_and_no_boundary_violation
    valid_with_warnings: required_fields_present_with_low_or_medium_risk_warnings
    operator_review_recommended: uncertainty_or_review_needed_but_packet_usable
    blocked_by_conflict: unresolved_conflict_prevents_safe_acceptance
    blocked_by_missing_state_owner: required_state_owner_or_source_is_missing
```

## Non-Goals

```yaml
non_goals:
  - Do not mutate project KB records directly.
  - Do not bypass project-kb-manager write rules or project-schema authority.
  - Do not redefine current_project_status_overview.
  - Do not redefine flow_recap_packet or project_status_delta schemas.
  - Do not redefine model_usage_delta or usage_summary schemas.
  - Do not create weekly_plan_packet, next_day_plan, flow_packet, or flow_prompt_pack.
  - Do not create calendar_event_write_request or calendar events.
  - Do not create runtime automation, agents, cron, schedulers, or automatic state overwrite.
```
