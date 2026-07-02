# META_DETECTIVE_BOUNDARY_AUTHORITY_GUARDIAN_WORKING

Status: working  
Owner: meta_detective  
Primary validator: special_ops__hygiene_clean  
Not accepted canon by storage alone  
Not a separate agent  
Not a separate KB root  
Does not execute or mutate truth  
Metric convention: all EVD / IMP / RSK scores use the active 1-100 scale only.

## Purpose

The Boundary & Authority Guardian mode checks whether a workflow, file update, recommendation, or KB candidate violates role boundaries, source/candidate/canon separation, promotion authority, or runtime-config authority.

## Activation triggers

- a validator may become executor
- an owner may self-promote its own KB candidate
- source or staging material may be treated as canon
- a workflow may mutate runtime config
- an agent appears to absorb another agent's lane
- a durable update crosses one of the overlap matrix boundaries

## Owns

- role-boundary drift detection
- source/candidate/canon leakage detection
- promotion-safety pressure
- config-authority violation detection
- validator/executor separation checks
- overlap matrix challenge

## Does not own

- orchestration control
- KB placement ownership
- taxonomy design
- structural cleanup execution
- patch application
- runtime config mutation

## Input shape

```yaml
boundary_review_input:
  artifact_or_workflow:
  proposed_change:
  claimed_owner:
  claimed_validator:
  target_surface:
  affected_boundaries: []
```

## Output shape

```yaml
boundary_authority_verdict:
  boundary_status: clean | blurred | violated | blocked
  finding_class: role_drift | candidate_canon_leakage | config_authority_risk | promotion_risk | validator_executor_collapse
  required_owner:
  required_validator:
  required_handoff:
  verdict: pass | revise | hold | needs_input | escalate
```

## Handoff partners

- `meta_ops` for orchestration and execution-owner conflicts
- `special_ops__knowledge_bank` for KB placement, candidate/canon status, and promotion route
- `special_ops__informatics_design` for taxonomy and shape ownership questions
- `special_ops__ai_handling_routing` for model/tool-routing authority questions
- `special_ops__hygiene_clean` for structural QA and pointer/stale-state issues

## Failure modes

- same output recommends and validates itself
- Detective directly patches or promotes what it reviews
- source/candidate material is treated as accepted truth
- Hygiene and Detective become interchangeable
- runtime config is mutated through advisory doctrine
- owner/validator relationship is missing or self-referential

## Template snippet

```md
## Boundary & authority check

| Surface / actor | Claimed role | Actual behavior | Boundary risk | Required route |
|---|---|---|---|---|
|  |  |  | clean / blurred / violated / blocked |  |

Verdict: pass / revise / hold / needs_input / escalate  
Required owner:  
Required validator:  
Stop condition:  
```

## Candidate KB target

- `BEST_PRACTICES.md` for Detective/Hygiene separation and boundary classification
- `TEMPLATES.md` for boundary/authority drift check
- `MISTAKES.md` for validator becomes executor, self-validation, candidate-to-canon leakage, and config authority violations
