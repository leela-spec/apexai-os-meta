---
title: "Low-Token Handoff Design"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "low-token-handoff-design"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 72-85; refs replace full context"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C002 and B01-C010; progressive disclosure"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch04-apex-application-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch04-apex-application-patterns.md"
    source_hash: "aa9058146dfd2f220bd9dcae682633c63cb2164d"
    source_pointer: "claims B04-C009, B04-C011, B04-C014; clean handoff and state frames"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Low-Token Handoff Design

```yaml
pattern: "A handoff should carry pointers, claim status, and next action rather than replaying full evidence."
used_when:
  - "A downstream role needs enough context to proceed safely."
not_used_when:
  - "The receiver must independently audit the full source set."
reads:
  - "source_refs"
  - "artifact paths"
  - "validation status"
writes:
  - "compact packet"
token_efficiency:
  - "Use refs, slugs, and concise YAML fields instead of prose dumps."
drift_controls:
  - "Source refs and explicit status reduce memory reconstruction errors."
unresolved_or_deferred:
  - "Exact packet size budget is compiled separately."
```
