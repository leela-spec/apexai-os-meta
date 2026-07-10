---
title: "Agent-Specific Knowledge Base"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "agent-specific-knowledge-base"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 67-70; agent KB design questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C011; progressive disclosure and references"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C006 through B04-C017; source authority and state contracts"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "progressive-disclosure-for-agent-kbs"
  - "compact-activation-seed"
  - "skill-boundary"
related_entities:
  - "claude-code"
review_flags: []
---

# Agent-Specific Knowledge Base

## Definition

A durable agent's own knowledge base is a per-role doctrine root: a stable, source-grounded
set of files a persistent agent (as opposed to an ephemeral subagent, a one-off skill call,
or a workflow step) can reload across sessions so it does not have to re-derive its rules,
templates, and evidence boundaries from raw sources every time. This page synthesizes the
concept; the exact phrase "agent-specific knowledge base" is not used verbatim in the Phase 1
batches read for this KB. It is inferred by combining Phase 1 skill-package findings about
progressive disclosure and concise entrypoints (B01-C002, B01-C010) with the Phase 2
specialized-index compile plan's `agent_orchestration_index` question
`why_durable_agents_need_own_kb_or_doctrine_root` and its neighboring questions about
activation-seed-vs-deeper-KB split and inter-agent redundancy
(phase2-specialized-index-compile-plan-20260702.md lines 65-68). Treat this page as a
working hypothesis, not an established fact, until an operator or later batch confirms the
pattern directly.

## Operating Rules

```yaml
rules:
  - "A durable agent KB should hold role-specific rules, templates, and evidence-handling conventions, not raw source dumps."
  - "The agent KB should be loaded via progressive disclosure (index -> compiled page -> raw source), mirroring skill-package practice (B01-C002)."
  - "Writes back into a durable agent KB should not be autonomous; candidate learning notes require review before promotion, mirroring the operator-gate discipline in B04-C005 and B04-C017."
  - "Agent KB content must stay traceable to source_refs so agent-specific doctrine cannot silently drift from its evidence base (B04-C015, B04-T004)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Primary source of the framing question (why durable agents need their own KB or doctrine root) that this concept page answers."
    coverage: "agent_orchestration_index core questions, lines 55-68."
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Supplies the progressive-disclosure and concise-entrypoint mechanics that a durable agent KB would reuse."
    coverage: "Claims B01-C001 through B01-C011 on skill package shape, progressive disclosure, and validation."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Supplies the operator-gate and source-authority discipline that constrains how an agent KB may be updated."
    coverage: "Claims B04-C005 through B04-C017 on operator gates, artifact contracts, and non-promotable external claims."
```

## Macro / Meso / Micro

### Macro

Across the corpus, durable roles are consistently kept thin at activation time and are given
pointers into deeper, versioned material rather than being handed the full raw corpus. The
same shape that works for skill packages (compact `SKILL.md` plus referenced resources) is the
most plausible shape for a persistent agent's own knowledge base: a small doctrine root the
agent reloads every session, with deeper reference material loaded only on demand.

### Meso

The mechanism is progressive disclosure applied at the agent level instead of the skill level:
an agent-specific KB would hold (1) a compact activation seed identifying the agent's role,
boundary, and non-purpose, (2) compiled doctrine pages analogous to this KB's own
summary/concept/entity pages, and (3) source_refs back to raw evidence. Updates to that KB
should follow the same operator-gated, source-authority-preflight discipline documented for
Apex prompt/workflow lanes (B04-C005, B04-C015, B04-C017), so an agent cannot silently
self-promote unverified conclusions into its own doctrine.

### Micro

- B01-C002 / B01-C010: progressive disclosure and "keep the entrypoint concise, push heavy
  material into references" are the reusable shape.
- B04-C006: a lane owns its reusable structures but not orchestration or promotion authority —
  the same separation should apply to an agent and its own KB.
- B04-C015 / B04-T004: external/runtime claims are not promotable without verification, which
  is the strongest available guardrail against an agent KB drifting into unverified doctrine.
- phase2-specialized-index-compile-plan-20260702.md lines 65-68: the open questions
  (`why_durable_agents_need_own_kb_or_doctrine_root`, `what_belongs_in_activation_seed_vs_deeper_kb`,
  `how_much_redundancy_between_agent_kbs_is_useful`, `when_redundancy_becomes_conflicting_doctrine`)
  are unresolved and define the boundary of this concept.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Progressive disclosure (catalog metadata, activated instructions, on-demand resources) is the reusable loading shape that a durable agent KB would need to stay lightweight at startup."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "The strongest reusable design rule is keeping the entrypoint concise/triggerable and pushing heavy contracts, schemas, and examples into referenced files — the same shape an agent-specific KB would need at the doctrine-root level."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C010"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Operator gates are first-class: downstream use of a proposed artifact or doctrine change should pause for explicit approval, which implies an agent KB should not self-update without review."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Whether durable agents need their own KB or doctrine root, and how much redundancy between agent KBs is useful versus conflicting, remains an open question in the specialized-index compile plan and is not yet answered by Phase 1 evidence."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 65-68 (agent_orchestration_index core questions)"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "Why would a persistent Apex agent need its own knowledge base instead of reading the shared KB every time?"
    leads_to: "claude-code-orchestration-design/concepts/progressive-disclosure-for-agent-kbs.md"
    rationale: "That page details the load-order mechanism this concept assumes."
  - question: "What exactly goes in an agent's fast-start file versus its deeper doctrine?"
    leads_to: "claude-code-orchestration-design/concepts/compact-activation-seed.md"
    rationale: "Direct split between activation seed and deeper KB content."
  - related_page: "claude-code-orchestration-design/concepts/skill-boundary.md"
    relation: "Contrasts a durable per-agent KB against a lighter-weight, single-procedure skill package."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C002"
    supports: "Progressive disclosure as the loading shape for durable role knowledge."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C010"
    supports: "Concise entrypoint / deep-reference split reused at the agent-KB level."
  - source_id: "phase1-batch04-apex-application-patterns"
    source_pointer: "claims B04-C005, B04-C015, B04-C017"
    supports: "Operator-gate and source-authority discipline constraining agent-KB updates."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 55-68, agent_orchestration_index"
    supports: "Framing question this page synthesizes an answer around."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Whether durable agents need their own KB or doctrine root is an explicit open question in the specialized-index compile plan, not a settled Phase 1 fact; this page's central claim is an inferential leap from adjacent skill-package and prompt/workflow evidence."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 55-68"
    proposed_handling: "revisit_source"
  - id: U002
    description: "How much redundancy between agent KBs is useful versus when it becomes conflicting doctrine is unresolved."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 65-68"
    proposed_handling: "planning_task_candidate"
  - id: U003
    description: "External/runtime/platform claims default to future-research status and must not be silently promoted into agent-KB doctrine without independent verification."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C015 and contradiction B04-T004"
    proposed_handling: "ask_operator"
```
