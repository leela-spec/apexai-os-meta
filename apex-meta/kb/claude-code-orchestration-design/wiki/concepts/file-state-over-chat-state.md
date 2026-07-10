---
title: "File State over Chat State"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "file-state-over-chat-state"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; file_state_over_chat_state"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C011, B04-C014 and tension B04-T002"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "current-state-vs-target-state"
  - "gated-write-side-mutation"
related_entities: []
review_flags: []
---

# File State over Chat State

## Definition

Durable, verifiable task state belongs in files or file-like artifacts that can be reopened, re-read, and checked — not in the transient conversational context of a chat session. A claim of completion or progress is only trustworthy once it is anchored to a written artifact that can be fetched back and inspected; conversational continuity alone is explicitly called out in Phase 1 batch 04 as insufficient for high-risk work.

## Operating Rules

```yaml
rules:
  - "Any fact that must survive past the current turn or session gets written to a file/artifact rather than left implicit in chat."
  - "A claim of task completion requires reading back the written artifact (fetch-back) before being reported as done."
  - "A new session, agent, or reviewer must be able to resume or audit work from files alone, without replaying prior chat history."
  - "Chat-only assertions of \"done\" are treated as unverified candidates until file evidence exists (see candidate-is-not-accepted-truth)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Provides the direct, high-confidence claims and the explicit contradiction (B04-T002) this pattern is named for: state frames over chat reconstruction, and fetch-back/closure proof requirements."
    coverage: "State frames, atomic task packets, file-output/task-closure contracts, chat-continuity insufficiency."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames this as an explicit token_economy_and_information_design_index concern (file-based state preventing chat-history drift)."
    coverage: "how_file_based_state_prevents_chat_history_drift core question."
```

## Macro / Meso / Micro

### Macro

This is one of the load-bearing constraints across the whole KB: both the `handoff_contract_index` and the `token_economy_and_information_design_index` depend on the idea that state travels through artifacts, not conversation, so that context can be safely dropped between turns, sessions, and agents without losing anything that matters.

### Meso

This is the general principle behind fetch-back validation (B04-C014) and explicit state frames/atomic task packets (B04-C011). B04-T002 makes the contrapositive explicit: chat continuity is called out as insufficient for high-risk work, and this conflicts directly with any workflow that claims completion from conversational memory alone.

### Micro

B04-C011 (source pointers: BEST_PRACTICES_v_old.md lines 190-230; APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md lines 118-190) requires explicit state frames and atomic task packets rather than chat-history reconstruction for high-risk execution. B04-C014 requires complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed. B04-T002 states plainly that Apex prompt/workflow sources require explicit state blocks, atomic payloads, gates, and fetch-back proof, which conflicts with any workflow that claims completion from conversational memory alone.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "High-risk execution should carry explicit state frames and atomic task packets rather than relying on chat-history reconstruction."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C011"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "File-output and task-closure contracts require complete content, scope proof, target-root validation, fetch-back, and explicit validation status before success is claimed."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C014"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Chat continuity is explicitly insufficient for high-risk work; this conflicts with any workflow that claims completion from conversational memory alone."
    source_pointer: "phase1-batch04-apex-application-patterns.md tension B04-T002"
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "Why can't an agent just trust its own chat history to know what state a project is in?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/file-state-over-chat-state.md"
    rationale: "This page states the rule and its direct source basis (B04-T002) for why chat state is insufficient."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/current-state-vs-target-state.md"
    relation: "Current state must be read from durable files, not chat memory, for the current/target pairing to be trustworthy."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "A confirmed mutation record is itself a file-state artifact, produced only after fetch-back validation."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C011"
    supports: "Explicit state frames and atomic task packets over chat-history reconstruction."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C014"
    supports: "Fetch-back and explicit validation status requirements before success is claimed."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "tension B04-T002"
    supports: "Direct statement that chat continuity is insufficient for high-risk work."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 124-137"
    supports: "Framing as a token_economy_and_information_design_index concern (file-based state preventing chat-history drift)."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This Phase 2 KB compile itself only writes KB wiki/log artifacts; it does not create the runtime fetch-back tooling or hooks that would enforce this rule mechanically. The general rule is source-backed, but its runtime enforcement remains unbuilt and should be reviewed by the operator before assuming it is already enforced anywhere."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 199-211 (phase2_non_goals)"
    proposed_handling: "ask_operator"
  - id: U002
    description: "Exact file/state-frame formats are not standardized across Phase 1 sources; multiple prompt/workflow sources describe similar but not identical schemas."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q003"
    proposed_handling: "revisit_source"
```
