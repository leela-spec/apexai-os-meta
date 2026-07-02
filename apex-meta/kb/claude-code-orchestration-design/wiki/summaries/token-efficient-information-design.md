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
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Token-Efficient Information Design

```yaml
summary_id: token_efficient_information_design
specialized_indexes:
  - token_economy_and_information_design_index
pattern: >
  Store durable knowledge in small source-grounded files, expose compact indexes
  first, and load deeper pages or raw sources only when the query requires them.
used_when:
  - "Designing KBs, skill packages, handoffs, prompt packs, or repo maps."
  - "Reducing repeated raw-source rereads across sessions."
not_used_when:
  - "The current user needs exhaustive raw-source audit instead of compiled retrieval."
reads:
  - "wiki/index.md"
  - "compiled summaries/concepts/entities"
  - "raw source only after source_refs justify it"
writes:
  - "compact pages with frontmatter, source_refs, and short YAML"
token_efficiency:
  - "Refs not copies."
  - "YAML-first structure."
  - "Progressive disclosure from index to page to raw source."
  - "File state over chat state."
drift_controls:
  - "claim_label and confidence are explicit."
  - "Stop conditions prevent momentum errors and context bloat."
unresolved_or_deferred:
  - "SQLite/retrieval index build is S7+, not S6."
```

This page is the KB's rule for making future orchestration cheap to query and harder to hallucinate.
