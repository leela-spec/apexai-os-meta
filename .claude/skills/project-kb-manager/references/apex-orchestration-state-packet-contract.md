# APEX Orchestration State Packet Contract

## Purpose

```yaml
purpose:
  artifact_name: apex_orchestration_state_packet
  role: compact_state_handoff_to_PreCapWeek_and_PreCapNextDay
  package_location: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
  goals:
    - Define the compact glue artifact consumed by PreCapWeek and PreCapNextDay.
    - Reference existing state and project-management owners instead of replacing them.
    - Prevent schema duplication across project-kb-manager, ProjectStatus, apex-plan, apex-sync, apex-session, and apex-kb.
    - Separate verified repository sources from candidate, stale, partial, or synthetic sources.
  primary_consumers:
    - PreCapWeek
    - PreCapNextDay
```

The `apex_orchestration_state_packet` is a compact handoff view. It is not the project database, not the current status overview, not an apex plan packet, not a sync registry, and not a session mutation packet.

## Ownership Boundary

```yaml
ownership_boundary:
  project-kb-manager:
    owns:
      - durable_project_records
      - project_schema
      - milestone_state
      - registry
      - consumed_recap_registry
      - next_PreCap_context_when_update_occurs
    may_contribute:
      - active_project_records
      - milestone_summary
      - next_precap_context
      - durable_project_state_refs
      - operator_review_needed_flags

  ProjectStatus:
    owns:
      - current_project_status_overview
      - compact_project_task_subtask_view
      - ranked_task_view
      - temporary_unassigned_items
      - operator_validation_flags
    may_contribute:
      - current_project_status_overview_ref
      - ranked_task_digest
      - unresolved_unassigned_digest
      - compact_status_snapshot

  apex-plan:
    owns:
      - project_capture
      - epic_task_planning
      - qualitative_priority_and_dependency_rationale
      - provisional_focus_recommendation
    may_contribute:
      - latest_apex_plan_packet_refs
      - proposed_task_summary
      - unresolved_planning_questions
      - qualitative_focus_signal

  apex-sync:
    owns_if_promoted:
      - exact_next_task_computation
      - dependency_graph_traversal
      - registry_rebuild
      - drift_detection
      - exact_priority_urgency_unlock_sorting
    may_contribute_if_available:
      - sync_status
      - registry_status
      - drift_flags
      - computed_focus_candidates
      - promotion_status

  apex-session:
    owns_if_promoted:
      - status_mutation
      - session_progress_log
      - next_session_context
      - operator_confirmed_write
      - state_delta
    may_contribute_if_available:
      - latest_session_summary
      - next_session_context_ref
      - pending_mutation_flags
      - session_delta_summary
      - promotion_status

  apex-kb:
    owns:
      - source_preserving_knowledge_base
      - source_refs
      - artifact_refs
      - retrieval_outputs
    may_contribute:
      - source_map_refs
      - artifact_index_refs
      - kb_query_refs
      - evidence_confidence_notes
```

Boundary rule: each snapshot may reference or summarize an upstream package output, but must not redefine the upstream package's schema or compute work reserved for that package.

## Source Package Map

```yaml
source_package_map:
  artifact:
    name: apex_orchestration_state_packet
    role: compact_state_handoff_to_PreCapWeek_and_PreCapNextDay
    source_packages:
      - apex-plan
      - apex-sync
      - apex-session
      - project-kb-manager
      - ProjectStatus
      - apex-kb
    downstream_consumers:
      - PreCapWeek
      - PreCapNextDay

  expected_repo_paths:
    apex-plan: .claude/skills/apex-plan/SKILL.md
    apex-sync: .claude/skills/apex-sync/apex-sync-final-extraction-report.md
    apex-session: .claude/skills/apex-session/apex-session-final-extraction-report.md
    project-kb-manager: .claude/skills/project-kb-manager/SKILL.md
    project-schema: .claude/skills/project-kb-manager/references/project-schema.md
    ProjectStatus: .claude/skills/ProjectStatus/SKILL.md
    apex-kb: .claude/skills/apex-kb/SKILL.md
    PreCapWeek: .claude/skills/PrecapWeek/SKILL.md
    PreCapNextDay: .claude/skills/PrecapNextDay/SKILL.md
```

## Schema: apex_orchestration_state_packet

```yaml
apex_orchestration_state_packet:
  type: object
  artifact_name: apex_orchestration_state_packet
  role: compact_state_handoff_to_weekly_and_daily_planning
  required:
    - packet_id
    - created_or_updated_at
    - source_status
    - source_package_status
    - project_kb_snapshot
    - project_status_snapshot
    - planning_snapshot
    - sync_snapshot
    - session_snapshot
    - evidence_snapshot
    - weekly_planning_view
    - next_day_planning_view
    - operator_review_flags
    - validation_status

  fields:
    packet_id:
      type: string
      format: apex_orchestration_state_packet_<YYYY_MM_DD>_<slug>

    created_or_updated_at:
      type: string
      format: YYYY-MM-DD

    source_status:
      type: enum
      allowed:
        - verified_repo_sources
        - mixed_verified_and_synthetic
        - synthetic_example
        - partial_context
        - stale_context

    source_package_status:
      type: object
      fields:
        apex_plan:
          type: string
          allowed:
            - verified_current
        project_kb_manager:
          type: string
          allowed:
            - verified_current
        ProjectStatus:
          type: string
          allowed:
            - verified_current
        apex_kb:
          type: string
          allowed:
            - verified_current
            - missing
        apex_sync:
          type: string
          allowed:
            - verified_current
            - extraction_report_only
            - missing
        apex_session:
          type: string
          allowed:
            - verified_current
            - extraction_report_only
            - missing

    project_kb_snapshot:
      owner: project-kb-manager
      type: object
      allowed_content:
        - active_project_record_refs
        - project_status_summary_for_precap
        - milestone_summary
        - next_precap_context
        - operator_review_needed_flags
        - durable_project_state_refs

    project_status_snapshot:
      owner: ProjectStatus
      type: object
      allowed_content:
        - current_project_status_overview_ref
        - compact_project_task_subtask_digest
        - ranked_task_digest
        - unresolved_unassigned_digest
        - status_review_flags

    planning_snapshot:
      owner: apex-plan
      type: object
      allowed_content:
        - latest_apex_plan_packet_refs
        - proposed_task_summary
        - unresolved_planning_questions
        - qualitative_focus_signal

    sync_snapshot:
      owner: apex-sync
      type: object
      status_note: may_be_extraction_report_only
      allowed_content:
        - sync_status
        - registry_status
        - drift_flags
        - computed_focus_candidates
        - source_package_promotion_status

    session_snapshot:
      owner: apex-session
      type: object
      status_note: may_be_extraction_report_only
      allowed_content:
        - latest_session_summary
        - next_session_context_ref
        - pending_mutation_flags
        - session_delta_summary
        - source_package_promotion_status

    evidence_snapshot:
      owner: apex-kb
      type: object
      allowed_content:
        - source_map_refs
        - artifact_index_refs
        - kb_query_refs
        - evidence_confidence_notes

    weekly_planning_view:
      consumed_by: PreCapWeek
      type: object
      contains:
        - weekly_priority_candidates
        - active_project_candidates
        - cross_project_constraints
        - operator_decisions_needed
        - source_confidence_summary

    next_day_planning_view:
      consumed_by: PreCapNextDay
      type: object
      contains:
        - next_day_focus_candidates
        - flow_candidate_inputs
        - immediate_blockers
        - prompt_or_workflow_preparation_needs
        - review_flags_for_daily_plan

    operator_review_flags:
      type: list
      item_type: string

    validation_status:
      type: enum
      allowed:
        - valid
        - valid_with_warnings
        - synthetic_example
        - blocked_by_missing_state_source
        - operator_review_required
```

## Field Mapping to Existing Packages

```yaml
field_mapping:
  project_kb_snapshot:
    source_package: project-kb-manager
    source_authority:
      - references/project-schema.md
      - .claude/kb/registry.md
      - .claude/kb/projects/<project-id>.md
      - .claude/kb/next-precap-context.md
    packet_rule: Reference durable records and summarize only the minimum needed for weekly or daily planning.

  project_status_snapshot:
    source_package: ProjectStatus
    source_authority:
      - current_project_status_overview
      - ranked_task_view
      - temporary_unassigned_items
    packet_rule: Use a compact digest; do not expand into workstreams, detailed database records, or decision registries.

  planning_snapshot:
    source_package: apex-plan
    source_authority:
      - apex_plan_packet
      - proposed_task_records
      - priority_urgency_focus_rationale
      - handoff_requests
    packet_rule: Carry qualitative planning signals only; do not compute exact next-task order.

  sync_snapshot:
    source_package: apex-sync
    source_authority:
      - apex-sync package if promoted
      - apex-sync extraction report if not promoted
    packet_rule: Include computed focus candidates only when source_package_promotion_status confirms a verified current package or explicitly label extraction-report-only status.

  session_snapshot:
    source_package: apex-session
    source_authority:
      - apex-session package if promoted
      - apex-session extraction report if not promoted
    packet_rule: Include session deltas and next-session references only when verified or explicitly label them as candidate/extraction-report-only.

  evidence_snapshot:
    source_package: apex-kb
    source_authority:
      - source_map_refs
      - artifact_index_refs
      - kb_query_refs
      - retrieval_outputs
    packet_rule: Preserve source references and confidence notes; do not mutate KB, plan, sync, session, PreCap, FlowRecap, or APSU state.
```

## PreCapWeek Consumption View

```yaml
precap_week_consumption_view:
  consumed_object: weekly_planning_view
  purpose: Seed weekly strategy without forcing PreCapWeek to inspect every project record.
  should_read:
    - weekly_priority_candidates
    - active_project_candidates
    - cross_project_constraints
    - operator_decisions_needed
    - source_confidence_summary
  must_preserve:
    - source_status
    - source_package_status
    - operator_review_flags
  must_not_do:
    - Do not treat synthetic example data as verified project state.
    - Do not expand this packet into a weekly_plan_packet schema.
    - Do not overwrite project-kb-manager records.
```

## PreCapNextDay Consumption View

```yaml
precap_next_day_consumption_view:
  consumed_object: next_day_planning_view
  purpose: Seed daily flow selection and review flags without making PreCapNextDay the project-state owner.
  should_read:
    - next_day_focus_candidates
    - flow_candidate_inputs
    - immediate_blockers
    - prompt_or_workflow_preparation_needs
    - review_flags_for_daily_plan
  must_preserve:
    - missing_or_partial_source_flags
    - candidate_status_for_unpromoted_sync_or_session_data
    - operator_review_flags
  must_not_do:
    - Do not fabricate missing project state.
    - Do not treat this packet as a next_day_plan.
    - Do not run FlowRecap or status merge.
    - Do not claim calendar or repo writes.
```

## Synthetic Example Policy

```yaml
synthetic_example_policy:
  allowed: true
  required_labels:
    source_status: synthetic_example
    repo_verified: false
    purpose: test_fixture_for_PreCapWeek_and_PreCapNextDay_consumption
  required_behavior:
    - Label every invented project, task, blocker, priority, and focus candidate as synthetic.
    - Keep synthetic examples out of durable project records unless the operator explicitly promotes them.
    - Use synthetic examples only for template testing, consumption testing, or UX review.
    - Do not let downstream PreCapWeek or PreCapNextDay infer real project state from synthetic examples.
```

## Validation Rules

```yaml
validation_rules:
  required_checks:
    packet_id_matches_format: true
    source_status_allowed_value: true
    source_package_status_present: true
    each_snapshot_has_owner: true
    each_snapshot_uses_allowed_content_only: true
    project_schema_not_redefined: true
    current_project_status_overview_not_redefined: true
    apex_plan_packet_not_redefined: true
    sync_registry_and_drift_logic_not_redefined: true
    session_mutation_and_next_session_context_not_redefined: true
    weekly_plan_packet_not_created: true
    next_day_plan_or_flow_packet_not_created: true
    synthetic_data_labeled_when_present: true
    operator_review_flags_preserved: true
    validation_status_allowed_value: true

  warning_conditions:
    - source_status_is_partial_context
    - source_status_is_stale_context
    - source_package_status_apex_sync_is_extraction_report_only
    - source_package_status_apex_session_is_extraction_report_only
    - evidence_snapshot_missing_source_refs
    - flow_candidate_inputs_have_no_verified_project_ref

  blocking_conditions:
    - project_kb_snapshot_redefines_project_schema_fields
    - project_status_snapshot_redefines_ProjectStatus_output
    - planning_snapshot_computes_exact_next_task_order
    - sync_snapshot_claims_verified_current_without_promoted_package_evidence
    - session_snapshot_claims_mutation_without_operator_confirmed_write
    - packet_contains_weekly_plan_packet
    - packet_contains_next_day_plan_or_flow_prompt_pack
```

## Non-Goals

```yaml
non_goals:
  - Do not define project-schema fields; project-kb-manager/references/project-schema.md owns them.
  - Do not define current_project_status_overview; ProjectStatus owns it.
  - Do not define apex_plan_packet; apex-plan owns it.
  - Do not define sync registry or drift logic; apex-sync owns it if promoted.
  - Do not define session mutation or next-session context; apex-session owns it if promoted.
  - Do not create weekly_plan_packet; PreCapWeek owns it.
  - Do not create next_day_plan, flow_packet, or flow_prompt_pack; PreCapNextDay owns them.
  - Do not run FlowRecap or status merge.
  - Do not build runtime automation, agents, cron, Hermes, FlowRecap execution, calendar writes, or status merge.
```
