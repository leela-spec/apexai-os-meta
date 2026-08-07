# flow_packet-20260801-F2

> TEST FIXTURE. Synthetic, not a real flow packet. Exists so V1/V2/V11 can assert
> against a pack whose refs actually resolve -- no live pack does yet (finding F2).

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: flow_packet
  gate: none
  packet_id: "flow_packet-20260801-F2"
  produced_by: apex-precap-next-day
  accountability: meta_ops
  lifecycle_stage: proposal
  status: planned
  target_surface: none
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

```yaml
flow_packet:
  packet_id: flow_packet_2026-08-01_F2
  artifact_name: flow_packet
  created_or_updated_at: "2026-07-31"
  execution_day: "2026-08-01"
  generation_mode: standard_mode
  review_status: valid

  flow_identity:
    flow_id: F2
    flow_slot: F2
    project: MasterOfArts
    flow_role: app_product_or_system_work
    flow_status: planned
    default_flow: true

  flow_sprint_plan:
    sprint_policy: default_three_sprints
    sprint_count: 3
    sprints: []
    recap_digest_required: true

  prompt_pack_ref:
    flow_prompt_pack_path: artifacts/flow-packets/20260801/prompt-packs/flow_prompt_pack-20260801-F2.md
    prompt_pack_status: operator_approved
    prompt_pack_authority: references/flow-prompt-pack-contract.md

  validation_status: valid
```

```yaml
skipped_flow_marker_template:
  marker_id: skipped_flow_marker_2026-08-01_F2
  flow_id: F2
  execution_day: "2026-08-01"
  skip_status: not_skipped
```
