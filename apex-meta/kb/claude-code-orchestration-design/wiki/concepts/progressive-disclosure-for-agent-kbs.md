---
title: "Progressive Disclosure for Agent KBs"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "progressive-disclosure-for-agent-kbs"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; progressive disclosure and compiled KB pages"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002, B01-C004, B01-C010"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "compact-activation-seed"
  - "agent-specific-knowledge-base"
  - "compact-activation-file"
related_entities:
  - "agent-skills-standard"
review_flags: []
---

# Progressive Disclosure for Agent KBs

## Definition

Progressive disclosure for agent KBs is the load-order rule that a durable knowledge base
should be read as index first, then a small number of relevant compiled summary/concept/entity
pages, and only then — if the task genuinely requires it — the raw source material behind those
pages. This directly extends the three-tier progressive disclosure model documented for Agent
Skills (catalog metadata, activated instructions, on-demand resources; B01-C002) up to the
scale of a whole knowledge base, and is named directly in the Phase 2 specialized-index compile
plan's `token_economy_and_information_design_index` (lines 122-134).

## Operating Rules

```yaml
rules:
  - "Read the KB index or a compact activation seed before any compiled page (B01-C002, B01-C004)."
  - "Read compiled summary/concept/entity pages before rereading raw sources for a routine task."
  - "Reopen raw source only when source_refs and claim status justify it, per the KB's own uncertainty triggers."
  - "Keep each compiled page small and pointer-rich rather than duplicating raw source content, mirroring the concise-entrypoint rule (B01-C010)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Origin of the three-tier progressive disclosure model this concept scales up to KB size."
    coverage: "Claims B01-C002, B01-C004, B01-C010 on loading tiers, client discovery/activation, and concise entrypoints."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names the KB-level version of this pattern directly as a token-economy design goal."
    coverage: "token_economy_and_information_design_index core questions, lines 122-134."
```

## Macro / Meso / Micro

### Macro

The same three-tier loading discipline that governs a single skill file scales cleanly to an
entire knowledge base: an index or seed narrows the search, compiled pages answer most
questions, and raw sources are reserved for genuine reopen triggers. This keeps most sessions
cheap while preserving a full audit trail back to evidence.

### Meso

Mechanically, this mirrors client-side skill handling: discovery and cataloging happen first
(B01-C004), full content activates only when selected, and bundled resources are enumerated but
not eagerly read (B01-C002, B01-C006 in the source batch). At KB scale, the "catalog" is the
index or a compact activation seed, the "activated instructions" are the compiled
summary/concept/entity pages, and the "on-demand resources" are the raw sources referenced via
`source_refs`.

### Micro

- B01-C002: three-tier loading — startup metadata/catalog, activated instructions, on-demand
  resources.
- B01-C004: clients should discover, parse frontmatter, disclose a compact catalog, and
  activate full content only on selection.
- B01-C010: keep entrypoints concise; move heavy material into references — applied at KB scale
  this is "keep compiled pages concise; point to raw sources instead of copying them."
- phase2-specialized-index-compile-plan-20260702.md lines 122-134: names
  `compiled_kb_pages_vs_raw_sources`, `refs_not_copies`, and `smallest_useful_file_shape` as
  explicit token-economy design questions this concept answers.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Agent Skills use a three-tier progressive disclosure model: catalog metadata, activated instructions, and on-demand resources."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Clients should discover skill directories, parse frontmatter, disclose a compact catalog, and activate full instructions only when selected by the model or user."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C004"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The reusable design rule is to keep entrypoints concise and move heavy contracts, schemas, and examples into referenced files rather than the main activated file."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C010"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C004
    claim: "The token-economy design goal for this KB includes 'compiled KB pages vs raw sources' and 'refs not copies' as explicit questions to answer through page design."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 122-134 (token_economy_and_information_design_index)"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "How should an agent read its own knowledge base without rereading the whole corpus every session?"
    leads_to: "claude-code-orchestration-design/concepts/agent-specific-knowledge-base.md"
    rationale: "Agent-specific-knowledge-base is the durable-role application of this loading pattern."
  - question: "What is the KB-wide rule for token-efficient file design?"
    leads_to: "claude-code-orchestration-design/summaries/token-efficient-information-design.md"
    rationale: "The summary page generalizes this concept across skills, handoffs, and agent KBs."
  - related_page: "claude-code-orchestration-design/concepts/compact-activation-seed.md"
    relation: "Compact-activation-seed is the first tier this concept's load order begins with."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C002"
    supports: "Three-tier progressive disclosure model."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C004"
    supports: "Discovery-catalog-activate sequencing."
  - source_id: "phase1-batch01-skill-package-contracts"
    source_pointer: "claim B01-C010"
    supports: "Concise-entrypoint, deep-reference rule at file scale."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "lines 122-134"
    supports: "KB-scale statement of the same pattern as a design objective."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Retrieval ranking across compiled pages is not yet built; this concept assumes an index or ranked source set exists, which is still being compiled in this same Phase 2 pass."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 216-223 (next_action)"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Whether Apex canonical skills should follow strict cross-client progressive disclosure rules or a Claude Code-native variant remains open (B01-Q001) and affects how strictly agent KBs should mirror the skill-level tiering."
    source_pointer: "phase1-batch01-skill-package-contracts.md open question B01-Q001"
    proposed_handling: "ask_operator"
```
