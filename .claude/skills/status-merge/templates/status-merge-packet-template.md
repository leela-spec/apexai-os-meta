# Status Merge Packet

```yaml
status_merge_packet:
  merge_packet_id: "{{ID}}"
  source_flow_recap_refs: []
  previous_session_or_sync_refs: []
  accepted_delta_candidates: []
  rejected_or_deferred_delta_candidates: []
  conflict_notes: []
  proposed_apex_session_mutation:
    mutation_scope: "{{SCOPE}}"
    approved_candidate_refs: []
    current_confirmed_refs: []
    evidence_refs: []
    operator_decision: "{{PENDING_OR_CONFIRMED}}"
    required_session_receipt: "{{SESSION_RESULT_REF}}"
  next_PreCapNextDay_input_context:
    next_actions: []
    blockers: []
    source_refs: []
  operator_review_flags: []
  validation_status: "{{STATUS}}"
```

This is proposal-only. Send it to Apex Session only after the operator confirms G5.
