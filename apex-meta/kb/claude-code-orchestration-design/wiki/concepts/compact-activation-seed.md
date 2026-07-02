---
title: "Compact Activation Seed"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "compact-activation-seed"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 67-70; activation seed vs deeper KB"
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

# Compact Activation Seed

```yaml
pattern: "A compact activation seed gives a role or skill enough routing, boundary, and next-read information to start without loading its full doctrine."
used_when:
  - "The system needs fast activation with progressive disclosure."
not_used_when:
  - "The task requires full source audit or detailed implementation instructions immediately."
reads:
  - "name or role"
  - "purpose"
  - "triggers"
  - "boundary"
  - "next files to read"
writes:
  - "activation context only"
token_efficiency:
  - "Keep long contracts, templates, and examples in referenced files."
drift_controls:
  - "Boundary and non-purpose clauses prevent role expansion."
unresolved_or_deferred:
  - "Concrete seed file format remains implementation-specific."
```
