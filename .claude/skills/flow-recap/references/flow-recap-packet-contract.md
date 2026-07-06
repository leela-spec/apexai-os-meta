# Flow Recap Packet Contract

## Contract Role

```yaml
flow_recap_packet_contract:
  artifact_name: flow_recap_packet
  file_role: flow_recap_reference_contract
  package: flow-recap
  purpose: >
    Define the minimal interface for converting one completed, partial, skipped,
    or blocked flow into a compact recap packet with evidence summaries,
    candidate-only project status deltas, candidate-only model usage deltas,
    next-step proposals, unresolved questions, and operator validation flags.

  ownership:
    owns:
      - flow_recap_packet
      - recap_summary
      - evidence_ref_summary
      - candidate_project_status_delta
      - model_usage_delta_candidate
      - next_step_proposal
      - unresolved_questions
      - operator_validation_gate_for_recap
    must_not_own:
      - normalized_raw_flow_dump_schema
      - flow_packet_schema
      - flow_prompt_pack_schema
      - prompt_packet_schema
      - accepted_project_status_update
      - project_kb_durable_schema
      - model_usage_delta_final_schema
      - usage_summary_schema
      - status_merge_packet_schema
      - updated_all_project_status_packet
      - next_PreCapNextDay_input_context
      - runtime_execution

  upstream_inputs:
    required:
      - source_flow_packet_ref
      - normalized_raw_flow_dump_ref
    optional:
      - flow_prompt_pack_ref
      - evidence_artifact_refs
      - model_usage_notes
      - skipped_flow_marker_ref
      - apex_orchestration_state_packet_ref

  downstream_consumers:
    primary:
      - operator_review
      - status-merge
      - model-usage-log
    secondary:
      - project-kb-manager
      - next_PreCapNextDay

  global_rules:
    one_flow_recap_packet_per_flow: true
    recap_summarizes_evidence_without_expanding_scope: true
    candidate_project_status_delta_is_not_accepted_state: true
    model_usage_delta_candidate_is_not_final_usage_log: true
    operator_validation_required_for_status_delta_acceptance: true
    status_merge_not_run: true
    project_kb_not_mutated: true
    calendar_events_not_created: true
    runtime_not_created: true
```

## Source Authority Inspection

```yaml
source_authority:
  inspected_sources:
    - path: .claude/Claude.md
      status: inspected
      relevant_finding: FlowRecap is listed as missing and should write flow_recap_packet behind operator gate G4.
    - path: .claude/skills/PrecapNextDay/Skill_precap-next-day.md
      status: inspected
      relevant_finding: PreCapNextDay prepares FlowRecap handoff context but must not run FlowRecap or create FlowRecap outputs.
    - path: .claude/skills/PrecapNextDay/references/flow-packet-contract.md
      status: inspected
      relevant_finding: flow_packet owns FlowRecap_handoff_block and raw-flow-dump preparation, but not FlowRecap output.
    - path: .claude/skills/PrecapNextDay/references/flow-prompt-pack-contract.md
      status: inspected
      relevant_finding: flow_prompt_pack may include FlowRecap preparation notes but does not own FlowRecap output.
    - path: .claude/skills/PrecapNextDay/references/usage-tracking-dependency-contract.md
      status: inspected
      relevant_finding: PreCapNextDay hands usage capture structure to FlowRecap but does not create actual usage deltas.
    - path: .claude/skills/raw-flow-dump-normalize/references/raw-flow-dump-contract.md
      status: inspected
      relevant_finding: normalized_raw_flow_dump is FlowRecap input and must not create project status or model usage deltas.
    - path: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/flow-recap-packet.md
      status: inspected
      relevant_finding: concept page defines FlowRecap as compression from flow packet plus raw flow dump into recap summary, candidate state delta, and open questions.
    - path: .claude/skills/project-kb-manager/SKILL.md
      status: inspected
      relevant_finding: project-kb-manager owns durable KB updates and must not be bypassed by FlowRecap.
    - path: .claude/skills/project-kb-manager/references/apex-orchestration-state-packet-contract.md
      status: inspected
      relevant_finding: apex_orchestration_state_packet is a compact handoff view consumed by planning skills, not a FlowRecap output.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_Package_BestPractice_Handover.md
      status: inspected
      relevant_finding: skill files should be concise, schema-governed, and avoid runtime/scheduler files.
    - path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-skill-design/sources/operator-supplied/notes/Claude_Skill_PromptFlow_Design_Guidance_v1.md
      status: inspected
      relevant_finding: YAML must remain parseable with 2-space indentation and skill procedures should stay coarse-grained.
  source_gap_register:
    - path: .claude/skills/raw-flow-dump-normalize/references/skipped-flow-marker-contract.md
      status: missing
      handling: Treat skipped_flow_marker_ref as optional until the skipped-flow marker contract exists.
    - path: .claude/skills/PrecapNextDay/precap-next-day-package-manifest.md
      status: not_reinspected_in_this_file_creation_step
      handling: Known package map exists from prior PreCap work, but this first FlowRecap contract does not depend on manifest internals.
```

## Schema: flow_recap_packet

```yaml
flow_recap_packet:
  type: object
  required:
    - recap_id
    - artifact_name
    - execution_day
    - flow_id
    - source_flow_packet_ref
    - normalized_raw_flow_dump_ref
    - recap_status
    - evidence_summary
    - work_completed_summary
    - outputs_created_or_changed
    - decisions_made
    - blockers_or_failures
    - candidate_project_status_delta
    - model_usage_delta_candidate
    - next_step_proposal
    - operator_review_flags
    - validation_status

  fields:
    recap_id:
      type: string
      format: flow_recap_<YYYY_MM_DD>_<flow_id>_<short_slug>
      required: true

    artifact_name:
      type: string
      const: flow_recap_packet
      required: true

    execution_day:
      type: string
      format: YYYY-MM-DD
      required: true

    flow_id:
      type: string
      required: true
      note: Use the source flow_packet flow_id. If ambiguous, preserve ambiguity in operator_review_flags.

    source_flow_packet_ref:
      type: object_ref
      ref: flow_packet
      required: true
      note: Reference only. flow_packet_schema is owned by PreCapNextDay.

    normalized_raw_flow_dump_ref:
      type: object_ref
      ref: normalized_raw_flow_dump
      required: true
      note: Reference only. normalized_raw_flow_dump_schema is owned by raw-flow-dump-normalize.

    flow_prompt_pack_ref:
      type: object_ref
      ref: flow_prompt_pack
      required: false
      note: Reference only. flow_prompt_pack_schema is owned by PreCapNextDay.

    skipped_flow_marker_ref:
      type: object_ref
      ref: skipped_flow_marker
      required: false
      note: Optional until skipped-flow marker contract exists.

    recap_status:
      type: string
      allowed:
        - ready_for_operator_review
        - operator_validated
        - low_confidence
        - blocked_by_missing_evidence
      required: true

    evidence_summary:
      type: object_ref
      ref: evidence_summary
      required: true

    work_completed_summary:
      type: string
      required: true
      note: Compact summary of what happened in the flow, grounded only in supplied evidence.

    outputs_created_or_changed:
      type: list
      item_ref: output_created_or_changed
      required: true

    decisions_made:
      type: list
      item_ref: recap_decision
      required: true

    blockers_or_failures:
      type: list
      item_ref: blocker_or_failure_summary
      required: true

    candidate_project_status_delta:
      type: object_ref
      ref: candidate_project_status_delta
      required: true
      note: Candidate only until status-merge or project-kb-manager acceptance.

    model_usage_delta_candidate:
      type: object_ref
      ref: model_usage_delta_candidate
      required: true
      note: Candidate only. Final usage schemas are owned by model-usage-log or ai-routing-and-usage-tracking.

    next_step_proposal:
      type: object_ref
      ref: next_step_proposal
      required: true
      note: Proposal only, not a next-day plan.

    unresolved_questions:
      type: list
      item_ref: unresolved_question
      required: false

    operator_review_flags:
      type: list
      item_ref: operator_review_flag
      min_items: 0
      max_items: 16
      required: true

    validation_status:
      type: string
      allowed:
        - valid
        - valid_with_warnings
        - operator_review_recommended
        - low_confidence
        - blocked_by_missing_minimum_evidence
      required: true
```

## Supporting Object Sketches

```yaml
evidence_summary:
  type: object
  required:
    - evidence_status
    - evidence_refs
    - confidence
  fields:
    evidence_status:
      type: string
      allowed:
        - sufficient
        - partial
        - conflicting
        - missing_minimum_evidence
    evidence_refs:
      type: list
      item_ref: evidence_ref
      min_items: 1
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown

output_created_or_changed:
  type: object
  required:
    - output_label
    - change_type
    - evidence_refs
  fields:
    change_type:
      type: string
      allowed:
        - created
        - updated
        - reviewed
        - proposed
        - no_output
        - unknown

recap_decision:
  type: object
  required:
    - decision_summary
    - evidence_refs
    - status
  fields:
    status:
      type: string
      allowed:
        - made
        - proposed
        - deferred
        - needs_operator_validation

model_usage_delta_candidate:
  type: object
  required:
    - candidate_id
    - source_notes
    - confidence
    - finalization_owner
  fields:
    finalization_owner:
      const: model-usage-log
    confidence:
      type: string
      allowed:
        - high
        - medium
        - low
        - unknown

next_step_proposal:
  type: object
  required:
    - proposal_summary
    - proposed_owner
    - source_evidence_refs
    - requires_operator_validation
  fields:
    proposed_owner:
      type: string
      allowed:
        - operator
        - PreCapNextDay
        - project-kb-manager
        - status-merge
        - model-usage-log
        - unknown
    requires_operator_validation:
      type: boolean
```

## Validation Rules

```yaml
flow_recap_packet_validation_rules:
  minimum_evidence:
    source_flow_packet_ref_present: true
    normalized_raw_flow_dump_ref_present: true
    evidence_refs_nonempty: true
  candidate_state_boundary:
    project_status_delta_must_be_candidate_only: true
    must_not_write_project_kb: true
    must_not_create_updated_all_project_status_packet: true
  usage_boundary:
    model_usage_delta_candidate_must_not_be_final_usage_log: true
    quota_or_cost_claims_require_explicit_evidence: true
  operator_gate:
    operator_review_flags_required_when_confidence_low: true
    candidate_delta_requires_operator_validation: true
  forbidden_outputs:
    runtime_execution: false
    calendar_write: false
    project_work_execution: false
    status_merge_execution: false
```
