---
title: "Compact Activation File"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compact-activation-file"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; what should be loaded every session"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002 and B01-C010; concise entrypoints"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "compact-activation-seed"
  - "progressive-disclosure-for-agent-kbs"
  - "skill-boundary"
related_entities:
  - "agent-skills-standard"
  - "claude-code"
review_flags: []
---

# Compact Activation File

## Definition

A compact activation file is the entrypoint document a model or role reads first: it carries
only stable triggers, a scope boundary, a short procedure summary, and pointers to deeper
material, rather than the full contract, schema, or example set. This is the same pattern the
Agent Skills specification and Anthropic's `skill-creator` describe for `SKILL.md` — a
concise, triggerable file that defers heavy detail to referenced resources
(phase1-batch01-skill-package-contracts.md claims B01-C001, B01-C002, B01-C010).

## Operating Rules

```yaml
rules:
  - "Keep only trigger metadata, scope boundary, and next-read pointers in the activation file (B01-C010)."
  - "Load full instructions only when the model or client activates the file, not eagerly at catalog time (B01-C002, B01-C004)."
  - "Protect activated content against context compaction, or deduplicate it, so activation-file guidance is not silently lost mid-session (B01-C007)."
  - "Push schemas, examples, and detailed contracts into referenced files rather than the activation file itself (B01-C010, B04-T001)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Primary and most directly grounded source: defines the SKILL.md entrypoint contract, progressive disclosure tiers, and the concise-entrypoint design rule this concept generalizes."
    coverage: "Claims B01-C001, B01-C002, B01-C004, B01-C007, B01-C010."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the same idea as a KB-wide design question about what must load every session versus only on trigger."
    coverage: "token_economy_and_information_design_index core questions, lines 124-137."
```

## Macro / Meso / Micro

### Macro

Every startup surface examined in Phase 1 — skill frontmatter, catalog disclosure, and the
Apex skill-file zoning guidance — converges on the same shape: keep the thing read at startup
small, and make everything else reachable but not mandatory.

### Meso

Mechanically this is progressive disclosure applied to a single file: metadata/catalog first,
full body only on activation, and bundled resources only when explicitly needed
(B01-C002, B01-C004, B01-C006). A dedicated activation tool can wrap the body, enumerate
resources without eagerly reading them, and enforce permissions (B01-C006). Because context
compaction can silently degrade behavior, activation-file content needs lifecycle handling —
protection or deduplication — after it is first loaded (B01-C007).

### Micro

- B01-C001: `SKILL.md` is the required entrypoint; scripts, references, and assets are optional
  and separate.
- B01-C002: startup metadata/catalog, activated instructions, and on-demand resources form the
  three loading tiers.
- B01-C010: the strongest reusable rule — keep the entrypoint concise and triggerable; move
  heavy contracts, schemas, examples, and templates into referenced files.
- B04-T001: Apex needs rich execution contracts, but sources converge on keeping the activation
  file itself compact and pushing schemas/evidence into references or appendices.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A skill's required entrypoint (SKILL.md) is a folder-based instruction package; optional scripts, references, and assets stay outside the entrypoint file."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C001"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Agent Skills rely on progressive disclosure: startup metadata/catalog, activated SKILL.md instructions, and on-demand bundled resources."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The strongest reusable design rule for an activation file is to keep it concise and triggerable, moving heavy contracts and schemas into referenced files."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C010"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "Context compaction can silently degrade behavior unless activated content is protected or deduplicated after loading."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C007"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What exactly should load at startup versus only when triggered?"
    leads_to: "claude-code-orchestration-design/summaries/token-efficient-information-design.md"
    rationale: "The summary page generalizes this file-level pattern into a KB-wide token-economy rule."
  - question: "How does this differ from an agent's own activation seed?"
    leads_to: "claude-code-orchestration-design/concepts/compact-activation-seed.md"
    rationale: "Compact-activation-seed applies the same shape at the persistent-agent/role level rather than the single-skill level."
  - related_page: "claude-code-orchestration-design/concepts/skill-boundary.md"
    relation: "Skill boundary defines when a compact activation file (SKILL.md) is the right mechanism at all."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C001"
    supports: "Entrypoint/optional-resource split definition."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C002"
    supports: "Three-tier progressive disclosure loading model."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C010"
    supports: "Concise-entrypoint, deep-reference design rule."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C007"
    supports: "Compaction protection requirement for activated content."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "There is a documented tension between rich Apex execution contracts and SKILL.md concision — both push toward references/appendices, but exact split thresholds are not fully specified."
    source_pointer: "phase1-batch04-apex-application-patterns.md contradiction B04-T001"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Whether Apex canonical activation files should follow strict Agent Skills spec fields or Claude Code-native permissive frontmatter remains open."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q001 and contradiction B01-T001"
    proposed_handling: "ask_operator"
```
