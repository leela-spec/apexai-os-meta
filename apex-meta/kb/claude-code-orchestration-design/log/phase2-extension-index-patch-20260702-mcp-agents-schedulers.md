---
title: "Phase 2 Extension Index Patch — MCP, Production Agents, Schedulers"
page_type: patch_instruction
kb_slug: "claude-code-orchestration-design"
source_refs:
  - source_id: "wiki/index"
    source_path: "apex-meta/kb/claude-code-orchestration-design/wiki/index.md"
    source_hash: "21ad52d5505cb117dc06470181c348b8a06a86bd"
    source_pointer: "current S6 index before extension package"
    source_storage_mode: "pointer_only"
  - source_id: "phase2-specialized-index-compile-plan-20260702"
    source_path: "apex-meta/kb/claude-code-orchestration-design/log/phase2-specialized-index-compile-plan-20260702.md"
    source_hash: "e9bce42761eeefce9db70e47e11171fa61550805"
    source_pointer: "specialized index compile target"
    source_storage_mode: "pointer_only"
created_at: "2026-07-02T14:30:00Z"
updated_at: "2026-07-02T14:30:00Z"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Phase 2 Extension Index Patch — MCP, Production Agents, Schedulers

```yaml
patch_type: "search_replace_add"
target_file: "apex-meta/kb/claude-code-orchestration-design/wiki/index.md"
overwrite_target: false
extension_intent: "Additive index registration only; do not delete existing entries."
new_pages_created:
  summaries:
    - "summaries/mcp-configuration-and-trust-boundary"
    - "summaries/production-agent-readiness-and-roster-boundary"
    - "summaries/scheduler-boundary-and-deferment"
  concepts:
    - "concepts/mcp-config-boundary"
    - "concepts/mcp-decision-model"
    - "concepts/mcp-allowlist-and-injection-risk"
    - "concepts/production-agent-roster-candidate-boundary"
    - "concepts/production-agent-readiness-gate"
    - "concepts/scheduler-boundary"
    - "concepts/scheduler-deferment-rule"
  entities:
    - "entities/scheduler"
```

## Patch 1 — Counts

```yaml
find:
  compiled_page_count: 62
  summaries: 6
  concepts: 45
  entities: 11
replace_with:
  compiled_page_count: 73
  summaries: 9
  concepts: 52
  entities: 12
```

## Patch 2 — Add summary links

```yaml
find: |
  - [[summaries/weekly-routine-as-orchestration-case-study|Weekly Routine as Orchestration Case Study]]
add_after: |
  - [[summaries/mcp-configuration-and-trust-boundary|MCP Configuration and Trust Boundary]]
  - [[summaries/production-agent-readiness-and-roster-boundary|Production Agent Readiness and Roster Boundary]]
  - [[summaries/scheduler-boundary-and-deferment|Scheduler Boundary and Deferment]]
```

## Patch 3 — Add concepts under claude mechanism mapping

```yaml
find: |
  claude_mechanism_mapping_index:
    - mechanism-ladder
    - skill-boundary
    - workflow-boundary
    - ephemeral-subagent-boundary
    - persistent-agent-boundary
    - deterministic-script-boundary
    - hook-vs-skill-instruction
    - plugin-deferment-rule
replace_with: |
  claude_mechanism_mapping_index:
    - mechanism-ladder
    - skill-boundary
    - workflow-boundary
    - ephemeral-subagent-boundary
    - persistent-agent-boundary
    - deterministic-script-boundary
    - hook-vs-skill-instruction
    - plugin-deferment-rule
    - mcp-config-boundary
    - mcp-decision-model
    - mcp-allowlist-and-injection-risk
    - scheduler-boundary
    - scheduler-deferment-rule
```

## Patch 4 — Add production-agent concepts under agent orchestration

```yaml
find: |
  agent_orchestration_index:
    - persistent-agent-vs-ephemeral-subagent
    - agent-specific-knowledge-base
    - compact-activation-seed
    - role-boundary-and-non-ownership
    - productive-agent-redundancy
    - validator-as-non-executor
    - agent-learning-queue-candidate-only
replace_with: |
  agent_orchestration_index:
    - persistent-agent-vs-ephemeral-subagent
    - agent-specific-knowledge-base
    - compact-activation-seed
    - role-boundary-and-non-ownership
    - productive-agent-redundancy
    - validator-as-non-executor
    - agent-learning-queue-candidate-only
    - production-agent-roster-candidate-boundary
    - production-agent-readiness-gate
```

## Patch 5 — Add scheduler entity

```yaml
find: |
  - [[entities/swe-agent|SWE-agent]]
add_after: |
  - [[entities/scheduler|Scheduler]]
```

## Patch 6 — Update LLM summary addendum

```yaml
find: |
  The compiled doctrine is intentionally non-runtime: it defines patterns, boundaries, reads/writes, token-efficiency rules, drift controls, and unresolved questions without creating hooks, skills, workflows, plugins, MCP config, schedulers, production agents, raw-source edits, manifest edits, or deterministic indexes.
add_after: |
  
  Extension package `phase2-extension-index-patch-20260702-mcp-agents-schedulers` adds explicit MCP configuration/trust, production-agent readiness, and scheduler boundary coverage without modifying runtime configuration or accepted production rosters.
```
