---
packet_id: "us-idea-01-sim-009"
role_accountability: alfred
lifecycle_stage: proposal
status: operator_review_needed
target_surface: "apex-meta/fable-orchestrator/fable-execution-best-practices.md (G1-A1) · apex-meta/registry/index.md (G2)"
next_state: "operator_validation recorded per gated item; confirmed items executed via apex-session path"
prerequisites: ["08-promotion-gate.md (artifact verified)", "03-sync-computed-packet.md (drift report)"]
expected_action: "operator: decide G1 and G2"
sources_evidence: ["01-candidate-entry.v2.md (verified, sha256 cd83e576…)", "02-placement-packet.md", "05/06/07/08 review chain"]
uncertainties: ["U1 (scope: all external prompts vs deep-research only) — decide with G1", "UU-3 (rule currently dormant — no external calls) — affects A1 vs A2 choice"]
unresolved_risk: []
stop_condition: "nothing executes without explicit operator answer per item"
operator_validation: not_requested
authority: { state: verified, basis_digest: "sha256:cd83e576d8e5b2caac3f8d40c11bc6d33482a669a50ed8c80be062ec05a13d54", verification_ref: "08-promotion-gate.md" }
---

# Operator gate — two decisions (G1, G2)

## G1 — Durable-knowledge gate (US-IDEA-01 stage 5)

The review-verified idea record distills your prompt-design feedback into one rule: *external-research prompts must name the orchestration system, the defining folders, and the relevant KB(s)*. Options (choose one; this gate authorizes knowledge mutation only — no project/task creation):

- **accept + A1**: record accepted; ONE numbered lesson added to `fable-execution-best-practices.md` §3 area (bounded: one section, no restructure)
- **accept + A2**: record accepted as knowledge only; no file mutation beyond the simulation folder
- **edit / reject / hold**: your wording changes, or the record is dropped/parked

## G2 — Registry materialization

Drift report (real run) says the registry has never been written. Approve `python3 scripts/apex_sync.py registry --root . --dry-run false`? Effect: creates `apex-meta/registry/index.md` with the 8 narm-support-knowledgebase tasks exactly as previewed in 03-sync-computed-packet.md. **approve / decline**
