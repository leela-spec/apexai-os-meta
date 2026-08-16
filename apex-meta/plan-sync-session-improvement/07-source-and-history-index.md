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

## Evidence copied into this folder

| File | Source | Purpose |
|---|---|---|
| `01-original-validation-handover.okf.md` | original main handover | proposal + validation mission |
| `02-independent-validation-report.md` | validation branch | live-contract analysis, failure modes, recommendation |
| `03-gate-policy-simulation.py` | validation branch | reproducible pressure-test logic |
| `04-simulation-results.txt` | validation branch | raw scenario results |
| `05-external-web-benchmark.md` | validation branch | external production-pattern + skill/web-search benchmark |
| `06-operator-decisions-and-current-direction.md` | current conversation synthesis | operator-validated A1′/B1/C1 direction |
| `00-START-HERE.md` | current conversation synthesis | durable restart/control index |

## Live Apex contracts inspected during validation

The validation explicitly inspected or traced the following current contract surfaces:

- `.claude/skills/apex-plan/SKILL.md`
- `.claude/skills/apex-plan/references/task-record-contract.md`
- `.claude/skills/apex-session/SKILL.md`
- `.claude/skills/apex-session/references/mutation-gate-rules.md`
- `.claude/skills/apex-session/references/state-delta-and-entity-rules.md`
- `.claude/skills/apex-sync/SKILL.md`
- `.claude/skills/weekly-orchestrator/SKILL.md`
- `.claude/skills/weekly-orchestrator/references/handoff-schema.md`
- `.claude/skills/weekly-orchestrator/references/review-wiring.md`
- `.claude/skills/status-merge/SKILL.md`
- `.claude/agents/apex-flow-recap.md`
- `.claude/agents/apex-status-merge.md`

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

## Conversation decision provenance

Sequence:

1. Operator requested independent detective/orchestrator review with simulations and no unilateral high-impact decisions.
2. Independent validation recommended **A1 + B1 + C1**.
3. Operator explicitly responded **`validated`**.
4. Operator then requested an additional web search because AI can hallucinate and required orientation on working internet examples and workflow/web-search/skill-design best practices.
5. External benchmark strengthened A1 and refined it to **A1′ — commit-time action authorization**; B1 and C1 remained unchanged.
6. Operator then requested this canonical repository folder so the research, decision process, and outputs would not be lost.

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
- Add new dated reports when evidence changes.
- Mark decisions as superseded explicitly rather than editing history invisibly.
- Production skill files remain their own live authority until the validated redesign is actually implemented.
