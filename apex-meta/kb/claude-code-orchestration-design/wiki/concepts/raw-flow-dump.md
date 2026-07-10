---
title: "Raw Flow Dump"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "raw-flow-dump"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 109-110; raw dumps and context bloat"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011; evidence and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "flow-packet"
  - "flow-recap-packet"
  - "compiled-kb-before-raw-source"
related_entities:
  - "flow-recap-skill"
review_flags: []
---

# Raw Flow Dump

## Definition

A raw flow dump is unstructured, unprocessed execution transcript — the messy, full-detail record of what actually happened during a flow — held as temporary evidence rather than durable project memory. It is presented here as the anti-pattern that flow-packet and state-delta discipline exist to prevent: durable context should be built from compiled, recap-level artifacts, not from re-reading raw dumps every cycle. This concept is a working hypothesis rather than a verbatim B04 claim: no source in batch 04 uses the phrase "raw flow dump," but the compile plan's `weekly_routine_case_index` names the underlying concern directly (`how_raw_dumps_are_prevented_from_bloating_future_context`), and B04-C009's requirement that out-of-mode improvements be captured explicitly (rather than silently folded in) is the closest direct claim describing why raw, unprocessed output cannot be trusted as accepted state.

## Operating Rules

```yaml
rules:
  - "A raw flow dump is acceptable as a transient artifact immediately after execution, before recap processing."
  - "A raw flow dump must never be read directly as accepted state by a future planning cycle; it must first be converted into a structured recap."
  - "Out-of-mode improvements or deviations that show up inside a raw dump must be captured explicitly as named items, not silently absorbed into future behavior."
  - "Retention of raw dumps (how long they are kept, where) is a policy question, not resolved by this KB."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the underlying concern directly as a weekly_routine_case_index core question, and frames the contrast between compiled KB pages and raw sources as a distinct token_economy_and_information_design_index question."
    coverage: "weekly_routine_case_index question how_raw_dumps_are_prevented_from_bloating_future_context (line 108); token_economy_and_information_design_index question compiled_kb_pages_vs_raw_sources (line 128)."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the closest direct claims: clean-handoff discipline (B04-C009) and the requirement for explicit state frames over chat-history/raw reconstruction (B04-C011), both of which motivate treating raw execution output as provisional rather than accepted."
    coverage: "Claims B04-C009 and B04-C011; entity flow-recap-skill (digest skill that converts raw flow execution evidence into structured recap memory)."
```

## Macro / Meso / Micro

### Macro

The KB's token-economy framing distinguishes compiled KB pages from raw sources as a general principle: future sessions should be able to work from compiled, ranked, source-pointing pages instead of re-reading entire raw corpora. Raw flow dump is the project-execution instance of "raw source" in that framing — the un-digested output of a single flow run.

### Meso

The `FlowRecapSkill` entity exists specifically to convert raw flow execution evidence into structured recap memory (B04 entities_extracted), which only makes sense if the raw dump itself is not fit to be read directly as durable state. B04-C009 reinforces this from the doctrine side: out-of-mode improvements must be captured explicitly instead of applied silently, and clean handoffs require settled state, source priority, non-redo list, exact next job, risks, and success condition — none of which a raw, unprocessed transcript provides on its own. B04-C011's requirement for explicit state frames over chat-history reconstruction applies the same logic: raw, ambient records are exactly what state frames are designed to replace.

### Micro

`BEST_PRACTICES_v_old.md` lines 114-149 (B04-C009) is the direct source describing clean-handoff content requirements, implicitly contrasting with an unprocessed dump. The compile plan's weekly_routine_case_index line 108 (`how_raw_dumps_are_prevented_from_bloating_future_context`) is the direct textual origin of the term "raw dumps" used in this KB's own framing, even though it originates in the compile plan rather than in a B04 source claim.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Out-of-mode improvements should be captured explicitly instead of applied silently; clean handoffs should include settled state, source priority, non-redo list, exact next job, risks, and success condition."
    source_pointer: "phase1-batch04-apex-application-patterns claim B04-C009"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "The weekly_routine_case_index poses 'how raw dumps are prevented from bloating future context' as an explicit core question, establishing raw-dump containment as a named orchestration concern for this KB."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 line 108"
    confidence: "medium"
    claim_label: "working_hypothesis"
  - claim_id: C003
    claim: "FlowRecapSkill exists as a digest skill that converts raw flow execution evidence into structured recap memory, implying raw flow output is treated as provisional pending recap rather than as accepted state."
    source_pointer: "phase1-batch04-apex-application-patterns entities_extracted (flow-recap-skill)"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Why shouldn't a future planning cycle just read the full execution transcript directly?"
    leads_to: "claude-code-orchestration-design/concepts/raw-flow-dump.md"
    rationale: "Direct match to compiled_kb_pages_vs_raw_sources and how_raw_dumps_are_prevented_from_bloating_future_context."
  - related_page: "claude-code-orchestration-design/concepts/flow-recap-packet.md"
    relation: "Contrast concept: flow-recap-packet is the compiled, structured counterpart that raw-flow-dump is converted into."
  - related_page: "claude-code-orchestration-design/concepts/flow-packet.md"
    relation: "Flow-packet scopes the execution unit that produces a raw flow dump as its byproduct."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C009"
    supports: "Definition and Meso section: clean-handoff requirements contrasted with unprocessed raw output."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Meso section: explicit state frames over chat-history/raw reconstruction."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "entities_extracted flow-recap-skill"
    supports: "Meso section and Key Claim C003: FlowRecapSkill's role in digesting raw evidence."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "line 108 (weekly_routine_case_index) and line 128 (token_economy_and_information_design_index)"
    supports: "Definition and Key Claim C002: named orchestration concern."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No B04 source claim uses the phrase 'raw flow dump' or defines it as a named artifact; the term and its anti-pattern framing are synthesized from the compile plan's index question wording. Confidence and claim_label are set to medium/working_hypothesis to reflect this."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 line 108"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Retention policy for raw dumps (how long kept, where stored) is explicitly out of scope for this compile pass."
    source_pointer: "phase1-batch04-apex-application-patterns phase 2 non-goals framing (see compile plan phase2_non_goals, lines 199-211)"
    proposed_handling: "leave_as_gap"
```
