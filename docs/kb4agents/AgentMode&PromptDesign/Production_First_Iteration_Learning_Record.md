# Production-First Iteration Learning Record

## 1. Core learning

For subscription-browser Agent Mode runs, prompt design must make the **requested target artifact impossible to miss**. When the user asks for files, KB updates, or unified diffs, the first successful run must produce those files or diffs directly. Validation, plausibility review, source-risk analysis, and second-pass research should happen **after** a concrete artifact exists.

The failed runs show a repeatable anti-pattern: sophisticated guardrails, source gates, ledgers, and control artifacts can crowd out the actual deliverable. This is especially dangerous in Agent Mode because the agent executes the described task literally. If the prompt emphasizes control infrastructure, the output will become control infrastructure.

## 2. Evidence from failed runs

| Evidence | What happened | Why it matters | Impact |
|---|---|---|---|
| Prompt objective mismatch | The prompt selected `RUN_BATCH: 0_CONTROL` and required scope contracts, source ledgers, claim caches, manifests, validation reports, and group-control files. | The user wanted one agent’s existing files read and patched, not a system-control batch. | The run optimized for pre-analysis and governance instead of the five target KB files. |
| Control artifacts substituted for production | The run produced the visible control artifact set and candidate group files, but not the intended one-agent/five-file repair. | Completeness looked high while the actual target remained untouched. | False progress; additional iteration required before any real KB repair. |
| Validation theater | Acceptance tests were defined but not run; `git apply --check` was not executed; the patch was not trustworthy. | A validation checklist without execution is not validation. | The output could not be promoted or applied safely. |
| Source-gate paralysis | Missing or mishandled primary sources caused the run to mark agents blocked and create manifest/audit status corrections rather than produce target-file diffs. | Source limits matter, but they should be represented inside the target artifact when possible. | Source control became the product; production stopped. |
| Iteration not operationalized | “Iterative” was described, but the run continued through in one go instead of stopping at explicit checkpoints. | Agent Mode does not infer staged continuation unless commanded to stop. | User lost steering control and got another all-at-once output. |
| Guardrail overweighting | The prompt had many “do not” and stop rules, but weaker positive production instructions. | Guardrails should bound production, not replace it. | The agent avoided risk by generating meta-work rather than the requested artifact. |

## 3. New doctrine

**Production-first iteration is the default for file, patch, KB, prompt, and workflow creation tasks.**

A run is successful only when the requested artifact exists. For a KB update, this means the updated file body or unified diff exists. For an Agent Mode patch run, this means the target diff exists and has been checked. A recommendation, audit, scope contract, source ledger, or “next action” is not a substitute for the target artifact.

Use guardrails as constraints around production, not as the deliverable. Source gaps, uncertainty, and risk should be encoded as bounded caveats inside the produced artifact or in a compact post-artifact validation section.

## 4. Anti-pattern to reject

Reject the **governance-first prompt**:

1. define broad control scope;
2. create source ledgers and claim caches;
3. create acceptance tests;
4. create audit reports;
5. mark blockers;
6. recommend another run;
7. never produce the requested file or diff.

This pattern is high-risk even when it sounds rigorous. It converts production work into an endless pre-analysis loop.

## 5. Positive operating pattern

Use the **produce → validate → improve → document learning** loop.

1. **Produce:** Create the requested file, five-file KB update, or unified diff first.
2. **Validate:** Check the produced artifact for scope, patchability, source fit, risk, and plausibility.
3. **Improve:** Produce a second-pass targeted patch only if validation finds concrete defects.
4. **Document learning:** Promote the rule only after a real artifact exists and has been reviewed.

For Agent Mode subscription-browser runs, define one unit of work per run: **one agent, one folder, one file group, or one diff**. If iteration is required, force it with explicit stop commands: “Stop after this artifact and wait for `CONTINUE`.”

## 6. Risk / evidence / impact classification

| Claim | Evidence strength | Impact | Risk if adopted | Risk if ignored | Verdict |
|---|---:|---:|---:|---:|---|
| File/diff tasks should produce the artifact before broad validation. | 5/5 | 5/5 | 2/5 — may produce an imperfect draft, but it can be validated. | 5/5 — likely repeats pre-analysis loops. | Adopt as default. |
| Guardrails must be subordinate to the concrete deliverable. | 5/5 | 5/5 | 2/5 — requires disciplined scope wording. | 5/5 — guardrails become the output. | Adopt as prompt-design rule. |
| Source gaps should not automatically trigger control-batch mode. | 4/5 | 5/5 | 3/5 — weak claims must be clearly marked. | 5/5 — production stops and ledgers multiply. | Adopt with source-limit caveats. |
| Iteration must include explicit stop points. | 5/5 | 4/5 | 1/5 — slower but controllable. | 4/5 — Agent Mode runs through in one pass. | Adopt for all multi-step Agent Mode runs. |
| Acceptance tests must be executed, not merely authored. | 5/5 | 5/5 | 1/5 — adds minimal effort after artifact exists. | 5/5 — validation theater repeats. | Adopt as QA rule. |

## 7. Integration targets

| Target KB/playbook file | Exact doctrine to add | Priority |
|---|---|---|
| `GPT_Agent_Mode_Business_Playbook.md` | Add a production-first Agent Mode section: when the deliverable is a file/diff, first produce the artifact; forbid control-artifact substitution; require explicit stop points. | P1 |
| Prompt Design agent `BEST_PRACTICES.md` | Add rule: prompts must foreground the target artifact and keep guardrails subordinate to output delivery. | P1 |
| Prompt Design agent `MISTAKES_FAILURES.md` | Add anti-patterns: governance-first prompt, ledger-as-output drift, source-gate paralysis, validation theater, recommended-next-action substitution. | P1 |
| Workflow / Process agent `BEST_PRACTICES.md` | Add default loop: produce → validate → improve → document learning. | P1 |
| Workflow / Process agent `ESSENCE.md` | Compress the doctrine into: “artifact first, validation second, learning third.” | P2 |
| `QA_HYGIENE_PROTOCOL.md` | Add QA distinction: validation checks an existing artifact; a checklist without execution is not validation. | P2 |
| `PROJECT_ROUTING.md` | Add routing rule: file/diff requests route to production mode, not audit/control mode, unless the user explicitly asks for audit. | P2 |

## 8. Promotion rule

Promote this learning as a high-evidence, high-impact, low-to-medium-risk operating doctrine for subscription-browser Agent Mode and KB-update workflows.

Promotion condition:

- at least one playbook patch and one agent-KB patch encode the doctrine;
- future Agent Mode prompts use one concrete target unit per run;
- validation happens after the artifact exists;
- no run is marked complete when it only returns a plan, ledger, audit, or recommended next action instead of the requested file/diff.
