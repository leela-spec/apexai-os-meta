# Next PreCap Handoff Context Contract

`status-merge` may prepare a compact next-planning seed. It is advisory context, not a plan, durable state, or an autonomous trigger.

```yaml
next_precap_handoff:
  required:
    - source_status_merge_packet_ref
    - operator_decision_ref
    - confirmed_apex_session_mutation_receipt_ref_or_pending
    - confirmed_apex_session_planning_feed_ref_or_pending
  optional:
    - apex_sync_next_action_report_ref
    - apex_sync_blocker_report_ref
    - carry_forward_items
    - unresolved_risks
  rules:
    - Before Session confirmation, mark all proposed changes pending and do not represent them as accepted state.
    - After Session confirmation, PrecapWeek and PrecapNextDay consume the Session planning feed first and supplied Sync reports second.
    - Project KB material may supplement context but never overrides confirmed Session or Sync output.
    - The operator chooses whether and when to invoke the next planning skill.
```

## Completion checks

```yaml
completion_checks:
  proposal_and_confirmed_state_separated: true
  session_receipt_reference_visible: true
  operator_choice_preserved: true
  no_plan_or_project_state_mutation: true
```
