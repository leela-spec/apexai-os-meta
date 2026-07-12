# Status Merge Packet Contract

```yaml
status_merge_packet:
  required:
    - merge_packet_id
    - source_flow_recap_refs
    - previous_session_or_sync_refs
    - accepted_delta_candidates
    - rejected_or_deferred_delta_candidates
    - conflict_notes
    - proposed_apex_session_mutation
    - next_PreCapNextDay_input_context
    - operator_review_flags
    - validation_status
  proposed_apex_session_mutation:
    required:
      - mutation_scope
      - approved_candidate_refs
      - current_confirmed_refs
      - evidence_refs
      - operator_decision
      - required_session_receipt
    rules:
      - proposal_only_until_operator_confirmation
      - apex_session_is_the_only_durable_owner
      - no_project_kb_or_root_state_write
  next_PreCapNextDay_input_context:
    role: compact_planning_seed
    must_not_be: next_day_plan
```

The packet preserves candidate-versus-confirmed separation. A G5-confirmed packet is an input to Apex Session, whose mutation record and refreshed planning feed are the only valid J10 receipt.
