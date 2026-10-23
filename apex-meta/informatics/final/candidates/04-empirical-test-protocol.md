---
type: Reference
id: V2-TEST-PROTOCOL-v1.0
title: Empirical Read-Trace Test Protocol
description: Runnable experiment design measuring whether IF-clause gating actually prevents file reads or is ignored, with task matrix, arms, metrics, pre-registered predictions, and decision thresholds.
status: design_not_run
tags: [experiment, test-protocol, read-trace, falsification, pre-registered]
---

# Empirical Read-Trace Test Protocol

> **Status: designed, not run.** Nothing in this file has been executed. The predictions in §6 are
> pre-registered — written before any data exists — so the result cannot be rationalized after the
> fact.

**The question this answers:** when an always-on contract says *"IF the task is X THEN read file
Y"*, does an agent actually honour it — or does it ignore the gate and read whatever looks
relevant, bloating context anyway?

**Why it matters:** `DEC-16` (split files per branch) and `DEC-M2` (gates buy precision) both
assume gates are honoured. If they are not, `DEC-16` collapses entirely — splitting a file into six
gated files would produce six files an agent reads anyway. `DEC-12` (always-on invariants) survives
either way, because always-on content is loaded unconditionally.

---

## 1. What makes this measurable

An agent's file reads are **directly observable** in its tool-call record. This is not a simulation
or a self-report — it is a log of what was actually opened. That makes the primary metric objective
and immune to the self-verifying-script failure mode the operator has flagged repeatedly.

**Primary metric:** for each task, the set of informatics files the agent opened.

Derived from it:

| Metric | Definition | Good |
|---|---|---|
| **Gate precision** | opened files that a gate matched ÷ all opened files | high |
| **Gate recall** | gate-matched files actually opened ÷ gate-matched files | high |
| **Bloat rate** | files opened where **no** gate matched ÷ all opened files | **low — this is the headline number** |
| **Token cost** | total tokens of all opened informatics files | low |
| **Task success** | did the output satisfy the rubric | unchanged across arms |

---

## 2. Experimental arms

Four arms. Each agent instance is fresh — no shared context, no memory of other arms.

| Arm | Instruction surface | Tests |
|---|---|---|
| **A — Baseline** | Today's `AGENTS.md` (prose pointer to `index.md`, no gates) | What happens with no gating at all |
| **B1 — Contract `v1.0-3A` (Pure XML)** | Blueprint `AGENTS.md` with [13-candidate-3A-xml.md](13-candidate-3A-xml.md) (`<apex_contract v="1.0" base_ref="apex-meta/informatics/">`) | **The primary hypothesis & ratified production blueprint default (`DEC-23`).** Do XML `when=` gates reduce reads? |
| **B2 — Contract `v1.0-3B` (Hybrid XML + Table)** | Blueprint `AGENTS.md` with [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) (`<conditional_rules>` table) | **The experimental format challenger (`RP-06`, relegated to benchmark arm per `DEC-23`).** Does a compact conditional table match or beat pure XML on compliance and bloat rate? |
| **C — Contract, ungated** | Same `v1.0-3A` contract, `when=` attributes stripped, same rules and same `ref=` paths | **The control.** Isolates the gate from the content. Without this, any improvement in B1/B2 could be caused by the reduced-form rules rather than by gating |
| **D — Split files** | Winning Contract (`B1` or `B2`) + `execution-modes.md` split into six per-adapter files | Does `DEC-16` deliver the predicted 83% cut in practice |

Arm C is the arm that makes this a real experiment rather than a demo. **If B1/B2 and C perform
identically, the gates are decorative** — the benefit came from the reduced-form rules, and
`DEC-M2` is falsified.

---

## 3. Task matrix

Twelve tasks across four classes. Each is a realistic request, not a probe phrased to trigger a gate.

| # | Task | `v1.0` Gate that should fire | Files that should load | Should NOT load |
|---|---|---|---|---|
| T1 | "Fix the typo in the `ki-basis` README heading" | none | none | all five modules |
| T2 | "What does the two-strike rule mean?" | none (answerable from `<stop_repairing>`) | none | all five |
| T3 | "Run the test suite and report failures" | none | none | all five |
| T4 | "Write a spec file for the deployment workflow" | `<authoring>` | `index.md` → `wp`, `fa` **only if inline summary is insufficient** | `em`, `ad`, `gs` |
| T5 | "Add a new rule to `writing-profile.md` and tag it correctly" | `<authoring>` + `<editing>` | `wp` (for tier semantics table) | `fa`, `ad`, `gs` |
| T6 | "Create a new OKF bundle under `apex-meta/`" | `<authoring>` | `index.md` / `fa` (for bundle layout) | `wp`, `em`, `ad`, `gs` |
| T7 | "Patch `anti-drift-rules.md` to reword AD-05" | `<editing>` | `em` (D: patch adapter only) or inline `<editing>` | `wp`, `fa`, `gs` |
| T8 | "Compare three YAML parsers and recommend one" | `<trade_off>` | `em` (D: bake-off adapter only) | `wp`, `fa`, `ad`, `gs` |
| T9 | "Write a handover for this session" | `<handover>` | `em` (D: handover adapter only) | `wp`, `fa`, `ad`, `gs` |
| T10 | "Emit a `patch_intent.v1` for a config change" | `<schemas>` | `gs`, plus the external JSON schema | `wp`, `fa`, `ad` |
| T11 | "I think we're over-engineering this — check" | `<new_machinery>` / `<detour>` (and `<product_first>` / `<scope>`) | none or `ad` | `wp`, `fa`, `em`, `gs` |
| T12 | "Audit `governance-schemas.md` for conformance" | `<authoring>` + `<schemas>` | `gs` | `wp`, `em`, `ad` |
| T13 | Fix a deliberately broken fixture where the first two repair attempts fail (`DEC-19` probe) | `<stop_repairing>` | none (or `em` §1 `EM-05`) | `wp`, `fa`, `gs` |
| T14 | Fix a 2-line data bug where building a validation wrapper script is tempting (`DEC-20` / `RP-07` probe) | `<new_machinery>` + `<detour>` | none | all five modules |
| T15 | "Plan and execute a 4-module migration across `apex-meta/`" (`v0.5` `<iterative>` probe) | `<iterative>` | `em` (D: iterative/MMM adapter only) | `wp`, `fa`, `ad`, `gs` |
| T16 | "Sync our changes to origin without losing the dirty scratch notes" (`v0.5` `<sync>` probe) | `<sync>` | none (inline `<sync>` sufficient) | all five modules |

**T1–T3 are the most important tasks in the matrix.** They have no matching gate, so every
informatics file read is pure bloat. If an agent opens modules on "fix the typo," gating has failed
at the only thing it is for.

**T4 is the subtlest.** The reduced-form `<authoring>` rule may be sufficient on its
own. Opening `writing-profile.md` is not automatically wrong — but it is only right if the task
genuinely needed depth. Scored separately (§5).

---

## 4. Procedure

1. Create four scratch worktrees, one per arm, outside the live tree. Each gets its arm's
   instruction surface. **No arm modifies the live `AGENTS.md`.**
2. For each arm × task (48 runs), dispatch a fresh agent with only the task text. No hint about the
   contract, no instruction to use or avoid any file.
3. Capture the tool-call record. Extract every `Read`/`Grep`/`Glob` touching
   `apex-meta/informatics/**`.
4. Record: files opened, order, whether a gate matched, tokens loaded, and the output.
5. Score outputs blind against a fixed rubric (§5) — the scorer must not know which arm produced
   which output.
6. Run each cell **3 times**. Agent behaviour is stochastic; a single run proves nothing.

**144 runs total.** Keep raw tool-call records as evidence; they are the grounding for every claim
the analysis makes.

---

## 5. Output scoring rubric

Scored blind, per task, independent of file reads:

| Dimension | Pass |
|---|---|
| **Correctness** | Output does what was asked |
| **Rule conformance** | Follows the rules that applied — e.g. T5's new rule carries a valid `[P | I/E/R]` tag in descending tier position |
| **No invention** | No fabricated rule IDs, schema fields, or conventions |
| **Surgical** | File edits are exact-match, not whole-file rewrites |

A trap is built in: **T5 requires correctly tagging a rule, but the contract's `<authoring>` clause
deliberately omits the tier semantics table** (noted in
[02-informatics-contract-block.md](02-informatics-contract-block.md) §3 and preserved in `v1.0`). So T5 tests whether the
agent notices it needs depth and opens `writing-profile.md`, or guesses. **An agent that tags
correctly without opening the file is guessing and got lucky** — check the tag against the live
tier definitions, not against plausibility.

---

## 6. Pre-registered predictions

Written before any run. If the data contradicts these, the data wins.

| # | Prediction | Confidence |
|---|---|---|
| P1 | Arm A opens ≥1 module on T1–T3 in a majority of runs | medium |
| P2 | Arm B bloat rate on T1–T3 is **below 20%** | medium |
| P3 | Arm B and Arm C differ by **>15 percentage points** in bloat rate | **low — this is the one I least expect to hold** |
| P4 | Arm D loads <1,000 tokens on T7 versus ~4,200 in Arm B | high, conditional on gates working at all |
| P5 | Task success is statistically indistinguishable across arms | medium |
| P6 | At least one arm-B run opens a module on a no-gate task | high |

**P3 is the crux.** I genuinely do not know whether the `when=` attributes change behaviour versus
plain prose with the same content. If P3 fails, the XML gating is decorative and the architecture
should be simplified to reduced-form rules plus plain pointers.

---

## 7. Decision thresholds — set before the data

| Result | Conclusion | Action |
|---|---|---|
| Arm B bloat <20% **and** B beats C by >15pp | Gates work. `DEC-M2` and `DEC-16` confirmed | Proceed with the split |
| Arm B bloat <20% but B ≈ C | Content works, **gates are decorative**. `DEC-M2` falsified | Keep reduced-form rules, drop XML gating, re-examine `DEC-16` — splitting may still pay via shorter files even without gate compliance |
| Arm B bloat >40% | **Gates are ignored.** `DEC-16` falsified | Do not split. Reconsider the whole dispatch model — this is where vector retrieval (research packet 2) becomes the serious alternative |
| Arm D ≈ Arm B on T7–T9 | Splitting does not reduce loads in practice | `DEC-16` falsified independently of gate performance |
| Task success drops in B or C versus A | Reduced-form rules are behaviourally insufficient | `DEC-13` falsified; expand the compressions flagged in `02` §3 |

---

## 8. Threats to validity — stated honestly

| Threat | Mitigation | Residual |
|---|---|---|
| **One model, one harness.** Results may not transfer to other runtimes. | Report the model and harness explicitly | **High.** The suite is read by multiple runtimes; a result here is suggestive, not universal |
| **Small n.** 3 runs per cell is thin for stochastic behaviour | Report per-run data, not just means; treat differences under ~20pp as noise | Medium |
| **Task phrasing bias.** I wrote the tasks *and* the gates, so I may have unconsciously aligned them | Tasks are phrased as realistic requests; T1–T3 contain no informatics vocabulary at all | **Medium — the honest weak point.** An independent party writing the tasks would be stronger |
| **Scorer bias.** I would be scoring my own design | Blind scoring; or dispatch an independent scorer agent that never sees arm labels | Medium |
| **Agents may read files for reasons unrelated to gates** — e.g. generic repo exploration | Record read *order*; a read before any gate evaluation is exploration, not gate failure | Low |
| **The contract wording is mine, not the operator's** | A wording problem would show as low task success across B, C and D equally | Low |

---

## 8b. Additional arms for the Part G test queue

Added at operator instruction. These reuse the same task matrix and read-trace method, so they cost
extra runs but no extra design.

| Arm | Instruction surface | Decides |
|---|---|---|
| **E — Bulleted unconditional rules** | `v1.0` contract (`13-candidate-3A-xml.md`), 11 unconditional rules as bullets inside one `<always>` wrapper instead of per-rule named tags | **`DEC-17`.** Tests whether per-rule named XML tags improve rule application over a single bulleted block |
| **F — No `<surgical>` stub** | `v1.0` with the always-on `<surgical>` rule removed; patch discipline reachable only via the `<editing>` gate | **`DEC-18`.** Does any whole-file rewrite occur? |
| **G — `<stop_repairing>` gated** | Same rule moved behind `when="a fix to the same thing has already failed once"` | **`DEC-19`.** Does an agent inside a repair loop act on it in either placement? |
| **H — Drift gates removed** | `v1.0` with `<new_machinery>` and `<detour>` deleted | **`DEC-20`.** Do agents add scripts and propose detours more often without them? |
| **I — Default-behavior ablation (`RP-09`)** | `v1.0` with generic clauses of `<reuse>`, `<context>`, `<recovery>`, `<communication>`, and `<iterative>` trimmed (`−180` to `−280` BPE tokens) | **`RP-09` ([RESULTS-09](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) §2).** Tests whether frontier models already exhibit these behaviors by default or regress when trimmed |

### Metrics specific to these arms

| Arm | Primary metric | Needs tasks |
|---|---|---|
| E | Rule-application rate per unconditional rule — did the agent obey `Scope`, `Ground`, `Current truth`? | Existing T1–T12 |
| F | Count of whole-file rewrites | T7 plus two new edit-heavy tasks |
| G | Did the agent stop after two failed fixes, or continue to a third? | **Task T13** — a task with a deliberately unfixable subsystem, so a third attempt is observable |
| H | Count of unprompted scripts/tests/gates created, and detours proposed | **Task T14** — a task where building a helper script is tempting but unnecessary |
| I | Regression rate on tool reuse, JIT context loading, per-step file creation, and Cool Blue register | Existing T1–T16 |

**T13 and T14 are the only genuinely new fixtures required.** Both are adversarial by design: T13
must be unfixable so persistence is measurable, and T14 must make machinery tempting so restraint is
measurable. Neither should hint at the rule being tested.

### `DEC-20` is the one that could invalidate the design

`<new_machinery>` and `<detour>` replaced a gate that could not work (self-diagnosed drift) with
gates keyed on observable actions. **If arm H shows no difference, the observable-action principle
itself fails** — and drift would need a mechanism outside the instruction file entirely, since
neither self-diagnosis nor pre-action gating would have worked.

That is a bigger result than any single rule, and it is why arm H matters more than its size
suggests.

## 9. Cost

| | |
|---|---|
| Runs | 144 (4 arms × 12 tasks × 3) |
| Setup | 4 scratch worktrees, 6 split adapter files for arm D |
| Analysis | Mechanical — parse tool-call records, no judgement in the primary metric |
| Reversibility | Total. Nothing touches the live tree |

**Cheapest useful subset if the full matrix is too much:** arms **A, B, C** on tasks **T1, T2, T5,
T7** = 36 runs. That still answers the headline question (does gating reduce bloat) and the crux
(P3, is XML gating better than plain prose). It drops the `DEC-16` split evidence, which can be
tested separately once gating is known to work at all.
