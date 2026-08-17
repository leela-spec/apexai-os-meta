```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_prompt_pack
  gate: G2
  packet_id: flow-prompt-pack-20260817-F2
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: partial
  target_surface: none
  expected_action: "After G2 confirmation, use degraded prompt placeholders for F2 source discovery/reconciliation; do not treat them as PromptEngineer-approved prompts."
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

```yaml
flow_prompt_pack:
  pack_id: flow_prompt_pack_20260817_F2
  artifact_name: flow_prompt_pack
  created_or_updated_at: "2026-08-17"
  execution_day: "2026-08-17"
  flow_id: F2
  project: MasterOfArts
  generation_mode: degraded_generic_prompt_mode
  pack_status: operator_review_recommended
  prompt_pack_policy:
    storage_policy: {one_file_per_flow_prompt_pack: true, embedded_in_daily_plan: false, referenced_from_flow_packet: true}
    prompt_system_policy: {one_primary_prompt_system_only: true, alternatives_allowed_by_default: false, follow_up_prompts_allowed: true, max_follow_up_prompts_per_sprint: 2}
    prompt_capture_policy: {light_capture_hints_allowed: true, mandatory_machine_readable_capture_block_inside_every_prompt: false, canonical_capture_home: raw_flow_dump}
    provider_rationale_policy: {provider_rationale_required: true, prompt_design_rationale_required: true, rationale_source: degraded_generic_prompt_mode_note}
    fallback_policy: {fallback_notes_allowed: true, fallback_prompt_system_allowed_by_default: false, fallback_requires_operator_review: true}
  source_flow_packet_ref: {flow_packet_id: flow_packet_20260817_F2, flow_packet_path_or_slot: artifacts/flow-packets/20260817/flow_packet-20260817-F2.md, flow_id: F2, project: MasterOfArts}
  daily_plan_ref: {next_day_plan_id: next_day_plan_2026_08_17_w34_monday, next_day_plan_path_or_slot: artifacts/next-day-plans/next_day_plan-20260817.md}
  sprint_prompt_sequences:
    - {sprint_id: S1, sprint_role: first_work_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: source_inventory}, workflow_stage_ref: {value: discovery}, process_stage_ref: {value: source_location}, start_prompt_ref: &f2s1 {prompt_packet_id: placeholder-F2-S1, packet_role: start_prompt, prompt_task_type: discovery, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f2s1], placement_rules_applied: ["Locate sources first; do not invent prior decisions."], validation_status: operator_review_recommended}
    - {sprint_id: S2, sprint_role: second_work_or_deepening_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: source_reconciliation}, workflow_stage_ref: {value: analysis}, process_stage_ref: {value: variant_comparison}, start_prompt_ref: &f2s2 {prompt_packet_id: placeholder-F2-S2, packet_role: start_prompt, prompt_task_type: comparison, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f2s2], placement_rules_applied: ["Preserve conflicts and evidence paths."], validation_status: operator_review_recommended}
    - {sprint_id: S3, sprint_role: recap_digest_preparation_sprint, sprint_status: operator_review_needed, expected_output_type_ref: {value: baseline_record}, workflow_stage_ref: {value: synthesis}, process_stage_ref: {value: baseline_selection}, start_prompt_ref: &f2s3 {prompt_packet_id: placeholder-F2-S3, packet_role: start_prompt, prompt_task_type: synthesis, provider_target: provider_unspecified, prompt_packet_path_or_slot: degraded_generic_prompt_mode}, prompt_packet_refs: [*f2s3], placement_rules_applied: ["State the selected continuation baseline and exact paths."], validation_status: operator_review_recommended}
  routing_usage_summary: {status: missing_dependency, provider_target: provider_unspecified}
  workflow_alignment_summary: {status: inferred_from_context, review_required: true}
  FlowRecap_preparation: {status: prepared, capture_home: raw_flow_dump, notes: ["Return sources found, conflicts, selected baseline, evidence paths, unresolved questions."]}
  dependency_status: {prompt_engineering_status: missing_use_degraded_generic_prompt_mode, ai_routing_status: missing_use_provider_unspecified, workflow_process_status: missing_use_operator_review_recommended}
  operator_review_flags: ["Prompt bodies are placeholders; no PromptEngineer or routing output was materialized."]
  validation_status: operator_review_recommended
```
