# HANDOFF_SCHEMA

## Purpose

Define Alfred's standard handoff schema for route briefs and downstream activation packets.

This file is constrained by `SOURCE_MANIFEST.md`, `COVERAGE_AUDIT.md`, `ROLE_BOUNDARIES.md`, and `ROUTING_CONTRACT.md`. It captures validated handoff minimums only and does not define detailed Leela product workflows, day/night rituals, 5V mechanics, or mobile-intake behavior.

## Status

```yaml
agent_id: alfred
kb_root: managed/agent_kb/alfred/
file_status: created_from_validated_routing_contract
source_manifest: managed/agent_kb/alfred/SOURCE_MANIFEST.md
coverage_audit: managed/agent_kb/alfred/COVERAGE_AUDIT.md
role_boundaries: managed/agent_kb/alfred/ROLE_BOUNDARIES.md
routing_contract: managed/agent_kb/alfred/ROUTING_CONTRACT.md
validated_claim_clusters: [VC-02, VC-06, VC-07]
source_posture: validated_core_only
validator: meta_ops
next_recommended_file: managed/agent_kb/alfred/DOCTRINE.md
```

## Schema principle

An Alfred handoff must make the next owner, expected output, evidence basis, risk posture, source gaps, and stop condition explicit before work leaves Alfred's lane.

The schema should stay compact enough to use during live intake and explicit enough for downstream agents to continue without guessing.

## Required handoff fields

| Field | Required | Meaning | Notes |
|---|---:|---|---|
| `handoff_id` | yes | Stable ID for the handoff. | Use a short durable identifier. |
| `from_agent` | yes | Originating agent. | Usually `alfred`. |
| `to_agent` | yes | Target agent or lane. | Must be verified direct route or routed through `meta_ops`. |
| `handoff_type` | yes | Kind of handoff. | Use controlled values below. |
| `target_surface` | yes | File, repo path, KB surface, or bounded artifact. | Use `none` only when no target exists yet. |
| `task_objective` | yes | What needs to happen. | One bounded objective. |
| `desired_output` | yes | Expected output shape. | Example: brief, patch, plan, audit, schema, recommendation. |
| `operator_context` | conditional | Operator-facing context needed for the next owner. | Include only relevant constraints and priorities. |
| `constraints` | yes | Limits, exclusions, assumptions, and hard boundaries. | Must include source limits when relevant. |
| `evidence_basis` | yes | Sources, files, claims, or audit pointers. | Do not cite unread local/manual sources as read. |
| `evd_band` | conditional | Evidence-strength band. | Required for material work. |
| `imp_band` | conditional | Impact band. | Required for material work. |
| `rsk_band` | conditional | Risk band. | Required for material work. |
| `validator` | conditional | Validation partner or posture. | Required when risk/impact/evidence warrants review. |
| `next_action` | yes | Immediate next action expected of receiver. | Must be concrete. |
| `stop_condition` | yes | Condition requiring pause, escalation, or return. | Prevents unsafe continuation. |
| `open_questions` | yes | Unresolved questions that affect execution quality. | Use `none` only when genuinely none. |
| `source_gaps` | yes | Source gaps, provisional claims, or unread sources. | Use `none` only when no source uncertainty exists. |
| `return_expected` | yes | What should come back to Alfred or upstream owner. | Example: verdict, draft, patch result, route decision. |

## Controlled handoff types

| `handoff_type` | Use when | Typical target |
|---|---|---|
| `execution_orchestration` | Multi-step execution or specialist activation is needed. | `meta_ops` |
| `strategy_options` | Options, scenarios, timing, leverage, or recommendation packet is needed. | `meta_strategy` |
| `validation_challenge` | Evidence, authority, contradiction, drift, or risk needs adversarial review. | `meta_detective` |
| `workflow_design` | Repeatable prompt, process, checklist, or handoff pattern is needed. | `special_ops__prompts_workflows` |
| `knowledge_placement` | Durable KB placement, source mapping, or candidate/canon separation is needed. | `special_ops__knowledge_bank` |
| `operator_clarification` | The work cannot safely route until the operator clarifies constraints or intent. | Alfred/operator loop |
| `source_gap_review` | Source gaps or unread material block doctrine or execution quality. | `special_ops__knowledge_bank`, optionally `meta_detective` |
| `escalation_recommendation` | Stop, hold, degraded mode, or higher-level review may be needed. | `meta_ops` or `meta_detective` |

## EVD / IMP / RSK bands

Scores are interpreted by band, not by fine-grain number.

| Band | Range | Routing implication |
|---|---:|---|
| `low` | 1-40 | Low evidence with material/high impact requires validation or source review. Low impact/risk may remain local. |
| `material` | 41-60 | Requires explicit constraints, owner, and validation posture. |
| `high` | 61-100 | Requires validator, stop condition, and careful evidence/source handling. |
| `unknown` | n/a | Use when scoring is not yet possible; usually route to clarification or validation. |
| `not_material` | n/a | Use only for trivial/local tasks where banding would add noise. |

## Canonical handoff template

```yaml
handoff_id: HND-alfred-YYYYMMDD-001
from_agent: alfred
to_agent: meta_ops | meta_strategy | meta_detective | special_ops__prompts_workflows | special_ops__knowledge_bank | operator
handoff_type: execution_orchestration | strategy_options | validation_challenge | workflow_design | knowledge_placement | operator_clarification | source_gap_review | escalation_recommendation
target_surface: <path-or-bounded-target-or-none>
task_objective: <one bounded objective>
desired_output: <expected output shape>
operator_context:
  priority: <operator priority or none>
  timing: <timing/capacity constraint or none>
  relevant_context: <compact context only>
constraints:
  must_do:
    - <required constraint>
  must_not_do:
    - <forbidden action or boundary>
  assumptions:
    - <explicit assumption or none>
evidence_basis:
  source_refs:
    - <source ID, file path, claim cluster, or audit pointer>
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: <agent-or-none>
next_action: <immediate next action>
stop_condition: <condition requiring pause/escalation/return>
open_questions:
  - <question or none>
source_gaps:
  - <gap or none>
return_expected:
  owner: alfred | meta_ops | operator | other
  expected_return: <what should come back>
```

## Compact operator-facing template

Use this when the handoff is being shown to the operator or kept short in chat.

```md
## Alfred Route Brief

- **To:** `<target agent>`
- **Type:** `<handoff_type>`
- **Objective:** <one bounded objective>
- **Expected output:** <desired output>
- **Constraints:** <hard limits / must-not-do items>
- **Evidence:** <source refs or audit pointer>
- **Risk posture:** EVD `<band>` / IMP `<band>` / RSK `<band>`
- **Validator:** `<validator or none>`
- **Next action:** <immediate next step>
- **Stop condition:** <pause/escalation trigger>
- **Open questions:** <none or list>
- **Source gaps:** <none or list>
```

## Target-specific examples

### Route to `meta_ops`

```yaml
handoff_id: HND-alfred-YYYYMMDD-ops-001
from_agent: alfred
to_agent: meta_ops
handoff_type: execution_orchestration
target_surface: managed/agent_kb/alfred/<target-file>.md
task_objective: Create or update exactly one bounded KB file from validated source claims.
desired_output: Verified file write with commit SHA, fetched blob SHA, verification result, and next recommended file.
constraints:
  must_do:
    - Fetch current file before writing.
    - Write exactly one file.
    - Fetch back and verify after write.
  must_not_do:
    - Do not use Apex files as substitutes for Master Of Arts source reading.
    - Do not harden local/manual source gaps into doctrine.
evidence_basis:
  source_refs:
    - managed/agent_kb/alfred/SOURCE_MANIFEST.md
    - managed/agent_kb/alfred/COVERAGE_AUDIT.md
  confidence: high
  source_status: mixed
evd_band: high
imp_band: material
rsk_band: material
validator: meta_ops
next_action: Execute bounded write and fetch-back verification.
stop_condition: Stop if source status, target ownership, or validation boundary becomes unclear.
open_questions:
  - none
source_gaps:
  - local/manual sources M01-M40 remain not_accessible unless separately read.
return_expected:
  owner: alfred
  expected_return: commit SHA, fetched blob SHA, verification result, next file
```

### Route to `meta_strategy`

```yaml
handoff_id: HND-alfred-YYYYMMDD-strategy-001
from_agent: alfred
to_agent: meta_strategy
handoff_type: strategy_options
target_surface: none
task_objective: Compare viable paths and recommend a bounded next path.
desired_output: Option comparison with assumptions, dependencies, risks, reversibility, and recommendation.
constraints:
  must_do:
    - Preserve operator constraints.
    - Surface assumptions explicitly.
  must_not_do:
    - Do not execute the recommendation.
    - Do not override operator constraints.
evidence_basis:
  source_refs:
    - operator request
    - relevant source/audit pointers
  confidence: medium
  source_status: mixed
evd_band: material
imp_band: material
rsk_band: material
validator: meta_detective if high-risk; otherwise meta_ops or none
next_action: Produce scenario/options packet.
stop_condition: Stop if recommendation would require execution, promotion, or authority not granted.
open_questions:
  - <decision-relevant unknowns>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred
  expected_return: recommendation packet or option comparison
```

### Route to `meta_detective`

```yaml
handoff_id: HND-alfred-YYYYMMDD-detective-001
from_agent: alfred
to_agent: meta_detective
handoff_type: validation_challenge
target_surface: <artifact-or-decision-under-review>
task_objective: Review the claim, artifact, or route for contradiction, authority drift, weak evidence, or unsafe continuation.
desired_output: Validation verdict, contradiction list, drift-risk notes, and required correction path.
constraints:
  must_do:
    - Check evidence sufficiency and authority boundary.
    - Identify stop/hold/escalation needs.
  must_not_do:
    - Do not silently rewrite the artifact under review.
evidence_basis:
  source_refs:
    - <claim cluster or file path>
  confidence: medium | low | unknown
  source_status: mixed | provisional | not_accessible
evd_band: low | material | high | unknown
imp_band: material | high
rsk_band: material | high
validator: special_ops__hygiene_clean when structural hygiene issue is detected; otherwise none
next_action: Return validation verdict and correction path.
stop_condition: Stop if truth mutation, config mutation, or authority ambiguity is detected.
open_questions:
  - <review questions>
source_gaps:
  - <source gaps>
return_expected:
  owner: alfred | meta_ops
  expected_return: validation verdict and required action
```

### Route to `special_ops__prompts_workflows`

```yaml
handoff_id: HND-alfred-YYYYMMDD-workflow-001
from_agent: alfred
to_agent: special_ops__prompts_workflows
handoff_type: workflow_design
target_surface: <workflow-or-template-target>
task_objective: Design a repeatable prompt/workflow/handoff pattern for bounded reuse.
desired_output: Reusable workflow structure, handoff wording, checklist, or drift-reduction pattern.
constraints:
  must_do:
    - Keep the pattern bounded and reviewable.
    - Include acceptance criteria or stop conditions.
  must_not_do:
    - Do not convert templates into governance by default.
    - Do not own orchestration or AI routing authority.
evidence_basis:
  source_refs:
    - <source refs or current prompt>
  confidence: medium
  source_status: mixed
evd_band: material
imp_band: material
rsk_band: low | material
validator: meta_ops
next_action: Produce reusable workflow or handoff pattern.
stop_condition: Stop if workflow design would mutate doctrine or config.
open_questions:
  - <template ambiguity or none>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred | meta_ops
  expected_return: reusable pattern and validation notes
```

### Route to `special_ops__knowledge_bank`

```yaml
handoff_id: HND-alfred-YYYYMMDD-kb-001
from_agent: alfred
to_agent: special_ops__knowledge_bank
handoff_type: knowledge_placement | source_gap_review
target_surface: managed/agent_kb/<agent-or-domain>/<candidate-file>.md
task_objective: Determine durable knowledge placement, source status, and candidate/canon boundary.
desired_output: KB placement recommendation, source-map note, and promotion-routing recommendation if needed.
constraints:
  must_do:
    - Preserve source status.
    - Separate candidate knowledge from accepted doctrine.
  must_not_do:
    - Do not approve promotion directly.
    - Do not treat learning queues as runtime truth.
evidence_basis:
  source_refs:
    - managed/agent_kb/alfred/SOURCE_MANIFEST.md
    - managed/agent_kb/alfred/COVERAGE_AUDIT.md
  confidence: high | medium | low
  source_status: fully_read | mixed | provisional | not_accessible
evd_band: material
imp_band: material
rsk_band: material
validator: special_ops__informatics_design if structure validation is required; otherwise meta_ops
next_action: Return placement and source-boundary recommendation.
stop_condition: Stop if source material is being silently canonized.
open_questions:
  - <placement or source question>
source_gaps:
  - <source gaps>
return_expected:
  owner: alfred | meta_ops
  expected_return: KB placement recommendation and boundary note
```

## Invalid handoff patterns

| Invalid pattern | Why invalid | Correction |
|---|---|---|
| Missing target owner | Downstream work cannot proceed legibly. | Name a verified `to_agent` or route through `meta_ops`. |
| No stop condition | Receiver may continue unsafely under uncertainty. | Add explicit stop, hold, escalation, or return condition. |
| Unread source treated as read | Creates source-gap hardening. | Mark `not_accessible`, `provisional`, or route to source-gap review. |
| Alfred self-validates high-risk work | Collapses intake and validation roles. | Route to `meta_detective` or named validator. |
| Strategy routed as execution | Produces premature implementation. | Route to `meta_strategy` first. |
| Knowledge placement treated as promotion | Confuses candidate/canon boundary. | Route to `special_ops__knowledge_bank`; promotion remains separate. |
| Template treated as governance | Turns reusable wording into authority. | Keep as workflow/template unless promoted. |

## Minimal handoff quality checklist

A handoff is acceptable only if it answers:

1. Who is receiving it?
2. What exactly should they produce?
3. What target surface or bounded artifact is affected?
4. What constraints and must-not-do rules apply?
5. What evidence supports the request?
6. What source gaps or provisional claims remain?
7. What EVD/IMP/RSK posture applies when material?
8. Who validates, if validation is needed?
9. What is the next action?
10. What condition stops or escalates the work?

## Update boundary

This schema may be updated when:

- `ROUTING_CONTRACT.md` changes,
- a new verified direct handoff partner is added to Alfred's seed layer,
- source-gap handling changes after a source-extension pass,
- promotion/governance rules require additional handoff fields.

This schema must not be expanded with Leela-specific product mechanics until those source gaps are resolved or explicitly marked provisional in a non-doctrine surface.
