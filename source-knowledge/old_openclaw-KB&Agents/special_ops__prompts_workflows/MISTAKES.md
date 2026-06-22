# MISTAKES

## Purpose

Accepted reusable Prompts Workflows failure patterns and countermeasures.

This scaffold is compact. Detailed evidence lives in `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`.

## Entry schema

```yaml
mistake_entry:
  id:
  status: accepted | deprecated
  pattern:
  trigger_conditions:
  countermeasure:
  evidence_refs:
  scores:
    EVD:
    IMP:
    RSK:
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due:
```

## Accepted mistake patterns

- id: `PW-MK-001`
  status: accepted
  pattern: Whole-document rewrite is used for a bounded defect, causing silent compression, omissions, or unrelated wording changes.
  trigger_conditions:
    - long Markdown file
    - localized defect or reference break
    - weak anchors or broad instruction such as "clean up" or "make coherent"
    - no explicit preservation invariant
  countermeasure: Use patch mode for stable local defects. If patch transport is fragile, use a full final body or live-edit instruction with explicit preservation and real diff/read-back verification.
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-001`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-003`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-002`
  status: accepted
  pattern: Source summaries, previous-chat claims, or candidate artifacts are treated as primary truth when raw source is available.
  trigger_conditions:
    - multiple source files exist
    - summaries are easier to read than originals
    - prompt says only "use these files"
    - authority order is not declared
  countermeasure: Declare source tiers before execution. Use raw/current source as primary when available; mark derived, working, speculative, or stale material explicitly.
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-008`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-003`
  status: accepted
  pattern: One prompt or promptflow blends research, architecture, editing, QA, packaging, and finalization into one opaque pass.
  trigger_conditions:
    - prompt asks for many major outputs
    - target is not one bounded artifact or closed file set
    - quality gates are mentioned but not sequenced
    - continuation is automatic
  countermeasure: Classify overload before execution. Split into bounded passes or treat the promptflow as a closed execution unit with explicit file order and verification gates.
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-002`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-004`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-004`
  status: accepted
  pattern: Output is approved because it is fluent, structured, or plausible, without evidence, read-back, diff, test, or checklist verification.
  trigger_conditions:
    - agent says "done" after generation
    - file write or patch is not fetched back
    - no instruction-parity check is run
    - no evidence refs are recorded
  countermeasure: Require verification before trust. Use read-back, diff review, file-state check, checklist, source evidence, or test depending on the output type.
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-006`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-005`
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-08--false-completion-without-fetch-back`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-005`
  status: accepted
  pattern: A reusable prompt, template, or workflow pattern is treated as hidden runtime governance.
  trigger_conditions:
    - template says what to do but does not name authority limits
    - operator uses a promptflow as proof of governance approval
    - KB scaffold content is copied into config, QA, promotion, or orchestration authority lanes
  countermeasure: Keep templates as construction aids. Route governance/config/QA/promotion questions to their owning surfaces or agents.
  evidence_refs:
    - `appendices/SOURCE_CONFLICT_REPORT.md#pw-conflict-003`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-014`
  scores:
    EVD: 4
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-006`
  status: accepted
  pattern: Out-of-mode improvements are silently applied during a bounded execution run.
  trigger_conditions:
    - agent notices adjacent cleanup or architecture improvement
    - current mode is closed or one-file only
    - improvement feels obviously useful
    - no explicit capture section exists
  countermeasure: Capture high-value improvements in a bounded `Improvement Opportunities Not Applied` section; do not apply them until a future authorized mode.
  evidence_refs:
    - `appendices/APPENDIX_KB_INFORMATION_RANKING_LEDGER.md#pw-info-008`
    - `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md#pw-drift-011`
  scores:
    EVD: 5
    IMP: 4
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-007`
  status: accepted
  pattern: A named promptflow artifact is treated as the whole task even when the operator intended execution of the broader flow.
  trigger_conditions:
    - operator names a promptflow, appendix, or artifact path
    - named artifact already exists or matches a prior commit
    - user asks to execute rather than merely inspect
    - assistant does not compare operator intent against the artifact contract and repo state
  countermeasure: Run an intent-contract check before reporting completion. If the operator's intended execution scope is broader than the named artifact status, create the missing bounded output artifact or stop on a real blocking question. Do not report `no-op` merely because one named file already exists.
  evidence_refs:
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#user-intent-versus-executed-promptflow-gap-analysis`
    - `appendices/APPENDIX_KB_EXAMPLES.md#example-2-user-intent-versus-named-artifact-mismatch`
    - `appendices/PROMPTFLOW_PROMPTS_WORKFLOWS_BOUNDED_EXECUTION_GUARDRAILS.md#5-required-execution-contract`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-008`
  status: accepted
  pattern: Completion is claimed from artifact existence instead of current completeness, intent fit, and validation against the requested phase.
  trigger_conditions:
    - prior artifact exists
    - previous commit already contains related content
    - assistant reports status before checking the intended deliverable
    - requested output includes decisions, options, recommendations, or next-step research
  countermeasure: Validate against the active requested deliverable: intended output, exact target, content completeness, one-file or one-artifact constraint, and stop condition. If the content exists but does not answer the requested decision layer, create the missing artifact or report the exact gap.
  evidence_refs:
    - `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md#current-qa-status`
    - `appendices/APPENDIX_KB_EXAMPLES.md#regression-checklist`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-009`
  status: accepted
  pattern: Execution state is reconstructed from chat history, prior messages, or implied continuity instead of an explicit current frame or state block.
  trigger_conditions:
    - task says continue from where we left off
    - current STATE_BLOCK or frame block is missing, stale, or contradictory
    - source refs or target file are inferred from prior chat
    - executor proceeds despite state ambiguity
  countermeasure: Require an explicit current frame/state block and atomic task payload. If state is missing, stale, or contradictory, emit HALT or CLARIFY before execution.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-01--implicit-chat-history-state-reconstruction`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-02--stale-or-missing-state_block`
  scores:
    EVD: 5
    IMP: 5
    RSK: 3
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-010`
  status: accepted
  pattern: A compound or underspecified task payload expands into multiple artifacts, directory scans, unauthorized targets, or scaffold edits.
  trigger_conditions:
    - scope contains AND or THEN
    - target file is missing, broad, or outside the allowed root
    - input_refs are absent, directory-level, or inferred
    - appendix task also mutates scaffold
  countermeasure: Split compound work into one atomic task per call. Require exact target file, exact source refs, and target-root validation before execution.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-03--compound-task_payload-using-andthen`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-04--target-path-outside-target-root`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-05--directory-scan-without-explicit-input_refs`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

- id: `PW-MK-011`
  status: accepted
  pattern: Execution continues after a HALT, CLARIFY, patch-check failure, split-required condition, or failed closure validation.
  trigger_conditions:
    - unresolved HALT exists
    - ambiguity should produce CLARIFY but executor guesses
    - patch preimage or dry-run fails
    - split-required output is replaced with a summary
    - closure is claimed despite failed or missing validation
  countermeasure: Treat control signals and validation failures as hard stops. Do not proceed until the payload, source refs, patch preimage, split plan, or validation evidence is corrected.
  evidence_refs:
    - `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
    - `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-06--ambiguity-that-should-return-clarify`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-07--unsafe-continuation-after-halt-condition`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-09--patch-preimage-mismatch`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-10--skipped-dry-run-before-patch`
    - `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md#rg-11--split-required-output-that-substitutes-summary`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27

## Appendix pointers

- Anti-drift evidence: `appendices/APPENDIX_KB_ANTI_DRIFT_EVIDENCE.md`
- Source conflict report: `appendices/SOURCE_CONFLICT_REPORT.md`
- Candidate ledger: `appendices/APPENDIX_KB_CANDIDATE_LEDGER.md`
- Examples: `appendices/APPENDIX_KB_EXAMPLES.md`
- QA and next research plan: `appendices/APPENDIX_KB_QA_AND_NEXT_RESEARCH_PLAN.md`
- Constant failure integration process: `appendices/APPENDIX_KB_CONSTANT_FAILURE_INTEGRATION_PROCESS.md`
- Execution control contracts: `appendices/APPENDIX_KB_EXECUTION_CONTROL_CONTRACTS.md`
- Constant failure source notes: `appendices/APPENDIX_KB_CONSTANT_FAILURE_SOURCE_NOTES.md`
- Patch transport protocols: `appendices/APPENDIX_KB_PATCH_TRANSPORT_PROTOCOLS.md`
- Regression examples: `appendices/APPENDIX_KB_REGRESSION_EXAMPLES_AGENT_DRIFT.md`
- Runtime template catalog: `appendices/APPENDIX_KB_RUNTIME_TEMPLATE_CATALOG.md`
- External claim verification: `appendices/APPENDIX_KB_EXTERNAL_CLAIM_VERIFICATION.md`

## Promotion boundary

Add entries here only after validation and promotion from `LEARNING_QUEUE.md`.
