# AGENT_INDEX

## Purpose

This file is the managed activation and routing entrypoint for the final v1 first-wave compact agent seed set.

It exists to make the named seed agents legible without turning companion prose or staging drafts into runtime authority.

## Read order

Read in this order when the task touches routing, overlap, activation, or multi-agent handoff:

1. `managed/rules/AGENTS.base.md`
2. `managed/rules/OPERATING_SPINE_CANON.md`
3. `managed/rules/AGENT_SWARM_INTERACTION_CANON.md`
4. `managed/rules/PROMOTION_PROTOCOL.md`
5. this file
6. `managed/agent_kb/AGENT_KB_INDEX.md`
7. `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`
8. `managed/processes/AGENT_HANDOFF_CONTRACTS.md`
9. `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`
10. `managed/knowledge/CROSS_REFERENCE_MANIFEST.md`

## Final v1 first-wave activation map

| Agent | Role summary | Seed path | KB root | Default validator |
|---|---|---|---|---|
| `alfred` | operator-facing intake, constraints, and route brief | `OpenClaw/07_finalopenclawsystem/managed/agents/alfred.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/alfred/` | `meta_ops` |
| `meta_ops` | orchestration, activation, sequence control, and handoff routing | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_ops.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_ops/` | `meta_detective` |
| `meta_strategy` | options, timing, leverage, and recommendation | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_strategy.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_strategy/` | `meta_detective` |
| `meta_detective` | adversarial validation, drift detection, plausibility pressure, and escalation pressure | `OpenClaw/07_finalopenclawsystem/managed/agents/meta_detective.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/meta_detective/` | `special_ops__hygiene_clean` |
| `special_ops__knowledge_bank` | KB placement, lifecycle, manifest, and source routing | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__knowledge_bank.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__knowledge_bank/` | `special_ops__informatics_design` |
| `special_ops__informatics_design` | structure, terminology, readability, and taxonomy | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__informatics_design.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__informatics_design/` | `special_ops__hygiene_clean` |
| `special_ops__prompts_workflows` | reusable prompt, workflow, and patchspec patterns | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__prompts_workflows.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__prompts_workflows/` | `meta_ops` |
| `special_ops__ai_handling_routing` | advisory model and tool routing posture | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__ai_handling_routing.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__ai_handling_routing/` | `meta_ops` |
| `special_ops__hygiene_clean` | QA findings, structural correctness, pointer integrity, and cleanup safety | `OpenClaw/07_finalopenclawsystem/managed/agents/special_ops__hygiene_clean.md` | `OpenClaw/07_finalopenclawsystem/managed/agent_kb/special_ops__hygiene_clean/` | `meta_detective` |

## Scaffold convention

Each first-wave KB root listed above uses the same lean five-file scaffold:

1. `ESSENCE.md`
2. `BEST_PRACTICES.md`
3. `MISTAKES.md`
4. `TEMPLATES.md`
5. `LEARNING_QUEUE.md`

Seed files remain compact activation specs.
Rich doctrine lives in `managed/agent_kb/` and shared governance lives in `managed/knowledge/`.
`LEARNING_QUEUE.md` is candidate-only and must not be treated as runtime truth.
`managed/agent_kb/AGENT_KB_INDEX.md` remains the KB-root index; this file remains the activation and routing index.

## Process and validation surfaces

- Handoff minimums live in `managed/processes/AGENT_HANDOFF_CONTRACTS.md`.
- Holding-layer orchestration flow lives in `managed/processes/HOLDING_ORCHESTRATION_FLOW.md`.
- Overlap and boundary checks live in `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md`.
- Durable cross-surface references live in `managed/knowledge/CROSS_REFERENCE_MANIFEST.md`.

## Default routing

- Start with `alfred` when the request begins from operator context, priorities, calendar, or ambiguity.
- Start with `meta_ops` when the task is already a concrete bounded execution or research problem.
- Add `meta_strategy` when the task has meaningful option space, timing tradeoffs, or scenario uncertainty.
- Add `meta_detective` when the task is T2+, evidence is weak, disagreement is high, or drift risk matters.
- Route through `special_ops__knowledge_bank` when durable source placement, lane routing, or candidate logging is needed.
- Route through `special_ops__informatics_design` when the output must be retrieval-safe, low-drift, or structurally clean.
- Route through `special_ops__prompts_workflows` when a reusable execution pattern or patchspec workflow is needed.
- Route through `special_ops__ai_handling_routing` when model/tool posture materially affects quality, cost, or safety.
- Route through `special_ops__hygiene_clean` when stale state, missing surfaces, broken pointers, or backlog hygiene appears.

## Hard overlap reminders

- Alfred must not absorb Meta Ops, Strategy, Detective, or runtime law.
- Meta Ops orchestrates; it does not own personal priorities, final strategy, or adversarial validation.
- Knowledge Bank owns placement and lifecycle; Informatics Design owns structure and readability.
- Hygiene audits structural correctness; Detective validates plausibility, authority, and drift.
- Prompts/Workflows owns reusable execution patterns; AI Handling/Routing owns advisory routing posture and is not config authority.
- Strategy proposes and escalates; it does not commandeer execution.

## Domain-axis note

Domain masters are not part of this seed set.
The domain-master pattern is source-gated and remains companion or future-seed work until there is explicit domain evidence and repeated bounded need.

## Boundary note

This file is a managed activation and routing index surface.
It does not override the constitutional rules in `managed/rules/`.
It does not replace `managed/agent_kb/AGENT_KB_INDEX.md` as the KB-root index.
