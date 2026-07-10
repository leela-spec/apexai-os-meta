---
title: "Compact Activation Seed"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compact-activation-seed"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 67-70; activation seed vs deeper KB"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002, B01-C004, B01-C010"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "working_hypothesis"
status: "active"
related_concepts:
  - "compact-activation-file"
  - "agent-specific-knowledge-base"
  - "progressive-disclosure-for-agent-kbs"
related_entities:
  - "claude-code"
review_flags: []
---

# Compact Activation Seed

## Definition

A compact activation seed is the minimal, always-loaded set of facts a role, agent, or skill
needs to start safely: name/role, purpose, triggers, boundary/non-purpose, and pointers to
what to read next — without loading the full doctrine, contract, or source set immediately.
The term "activation seed" comes from the Phase 2 specialized-index compile plan's
`agent_orchestration_index` question `what_belongs_in_activation_seed_vs_deeper_kb`
(phase2-specialized-index-compile-plan-20260702.md lines 65-68); it is not a verbatim Phase 1
term. The mechanics it describes, however, map directly onto the skill-package progressive
disclosure and frontmatter findings in Batch 01 (B01-C002, B01-C003, B01-C004, B01-C010), so
this page treats "activation seed" as the agent/role-level generalization of the skill-level
"compact activation file" concept, flagged as a working hypothesis where it extends beyond a
skill file to a persistent agent or role.

## Operating Rules

```yaml
rules:
  - "An activation seed should contain name/role, purpose, triggers, boundary, and next-read pointers only (compile-plan lines 65-68; B01-C003)."
  - "Detailed schemas, contracts, and examples belong in deeper KB pages or referenced files, not the seed itself (B01-C010)."
  - "Discovery/parsing/disclosure of the seed should happen before any full-content activation, mirroring client-side skill discovery (B01-C004)."
  - "Boundary and non-purpose clauses in the seed exist specifically to prevent role or scope expansion."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Source of the explicit 'activation seed vs deeper KB' framing this page is built around."
    coverage: "agent_orchestration_index core questions, lines 55-68."
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Supplies the concrete mechanics (frontmatter constraints, progressive disclosure, concise-entrypoint rule) that a seed at any scale would reuse."
    coverage: "Claims B01-C002, B01-C003, B01-C004, B01-C010."
```

## Macro / Meso / Micro

### Macro

The corpus repeatedly separates a small, fast-loading identity/trigger layer from a larger body
of doctrine that loads only on demand. Applied above the single-skill level, this becomes the
"activation seed" question the compile plan raises directly: what minimal facts must a durable
agent or role always carry, versus what can wait for a deeper KB read.

### Meso

At the skill level this is already documented: frontmatter with `name` and `description` acts
as the trigger layer (B01-C003), client discovery/parsing/catalog-disclosure happens before
full activation (B01-C004), and the reusable design rule is to keep the entrypoint concise
while pushing heavy material to references (B01-C010). Generalizing this to an agent or role
means the same three fields — identity, trigger conditions, and boundary — form the seed, with
deeper KB pages and raw sources one hop away.

### Micro

- B01-C003: frontmatter requires `name` and `description`; `description` should state what the
  skill does and when to use it — the direct analog of an activation seed's trigger layer.
- B01-C004: clients discover directories, parse frontmatter, disclose a compact catalog, and
  activate full instructions only when selected — the seed-then-activate sequence.
- B01-C010: keep the entrypoint concise and triggerable; move heavy material to references.
- phase2-specialized-index-compile-plan-20260702.md lines 65-68: raises
  `what_belongs_in_activation_seed_vs_deeper_kb` as an open agent_orchestration_index question,
  which this page answers only at the level of a working hypothesis.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The Agent Skills specification requires name/description frontmatter functioning as the model-facing trigger layer, which is the seed-equivalent for a skill."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C003"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Clients should discover, parse, and disclose a compact catalog before activating full instructions — a seed-then-detail sequence."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C004"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Keeping an entrypoint concise and triggerable while moving heavy contracts into references is the strongest reusable design rule found in Phase 1 for this shape of file."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C010"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "What belongs in an activation seed versus a deeper agent KB is an open, unresolved design question at the agent-orchestration level, not yet settled by Phase 1 evidence."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 65-68 (agent_orchestration_index)"
    confidence: "medium"
    claim_label: "working_hypothesis"
```

## Routes Here

```yaml
routes:
  - question: "What is the minimal information a durable agent needs to start every session?"
    leads_to: "claude-code-orchestration-design/concepts/agent-specific-knowledge-base.md"
    rationale: "Agent-specific-knowledge-base discusses the deeper doctrine root the seed points into."
  - question: "How is this different from a single skill's SKILL.md entrypoint?"
    leads_to: "claude-code-orchestration-design/concepts/compact-activation-file.md"
    rationale: "Compact-activation-file is the skill-scoped version of this same seed pattern."
  - related_page: "claude-code-orchestration-design/concepts/progressive-disclosure-for-agent-kbs.md"
    relation: "Shares the same load-order mechanism generalized to full agent KBs."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C003"
    supports: "Frontmatter as trigger/identity layer."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C004"
    supports: "Discovery-then-activation sequencing."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C010"
    supports: "Concise-entrypoint design rule."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 65-68"
    supports: "Explicit framing of the activation-seed-vs-deeper-KB question."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact concrete seed file format and its boundary against the deeper agent KB is unresolved implementation work, not yet specified by Phase 1 sources."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 65-68"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "This page generalizes a skill-level pattern (B01) to the agent/role level via the compile plan's terminology; treat the generalization itself as unverified until a later batch or operator confirms it."
    source_pointer: "phase1-batch01-skill-package-contracts.md claims B01-C002 through B01-C010"
    proposed_handling: "revisit_source"
```
