# AGENT_KB_LANES

## Purpose

This file defines how OpenClaw knowledge-bank lanes are placed, loaded, validated, and kept separate from source material, promotion packets, runtime config, and compact agent activation seeds.

It is the durable managed knowledge policy for connecting:

- compact agent seeds in `OpenClaw/07_finalopenclawsystem/managed/agents/`
- per-agent KB roots in `OpenClaw/07_finalopenclawsystem/managed/agent_kb/<agent_id>/`
- shared governance surfaces in `OpenClaw/07_finalopenclawsystem/managed/knowledge/`
- process contracts in `OpenClaw/07_finalopenclawsystem/managed/processes/`

## Scope

This file governs KB lane placement and lane responsibility.

It is in scope for:

- deciding where agent-specific doctrine belongs
- deciding where shared KB governance belongs
- distinguishing accepted KB content from candidate learning
- routing knowledge items to owner and validator lanes
- preventing source material from becoming canon by storage alone
- preserving compact activation seeds instead of overloading seed files

It is out of scope for:

- full source provenance mapping; use `KB_STARTING_SOURCE_MAP.md`
- full promotion candidate schema; use `KB_PROMOTION_LEDGER_TEMPLATE.md`
- long agent doctrine; use the relevant per-agent KB root
- full process or handoff schemas; use `managed/processes/`
- runtime configuration changes; do not route config doctrine into this file

## Lane Model

OpenClaw uses three complementary knowledge lane classes.

| Lane class | Primary location | Main job | Runtime truth status |
|---|---|---|---|
| Compact activation seed | `managed/agents/<agent_id>.md` | activate the agent, state role boundary, point to KB root | runtime activation surface, intentionally compact |
| Per-agent KB root | `managed/agent_kb/<agent_id>/` | store accepted rich doctrine, accepted practices, accepted mistakes, accepted templates, and candidate queue | accepted files are usable on demand; queue is not truth |
| Shared governance surface | `managed/knowledge/` | govern KB placement, source routing, promotion templates, manifests, and overlap validation | managed governance surface |
| Process contract surface | `managed/processes/` | define handoff, orchestration, and workflow contracts | process authority, not KB doctrine |

## Per-Agent KB Root Policy

Each first-wave agent has exactly one KB root under `managed/agent_kb/`.

Each KB root uses the same five-file scaffold:

```text
ESSENCE.md
BEST_PRACTICES.md
MISTAKES.md
TEMPLATES.md
LEARNING_QUEUE.md
```

### File roles

| File | Role | Accepted-truth status | Update boundary |
|---|---|---|---|
| `ESSENCE.md` | accepted role boundary, core doctrine, durable operating essence | accepted KB truth after promotion | promotion-gated |
| `BEST_PRACTICES.md` | accepted reusable practices | accepted KB truth after promotion | promotion-gated |
| `MISTAKES.md` | accepted recurring mistake patterns and anti-patterns | accepted KB truth after promotion | promotion-gated |
| `TEMPLATES.md` | accepted reusable local templates | accepted KB truth after promotion | promotion-gated |
| `LEARNING_QUEUE.md` | candidate capture only | not runtime truth | validate before promotion |

### First-wave KB roots

| Agent ID | KB root | Default owner | Default validator | Primary KB boundary |
|---|---|---|---|---|
| `alfred` | `managed/agent_kb/alfred/` | `alfred` | `meta_ops` | operator-facing intake, alignment, and sequencing support |
| `meta_ops` | `managed/agent_kb/meta_ops/` | `meta_ops` | `meta_detective` | orchestration, activation, state, and coordination doctrine |
| `meta_strategy` | `managed/agent_kb/meta_strategy/` | `meta_strategy` | `meta_detective` | option framing, strategic recommendation, leverage logic |
| `meta_detective` | `managed/agent_kb/meta_detective/` | `meta_detective` | `special_ops__hygiene_clean` | adversarial review, contradiction checks, drift detection |
| `special_ops__knowledge_bank` | `managed/agent_kb/special_ops__knowledge_bank/` | `special_ops__knowledge_bank` | `special_ops__informatics_design` | KB lifecycle, placement, candidate routing, promotion readiness |
| `special_ops__informatics_design` | `managed/agent_kb/special_ops__informatics_design/` | `special_ops__informatics_design` | `special_ops__hygiene_clean` | structure, naming, taxonomy, retrieval shape |
| `special_ops__prompts_workflows` | `managed/agent_kb/special_ops__prompts_workflows/` | `special_ops__prompts_workflows` | `meta_ops` | reusable prompt and workflow patterns |
| `special_ops__ai_handling_routing` | `managed/agent_kb/special_ops__ai_handling_routing/` | `special_ops__ai_handling_routing` | `meta_ops` | advisory model, tool, and path-routing doctrine |
| `special_ops__hygiene_clean` | `managed/agent_kb/special_ops__hygiene_clean/` | `special_ops__hygiene_clean` | `meta_detective` | structural QA, cleanup, traceability, stale-surface detection |

No additional first-wave agent KB roots are defined by this file.

## Shared Governance Surface Policy

Shared KB governance belongs in `managed/knowledge/` when the rule or artifact applies across multiple agents, KB roots, or governance lanes.

| Shared file | Role | Not for |
|---|---|---|
| `AGENT_KB_LANES.md` | KB lane placement, owner/validator expectations, runtime-loading boundary | source maps, ledger schemas, agent doctrine |
| `KB_STARTING_SOURCE_MAP.md` | source classes, authority order, evidence-only source boundaries, source-to-target routing | promotion decisions or accepted doctrine by itself |
| `KB_PROMOTION_LEDGER_TEMPLATE.md` | candidate packet template for proposed KB promotions | automatic promotion or runtime truth mutation |
| `CROSS_REFERENCE_MANIFEST.md` | durable cross-surface reference map | replacing source maps or accepted KB files |
| `OVERLAP_VALIDATION_MATRIX.md` | overlap-risk checks between agents and governance surfaces | long handoff schema or process execution law |

Shared governance files may point into per-agent KB roots, but they must not absorb full per-agent doctrine.

## File Placement Rules

Use the narrowest stable target that owns the knowledge item.

| Knowledge item type | Correct target | Rule |
|---|---|---|
| Agent activation role, minimal boundary, KB pointer | `managed/agents/<agent_id>.md` | keep compact; do not store rich doctrine here |
| Agent-specific accepted essence | `managed/agent_kb/<agent_id>/ESSENCE.md` | promote only after validation |
| Agent-specific accepted practice | `managed/agent_kb/<agent_id>/BEST_PRACTICES.md` | one accepted practice per durable entry pattern |
| Agent-specific accepted mistake or anti-pattern | `managed/agent_kb/<agent_id>/MISTAKES.md` | record prevention value and validator basis |
| Agent-specific accepted reusable template | `managed/agent_kb/<agent_id>/TEMPLATES.md` | keep reusable; avoid source dumps |
| Agent-specific unvalidated learning | `managed/agent_kb/<agent_id>/LEARNING_QUEUE.md` | candidate-only; never runtime truth |
| Cross-agent KB placement rule | `managed/knowledge/AGENT_KB_LANES.md` | keep policy-level, not case ledger |
| Source classification or initial evidence routing | `managed/knowledge/KB_STARTING_SOURCE_MAP.md` | source material remains evidence, not canon |
| Promotion candidate packaging | `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md` | packet template only; not approval itself |
| Cross-surface reference graph | `managed/knowledge/CROSS_REFERENCE_MANIFEST.md` | keep references durable and bounded |
| Overlap or boundary validation | `managed/knowledge/OVERLAP_VALIDATION_MATRIX.md` | validate role-boundary conflicts |
| Handoff, workflow, or orchestration contract | `managed/processes/` | process contract, not KB doctrine |
| Runtime config behavior | `managed/config/openclaw.json` | operator-reviewed config only; not this lane file |

## Runtime Loading Boundary

OpenClaw should not preload every KB file by default.

Runtime loading follows these boundaries:

- compact seeds in `managed/agents/` may be read for activation and routing
- per-agent `ESSENCE.md` may be read when that agent is activated or its boundary materially matters
- `BEST_PRACTICES.md`, `MISTAKES.md`, and `TEMPLATES.md` are read on demand for the bounded task
- shared `managed/knowledge/` files are read when placement, provenance, promotion, manifest, or overlap questions are active
- `managed/processes/` files are read when workflow, handoff, or orchestration contract questions are active
- `LEARNING_QUEUE.md` is never read as accepted runtime truth

A candidate may inform a review question, but it may not silently drive execution as if it were accepted doctrine.

## Candidate-Only Learning Queue Rule

`LEARNING_QUEUE.md` files are capture queues, not truth surfaces.

A queue entry may record:

- observed issue or improvement candidate
- source or evidence reference
- proposed target file
- owner and validator
- initial `EVD`, `IMP`, and `RSK` scores on the 1-5 scale
- review need or due path

A queue entry may not:

- override an accepted KB file
- modify compact seed behavior
- change runtime config
- bypass validation
- self-promote because it was written by the owning agent
- become canon by repetition, storage, or convenience

Promotion requires a separate validation and decision path through the governed promotion process.

## Owner And Validator Expectations

Each KB lane has an owner and a validator.

- **Owner:** maintains lane coherence, drafts candidate entries, routes evidence, and proposes target placement.
- **Validator:** checks boundary fit, overlap risk, evidence strength, impact, and promotion safety.
- **No self-promotion:** an owner may propose a KB change but may not be the sole validator for its own accepted-truth promotion.
- **Escalation:** unresolved authority, overlap, or evidence conflicts route to the appropriate governance, hygiene, or escalation surface instead of being silently averaged.

Minimum validation questions:

1. Does the item belong in a compact seed, per-agent KB root, shared governance file, process contract, or source map?
2. Is the item accepted truth, a candidate, evidence, a template, or process contract content?
3. Is the proposed target the narrowest stable target?
4. Is a separate validator named?
5. Are source, candidate, and canon status visibly separated?
6. Would promotion create overlap or authority leakage with another agent or surface?

## Anti-Drift Safeguards

- Do not expand compact seeds into doctrine repositories.
- Do not use `managed/knowledge/` as a dumping ground for long agent-specific doctrine.
- Do not treat source material, staging output, research notes, or session traces as canon by default.
- Do not treat `LEARNING_QUEUE.md` as accepted truth.
- Do not promote an owner-authored candidate without separate validation.
- Do not store process contracts inside per-agent KB files when `managed/processes/` is the correct host.
- Do not store runtime configuration doctrine in KB governance files.
- Do not add domain-master KB roots under the first-wave scaffold unless a later governed decision creates them.
- Do not duplicate full promotion schemas here; use the ledger template.
- Do not duplicate full source maps here; use the starting source map.

## Acceptance Criteria

This file is valid when:

- compact seeds are clearly assigned to `managed/agents/`
- per-agent rich doctrine is clearly assigned to `managed/agent_kb/<agent_id>/`
- shared KB governance is clearly assigned to `managed/knowledge/`
- process contracts are clearly assigned to `managed/processes/`
- every first-wave agent has exactly one KB root listed
- every KB root uses the five-file scaffold
- `LEARNING_QUEUE.md` is explicitly candidate-only and not runtime truth
- source material is explicitly evidence, not canon
- self-promotion is explicitly forbidden
- owner and validator expectations are explicit
- runtime loading is bounded and on demand
- no full source map, promotion ledger schema, long agent doctrine, handoff schema, or config doctrine is embedded here
