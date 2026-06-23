# APPENDIX_KB_ANTI_DRIFT_EVIDENCE

## Purpose

Anti-drift evidence appendix for `special_ops__prompts_workflows`.

This appendix stores failure evidence and safeguards so scaffold files can stay compact.

## Core anti-drift findings

|evidence_id|source_ref|failure_or_risk|safeguard|target_scaffold|
|---|---|---|---|---|
|PW-DRIFT-001|SRC-PW-006|Vague prompts produce meta-discussion, drift, and extra work.|Name the exact target first; use one primary objective and explicit output contract.|`BEST_PRACTICES.md`|
|PW-DRIFT-002|SRC-PW-006|Source ambiguity blends truth, examples, and background.|Declare source authority and conflict handling before execution.|`BEST_PRACTICES.md`, `TEMPLATES.md`|
|PW-DRIFT-003|SRC-PW-006|Whole-document rewrite causes silent compression and loss.|Use patch mode for bounded defects; preserve non-target content explicitly.|`BEST_PRACTICES.md`, `MISTAKES.md`|
|PW-DRIFT-004|SRC-PW-007|Large mixed prompts merge research, architecture, editing, QA, packaging, and finalization.|Classify overload before execution and split into one deliverable per pass.|`ESSENCE.md`, `BEST_PRACTICES.md`|
|PW-DRIFT-005|SRC-PW-007|Finished-looking output is mistaken for reliable output.|Require read-back, diff review, checklist, artifact grounding, or targeted audit before trust.|`BEST_PRACTICES.md`|
|PW-DRIFT-006|SRC-PW-008|Broad autonomy by default creates uncontrolled scope widening.|Use bounded, stage-gated, artifact-centered execution instead.|`ESSENCE.md`, `MISTAKES.md`|
|PW-DRIFT-007|SRC-PW-009|Fix-first behavior patches imagined problems and corrupts target state.|Detect before correct: inspect current state before modifying anything.|`BEST_PRACTICES.md`, `MISTAKES.md`|
|PW-DRIFT-008|SRC-PW-011|A summary or chat output is treated as primary source when raw source exists.|Use source tiers; primary source outranks derived summaries and working material.|`BEST_PRACTICES.md`, `TEMPLATES.md`|
|PW-DRIFT-009|SRC-PW-011|Unsafe or missing-source output is delivered as complete.|Use explicit confidence states and stop/escalate on missing input, conflicting primary sources, or unsafe output.|`MISTAKES.md`|
|PW-DRIFT-010|SRC-PW-012|Codex-style execution drifts from mode, path, or closed file set.|Lock mode, repo, branch, target root, closed files, allowed actions, forbidden actions, and stop conditions.|`TEMPLATES.md`|
|PW-DRIFT-011|SRC-PW-013|Detected improvements are silently applied outside the current scope.|Capture out-of-mode improvements separately; do not apply them in the bounded run.|`BEST_PRACTICES.md`, `TEMPLATES.md`|
|PW-DRIFT-012|SRC-PW-014|Promptflows proceed to rewrite/build before source lock, coverage, contradiction, or manifest freeze.|Use staged source lock, coverage matrix, contradiction matrix, manifest freeze, and handoff before build execution.|`TEMPLATES.md`|
|PW-DRIFT-013|SRC-PW-015|New chats or continuation runs re-litigate settled architecture and lose exact next job.|Use clean handoff: settled decisions, non-redo list, authority stack, exact next job, risks, and success condition.|`TEMPLATES.md`|
|PW-DRIFT-014|SRC-PW-005|Prompt/workflow assets become hidden runtime law or broad process redesign.|State that templates are reusable patterns, not governance. Route authority questions to proper owners.|`ESSENCE.md`, `MISTAKES.md`|

## Reusable safeguards

### Safeguard A — Scope lock

- **Rule:** Every prompt/workflow must name target, scope, intended output, non-goals, and stop condition.
- **Use when:** task is file-producing, patch-producing, research-producing, or handoff-producing.
- **Failure prevented:** helpful overreach and broad redesign.

### Safeguard B — Source authority preflight

- **Rule:** State which source is primary, derived, working, speculative, or stale before acting.
- **Use when:** multiple files, summaries, or prior chats are involved.
- **Failure prevented:** blended authority and invented truth.

### Safeguard C — One deliverable gate

- **Rule:** Produce one substantial deliverable per pass, then stop or explicitly hand off.
- **Use when:** output could naturally expand into multiple files, matrices, prompts, or patches.
- **Failure prevented:** multi-output compression, hidden omissions, and context bloat.

### Safeguard D — Verification gate

- **Rule:** A result is not trusted until verified by read-back, diff, file state, checklist, evidence, or test.
- **Use when:** result will be reused, committed, handed off, or treated as a base for later work.
- **Failure prevented:** phantom verification and fluent false completion.

### Safeguard E — Out-of-mode capture

- **Rule:** Detection is allowed; out-of-mode execution is not.
- **Use when:** the agent sees a high-value improvement outside the current task.
- **Failure prevented:** scope widening disguised as helpful improvement.

### Safeguard F — Handoff reset

- **Rule:** Handoffs must include settled state, source priority, do-not-redo list, exact next action, risks, and success condition.
- **Use when:** moving to a new chat, new agent, or Codex execution lane.
- **Failure prevented:** re-litigation, lost context, and stale assumptions.

## Evidence boundary

- **Decision:** Failure evidence can justify scaffold safeguards.
- **Constraint:** Failure evidence does not by itself create governance authority.
- **Constraint:** Do not overgeneralize one incident into universal doctrine unless supported by convergence across prompt, workflow, source-authority, and execution sources.

## Appendix-to-scaffold pointers

- `ESSENCE.md` should include only the highest-compression doctrine.
- `BEST_PRACTICES.md` should include accepted safeguards as compact rules.
- `MISTAKES.md` should include reusable failure pattern/countermeasure pairs.
- `TEMPLATES.md` should operationalize safeguards in reusable prompt bodies.
- `LEARNING_QUEUE.md` should hold unvalidated anti-drift variants only.
