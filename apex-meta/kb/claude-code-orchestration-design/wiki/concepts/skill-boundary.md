---
title: "Skill Boundary"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "skill-boundary"
source_refs:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C011; skill package contract"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C004; skills and runtime controls"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Skill Boundary

```yaml
pattern: "Use a skill for a repeatable procedure with clear triggers, compact instructions, and optional referenced resources."
used_when:
  - "A workflow step recurs and benefits from packaged instructions."
not_used_when:
  - "The task needs multi-stage orchestration, isolated context, or hard enforcement."
reads:
  - "trigger description"
  - "procedure"
  - "referenced resources"
writes:
  - "procedure output artifact"
token_efficiency:
  - "Skill metadata is compact; deeper files load only when needed."
drift_controls:
  - "Skill non-purpose and completion gate constrain execution."
unresolved_or_deferred:
  - "Canonical Apex validation policy is strict, but runtime compatibility details may remain tool-specific."
```
