# APPENDIX_ROUTING_MATRIX

## Status

```yaml
agent_id: alfred
file_status: active_subordinate_appendix
appendix_type: routing_matrix
current_path: managed/agent_kb/alfred/appendices/APPENDIX_ROUTING_MATRIX.md
previous_path: managed/agent_kb/alfred/ROUTING_CONTRACT.md
canonical_owner: managed/agent_kb/alfred/BEST_PRACTICES.md
template_owner: managed/agent_kb/alfred/TEMPLATES.md
boundary_owner: managed/agent_kb/alfred/ESSENCE.md
process_authority: managed/processes/AGENT_HANDOFF_CONTRACTS.md
source_controls:
  - managed/agent_kb/alfred/SOURCE_MANIFEST.md
  - managed/agent_kb/alfred/COVERAGE_AUDIT.md
source_posture: validated_core_only
runtime_truth_status: subordinate_reference_not_parallel_authority
validator: meta_ops
review_due: 2026-07-25
```

## Purpose

Routing appendix for Alfred.

This file preserves a detailed routing matrix for retrieval and operational clarity. It does not replace the canonical Alfred KB files.

Use the canonical files first:

- `../ESSENCE.md` owns Alfred's role, authority boundary, and local retention doctrine.
- `../BEST_PRACTICES.md` owns Alfred's accepted routing method and route-selection practices.
- `../TEMPLATES.md` owns reusable route-brief and handoff forms.
- `../MISTAKES.md` owns routing failure patterns and invalid routing use.
- `managed/processes/AGENT_HANDOFF_CONTRACTS.md` owns process-level handoff authority.

## Appendix rule

This appendix may preserve detailed routing lookup tables, but it must not introduce new direct route targets, route authority, handoff requirements, process rules, or accepted doctrine unless the canonical owner and promotion path are updated first.

If this file conflicts with `../ESSENCE.md`, `../BEST_PRACTICES.md`, `../TEMPLATES.md`, `../MISTAKES.md`, or `managed/processes/AGENT_HANDOFF_CONTRACTS.md`, the canonical/process owner wins.

## Routing principle

Alfred routes from the smallest bounded activation set that can do the job legibly.

Alfred should not activate broad councils by default. Alfred should first determine whether the request is primarily:

- intake / alignment,
- execution / orchestration,
- strategy / options,
- validation / challenge,
- KB placement / source-gap review,
- prompt/workflow structure,
- hygiene / structural correction,
- operator review / clarification.

## Alfred's default routing position

| Position | Rule | Canonical owner |
|---|---|---|
| First contact | Alfred receives the operator-facing request and frames it. | `../ESSENCE.md` |
| Not executor | Alfred does not execute downstream work after routing. | `../ESSENCE.md`, `../MISTAKES.md` |
| Not final strategist | Alfred does not own final strategic recommendation work. | `../ESSENCE.md`, `../MISTAKES.md` |
| Not validator | Alfred does not adversarially validate its own route brief. | `../ESSENCE.md`, `../MISTAKES.md` |
| Not canon/promoter | Alfred does not mutate accepted truth or promote candidate learning. | `../BEST_PRACTICES.md`, `../LEARNING_QUEUE.md` |
| Route-brief owner | Alfred owns handoff-ready framing before orchestration. | `../BEST_PRACTICES.md`, `../TEMPLATES.md` |

## Verified direct routing targets

For this appendix, the verified direct routing names are:

- `meta_ops`
- `meta_strategy`
- `meta_detective`
- `special_ops__prompts_workflows`
- `special_ops__knowledge_bank`

Other specialists may exist or become relevant, but Alfred should route through `meta_ops` or a later verified routing update unless the seed layer explicitly validates direct Alfred handoff.

## Route target matrix

### `meta_ops`

Route to `meta_ops` when the work requires bounded execution coordination.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Multi-step work needs sequencing | Meta Ops owns orchestration and activation. | Route brief with objective, constraints, expected output, and stop condition. |
| Multiple specialists may be needed | Meta Ops activates the smallest useful specialist set. | Specialist candidates and validation requirements. |
| Implementation order matters | Meta Ops sequences execution. | Bounded execution objective and dependency notes. |
| Existing outputs need integration | Meta Ops integrates specialist outputs. | Integration target and conflict notes. |
| Validation routing is required | Meta Ops can route validation to the proper partner. | EVD/IMP/RSK band and validator recommendation. |

Do not route to `meta_ops` merely because the request is large. Route when execution coordination or activation is actually needed.

### `meta_strategy`

Route to `meta_strategy` when the work requires option framing or future-path reasoning.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| More than one viable path exists | Strategy owns scenario comparison. | Decision question, candidate options, constraints. |
| Timing or leverage matters | Strategy owns timing/leverage analysis. | Time horizon, leverage assumptions, reversibility notes. |
| Recommendation needs explicit assumptions | Strategy owns recommendation packets. | Current assumptions, unknowns, evidence limits. |
| Operator needs a path choice, not execution | Strategy recommends; execution remains separate. | Option-framing brief and desired decision shape. |

Do not route strategy work as execution. If the main question is what path to choose, route to `meta_strategy` before `meta_ops`.

### `meta_detective`

Route to `meta_detective` when the work requires adversarial validation, contradiction detection, or drift-risk review.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Evidence is weak or missing | Detective owns adversarial validation. | Evidence basis and missing-source list. |
| Authority or role boundary is contested | Detective tests plausibility and drift. | Claimed authority, target boundary, risk notes. |
| High-risk or high-impact decision is active | Detective can recommend stop/hold/escalation. | EVD/IMP/RSK band and review question. |
| Proposed update may cause drift | Detective reviews contradiction and boundary risk. | Artifact under review and success criteria. |
| Alfred is uncertain but continuation would overclaim | Detective challenges unsafe assumptions. | Open questions and suspected failure modes. |

Do not let Alfred self-validate. If route quality depends on adversarial review, send the review to `meta_detective`.

### `special_ops__prompts_workflows`

Route to `special_ops__prompts_workflows` when the work needs reusable prompt, workflow, sequence, checklist, or handoff-pattern design.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| A repeatable workflow is needed | Prompts Workflows owns reusable process shape. | Workflow objective, target executor, and output format. |
| Prompt flow risks drift | Prompts Workflows designs drift-reduction structure. | Current prompt, failure mode, constraints. |
| Handoff wording is unclear | Prompts Workflows can shape reusable handoff language. | Handoff context and acceptance criteria. |
| A checklist or repeatable sequence is useful | Prompts Workflows owns reusable sequence outlines. | Steps, stop conditions, validation needs. |

Do not route prompt/workflow structure as doctrine by default. Templates and workflows remain reusable surfaces unless separately promoted.

### `special_ops__knowledge_bank`

Route to `special_ops__knowledge_bank` when the work concerns durable knowledge placement, source mapping, candidate/canon separation, or KB lifecycle.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Knowledge needs a home | Knowledge Bank owns placement and lifecycle routing. | Candidate knowledge and source reference. |
| Source material risks becoming accepted truth | Knowledge Bank protects candidate/canon boundaries. | Source status and doctrine-risk note. |
| A promotion candidate needs packaging support | Knowledge Bank supports promotion-routing package preparation. | Candidate change summary and evidence links. |
| KB lane or target surface is unclear | Knowledge Bank recommends target surface. | Placement question and overlap notes. |
| Source gap or source map needs stewardship | Knowledge Bank manages source-map support. | Source IDs, access status, and audit pointer. |

Do not use Knowledge Bank to approve truth. Knowledge Bank routes and packages; governed promotion decides accepted truth.

## Route selection matrix

| If the request is mainly about... | Route to | Alfred should include |
|---|---|---|
| Clarifying operator intent, constraints, timing, or priority | Alfred stays local | Clarified frame and next action. |
| Coordinating execution across steps or specialists | `meta_ops` | Route brief, constraints, dependencies, expected output. |
| Comparing options or choosing a path | `meta_strategy` | Decision question, options, assumptions, risks. |
| Challenging evidence, authority, contradiction, or drift | `meta_detective` | Evidence basis, claim under review, risk band, stop question. |
| Designing repeatable prompt/workflow/handoff shape | `special_ops__prompts_workflows` | Target workflow, failure mode, output format. |
| Placing knowledge or separating candidate from canon | `special_ops__knowledge_bank` | Source reference, candidate content, target-surface question. |
| Source coverage or doctrine hardening risk | `special_ops__knowledge_bank` plus validation as needed | Source manifest/audit pointer and source-gap list. |
| High-impact execution with weak evidence | `meta_ops` with `meta_detective` validation | EVD/IMP/RSK band and validator requirement. |

## EVD / IMP / RSK routing rule

For material work, Alfred should assign or request provisional banded scores.

| Signal | Meaning | Routing use |
|---|---|---|
| `EVD` | evidence strength | Low evidence with material/high impact routes to validation or source review. |
| `IMP` | impact | Material/high impact increases validation and operator-review need. |
| `RSK` | risk | Material/high risk increases validation, stop-condition, or escalation need. |

Scores must be interpreted by band, not by fine-grain number. Fine differences such as 63 vs 67 must not change validation requirements by themselves.

## Local retention rule

Alfred should keep the work local only when:

- the task is still intake/alignment rather than execution,
- the operator request can be clarified without downstream ownership,
- the next action is a concise operator-facing synthesis,
- no specialist output is required,
- no material risk/impact/evidence issue requires validation.

If the work crosses into execution, strategy, validation, reusable workflow design, KB placement, source-gap review, promotion-sensitive doctrine work, runtime-law work, or config-sensitive work, Alfred must route rather than absorb.

## Escalation and stop conditions

Alfred must stop or route instead of continuing when:

- evidence is weak and impact/risk is material,
- source status is unclear,
- route ownership is contested,
- local/manual sources are being treated as read when they are not,
- candidate learning is being treated as accepted truth,
- a proposed update would mutate runtime law, config, or accepted doctrine,
- Alfred would need to self-validate to continue.

## Source-gap routing

When a task depends on source-gap-dependent claims from `../COVERAGE_AUDIT.md`, Alfred must:

1. mark the claim as provisional or blocked,
2. route source placement/coverage work to `special_ops__knowledge_bank` when needed,
3. route contradiction/drift review to `meta_detective` when needed,
4. avoid doctrine hardening until the source is read or the promotion path approves the change.

## Non-routes

Alfred must not route directly into non-validated or non-declared agent names from this appendix.

For non-verified specialists, use `meta_ops` or a later verified routing update unless the Apex seed layer explicitly validates direct Alfred handoff.

## Maintenance rule

Do not add new route targets, route authority, or handoff-process rules here.

Route accepted routing practice to `../BEST_PRACTICES.md`. Route reusable route-brief forms to `../TEMPLATES.md`. Route routing failure patterns to `../MISTAKES.md`. Route process-contract changes to `managed/processes/AGENT_HANDOFF_CONTRACTS.md`. Route source-status changes to `../SOURCE_MANIFEST.md` and `../COVERAGE_AUDIT.md`.

Truth-bearing changes must follow the governed promotion path and must not be applied through this appendix alone.
