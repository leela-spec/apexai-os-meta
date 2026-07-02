---
title: "Agent Skills Standard"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "agent-skills-standard"
entity_type: "standard"
source_refs:
  - source_id: "phase1-batch01-skill-package-contracts"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch01-skill-package-contracts.md"
    source_hash: "8a46dcf8bf15c18b0f0c6541cdf4e68475a777c1"
    source_pointer: "claims B01-C001 through B01-C013; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Agent Skills Standard

```yaml
role: "Portable folder, SKILL.md, frontmatter, resource, and validation standard for skills."
used_when:
  - "Evaluating canonical Apex skill-package shape."
not_used_when:
  - "Assuming every Claude Code runtime behavior is identical to the portable standard."
reads:
  - "SKILL.md"
  - "references"
  - "resources"
writes:
  - "validation expectations"
token_efficiency:
  - "Standard frontmatter and progressive disclosure reduce activation cost."
drift_controls:
  - "Spec tension with Claude Code runtime is kept visible."
deferred:
  - "Tool-specific compatibility policy may need later update."
```
