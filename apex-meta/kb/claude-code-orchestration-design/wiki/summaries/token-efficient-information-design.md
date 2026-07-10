---
title: "Token-Efficient Information Design"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "token-efficient-information-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; token_economy_and_information_design_index questions"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C011; progressive disclosure"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C008 through B03-C013; repo-map context compression"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "progressive-disclosure-for-agent-kbs"
  - "compact-activation-file"
  - "compact-activation-seed"
  - "low-token-handoff-design"
related_entities:
  - "agent-skills-standard"
review_flags: []
---

# Token-Efficient Information Design

## Core Summary

This KB's evidence converges on one repeated design rule at every scale examined — a single
skill file, a handoff packet, and a whole knowledge base: store durable knowledge in small,
source-grounded files, expose a compact catalog or index first, and load deeper pages or raw
sources only when the specific task requires them. At the skill level this is documented
directly as the three-tier progressive disclosure model (catalog metadata, activated
instructions, on-demand resources) plus the rule to keep the entrypoint concise and push heavy
contracts into references (phase1-batch01-skill-package-contracts.md claims B01-C002, B01-C010).
At the Apex application level, the same instinct shows up as "thin scaffold, deep appendices"
and explicit source-authority preflight before synthesis or writes
(phase1-batch04-apex-application-patterns.md concepts thin-scaffold-deep-appendices,
source-authority-preflight; claim B04-C012). The Phase 2 specialized-index compile plan names
this pattern directly as its own index target, `token_economy_and_information_design_index`,
with explicit questions about what loads every session, what loads only on trigger, and how
refs replace copies (phase2-specialized-index-compile-plan-20260702.md lines 122-134).

## What This Adds

```yaml
adds:
  - "A named, KB-wide design objective (token_economy_and_information_design_index) that ties together skill-level progressive disclosure, Apex handoff/state discipline, and repo-map-style context compression under one rule."
  - "An explicit contrast between what should load every session (compact activation seeds/indexes) and what should almost never load directly (raw source corpora) unless justified by an uncertainty trigger."
clarifies:
  - "Progressive disclosure is not merely a skill-authoring convention; it is the same shape this KB itself uses for its own summary/concept/entity pages."
  - "Thin-scaffold-deep-appendices (Apex application patterns) and progressive-disclosure (skill packages) are two independently-sourced statements of the same underlying rule."
limits:
  - "This summary does not fix an exact packet size budget or a numeric token ceiling; those remain open per the compile plan's own core questions."
  - "This summary does not reread phase1-batch03-external-orchestration-patterns.md in full for this compile pass; its repo-map/context-compression claims are carried forward via the existing source_ref rather than re-verified line-by-line."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch01-skill-package-contracts"
    rationale: "Directly read for this compile pass; supplies the concrete, high-confidence progressive-disclosure and concise-entrypoint mechanics this pattern generalizes from."
    coverage: "Claims B01-C001 through B01-C011; concepts skill-package-contract, progressive-disclosure."
  - source_id: "phase1-batch04-apex-application-patterns"
    rationale: "Directly read for this compile pass; supplies the Apex-specific 'thin scaffold, deep appendices' and 'source authority preflight' concepts that extend the same rule beyond skill files into prompt/workflow and KB-build practice."
    coverage: "Claim B04-C012; concepts thin-scaffold-deep-appendices, source-authority-preflight, fetch-back-validation; contradiction B04-T001."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Names this pattern as its own specialized index and supplies the explicit core questions this summary organizes around."
    coverage: "token_economy_and_information_design_index core questions, lines 122-134."
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Existing source_ref carried forward from this page's prior compile; covers repo-map-style context compression as an additional instance of the same pattern, not reread in full this pass."
    coverage: "Claims B03-C008 through B03-C013 (per existing source_ref pointer; not re-verified line-by-line in this compile)."
```

## Macro / Meso / Micro

### Macro

Whether the unit is a single skill file, a handoff packet between agents, or an entire
knowledge base, the corpus repeatedly rewards the same shape: a small, always-available surface
that routes to deeper material, with the deeper material staying source-grounded and reachable
by reference rather than duplicated inline. This is the KB's own rule for making future
orchestration cheap to query and harder to hallucinate.

### Meso

At the skill level, this is the three-tier progressive disclosure model plus the concise-
entrypoint rule (B01-C002, B01-C010). At the Apex application level, it is "thin scaffold, deep
appendices" — activation/scaffold files stay compact while schemas and evidence live in
referenced appendices (B04-C012, concept thin-scaffold-deep-appendices) — paired with a
source-authority preflight that establishes which sources outrank memory or unverified claims
before any synthesis or write happens (concept source-authority-preflight). Both instantiate the
same underlying rule from independent source lanes (official Agent Skills material versus
Apex-specific prompt/workflow doctrine), which raises this pattern's confidence.

### Micro

- B01-C002: three-tier progressive disclosure (catalog, activated instructions, on-demand
  resources).
- B01-C010: keep entrypoints concise; move heavy contracts/schemas/examples to references.
- B04-C012: the promptflow base-build contract enforces thin scaffold/deep appendices, index
  plausibility checks, and quality gates before scaffold drafting.
- B04-T001: explicit documented tension — rich execution contracts are needed, but should not
  bloat activation files; sources converge on pushing detail into references/appendices instead.
- phase2-specialized-index-compile-plan-20260702.md lines 122-134: names
  `compiled_kb_pages_vs_raw_sources`, `refs_not_copies`, `yaml_first_artifact_design`,
  `smallest_useful_file_shape`, and `packet_size_budget` as the concrete design questions this
  pattern must answer.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Agent Skills rely on progressive disclosure: startup metadata/catalog, activated SKILL.md instructions, and on-demand bundled resources."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C002"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C002
    claim: "The strongest reusable design rule is keeping the entrypoint concise/triggerable and pushing heavy contracts, schemas, and examples into referenced files."
    source_pointer: "phase1-batch01-skill-package-contracts.md claim B01-C010"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "The promptflow base-build contract enforces repo boundary, target lock, source authority, thin scaffold/deep appendices, index plausibility checks, and quality gates before scaffold drafting."
    source_pointer: "phase1-batch04-apex-application-patterns.md claim B04-C012"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C004
    claim: "There is a documented tension between needing rich Apex execution contracts and keeping activation/scaffold files compact; the resolution both sources converge on is pushing dense material into references or appendices."
    source_pointer: "phase1-batch04-apex-application-patterns.md contradiction B04-T001"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What should load every session versus only when a task specifically triggers it?"
    leads_to: "claude-code-orchestration-design/concepts/progressive-disclosure-for-agent-kbs.md"
    rationale: "That concept page details the mechanism this summary generalizes across skills, handoffs, and KBs."
  - question: "How should a compact entrypoint file be structured to stay within this design rule?"
    leads_to: "claude-code-orchestration-design/concepts/compact-activation-file.md"
    rationale: "Direct file-level instance of the rule this summary states at KB scale."
  - related_page: "claude-code-orchestration-design/concepts/low-token-handoff-design.md"
    relation: "Applies the same refs-not-copies, compact-packet principle specifically to agent-to-agent handoffs."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The SQLite/retrieval index build for this KB is explicitly deferred to a later phase (S7+), so 'compiled KB pages vs raw sources' retrieval ranking is not yet mechanized."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 26-27 (retrieval_indexing_after_phase2: not_yet)"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "This summary's phase1-batch03-external-orchestration-patterns references (repo-map context compression) were carried forward from the page's existing source_refs and not reread line-by-line in this compile pass; treat those specific claim numbers as unverified for this revision."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md claims B03-C008 through B03-C013 (existing source_ref, not reread this pass)"
    proposed_handling: "revisit_source"
  - id: U003
    description: "No fixed numeric packet size budget or file-size ceiling has been established; the compile plan lists 'packet_size_budget' as an open core question rather than a settled answer."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md lines 122-134 (token_economy_and_information_design_index)"
    proposed_handling: "leave_as_gap"
```

This page is the KB's rule for making future orchestration cheap to query and harder to hallucinate.
