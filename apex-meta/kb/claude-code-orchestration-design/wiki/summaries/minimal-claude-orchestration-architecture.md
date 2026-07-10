---
title: "Minimal Claude Orchestration Architecture"
page_type: summary
kb_slug: "claude-code-orchestration-design"
summary_slug: "minimal-claude-orchestration-architecture"
source_refs:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "lines 38-137; corrected compile objective and specialized indexes"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-completion-report"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-completion-report.md"
    source_hash: "f604b3e31858da764eb2807084ca8282a1e4acc2"
    source_pointer: "lines 104-138; major concepts found"
    source_storage_mode: "pointer_only"
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    source_path: "apex-meta/kb/claude-code-orchestration-design/ingest-analysis/phase1-batch02-claude-code-orchestration-surface.md"
    source_hash: "505c6297d2c7198cbf0e77800577ab8e18a25d73"
    source_pointer: "claims B02-C001 through B02-C016"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T13:30:00Z"
updated_at: "2026-07-10T20:00:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
related_concepts:
  - "claude-code-orchestration-design/concepts/deterministic-script-boundary.md"
related_entities:
  - "claude-code-orchestration-design/entities/claude-code-skills.md"
review_flags: []
---

# Minimal Claude Orchestration Architecture

## Core Summary

A resilient Claude/Apex orchestration system should be a small layered control plane, not a swarm. Use always-loaded guidance for stable norms, skills for repeatable procedures, workflows for multi-stage processes, subagents for context-isolated work, scripts/hooks for deterministic enforcement, and plugins or MCP only when distribution or external connectivity is justified (compile plan lines 38-137; B02-C014). The central compiled pattern is a mechanism ladder. Plain Markdown/YAML artifacts come first. Skills, workflows, subagents, persistent agents, deterministic scripts/hooks, plugins, and MCP are added only when the previous mechanism cannot safely carry the work. This ladder is not an invention of this summary — it follows directly from Claude Code's own documented layering of guidance versus enforcement versus isolation versus distribution (B02-C014), combined with the Phase 2 compile plan's explicit reframing of this KB's purpose: to compile abstract, source-grounded orchestration knowledge, not to prematurely implement a named Apex agent system, the weekly routine, or any final runtime configuration (compile plan lines 15-17).

## What This Adds

```yaml
adds:
  - "A single named pattern (the mechanism ladder) that unifies the Phase 1 major-concepts list (claude-code-control-plane, soft-guidance-vs-hard-enforcement, skill-command-convergence, subagent-context-isolation, hook-enforcement-gate, plugin-bundled-orchestration, mcp-tool-connectivity-layer) into one ordering."
  - "An explicit non-goal boundary carried from the compile plan: this architecture is not a final named agent implementation, production runtime setup, weekly routine build, plugin implementation, MCP configuration, scheduler implementation, or hook/executable authoring (compile plan section 7)."
clarifies:
  - "'Minimal' means smallest mechanism sufficient for the task, not fewest total mechanisms ever used — the ladder still includes seven rungs, used selectively."
  - "The specialized indexes this pattern answers are agent_orchestration_index, claude_mechanism_mapping_index, and token_economy_and_information_design_index (compile plan lines 141-146, 158-163, 176-180)."
limits:
  - "No runtime configuration, hooks, plugins, workflows, MCP servers, or agent files are produced by this summary."
  - "The exact persistent agent roster, plugin packaging, and MCP allowlist remain deferred (see Uncertainty)."
```

## Adaptive Ranked Source Set

```yaml
adaptive_ranked_sources:
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    rationale: "Sets the corrected Phase 2 compile objective this summary follows, and defines the specialized indexes and cross-index master questions (notably M001_minimal_resilient_orchestration_architecture) that this page directly answers."
    coverage: "lines 13-49 corrected compile objective; lines 51-135 specialized indexes; lines 137-180 cross-index master questions and page-shape rule; lines 199-211 explicit non-goals."
  - source_id: "phase1-completion-report"
    rationale: "Aggregates the full set of major concepts found across all four Phase 1 batches, confirming the mechanism ladder's components are not invented for this summary but drawn from the completed ingest."
    coverage: "lines 104-136 major_concepts_found across skill_package_layer, claude_code_surface_layer, external_pattern_layer, apex_application_layer."
  - source_id: "phase1-batch02-claude-code-orchestration-surface"
    rationale: "Primary source for the layered-control-plane interpretation (B02-C014) that is the direct technical basis for the mechanism ladder's ordering."
    coverage: "B02-C001 through B02-C016; concepts_extracted claude-code-control-plane, soft-guidance-vs-hard-enforcement."
```

## Macro / Meso / Micro

### Macro

The minimal resilient architecture is not a specific set of files — it is a discipline for choosing mechanisms. Start every design question with the smallest mechanism (a plain artifact) and move up the ladder (skill, workflow, ephemeral subagent, persistent agent, deterministic script/hook, plugin/MCP) only when the current rung provably cannot carry the work safely, auditable, or token-efficiently. This discipline directly prevents the two failure modes Phase 2 was reframed to avoid: prematurely building a named agent system, and collapsing all orchestration behavior into one skill or one CLAUDE.md file (compile plan lines 15-17, 36-49).

### Meso

The ladder's rungs are drawn from Claude Code's own documented surface rather than invented: guidance files (CLAUDE.md, rules) versus enforced mechanisms (settings, permissions, hooks) versus isolation mechanisms (subagents) versus distribution mechanisms (plugins) versus external connectivity (MCP), all under one layered control-plane model (B02-C014). Each specialized index in the compile plan maps to a piece of this ladder: the `claude_mechanism_mapping_index` asks exactly when each rung applies (compile plan lines 110-123), the `agent_orchestration_index` asks when persistent agents are justified versus ephemeral subagents (lines 55-68), and the `token_economy_and_information_design_index` asks what should load every session versus only when triggered (lines 122-135) — which is the token-efficiency test each rung must pass before being adopted.

### Micro

Source pointers: compile plan lines 36-49 (corrected compile objective), lines 141-146 (M001_minimal_resilient_orchestration_architecture cross-index question), lines 199-211 (explicit non-goals); phase1-completion-report.md lines 104-136 (major concepts found); B02-C014 (layered control-plane interpretation).

## Key Claims

```yaml
key_claims:
  - claim_id: C001
    claim: "A resilient Claude/Apex orchestration system should be a small layered control plane, not a swarm: always-loaded guidance for stable norms, skills for repeatable procedures, workflows for multi-stage processes, subagents for context-isolated work, scripts/hooks for deterministic enforcement, and plugins or MCP only when distribution or external connectivity is justified."
    source_pointer: "compile plan lines 38-49; B02-C014"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages:
      - "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
  - claim_id: C002
    claim: "The KB should not compile toward a premature implementation of a named Apex agent system, the weekly routine, or any final runtime configuration; it should compile abstract, source-grounded orchestration knowledge so later implementation agents can answer practical design questions without rereading the raw corpus."
    source_pointer: "compile plan lines 15-17"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
  - claim_id: C003
    claim: "Major concepts found across Phase 1 span four layers: skill-package layer, Claude Code surface layer, external-pattern layer, and Apex-application layer, confirming the mechanism ladder draws on the full ingested corpus rather than one batch."
    source_pointer: "phase1-completion-report.md lines 104-136"
    confidence: "high"
    claim_label: "source_backed_summary"
    used_in_pages: []
```

## Routes Here

```yaml
routes:
  - question: "What is the smallest mechanism I should reach for first when designing a new Apex/Claude capability?"
    leads_to: "claude-code-orchestration-design/summaries/claude-mechanism-decision-model.md"
    rationale: "That page is the detailed, per-rung version of the same mechanism ladder this summary states at the architecture level."
  - related_page: "claude-code-orchestration-design/entities/claude-code-skills.md"
    relation: "Skills are the second rung of the ladder and the default answer for repeatable procedures once a plain artifact is insufficient."
```

## Uncertainty / Raw Source Reopen Triggers

```yaml
uncertainty_triggers:
  - id: U001
    description: "The exact persistent agent roster remains deferred; Phase 2 should not invent a final agent list without further operator confirmation."
    source_pointer: "compile plan lines 55-68 (agent_orchestration_index core questions)"
    proposed_handling: "planning_task_candidate"
  - id: U002
    description: "Plugin and MCP packaging remain deferred per operator decisions Q003 and Q005; this architecture summary treats them as outer, unused rungs rather than settled implementation targets."
    source_pointer: "operator-phase1-review-decisions-20260702.md lines 67-72 (Q003), lines 86-89 (Q005)"
    proposed_handling: "leave_as_gap"
  - id: U003
    description: "Explicit Phase 2 non-goals include final named agent implementation, production runtime setup, final weekly routine build, plugin implementation, MCP configuration, scheduler implementation, and writing hooks or executable runtime surfaces; any draft that crosses these lines should be flagged."
    source_pointer: "compile plan lines 199-211"
    proposed_handling: "ask_operator"
```
