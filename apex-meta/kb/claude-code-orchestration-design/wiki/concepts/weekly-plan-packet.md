---
title: "Weekly Plan Packet"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "weekly-plan-packet"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; stage reads and writes"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C004, B04-C005"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "behavioral_inference"
status: "active"
related_concepts:
  - "next-day-plan"
  - "weekly-routine-workflow-case"
  - "operator-confirmed-mutation"
related_entities:
  - "precap-week"
  - "precap-next-day"
review_flags:
  - "PreCapWeek/PreCapNextDay entity confidence is medium in Phase 1; no field schema is specified"
---

# Weekly Plan Packet

## Definition

A weekly plan packet is the artifact produced by Apex's weekly strategic-planning skill, `PreCapWeek` ("Weekly strategic planning skill in the Apex orchestration loop," Batch 04 entities_extracted, confidence medium), that carries stable weekly direction, priorities, and constraints into daily planning. It is consumed by `PreCapNextDay`, described as the "Daily executable planning skill that consumes weekly direction and project state."

## Operating Rules

```yaml
rules:
  - "Must be produced before daily/next-day planning consumes it; weekly direction precedes daily execution."
  - "Must read prior status and operator intent as inputs before producing weekly direction."
  - "Should pause for explicit operator approval where the transition requires validation, consistent with Apex's general operator-gate rule (B04-C005)."
  - "Must be handed off as a bounded artifact (direction plus constraints) rather than as freeform strategy discussion."
  - "Downstream daily planning should read this packet instead of re-deriving strategy each day."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Names the PreCapWeek/PreCapNextDay entities directly and supplies the artifact-contract (B04-C004) and operator-gate (B04-C005) rules this packet follows."
    coverage: "PreCapWeek and PreCapNextDay entity roles; PreCap/FlowRecap/APSU loop mapping; artifact-contract and operator-gate claims."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the stage-reads-and-writes question this packet is one instance of."
    coverage: "weekly_routine_case_index question on what each stage reads and writes."
```

## Macro / Meso / Micro

### Macro

Batch 04's entities_extracted names `PreCapWeek` as Apex's weekly strategic-planning skill and `PreCapNextDay` as the daily planning skill that consumes weekly direction and project state (both confidence medium). Together these define an upstream-to-downstream packet relationship that this page generalizes as a "weekly plan packet."

### Meso

B04-C001 places PreCapWeek within the PreCap/FlowRecap/APSU loop that Apex maps into discrete Claude skills. B04-C004 (artifact contracts connect skills, not direct calls) and B04-C005 (operator gates are first-class for transitions requiring validation) together imply that the weekly-to-daily handoff should occur via an explicit artifact, and that this artifact plausibly requires operator confirmation given B04-C005's rule that skills must pause for explicit approval before downstream use when validation is required.

### Micro

PreCapWeek and PreCapNextDay both carry only medium confidence in Phase 1 (entities_extracted, not a detailed spec). The "packet" framing used here — weekly direction, priorities, and constraints as an explicit artifact with defined reads/writes — is a Phase 2 generalization of the entity role descriptions; Batch 04 does not spell out a field schema for this packet.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "PreCapWeek is Apex's weekly strategic-planning skill in the orchestration loop, and PreCapNextDay is the daily planning skill that consumes weekly direction and project state."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted 'precap-week', 'precap-next-day'"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex skills are connected by artifact contracts, and operator gates are first-class for transitions requiring validation."
    source_pointer: "B04-C004, B04-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Generalizing PreCapWeek's output into a reusable 'weekly plan packet' pattern (direction, priorities, constraints, handoff to daily planning) is a Phase 2 working hypothesis, since Batch 04 does not spell out the packet's field schema."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 99-111"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What carries weekly strategy into daily planning without re-deriving it each day?"
    leads_to: "claude-code-orchestration-design/concepts/next-day-plan.md"
    rationale: "Next-day-plan is the downstream artifact PreCapNextDay produces after consuming this weekly plan packet."
  - related_page: "claude-code-orchestration-design/concepts/weekly-routine-workflow-case.md"
    relation: "The broader workflow case this packet is one stage of."
  - related_page: "claude-code-orchestration-design/concepts/operator-confirmed-mutation.md"
    relation: "The gate pattern that plausibly governs approval of weekly direction before it becomes binding."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entities_extracted 'precap-week'"
    supports: "PreCapWeek's role as weekly strategic-planning skill."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entities_extracted 'precap-next-day'"
    supports: "PreCapNextDay's role consuming weekly direction and project state."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C001, B04-C004, B04-C005"
    supports: "Loop mapping, artifact-contract handoff, and operator-gate rule this packet follows."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 99-111"
    supports: "Stage-reads-and-writes question this page instantiates."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "PreCapWeek/PreCapNextDay entity confidence is medium, not high, in Phase 1 — role descriptions exist but no detailed packet schema."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted 'precap-week', 'precap-next-day'"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Whether weekly-plan-packet approval is truly operator-gated (versus skill-internal) is inferred from B04-C005's general rule, not stated specifically for PreCapWeek."
    source_pointer: "B04-C005"
    proposed_handling: "ask_operator"
```
