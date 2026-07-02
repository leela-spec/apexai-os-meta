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
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Progressive Disclosure for Agent KBs

```yaml
pattern: "Agent KBs should load as index, then summary/concept, then raw source only when needed."
used_when:
  - "A durable role needs reusable doctrine without constant raw-source loading."
not_used_when:
  - "The operator requests a full source-by-source review."
reads:
  - "index"
  - "relevant compiled pages"
  - "raw source refs only as needed"
writes:
  - "source-grounded KB pages"
token_efficiency:
  - "Most tasks read one to three compiled pages instead of the corpus."
drift_controls:
  - "Source_refs preserve a path back to evidence."
unresolved_or_deferred:
  - "Retrieval ranking is built after S6."
```
