# Shared Handoff Schema (canonical)

Rule: every packet passed between weekly-loop stages — weekly_plan_packet, next_day_plan, flow_packet, normalized_raw_flow_dump, skipped_flow_marker, flow_recap_packet, model_usage_delta, status_merge_packet, updated_all_project_status_packet, and every stage-agent return — carries this one envelope. Per-packet body fields are owned by the producing skill's contract; the envelope is owned here.

Applies when: any stage agent returns output to the orchestrator, and any stage artifact is written to `artifacts/` or proposed against `state/`.

## envelope

```yaml
handoff_envelope:
  packet_type: weekly_plan_packet | next_day_plan | flow_packet | prompt_pack | normalized_raw_flow_dump | skipped_flow_marker | flow_recap_packet | model_usage_delta | status_merge_packet | all_project_status_packet | review_verdict | stage_agent_return
  packet_id: "<packet_type>-<YYYYMMDD>-<short-slug>"
  produced_by: <stage_agent_name_or_skill_name>
  accountability: alfred | meta_strategy | meta_ops | meta_detective
  lifecycle_stage: proposal | computed | confirmed
  status: complete | partial | skipped | blocked
  target_surface: <repo_relative_path_or_none>   # the durable file this packet proposes to affect; none for read-only returns
  next_state: <one_line_what_becomes_true_if_accepted>
  prerequisites: []                               # packet_ids or paths that must be accepted/present first
  expected_action: <exact_next_job_for_consumer>
  sources: []                                     # repo-relative evidence paths; refs not copies
  uncertainties: []                               # open questions the producer could not resolve
  unresolved_risk: <one_line_or_none>
  stop_condition: <when_the_consumer_must_halt_instead_of_continuing>
  authority:
    state: candidate | verified | invalidated
    basis_digest: null | "sha256:<64-hex>"        # canonicalized content + declared evidence closure
    verification_ref: null | <repo_relative_review_artifact_path>
  operator_validation: confirmed | rejected | needs_revision | not_requested
```

## field_rules

- Rule: `lifecycle_stage` and `authority.state` are distinct axes. `lifecycle_stage` says where the packet sits in the loop; `authority.state` says whether it may be treated as authoritative input by a downstream stage.
- Rule: on creation and on any content or declared-evidence change: `authority.state: candidate`, `basis_digest: null`, `verification_ref: null`.
- Rule: `candidate → verified` only when `verification_ref` resolves to an independent review artifact with a pass verdict, the reviewer run differs from the creator run, and the review's basis_digest equals the packet's current digest. See `review-wiring.md`.
- Rule: `→ invalidated` when a review verdict is fail/needs_revision, a governing source contradiction is recorded, or the stored basis_digest no longer matches current content.
- Rule: `invalidated → candidate` only after substantive revision; digest and verification_ref reset to null.
- Constraint: a canon-changing write (anything under `state/` or `.claude/kb/`) requires BOTH `operator_validation: confirmed` AND every authoritative input in the packet's `prerequisites`/`sources` closure at `authority.state: verified` (or explicitly waived by the operator in the same confirmation).
- Constraint: `operator_validation` answers "may this mutation be applied"; `authority.state` answers "may this artifact justify a mutation". Neither substitutes for the other.
- Do not: continue from a packet whose `expected_action` or `stop_condition` is missing — silent continuation from an unclear handoff is invalid; return `blocked` with the gap named.

## gate_primitive

One reusable gate, applied where consequence lives, not everywhere:

```yaml
gate_primitive:
  field: operator_validation
  values: [confirmed, rejected, needs_revision, not_requested]
  requested_operator_action: confirm | reject | revise | none
  no_implicit_apply: true
  phase_transition_confirmation: literal operator phrase required (e.g. "confirm G1")
```

Gate map for the weekly loop:

```yaml
gates:
  G1: {stage: precap_week,        packet: weekly_plan_packet,              required: always}
  G2: {stage: precap_next_day,    packet: next_day_plan,                   required: always}
  G3: {stage: operator_execution, packet: raw_flow_dump_or_skip_marker,    required: always, note: operator confirms completion state, not content quality}
  G4: {stage: flow_recap,         packet: flow_recap_packet,               required: always, scope: next_step_proposal + candidate_project_status_delta}
  G5: {stage: status_merge,       packet: status_merge_packet,             required: selective, trigger: conflicts | high_impact | ambiguity}
```

- Rule: gate passage is recorded in the packet itself (`operator_validation` + date), never only in chat.
- Rule: autonomous-override runs (operator explicitly requests no-approval execution) may skip G1/G2/G5 confirmation ceremonies but never skip the write-path constraint above for `state/` and `.claude/kb/` mutations, and never fabricate `operator_validation: confirmed`. Packets produced in such runs stay `not_requested` and are batch-presented at run end.

## storage_rules

- Rule: packets are MD files with one fenced YAML envelope block first, body second. snake_case identifiers. Refs not copies: cite artifact paths, never inline upstream content.
- Rule: file naming `artifacts/<family>/<packet_id>.md`; families per CLAUDE.md `artifact_paths`.
- Rule: `state/` files are append-or-flag only; a status merge appends a dated section, it never rewrites history.
