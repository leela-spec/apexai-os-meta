---
title: "SWE-agent"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "swe-agent"
entity_type: "external_repo"
source_refs:
  - source_id: "phase1-batch03-external-orchestration-patterns"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch03-external-orchestration-patterns.md"
    source_hash: "dbe4e500d5c22cc61adc4e1364412da71d3db683"
    source_pointer: "claims B03-C011 through B03-C012; entities extracted"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-02T13:30:00Z"
confidence: "medium"
claim_label: "source_backed_summary"
status: "active"
---

# SWE-agent

```yaml
role: "Comparative source for agent-computer-interface and tool-output discipline."
used_when:
  - "Retrieving examples of bounded tool interaction design."
not_used_when:
  - "Treating external implementation details as Apex authority."
reads:
  - "ACI documentation"
writes:
  - "comparative interface pattern only"
token_efficiency:
  - "Concise tool outputs reduce context cost."
drift_controls:
  - "External details remain comparative, not authoritative."
deferred:
  - "No external repo runtime files are created in S6."
```
