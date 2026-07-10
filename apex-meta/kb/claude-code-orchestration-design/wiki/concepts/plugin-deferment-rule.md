---
title: "Plugin Deferment Rule"
page_type: concept
kb_slug: "claude-code-orchestration-design"
concept_slug: "plugin-deferment-rule"
source_refs:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C012 through B02-C013; plugins and MCP"
    source_storage_mode: "pointer_only"
  - source_id: "operator-phase1-review-decisions-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/operator-phase1-review-decisions-20260702.md"
    source_hash: "34d9c16967d2f7f49b716d75c8bb1a2a10eb96a7"
    source_pointer: "lines 69-74 and 88-91; plugins and MCP deferred"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "mcp-decision-model"
  - "mechanism-ladder"
related_entities:
  - "claude-code-plugins"
review_flags: []
---

# Plugin Deferment Rule

## Definition

The plugin deferment rule states that Apex uses project skills as its current reusable orchestration surface, and explicitly defers plugin packaging (bundling skills, agents, hooks, MCP servers, and LSP integrations into distributable directories) until the project-skill layer has stabilized. Plugins remain a recognized, well-defined Claude Code mechanism, but adopting them for Apex's own orchestration is treated as later packaging work rather than a current requirement.

## Operating Rules

```yaml
rules:
  - "Use project skills as the current reusable orchestration surface for Apex; do not build plugin packaging as a first-line surface."
  - "Treat plugin adoption as later packaging work, to be revisited after the project-skill layer stabilizes."
  - "Do not bundle MCP servers, hooks, or agents into a plugin as an Apex deliverable during the current phase; MCP policy itself is separately deferred (see mcp-decision-model)."
  - "When a capability may later need distribution or external connectivity, note it as a deferment candidate rather than building plugin infrastructure prematurely."
  - "Do not write plugin manifests, plugin hooks, or plugin MCP configuration during Phase 2 KB compile (S6)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "operator-phase1-review-decisions-20260702"
    rationale: "Operator decision Q003 is the direct compile-policy source: use project skills now, plugins later, with an explicit defer list."
    coverage: "Q003_packaging_surface decision and defer list; Q005_mcp_policy deferral, since plugins can bundle MCP servers."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "B02-C012 and B02-C013 ground what plugins and MCP actually are, which is the mechanism this deferment decision applies to."
    coverage: "Plugin component bundling (skills, agents, hooks, MCP servers, LSP integrations) and MCP's external connectivity/trust requirement."
```

## Macro / Meso / Micro

### Macro

Claude Code plugins are a powerful distribution mechanism — a single installable package can carry skills, agents, hooks, MCP servers, and LSP integrations together. That power is exactly why Apex defers adopting plugins for its own orchestration: packaging decisions made too early tend to freeze an unstable design. Apex instead builds and stabilizes its reusable orchestration logic as plain project skills first, leaving the question of how (or whether) to package that logic as a distributable plugin for later.

### Meso

This deferment sits alongside a related deferment: MCP policy (Q005) is also deferred, and since plugins can bundle MCP servers (B02-C012), the two deferments reinforce each other — Apex is not yet ready to commit to either a distributable plugin surface or committed external-tool connectivity. Operator decision Q003 makes the packaging-surface decision explicit: `project_skills_now_plugins_later`, with plugins named directly under `defer`. The phase2_implications section separately confirms `project_skills_now_plugins_later` should be written as doctrine, while `plugin_packaging_timing` remains a boundary/open question — meaning the KB can assert the current-state decision (skills now) as settled, while still leaving the eventual plugin timeline open.

### Micro

B02-C012: "Plugins bundle multiple Claude Code components, including skills, agents, hooks, MCP servers, LSP servers, and monitors, into distributable directories" (`phase1-batch02-claude-code-orchestration-surface.md` claim B02-C012). Operator decision Q003 (`operator-phase1-review-decisions-20260702.md` lines 67-72): `decision: use_project_skills_as_current_reusable_orchestration_surface`; `defer: [plugins]`; note: "Plugins remain later packaging work after the project-skill layer stabilizes." The phase2_implications block lists `project_skills_now_plugins_later` under `write_as_doctrine` and `plugin_packaging_timing` under `write_as_boundary_or_open_question` (lines 122-137), meaning the "skills now" half is settled while the "plugins when" half stays open.

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "Apex uses project skills as the current reusable orchestration surface and defers plugin packaging until the project-skill layer stabilizes."
    source_pointer: "operator-phase1-review-decisions-20260702.md Q003_packaging_surface"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C002
    claim: "Plugins bundle multiple Claude Code components, including skills, agents, hooks, MCP servers, LSP servers, and monitors, into distributable directories."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md claim B02-C012"
    confidence: "high"
    claim_label: "source_backed_summary"
  - claim_id: C003
    claim: "The decision to use project skills now and defer plugins is written as Phase 2 doctrine, while the exact plugin packaging timing remains an open boundary question."
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.write_as_doctrine and write_as_boundary_or_open_question"
    confidence: "high"
    claim_label: "source_backed_summary"
```

## Routes Here

```yaml
routes:
  - question: "Should this capability be packaged as a plugin now, or kept as a project skill?"
    leads_to: "claude-code-orchestration-design/concepts/plugin-deferment-rule.md"
    rationale: "This page directly answers the packaging-surface timing question."
  - related_page: "claude-code-orchestration-design/concepts/mcp-decision-model.md"
    relation: "Plugins can bundle MCP servers, so plugin deferment and MCP deferment are linked packaging-timing decisions."
  - related_page: "claude-code-orchestration-design/concepts/mechanism-ladder.md"
    relation: "Plugin adoption sits at the distribution rung of the broader mechanism-selection ladder."
```

## Evidence

```yaml
evidence:
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_pointer: "B02-C012, B02-C013"
    supports: "What plugins bundle and why MCP (often bundled by plugins) carries trust requirements."
  - source_id: "operator-phase1-review-decisions-20260702"
    source_pointer: "Q003_packaging_surface, Q005_mcp_policy, phase2_implications"
    supports: "Explicit decision to use project skills now and defer plugins/MCP packaging."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "Open question: should Apex package reusable orchestration surfaces as plain repo skills, plugins, or both, once the project-skill layer stabilizes?"
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-Q002"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Contradiction: plugins support distribution of full orchestration bundles, but plugin-shipped agents have security restrictions and do not support every frontmatter field available to project/user subagents — relevant once plugin adoption is revisited."
    source_pointer: "phase1-batch02-claude-code-orchestration-surface.md B02-T003"
    proposed_handling: "audit_item"
  - id: U003
    description: "Plugin packaging timing remains an explicit boundary/open question, not settled beyond 'skills now, plugins later.'"
    source_pointer: "operator-phase1-review-decisions-20260702.md phase2_implications.write_as_boundary_or_open_question (plugin_packaging_timing)"
    proposed_handling: "revisit_source"
```
