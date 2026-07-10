---
title: "Claude Code"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code"
entity_type: "runtime_surface"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "source scope and entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "skill-boundary"
  - "compact-activation-file"
review_flags: []
---

# Claude Code

## Identity

```yaml
entity:
  label: "Claude Code"
  type: "runtime_surface"
  aliases: []
```

## Source-Grounded Summary

Claude Code is the runtime surface that discovers and invokes skills, commands, agents, hooks,
and MCP integrations, per its entities_extracted entry in the skill-package-contracts batch
(phase1-batch01-skill-package-contracts.md entities_extracted: `claude-code`). This KB's
dedicated Batch 02 source pass (phase1-batch02-claude-code-orchestration-surface.md) covers its
orchestration surface in more depth than was reread for this compile pass; this page carries
forward that batch's existing source_ref pointer ("source scope and entities extracted") as its
frontmatter grounding and adds the directly-read Batch 01 entity definition as corroborating
evidence. Batch 01 also documents a concrete point of Claude Code-specific behavior: its skill
docs treat `description` as the key recommended frontmatter field and derive command/invocation
naming from file location, in tension with the stricter Agent Skills specification's `name`
requirement (B01-C012, B01-T001).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "This entity's original and primary source grouping; defines Claude Code's orchestration surface (skills, commands, agents, hooks, MCP) as its own batch focus."
    coverage: "Source scope and entities_extracted for the Claude Code orchestration surface (not reread in full for this compile pass; existing source_ref preserved)."
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Directly read for this compile pass; supplies a corroborating entity definition and a concrete documented tension in Claude Code's skill-frontmatter behavior."
    coverage: "entities_extracted entry 'claude-code'; claim B01-C012; contradiction B01-T001."
```

## Macro / Meso / Micro

### Macro

Claude Code is treated in this KB as one runtime surface among several possible orchestration
substrates, not as the final named implementation target. It is the concrete host for skills,
commands, subagents, hooks, and MCP integrations that the rest of this KB's concepts (skill
boundary, compact activation file, progressive disclosure) assume as their runtime context.

### Meso

Its role, per Batch 01's entity extraction, is to discover and invoke skills, commands, agents,
hooks, and MCP integrations (phase1-batch01-skill-package-contracts.md entities_extracted:
`claude-code`). Its documented skill-loading behavior is more permissive than the strict Agent
Skills specification: Claude Code's docs recommend `description` as the key field and derive
invocation naming from file location rather than strictly enforcing a `name` field matching the
parent directory (B01-C012). This is an explicit, unresolved tension Phase 1 flags rather than
resolves (B01-T001).

### Micro

- phase1-batch01-skill-package-contracts.md entities_extracted: Claude Code entity role —
  "Runtime that discovers and invokes skills, commands, agents, hooks, and MCP integrations."
- B01-C012 / B01-T001: Claude Code's skill docs treat `description` as the key recommended
  field and derive command names from location, versus the Agent Skills spec's strict `name`
  requirement.
- phase1-batch02-claude-code-orchestration-surface.md: original dedicated source pass for this
  entity's fuller orchestration-surface behavior (source scope and entities extracted per this
  page's preserved source_ref; not reread line-by-line in this compile pass).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code is the runtime that discovers and invokes skills, commands, agents, hooks, and MCP integrations."
    source_pointer: "phase1-batch01-skill-package-contracts.md entities_extracted entry 'claude-code'"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Claude Code's documented skill behavior treats description as the key recommended frontmatter field and derives the command/invocation name from file location, unlike the Agent Skills specification's strict name requirement."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C012 and contradiction B01-T001"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Claude Code's orchestration surface (skills, commands, agents, hooks, MCP) is documented as its own dedicated Phase 1 batch topic."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md source scope and entities extracted"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What runtime hosts skill packages, and how does its behavior compare to the portable Agent Skills standard?"
    leads_to: "claude-code-orchestration-design/entities/agent-skills-standard.md"
    rationale: "Agent-skills-standard is the portable spec Claude Code's runtime behavior is compared against."
  - related_page: "claude-code-orchestration-design/concepts/skill-boundary.md"
    relation: "Skill-boundary defines when the skill mechanism Claude Code hosts is the right choice versus other runtime mechanisms."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "entities_extracted entry 'claude-code'"
    supports: "Definition of Claude Code's role as a runtime surface."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C012, contradiction B01-T001"
    supports: "Documented Claude Code-specific skill-frontmatter behavior and its tension with the Agent Skills spec."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "source scope and entities extracted (existing source_ref)"
    supports: "Original dedicated batch scope for Claude Code's orchestration surface."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "This compile pass did not reread phase1-batch02-claude-code-orchestration-surface.md in full; its existing source_ref pointer is preserved as-is, but detailed claim IDs from that batch were not reverified for this page."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md (existing source_ref, not reread this pass)"
    proposed_handling: "revisit_source"
  - id: U002
    description: "Whether Apex canonical skills should target strict Agent Skills validation or Claude Code-native permissive frontmatter (or a two-tier policy) remains an open question directly involving Claude Code's documented behavior."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q001, contradiction B01-T001"
    proposed_handling: "ask_operator"
  - id: U003
    description: "Platform/runtime behavior claims about Claude Code should be treated as volatile and reverified rather than assumed permanently accurate."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C015 and contradiction B04-T004"
    proposed_handling: "revisit_source"
```
