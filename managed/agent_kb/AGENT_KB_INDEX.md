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

## Boundary note

This index maps KB roots only. It does not replace compact activation seeds, shared governance surfaces, or the promotion protocol.
