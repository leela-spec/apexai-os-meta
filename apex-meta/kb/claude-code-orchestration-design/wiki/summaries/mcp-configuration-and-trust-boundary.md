---
title: "MCP Configuration and Trust Boundary"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "mcp-configuration-and-trust-boundary"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C014; MCP connects external tools and requires trust evaluation"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "Q005 MCP policy and phase2_implications lines 49-52, 95-100"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "claude_mechanism_mapping_index core question: when_plugin_or_mcp_is_deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_entities:
  - "claude-code-orchestration-design/entities/mcp.md"
review_flags: []
---

# MCP Configuration and Trust Boundary

## Core Summary

MCP is an external connectivity layer, not a default orchestration layer. It connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk (B02-C013). Apex should treat MCP configuration as deferred until server allowlists, trust boundaries, and prompt-injection handling are explicit — a stance the operator confirmed directly in Phase 1 review: `mcp_later`, defer MCP policy and committed `.mcp.json` rules, and preserve the topic as an open question or later policy page (Q005). This mirrors the broader tension already flagged in Phase 1: project-level skills, hooks, and MCP configuration are all shareable and useful, but also trust-sensitive, and Apex wants repo-native orchestration while Claude Code's own docs warn that untrusted projects should not silently inject instructions or tool surfaces (B02-T002).

## What This Adds

```yaml
adds:
  - "An explicit deferred-policy stance for MCP: no committed .mcp.json, no server allowlist, and no runtime server configuration in this KB compile step (per operator Q005 and Phase 2 non-goals)."
  - "A named trigger condition for when MCP stops being deferred: when a future implementation must decide whether a server belongs in project, user, or managed scope."
clarifies:
  - "MCP's value proposition (external tool/data access) is inseparable from its cost (trust evaluation, injection-risk exposure) per B02-C013; this summary does not treat MCP as a free capability."
  - "This summary extends, but does not edit, the existing entities/mcp.md page — the entity page documents what MCP is; this page documents the current Apex policy stance toward it."
limits:
  - "No .mcp.json or runtime server config is produced by this summary."
  - "Server allowlist policy and trust review procedure remain unresolved (see Uncertainty)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary-docs-derived claim establishing MCP's purpose and its trust/injection-risk requirement, which is the technical basis for the deferred-policy stance."
    coverage: "B02-C012 plugin/MCP bundling context; B02-C013 MCP purpose and trust evaluation; B02-C014 layered control plane placing MCP at the outer edge; B02-T002 repo-native orchestration vs trust safety."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "The direct operator decision (Q005) that this summary compiles into doctrine; without this decision the deferred stance would only be an inference."
    coverage: "Q005 mcp_policy decision and phase2_implications listing MCP allowlist/committed .mcp.json policy as a boundary/open item."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Frames the mapping question (when_plugin_or_mcp_is_deferred) that this summary directly answers for MCP."
    coverage: "claude_mechanism_mapping_index core question list, lines 110-123."
```

## Macro / Meso / Micro

### Macro

MCP sits at the outer edge of the Claude Code mechanism ladder because it is the mechanism with the highest external-trust cost. Apex's current posture toward MCP is deliberate deferral: document what MCP is and why it matters (entity page), but do not commit server configuration, allowlists, or trust procedures until those decisions can be made explicitly rather than by default.

### Meso

Two Phase 1 findings jointly produce this stance. First, the primary Claude Code docs describe MCP's dual nature directly: it is a genuine connectivity layer for external tools/data (B02-C013, use cases), but the same claim carries the trust-evaluation and injection-risk warning as an inseparable half of MCP's definition. Second, the operator explicitly reviewed this and chose deferral (Q005) rather than either adopting MCP now or ruling it out permanently — the decision is `mcp_later`, meaning the door stays open but the policy work stays undone until it is confirmed necessary.

### Micro

Source pointers: `secondary-code-claude-com-docs-en-mcp.md.md` lines 7-15 (MCP purpose), lines 17-27 (use cases), lines 32-36 (trust and prompt-injection warning), lines 60-146 (server transports), lines 147-190 (management, trust approval, reconnection), lines 196-218 (channels, timeout, output limits); operator-phase1-review-decisions-20260702.md lines 86-89 (Q005), lines 132-137 (phase2_implications boundary/open items).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk."
    source_pointer: "B02-C013"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/entities/mcp.md"
  - claim_id: C002
    claim: "Apex's Phase 1 operator review decided to defer MCP policy and committed .mcp.json rules (mcp_later), preserving the topic as an open question or later policy page rather than current doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 86-89 (Q005)"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/entities/mcp.md"
  - claim_id: C003
    claim: "Project-level skills, hooks, and MCP configuration are shareable and useful but trust-sensitive; Apex wants repo-native orchestration while Claude Code warns against silently trusting untrusted-project instruction or tool injection."
    source_pointer: "B02-T002"
    confidence: "medium"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "Is it safe to commit an MCP server config to this repo?"
    leads_to: "claude-code-orchestration-design/entities/mcp.md"
    rationale: "The entity page documents MCP's identity and trust requirement; this summary documents the current deferred-policy stance around it."
  - related_page: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    relation: "MCP occupies the outermost, most-deferred rung of the same mechanism ladder this summary applies to MCP specifically."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "How should Apex distinguish MCP servers that are safe to commit in .mcp.json from user-local or operator-private MCP servers? (B02-Q004)"
    source_pointer: "B02-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "MCP server allowlist and committed .mcp.json policy remain explicit boundary/open items per operator Phase 2 implications, not settled doctrine."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 132-137"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Trust review procedure for MCP servers is unresolved; revisit if any future implementation proposes a concrete server allowlist."
    source_pointer: "B02-T002; operator-phase1-review-decisions-20260702.md lines 86-89"
    proposed_handling: "ask_operator"
```
