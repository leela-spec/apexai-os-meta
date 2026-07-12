# normalized-raw-flow-dump-F3

```yaml
handoff_envelope:
  envelope_version: 1
  packet_type: normalized_raw_flow_dump
  gate: G3
  packet_id: "normalized_raw_flow_dump-20260713-F3"
  produced_by: fable-orchestrator-closure-verification
  accountability: meta_ops
  lifecycle_stage: computed
  status: complete
  target_surface: none
  next_state: "F3 system-verification evidence is available to FlowRecap; no project status is accepted."
  prerequisites: [artifacts/flow-packets/20260713/flow_packet-20260713-F3.md]
  expected_action: "flow-recap consumes this dump with its flow_packet"
  sources: [apex-meta/fable-orchestrator/simulations/weekly-loop-20260713-F3.md]
  uncertainties: ["Bootstrap project-state and calendar inputs remain unavailable."]
  unresolved_risk: none
  stop_condition: "Do not interpret this evidence as an accepted project-state change."
  authority: {state: candidate, basis_digest: null, verification_ref: null}
  operator_validation: not_requested
```

```yaml
normalized_raw_flow_dump:
  dump_id: normalized_raw_flow_dump_20260713_F3
  artifact_name: normalized_raw_flow_dump
  execution_day: "2026-07-13"
  flow_id: F3
  source_flow_packet_ref: artifacts/flow-packets/20260713/flow_packet-20260713-F3.md
  completion_state: done
  evidence_sources: [apex-meta/fable-orchestrator/simulations/weekly-loop-20260713-F3.md]
  operator_summary: "Executed live F3 closure verification: 10 agents, 11 skills, routing and handoff paths resolved."
  produced_outputs:
    - apex-meta/fable-orchestrator/simulations/weekly-loop-20260713-F3.md
    - artifacts/flow-recap-packets/flow_recap_packet-20260713-F3.md
  decisions_made: ["Do not run a status merge: G4 is unconfirmed and durable state must remain untouched."]
  blockers_or_failures: []
  open_questions: ["Calendar and accepted project-state context are absent in this bootstrap cycle."]
  model_usage_notes: ["Codex local repository inspection; provider quota totals unavailable."]
  normalization_confidence: high
  validation_status: valid_with_warnings
```
