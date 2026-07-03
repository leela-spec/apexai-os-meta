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
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# Aider

```yaml
role: "Comparative source for repo-map and context-compression patterns."
used_when:
  - "Retrieving compact repository-map design examples."
not_used_when:
  - "Adopting ctags as current Apex implementation target."
reads:
  - "repo-map documentation"
writes:
  - "context-compression pattern only"
token_efficiency:
  - "Repo maps help agents select relevant files before loading them."
drift_controls:
  - "Aider ctags material is treated as historical pattern where superseded."
deferred:
  - "Tree-sitter or LSP map decisions remain later work."
```
