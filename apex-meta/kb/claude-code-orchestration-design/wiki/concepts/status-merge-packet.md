---
title: "Status Merge Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "status-merge-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; canonical state vs temporary execution evidence"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C011, B04-C014"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
related_concepts:
  - "state-delta-preservation"
  - "flow-recap-packet"
  - "candidate-is-not-accepted-truth"
related_entities:
  - "all-project-status-packet-update"
review_flags:
  - "APSU entity carries only medium confidence in Phase 1 entities_extracted; conflict-exposure behavior is inferred, not stated"
---

# Status Merge Packet

## Definition

A status merge packet is the artifact/process modeled on Apex's `AllProjectStatusPacketUpdate` (APSU) entity, which Batch 04 describes as a "status-merge process that consumes flow recap packets and updates project status" (entities_extracted, confidence medium). It is the mechanism that reconciles validated flow-recap deltas into canonical project status, and it answers the `project_execution_index`'s `canonical_state_vs_temporary_execution_evidence` question.

## Operating Rules

```yaml
rules:
  - "Must only consume accepted/validated recap deltas, not raw or candidate evidence."
  - "Should expose conflicts between competing deltas for review rather than silently overwriting prior status (inferred from the closure/verification discipline in B04-C011 and B04-C014, not stated directly for APSU)."
  - "Must write updated status plus a next-context seed, not just an append-only log entry."
  - "Must not itself author new evidence — it merges and reconciles, it does not execute flows or investigate."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Names the APSU entity and its role directly (entities_extracted), and supplies the loop context (B04-C001) plus closure discipline (B04-C011, B04-C014) this page extends."
    coverage: "AllProjectStatusPacketUpdate entity role, PreCap/FlowRecap/APSU loop mapping, and state-frame/closure requirements."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the canonical-state-vs-temporary-evidence question this packet resolves."
    coverage: "project_execution_index and weekly_routine_case_index questions on canonical vs temporary state."
```

## Macro / Meso / Micro

### Macro

Batch 04 names `AllProjectStatusPacketUpdate` (APSU) as a status-merge process within Apex's PreCap/FlowRecap/APSU loop, confidence medium. The compile plan's `project_execution_index` treats "canonical state vs. temporary execution evidence" as a live open design question, and this packet is the mechanism that promotes validated temporary evidence into canonical state.

### Meso

B04-C001 places APSU within the PreCap/FlowRecap/APSU loop that Apex maps into discrete Claude skills, distinct from `OperatorExecutesPlannedFlow`, which stays a human action. B04-C011 (explicit state frames rather than chat-history reconstruction) and B04-C014 (file-output/task-closure requirements before success is claimed) together supply the verification discipline a merge step must satisfy before it may update canonical status.

### Micro

The APSU entity itself carries only medium confidence in Phase 1's entities_extracted section — it is a role description, not a detailed spec. This page's specific claims about conflict exposure and accept-only-validated-input behavior are a Phase 2 extrapolation of B04-C011/B04-C014's general closure discipline applied to the APSU role, not a directly stated APSU behavior.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "AllProjectStatusPacketUpdate (APSU) is an Apex process-skill entity whose role is a status-merge process that consumes flow recap packets and updates project status."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted 'all-project-status-packet-update'"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "APSU sits within the PreCap/FlowRecap/APSU loop that Apex maps into discrete Claude skills, while OperatorExecutesPlannedFlow remains a human action."
    source_pointer: "B04-C001 (Apex_Alfred_Skill_Definition_Guide.md lines 5-18)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "A status-merge step should expose conflicts for review rather than silently resolve them, and should only accept validated deltas as input."
    source_pointer: "extrapolated from B04-C011 and B04-C014 closure discipline"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What merges multiple recap outputs into one project status view?"
    leads_to: "claude-code-orchestration-design/concepts/state-delta-preservation.md"
    rationale: "State-delta-preservation supplies the validated deltas a status merge packet consumes."
  - related_page: "claude-code-orchestration-design/concepts/flow-recap-packet.md"
    relation: "The upstream recap artifact that a status-merge packet reads."
  - related_page: "claude-code-orchestration-design/concepts/candidate-is-not-accepted-truth.md"
    relation: "The claim-status distinction that gates what a status-merge packet may accept as input."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entities_extracted 'all-project-status-packet-update'"
    supports: "APSU's role as a status-merge process."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C001"
    supports: "APSU's place in the PreCap/FlowRecap/APSU loop."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C011, B04-C014"
    supports: "Closure/verification discipline this page extrapolates onto the status-merge step."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 99-111"
    supports: "Canonical-state-vs-temporary-evidence framing this packet resolves."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The APSU entity carries only medium confidence in Phase 1 — it is a role description, not a detailed spec, and no runtime or schema exists."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted 'all-project-status-packet-update'"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Conflict-exposure and accept-only-validated behavior is a working hypothesis extrapolated from general closure claims, not a directly stated APSU behavior."
    source_pointer: "B04-C011, B04-C014"
    proposed_handling: "ask_operator"
```
