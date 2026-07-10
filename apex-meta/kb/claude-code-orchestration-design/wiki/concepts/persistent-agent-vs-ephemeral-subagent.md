---
title: "Persistent Agent vs Ephemeral Subagent"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "persistent-agent-vs-ephemeral-subagent"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 57-70; agent_orchestration_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C008 through B02-C009; subagent context isolation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 76-87; persistent vs ephemeral subagent decision"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "ephemeral-subagent-boundary"
  - "mechanism-ladder"
related_entities:
  - "claude-code-subagents"
review_flags:
  - "Mapping this concept slug onto B02-C008/C009 plus operator Q004 is a reasonable but explicit synthesis; the batch file does not use the phrase 'persistent agent vs ephemeral subagent' verbatim."
---

# Persistent Agent vs Ephemeral Subagent

## Definition

Persistent agent vs ephemeral subagent is the decision boundary between two ways of using Claude Code's subagent mechanism: a small set of persistent, project-defined subagent roles that recur across many tasks and carry stable validation/audit expectations, versus an unbounded set of ephemeral, ad hoc subagent invocations used once for exploration, scouting, or comparison and then discarded. Both share the same underlying mechanism — an isolated context window that returns a summary to the main conversation — but differ in whether a named, checked-in definition persists after the task completes.

## Operating Rules

```yaml
rules:
  - "Keep persistent subagent definitions small and validated; do not create a persistent subagent for every delegation."
  - "Make a subagent persistent when it fills a repeated domain role, a stable validation or audit role, or a security-sensitive repo-executor role with explicit constraints."
  - "Keep a subagent ephemeral when it performs one-off source scouting, temporary comparison reading, or broad exploration."
  - "Route ephemeral subagent findings back through review before treating them as doctrine; do not skip validation just because a role was one-off."
  - "Do not finalize a full persistent subagent roster as part of Phase 2 KB compile (S6); the roster is deferred future work per operator decision."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator decision Q004 is the direct compile-policy source, explicitly listing persistent_when and ephemeral_when conditions that define this boundary."
    coverage: "Q004_subagent_persistence: decision to keep persistent subagents small and validated, with explicit persistent_when/ephemeral_when lists."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "B02-C008 and B02-C009 ground the underlying subagent context-isolation mechanism that both persistent and ephemeral usage share."
    coverage: "Subagent isolation, benefits, built-in Explore/Plan subagent behavior, general-purpose subagent scope."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "The agent_orchestration_index questions in this planning log frame the persistent/ephemeral distinction as an indexed routing question for Apex's own agent design."
    coverage: "Agent orchestration index questions (lines 57-70)."
```

## Macro / Meso / Micro

### Macro

Not every delegated task should create a permanent role, and not every permanent role should be re-derived from scratch each time. Apex's compile policy draws a clear line between agent roles that deserve to be persistent, versioned, and validated project artifacts, and delegations that are better left as lightweight, disposable subagent calls. This keeps the eventual agent roster small and deliberate rather than accreting one agent definition per task type.

### Meso

The mechanism underneath both cases is the same: subagents isolate exploratory or specialized work in a separate context window and return summaries to preserve main-thread context (B02-C008), with built-in Explore/Plan subagents being read-only/research-oriented and general-purpose subagents supporting broader, multi-step operations (B02-C009). What differs is persistence and validation overhead. Operator decision Q004 sorts roles into persistent_when (repeated domain role; stable validation or audit role; security-sensitive repo executor with explicit constraints) and ephemeral_when (one-off source scouting; temporary comparison reading; broad exploration). This yields a working rule: default new delegations to ephemeral, and only promote a role to a persistent, validated definition once it has demonstrably repeated and stabilized.

### Micro

B02-C008: "Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization" (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C008). B02-C009: "Built-in Explore and Plan subagents are read-only/research-oriented... while general-purpose subagents can perform complex multi-step operations with broader tools" (claim B02-C009). Operator decision Q004 (`operator-phase1-review-decisions-20260702.md` lines 74-84): `decision: keep_persistent_subagents_small_and_validated`; `persistent_when: [repeated domain role, stable validation or audit role, security-sensitive repo executor with explicit constraints]`; `ephemeral_when: [one-off source scouting, temporary comparison reading, broad exploration]`.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Subagents isolate exploratory or specialized work in separate context windows and return summaries to the main conversation, preserving main-thread context and enabling tool/model specialization."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C008"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "A subagent role should be persistent when it fills a repeated domain role, a stable validation/audit role, or a security-sensitive repo-executor role with explicit constraints; it should stay ephemeral for one-off scouting, temporary comparison reading, or broad exploration."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q004_subagent_persistence"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Built-in Explore and Plan subagents are read-only/research-oriented and keep results out of the main context, while general-purpose subagents can perform complex multi-step operations with broader tools — a distinction relevant to how persistent roles should be scoped."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C009"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should this recurring task become a checked-in persistent subagent, or stay a one-off delegation?"
    leads_to: "claude-code-orchestration-design/concepts/persistent-agent-vs-ephemeral-subagent.md"
    rationale: "This page is the direct decision point for promoting a subagent role to persistent status."
  - related_page: "claude-code-orchestration-design/concepts/ephemeral-subagent-boundary.md"
    relation: "Companion concept page specializing the ephemeral side of this same boundary."
  - related_page: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    relation: "Persistent-vs-ephemeral subagent choice is one rung on the broader mechanism-selection ladder."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C008, B02-C009"
    supports: "Underlying subagent context-isolation mechanism shared by persistent and ephemeral usage."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q004_subagent_persistence"
    supports: "Explicit persistent_when / ephemeral_when decision criteria."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: which Apex subagent definitions should be persistent project files, and which should remain ephemeral CLI/session definitions? No concrete roster exists."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q003"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "This concept-slug mapping (persistent-agent-vs-ephemeral-subagent) is a synthesis of B02-C008/C009 and operator Q004; the batch file does not use this exact phrase, so treat the framing (not the underlying claims) as an inferential leap rather than a literal source quote."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-C008, B02-C009; operator-phase1-review-decisions-20260702.md Q004_subagent_persistence"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Full subagent roster is explicitly named as a boundary/open-question item, not settled Phase 2 doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.write_as_boundary_or_open_question"
    proposed_handling: "revisit_source"
```
