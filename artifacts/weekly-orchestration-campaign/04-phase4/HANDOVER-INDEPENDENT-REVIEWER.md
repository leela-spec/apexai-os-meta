# HANDOVER — Independent Reviewer Assignment
## Weekly Orchestration Eval-Driven Improvement Campaign

> **You are being engaged as an external, independent reviewer** for Phase 4 of
> this campaign. You did NOT generate the material you will review, you have no
> stake in its scores, and your output feeds a blind comparison later. This
> document contains everything you need. Read it fully before writing anything.

---

## 1. Engagement facts

| Field | Value |
| :-- | :-- |
| Repository | `leela-spec/apexai-os-meta` (branch `main`) |
| Campaign root | `artifacts/weekly-orchestration-campaign/` |
| Campaign phases completed | 0 (authority freeze), 1 (findings + eval cases) |
| Your phase | 4 — Independent Divergent Design review |
| Your output directory | `artifacts/weekly-orchestration-campaign/04-phase4/reviewers/<YOUR-REVIEWER-ID>/` |
| Contact for questions | Return questions via a `QUESTIONS.md` file in your output directory; do not modify anything outside it |

## 2. What this system is (60-second orientation)

APEX OS runs a **Weekly Orchestrator loop**: a weekly planning stage produces a
*Weekly Command Brief* (PrecapWeek skill), a daily planning stage produces a
*PreCap Next Day Brief* + *Flow Execution Cards* + *sprint prompt files*
(PrecapNextDay skill), the operator executes, evidence flows back through recap
and status-merge stages, and a control-plane skill (`weekly-orchestrator`)
holds five stage gates (loop-G1…G5) and routes durable mutations.

One human operator ("the operator") consumes these artifacts every week to
decide, execute, and resume work. The campaign's goal: make those artifacts
genuinely better at the operator's actual jobs — not prettier, not smaller,
not higher-scoring.

## 3. Required reading (in order)

All paths relative to repo root. Read fully:

1. `artifacts/weekly-orchestration-campaign/00-phase0/00-AUTHORITY-MAP.md`
   — which file owns which semantics. Note the G1–G5 disambiguation rule.
2. `artifacts/weekly-orchestration-campaign/00-phase0/00-CONTRADICTION-REGISTER.md`
   — especially C-01 (three-way gate collision) and C-04 (your independence definition).
3. `artifacts/weekly-orchestration-campaign/01-phase1/01-FINDINGS.okf.md`
   — the ten findings F01–F10 with verbatim evidence. **Your review must anchor
   on these findings**, not invent its own problem statement.
4. `artifacts/weekly-orchestration-campaign/01-phase1/01-EVAL-CASES.yaml`
   — the operator tasks Q1–Q20 you will evaluate against.
5. The production templates themselves:
   - `.claude/skills/PrecapWeek/weekly-command-brief-template.md`
   - `.claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md`
   - `.claude/skills/PrecapNextDay/templates/flow-execution-card-template.md`
   - `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md`

## 4. Baseline artifacts you will review

The frozen baseline lives at:

```
artifacts/weekly-orchestration-campaign/02-phase2/
```

with scenario classes:

| Class | Scenario | Directory pattern |
| :-- | :-- | :-- |
| A | normal week | `02-BASELINE/case-A-normal-week/` |
| B | meeting-heavy/constrained week | `02-BASELINE/case-B-constrained-week/` |
| C | deadline vs high-impact conflict | `02-BASELINE/case-C-dependency-conflict/` |
| D | stale/missing source state | `02-BASELINE/case-D-stale-state/` |
| E | usage-scarcity/routing degradation | `02-BASELINE/case-E-usage-scarcity/` |

Each case directory contains the full artifacts production would emit, plus a
`receipt.yaml` (inputs supplied, provenance, model/profile, tool access,
budgets, validation results).

**Precondition:** if `02-phase2/` does not yet contain the case you were told
to review, STOP and write `QUESTIONS.md` saying so. Do not reconstruct
baselines yourself and do not review simulated material from
`apex-meta/orchestration/simulation/` as if it were the baseline — that corpus
is evidence of failures (see findings), not review input.

## 5. Your reviewer lens

You have been assigned ONE lens (stated in the dispatch message that pointed
you here). If no lens was stated, ask via `QUESTIONS.md` — do not pick one
yourself and do not cover all four.

| ID | Lens | Focus |
| :-- | :-- | :-- |
| R-A | BMAD UX workflow | If a BMAD installation is available to you, invoke its actual UX workflow and produce its native outputs. Otherwise declare that plainly in your output header and proceed with explicit UX-method annotation of what you did instead. Operator tasks, navigation, interaction boundaries. |
| R-B | Marketing/CRO skills | Use installed marketing skills if present (declare which). CRO principles for 5-second state/action clarity and friction; information/site-architecture principles for artifact hierarchy. This is an internal control system — do NOT turn it into marketing copy. |
| R-C | Information design | Hierarchy, matrices, comparison structures, progressive disclosure, information density, exception visibility. |
| R-D | Systems/contract architecture | Authority, provenance, duplication, state ownership, handoffs, weekly-vs-daily boundary integrity. |

## 6. Independence rules (binding)

Per contradiction-register C-04 and campaign hard prohibitions:

1. Run in **your own fresh context**. Do not read any other reviewer's output.
   Other reviewers' directories are off-limits (`04-phase4/reviewers/*` except yours).
2. Work only from: required reading (§3), the frozen baseline (§4), and the
   operator-task definitions (§7).
3. Do not read this campaign's chat transcript or session history — none exists for you.
4. **No fabricated measurements.** You may not invent elapsed/scannability times.
   If you measure something, record subject, method, and raw observations. If
   you cannot measure, write `not_measured`.
5. **Label yourself accurately.** State in your output header: reviewer id,
   lens, date, the context/tool you actually ran in, and whether the run was
   isolated per rule 1. An unisolated run must be labeled non-independent.
6. Scores alone are insufficient and may be omitted entirely. Evidence and
   reasoning are mandatory; numbers are optional decoration at best.

## 7. The operator jobs you evaluate against

From `01-EVAL-CASES.yaml` — answer-ability of real tasks, not aesthetics:

Weekly Command Brief: Q1 what changed vs last week · Q2 top 2–4 outcomes ·
Q3 why now · Q4 what Monday advances · Q5 where capacity is constrained ·
Q6 blocked/deferred · Q7 decision needing operator input · Q8 confirmed vs
assumed · Q9 provenance of each consequential fact · Q10 what belongs to the
daily layer instead.

Daily Brief: Q11 what changed since weekly plan/yesterday · Q12 execution order
and why · Q13 flows compressed/blocked/omitted · Q14 exact next operator action ·
Q15 where sprint detail lives.

Flow/Prompt: Q16 worker self-sufficiency without reopening portfolio · Q17
task-specific prompt inputs · Q18 concrete expected output · Q19 concrete
done/stop/evidence conditions · Q20 S1/S2/S3 semantically distinct, not renamed
boilerplate.

## 8. Required output (all six-plus-one, in one file or a small set)

Write to `artifacts/weekly-orchestration-campaign/04-phase4/reviewers/<YOUR-ID>/review.md`:

1. **Diagnosed root causes** — tied to finding IDs (F01–F10); if you diagnose
   something new, give it an ID in your own namespace (`<YOUR-ID>-N1…`).
2. **Proposed information architecture** — how the artifact family should be
   structured; name the layer that owns each block.
3. **A concrete redesigned artifact example** — take ONE representative
   baseline artifact and show the redesign with realistic content, same
   underlying facts. Full fidelity, not a sketch of a sketch.
4. **What should be removed** — with the finding each removal serves.
5. **What should move to another layer** — source layer → target layer → why.
6. **Expected measurable improvement** — expressed as which eval cases
   (W-Q*/D-Q*/P-Q*) should improve and WHY the design change causes that
   improvement. No invented percentages or seconds; predictions must be
   mechanism-based.
7. **Risks/regressions** — what could get worse, which operator jobs might
   degrade, and how you would detect it.

Also include the header block from §6 rule 5 and a `receipt.yaml`:
tools/access you used, files read (paths list), and your isolation declaration.

## 9. Hard prohibitions (mirror of campaign rules)

- No fabricated operator approvals or confirmations.
- No fabricated elapsed/scannability times.
- No claiming independence you don't have.
- No declaring anything improved from its own self-score.
- No mutating production files (`.claude/skills/**`, templates, SKILL.md files)
  or any campaign file outside your output directory.
- A patch proposal is NOT part of your job — you propose designs; application
  happens only through the campaign's later operator-approved patch phase.

## 10. Completion checklist

- [ ] All §3 reading done
- [ ] Correct baseline case set reviewed (§4 precondition satisfied)
- [ ] Output covers items 1–7 of §8
- [ ] Every claim anchored to a finding id or your own named diagnosis
- [ ] Header + receipt present; isolation declared truthfully
- [ ] Nothing outside `04-phase4/reviewers/<YOUR-ID>/` modified
- [ ] `QUESTIONS.md` written if anything above blocked you

When done, commit only your directory with message
`docs(campaign): independent reviewer <YOUR-ID> (<LENS>) phase-4 review`
and push. The campaign orchestrator handles everything after that.
