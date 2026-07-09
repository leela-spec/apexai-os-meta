---
title: "MCP Allowlist and Injection Risk"
page_type: concept
kb_slug: claude-code-orchestration-design
run_id: max-run-20260709
status: new_parallel_compile
source_policy: source_preserving
legacy_output_policy: old_pages_for_comparison_only
confidence: high
claim_label: source_backed_summary
source_refs:
  - source_path: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
---

# MCP Allowlist and Injection Risk

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - rank: 1
    source: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
    rationale: "Primary source for Claude Code MCP behavior and trust warning."
    coverage: "External tools, databases, APIs, transports, approvals, and prompt-injection warning."
```

## Macro / Meso / Micro

### Macro

MCP is an external connectivity layer and therefore higher risk than a local knowledge page or skill instruction.

### Meso

Use MCP only when external systems are necessary, servers are trusted, and access scope is explicit.

### Micro

This KB should route MCP questions to risk review before recommending configuration.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "MCP servers should be trusted before connection because external content can create prompt-injection risk."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
    confidence: high
    claim_label: source_backed_summary
```

## Routes Here

```yaml
routes:
  - question: "What are the risks of MCP and plugin surfaces?"
    leads_to: apex-meta/kb/claude-code-orchestration-design/wiki/concepts/max-run-20260709/mcp-allowlist-and-injection-risk.md
    rationale: "MCP trust and injection-risk route."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Reopen before approving or writing any MCP server configuration."
    source_pointer: apex-meta/kb/claude-code-orchestration-design/raw/source-groups/claude-orchestration-agents/raw/refs/orchestration-agents-in-cc/secondary-code-claude-com-docs-en-mcp.md.md
    proposed_handling: ask_operator
```
