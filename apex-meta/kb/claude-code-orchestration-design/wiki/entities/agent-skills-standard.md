---
title: "Agent Skills Standard"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "agent-skills-standard"
entity_type: "standard"
source_refs:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C013; entities extracted"
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

# Agent Skills Standard

## Identity

```yaml
entity:
  label: "Agent Skills Standard"
  type: "standard"
  aliases:
    - "Agent Skills specification"
    - "agentskills-agentskills specification"
```

## Source-Grounded Summary

The Agent Skills specification defines the portable, cross-client folder structure, `SKILL.md`
entrypoint, YAML frontmatter fields, and resource conventions that a skill package must satisfy
to be recognized consistently across clients (B01-C001, B01-C003). It requires `name` and
`description` frontmatter fields, with `name` constrained to lowercase/hyphenated form matching
the parent directory, and `description` expected to state what the skill does and when to use
it (B01-C003). It defines the three-tier progressive disclosure model of catalog metadata,
activated instructions, and on-demand resources (B01-C002), and specifies how clients should
discover, parse, disclose, and validate skills, including handling of name collisions and trust
boundaries for project-level skills (B01-C004, B01-C005). Phase 1 evidence also identifies a
documented tension between this specification's strict `name` requirements and Claude Code's
more permissive, path-derived skill invocation behavior (B01-T001), which is an open question
for how strictly Apex should enforce the standard.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Sole and directly-read Phase 1 source defining this entity; covers its full claim set, concepts, and known tensions with Claude Code's runtime behavior."
    coverage: "Claims B01-C001 through B01-C013; entities_extracted entry 'agent-skills-specification'; contradictions B01-T001, B01-T002; open question B01-Q001."
```

## Macro / Meso / Micro

### Macro

The Agent Skills standard is the portable contract layer beneath any specific client's skill
implementation (including Claude Code): it defines what a skill package is, structurally and in
frontmatter, independent of any one runtime's behavior.

### Meso

Structurally, the standard requires a `SKILL.md` entrypoint with optional scripts/references/
assets (B01-C001), mandates `name`/`description` frontmatter with strict `name` constraints
(B01-C003), and defines the progressive disclosure loading tiers that client implementations
should honor (B01-C002, B01-C004). It also expects clients to enforce deterministic collision
handling and trust boundaries for less-trusted (e.g., project-level) skills before their content
or resources are used (B01-C005).

### Micro

- B01-C001: required `SKILL.md` entrypoint; optional scripts, references, assets.
- B01-C002: three-tier progressive disclosure (catalog, activated instructions, on-demand
  resources).
- B01-C003: `name`/`description` frontmatter with strict `name` constraints and
  what/when-oriented `description`.
- B01-C004: expected client discovery/parsing/disclosure/activation sequence.
- B01-C005: deterministic collision handling and trust checks for project-level skills.
- B01-T001: tension between this spec's strict `name` rule and Claude Code's path-derived,
  more permissive behavior.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "The Agent Skills specification requires YAML frontmatter with name and description; name has strict lowercase/hyphen constraints and must match the parent directory, while description should state what the skill does and when to use it."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C003"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Agent Skills rely on progressive disclosure: startup metadata/catalog, activated SKILL.md instructions, and on-demand bundled resources."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "There is a specification tension between strict Agent Skills name requirements and Claude Code's documented behavior of deriving command names from location while treating description as the key recommended field."
    source_pointer: "phase1-batch01-skill-package-contracts.md contradiction B01-T001"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What is the portable rule set a skill package needs to satisfy across clients?"
    leads_to: "claude-code-orchestration-design/concepts/skill-boundary.md"
    rationale: "Skill-boundary uses this standard's rules to define when a skill is the right mechanism."
  - related_page: "claude-code-orchestration-design/entities/claude-code.md"
    relation: "Claude Code is a specific runtime implementation whose behavior is compared against this portable standard."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C001"
    supports: "SKILL.md entrypoint and optional-resource structure."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C002"
    supports: "Progressive disclosure loading tiers."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C003"
    supports: "Frontmatter name/description requirements."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C005"
    supports: "Collision handling and trust boundary expectations."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Whether Apex canonical skills should enforce this specification strictly, or allow Claude Code-specific optional frontmatter and path-derived command names, is an open question."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q001"
    proposed_handling: "ask_operator"
  - id: U002
    description: "The spec treats allowed-tools as optional/experimental while Apex guidance and Claude Code treat it more centrally; Apex should avoid treating allowed-tools as a universal cross-client contract."
    source_pointer: "phase1-batch01-skill-package-contracts.md contradiction B01-T002"
    proposed_handling: "revisit_source"
```
