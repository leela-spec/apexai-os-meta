# Flow Prompt Pack — F2 — fixture

> TEST FIXTURE. Synthetic. Exercises the YAML `sprint_prompt_sequences` path and a
> deliberate provider mix so lane partitioning (V11) has something to partition.

```yaml
flow_prompt_pack_status:
  pack_id: flow_prompt_pack_20260801_F2
  artifact_name: flow_prompt_pack
  execution_day: "2026-08-01"
  flow_id: F2
  project: MasterOfArts
  generation_mode: standard_mode
  pack_status: operator_approved
  validation_status: valid
```

```yaml
source_flow_packet_ref:
  flow_packet_id: flow_packet_2026-08-01_F2
  flow_packet_path_or_slot: ../flow_packet-20260801-F2.md
  flow_id: F2
  project: MasterOfArts
```

```yaml
sprint_prompt_sequences:
  - sprint_id: S1
    sprint_role: first_work_sprint
    sprint_status: active
    sprint_goal: Draft the migration outline.
    prompt_packet_id: pkt_F2_S1_outline
    provider_target: Claude
  - sprint_id: S2
    sprint_role: second_work_or_deepening_sprint
    sprint_status: active
    sprint_goal: Stress-test the outline against constraints.
    prompt_packet_id: pkt_F2_S2_stress
    provider_target: ChatGPT
  - sprint_id: S3
    sprint_role: recap_digest_preparation_sprint
    sprint_status: active
    sprint_goal: Prepare the recap digest.
    prompt_packet_id: pkt_F2_S3_recap
    provider_target: Gemini
```

```yaml
routing_usage_summary:
  routing_recommendation_ref: fixture
  primary_surface_class: subscription_frontier_chat
  quota_or_price_claims_made: false
```

```yaml
workflow_alignment_summary:
  dependency_status: satisfied
```
