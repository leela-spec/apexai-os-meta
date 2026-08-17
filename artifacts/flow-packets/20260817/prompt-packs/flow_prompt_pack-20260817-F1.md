```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_prompt_pack
  gate: G2
  packet_id: flow-prompt-pack-20260817-F1
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  expected_action: "After G2 confirmation, materialize or use the degraded generic prompt placeholders during F1 execution; do not treat placeholders as PromptEngineer-approved prompts."
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

```yaml
flow_prompt_pack:
  pack_id: flow_prompt_pack_20260817_F1
  artifact_name: flow_prompt_pack
  created_or_updated_at: "2026-08-17"
  execution_day: "2026-08-17"
  flow_id: F1
  project: Leela
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_pack_policy:
    storage_policy: {one_file_per_flow_prompt_pack: true, embedded_in_daily_plan: false, referenced_from_flow_packet: true}
    prompt_system_policy: {one_primary_prompt_system_only: true, alternatives_allowed_by_default: false, follow_up_prompts_allowed: true, max_follow_up_prompts_per_sprint: 2}
    prompt_capture_policy: {light_capture_hints_allowed: true, mandatory_machine_readable_capture_block_inside_every_prompt: false, canonical_capture_home: raw_flow_dump}
    provider_rationale_policy: {provider_rationale_required: true, prompt_design_rationale_required: true, rationale_source: degraded_generic_prompt_mode_note}
    fallback_policy: {fallback_notes_allowed: true, fallback_prompt_system_allowed_by_default: false, fallback_requires_operator_review: true}
  source_flow_packet_ref: {flow_packet_id: flow_packet_20260817_F1, flow_packet_path_or_slot: artifacts/flow-packets/20260817/flow_packet-20260817-F1.md, flow_id: F1, project: Leela}
  daily_plan_ref: {next_day_plan_id: next_day_plan_2026_08_17_w34_monday, next_day_plan_path_or_slot: artifacts/next-day-plans/next_day_plan-20260817.md}
  sprint_prompt_sequences:
    - sprint_id: S1
      sprint_role: first_work_sprint
      sprint_status: operator_review_needed
      expected_output_type_ref: {value: runtime_observations}
      workflow_stage_ref: {value: verification}
      process_stage_ref: {value: evidence_collection}
      start_prompt_ref: &f1s1 {prompt_packet_id: placeholder-F1-S1, packet_role: start_prompt, prompt_task_type: verification, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}
      prompt_packet_refs: [*f1s1]
      placement_rules_applied: ["Use current screen contract and runtime evidence; do not infer unseen behavior."]
      validation_status: operator_review_recommended
    - sprint_id: S2
      sprint_role: second_work_or_deepening_sprint
      sprint_status: operator_review_needed
      expected_output_type_ref: {value: gap_classification}
      workflow_stage_ref: {value: verification}
      process_stage_ref: {value: classification}
      start_prompt_ref: &f1s2 {prompt_packet_id: placeholder-F1-S2, packet_role: start_prompt, prompt_task_type: classification, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}
      prompt_packet_refs: [*f1s2]
      placement_rules_applied: ["Classify only observed gaps using the canonical task categories."]
      validation_status: operator_review_recommended
    - sprint_id: S3
      sprint_role: recap_digest_preparation_sprint
      sprint_status: operator_review_needed
      expected_output_type_ref: {value: conformance_report}
      workflow_stage_ref: {value: synthesis}
      process_stage_ref: {value: evidence_summary}
      start_prompt_ref: &f1s3 {prompt_packet_id: placeholder-F1-S3, packet_role: start_prompt, prompt_task_type: synthesis, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}
      prompt_packet_refs: [*f1s3]
      placement_rules_applied: ["Preserve evidence refs and unresolved gaps for raw-flow capture."]
      validation_status: operator_review_recommended
  routing_usage_summary: {status: missing_dependency, provider_target: provider_unspecified}
  workflow_alignment_summary: {status: inferred_from_context, review_required: true}
  FlowRecap_preparation: {status: prepared, capture_home: raw_flow_dump, notes: ["Return actual observations, classifications, artifacts, blockers, and next-step guess."]}
  dependency_status: {prompt_engineering_status: missing_use_degraded_generic_prompt_mode, ai_routing_status: missing_use_provider_unspecified, workflow_process_status: missing_use_operator_review_recommended}
  operator_review_flags: ["Prompt bodies are placeholders; no PromptEngineer or routing output was materialized."]
  validation_status: operator_review_recommended
```
