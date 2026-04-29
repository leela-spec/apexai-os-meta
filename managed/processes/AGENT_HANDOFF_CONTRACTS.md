# AGENT_HANDOFF_CONTRACTS

## Purpose

This file defines the durable minimum handoff contract between first-wave OpenClaw agents.

It exists to keep agent-to-agent work bounded, reviewable, state-aware, and resistant to drift. A handoff is valid only when the receiver can understand the objective, current state, authority basis, risks, expected output, validator requirement, and next action without reconstructing hidden reasoning from transient chat.

This process file replaces stale scalar threshold and current-state semantics with final structured handoff semantics using:

- `EVD`, `IMP`, and `RSK` on a 1-100 scale
- explicit current-state and finality-state language
- explicit owner, validator, lifecycle, stop, and escalation rules
- first-wave agent boundaries only

## Scope

This file governs handoffs among the first-wave agents:

| Agent | Handoff role in this file |
|---|---|
| `alfred` | operator-facing intake, alignment, and route-brief lane |
| `meta_ops` | bounded orchestration, activation, sequencing, and output integration lane |
| `meta_strategy` | option framing, timing logic, leverage analysis, and recommendation packet lane |
| `meta_detective` | adversarial validation, contradiction detection, and drift-risk challenge lane |
| `special_ops__knowledge_bank` | KB placement, lifecycle routing, source mapping, and candidate/canon separation lane |
| `special_ops__informatics_design` | structure, taxonomy, decomposition, naming, and retrieval-safe packaging lane |
| `special_ops__prompts_workflows` | reusable prompt, workflow, and handoff-pattern support lane |
| `special_ops__ai_handling_routing` | advisory model/tool/routing posture lane |
| `special_ops__hygiene_clean` | structural QA, pointer integrity, stale-state detection, and hygiene routing lane |

This file applies when work moves between agents, roles, states, or control surfaces. It is especially important when the handoff affects governed files, truth boundaries, KB placement, process contracts, validation, risk, or operator approval.

## Non-goals

This file does not define:

- full per-agent doctrine
- complete agent activation seeds
- per-agent KB module contents
- promotion ledger entries
- learning queue entries
- source dumps
- full prompt templates
- runtime config schema
- `openclaw.json` changes
- source or staging patches
- new agents
- domain-master agents

This file does not turn handoff into implementation authority. Handoff can authorize bounded work only inside the receiving agent's role boundary, state boundary, and governing surface constraints.

## Handoff principles

### 1. Bounded transfer

Every handoff must transfer a bounded task, not an open-ended responsibility cloud. The receiving agent must be able to tell:

- what is being asked
- why it is being asked
- what input is authoritative
- what output is expected
- what must not be changed
- when to stop

### 2. Authority visibility

Every handoff must name its authority basis. Authority may come from accepted managed law, accepted KB doctrine, operator instruction, a validated packet, or bounded evidence. Authority may not be inferred from convenience, urgency, repetition, or agent confidence.

### 3. Candidate is not accepted truth

A handoff may pass candidate material, draft material, learning queue material, research findings, or source evidence. None of these become accepted truth by being handed off.

### 4. Validation is proportional to impact and risk

Higher `IMP` increases the need for explicit validation. Higher `RSK` increases the need for adversarial review, hygiene review, or operator review. Weak `EVD` must be surfaced rather than hidden.

### 5. Separation of build and validation

An agent that builds, drafts, or recommends a high-impact output must not be the sole validator of that same output. Meta Ops may integrate outputs, but it must not self-validate high-impact changes.

### 6. Rejection is valid

A receiving agent must reject a handoff when the task is outside its lane, lacks minimum context, conflicts with role boundaries, requires forbidden authority, or would force unsafe implementation.

### 7. Stop conditions outrank momentum

When a handoff exposes authority ambiguity, missing evidence, blocked state, config mutation, source/staging mutation, learning-queue-as-truth leakage, or role-boundary drift, the correct outcome is hold, reject, or escalate.

## Standard handoff packet schema

Use this schema for material handoffs. Markdown tables or prose may wrap the schema for readability, but the concepts must remain present.

```yaml
handoff_packet:
  id: string
  from_agent: first_wave_agent_id
  to_agent: first_wave_agent_id
  handoff_type: route_brief | execution_request | strategy_request | validation_request | hygiene_request | kb_routing_request | structure_request | prompt_workflow_request | ai_routing_advice | verdict_return | escalation_return
  objective: string
  current_state: draft | candidate | needs_validation | validated | accepted | rejected | archived | blocked | operator_review_required
  target_state: draft | candidate | needs_validation | validated | accepted | rejected | archived | blocked | operator_review_required
  context_summary: string
  inputs:
    - path_or_ref: string
      role: accepted_truth | process_contract | seed | kb_doctrine | candidate | source_evidence | trace | operator_instruction | config_reference
      status: accepted | candidate | evidence_only | review_required | blocked
  expected_outputs:
    - output_name: string
      output_shape: string
      acceptance_criteria: string
  constraints:
    - string
  authority_basis:
    - accepted_surface_or_instruction: string
      authority_type: managed_law | accepted_kb | operator_instruction | validated_packet | evidence_only
  unresolved_questions:
    - question: string
      blocking: true | false
  risks:
    - risk: string
      mitigation_or_validator: string
  threshold:
    EVD: 1-100
    IMP: 1-100
    RSK: 1-100
  validation_required: true | false
  validator: first_wave_agent_id | operator | none
  next_action: accept | reject | validate | revise | execute_bounded | escalate | request_operator_review | archive
  stop_conditions:
    - string
```

### Required packet minimums

A handoff packet is invalid if it omits:

- `id`
- `from_agent`
- `to_agent`
- `objective`
- `current_state`
- `target_state`
- `inputs`
- `expected_outputs`
- `constraints`
- `authority_basis`
- `threshold.EVD`
- `threshold.IMP`
- `threshold.RSK`
- `validation_required`
- `validator`
- `next_action`
- `stop_conditions`

## Threshold and risk band semantics

### Scale

All material handoffs use `EVD`, `IMP`, and `RSK` on a 1-100 scale.

| Score range | Meaning |
|---:|---|
| 1-20 | low |
| 21-40 | limited |
| 41-60 | material |
| 61-80 | strong/high |
| 81-100 | decisive/highest |

### Dimensions

| Dimension | Meaning | Handoff consequence |
|---|---|---|
| `EVD` | strength and traceability of evidence | weak evidence must be surfaced; low `EVD` cannot be hidden behind confident prose |
| `IMP` | downstream impact if the handoff is accepted or implemented | higher impact increases validation and operator-review need |
| `RSK` | drift, authority, safety, reversibility, or structural risk | higher risk increases adversarial, hygiene, or operator-review need |

### Validation bands

| Band | Typical condition | Required posture |
|---|---|---|
| low-control | `IMP` and `RSK` both 1-40 | receiver may proceed if authority is clear and evidence is adequate |
| material-control | `IMP` 41-60 or `RSK` 41-60 | receiver must preserve explicit acceptance criteria and record unresolved questions |
| high-control | `IMP` 61-100 or `RSK` 61-100 | validator involvement is required before implementation or accepted-truth mutation |
| weak-evidence-control | `EVD` 1-40 with material or higher impact/risk | stop, narrow scope, request evidence, or route validation before execution |

### Threshold rules

- Higher `IMP` increases the need for explicit validation.
- Higher `RSK` increases the need for adversarial review, hygiene review, operator review, or escalation.
- Weak `EVD` must be surfaced as a blocker, caveat, or explicit validation need.
- High-risk handoffs require validator involvement before implementation.
- A handoff with `RSK` 81-100 must name a validator or operator review path.
- A handoff with `IMP` 81-100 must not be implemented solely by the originating agent.
- A handoff with `EVD` 1-20 and `IMP` 41 or higher must not proceed as if evidence were sufficient.

## Current-state and finality-state semantics

The `current_state` and `target_state` fields describe the finality and review status of the transferred object. They do not grant implementation permission by themselves.

| State | Meaning | Handoff rule |
|---|---|---|
| `draft` | working content not yet packaged as a candidate | may be revised; must not be treated as truth |
| `candidate` | packaged for review or possible promotion | not accepted truth; requires validation or promotion route |
| `needs_validation` | known to require review before use | receiver must validate, route, or reject |
| `validated` | checked for the bounded purpose | may proceed only within the validation scope |
| `accepted` | approved as durable truth or durable process content through the correct path | may be referenced as accepted within its scope |
| `rejected` | reviewed and found invalid for the target purpose | preserve trace; do not silently reuse |
| `archived` | preserved for history but not active authority | may be cited as history only |
| `blocked` | cannot safely proceed because a prerequisite, authority, evidence, or approval condition is missing | must not be silently implemented |
| `operator_review_required` | human/operator approval is required before apply, promotion, or config-affecting action | stop before implementation until approval exists |

### State rules

- `candidate` is not accepted truth.
- Learning queue material is not runtime truth.
- Evidence-only source material is not runtime truth.
- Blocked work must not be silently implemented.
- Operator-review-required work needs explicit approval before apply.
- Rejected and archived states should preserve trace rather than disappear silently.
- A state transition must be explicit enough that a later reader can reconstruct what changed and why.

## Owner and validator rules

### Owner rules

The source agent owns the clarity of the handoff packet. The target agent owns acceptance or rejection of fit. The validator owns the review verdict for the validation question only.

| Responsibility | Owner |
|---|---|
| create a clear packet | source agent |
| confirm fit to lane | target agent |
| reject out-of-lane work | target agent |
| validate bounded output | named validator |
| preserve unresolved questions | source and target agents |
| escalate stop conditions | any agent that detects them |
| approve operator-review-required work | operator |

### Validator rules

- A validator must be named when `IMP` or `RSK` is high.
- Meta Detective validates contradictions, drift risk, adversarial sufficiency, and challenge requests.
- Hygiene Clean validates structural QA, pointer integrity, stale-state, and cleanup-risk issues.
- Informatics Design validates shape, taxonomy, naming, decomposition, and retrieval-safety issues.
- Meta Ops may integrate outputs, but must not self-validate high-impact output.
- AI Handling Routing gives advisory routing posture only and does not validate config changes.
- Knowledge Bank may package or route KB candidates, but must not directly promote accepted truth.

### Default validator pairings

| Agent or lane | Default validator |
|---|---|
| `alfred` | `meta_ops` |
| `meta_ops` | `meta_detective` |
| `meta_strategy` | `meta_detective` |
| `meta_detective` | `special_ops__hygiene_clean` when structure matters, otherwise `meta_ops` for execution implications |
| `special_ops__knowledge_bank` | `special_ops__informatics_design` for placement shape; `meta_detective` for promotion or canonization risk |
| `special_ops__informatics_design` | `special_ops__hygiene_clean` |
| `special_ops__prompts_workflows` | `meta_ops` |
| `special_ops__ai_handling_routing` | `meta_ops` for operational fit; operator for config-affecting recommendations |
| `special_ops__hygiene_clean` | `meta_detective` when adversarial review is needed |

## Standard handoff lifecycle

1. Source agent identifies a bounded need to hand off.
2. Source agent creates a handoff packet with objective, state, authority, thresholds, expected outputs, risks, validator need, and stop conditions.
3. Target agent confirms fit or rejects with a stated reason.
4. Validator is invoked when risk, impact, evidence weakness, authority boundary, or packet rules require it.
5. Unresolved questions are surfaced rather than buried.
6. Next action is bounded as accept, reject, validate, revise, execute bounded, escalate, request operator review, or archive.
7. Closure or escalation is recorded in the relevant trace, packet, plan, or governed output surface.

### Valid receiver dispositions

| Disposition | Meaning | Required note |
|---|---|---|
| `accept` | target can perform the bounded task | accepted scope and expected output |
| `reject` | target cannot safely or validly perform the task | rejection reason and suggested route if known |
| `validate` | target can review but not execute | validation question and verdict format |
| `revise` | packet needs repair before work | missing fields or ambiguity |
| `escalate` | stop condition or authority issue exists | escalation class and required disposition |
| `operator_review_required` | human approval is required | exact decision needed |

## First-wave handoff map

| From | To | Purpose | Default validator posture |
|---|---|---|---|
| `alfred` | `meta_ops` | route brief to orchestration | `meta_ops` confirms fit; `meta_detective` if high-risk |
| `alfred` | `meta_strategy` | strategy/options request | `meta_detective` if recommendation is high-impact |
| `meta_ops` | `meta_detective` | validation request | `meta_detective` returns verdict only |
| `meta_ops` | `special_ops__prompts_workflows` | workflow/prompt pattern request | `meta_ops` validates execution fit |
| `meta_ops` | `special_ops__hygiene_clean` | structural QA/hygiene request | `special_ops__hygiene_clean` issues finding; `meta_detective` if adversarial escalation needed |
| `meta_strategy` | `meta_detective` | challenge strategic recommendation | `meta_detective` returns challenge verdict |
| `meta_detective` | `meta_ops` | return validation verdict or stop condition | `meta_ops` integrates; does not erase verdict constraints |
| `meta_detective` | `special_ops__hygiene_clean` | route structural/hygiene finding | `special_ops__hygiene_clean` validates structural class and severity |
| `special_ops__knowledge_bank` | `special_ops__informatics_design` | validate KB placement shape | `special_ops__informatics_design` validates structure and retrieval shape |
| `special_ops__knowledge_bank` | `meta_detective` | validate promotion or canonization risk | `meta_detective` checks truth/candidate drift |
| `special_ops__informatics_design` | `special_ops__hygiene_clean` | validate structural hygiene | `special_ops__hygiene_clean` checks pointer, stale-state, and cleanup risk |
| `special_ops__prompts_workflows` | `meta_ops` | return reusable workflow/prompt pattern | `meta_ops` validates bounded orchestration fit |
| `special_ops__ai_handling_routing` | `meta_ops` | advisory routing recommendation | `meta_ops` treats as advisory; operator review for config effect |
| `special_ops__hygiene_clean` | `meta_detective` | return hygiene finding for adversarial review | `meta_detective` checks authority and drift risk |
| `meta_ops` | `special_ops__knowledge_bank` | KB placement or candidate routing request | `special_ops__informatics_design` or `meta_detective` depending on risk |
| `special_ops__prompts_workflows` | `special_ops__ai_handling_routing` | routing-posture advice for reusable workflow only | advisory only; no config mutation |

## Pair-specific handoff minimums

### `alfred` to `meta_ops`

Must include:

- operator request summary
- why this needs orchestration
- bounded objective
- operator constraints
- current state and target state
- success shape
- suggested activation set, if any
- approval-needed marker
- `EVD` / `IMP` / `RSK`
- stop conditions

### `alfred` to `meta_strategy`

Must include:

- strategic question
- decision context
- options requested
- time or leverage sensitivity
- known constraints
- what recommendation format is needed
- whether operator approval is expected
- `EVD` / `IMP` / `RSK`

### `meta_ops` to `meta_detective`

Must include:

- artifact or decision under review
- claim being challenged
- evidence references or evidence gap
- suspected drift, contradiction, or risk class
- expected verdict format: pass, fail, escalate, or revise
- implementation status and whether work is blocked pending verdict
- `EVD` / `IMP` / `RSK`

### `meta_ops` to `special_ops__prompts_workflows`

Must include:

- workflow or prompt-pattern need
- target user/process context
- reusable parts versus one-off parts
- constraints on output length, sections, and acceptance checks
- expected return shape
- whether the output is candidate-only or accepted process content
- `EVD` / `IMP` / `RSK`

### `meta_ops` to `special_ops__hygiene_clean`

Must include:

- bounded target surface
- suspected structural issue
- pointer, state, trace, or stale-condition concern
- requested check family
- expected finding format
- whether the finding can block progress
- `EVD` / `IMP` / `RSK`

### `meta_strategy` to `meta_detective`

Must include:

- recommendation or option frame to challenge
- key assumptions
- reversibility and downstream impact
- known weak evidence
- disagreement or uncertainty
- verdict needed before execution, if applicable
- `EVD` / `IMP` / `RSK`

### `meta_detective` to `meta_ops`

Must include:

- validation verdict
- pass, fail, revise, hold, or escalate disposition
- contradiction or drift finding, if any
- evidence basis
- implementation implications
- stop condition, if triggered
- next bounded action

### `meta_detective` to `special_ops__hygiene_clean`

Must include:

- structural or trace concern found during adversarial review
- affected surface
- why the issue may cross into hygiene, pointer, or stale-state territory
- requested hygiene check family
- severity suspicion if known
- `EVD` / `IMP` / `RSK`

### `special_ops__knowledge_bank` to `special_ops__informatics_design`

Must include:

- source or candidate material
- intended KB lane or target surface
- placement uncertainty
- candidate/canon boundary status
- structure, naming, or retrieval concern
- promotion route if material could become durable
- `EVD` / `IMP` / `RSK`

### `special_ops__knowledge_bank` to `meta_detective`

Must include:

- candidate material or proposed promotion risk
- current state and target state
- authority basis
- candidate/canon separation risk
- downstream accepted-truth implication
- exact verdict requested
- `EVD` / `IMP` / `RSK`

### `special_ops__informatics_design` to `special_ops__hygiene_clean`

Must include:

- structure or taxonomy output
- affected path or surface
- pointer and naming assumptions
- retrieval-safety claim
- suspected stale or collision risk
- expected hygiene verdict
- `EVD` / `IMP` / `RSK`

### `special_ops__prompts_workflows` to `meta_ops`

Must include:

- returned workflow or prompt-pattern summary
- intended use case
- reusable parts
- non-reusable constraints
- acceptance checks
- remaining risks
- whether operator review or validation is needed

### `special_ops__ai_handling_routing` to `meta_ops`

Must include:

- advisory routing recommendation
- model/tool/capability fit rationale
- fallback posture
- cost-quality or risk tradeoff
- config-affecting implications, if any
- explicit statement that config mutation is not authorized
- operator-review flag when config or runtime authority would be affected

### `special_ops__hygiene_clean` to `meta_detective`

Must include:

- hygiene finding summary
- finding class and severity when assigned
- affected surfaces
- evidence references or evidence gap
- why adversarial review may be needed
- hold, escalation, or backlog recommendation
- `EVD` / `IMP` / `RSK`

## Validation and stop conditions

### Handoff validity checks

A material handoff is valid only when:

- source and target agents are first-wave agents
- objective is bounded
- current state and target state are explicit
- authority basis is named
- expected output is concrete
- constraints are visible
- threshold values use `EVD`, `IMP`, and `RSK` on the 1-100 scale
- validator requirement is explicit
- stop conditions are explicit
- no forbidden authority is created

### Mandatory stop conditions

Stop, reject, or escalate the handoff when any of the following occur:

- target agent is not a first-wave agent
- domain-master or new-agent creation is implied
- target agent would need authority outside its lane
- Meta Detective would become executor
- AI Handling Routing would become config authority
- Hygiene Clean would mutate accepted truth through cleanup
- Knowledge Bank would silently promote candidate or source material
- Informatics Design would become truth authority
- Prompts Workflows would become orchestration authority
- Alfred would become the whole system
- Meta Ops would self-validate high-impact output
- learning queue material would be treated as runtime truth
- source or staging material would be treated as runtime authority
- `openclaw.json` would be changed through handoff
- config change is implied without operator review
- accepted truth would change without promotion path
- evidence is too weak for the claimed impact or risk
- current state is `blocked` and no unblock condition is named
- current state is `operator_review_required` and no explicit approval exists
- rejected or archived material is being reused without trace and justification

## Anti-drift safeguards

### Role-boundary safeguards

- Meta Detective is validation-only and must not implement its own findings.
- AI Handling Routing is advisory only and must not mutate `openclaw.json` or become runtime config authority.
- Hygiene Clean may classify, route, and recommend cleanup, but must not mutate accepted truth through cleanup.
- Knowledge Bank may route, package, and map knowledge, but must not silently canonize source or candidate material.
- Informatics Design may structure, decompose, name, and package, but must not become truth authority.
- Prompts Workflows may provide reusable patterns, but must not become orchestration authority.
- Alfred may intake, align, and brief routes, but must not become the whole system or execution controller.
- Meta Ops may orchestrate and integrate, but must not self-validate high-impact output.

### Surface-boundary safeguards

- Learning queues are candidate-only capture surfaces.
- Source and staging files are evidence-only unless promoted through the governed path.
- Runtime authority stays in managed runtime surfaces, not in source dumps.
- Handoff packets do not create config authority.
- Handoff packets do not apply patches.
- Handoff packets do not replace promotion packets.
- Handoff packets do not erase operator-review requirements.

### Evidence safeguards

- Low `EVD` must be visible in the packet.
- High `IMP` with weak evidence requires validation before action.
- High `RSK` requires adversarial, hygiene, or operator review as appropriate.
- Evidence-only input must be labeled evidence-only.
- Candidate input must be labeled candidate.
- Accepted input must be tied to an accepted surface or instruction.

## Acceptance criteria

This file is acceptable when all of the following are true:

- it defines purpose, scope, and non-goals
- it defines handoff principles
- it includes a reusable standard handoff packet schema
- it uses `EVD`, `IMP`, and `RSK` on a 1-100 scale
- it excludes obsolete scalar-only threshold semantics as the operative model
- it distinguishes `draft`, `candidate`, `needs_validation`, `validated`, `accepted`, `rejected`, `archived`, `blocked`, and `operator_review_required`
- it makes clear that candidate material and learning queue material are not accepted truth
- it defines owner and validator rules
- it defines a standard handoff lifecycle
- it includes a first-wave handoff map
- it includes pair-specific handoff minimums for required relationships
- it defines validation checks and stop conditions
- it prevents first-wave role-boundary drift
- it forbids config mutation through handoff
- it forbids source/staging patches through handoff
- it forbids new agents and domain masters
- it keeps process contract semantics in `managed/processes/`

## Validation checklist

| Check | Pass |
|---|---:|
| exactly one Pack C target produced | yes |
| report action confirmed as rewrite | yes |
| no config changes proposed | yes |
| no source/staging runtime patches proposed | yes |
| EVD/IMP/RSK 1-100 used | yes |
| obsolete 1-5 scoring excluded | yes |
| old scalar-only T0-T4 threshold model excluded | yes |
| first-wave agents only | yes |
| Meta Detective remains validator, not executor | yes |
| AI Handling Routing remains advisory, not config authority | yes |
| Hygiene Clean does not mutate truth through cleanup | yes |
| learning queues treated as candidate-only | yes |
| handoff packet schema included | yes |
| lifecycle and stop conditions included | yes |
