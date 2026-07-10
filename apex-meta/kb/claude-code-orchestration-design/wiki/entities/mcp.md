---
title: "Model Context Protocol"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "mcp"
entity_type: "protocol"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C013; entities extracted model-context-protocol"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 88-91; MCP later/allowlist decision"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/summaries/mcp-configuration-and-trust-boundary.md"
review_flags: []
---

# Model Context Protocol

## Identity

```yaml
entity:
  label: "Model Context Protocol"
  type: "protocol"
  aliases:
    - "MCP"
    - "MCP servers"
```

## Source-Grounded Summary

MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk (B02-C013). It is documented with server transports, management/trust-approval/reconnection behavior, and channel/timeout/output limits (secondary-code-claude-com-docs-en-mcp.md.md lines 60-218). Apex's Phase 1 operator review explicitly deferred MCP policy: the decision was `mcp_later` — defer MCP policy and committed `.mcp.json` rules, and preserve the topic as an open question or later policy page rather than as current doctrine (operator decision Q005, lines 86-89).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary-docs-derived claim on MCP purpose, use cases, and trust/injection risk; the only source establishing MCP's functional role in the control plane."
    coverage: "B02-C013 MCP purpose and trust evaluation; B02-T002 repo-native orchestration vs trust safety tension; concepts_extracted mcp-tool-connectivity-layer."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator policy decision governing how this KB should treat MCP in Phase 2 — as deferred, not as implemented doctrine."
    coverage: "Q005 mcp_policy decision: defer MCP policy and committed .mcp.json rules."
```

## Macro / Meso / Micro

### Macro

MCP is the external-connectivity layer of the Claude Code control plane — the mechanism by which Claude Code reaches beyond its own file/tool surface to external systems (B02-C013). In the layered control-plane model (B02-C014), MCP sits at the outer edge alongside plugins: it is powerful but also the most trust-sensitive surface, since content returned from external servers is not automatically safe from prompt injection.

### Meso

The primary docs frame MCP's value (tool/data connectivity, B02-C013) against its cost (explicit trust evaluation and injection-risk exposure, same claim). This is not a hypothetical concern in Phase 1 — it is directly why the operator chose to defer MCP policy rather than adopt it as current doctrine (Q005). The unresolved tension is broader than MCP alone: project-level skills, hooks, and MCP configuration are all shareable and useful but also trust-sensitive, and Apex wants repo-native orchestration while Claude Code warns that untrusted projects should not silently inject instructions or tool surfaces (B02-T002).

### Micro

Source pointers: `secondary-code-claude-com-docs-en-mcp.md.md` lines 7-15 (MCP purpose), lines 17-27 (use cases), lines 32-36 (trust and prompt-injection warning), lines 60-146 (server transports), lines 147-190 (management, trust approval, reconnection), lines 196-218 (channels, timeout limits, output limits).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk."
    source_pointer: "B02-C013; secondary-code-claude-com-docs-en-mcp.md.md lines 7-36, 196-218"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Apex's Phase 1 operator review decided to defer MCP policy and committed .mcp.json rules, treating the topic as an open question or later policy page rather than current doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 86-89 (Q005)"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Project-level skills, hooks, and MCP configuration are shareable and useful but trust-sensitive; Apex wants repo-native orchestration while Claude Code warns against silently trusting untrusted-project instruction or tool injection."
    source_pointer: "B02-T002"
    confidence: "medium"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "When should Apex configure an MCP server instead of a project skill?"
    leads_to: "claude-code-orchestration-design/summaries/mcp-configuration-and-trust-boundary.md"
    rationale: "The MCP configuration and trust boundary summary is the compiled doctrine page for exactly this decision, and it explicitly treats MCP as deferred pending allowlist/trust design."
  - related_page: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    relation: "MCP is the outermost rung of the mechanism ladder, alongside plugins, used only when a task needs external connectivity that no internal mechanism can provide."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C013"
    supports: "MCP purpose and trust requirement"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-T002"
    supports: "Repo-native orchestration vs trust-safety tension"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q005, lines 86-89"
    supports: "MCP policy deferral decision"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "How should Apex distinguish MCP servers that are safe to commit in .mcp.json from user-local or operator-private MCP servers? (B02-Q004, open question)"
    source_pointer: "B02-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "MCP server allowlist and committed .mcp.json policy are explicitly listed as boundary/open items for Phase 2, not settled doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 132-137"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Project-level skills, hooks, and MCP configuration are trust-sensitive even though Apex wants repo-native orchestration (B02-T002); any Apex MCP design should reopen this tension before committing server config."
    source_pointer: "B02-T002"
    proposed_handling: "revisit_source"
```
