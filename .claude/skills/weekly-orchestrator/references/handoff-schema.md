# Weekly Handoff Schema

Every weekly-stage packet carries this envelope. The body remains owned by its producing skill. Apex Plan, Sync, and Session use their own native contracts and exchange references with the weekly workflow only at defined boundaries.

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: weekly_plan_packet | next_day_plan | flow_packet | prompt_pack | normalized_raw_flow_dump | skipped_flow_marker | flow_recap_packet | model_usage_delta | status_merge_packet | all_project_status_packet | review_verdict | stage_agent_return
  gate: G1 | G2 | G3 | G4 | G5 | review | none
  packet_id: "<packet_type>-<YYYYMMDD>-<short-slug>"
  produced_by: <stage_agent_name_or_skill_name>
  accountability: alfred | meta_strategy | meta_ops | meta_detective
  lifecycle_stage: proposal | computed | confirmed
  status: complete | partial | skipped | blocked
  target_surface: none
  next_state: <one_line_what_becomes_true_if_accepted>
  prerequisites: []
  expected_action: <exact_next_job_for_consumer>
  sources: []
  uncertainties: []
  unresolved_risk: <one_line_or_none>
  stop_condition: <when_the_consumer_must_halt>
  authority:
    state: candidate | verified | invalidated
    basis_digest: null | "sha256:<64-hex>"
    verification_ref: null | <repo_relative_review_artifact_path>
  operator_validation: confirmed | rejected | needs_revision | not_requested
```

## Rules

- The orchestrator supplies run dates and week identifiers; agents do not infer them.
- Weekly packets are proposal or context artifacts. They never directly mutate project, task, registry, or KB state.
- A confirmed status merge is supplied to `apex-session` with its evidence references. Session validates and performs any mutation under its own contract.
- `authority.state` answers whether an artifact may justify a decision. `operator_validation` answers whether the operator approved the proposed action. Neither replaces the other.
- A changed packet or declared source invalidates its prior review digest and returns it to candidate state.
- Missing `expected_action` or `stop_condition` blocks the handoff.

## Gates

```yaml
gates:
  G1: {stage: precap_week, packet: weekly_plan_packet, required: always}
  G2: {stage: precap_next_day, packet: next_day_plan, required: always}
  G3: {stage: operator_execution, packet: raw_flow_dump_or_skip_marker, required: always}
  G4: {stage: flow_recap, packet: flow_recap_packet, required: always}
  G5: {stage: status_merge, packet: status_merge_packet, required: selective}
```

Gate passage is recorded in its packet. Autonomous runs may leave gates `not_requested`; they never authorize an Apex Session mutation.

## Storage

- Store weekly packets under their existing `artifacts/` family as Markdown with the YAML envelope first.
- Reference upstream artifacts by path; do not copy their bodies into a packet.
- Store confirmed project/task/session mutations and refreshed planning context through Apex Session, not this weekly schema.
