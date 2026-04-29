# HOLDING_ORCHESTRATION_FLOW

## Purpose

This file defines the minimum coherent first-wave flow for intake, activation, validation, and promotion handling in the holding-layer architecture.

## Entry rule

Start from the smallest bounded activation set that can do the job legibly.

## Flow

### Intake and thresholding

1. capture task, desired output, and current constraints
2. assign provisional `EVD`, `IMP`, and `RSK` scores on the 1-100 scale
3. interpret scores by band, not by fine-grain number
4. surface weak evidence, material impact, high risk, operator-review need, and any blocking state before activation
5. decide whether the task is:
   - intake / alignment
   - execution / orchestration
   - strategy / options
   - validation / challenge
   - KB placement
   - structure / readability
   - AI routing posture
   - hygiene / structural correction

### Activation

`meta_ops` activates only the necessary agents.

Typical patterns:

- `alfred -> meta_ops`
- `meta_ops + special_ops__knowledge_bank`
- `meta_ops + special_ops__informatics_design`
- `meta_ops + special_ops__prompts_workflows`
- `meta_ops + meta_strategy`
- `meta_ops + meta_detective`
- `meta_ops + special_ops__hygiene_clean`

### Validation

Validation posture follows band logic:

- Low control: `IMP` and `RSK` both 1-40
- Material control: `IMP` 41-60 or `RSK` 41-60
- High control: `IMP` 61-100 or `RSK` 61-100
- Weak evidence: `EVD` 1-40 with material/high impact
- High-risk or high-impact work requires the relevant validator before durable application

### Output routing

The orchestration flow may produce:

- handoff brief
- orchestration plan
- strategy options packet
- challenge packet
- KB candidate entry
- QA finding
- promotion packet draft
- operator change notice

## Handoff expectation

Every handoff must name:

- from agent
- to agent
- target surface
- expected output
- `EVD` / `IMP` / `RSK` scores and band interpretation
- validator
- next action
- stop condition

## Promotion and hygiene rule

- Learning may create candidate entries.
- Candidate entries do not equal promotion.
- Severe hygiene findings route; they do not self-resolve by silence.

## Boundary note

This process file operationalizes the canons.
It does not replace constitutional runtime law.
Scores must be interpreted by band. Fine-grain differences (e.g. 63 vs 67) must not change validation requirements.
