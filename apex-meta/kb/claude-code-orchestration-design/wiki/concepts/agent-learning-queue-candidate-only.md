---
title: "Agent Learning Queue Candidate Only"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "agent-learning-queue-candidate-only"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 47-48 and 67-70; agent-specific KBs, verifier loops, drift control"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C015, B04-C017; out-of-mode capture and promotion caution"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "needs_review"
related_concepts:
  - "candidate-is-not-accepted-truth"
  - "gated-write-side-mutation"
related_entities: []
review_flags:
  - "operator_review_needed_before_treating_as_settled_doctrine"
---

# Agent Learning Queue Candidate Only

## Definition

An agent learning queue is the staging list where a durable agent records newly observed lessons, template candidates, or process improvements discovered during execution. The queue entry is explicitly a candidate: it is never written directly into the agent's accepted operating doctrine or agent-specific KB. It only becomes doctrine after the same candidate-to-accepted gate discipline used elsewhere in Apex handoffs is applied. This concept is synthesized from the `agent_orchestration_index` questions about agent-KB redundancy and drift (`why_durable_agents_need_own_kb_or_doctrine_root`, `how_much_redundancy_between_agent_kbs_is_useful`, `when_redundancy_becomes_conflicting_doctrine`) combined with Phase 1 batch 04's operator-gate and promotion-caution claims. It is not a literal, named pattern quoted verbatim in Phase 1 batch claims.

## Operating Rules

```yaml
rules:
  - "A new lesson or improvement observed during execution is logged as a candidate item with a source/evidence pointer, not applied silently to doctrine."
  - "Candidate items never overwrite an agent's existing accepted KB or doctrine root directly."
  - "Promotion from candidate to accepted status requires the same validation/operator-gate discipline used for other candidate outputs (see candidate-is-not-accepted-truth)."
  - "Queue entries carry enough pointer context to be re-derived or audited later without replaying the original session's full chat history."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Provides the direct claims this pattern generalizes from: explicit capture of out-of-mode improvements (B04-C009) and promotion caution for unverified claims (B04-C015, B04-C017)."
    coverage: "Out-of-mode improvement capture, operator gates, promotion caution."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the agent_orchestration_index questions this page answers about agent-KB redundancy and drift, which have no direct B04 claim equivalent."
    coverage: "Agent-specific KB ownership, redundancy, and conflicting-doctrine framing questions."
```

## Macro / Meso / Micro

### Macro

Persistent agents accumulate observations across many runs. Without an explicit staging boundary between "things this run noticed" and "things this agent now believes," a single bad inference could silently propagate into an agent's accepted doctrine, and multiple agent-specific KBs could drift into contradiction with one another over time.

### Meso

This pattern is the agent-memory-specific instance of the general candidate/accepted-truth gate (see `candidate-is-not-accepted-truth`). It exists because agent-specific KBs are exactly the place where compounding drift is most likely, which is why the compile plan raises redundancy and conflicting-doctrine as explicit `agent_orchestration_index` questions rather than assuming agent KBs simply accumulate correctly on their own.

### Micro

B04-C009 requires that out-of-mode improvements be captured explicitly instead of applied silently. B04-C015 requires that external/unverified claims default to future-research status rather than accepted doctrine. B04-C017 requires that Apex preserve lifecycle safety through explicit artifacts and gates rather than relying on conversational continuity or self-promotion of learned behavior. Read together, these three claims support — but do not literally name — an "agent learning queue" as the concrete artifact where this discipline is applied to agent self-improvement specifically.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Out-of-mode improvements should be captured explicitly instead of applied silently."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C009"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C002
    claim: "External, runtime, or unverified claims default to future-research/adjacent-lane status and should not become accepted doctrine without independent verification."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C015"
    confidence: high
    claim_label: source_backed_summary
  - claim_id: C003
    claim: "Generalizing B04-C009/B04-C015/B04-C017 to agent self-improvement: an agent's proposed lessons should be held in an explicit, separately-gated candidate queue rather than folded directly into the agent's operating doctrine or KB."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md agent_orchestration_index core_questions (lines 63-68)"
    confidence: medium
    claim_label: working_hypothesis
```

## Routes Here

```yaml
routes:
  - question: "How does Apex prevent a single agent run's mistaken inference from becoming permanent doctrine?"
    leads_to: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/agent-learning-queue-candidate-only.md"
    rationale: "This page defines the staging boundary between observed lessons and accepted agent doctrine."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/candidate-is-not-accepted-truth.md"
    relation: "Shares the same candidate-to-accepted gate mechanism, applied here specifically to agent self-improvement."
  - related_page: "apex-meta/kb/claude-code-orchestration-design/wiki/concepts/gated-write-side-mutation.md"
    relation: "Promoting a candidate lesson to accepted doctrine is itself a gated write-side mutation of the agent's KB."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C009"
    supports: "Explicit capture of improvements instead of silent application."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C015"
    supports: "Promotion caution for unverified/external claims."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claim B04-C017"
    supports: "Preserving lifecycle safety via explicit artifacts and gates rather than conversational continuity."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "agent_orchestration_index core_questions, lines 63-68"
    supports: "Framing of agent-KB ownership, redundancy, and conflicting-doctrine risk that this page's synthesis answers."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "\"Agent learning queue\" is a synthesized concept built from the specialized-index question framework (agent_orchestration_index) and general B04 promotion-caution claims; it is not a named or defined pattern in any Phase 1 batch claim. This synthesis should be reviewed by the operator before being treated as settled doctrine."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 63-68; phase1-batch04-apex-application-patterns.md claims B04-C009, B04-C015, B04-C017"
    proposed_handling: "ask_operator"
  - id: U002
    description: "Exact learning-queue file layout, storage location, and promotion workflow are undefined and deferred beyond this compile."
    source_pointer: "phase1-batch04-apex-application-patterns.md B04-Q002, B04-Q003"
    proposed_handling: "planning_task_candidate"
```
