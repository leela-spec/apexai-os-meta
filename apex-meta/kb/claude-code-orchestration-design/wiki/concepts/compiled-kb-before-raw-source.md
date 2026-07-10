---
title: "Compiled KB Before Raw Source"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compiled-kb-before-raw-source"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 124-137; compiled KB pages vs raw sources"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-process-retrospective-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase1-process-retrospective-20260702.md"
    source_hash: "8b011af3de9d3dc7ef5859964437603717d4b9a7"
    source_pointer: "lines 77-123; source-routed not exhaustive"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts: []
related_entities: []
review_flags: []
---

# Compiled KB Before Raw Source

## Definition

Compiled KB before raw source is the retrieval-priority rule that a future agent answering an orchestration-design question should consult this KB's compiled wiki index and pages first, and open raw source material only when a compiled page is missing, flags low confidence, or explicitly requires verification via its `source_refs`. This concept directly answers the compile plan's `token_economy_and_information_design_index` core question `compiled_kb_pages_vs_raw_sources`, and it is evidenced by this KB's own design: Phase 1 was itself a source-routed, not exhaustive, pass over the raw corpus, which is precisely why the compiled layer — not the raw corpus — should be the default entry point.

## Operating Rules

```yaml
rules:
  - "Start a query at wiki/index.md and the relevant summary/concept/entity pages before opening raw/ source material."
  - "Open raw source material only when a compiled page is absent, marked low confidence, flags an uncertainty trigger, or when a claim must be independently re-verified."
  - "Use each compiled page's source_refs as the pointer path into raw material rather than re-searching the raw corpus from scratch."
  - "Do not treat compiled pages as exhaustive corpus coverage; Phase 1 was source-routed sampling, not a full line-by-line pass over every raw file."
reads:
  - "wiki/index.md"
  - "summary/concept/entity pages"
  - "source material only when source_refs require it"
writes:
  - "query packet or answer context"
token_efficiency: "Compiled pages reduce repeated full-corpus reads for the same recurring orchestration-design questions."
drift_controls: "Source material remains reachable through source_refs for verification, so compiled-first retrieval does not silently hide provenance."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Primary source: names compiled_kb_pages_vs_raw_sources as an explicit token_economy_and_information_design_index core question, alongside refs_not_copies and what_should_be_loaded_only_when_triggered."
    coverage: "Frames the retrieval-priority question this concept answers."
  - source_id: "phase1-process-retrospective-20260702"
    rationale: "Direct evidence for why compiled pages must be the default: Phase 1 itself was deliberately source-routed rather than exhaustive, so raw corpus completeness cannot be assumed even by an agent willing to read raw files directly."
    coverage: "Section 3, source-routed value and blind-spot profile, lines 77-123."
```

## Macro / Meso / Micro

### Macro

`token_economy_and_information_design_index` asks directly what should be loaded every session, what should be loaded only when triggered, what should almost never be loaded directly, and — specifically — how compiled KB pages should be weighed against raw sources. Compiled-KB-before-raw-source is this KB's answer for that last question: the compiled wiki layer is the default entry point precisely because it already carries source pointers, confidence labels, and claim status, while the raw corpus does not carry any of that framing on its own.

### Meso

This is reinforced by the KB's own retrospective on how Phase 1 was actually built: Phase 1 did not read all files in the raw corpus end-to-end; it used deterministic Phase 0 artifacts (corpus profile, source-priority candidates, topic-file map, navigation report, migration source-root map) to route the LLM toward high-value source batches. The retrospective is explicit that this is "a targeted semantic ingest, not a complete line-by-line semantic pass over the entire raw corpus," and it lists concrete blind spots this creates (low-ranked files, duplicated sources, code-heavy external repos, stale snapshots, operator-policy-only questions). Because the compiled layer already accounts for this — auditable source selection, explicit confidence, and visible open questions — a future agent gets more reliable, better-labeled information from the compiled pages than from randomly sampling the raw corpus itself.

### Micro

- Compile plan `token_economy_and_information_design_index` core question `compiled_kb_pages_vs_raw_sources`, alongside `refs_not_copies` and `what_should_be_loaded_only_when_triggered` (compile plan lines ~124-134).
- Retrospective section 3 (`phase1-process-retrospective-20260702.md` lines 77-98): source-routed value — reduces token cost, avoids blind full-corpus loading, preserves auditable source selection, keeps Phase 1 human-reviewable, supports iterative later deepening.
- Same section, blind-spot profile (lines 100-119): low-ranked files, duplicated sources, code-heavy external repos, stale/snapshot docs, operator-policy questions, each with a stated mitigation (e.g., use Phase 2 open questions to pull additional files when gaps appear).
- Retrospective conclusion (lines 121): source-routed Phase 1 creates useful semantic coverage at lower token cost but "must not be represented as exhaustive corpus comprehension" — the direct textual basis for why the compiled layer, with its explicit confidence/uncertainty framing, should be consulted first rather than treated as equivalent to the raw corpus.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "token_economy_and_information_design_index names compiled_kb_pages_vs_raw_sources as a core question for how retrieval priority should be designed to reduce token cost and drift."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, token_economy_and_information_design_index core_questions"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Phase 1 semantic ingest was source-routed rather than exhaustive: it used deterministic Phase 0 routing artifacts to select high-value batches instead of reading the full raw corpus line-by-line."
    source_pointer: "phase1-process-retrospective-20260702.md lines 77-98"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Source-routed Phase 1 coverage creates identifiable blind spots (low-ranked files, duplicate sources, code-heavy repos, stale snapshots, operator-policy-only questions), each with a stated mitigation, which is why compiled pages should carry explicit confidence/uncertainty framing rather than be treated as raw-corpus-equivalent."
    source_pointer: "phase1-process-retrospective-20260702.md lines 100-121"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should a future agent copy source text into the KB or just point to it?"
    leads_to: "claude-code-orchestration-design/concepts/refs-not-copies.md"
    rationale: "Refs-not-copies is the sibling token_economy_and_information_design_index answer about how compiled pages should reference (not duplicate) raw material."
  - question: "How was this KB's Phase 1 ingest actually scoped, and what are its known blind spots?"
    leads_to: "claude-code-orchestration-design/wiki/summaries/token-efficient-information-design.md"
    rationale: "That summary page compiles the broader token-economy synthesis this concept is one specific answer within."
  - related_page: "claude-code-orchestration-design/concepts/yaml-first-artifact-design.md"
    relation: "Both concepts come from the same token_economy_and_information_design_index and both use this KB's own compiled artifacts as self-evidence."
```

## Evidence

```yaml
evidence:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "token_economy_and_information_design_index core_questions, compiled_kb_pages_vs_raw_sources"
    supports: "Definition and Macro section."
  - source_id: "phase1-process-retrospective-20260702"
    source_pointer: "lines 77-98, source_routed_value"
    supports: "Meso section: why the compiled layer is more reliable than raw sampling."
  - source_id: "phase1-process-retrospective-20260702"
    source_pointer: "lines 100-121, possible_blind_spots and conclusion"
    supports: "Micro section: concrete blind spots and the explicit non-exhaustive framing."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Deterministic retrieval-index/lint support for enforcing compiled-first lookup (rather than relying on agent discipline alone) is a later S7+ concern, not yet built."
    source_pointer: "phase2-specialized-index-compile-plan-20260702.md, section 8 next_action"
    proposed_handling: "leave_as_gap"
  - id: U002
    description: "Low-ranked files, duplicated sources, code-heavy external repos, and stale snapshots are named blind spots of the source-routed Phase 1 pass; a compiled page silent on one of these should trigger a raw-source revisit rather than be assumed complete."
    source_pointer: "phase1-process-retrospective-20260702.md lines 100-119, possible_blind_spots"
    proposed_handling: "revisit_source"
```
