# LEARNING_QUEUE

## Purpose

Candidate-only capture surface for Prompts Workflows learning. This file is never runtime truth.

## Write permissions

- `special_ops__prompts_workflows` may add candidate entries
- `meta_ops` may add validation notes
- no writer may self-promote entries into accepted files

## Entry schema

```yaml
learning_entry:
  id:
  status: candidate | strong_candidate | needs_validation | rejected | archived
  source_ref:
  summary:
  candidate_target: essence | best_practice | mistake | template | appendix | archive
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check:
  review_due:
```

## Pending entries

- id: `PW-LQ-001`
  status: candidate
  source_ref: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-pw-001`
  summary: Additional prompt-design ranking files may refine examples or wording beyond the compact 80/20 prompt doctrine.
  candidate_target: best_practice
  evidence_refs:
    - `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-risk-register`
    - `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#pw-cand-015`
  scores:
    EVD: 3
    IMP: 3
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: likely overlaps `PW-BP-002`; validate only for non-duplicate operational value
  review_due: 2026-07-27

- id: `PW-LQ-002`
  status: candidate
  source_ref: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-pw-002`
  summary: Additional workflow research variants may add phrasing but appear convergent with the accepted bounded/stage-gated workflow doctrine.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-risk-register`
    - `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md#pw-cand-014`
  scores:
    EVD: 3
    IMP: 2
    RSK: 2
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: compare against `PW-BP-003` and `PW-TPL-004`; do not promote duplicate wording
  review_due: 2026-07-27

- id: `PW-LQ-003`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-pw-003`
  summary: Additional promptflow and handoff files from repo-accessible equivalents may contain reusable promptflow structures not captured in the clean handoff and harmonization examples.
  candidate_target: template
  evidence_refs:
    - `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-risk-register`
  scores:
    EVD: 3
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: validate against `PW-TPL-004` and `PW-TPL-005` before promotion
  review_due: 2026-07-27

- id: `PW-LQ-004`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-pw-004`
  summary: Deeper failure files about blind long-document updating and promptflow drift may add sharper countermeasures.
  candidate_target: mistake
  evidence_refs:
    - `appendices/APPENDIX_KB_SOURCE_MANIFEST.md#gap-risk-register`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
  scores:
    EVD: 3
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: avoid duplicating `PW-MK-001`, `PW-MK-003`, and `PW-MK-005`
  review_due: 2026-07-27

- id: `PW-LQ-005`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md#12-future-research-queue`
  summary: Verify external model, model-alias, model-family, browser, API, output-limit, and platform behavior claims before any future scaffold or runtime doctrine uses them.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`
    - `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
  scores:
    EVD: 3
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: keep external claims out of accepted scaffold unless primary/current evidence or runtime tests validate them
  review_due: 2026-07-27

- id: `PW-LQ-006`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md#10-adjacent-lane-routing-table`
  summary: Route model pinning, API response-format enforcement, streaming, temperature, max-token budgets, and server/runtime architecture to AI Handling/Routing or runtime owners.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`
    - `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
  scores:
    EVD: 4
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: do not encode runtime parameters as prompts/workflows doctrine; require adjacent-lane owner review
  review_due: 2026-07-27

- id: `PW-LQ-007`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
  summary: Decide whether state keeper should remain a process role inside promptflow execution or become a separate OpenClaw architectural/runtime role.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
    - `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`
  scores:
    EVD: 4
    IMP: 4
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: separate source-local explicit-state prompt discipline from persistent-state implementation ownership
  review_due: 2026-07-27

- id: `PW-LQ-008`
  status: candidate
  source_ref: `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
  summary: Formalize patch-transport tooling tests for SEARCH/REPLACE, unified diff, full-body replacement, live-edit instruction, and no-patch/manual-review modes.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
  scores:
    EVD: 5
    IMP: 4
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: extend existing PW-TPL-007 and PW-BP-001 only through validated tooling evidence; avoid universal transport law
  review_due: 2026-07-27

- id: `PW-LQ-009`
  status: candidate
  source_ref: `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
  summary: Evaluate whether generated template sidecars should become machine-readable artifacts, remain evidence-only, or be rejected as duplicate runtime templates.
  candidate_target: template
  evidence_refs:
    - `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
    - `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
  scores:
    EVD: 4
    IMP: 3
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: compare generated sidecars against PW-TPL-009, PW-TPL-010, and accepted hand-authored templates before any promotion
  review_due: 2026-07-27

- id: `PW-LQ-010`
  status: candidate
  source_ref: `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
  summary: Convert regression examples into an executable behavioral test harness for promptflow executor compliance.
  candidate_target: appendix
  evidence_refs:
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
  scores:
    EVD: 5
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: do not duplicate PW-BP-008; validate whether examples should remain documentation or become executable tests
  review_due: 2026-07-27

- id: `PW-LQ-011`
  status: needs_validation
  source_ref: `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md#future-research-mapping`
  summary: Repair or resolve the missing `SOURCE_CONFLICT_REPORT.md` reference from the new research pack before any source-conflict claims from that file are used.
  candidate_target: archive
  evidence_refs:
    - `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
  scores:
    EVD: 2
    IMP: 3
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  overlap_check: do not rely on missing-source evidence; either restore the file, correct the path, or mark the source permanently rejected
  review_due: 2026-07-27

## Promotion route

1. capture candidate here
2. score `EVD` / `IMP` / `RSK`
3. validate with `meta_ops`
4. check overlap against accepted scaffold entries and appendices
5. route to the target file class
6. package durable promotions through `managed/knowledge/KB_PROMOTION_LEDGER_TEMPLATE.md`
7. apply only through the governed promotion path

## Boundary

Learning queue entries are candidates only. They do not update `ESSENCE.md`, `BEST_PRACTICES.md`, `MISTAKES.md`, or `TEMPLATES.md` without validation.
