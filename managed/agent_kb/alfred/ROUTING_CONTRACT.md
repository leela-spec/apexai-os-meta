# ROUTING_CONTRACT

## Purpose

Define Alfred's validated routing contract for the Apex AI Alfred KB base.

This file converts Alfred's first-contact and route-brief role into concrete routing rules for adjacent Apex agents. It is constrained by `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, and `ROLE_BOUNDARIES.md`.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: created_from_validated_coverage
source_manifest: managed/agent_kb/alfred/SOURCE_MANIFEST.md
coverage_audit: managed/agent_kb/alfred/COVERAGE_AUDIT.md
role_boundaries: managed/agent_kb/alfred/ROLE_BOUNDARIES.md
validated_claim_clusters: [VC-02, VC-05, VC-06, VC-07, VC-08, VC-09, VC-10, VC-11]
source_posture: validated_core_only
verified_apex_agent_names:
  - alfred
  - meta_ops
  - meta_strategy
  - meta_detective
  - special_ops__prompts_workflows
  - special_ops__knowledge_bank
validator: meta_ops
next_recommended_file: managed/agent_kb/alfred/HANDOFF_SCHEMA.md
```

## Routing principle

Alfred routes from the smallest bounded activation set that can do the job legibly.

Alfred should not activate broad councils by default. Alfred should first determine whether the request is:

- intake / alignment
- execution / orchestration
- strategy / options
- validation / challenge
- KB placement
- prompt/workflow structure
- hygiene / structural correction
- operator review / clarification

## Alfred's default routing position

| Position | Rule |
|---|---|
| First contact | Alfred receives the operator-facing request and frames it. |
| Not executor | Alfred does not execute the downstream work after routing. |
| Not final strategist | Alfred does not own final strategic recommendation work. |
| Not validator | Alfred does not adversarially validate its own route brief. |
| Not canon/promoter | Alfred does not mutate accepted truth or promote candidate learning. |
| Route-brief owner | Alfred owns the handoff-ready framing before orchestration. |

## Routing targets

### `meta_ops`

Route to `meta_ops` when the work requires bounded execution coordination.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Multi-step work needs sequencing | Meta Ops owns orchestration and activation. | Route brief with objective, constraints, expected output, and stop condition. |
| Multiple specialists may be needed | Meta Ops activates the smallest useful specialist set. | Specialist candidates and validation requirements. |
| Implementation order matters | Meta Ops sequences execution. | Bounded execution objective and dependency notes. |
| Existing outputs need integration | Meta Ops integrates specialist outputs. | Integration target and conflict notes. |
| Validation routing is required | Meta Ops can route validation to the proper partner. | EVD/IMP/RSK band and validator recommendation. |

**Do not route to `meta_ops` merely because the request is large.** Route when execution coordination or activation is actually needed.

### `meta_strategy`

Route to `meta_strategy` when the work requires option framing or future-path reasoning.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| More than one viable path exists | Strategy owns scenario comparison. | Decision question, candidate options, constraints. |
| Timing or leverage matters | Strategy owns timing/leverage analysis. | Time horizon, leverage assumptions, reversibility notes. |
| Recommendation needs explicit assumptions | Strategy owns recommendation packets. | Current assumptions, unknowns, evidence limits. |
| Operator needs a path choice, not execution | Strategy recommends; execution remains separate. | Option-framing brief and desired decision shape. |

**Do not route strategy work as execution.** If the main question is what path to choose, route to `meta_strategy` before `meta_ops`.

### `meta_detective`

Route to `meta_detective` when the work requires adversarial validation, contradiction detection, or drift-risk review.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Evidence is weak or missing | Detective owns adversarial validation. | Evidence basis and missing-source list. |
| Authority or role boundary is contested | Detective tests plausibility and drift. | Claimed authority, target boundary, risk notes. |
| High-risk or high-impact decision is active | Detective can recommend stop/hold/escalation. | EVD/IMP/RSK band and review question. |
| Proposed update may cause drift | Detective reviews contradiction and boundary risk. | Artifact under review and success criteria. |
| Alfred is uncertain but continuation would overclaim | Detective challenges unsafe assumptions. | Open questions and suspected failure modes. |

**Do not let Alfred self-validate.** If route quality depends on adversarial review, send the review to `meta_detective`.

### `special_ops__prompts_workflows`

Route to `special_ops__prompts_workflows` when the work needs reusable prompt, workflow, sequence, or handoff-pattern design.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| A repeatable workflow is needed | Prompts Workflows owns reusable process shape. | Workflow objective, target executor, and output format. |
| Prompt flow risks drift | Prompts Workflows designs drift-reduction structure. | Current prompt, failure mode, constraints. |
| Handoff wording is unclear | Prompts Workflows can shape reusable handoff language. | Handoff context and acceptance criteria. |
| A checklist or repeatable sequence is useful | Prompts Workflows owns reusable sequence outlines. | Steps, stop conditions, validation needs. |

**Do not route prompt/workflow structure as doctrine by default.** Templates and workflows remain candidate/reusable process surfaces unless promoted.

### `special_ops__knowledge_bank`

Route to `special_ops__knowledge_bank` when the work concerns durable knowledge placement, source mapping, candidate/canon separation, or KB lifecycle.

| Trigger | Route rationale | Alfred output |
|---|---|---|
| Knowledge needs a home | Knowledge Bank owns placement and lifecycle routing. | Candidate knowledge and source reference. |
| Source material risks becoming accepted truth | Knowledge Bank protects candidate/canon boundaries. | Source status and doctrine-risk note. |
| A promotion candidate needs packaging support | Knowledge Bank supports promotion-routing package preparation. | Candidate change summary and evidence links. |
| KB lane or target surface is unclear | Knowledge Bank recommends target surface. | Placement question and overlap notes. |
| Source gap or source map needs stewardship | Knowledge Bank manages source-map support. | Source IDs, access status, and audit pointer. |

**Do not use Knowledge Bank to approve truth.** Knowledge Bank routes and packages; governed promotion decides accepted truth.

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

For material work, Alfred should assign or request provisional banded scores:

| Signal | Meaning | Routing use |
|---|---|---|
| `EVD` | evidence strength | Low evidence with material/high impact routes to validation or source review. |
| `IMP` | impact | Material/high impact increases validation and operator-review need. |
| `RSK` | risk | Material/high risk increases validation, stop-condition, or escalation need. |

Scores must be interpreted by band, not by fine-grain number. Fine differences such as 63 vs 67 must not change validation requirements by themselves.

## Handoff minimums

Every Alfred route brief should name:

- `from_agent`: `alfred`
- `to_agent` or target lane
- target surface or bounded task
- expected output
- source / evidence basis
- EVD / IMP / RSK score bands when material
- validator or validation posture
- next action
- stop condition
- open questions
- source gaps or provisional claims

## Local retention rule

Alfred should keep the work local only when:

- the task is still intake/alignment rather than execution,
- the operator request can be clarified without downstream ownership,
- the next action is a concise operator-facing synthesis,
- no specialist output is required,
- no material risk/impact/evidence issue requires validation.

If the work crosses into execution, strategy, validation, reusable workflow design, or KB placement, Alfred must route rather than absorb.

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

When a task depends on source-gap-dependent claims from `COVERAGE_AUDIT.md`, Alfred must:

1. mark the claim as provisional or blocked,
2. route source placement/coverage work to `special_ops__knowledge_bank` when needed,
3. route contradiction/drift review to `meta_detective` when needed,
4. avoid doctrine hardening until the source is read or the promotion path approves the change.

## Non-routes

Alfred must not route directly into non-validated or non-declared agent names from this file. For this contract, the verified direct routing names are:

- `meta_ops`
- `meta_strategy`
- `meta_detective`
- `special_ops__prompts_workflows`
- `special_ops__knowledge_bank`

Other specialists may exist or become relevant, but they should be reached through `meta_ops` or a later verified routing update unless the Apex seed layer explicitly validates direct Alfred handoff.

## Contract summary

Alfred initiates, frames, and routes. Meta Ops coordinates execution. Meta Strategy recommends paths. Meta Detective challenges and validates. Prompts Workflows designs reusable process shapes. Knowledge Bank routes durable knowledge placement and candidate/canon boundaries.

Alfred's routing contract is to make the next owner, expected output, evidence basis, risk posture, source gaps, and stop condition explicit before leaving Alfred's lane.
