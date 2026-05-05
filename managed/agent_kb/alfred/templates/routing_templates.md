# Routing Templates

## Purpose

Reusable Alfred routing forms.

These templates support first-contact intake, compact route briefs, material handoffs, escalation/hold decisions, validation challenges, source-gap review, and KB repair reporting.

## Boundary

Templates are reusable forms, not governance, runtime law, source ledgers, or process authority. If a template conflicts with `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, or `managed/processes/AGENT_HANDOFF_CONTRACTS.md`, the canonical/process owner wins.

## ALFRED-TPL-001 — First-contact intake

Use when a new operator request arrives and Alfred must convert raw intent into an aligned task frame.

```md
## Alfred Intake

- **Goal:** [what the operator wants changed, decided, created, or understood]
- **Desired output:** [answer / file / patch / route brief / plan / review / recommendation]
- **Context:** [current situation, relevant prior state, live constraint]
- **Timing:** [deadline, day/week pressure, calendar boundary]
- **Capacity:** [energy, available time, cognitive load, emotional sensitivity]
- **Priority:** [why this matters now]
- **Evidence/source status:** [fully_read / partially_read / not_accessible / provisional / mixed]
- **Risk:** [what can go wrong if routed or executed incorrectly]
- **Open questions:** [only questions required for safe continuation]
- **Recommended owner:** [Alfred / meta_ops / meta_strategy / meta_detective / special_ops__prompts_workflows / special_ops__knowledge_bank / operator]
- **Next action:** [smallest useful step]
- **Stop condition:** [what blocks safe continuation]
```

## ALFRED-TPL-005 — Compact route brief

Use when Alfred's recommendation requires another owner to act, and the handoff should remain operator-readable.

```md
## Alfred Route Brief

- **To:** `<target agent or operator>`
- **Type:** `<execution_orchestration | strategy_options | validation_challenge | workflow_design | knowledge_placement | operator_clarification | source_gap_review | escalation_recommendation>`
- **Objective:** <one bounded objective>
- **Expected output:** <desired output>
- **Constraints:** <hard limits / must-not-do items>
- **Evidence:** <source refs or audit pointer>
- **Risk posture:** EVD `<low | material | high | unknown | not_material>` / IMP `<low | material | high | unknown | not_material>` / RSK `<low | material | high | unknown | not_material>`
- **Validator:** `<validator or none>`
- **Next action:** <immediate next step>
- **Stop condition:** <pause/escalation trigger>
- **Open questions:** <none or list>
- **Source gaps:** <none or list>
```

## ALFRED-TPL-006 — Canonical handoff packet

Use when the handoff is material, multi-step, source-sensitive, high-risk, or needs downstream execution without context reconstruction.

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

## ALFRED-TPL-007 — Escalation / route decision

Use when Alfred detects that normal first-contact coaching is insufficient and the task must route to a governed specialist lane.

```md
## Escalation / Route Decision

- **Reason for escalation:** [execution / strategy / validation / KB / prompt-workflow / AI-routing / hygiene / source gap / operator clarification]
- **Why Alfred should not continue alone:** [boundary, evidence, risk, authority, or source-status reason]
- **Target owner:** [agent id or operator]
- **Expected result:** [specific return artifact]
- **Evidence:** [source, current context, audit pointer, or operator statement]
- **EVD band:** [low / material / high / unknown / not_material]
- **IMP band:** [low / material / high / unknown / not_material]
- **RSK band:** [low / material / high / unknown / not_material]
- **Validator:** [agent id or none]
- **Open questions:** [questions that affect safe continuation]
- **Stop condition:** [what blocks safe continuation]
```

## ALFRED-TPL-008 — Validation challenge request

Use when Alfred needs a separate validator because evidence, authority, contradiction, impact, or risk makes self-validation unsafe.

```yaml
handoff_id: HND-alfred-YYYYMMDD-detective-001
from_agent: alfred
to_agent: meta_detective
handoff_type: validation_challenge
target_surface: <artifact-or-decision-under-review>
task_objective: Review the claim, artifact, route, or decision for contradiction, authority drift, weak evidence, or unsafe continuation.
desired_output: Validation verdict, contradiction list, drift-risk notes, and required correction path.
constraints:
  must_do:
    - Check evidence sufficiency and authority boundary.
    - Identify stop/hold/escalation needs.
  must_not_do:
    - Do not silently rewrite the artifact under review.
evidence_basis:
  source_refs:
    - <claim cluster, file path, audit pointer, or operator statement>
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: none
next_action: Return validation verdict and correction path.
stop_condition: Stop if truth mutation, config mutation, or authority ambiguity is detected.
open_questions:
  - <review questions or none>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred | meta_ops
  expected_return: validation verdict and required action
```

## ALFRED-TPL-009 — Knowledge placement / source-gap review

Use when material needs durable placement, source mapping, candidate/canon separation, or source-gap handling.

```yaml
handoff_id: HND-alfred-YYYYMMDD-kb-001
from_agent: alfred
to_agent: special_ops__knowledge_bank
handoff_type: knowledge_placement | source_gap_review
target_surface: managed/agent_kb/<agent-or-domain>/<candidate-file>.md | managed/knowledge/<file>.md | none
task_objective: Determine durable knowledge placement, source status, and candidate/canon boundary.
desired_output: KB placement recommendation, source-map note, and promotion-routing recommendation if needed.
constraints:
  must_do:
    - Preserve source status.
    - Separate candidate knowledge from accepted doctrine.
    - Identify whether material belongs in ESSENCE, BEST_PRACTICES, MISTAKES, TEMPLATES, LEARNING_QUEUE, source/audit control, or managed process/governance.
  must_not_do:
    - Do not approve promotion directly.
    - Do not treat learning queues as runtime truth.
    - Do not treat support files as a second scaffold.
evidence_basis:
  source_refs:
    - managed/agent_kb/alfred/SOURCE_MANIFEST.md
    - managed/agent_kb/alfred/COVERAGE_AUDIT.md
  confidence: high | medium | low | unknown
  source_status: fully_read | partially_read | not_accessible | provisional | mixed
evd_band: low | material | high | unknown | not_material
imp_band: low | material | high | unknown | not_material
rsk_band: low | material | high | unknown | not_material
validator: special_ops__informatics_design if structure validation is required; otherwise meta_ops
next_action: Return placement and source-boundary recommendation.
stop_condition: Stop if source material is being silently canonized.
open_questions:
  - <placement or source question>
source_gaps:
  - <source gaps or none>
return_expected:
  owner: alfred | meta_ops
  expected_return: KB placement recommendation and boundary note
```

## ALFRED-TPL-010 — One-file KB repair report

Use after a single-file KB patch or repair iteration.

```md
## KB Patch Report

- **Target file:** `managed/agent_kb/alfred/<file>.md`
- **Operation:** [created / updated / redirected / deleted / verified unchanged]
- **Canonical class:** [ESSENCE / BEST_PRACTICES / MISTAKES / TEMPLATES / LEARNING_QUEUE / source-audit-control / appendix]
- **Reason:** [why the patch was needed]
- **Source basis:** [ESSENCE / BEST_PRACTICES / MISTAKES / TEMPLATES / SOURCE_MANIFEST / COVERAGE_AUDIT / other]
- **Commit SHA:** `<sha>`
- **Fetched blob SHA:** `<sha>`
- **Verification result:** [passed / failed]
- **Remaining risk:** [none / source gap / duplicate doctrine / appendix drift / needs redirect]
- **Next recommended file:** `<path or none>`
```

## ALFRED-TPL-030 — Alfred escalation hold

Use when continuation is unsafe and no normal route should proceed until the blocker is resolved.

```yaml
alfred_escalation_hold_v1:
  blocker:
  unsafe_continuation_risk:
  current_evidence:
  affected_surface:
  recommended_next_owner:
  operator_decision_needed: true | false
  stop_condition:
```
