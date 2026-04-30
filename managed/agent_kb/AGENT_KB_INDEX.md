# AGENT_KB_INDEX

## Purpose

This file maps every first-wave agent to its KB root inside `managed/agent_kb/`.

## Scaffold convention

Each KB root derives the same five-file scaffold:

- `ESSENCE.md`
- `BEST_PRACTICES.md`
- `MISTAKES.md`
- `TEMPLATES.md`
- `LEARNING_QUEUE.md`

`LEARNING_QUEUE.md` is candidate-only and is never runtime truth.

## Agent KB root map

| Agent ID | KB root | Essence role | Default owner | Default validator | Notes |
|---|---|---|---|---|---|
| `alfred` | `managed/agent_kb/alfred/` | operator-facing intake and alignment boundary | `alfred` | `meta_ops` | compact seed remains in `managed/agents/alfred.md` |
| `meta_ops` | `managed/agent_kb/meta_ops/` | orchestration and activation boundary | `meta_ops` | `meta_detective` | seed stays compact |
| `meta_strategy` | `managed/agent_kb/meta_strategy/` | options and recommendation boundary | `meta_strategy` | `meta_detective` | seed stays compact |
| `meta_detective` | `managed/agent_kb/meta_detective/` | adversarial-validation boundary | `meta_detective` | `special_ops__hygiene_clean` | not an executor |
| `special_ops__knowledge_bank` | `managed/agent_kb/special_ops__knowledge_bank/` | KB placement and lifecycle boundary | `special_ops__knowledge_bank` | `special_ops__informatics_design` | shared governance remains in `managed/knowledge/` |
| `special_ops__informatics_design` | `managed/agent_kb/special_ops__informatics_design/` | structure, taxonomy, and retrieval boundary | `special_ops__informatics_design` | `special_ops__hygiene_clean` | not truth authority |
| `special_ops__prompts_workflows` | `managed/agent_kb/special_ops__prompts_workflows/` | reusable prompt/workflow boundary | `special_ops__prompts_workflows` | `meta_ops` | not orchestration authority |
| `special_ops__ai_handling_routing` | `managed/agent_kb/special_ops__ai_handling_routing/` | advisory model/tool routing boundary | `special_ops__ai_handling_routing` | `meta_ops` | not config authority |
| `special_ops__hygiene_clean` | `managed/agent_kb/special_ops__hygiene_clean/` | structural QA and hygiene boundary | `special_ops__hygiene_clean` | `meta_detective` | not promotion authority |

## Companion doc benefit index

The following docs are companion maps that benefit multiple agents. They may inform bounded work, but they do not replace each agent's KB root, compact seed, shared governance files, or promotion authority.

| Companion doc | Primary beneficiary agents | Use when | Boundary |
|---|---|---|---|
| `docs/LEARNING_SYSTEM.md` | `special_ops__knowledge_bank`, `special_ops__prompts_workflows`, `special_ops__hygiene_clean`, `meta_ops`, `meta_detective` | learning capture, candidate routing, production-result write-down, and distinguishing accepted truth from candidate lessons | companion explainer; promotion still routes through `managed/rules/PROMOTION_PROTOCOL.md` and managed KB governance |
| `docs/PROCESS_BLUEPRINT_SYSTEM.md` | `meta_ops`, `special_ops__prompts_workflows`, `special_ops__knowledge_bank`, `special_ops__hygiene_clean`, `alfred` | process-map lookup, artifact-production sequencing, and routing operators to the correct managed authority surface | companion map; runtime law remains in managed canons, managed rituals, and managed processes |
| `docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline.md` | `special_ops__ai_handling_routing`, `special_ops__prompts_workflows`, `meta_ops`, `alfred`, `meta_detective`, `special_ops__hygiene_clean` | choosing between Agent Mode, extended thinking, Deep Research, and Codex/repo execution by bottleneck | companion baseline; accepted routing entries live in the AI Handling Routing KB and hygiene consequences live in `managed/rules/QA_HYGIENE_PROTOCOL.md` |
| `docs/Agent_Mode_vs_Thinking_Mode_Routing_Baseline_Context.md` | `special_ops__ai_handling_routing`, `special_ops__prompts_workflows`, `meta_ops`, `meta_detective`, `special_ops__hygiene_clean` | diagnosing mode-mismatch substitution and reconciling Agent Mode playbooks with exact-artifact workflows | companion rationale; mistake patterns and countermeasures live in `managed/agent_kb/special_ops__ai_handling_routing/MISTAKES.md` |

## Boundary note

This index maps KB roots only. It does not replace compact activation seeds, shared governance surfaces, or the promotion protocol.
