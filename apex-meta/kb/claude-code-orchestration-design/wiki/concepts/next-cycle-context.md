---
title: "Next-Cycle Context"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "next-cycle-context"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 99-111; next cycle context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C017"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "next-day-plan"
  - "session-memory-and-next-context"
  - "status-merge-packet"
related_entities:
  - "precap-week"
  - "precap-next-day"
  - "all-project-status-packet-update"
review_flags: []
---

# Next-Cycle Context

## Definition

Next-cycle context is the compact, accepted-state input that seeds the next planning cycle after a status merge — e.g., what a subsequent `PreCapWeek` or `PreCapNextDay` run reads to begin work. It carries updated status, open decisions, and operator constraints, and deliberately excludes unprocessed raw execution evidence. This concept is a synthesis: Phase 1 batch 04 does not name "next-cycle context" verbatim, but it is the natural answer to the `weekly_routine_case_index` questions `what_each_stage_reads_and_writes` and `canonical_state_vs_temporary_execution_evidence`, read together with the batch's PreCapWeek/PreCapNextDay/FlowRecap/APSU entity chain and the clean-handoff requirements of B04-C009.

## Operating Rules

```yaml
rules:
  - "A planning cycle reads accepted, merged status from the prior cycle, not the full raw evidence trail that produced it."
  - "Open decisions and operator constraints carry forward explicitly; they are not left to be reconstructed from chat history or prior packets."
  - "Candidate or unvalidated evidence is excluded from next-cycle context unless a specific artifact is referenced by pointer."
  - "The clean-handoff fields (settled state, source priority, non-redo list, exact next job, risks, success condition) are the template for what belongs in next-cycle context."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Supplies the weekly_routine_case_index questions this concept answers; it is the primary framing source since no B04 claim names 'next-cycle context' directly."
    coverage: "weekly_routine_case_index core_questions, especially what_each_stage_reads_and_writes and canonical_state_vs_temporary_execution_evidence (lines 106-108)."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the clean-handoff content requirements (B04-C009), the explicit-state-frame requirement (B04-C011), and the entity chain (PreCapWeek, PreCapNextDay, APSU) that this concept generalizes into a 'next cycle' seed."
    coverage: "Claims B04-C009, B04-C011, B04-C017; entities precap-week, precap-next-day, all-project-status-packet-update."
```

## Macro / Meso / Micro

### Macro

Apex's recurring planning loop only works if each cycle starts from a small, accepted snapshot rather than the entire history of what happened. The compile plan frames this generically across any recurring routine: each stage in a workflow reads and writes specific artifacts, and canonical accepted state must stay distinct from temporary execution evidence. Next-cycle context is the name for the artifact that carries the accepted half of that split forward.

### Meso

Phase 1 batch 04's entity chain — `PreCapWeek` (weekly strategic planning), `PreCapNextDay` (daily planning consuming weekly direction and project state), `FlowRecapSkill` (raw evidence to structured recap), and `AllProjectStatusPacketUpdate`/APSU (status merge) — describes a pipeline that ends in a merged status artifact. Next-cycle context is the natural name for what that merged artifact becomes when it is read back in as input to the next `PreCapWeek` or `PreCapNextDay` run. B04-C009's clean-handoff fields (settled state, source priority, non-redo list, exact next job, risks, success condition) describe the shape that seed should take, and B04-C011's requirement for explicit state frames over chat-history reconstruction is the reason it must be a written artifact rather than assumed continuity.

### Micro

The compile plan's `weekly_routine_case_index` lists `what_each_stage_reads_and_writes` and `canonical_state_vs_temporary_execution_evidence` as explicit core questions (lines 106-108), which this page answers for the boundary between one cycle and the next. B04-C009 (`BEST_PRACTICES_v_old.md` lines 114-149) is the direct source for what a clean handoff/seed artifact should contain.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Out-of-mode improvements should be captured explicitly instead of applied silently; clean handoffs should include settled state, source priority, non-redo list, exact next job, risks, and success condition."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C009"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction, which is why next-cycle context must be a written artifact."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C011"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The weekly routine's PreCapWeek/PreCapNextDay/FlowRecap/APSU chain implies a distinct 'next-cycle context' artifact separating accepted merged status from raw execution evidence, even though no B04 claim names this artifact directly."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted (precap-week, precap-next-day, all-project-status-packet-update); phase2-specialized-index-compile-plan-20260702 lines 106-108"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What does the next planning cycle actually read after a status merge?"
    leads_to: "claude-code-orchestration-design/concepts/next-cycle-context.md"
    rationale: "Direct match to weekly_routine_case_index's what_each_stage_reads_and_writes question."
  - related_page: "claude-code-orchestration-design/concepts/next-day-plan.md"
    relation: "Sibling concept: next-cycle-context is the input seed, next-day-plan is the output artifact of the cycle that consumes it."
  - related_page: "claude-code-orchestration-design/concepts/session-memory-and-next-context.md"
    relation: "General session-memory pattern that next-cycle-context specializes for the weekly/daily routine case."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C009"
    supports: "Definition and Meso section: clean-handoff field shape."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Operating Rules: explicit state frame over chat-history reconstruction."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "weekly_routine_case_index core_questions, lines 106-108"
    supports: "Macro section and Key Claim C003."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No B04 claim names 'next-cycle context' as a distinct artifact; this page synthesizes it from the weekly_routine_case_index question framework and the PreCapWeek/PreCapNextDay/APSU entity chain. Treat as a working hypothesis pending a directly named source."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 97-108"
    proposed_handling: "revisit_source"
  - id: U002
    description: "No scheduler or auto-trigger mechanism for cycling into the next context is defined; this remains outside the current KB scope."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 phase2_non_goals, lines 199-211"
    proposed_handling: "leave_as_gap"
```
