# MISTAKES

## Purpose

Accepted validated Prompts Workflows failure patterns and countermeasures.

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
  pattern: Chat-authored unified diffs are used as the primary transport artifact for existing Markdown files.
  trigger_conditions:
    - exact repo preimage is unavailable
    - diff is copied through Markdown or code fences
    - line endings, whitespace, or hidden characters may be normalized
    - validation occurs in a temporary or simulated checkout
  countermeasure: Replace the diff artifact with a full final body or one-file live-edit instruction; run `git diff --check` and `git diff -- <file>` in the actual checkout for review.
  evidence_refs:
    - operator feedback, 2026-04-27, "CRLF check 1 error: patch failed"
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-MK-002`
  status: accepted
  pattern: Patch validation is reported without distinguishing real-checkout validation from temporary simulation or chat-side intent.
  trigger_conditions:
    - generated artifact says both checked and not checked
    - temp repo validation is treated as equivalent to local apply validation
    - executor is asked to repair ambiguous diffs after failure
  countermeasure: Record artifact validity, live target state, line-ending state, and real `git apply --check` or live-edit diff state separately; block the patch if any state is unknown.
  evidence_refs:
    - operator feedback, 2026-04-27, "patch state became misleading"
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 4
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-MK-003`
  status: accepted
  pattern: Markdown-carried unified diff is semantically reviewable but malformed or truncated as a patch artifact.
  trigger_conditions:
    - `git apply --check` reports a corrupt patch
    - the fenced diff lacks complete hunk context or continuation
    - the live target still matches the intended preimage
    - the intended bounded additions are visible in the artifact
  countermeasure: Do not force-apply or hand-repair the patch bytes. Verify target drift, live-edit only the intended bounded content into the target file, show the real `git diff`, then resume downstream validation.
  evidence_refs:
    - `OpenClaw/07_finalopenclawsystem/NewFinals/NextLevel2/NeweFinal/PACK_D_CROSS_REFERENCE_MANIFEST_UNIFIED_DIFF.md`
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 5
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-27
- id: `PW-MK-004`
  status: accepted
  pattern: Deep-research prompt states locked assumptions and exclusions, but leaves source-access, citation handling, and detour budget underspecified, causing the research agent to spend early cycles on connector discovery, generic capability verification, or citation mechanics instead of the requested synthesis.
  trigger_conditions:
    - prompt requires a large implementation-ready report
    - prompt lists many exclusions but does not assign a zero-detour rule to them
    - required repo surfaces are named, but exact local/read/fetch priority is not specified
    - citation expectations are implicit or mixed with private/local source use
    - tool capability is marked as assumed, but the prompt does not say to convert uncertainty into validation tests
  countermeasure: Add a deep-research preflight block that names source-access priority, citation/evidence format, locked-assumption handling, detour budget, missing-source routing, and Phase 1 fallback. Keep excluded topics at zero research budget unless explicitly reopened.
  evidence_refs:
    - `OpenClaw/02_research-kb/best-practices/operational-framework/UpdateProcessSSOTS/DRGPT55THinkingProcess.md`
    - `OpenClaw/04_final-system-setup/AfterOpenClawFIrstSetup/New_orchestration/DeepResearchPrompt_v2.md`
    - `managed/processes/DEEP_RESEARCH_TO_PATCHSPEC_WORKFLOW.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-28

- id: `PW-MK-005`
  status: accepted
  pattern: Governance-first substitution in artifact-producing workflows.
  trigger_conditions:
    - the user asks for a concrete file, diff, KB update, or prompt artifact
    - the workflow produces source ledgers, scope contracts, broad audits, claim caches, or acceptance-test scaffolds first
    - validation is described before any target artifact exists
    - the run ends with a recommended next action rather than the requested artifact
  countermeasure: Reframe the workflow as one bounded production unit: produce the target artifact first, validate the concrete artifact second, repair once if validation fails, and stop for operator continuation.
  evidence_refs:
    - `Production_First_Iteration_Learning_Record.md`
    - `Production_First_Diff_Validation_Report.md`
    - `GitHub_Extended_Thinking_Production_First_Patch_Flow.md`
  scores:
    EVD: 5
    IMP: 5
    RSK: 4
  owner: special_ops__prompts_workflows
  validator: meta_ops
  review_due: 2026-07-30

## Empty-state marker or initial entries

Add entries here only after validation and promotion from `LEARNING_QUEUE.md`.
