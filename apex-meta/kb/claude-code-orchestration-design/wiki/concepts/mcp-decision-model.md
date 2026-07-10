---
title: "MCP Decision Model"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "mcp-decision-model"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "B02-C012 through B02-C014; plugins bundle MCP, MCP external connectivity, layered control plane"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "claude_mechanism_mapping_index: when_plugin_or_mcp_is_deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "mcp-config-boundary"
  - "mcp-allowlist-and-injection-risk"
  - "plugin-deferment-rule"
  - "mechanism-ladder"
related_entities:
  - "model-context-protocol"
review_flags: []
---

# MCP Decision Model

## Definition

The MCP decision model is the ordered set of checks Apex applies before adopting Model Context Protocol as the mechanism for a capability: confirm the capability genuinely requires live external access (tool, API, database, repository service, or event channel) rather than static or copied source material, confirm no simpler local mechanism (compiled KB page, project file, project skill, deterministic script, or operator-mediated handoff) already satisfies the need, and only then propose an MCP server subject to the allowlist and injection-risk review described on companion pages. It is the "should we even consider MCP" gate that precedes the config-boundary and allowlist gates.

## Operating Rules

```yaml
rules:
  - "Choose MCP only after confirming a compiled KB page, local file, project skill, deterministic report, or operator-mediated handoff is not sufficient."
  - "Require the capability need to involve live access to an external tool, API, database, repository service, or event channel before considering MCP at all."
  - "Record the outcome of this check as a decision record: use_local, defer_mcp, or propose_mcp_review — never as a silent default to MCP."
  - "Do not promote MCP tool output into doctrine without source validation and injection-risk review, even after a propose_mcp_review outcome."
  - "Do not write any runtime MCP configuration as part of applying this decision model during Phase 2 KB compile (S6)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "B02-C012 through B02-C014 ground the layered-control-plane view in which MCP is one specific rung (external tool surfaces), reserved for when other layers are insufficient."
    coverage: "Plugin bundling of MCP servers, MCP's external connectivity purpose, and the interpretive layered control plane claim."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "The mechanism-mapping index in this planning log names the explicit condition set for when plugin-or-MCP adoption should be deferred, which is the direct decision-model input for this page."
    coverage: "claude_mechanism_mapping_index: when_plugin_or_mcp_is_deferred criteria."
```

## Macro / Meso / Micro

### Macro

MCP is the most externally-reaching, most trust-costly mechanism in Claude Code's orchestration surface, so Apex treats adopting it as a decision to justify rather than a default. The decision model exists to stop MCP from becoming the reflexive answer to "how do we connect to X," when a local file, a project skill, or a deterministic script would satisfy the same need with far less trust and maintenance overhead.

### Meso

The model works as a gate: first ask whether the task actually needs live external access rather than a one-time copy of external information (if it's just reference material, ingest it into the KB instead); second ask whether a controlled tool interface is truly required rather than static content; only if both hold does the task proceed to a propose_mcp_review outcome, which then must pass the allowlist and injection-risk checks described in `mcp-allowlist-and-injection-risk` and respect the `mcp-config-boundary` rule against compile-time config writes. This mirrors the broader layered-control-plane interpretation (B02-C014), where `CLAUDE.md`/rules handle guidance, skills handle repeatable procedures, hooks/settings handle enforcement, subagents handle context isolation, and MCP is reserved specifically for external tool surfaces — the last, most expensive rung.

### Micro

B02-C012 notes plugins bundle multiple components including MCP servers into distributable directories (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C012), and B02-C013 grounds MCP's purpose and trust requirement (claim B02-C013). B02-C014, labeled `interpretation` at high confidence, frames the full layered control plane: "CLAUDE.md and rules for always-on/path-scoped guidance; skills for repeatable procedures; hooks/settings for enforcement; subagents for context isolation; MCP for external tool surfaces; plugins for distributable bundles" (claim B02-C014). The referenced `phase2-specialized-index-compile-plan-20260702.md` mechanism-mapping index names the criteria for when plugin-or-MCP adoption is deferred rather than adopted.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Claude Code orchestration should be modeled as a layered control plane in which MCP specifically serves external tool surfaces, distinct from skills, hooks, subagents, and plugins."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "MCP connects Claude Code to external tools, databases, APIs, and event channels, but requires explicit trust evaluation because external content can expose prompt-injection risk."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C013"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Plugins bundle multiple Claude Code components, including MCP servers, into distributable directories, which means MCP adoption can arrive either as a standalone server decision or as part of a plugin decision."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C012"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Do we actually need MCP for this, or is there a simpler mechanism?"
    leads_to: "claude-code-orchestration-design/concepts/mcp-decision-model.md"
    rationale: "This page is the entry gate for deciding whether MCP is the right mechanism before any config or allowlist question arises."
  - related_page: "claude-code-orchestration-design/concepts/mcp-config-boundary.md"
    relation: "Once MCP passes this decision gate, config-boundary rules govern how and where it may be configured."
  - related_page: "claude-code-orchestration-design/concepts/plugin-deferment-rule.md"
    relation: "Plugins can bundle MCP servers, so plugin deferment and MCP deferment are linked packaging-timing decisions."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C012, B02-C013, B02-C014"
    supports: "Layered control-plane framing that positions MCP as the external-tool-surface rung, reserved for genuine external access needs."
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_pointer: "claude_mechanism_mapping_index.when_plugin_or_mcp_is_deferred"
    supports: "Explicit deferral criteria for plugin/MCP adoption decisions."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: how should Apex distinguish MCP servers that are safe to commit in .mcp.json from user-local or operator-private MCP servers? This affects the propose_mcp_review outcome path."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q004"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Contradiction: plugins support distribution of full orchestration bundles (including MCP servers), but plugin-shipped agents carry security restrictions and do not support every frontmatter field available to project/user subagents — this may affect whether MCP arrives via plugin or standalone server."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-T003"
    proposed_handling: "audit_item"
  - id: U003
    description: "MCP policy is deferred (Q005: mcp_later); the decision model here describes a gating pattern derived from the interpretive B02-C014 claim, not a finalized operational procedure."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q005_mcp_policy"
    proposed_handling: "revisit_source"
```
