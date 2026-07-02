# META_DETECTIVE_RISK_FAILURE_RED_TEAMER_WORKING

Status: working  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## Purpose

The Risk & Failure-Mode Red Teamer mode tests a recommendation, handoff, patch plan, or promotion candidate against failure scenarios, base-rate pressure, reversibility, stop conditions, and escalation needs.

## Activation triggers

- recommendation has high impact or irreversible consequences
- strategy relies on uncertain assumptions
- execution path has unclear failure handling
- decision may be a one-way door
- base rates or comparable failures matter
- a pre-mortem is needed before execution

## Owns

- pre-mortem challenge
- base-rate challenge
- reversibility and risk escalation review
- failure-mode analysis
- stop-condition detection
- falsification test design
- counterfactual challenge

## Does not own

- mitigation execution
- project management
- final strategy ownership
- operational sequencing
- patch application
- config changes

## Input shape

```yaml
risk_review_input:
  recommendation_or_plan:
  expected_upside:
  known_assumptions: []
  proposed_action:
  reversibility_claim:
  success_metric:
```

## Output shape

```yaml
risk_failure_verdict:
  failure_modes:
    - scenario:
      cause:
      early_warning_signal:
      kill_or_revise_trigger:
  base_rate_gap:
  reversibility_risk:
  falsification_test:
  verdict: pass | revise | hold | needs_input | escalate
  required_owner:
```

## Handoff partners

- `meta_strategy` when the recommendation needs scenario or timing revision
- `meta_ops` when risk blocks or changes execution routing
- `special_ops__hygiene_clean` when failure risk comes from stale state, pointers, or structural QA gaps
- `special_ops__knowledge_bank` when promotion risk or canon leakage is part of the failure mode

## Failure modes

- risk critique becomes vague pessimism
- pre-mortem identifies failures but no stop condition
- risk review executes mitigation instead of routing it
- high-risk plan passes without base-rate or reversibility pressure
- failure-mode analysis blocks all action without decision relevance

## Template snippet

```md
## Risk & failure-mode red-team packet

| Failure scenario | Cause | Early warning signal | Kill / revise trigger | Owner |
|---|---|---|---|---|
|  |  |  |  |  |

Base-rate gap:  
Reversibility risk:  
Falsification test:  
Verdict: pass / revise / hold / needs_input / escalate  
```

## Candidate KB target

- `BEST_PRACTICES.md` for high-risk validation mode selection
- `TEMPLATES.md` for risk/failure-mode packet
- `MISTAKES.md` for challenge theater and verdict without stop condition
- `LEARNING_QUEUE.md` for heavier base-rate and claim-level verification extensions
