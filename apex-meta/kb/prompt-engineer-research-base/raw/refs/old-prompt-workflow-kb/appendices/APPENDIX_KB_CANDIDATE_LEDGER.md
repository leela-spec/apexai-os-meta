# APPENDIX_KB_CANDIDATE_LEDGER

## Purpose

Candidate ledger for `special_ops__prompts_workflows` KB-base build.

This appendix records source-backed candidates before or alongside scaffold inclusion. It is not accepted runtime governance.

## Candidate status vocabulary

- `accepted_for_base`: included in compact scaffold guidance.
- `accepted_for_appendix`: retained as appendix evidence only.
- `candidate_only`: useful, but not promoted into scaffold guidance.
- `deferred`: source or idea needs later validation.
- `excluded`: outside the agent boundary.

## Candidates

|candidate_id|source_ref|candidate_summary|candidate_target|evidence_strength|impact|risk_if_wrong|status|promotion_note|
|---|---|---|---|---:|---:|---:|---|---|
|PW-CAND-001|SRC-PW-006|Prompt design must name the exact target, source authority, preservation invariants, output contract, and integrity checks before execution.|best_practice|5|5|2|accepted_for_base|Promote as compact rule, not full source copy.|
|PW-CAND-002|SRC-PW-007|Workflow execution should freeze objective, bound scope, execute one deliverable, ground, verify, stop, and decide continue/migrate.|essence|5|5|2|accepted_for_base|Core ESSENCE doctrine.|
|PW-CAND-003|SRC-PW-008|The strongest practical workflow is bounded, stage-gated, and artifact-centered; broad autonomy and giant one-turn plans are anti-patterns.|best_practice|5|5|3|accepted_for_base|Use in BEST_PRACTICES and MISTAKES.|
|PW-CAND-004|SRC-PW-009|Tier A rules include one-artifact-per-step, stop-after-step, detect-before-correct, patch-before-rewrite, explicit source authority, verify-before-trust, escalate-don't-guess.|best_practice|4|5|2|accepted_for_base|Use as compact checklist.|
|PW-CAND-005|SRC-PW-010|A research prompt should include frozen target frame, strong anti-goals, required comparison lens, strict output format, and hard response rules.|template|4|4|2|accepted_for_base|Convert into research-prompt template.|
|PW-CAND-006|SRC-PW-011|Separate source authority from verification; missing source, conflicting primary sources, or unsafe output must stop or escalate.|mistake|5|5|3|accepted_for_base|Use as mistake/countermeasure and source-authority template rule.|
|PW-CAND-007|SRC-PW-012|Codex execution prompts need mode lock, path lock, closed file set, stop conditions, review gates, and minimal Git-visible diffs.|template|5|5|4|accepted_for_base|Use as Codex execution preflight template.|
|PW-CAND-008|SRC-PW-013|Out-of-mode improvements may be detected but must not be applied silently; capture them in a bounded section with status and smallest safe future mode.|best_practice|5|4|3|accepted_for_base|Use in BEST_PRACTICES and templates.|
|PW-CAND-009|SRC-PW-014|Promptflows should source-lock, classify surfaces, check coverage, identify contradictions, freeze manifests, generate patchspecs, and produce deterministic handoff.|template|4|4|4|accepted_for_base|Use as promptflow skeleton; avoid importing harmonization-specific governance.|
|PW-CAND-010|SRC-PW-015|Clean handoff should state settled decisions, source priority, non-redo list, exact next job, risks, and success condition.|template|4|5|2|accepted_for_base|Use as handoff template.|
|PW-CAND-011|SRC-PW-002|KB rankings identify prompt/workflow and Codex-execution candidates with high scores across prompts_workflows and meta_ops validation lanes.|appendix|4|4|3|accepted_for_appendix|Ranking data remains appendix evidence.|
|PW-CAND-012|SRC-PW-003|Source inventory duplicate handling prevents same-filename variants from inflating evidence or causing inconsistent source selection.|appendix|4|3|3|accepted_for_appendix|Use in manifest and source hygiene notes.|
|PW-CAND-013|SRC-PW-005|Failure evidence says prompt/workflow assets can become hidden runtime law or broad process redesign if over-promoted.|mistake|4|5|4|accepted_for_base|Use as boundary mistake.|
|PW-CAND-014|Deferred workflow variants|Additional WorkflowResearchGem and same-filename duplicates may add wording but not new core doctrine.|learning_queue|3|2|2|candidate_only|Capture only if later validation finds non-duplicate value.|
|PW-CAND-015|Additional prompt-design rating files|Prompt design ranking variants may refine examples, but base build already has the compact 80/20 doctrine.|learning_queue|3|3|2|deferred|No scaffold blocker.|

## Candidate-to-scaffold map

|scaffold|candidate_ids|notes|
|---|---|---|
|`ESSENCE.md`|PW-CAND-002, PW-CAND-003|Compress lane doctrine and hard boundary.|
|`BEST_PRACTICES.md`|PW-CAND-001, PW-CAND-002, PW-CAND-003, PW-CAND-004, PW-CAND-008|Accepted reusable rules.|
|`MISTAKES.md`|PW-CAND-006, PW-CAND-013|Failure patterns and countermeasures.|
|`TEMPLATES.md`|PW-CAND-005, PW-CAND-007, PW-CAND-008, PW-CAND-009, PW-CAND-010|Reusable prompt/workflow/handoff templates.|
|`LEARNING_QUEUE.md`|PW-CAND-014, PW-CAND-015|Deferred source-mining candidates only.|

## Non-target candidates

|candidate|reason excluded|
|---|---|
|Broad meta-orchestration doctrine|Outside role boundary unless directly used for promptflow gates or handoff discipline.|
|QA severity governance|Belongs to QA/Hygiene authority, not this KB.|
|Config or loader behavior|Explicitly outside promptflow target.|
|KB placement authority|Belongs to Knowledge Bank / Meta Ops, not Prompts Workflows.|

## Base-build verdict

- **Verdict:** candidate set is sufficient for scaffold drafting.
- **Constraint:** accepted scaffold entries are compact operational summaries, not wholesale promotion of every source claim.
