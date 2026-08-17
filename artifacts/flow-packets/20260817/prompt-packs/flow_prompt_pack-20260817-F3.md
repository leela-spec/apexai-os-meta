```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_prompt_pack
  gate: G2
  packet_id: flow-prompt-pack-20260817-F3
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  expected_action: "After G2 confirmation, use degraded prompt placeholders for F3 current-main audit/rebaseline; do not treat them as PromptEngineer-approved prompts."
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

```yaml
flow_prompt_pack:
  pack_id: flow_prompt_pack_20260817_F3
  artifact_name: flow_prompt_pack
  created_or_updated_at: "2026-08-17"
  execution_day: "2026-08-17"
  flow_id: F3
  project: Apex
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_pack_policy:
    storage_policy: {one_file_per_flow_prompt_pack: true, embedded_in_daily_plan: false, referenced_from_flow_packet: true}
    prompt_system_policy: {one_primary_prompt_system_only: true, alternatives_allowed_by_default: false, follow_up_prompts_allowed: true, max_follow_up_prompts_per_sprint: 2}
    prompt_capture_policy: {light_capture_hints_allowed: true, mandatory_machine_readable_capture_block_inside_every_prompt: false, canonical_capture_home: raw_flow_dump}
    provider_rationale_policy: {provider_rationale_required: true, prompt_design_rationale_required: true, rationale_source: degraded_generic_prompt_mode_note}
    fallback_policy: {fallback_notes_allowed: true, fallback_prompt_system_allowed_by_default: false, fallback_requires_operator_review: true}
  source_flow_packet_ref: {flow_packet_id: flow_packet_20260817_F3, flow_packet_path_or_slot: artifacts/flow-packets/20260817/flow_packet-20260817-F3.md, flow_id: F3, project: Apex}
  daily_plan_ref: {next_day_plan_id: next_day_plan_2026_08_17_w34_monday, next_day_plan_path_or_slot: artifacts/next-day-plans/next_day_plan-20260817.md}
  sprint_prompt_sequences:
    - {sprint_id: S1, sprint_role: first_work_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: implementation_inventory}, workflow_stage_ref: {value: audit}, process_stage_ref: {value: current_state_inventory}, start_prompt_ref: &f3s1 {prompt_packet_id: placeholder-F3-S1, packet_role: start_prompt, prompt_task_type: audit, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f3s1], placement_rules_applied: ["Use current main as authority; historical handovers are non-current evidence."], validation_status: operator_review_recommended}
    - {sprint_id: S2, sprint_role: second_work_or_deepening_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: verification_matrix}, workflow_stage_ref: {value: verification}, process_stage_ref: {value: architecture_and_behavior_check}, start_prompt_ref: &f3s2 {prompt_packet_id: placeholder-F3-S2, packet_role: start_prompt, prompt_task_type: verification, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f3s2], placement_rules_applied: ["Separate verified facts, unresolved risks, and superseded historical claims."], validation_status: operator_review_recommended}
    - {sprint_id: S3, sprint_role: recap_digest_preparation_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: implementation_baseline}, workflow_stage_ref: {value: synthesis}, process_stage_ref: {value: baseline_compilation}, start_prompt_ref: &f3s3 {prompt_packet_id: placeholder-F3-S3, packet_role: start_prompt, prompt_task_type: synthesis, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f3s3], placement_rules_applied: ["Cite current-main paths close to each material finding."], validation_status: operator_review_recommended}
  routing_usage_summary: {status: missing_dependency, provider_target: provider_unspecified}
  workflow_alignment_summary: {status: inferred_from_context, review_required: true}
  FlowRecap_preparation: {status: prepared, capture_home: raw_flow_dump, notes: ["Return sources inspected, verified behavior, risk disposition, baseline artifact, unresolved questions."]}
  dependency_status: {prompt_engineering_status: missing_use_degraded_generic_prompt_mode, ai_routing_status: missing_use_provider_unspecified, workflow_process_status: missing_use_operator_review_recommended}
  operator_review_flags: ["Prompt bodies are placeholders; no PromptEngineer or routing output was materialized."]
  validation_status: operator_review_recommended
```
