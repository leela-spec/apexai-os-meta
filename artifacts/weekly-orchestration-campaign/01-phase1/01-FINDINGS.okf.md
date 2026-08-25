# 01-FINDINGS — Weekly Orchestration Failure/Eval Corpus

> Format: OKF-style finding records. Every finding is grounded in observed
> evidence from (a) the live production skills/templates on `main` and (b) the
> materialized two-week orchestration simulation under
> `apex-meta/orchestration/simulation/` — which is treated strictly as a
> **corpus of observed outputs**, never as design authority.
>
> Evidence timestamps refer to file states read during Phase 0/1 of this
> campaign (repo HEAD post-`6c8ab225`, branch `main`).

---

## F01 · Weekly artifact contains daily sprint-detail leakage

- **finding_id:** F01
- **actual evidence:**
  - Production template `.claude/skills/PrecapWeek/weekly-command-brief-template.md` (`04ed2662`), Matrix 2 rows embed per-day sprint goals: `• S1: {{F1_MON_S1_GOAL}} • S2: … • S3: …` for every flow × weekday (16 sprint-goal cells/day-grid).
  - PrecapWeek's own contract forbids this layer: `planning_scope.excluded: detailed_next_day_plan_creation`; `output_boundary.must_not_be: detailed_daily_plan`. The template violates the skill's own boundary by carrying S1–S3 granularity.
  - Simulation W1 brief Matrix 2 carries day-level task names ("Retrieval Architecture Draft", "Registry Candidate Audit") — 20 task cells duplicating what the daily layer must decide.
- **affected user job:** Q10 — operator scanning the weekly brief cannot tell what belongs to the weekly decision vs. what PrecapNextDay will own; weekly approval gets contaminated by sprint-level review the operator cannot meaningfully do yet.
- **affected production file:** `.claude/skills/PrecapWeek/weekly-command-brief-template.md`
- **severity:** HIGH
- **failure example:** Operator approving "the week" is shown 48+ sprint goal cells (4 flows × 5 days × ~2.4 sprints). Any change to one sprint forces re-review of the whole grid; the weekly decision surface and the daily plan compete for the same attention.
- **expected behavior:** The Weekly Command Brief expresses weekly targets, priorities, constraints, sequence, and a *directional* day emphasis only. Sprint-level goals appear first in the daily layer (Flow Execution Card / Next Day Brief).
- **objective or human-verifiable test:** Deterministic scan of a generated Weekly Command Brief: zero occurrences of sprint-level tokens (`S1:`/`S2:`/`S3:` or per-day task sentences) outside an explicitly marked directional-seed block; operator can answer Q1–Q7 from top-of-artifact sections alone.
- **regression risk:** Removing sprint cells could strip legitimate capacity signal (which project gets which day). Mitigation: keep a compact day×project emphasis marker without sprint decomposition; verify Q5 (capacity constrained) remains answerable.

## F02 · Weekly and daily artifacts duplicate information

- **finding_id:** F02
- **actual evidence:**
  - The sentence-level deliverable "4-Pillar Active Recall & Feynman Extraction Engine" appears verbatim in: simulation W1 Weekly Brief Matrix 1 + Matrix 2 Mon cell, Day-1 Next Day Brief priority table, Flow Card F1 outcome target/goals, and prompt `flow_prompt-f1-s1.md` Target Goal — ≥4 encounters to plan one day.
  - Daily briefs are byte-identical to each other apart from headers (diff of `week-01/day-mon/precap-next-day-brief-day1.md` vs `week-02/day-wed/…day3.md`: only title/date/gate lines), so the "daily" layer re-states the weekly matrix instead of adding day value.
  - Production ownership rule exists and is sound (PrecapWeek SKILL `downstream.transfer: reference_plus_minimal_seed`; PrecapNextDay boundary "Do not duplicate the full flow context across the Brief, a Flow Execution Card, and its prompt files"). Observed outputs violate it; nothing enforces it mechanically.
- **affected user job:** Q11/Q12 — operator rereads the same content in multiple artifacts to confirm the day actually advances the week, burning context budget per hop.
- **affected production files:** `templates/precap-next-day-brief-template.md` (flow summary blocks restating card content); `weekly-command-brief-template.md` (Matrix 2 overlap).
- **severity:** HIGH
- **failure example:** To answer "what is today's execution order and why," the operator meets the same deliverable text four times across three artifacts; none of the encounters states what is *new today* versus carried forward.
- **expected behavior:** Each fact lives at exactly one owning layer; other layers hold qualified references (tag + path). Duplicate-content ratio across weekly→daily→card→prompt approaches zero.
- **objective or human-verifiable test:** Deterministic n-gram/shingle comparison between a produced weekly brief, next-day brief, flow cards, and prompt files for the same day: duplicated non-boilerplate shingle count below threshold; reference hops resolve instead of restating.
- **regression risk:** Over-aggressive dedup could break standalone readability when an artifact is opened without its parents. Mitigation: allow one-line carry-forward summaries marked as references, verify Q16 still passes (worker can execute without reopening the portfolio).

## F03 · Daily artifacts fail to emphasize what changed

- **finding_id:** F03
- **actual evidence:**
  - `precap-next-day-brief-template.md` (`c96747e2`) has no delta/change section: closest is a single line `**Continuity from the week:**` and optional review flags. No field captures "changed since weekly plan / since yesterday."
  - Simulation daily briefs are identical across all 10 days except headings — no artifact ever surfaces a change even though the underlying Matrix 2 schedule nominally differs per day.
  - Flow Recap packets report "100% completed" for every flow every day, so the raw inputs for a delta exist but never reach the daily planning output.
- **affected user job:** Q11 ("what changed since the weekly plan / yesterday?") is unanswerable from the daily brief; operator must mentally diff artifacts.
- **affected production file:** `.claude/skills/PrecapNextDay/templates/precap-next-day-brief-template.md`
- **severity:** HIGH
- **failure example:** After Monday slips (flow blocked), Tuesday's brief looks exactly like Monday's; the operator discovers the slip only by noticing stale sprint statuses inside a flow card.
- **expected behavior:** The daily brief leads with an explicit delta block: changes vs. weekly plan and vs. previous day (newly blocked, compressed, deferred, completed, newly flagged), each with a reason and source reference.
- **objective or human-verifiable test:** Inject a known state change between day N and day N+1 inputs; deterministic check that the N+1 brief names the injected change in its delta block; human check that the delta appears above flow details in reading order.
- **regression risk:** Delta noise on quiet days. Mitigation: explicit "no changes since yesterday" state is a valid, short delta entry.

## F04 · Provenance/source authority is hard to see

- **finding_id:** F04
- **actual evidence:**
  - Grep for `provenance|Provenance` across simulation weekly brief, daily briefs, and all flow cards: **zero matches**. Artifacts assert facts ("60-indicator expansion verified", "zero fact bleed confirmed") with no source.
  - Production templates do have provenance sections (Weekly: `## Provenance and confidence` near the bottom; Card: bottom section), i.e., present-but-last — after ~130 lines in the weekly, ~180 in the card.
  - Simulation briefs' only sourcing is a small yaml `upstream_inputs` path list with no freshness, no confirmation status, no SHA.
- **affected user job:** Q9 ("where did each consequential planning fact come from?") requires scrolling to artifact end or is unanswerable; confirmed-vs-assumed (Q8) blurs.
- **affected production files:** all three brief/card templates (placement problem), plus downstream compliance in generated artifacts.
- **severity:** MEDIUM-HIGH
- **failure example:** Weekly brief states a capacity constraint that traces to a stale snapshot; the freshness note exists only in a bottom section the operator never reaches during a morning scan.
- **expected behavior:** Consequential facts carry inline source markers (ref tag resolving to one authority path + date/status); a compact source table sits at the top or beside the facts, not only at the tail.
- **objective or human-verifiable test:** For each consequential fact seeded into a baseline input, a tracer resolves a source within ≤1 hop from the fact's location; deterministic check that every fact class marked "decisive" in inputs appears with a source marker in the output.
- **regression risk:** Marker clutter. Mitigation: markers only on decisive facts; single-letter tags expanding in one source table.

## F05 · Constrained/meeting-heavy days are not clearly differentiated

- **finding_id:** F05
- **actual evidence:**
  - Simulation contains no meeting/capacity variation anywhere: `FreeT Allocation: AM 09:00–12:00 -> F1 & F4 · PM 14:00–17:00 -> F2, F3, F4.` is byte-identical across days and weeks (verified day-mon W1 vs day-wed W2).
  - Grep for `meeting|constrained` across W1 weekly brief and Wednesday daily artifacts: zero matches.
  - Production support exists but is opt-in prose: PrecapWeek has `calendar-planning-guidance.md` + `weekly-blueprint-meeting-example.md` ("meeting_heavy_day_needs_deformation"); the Weekly template reduces this to per-day `FreeT:/Meets:` header fragments inside Matrix 2 cells — easy to leave uniform, nothing validates differentiation.
  - PrecapNextDay has a `calendar_constrained_mode` execution mode, but the daily template has no dedicated constrained-day presentation (compressed/omitted flows appear only as generic status values).
- **affected user job:** Q5 (where is capacity constrained?) and Q13 (which flows were compressed/blocked/omitted?) get uniform-looking answers regardless of actual load; the operator misjudges what a heavy day can absorb.
- **affected production files:** `weekly-command-brief-template.md` (Matrix 2 day headers), `precap-next-day-brief-template.md` (capacity assumption line only).
- **severity:** MEDIUM-HIGH
- **failure example:** A Wednesday with 4 hours of meetings renders with the same shape as an open Monday; planned flows silently assume full capacity and fail mid-day.
- **expected behavior:** Capacity-constrained days visibly deform: available-hours budget stated, flows explicitly marked FULL/COMPRESSED/MINIMAL/OMITTED with the capacity reason adjacent, and the weekly grid highlighting the constrained day rather than hiding it in a cell fragment.
- **objective or human-verifiable test:** Baseline case B (meeting-heavy) vs case A (normal): deterministic check that constrained-day output differs structurally (status vocabulary + capacity statement present); operator answers Q5/Q13 correctly within the artifact without opening calendar sources.
- **regression risk:** None material; worst case verbose constraint notes on mildly loaded days.

## F06 · Prompt files can be formally unique while semantically generic

- **finding_id:** F06
- **actual evidence:**
  - All 60 simulated prompt bodies follow one skeleton; `flow_prompt-f1-s1.md` vs `-s2.md` differ ONLY in the words "Sprint 1"/"Sprint 2" (verified byte-comparison of bodies). Across five days, day-mon vs day-tue vs … fri `f1-s1` bodies are byte-identical.
  - Sprint labels are semantically empty: S1 "Scoping", S2 "Deep Formulation", S3 "Verification & Packaging" reused verbatim for a website-extraction flow, a curriculum flow, and a quant-engineering flow alike.
  - The production quality check (`prompt-files-and-index-template.md`) tests "task-specific inputs appear once" only as a checkbox; nothing measures semantic specificity.
- **affected user job:** Q17/Q18/Q20 — worker receives a prompt with no task-specific inputs; expected output is "complete production deliverable" (unbounded); S1/S2/S3 are renames, so sprint sequencing carries no information.
- **affected production file:** `.claude/skills/PrecapNextDay/templates/prompt-files-and-index-template.md` (quality-check insufficiency)
- **severity:** HIGH
- **failure example:** Dispatching F1-S2's prompt executes nothing meaningful: "Execute Sprint 2 … Output the complete, unedited production deliverable" fits any project any day; uniqueness checks pass while the corpus contains effectively 1 prompt, not 12 per day.
- **expected behavior:** Each sprint prompt binds concrete inputs (files/refs), a bounded expected return artifact, done/evidence conditions, and sprint-specific intent that differs semantically from sibling sprints (not just label swaps).
- **objective or human-verifiable test:** (a) Deterministic: body-similarity clustering over a produced prompt set — pairwise similarity below ceiling except shared scaffolding; required-field extraction (inputs/return/done-condition) must succeed per prompt. (b) Independent inspection: sampled prompts executed or reviewed against their own stated done-conditions (Phase 9 requirement).
- **regression risk:** Over-constraining prompts could push flow-plan detail INTO prompts (violating J4-ownership). Mitigation: pair the specificity test with the existing "does not duplicate J4 tasks" check.

## F07 · Simulated reviewer results self-certify without execution evidence

- **finding_id:** F07
- **actual evidence:**
  - `tri-agent-end-of-week-synthesis-w1.md` reports "Scannability: 68/42/**34 seconds**" and ratings 6.8/7.5/**9.2** with no methodology, no measurement subject, no instrument — the numbers originate inside the same generation context as the artifacts being rated.
  - `g1-checkpoint.yaml` records `scannability_seconds: 46` and `status: APPROVED` as if measured.
  - `acceptance-verdict.yaml` (W2 final): `scannability_improvement: -40.7%`, `verdict: FULL_PASS_COMPOUNDED` computed entirely from those unobserved numbers.
  - No human-time measurement record exists anywhere in the corpus; the "Experience Designer Audit"/"MarketingSkills Audit" lines live inside the very brief they approve.
- **affected user job:** Operator trust in gate checkpoints (Q8 confirmed-vs-assumed) collapses: APPROVED states cannot be distinguished from self-asserted ones.
- **affected production surface:** checkpoint/verdict practices around the loop (weekly-orchestrator's `operator_validation` discipline is correct; the simulation violated it — this finding governs campaign methodology AND future checkpoint hygiene).
- **severity:** CRITICAL (methodological)
- **failure example:** An improvement claim ("40% faster to scan") enters the decision package purely by being written down; later phases would optimize toward a fabricated baseline.
- **expected behavior:** Reviewer results cite execution evidence: who/what ran, in which isolated context, on which inputs, with what method. Elapsed-time claims require recorded human measurement with methodology. Self-scores are labeled non-evidence by default.
- **objective or human-verifiable test:** Every reviewer/scoring claim in campaign artifacts carries a receipt (context id, input hash, method) OR is explicitly marked unmeasured; grep-based audit finds zero bare "X seconds" claims without a measurement record.
- **regression risk:** Slower evaluation cadence. Accepted — prohibitions override speed.

## F08 · Improvement synthesis can drop critical reviewer findings

- **finding_id:** F08
- **actual evidence:**
  - `tri-agent-end-of-week-synthesis-w1.md` synthesizes three "audits" into Option-C-wins with zero preserved disagreement — three audits, three unanimous lines, no dissent channel.
  - Its Patch Pack proposes "trim token overhead by 21.5%" and "elevate Option C to the live standard" with no traceability to any specific diagnosed problem, and asserts "deterministic test suites passed 100% (204/204 IDs reconciled)" while no test artifacts exist anywhere under `simulation/week-0*/`.
  - The W1→W2 delta report tracks token/time metrics only; no reviewer finding is carried, satisfied, or dropped with a named reason.
- **affected user job:** Operator reviewing a synthesis cannot see which concerns were raised and which were silently discarded; improvements lose information exactly at the aggregation step.
- **affected production surface:** synthesis/aggregation step of the loop (weekly-orchestrator step 4: "present both verdicts; never tiebreak" — the practice shown here bypasses that discipline).
- **severity:** HIGH
- **failure example:** Reviewer B flags missing traceability in Option C (visible even in-corpus: Option B was penalized for exactly that); the synthesis drops the concern because the winner is declared on style scores — the flaw ships into "production standard".
- **expected behavior:** Synthesis enumerates every material reviewer finding with disposition: adopted (→ change id), rejected (→ named reason), or deferred (→ owner). Unresolved disagreements stay visible, never averaged away.
- **objective or human-verifiable test:** Given frozen reviewer outputs with N material findings, the synthesis account for all N (adopted/rejected/deferred) — deterministic completeness check against the finding registry; spot-check that no finding disappears without a recorded disposition.
- **regression risk:** Verbose synthesis. Acceptable; dispositions may be tabular.

## F09 · Usage/routing information becomes visual noise

- **finding_id:** F09
- **actual evidence:**
  - Routing metadata appears in triplicate around the same sprint: Flow Execution Card "Prompt access" block (surface + routing ref + readiness per sprint), Prompt Index table row (same three fields again), and each prompt file header (recommended surface + routing ref again) — three restatements of one route decision.
  - In simulation index tables, `Recommended surface: Hermes Worker | Use when: Execute Sprint N for FX` is pure boilerplate repeated 12×/day with zero routing information content.
  - PrecapNextDay's own output_requirements already forbid routing schemas inline ("Do not include routing, quota, planned-budget, or usage-delta schemas"), yet per-sprint route decoration survives in templates as noise.
- **affected user job:** During execution (Q14/Q16), the operator wades repeated routing badges to find the actual next action; genuinely degraded routes don't stand out because READY-state decoration is equally loud.
- **affected production files:** `flow-execution-card-template.md`, `prompt-files-and-index-template.md`.
- **severity:** MEDIUM
- **failure example:** A card shows six routing lines (two sprints × 3 fields) where one shared route line + exceptions-only flags would do; the operator's eye learns to skip "Routing reference" lines — including the one day a route is actually broken.
- **expected behavior:** Route stated once per flow (or per prompt-file pointer), with visibility reserved for exceptions (DEGRADED/MISSING/unapproved route); stable defaults render as a single low-emphasis line or collapse into the index.
- **objective or human-verifiable test:** Count routing-metadata occurrences per sprint across card+index+prompt file in produced artifacts (baseline vs candidate); exception-visibility check: injected DEGRADED prompt is located faster/more reliably than in baseline (operator-verifiable search task).
- **regression risk:** Hiding routing could strand offline execution needing surface info. Mitigation: keep one authoritative route line per prompt file; only remove duplication.

## F10 · Competing gate semantics cause control-plane drift

- **finding_id:** F10
- **actual evidence:**
  - Full collision documented in `00-phase0/00-CONTRADICTION-REGISTER.md` C-01: `weekly-orchestrator/SKILL.md` G1–G5 = stage gates; `WEEKLY_ORCHESTRATION_BLUEPRINT.md` G1–G5 = milestone locks (merged 2026-08-24, after the skills); MCDA charter G1–G10 = selection criteria.
  - Drift already materialized in-corpus: simulation checkpoint files stamp `gate: G1 … status: APPROVED` (milestone sense) while occupying the loop position of loop-G1 (weekly planning validated) — the two vocabularies interleave in the same pipeline (`exit_gate: G1_SSoT_Lock` inside a weekly plan; `Target Gate: G3/G5` columns meaning milestone locks inside a brief whose stage gates are also called G3/G5).
  - `README.md` presents the blueprint as the cadence law for the same Monday–Friday cycle without disambiguation.
- **affected user job:** Resuming/auditing the loop (Q8, provenance jobs): a reader cannot tell which gate semantics an APPROVED marker encodes; automation keying on `gate: G*` values can advance the wrong stage.
- **affected production files:** control-plane namespace spanning `.claude/skills/weekly-orchestrator/SKILL.md` (owner) vs `apex-meta/orchestration/workflows/WEEKLY_ORCHESTRATION_BLUEPRINT.md` + `README.md` (foreign vocabulary, unresolved).
- **severity:** CRITICAL
- **failure example:** An agent resuming from disk reads Friday "milestone gate verification (G1–G5)" from the blueprint, concludes loop-G5 passed, and routes a durable mutation through apex-session without status-merge having run.
- **expected behavior:** Exactly one owner for loop-gate semantics (weekly-orchestrator SKILL.md). Foreign documents use disjoint identifiers (campaign rule: `loop-G*` vs `milestone-lock-G*`); eventually renamed/moved in production via approved patch (Phase 8+).
- **objective or human-verifiable test:** Deterministic namespace audit: any campaign-produced artifact referencing gates uses qualified identifiers; grep over produced packets finds no ambiguous bare `G[1-5]` outside the owning skill's own packet schema. Production-side fix verified by exact-match patch + `git apply --check` in Phase 8.
- **regression risk:** Renaming blueprint gates touches showcase docs only; no runtime consumer found in skills/scripts (to be re-verified before any patch).

---

## Cross-cutting severity roll-up

| Finding | Severity | Class | Primary layer |
| :-- | :-- | :-- | :-- |
| F01 | HIGH | information architecture | weekly |
| F02 | HIGH | duplication/ownership | weekly↔daily |
| F03 | HIGH | delta visibility | daily |
| F04 | MED-HIGH | provenance placement | all |
| F05 | MED-HIGH | capacity expression | weekly+daily |
| F06 | HIGH | prompt specificity | prompts |
| F07 | CRITICAL | evaluation methodology | campaign/checkpoints |
| F08 | HIGH | synthesis integrity | campaign/checkpoints |
| F09 | MEDIUM | noise/exceptions | card+prompts |
| F10 | CRITICAL | authority namespace | control plane |

F07/F08/F10 are process-integrity findings: they gate how the campaign itself may
produce evidence (no self-scores, no dropped findings, qualified gate ids), while
F01–F06/F09 define the artifact-design space Phases 4–7 will attack.
