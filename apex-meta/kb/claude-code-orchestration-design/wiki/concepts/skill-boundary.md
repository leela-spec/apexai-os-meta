---
title: "Skill Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "skill-boundary"
source_refs:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C011; skill package contract"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C004; skills and runtime controls"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "compact-activation-file"
  - "compact-activation-seed"
related_entities:
  - "agent-skills-standard"
  - "claude-code"
review_flags: []
---

# Skill Boundary

## Definition

A skill boundary is the design test for when a repeatable procedure should be packaged as a
skill (a folder-based instruction package with a `SKILL.md` entrypoint) versus when it needs a
heavier mechanism (multi-stage workflow, isolated subagent context, or hard runtime
enforcement) or a lighter one (a plain artifact or reference file). The boundary is defined by
what a skill package contract actually is and is not: a triggerable, concise entrypoint plus
optional scripts/references/assets (B01-C001), not an orchestration engine, and not a substitute
for context isolation or enforcement mechanisms that Claude Code provides separately.

## Operating Rules

```yaml
rules:
  - "Use a skill when a procedure recurs and can be triggered by a clear name/description pair (B01-C003, B01-C010)."
  - "Do not use a skill alone when the task needs multi-stage orchestration, isolated context, or hard enforcement — those are separate Claude Code mechanisms."
  - "Skill frontmatter name/description function as routing keys; description should state what the skill does and when to use it (B01-C003)."
  - "Project-level or repo-provided skills should be treated as potentially untrusted until a trust check or equivalent approval occurs (B01-C005)."
  - "Validate critical skills with both deterministic checks (shape/name/frontmatter/path) and inference-based review (workflow clarity, scope boundaries, trigger quality) (B01-C011)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Primary, fully-read source defining the skill package contract, frontmatter constraints, trust boundary, and validation loop that set this concept's boundary conditions."
    coverage: "Claims B01-C001 through B01-C013; concepts skill-package-contract, skill-trigger-description, skill-trust-boundary, skill-validation-loop."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Documents where skills sit relative to other Claude Code runtime controls (commands, hooks, subagents); referenced for contrast but not read in full for this compile pass."
    coverage: "Claims B02-C001 through B02-C004 on skills and runtime controls, per this page's existing source_refs pointer."
```

## Macro / Meso / Micro

### Macro

A skill is the right mechanism exactly when a workflow step is repeatable, nameable, and
boundable by a concise entrypoint. Once a task needs orchestration across multiple stages,
isolated execution context, or non-negotiable enforcement, the skill boundary has been crossed
and a different Claude Code mechanism (workflow, subagent, script, hook) is the better fit.

### Meso

The skill package contract itself enforces this boundary structurally: `SKILL.md` is required,
optional resources are separate, frontmatter name/description drive triggering, and the
description functions as a routing key naming what the skill does and when to use it
(B01-C001, B01-C003). Trust and validation are boundary-enforcement mechanisms too — untrusted
project-level skills are gated before their instructions or resources load (B01-C005), and
critical skills get both deterministic and inference-based review before being relied upon
(B01-C011).

### Micro

- B01-C001: skill = folder-based instruction package, `SKILL.md` entrypoint required, other
  resources optional.
- B01-C003: frontmatter requires `name`/`description`; description should state what and when.
- B01-C005: collisions handled deterministically; project-level skills gated by trust checks.
- B01-C010: keep `SKILL.md` concise and triggerable; move heavy contracts to references —
  the practical upper bound of what belongs inside the skill boundary.
- B01-C011: deterministic + inference-based validation for critical skills.
- B01-T001/B01-T002 (contradictions): tension between strict Agent Skills spec fields and
  Claude Code's more permissive, path-derived frontmatter behavior affects exactly where this
  boundary sits for Apex.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A skill is a folder-based instruction package whose required entrypoint is SKILL.md; optional resources include scripts, references, and assets."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C001"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Skill frontmatter description functions as a routing key and should state what the skill does and when to use it."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C003"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Client implementations should handle skill-name collisions deterministically and treat project-level skills as potentially untrusted until a trust check or equivalent approval occurs."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C005"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Apex should validate critical skills with both deterministic checks and inference-based review covering workflow clarity, scope boundaries, and trigger quality."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C011"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When is a compact SKILL.md file the right mechanism, and what belongs inside it?"
    leads_to: "claude-code-orchestration-design/concepts/compact-activation-file.md"
    rationale: "Compact-activation-file details the internal shape once the skill boundary decision is made."
  - question: "What entity defines the portable rules a skill package must satisfy?"
    leads_to: "claude-code-orchestration-design/entities/agent-skills-standard.md"
    rationale: "Agent-skills-standard is the specification entity this concept's operating rules are drawn from."
  - related_page: "claude-code-orchestration-design/entities/claude-code.md"
    relation: "Claude Code is the runtime surface that hosts skills alongside the other mechanisms this boundary distinguishes them from."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C001"
    supports: "Skill package definition."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C003"
    supports: "Frontmatter as routing/trigger mechanism."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C005"
    supports: "Trust boundary for project-level skills."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C011"
    supports: "Validation discipline for critical skills."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Canonical Apex validation policy is strict in this KB's working assumption, but runtime compatibility details may remain tool-specific and are not fully settled."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q001, contradiction B01-T001"
    proposed_handling: "ask_operator"
  - id: U002
    description: "Whether allowed-tools should be treated as a universal cross-client contract or a Claude Code-specific runtime affordance is unresolved."
    source_pointer: "phase1-batch01-skill-package-contracts.md contradiction B01-T002"
    proposed_handling: "revisit_source"
  - id: U003
    description: "Which Apex skill types require deterministic test harnesses versus qualitative operator review only is still an open question."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q002"
    proposed_handling: "planning_task_candidate"
```
