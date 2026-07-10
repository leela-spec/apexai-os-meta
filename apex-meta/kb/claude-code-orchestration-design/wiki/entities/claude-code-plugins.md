---
title: "Claude Code Plugins"
page_type: entity
kb_slug: "claude-code-orchestration-design"
entity_slug: "claude-code-plugins"
entity_type: "distribution_component"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C013; entities extracted"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 69-74; project skills now, plugins later"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
review_flags: []
---

# Claude Code Plugins

## Identity

```yaml
entity:
  label: "Claude Code plugins"
  type: "distribution_component"
  aliases:
    - "plugin bundle"
    - "plugin-bundled orchestration"
```

## Source-Grounded Summary

Plugins bundle multiple Claude Code components — skills, agents, hooks, MCP servers, and LSP integrations — into a single distributable directory (B02-C012). They exist so a stable capability can be packaged and shared beyond one project, rather than copy-pasted project by project. But plugin-shipped agents carry security restrictions and do not expose every frontmatter field that project- or user-level subagents get (B02-T003), so plugins are not a drop-in equivalent of native project configuration. The operator's Phase 1 review explicitly decided that Apex should use project skills as the current reusable orchestration surface and defer plugin packaging until that project-skill layer stabilizes (operator decision Q003, lines 69-74).

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary-docs-derived claims about plugin composition, components, and the plugin-agent security caveat."
    coverage: "B02-C012 plugin bundling; B02-T003 plugin agent restriction contradiction; concepts_extracted plugin-bundled-orchestration."
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator policy decision that directly governs how this KB should treat plugins in Phase 2 doctrine."
    coverage: "Q003 packaging_surface decision: project skills now, plugins deferred."
```

## Macro / Meso / Micro

### Macro

Plugins are the packaging and distribution layer of the Claude Code control plane. Where skills, hooks, subagents, and MCP servers are individual mechanisms, a plugin is a way to bundle several of them together as one installable unit. In the layered control-plane model (B02-C014), plugins sit at the outer edge — used only once a capability's shape has stabilized enough to be worth distributing.

### Meso

Phase 1 found that plugin components largely mirror their standalone counterparts (plugin skills, plugin agents, plugin hooks, plugin MCP servers, plugin LSP integrations — B02-C012), but with caveats: plugin-shipped subagents have security restrictions and an incomplete frontmatter surface compared to project/user subagent files (B02-T003). This means "plugin" is not simply "project config, zipped" — it is a distinct, more constrained runtime surface.

### Micro

Source pointers: `primary-code-claude-com-docs-en-plugins-reference.md.md` lines 15-18 (plugin definition and component list), lines 19-49 (plugin skills), lines 51-83 (plugin agents), lines 85-155 (plugin hooks), lines 156-190 (plugin MCP servers), lines 192-222 (plugin LSP integration); `primary-code-claude-com-docs-en-sub-agents.md.md` lines 230-237 (plugin subagent caveat).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Plugins bundle multiple Claude Code components, including skills, agents, hooks, MCP servers, LSP servers, and monitors, into distributable directories."
    source_pointer: "B02-C012; primary-code-claude-com-docs-en-plugins-reference.md.md lines 15-190"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Plugins support distribution of full orchestration bundles, but plugin-shipped agents have security restrictions and do not support every frontmatter field available to project/user subagents."
    source_pointer: "B02-T003; plugins-reference.md.md lines 51-83; sub-agents.md.md lines 230-237"
    confidence: "medium"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "Apex's Phase 1 operator review decided to use project skills as the current reusable orchestration surface and to defer plugin packaging until that layer stabilizes."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 67-72 (Q003)"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should Apex package reusable orchestration as a plugin instead of a project skill?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "The mechanism ladder places plugins after skills, workflows, and subagents; this page explains why."
  - related_page: "claude-code-orchestration-design/entities/claude-code-subagents.md"
    relation: "Plugin agents are a restricted variant of subagents; this page's B02-T003 claim is the key difference."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C012"
    supports: "Plugin bundling of components"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-T003"
    supports: "Plugin agent security/frontmatter restriction"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q003 packaging_surface, lines 67-72"
    supports: "Project skills now / plugins later doctrine"
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Should Apex package reusable orchestration surfaces as plain repo skills, plugins, or both? (B02-Q002, open question)"
    source_pointer: "B02-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Plugins support distribution but plugin agents carry security restrictions and an incomplete frontmatter surface versus project/user subagents (B02-T003)."
    source_pointer: "B02-T003"
    proposed_handling: "revisit_source"
  - id: U003
    description: "Plugin packaging timing is an explicit deferred/open item per operator Phase 2 implications (write_as_boundary_or_open_question: plugin_packaging_timing)."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 132-137"
    proposed_handling: "leave_as_gap"
```
