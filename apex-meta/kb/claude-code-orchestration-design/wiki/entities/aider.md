---
title: "Aider"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "aider"
entity_type: "external_repo"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C008 through B03-C010; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "repo-map-context-compression"
review_flags: []
---

# Aider

## Identity

```yaml
entity:
  label: "Aider"
  type: "external_repo"
  aliases:
    - "Aider-AI/aider"
```

## Source-Grounded Summary

Aider is treated in this KB purely as a comparative external repository, used only for its repo-map / context-compression documentation (`aider/website/docs/ctags.md`). Batch 03 read this doc to understand how Aider frames the large-codebase context problem (B03-C008), how its repo map sends a compact representation of files, symbols, and call signatures (B03-C009), and to note that the specific ctags-based mechanism described was itself already superseded by a newer tree-sitter approach inside Aider (B03-C010). Aider is not treated as authoritative over Claude Code or Agent Skills documentation, and no Aider runtime behavior is adopted as Apex doctrine.

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    rationale: "Sole ingested source for this entity; ranked first (and only) because all claims about Aider trace back to this single batch's reading of ctags.md."
    coverage: "B03-C008 (context-compression problem framing), B03-C009 (repo-map mechanism and benefits), B03-C010 (ctags superseded by tree-sitter)."
```

## Macro / Meso / Micro

### Macro

Aider contributes one reusable idea to this KB: a compact repo map can let an agent infer APIs and ask for specific files instead of either loading a whole codebase or requiring hand-picked file selection. That idea is extracted as the `repo-map-context-compression` concept; Aider itself is retained only as the comparative source for that idea, not as an implementation target.

### Meso

Batch 03 read Aider's ctags documentation for three things: the problem statement (whole-codebase context doesn't fit, hand-picked files waste context and require manual selection — B03-C008), the mechanism (a concise map of files/symbols/signatures sent to the model — B03-C009), and a caveat (Aider's own docs note this ctags-based approach was superseded by tree-sitter — B03-C010). The caveat matters: it means Aider is being cited for a pattern it documents about its own history, not for its current implementation.

### Micro

- B03-C008: "Aider's repo-map documentation frames the core large-codebase problem as context compression: whole-codebase inclusion does not fit the context window, and hand-picked files waste context and require manual selection." (`ctags.md` lines 26-52, 86-107)
- B03-C009: "Aider's repo-map pattern sends a concise map of repository files, symbols, and call signatures so the model can infer APIs and ask for specific files when needed." (`ctags.md` lines 108-162, 164-205)
- B03-C010: "Aider itself notes that the older ctags-based map was superseded by a tree-sitter repo map, making ctags a historical pattern rather than the current implementation target." (`ctags.md` lines 18-23)

## Key Claims

```yaml
key_claims:
  - claim_id: B03-C008
    claim: "Aider's repo-map documentation frames the core large-codebase problem as context compression: whole-codebase inclusion does not fit the context window, and hand-picked files waste context and require manual selection."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; ctags.md lines 26-52, 86-107"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B03-C009
    claim: "Aider's repo-map pattern sends a concise map of repository files, symbols, and call signatures so the model can infer APIs and ask for specific files when needed."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; ctags.md lines 108-162, 164-205"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: B03-C010
    claim: "Aider itself notes that the older ctags-based map was superseded by a tree-sitter repo map, making ctags a historical pattern rather than the current implementation target."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; ctags.md lines 18-23"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "What repo-map pattern is Apex comparing against when it considers context compression for code-heavy repos?"
    leads_to: "claude-code-orchestration-design/entities/aider.md"
    rationale: "Aider's ctags documentation is the sole ingested example of a repo-map context-compression mechanism."
  - related_page: "claude-code-orchestration-design/entities/swe-agent.md"
    relation: "Both are batch03 comparative external-repo entities used for adjacent-but-distinct patterns (repo-map vs. agent-computer-interface)."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_pointer: "ctags.md lines 18-23, 26-52, 86-162, 164-205, 221-245"
    supports: "All B03-C008 through B03-C010 claims and the repo-map-context-compression concept"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Whether Apex should invest in a tree-sitter/LSP style repo-map layer for code-heavy repos, or keep Phase 0 maps to Markdown headings/links/frontmatter/keywords, remains unresolved. Operator decision Q006 explicitly defers this (defer_phase0_v1_5_code_repo_map_extension) pending code-heavy query failures."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-Q001, ctags.md lines 18-23, 221-245; operator-phase1-review-decisions-20260702.md Q006"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Aider's ctags approach is documented as already superseded within Aider's own project; future re-ingest should check whether the current tree-sitter mechanism is worth a dedicated read."
    source_pointer: "phase1-batch03-external-orchestration-patterns.md; B03-T001"
    proposed_handling: "revisit_source"
```
