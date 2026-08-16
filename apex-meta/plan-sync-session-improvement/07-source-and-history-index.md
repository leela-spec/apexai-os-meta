# Source and History Index

Date: 2026-08-16
Canonical project folder: `apex-meta/plan-sync-session-improvement/`

## Repository history

### Original independent-validation handover

- Original path: `apex-meta/handoff/apex-gate-policy-skill-redesign-validation-handover-20260816.okf.md`
- Commit: `76b5ae2af1a6eb41f837958fe7f4740d5f9df383`
- Role: captures the original one-gate / risk-based authorization proposal, the double-gate concern, required validation scenarios, affected contract surfaces, and explicit instruction not to implement blindly.
- Canonical-folder snapshot: `01-original-validation-handover.okf.md`

### Real W34 trace that reproduced the duplicate confirmation

- Session mutation preview commit: `8748fcd6c455832bd01e66382f61502c6ff01a24`
- Canonical project/task creation commit: `cdcb6bd282547238f819881cfc58185c6f30ed09`
- Session handoff/planning-feed refresh commit: `ba1af5d791f0b62104b90454c6a34d01f0f30343`
- Later Sync local-execution packet / main base observed during validation: `d2f9d1d82bcfea6a11a16f48d9271f83f7591376`

Key reproduction:

1. Plan proposal set already had operator approval.
2. Session generated an exact serialization preview whose source basis included that approval.
3. Session still required explicit operator confirmation of the exact preview under the current contract.
4. Only after the second confirmation were nine epics / 54 tasks canonicalized.

### Independent validation branch

- Branch: `validation/gate-policy-20260816`
- Purpose: isolate research/simulation from production contracts during validation.
- Important commits:
  - `258bb5fd607ccf3ffaa58cf380891709e70a5cc6` — pressure-test simulator
  - `440965ba8b6da65248fedd9a3b3b8c39c0d3859a` — simulation results
  - `1053a20e49df08ba32a46766127f747c2ce283f8` — independent validation report
  - `fad50a0c6d9aa4f7c99e7dab8f68a8a0359332f1` — external web benchmark

The branch remains historical evidence. The canonical project copies now live in this folder on `main`.

### Canonical-folder consolidation on main

- `2b40dd740336ce85b2af61df9e714c6cec6842ee` — start Plan / Sync / Session improvement folder
- `e37e1d77d3f2dab1d56872be5efd2d38dd4620c8` — record operator decisions/current direction
- `11fe18e349f196ca25fbca0c2db9d8e85c85c916` — create source/history index
- `e9d6521b8788773957ba58626d211eb18db0c1fd` — snapshot original validation handover
- `2f39753d2ee32d83314136bbe3490583d22e01bd` — snapshot pressure-test simulator
- `423e4251c7c7081b9a4c85462c8597a09459b0d6` — snapshot simulation results
- `26a9198830955df024cdaa291915c050aebde50f` — snapshot independent validation report
- `1e31571e8513e5588a5d79fb269495cd0ddbc44f` — snapshot external web benchmark

### Contract / eval / carrier-spike sequence on main

This sequence was intentionally committed incrementally so each step remains independently inspectable and recoverable:

- `11ba7b54bd27d3b5a72a9d06638938b0f331c6cc` — draft minimal commit-time authorization contract (`08`)
- `a569b9dcb194a1851802dce3d39301012e15315b` — define authorization regression and duration eval matrix (`09`)
- `b9f0c9a56a6148747a52a7a5a45956adbd403520` — add executable minimal authorization carrier spike (`10`)
- `db67ddc583c2add9ddd584b74b89b089474fd678` — save carrier-spike results (`11`)
- `f925e3cf23cd06e206a5f5bc9911e452991a20aa` — record carrier-spike verdict and compatibility map (`12`)
- `5c1152eea090c0c9006f24d55fd23e18e98d71c3` — advance restart point
- `8b6aa657236ad29dc10f50ce39ef2487cf8225be` — record remaining P1/W1 decision boundary

### Local coding handover sequence

- `26969e9c9171ed3d8eb1fc88fbbe90c102f4fb93` — add precise OKR-oriented local coding/implementation handover (`13`)
- `488a51548c2962097331b4c867a265de44e8ce81` — index `13` in `00-START-HERE.md` and make it the local coding restart point

## Canonical folder inventory and role

| File | Source | Purpose |
|---|---|---|
| `00-START-HERE.md` | canonical synthesis | durable restart/control index; points local coding sessions to `13` |
| `01-original-validation-handover.okf.md` | original main handover | proposal + independent-validation mission |
| `02-independent-validation-report.md` | validation branch | live-contract analysis, failure modes, recommendation |
| `03-gate-policy-simulation.py` | validation branch | reproducible first pressure-test logic |
| `04-simulation-results.txt` | validation branch | raw first pressure-test results |
| `05-external-web-benchmark.md` | validation branch | external production-pattern + skill/web-search benchmark |
| `06-operator-decisions-and-current-direction.md` | canonical synthesis | operator-validated A1′/B1/C1 direction + remaining P1/W1 boundary |
| `07-source-and-history-index.md` | canonical synthesis | source paths, commits, evidence/history map |
| `08-authorization-policy-contract-draft.md` | design spike | minimal A1′ witness and commit-time validation contract |
| `09-authorization-eval-matrix.md` | design spike | lifecycle/duration, safety, automation, complexity, R01-R30 eval contract |
| `10-carrier-spike.py` | executable design spike | models Plan / Weekly / Session / Sync carrier and commit-time policy behavior |
| `11-carrier-spike-results.txt` | executable design spike output | raw `17/17`, zero unsafe/overblock, zero repeated-gate result |
| `12-carrier-spike-verdict-and-compatibility-map.md` | design-spike synthesis | minimum carrier surface, no-subsystem conclusion, writer ambiguity, P1/W1 decision |
| `13-local-code-implementation-handover.okr.md` | local implementation handover | precise local procedure, OKR objectives, locked/pending decisions, anti-drift rules, edit surface, metrics, handback contract |

## Live Apex contracts inspected during validation / required before production edits

The validation explicitly inspected or traced the following contract surfaces; the local coding agent must re-read their current versions before editing:

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-plan/references/task-record-contract.md`
- `.claude/skills/apex-session/SKILL.md`
- `.claude/skills/apex-session/references/mutation-gate-rules.md`
- `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`
- `.claude/skills/Workflow&Processes/operator-validation-and-conflict-resolution.md`
- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/weekly-orchestrator/references/review-wiring.md`
- `.claude/skills/apex-status-merge/SKILL.md` or the current status-merge skill path if renamed
- `.claude/agents/apex-flow-recap.md`
- `.claude/agents/apex-status-merge.md`

Do not assume that a validation-era path or contract is still current merely because it existed earlier. If a path has moved, locate the current authority and record the mapping.

## Concrete repository examples used in reasoning

### ApexKB decision task

`apex-meta/epics/apex-kb-evolution/006.md`

Used to demonstrate that **persisting a task record** and **making the future human decision described by that task** are different actions with different authorization requirements.

### Business invoicing task

`apex-meta/epics/business-invoicing/001.md`

Used to demonstrate that it can be safe to persist an approved task while **actually sending the invoice** remains a separate external consequential action.

## External production-pattern benchmark sources

The external validation intentionally preferred primary/official sources and inspected current patterns from:

- OpenAI Agents SDK human-in-the-loop approvals and tool guardrails;
- LangGraph interrupts / human-in-the-loop durable checkpoints;
- Temporal durable workflows and idempotent Activities;
- GitHub Actions protected environments / deployment approval boundaries;
- Claude Code permission rules / hooks / permission modes;
- Anthropic Agent Skills progressive-disclosure / deterministic-script guidance;
- current OpenAI / Anthropic web-search tooling patterns;
- recent primary research on commit-time authorization.

Exact URLs and observations are preserved in `05-external-web-benchmark.md`.

## Conversation / operator decision provenance

Sequence:

1. Operator requested independent detective/orchestrator review with simulations and no unilateral high-impact decisions.
2. Independent validation recommended **A1 + B1 + C1**.
3. Operator explicitly responded **`validated`**.
4. Operator then requested an additional web search because AI can hallucinate and required orientation on working internet examples and workflow/web-search/skill-design best practices.
5. External benchmark strengthened A1 and refined it to **A1′ — commit-time action authorization**; B1 and C1 remained unchanged.
6. Operator requested a canonical repository folder so research, decision process, and outputs would not be lost.
7. Operator requested the next engineering step: compact authorization contract, duration/lifecycle eval metrics, and a Plan/Weekly/Session carrier spike that avoids a large subsystem.
8. That engineering step completed on `main` with an executable spike and compatibility map. It deliberately left **P1** (Session-local policy home) and **W1** (clarify existing durable writer boundary) as recommendations rather than silently operator-approved decisions.
9. Operator then requested a precise handover for local code execution, indexed from the canonical folder and resilient against drift/over-engineering. This became `13-local-code-implementation-handover.okr.md`.

## Missing-source note retained from validation

The original handover claimed a fuller operator-saved project source could be located by phrases such as:

- `one semantic approval gate`
- `authorization envelope`
- `The operator approves authority, not individual writes`
- `default_gate: exception_only`

Repository search at validation time found those phrases only in the handover itself. The independent validation therefore treated that fuller source as **unverified/missing** rather than inventing its contents.

If that source is later located, compare it explicitly against this folder and record any differences as new evidence. Do not silently rewrite the existing record.

## Preservation / supersession rule

This folder is a historical + current decision record.

- Preserve raw simulation results and earlier reports.
- Add new dated/numbered reports when evidence changes.
- Mark decisions as superseded explicitly rather than editing history invisibly.
- Production skill files remain their own live authority until the validated redesign is actually implemented.
- Local coding sessions should begin at `00-START-HERE.md`, then use `13-local-code-implementation-handover.okr.md` as the execution handover.
