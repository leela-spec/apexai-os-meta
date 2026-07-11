---
title: "Model Context Protocol"
page_type: entity
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: needs_review
created_at: "2026-07-09"
updated_at: "2026-07-11"
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
---

# Model Context Protocol

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: secondary-code-claude-com-docs-en-mcp.md.md
    rationale: "Primary MCP source."
    coverage: "External tools, servers, transports, approvals, security warning, dynamic tools."
```

## Macro / Meso / Micro

### Macro

MCP connects Claude Code to external tools and systems.

### Meso

It can expose databases, APIs, issue trackers, designs, monitoring, and external event channels. This creates usefulness and prompt-injection/trust risk.

### Micro

Apex should use MCP only after explicit trust and allowlist review.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "MCP servers give Claude Code access to external tools, databases, and APIs."
    source_pointer: secondary-code-claude-com-docs-en-mcp.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What is MCP and when is it risky?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/entities/max-run-20260709/mcp.md
    rationale: "MCP entity route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before connecting any MCP server or approving project-scoped MCP configuration."
    source_pointer: secondary-code-claude-com-docs-en-mcp.md.md
    proposed_handling: ask_operator
```
