---
title: "Next-Day Plan"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "next-day-plan"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; weekly routine stages"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C001, B04-C004, B04-C005"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "next-cycle-context"
  - "flow-packet"
  - "weekly-plan-packet"
related_entities:
  - "precap-next-day"
  - "precap-week"
review_flags: []
---

# Next-Day Plan

## Definition

A next-day plan is the artifact that translates weekly direction and current project state into a scoped set of executable flow packets for a near-term workday. It corresponds to the `PreCapNextDay` entity in Phase 1 batch 04 — a daily executable planning skill that consumes weekly direction and project state (entities_extracted, `precap-next-day`) — read through the `weekly_routine_case_index` question `what_each_stage_reads_and_writes`. No B04 claim defines "next-day plan" as a named artifact verbatim; the page synthesizes the artifact shape from the entity role plus the general artifact-contract and operator-gate claims (B04-C001, B04-C004, B04-C005).

## Operating Rules

```yaml
rules:
  - "A next-day plan is produced only when a near-term workday needs scoped flows before execution; it is not produced merely to record completed work."
  - "It reads the weekly plan packet and current project state as its canonical inputs."
  - "It writes a bounded plan plus a list of flow packets and prompt-pack references, not the full prompts themselves."
  - "Operator approval separates the plan (proposed) from human execution (accepted), consistent with the operator-gate pattern."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the PreCapNextDay entity definition and the artifact-contract (B04-C004) and operator-gate (B04-C005) claims that define how the plan connects to upstream weekly direction and downstream flow execution."
    coverage: "Claims B04-C001, B04-C004, B04-C005; entity precap-next-day."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Supplies the weekly_routine_case_index question framework that names the stage boundaries this artifact sits between."
    coverage: "weekly_routine_case_index core_questions, lines 99-108."
```

## Macro / Meso / Micro

### Macro

Apex's recurring routine separates strategic weekly direction from tactical daily execution. The compile plan frames this as a generic orchestration-stage question — which parts of a recurring routine are generic stages, which are specific to the weekly case, and what each stage reads and writes. A next-day plan is the concrete stage boundary between weekly direction and daily flow execution.

### Meso

Apex maps its process loop into discrete skills, and `OperatorExecutesPlannedFlow` remains a human action with a documented output contract rather than a skill file (B04-C001) — meaning the next-day plan must produce something a human can pick up and execute, not just internal agent state. Because Apex skills connect through artifact contracts rather than direct calls (B04-C004), the next-day plan is written to a canonical slot that downstream flow execution reads. Because operator gates are first-class (B04-C005), the plan is a proposal until the operator approves it for execution.

### Micro

Entity `precap-next-day` (Phase 1 batch 04, entities_extracted) is described as "a daily executable planning skill that consumes weekly direction and project state" at medium confidence. The compile plan's weekly_routine_case_index (lines 99-108) frames the surrounding questions: which subprocedures could be skills, where ephemeral subagents help, which steps remain operator-gated, and what each stage reads and writes.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex maps the PreCap/FlowRecap/APSU loop into discrete Claude skills, while OperatorExecutesPlannedFlow remains a human action with a documented output contract rather than a skill file."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C001"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex skills are connected by artifact contracts rather than direct calls: one skill writes an artifact to a canonical slot and downstream skills read that artifact."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C004"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "PreCapNextDay, as a daily executable planning skill consuming weekly direction and project state, is the entity that produces the next-day plan artifact; this specific artifact framing is synthesized from the entity role and the weekly_routine_case_index question set rather than a direct B04 claim."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted (precap-next-day); phase2-specialized-index-compile-plan-20260702 lines 99-108"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What artifact bridges weekly direction and a specific day's executable flows?"
    leads_to: "claude-code-orchestration-design/concepts/next-day-plan.md"
    rationale: "Direct answer to the weekly_routine_case_index staging questions."
  - related_page: "claude-code-orchestration-design/concepts/flow-packet.md"
    relation: "A next-day plan's output is a list of flow packets; flow-packet is the unit it scopes."
  - related_page: "claude-code-orchestration-design/concepts/weekly-plan-packet.md"
    relation: "Upstream input: the next-day plan reads the weekly plan packet."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C001"
    supports: "Meso section: skill-vs-human-action boundary for OperatorExecutesPlannedFlow."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C004"
    supports: "Operating Rules: artifact-contract write/read pattern."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C005"
    supports: "Operating Rules: operator gate separating plan from execution."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "weekly_routine_case_index core_questions, lines 99-108"
    supports: "Macro/Meso framing of stage boundaries."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No B04 claim names 'next-day plan' as a distinct artifact; this concept is synthesized from the PreCapNextDay entity role and the weekly_routine_case_index question set. Treat the exact artifact shape as a working hypothesis."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted (precap-next-day)"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The exact daily planner implementation (filesystem slot, scheduling trigger) remains outside the current KB scope and is explicitly a Phase 2 non-goal (production runtime setup)."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 phase2_non_goals, lines 199-211"
    proposed_handling: "leave_as_gap"
```
