---
title: "Session Memory and Next Context"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "session-memory-and-next-context"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 95-98; state delta and next session context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C017; clean handoffs and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "state-delta-preservation"
  - "next-cycle-context"
  - "file-state-over-chat-state"
related_entities: []
review_flags:
  - "the term 'session memory' is Phase 2 vocabulary applied to Batch 04's clean-handoff and state-frame claims"
---

# Session Memory and Next Context

## Definition

Session memory and next context is the pattern by which validated outcomes of a completed session are externalized into a compact, bounded artifact that a future session reads at start-up, instead of the future session re-deriving state by rereading chat history. It answers the `project_execution_index` question `how_state_delta_becomes_next_session_context`. Batch 04 does not use the terms "session memory" or "next context" verbatim; it grounds the underlying behavior in the clean-handoff requirements of B04-C009 and the explicit-state-frame requirements of B04-C011 and B04-C017.

## Operating Rules

```yaml
rules:
  - "Only validated/accepted deltas may enter the next-context artifact; candidate or unreviewed material must not."
  - "The next-context artifact must be a bounded file or packet, not a chat transcript or its summary."
  - "A future session should read the next-context packet plus source_refs, not reopen the full prior conversation."
  - "Next-context formation depends on state-delta-preservation having already reduced execution evidence to an accepted delta."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the clean-handoff content shape (B04-C009) and the explicit-state-frame requirement (B04-C011, B04-C017) that this pattern is built from."
    coverage: "Clean handoff fields, atomic task packets, and the general rejection of chat-history reconstruction for high-risk work."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the specific question this concept answers within the project_execution_index."
    coverage: "The 'how_state_delta_becomes_next_session_context' core question and its place after state-delta formation."
```

## Macro / Meso / Micro

### Macro

Apex design explicitly separates durable state from ephemeral conversational memory. The compile plan's `project_execution_index` treats next-session continuity as an artifact problem rather than a memory problem, which echoes Batch 04's broader stance (B04-C017, B04-T002) that conversational continuity is insufficient for high-risk work.

### Meso

B04-C009 defines the content shape a clean handoff must carry: settled state, source priority, a non-redo list, the exact next job, risks, and a success condition — this is effectively the field shape a next-context packet needs. B04-C011 requires explicit state frames and atomic task packets rather than chat-history reconstruction for high-risk execution. B04-T002 states directly that chat continuity is explicitly insufficient for high-risk work, which is the strongest grounding for why next-session context must be file-based rather than memory-based.

### Micro

The label "session memory and next context" is Phase 2 vocabulary drawn from the compile plan's index question at lines 95-98, applied to Batch 04's clean-handoff (B04-C009) and state-frame (B04-C011) claims. Batch 04 itself never names a "session" or a "next-context" artifact; those are this KB's synthesis of the underlying pattern.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Clean handoffs must include settled state, source priority, a non-redo list, the exact next job, risks, and a success condition."
    source_pointer: "B04-C009 (BEST_PRACTICES_v_old.md lines 114-149)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than rely on chat-history reconstruction."
    source_pointer: "B04-C011 (BEST_PRACTICES_v_old.md lines 190-230; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-190)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Chat continuity is explicitly insufficient for high-risk work; this conflicts with any workflow that claims completion from conversational memory alone."
    source_pointer: "B04-T002"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Framing this as a distinct 'session memory and next context' pattern, sequenced after state-delta-preservation, is a Phase 2 synthesis from the project_execution_index question rather than a verbatim Phase 1 concept."
    source_pointer: "phase2-specialized-index-compile-plan-20260702 lines 95-98"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "How does a future session pick up where the last one stopped without rereading everything?"
    leads_to: "claude-code-orchestration-design/concepts/state-delta-preservation.md"
    rationale: "State-delta-preservation is the upstream step that produces the accepted delta this pattern packages into next-session context."
  - related_page: "claude-code-orchestration-design/concepts/next-cycle-context.md"
    relation: "Sibling artifact pattern for cycle-level (rather than single-session-level) continuity."
  - related_page: "claude-code-orchestration-design/concepts/file-state-over-chat-state.md"
    relation: "The general principle (file-based state beats chat-based state) that this pattern instantiates for session continuity specifically."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C009"
    supports: "Clean-handoff content shape mirrored by the next-context packet."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-C011"
    supports: "Explicit state frames over chat-history reconstruction."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "B04-T002"
    supports: "Chat continuity is insufficient for high-risk work, justifying a file-based next-context artifact."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 95-98"
    supports: "Names the state-delta-to-next-session-context question this page answers."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "No canonical file format or schema exists yet for a next-context packet; 'session memory' framing is Phase 2 synthesis, not a named Phase 1 artifact."
    source_pointer: "B04-Q002; phase2-specialized-index-compile-plan-20260702 lines 95-98"
    proposed_handling: "revisit_source"
  - id: U002
    description: "The sequencing implied here (execution evidence -> state delta -> next context) is this KB's organizing structure; Batch 04 does not itself sequence these terms explicitly."
    source_pointer: "phase1-batch04-apex-application-patterns claims B04-C009, B04-C011"
    proposed_handling: "leave_as_gap"
```
