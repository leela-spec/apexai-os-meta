---
title: "Hook vs Skill Instruction"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "hook-vs-skill-instruction"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C005 through B02-C007 and B02-C015; hooks and enforcement"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 54-68; hard vs soft enforcement"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Hook vs Skill Instruction

```yaml
pattern: "Skill instructions guide behavior; hooks enforce selected tool or lifecycle gates."
used_when:
  - "A boundary must be reliable before or after a tool action."
not_used_when:
  - "The rule is style, terminology, or low-risk preference."
reads:
  - "risk category"
  - "tool/event context"
writes:
  - "policy decision or gate result"
token_efficiency:
  - "Hard gates remove repeated prose warnings from prompts."
drift_controls:
  - "High-risk gates are not left only to model compliance."
unresolved_or_deferred:
  - "No hook files are written in S6."
```
