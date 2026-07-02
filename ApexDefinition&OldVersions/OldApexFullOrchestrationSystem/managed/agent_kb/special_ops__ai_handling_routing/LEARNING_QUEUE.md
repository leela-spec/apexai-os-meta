# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for AI Handling Routing learning. This file is never runtime truth.

## Write permissions

- `special_ops__ai_handling_routing` may add candidate entries
- `meta_ops` may add validation notes
- `meta_detective` may add escalation notes when overreach risk appears
- no writer may self-promote entries into accepted files

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | archive
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  overlap_check:
  review_due:
```

## Pending entries

### AIHR-LQ-001 — Current model/provider decision matrix

```yaml
learning_entry:
  id: AIHR-LQ-001
  status: needs_validation
  source_ref: APPENDIX_KB_CANDIDATE_LEDGER.md#AIHR-DEFER-001
  summary: Build a current model/provider/cost-quality matrix only from freshly verified provider and benchmark sources.
  candidate_target: template
  evidence_refs:
    - APPENDIX_KB_SOURCE_MANIFEST.md#Ranking-plausibility-check
    - APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-011
  scores:
    EVD: 3
    IMP: 5
    RSK: 5
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  overlap_check: must not duplicate runtime config authority or provider-policy authority
  review_due: 2026-07-25
```

### AIHR-LQ-002 — Config-impact review packet pattern

```yaml
learning_entry:
  id: AIHR-LQ-002
  status: needs_validation
  source_ref: APPENDIX_KB_CANDIDATE_LEDGER.md#AIHR-DEFER-002
  summary: Define a formal handoff pattern for routing advisory recommendations that may affect runtime config into manual/governance review.
  candidate_target: template
  evidence_refs:
    - APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-010
    - TEMPLATES.md#AIHR-TPL-006
  scores:
    EVD: 4
    IMP: 5
    RSK: 5
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  overlap_check: must not authorize direct edits to openclaw.json or model registry
  review_due: 2026-07-25
```

### AIHR-LQ-003 — Cross-agent routing boundary review

```yaml
learning_entry:
  id: AIHR-LQ-003
  status: candidate
  source_ref: APPENDIX_KB_CANDIDATE_LEDGER.md#AIHR-DEFER-003
  summary: Review whether AI Handling Routing needs a bounded cross-agent routing matrix or whether existing templates are sufficient.
  candidate_target: archive
  evidence_refs:
    - APPENDIX_KB_SOURCE_MANIFEST.md#Material-conflicts
    - APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#AIHR-DRIFT-008
  scores:
    EVD: 3
    IMP: 3
    RSK: 4
  owner: special_ops__ai_handling_routing
  validator: meta_ops
  overlap_check: must not create all-agent orchestration authority or new first-wave agents
  review_due: 2026-07-25
```

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK`
3. validate with `meta_ops`
4. escalate to manual review whenever config impact is implicated
5. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
6. apply only through the governed promotion path

## Hard boundaries

- **Constraint:** Candidate entries are not accepted practices.
- **Constraint:** This queue does not authorize config mutation.
- **Constraint:** This queue does not create new routing authority.
- **Constraint:** Provider/model-specific entries require current verification before use.
