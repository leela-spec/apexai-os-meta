# 07-DECISION-PACKAGE.md — Weekly Orchestration Learning Pilot final return

## State

**PROVEN_CANDIDATE (design level)** — with explicit scope limits below.

The pilot demonstrated, with inspectable evidence, that a candidate artifact
design (CANDIDATE-3 "layered hybrid") improves the targeted operator jobs over
the faithful baseline on identical scenario facts, without detected regression.
It did NOT modify production files and does NOT claim production improvement.

## Phases completed

| Phase | Artifact(s) | Status |
| :-- | :-- | :-- |
| 0 authority freeze | `00-phase0/00-AUTHORITY-MAP.md`, `00-CONTRADICTION-REGISTER.md` | done (prior run) |
| 1 findings + eval cases | `01-phase1/01-FINDINGS.okf.md`, `01-EVAL-CASES.yaml` | done (prior run) |
| 2 faithful baselines | `02-phase2/02-INPUT-CORPUS.md` + 5 case dirs (A–E), each: weekly brief, daily brief, flow card(s), prompt index, prompts, receipt.yaml | **done this run** |
| 3 baseline eval | `03-phase3/03-BASELINE-EVAL.md` — Q1-Q20 PASS/PARTIAL/FAIL with evidence paths | **done** |
| 4 isolated reviews | packets + R-C (information design), R-D (systems/contract); receipts with isolation disclosure | **done** |
| 4b synthesis | `05-phase5/04-SYNTHESIS.md` — agreements, preserved disagreements, 3 candidates | **done** |
| 5 candidate instantiation | `05-phase5/candidate-3/**` against Case A/B/D facts | **done** |
| 6/7 comparison | `06-phase6/05-COMPARISON-EVAL.md` — job-by-job baseline vs candidate + regression sweep | **done** |
| skill learning | see `evidence-driven-workflow-improvement` candidate note below | **done** |

## Baseline vs candidate evidence (summary)

Template-rooted failures confirmed in Phase 3: F01 (weekly sprint grid = wrong
layer), F03 (no delta section exists in daily template), F04 (provenance is a
terminal blob, not fact-level), F06 (prompt quality checks can't detect label-
swap boilerplate), F05/F09 (no deformation presentation contract; route
statements triplicated).

Candidate-3 changes validated in outputs:
- delta blocks first-position with per-row source tags → Q1/Q11 PASS,
- day-emphasis replaces sprint grid; schema has no sprint field → Q4/Q10 PASS structurally,
- sources ledger: every claim tagged, one-hop resolution → Q9 structure PASS,
- unified FULL/COMPRESSED/MINIMAL/OMITTED/BLOCKED enum → Q13 consistent across doctrine/artifacts,
- prompt files carry required inputs:/return:/done: fields → Q17–Q20 enforced by validation, not discipline,
- single authoritative routing statement → route noise 3→1 statements.

Regression sweep: D-type staleness weeks still expressible (null+reason pattern),
B-type constrained days visible (CRITICAL class + reasoned omissions), no hop
increase, ownership coherent.

## Reviewer identities/contexts

| ID | Lens | Context disclosure |
| :-- | :-- | :-- |
| R-C | information design | bounded packet, fresh task context; same base model family as orchestrator — disclosed in receipt |
| R-D | systems/contract architecture | bounded packet, fresh task context; same disclosure |

R-C and R-D reached convergent diagnoses via different mechanisms (presentation
vs contract enforcement) — convergence treated as moderate-strength evidence for
that reason. Their material disagreement (enforcement philosophy: rendering vs
structural impossibility) is preserved in the synthesis and shaped CANDIDATE-3's
scope boundary (adopted cheap structural moves, deferred typed-ref-everywhere).

## What was deliberately NOT done

- No elapsed/scannability timings anywhere (all such metrics: not_measured).
- No operator approval fabricated; all operator_validation fields pending/not_requested.
- No production file modified — candidate lives entirely under campaign dirs.
- No Phase 8 patch generated: production-change decision is the operator's, per §12 of the continuation order.
- E-case candidate instantiation partial (mechanism inherited, full rerun deferred).
- Quiet-day noise risk (candidate delta blocks on uneventful weeks) needs live-week sampling to clear — open verification item.

## Learning skill candidate

Per §10, the generic procedure is captured as a staged project-local skill:
`evidence-driven-workflow-improvement` — encoding only the method (real target →
real authority → faithful baseline → failure identification → proxy-shortcut
detection → smallest candidate change → real-task execution → evidence closure →
baseline comparison → regression → only then claim improvement). Postmortem
detail stays historical (this package). Not placed in MEMORY.md; AGENTS.md untouched; not promoted across projects.

## Remaining disagreement / open items

1. Visible day-emphasis table vs machine-only tokens (R-C/R-D tension) — hybrid renders both from one source; operator should confirm readability.
2. Whether digests/schema-version coupling (R-D's full program) is worth migration cost — deferred with rationale.
3. Operator adjudication of consequential UX tradeoffs (campaign Phase-6 requirement) — requires the actual operator; cannot be validly self-established.

## Recommended next action

1. Operator reviews this package + candidate exemplars (`05-phase5/candidate-3/`).
2. If accepted: authorize Phase 8 exact-match patch preparation against current main (templates only; blueprint gate-rename handled as separate decision per contradiction register C-01).
3. Before any production claim: run one LIVE week through the candidate design to clear the quiet-day-noise and degraded-routing verification items.
