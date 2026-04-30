# CROSS_REFERENCE_MANIFEST

## Purpose

This file records the durable cross-reference graph for the first-wave holding-orchestration infrastructure.

## Core references

| Source file | Points to | Why |
|---|---|---|
| `managed/rules/AGENTS.base.md` | `managed/agents/AGENT_INDEX.md` | compact startup pointer |
| `managed/agents/AGENT_INDEX.md` | all agent seed files | named-seed entrypoint |
| `managed/agents/AGENT_INDEX.md` | `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | routing and activation flow |
| `managed/agents/AGENT_INDEX.md` | `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | handoff schema |
| `managed/agents/AGENT_INDEX.md` | `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | overlap validation |
| `managed/agents/AGENT_INDEX.md` | `managed/agent_kb/AGENT_KB_INDEX.md` | KB-root index pointer |
| `managed/agent_kb/AGENT_KB_INDEX.md` | first-wave KB roots | durable KB-root map |
| `managed/agent_kb/AGENT_KB_INDEX.md` | `docs/LEARNING_SYSTEM.md` and `docs/PROCESS_BLUEPRINT_SYSTEM.md` | companion-doc benefit map for agents |
| `managed/knowledge/AGENT_KB_LANES.md` | `managed/agent_kb/AGENT_KB_INDEX.md` | lane-to-root boundary |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/knowledge/KB_STARTING_SOURCE_MAP.md` | source seeding |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | candidate logging |
| `managed/agents/special_ops__informatics_design.md` | `managed/knowledge/AGENT_KB_LANES.md` | lane boundaries |
| `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | all relevant seed agents | orchestration entry |
| `managed/processes/AGENT_HANDOFF_CONTRACTS.md` | seed agents and overlap matrix | durable handoff behavior |
| `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md` | KB source map, ledger template, handoff contracts | implementation workflow |
| `managed/knowledge/KB_STARTING_SOURCE_MAP.md` | first-wave KB roots | source-to-KB seeding route |
| `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | per-agent `LEARNING_QUEUE.md` files | candidate promotion packaging |
| `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | seed agents, KB roots, and handoff contracts | boundary validation |
| `docs/ROLE_SYSTEM.md` | `managed/agents/AGENT_INDEX.md` | companion-to-managed named map |
| `docs/PROJECT_ROUTING.md` | `managed/processes/HOLDING_ORCHESTRATION_FLOW.md` | scenario routing guide |
| `docs/LEARNING_SYSTEM.md` | `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | learning-to-candidate pointer |
| `docs/LEARNING_SYSTEM.md` | `managed/agent_kb/special_ops__knowledge_bank/`, `managed/agent_kb/special_ops__prompts_workflows/`, `managed/agent_kb/special_ops__hygiene_clean/` | agent benefit pointer for learning capture and production-result write-down |
| `docs/PROCESS_BLUEPRINT_SYSTEM.md` | `managed/rules/OPERATING_SPINE_CANON.md`, `managed/agent_kb/special_ops__prompts_workflows/`, `managed/agent_kb/meta_ops/` | companion process map for authority lookup and artifact-production sequencing |

## First-wave seed-to-KB references

| Seed file | KB root | Why |
|---|---|---|
| `managed/agents/alfred.md` | `managed/agent_kb/alfred/` | operator-facing intake boundary depth |
| `managed/agents/meta_ops.md` | `managed/agent_kb/meta_ops/` | orchestration boundary depth |
| `managed/agents/meta_strategy.md` | `managed/agent_kb/meta_strategy/` | options and recommendation boundary depth |
| `managed/agents/meta_detective.md` | `managed/agent_kb/meta_detective/` | adversarial-validation boundary depth |
| `managed/agents/special_ops__knowledge_bank.md` | `managed/agent_kb/special_ops__knowledge_bank/` | KB placement and lifecycle depth |
| `managed/agents/special_ops__informatics_design.md` | `managed/agent_kb/special_ops__informatics_design/` | structure and taxonomy depth |
| `managed/agents/special_ops__prompts_workflows.md` | `managed/agent_kb/special_ops__prompts_workflows/` | reusable prompt/workflow depth |
| `managed/agents/special_ops__ai_handling_routing.md` | `managed/agent_kb/special_ops__ai_handling_routing/` | advisory model/tool routing depth |
| `managed/agents/special_ops__hygiene_clean.md` | `managed/agent_kb/special_ops__hygiene_clean/` | structural QA and hygiene depth |

## KB scaffold references

Each first-wave KB root resolves to the same five-file scaffold:

- `ESSENCE.md`
- `BEST_PRACTICES.md`
- `MISTAKES.md`
- `TEMPLATES.md`
- `LEARNING_QUEUE.md`

`LEARNING_QUEUE.md` files are candidate-only and are not runtime truth.

## Boundary references

- All managed files in this manifest stay within `managed/`, `docs/`, `user/`, and `README-OpenClaw.md`.
- Companion docs may point to agents and managed surfaces, but they do not replace the managed authority surfaces they reference.
- No runtime cross-reference should target `NewFinals/`, `BaselinePatches/`, or `AdvancedUpdateProcess/` as authority.

## Maintenance rule

Whenever a new managed seed, lane file, or process file becomes durable, add it here before treating it as a normal routing dependency.
