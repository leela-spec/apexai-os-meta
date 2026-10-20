---
type: Reference
id: V2-DECISION-REGISTER-v1.0
title: Decision Register — Always-On Architecture
description: Settled decisions, superseded positions, mechanical facts, open operator calls, and falsification conditions for the Apex Informatics always-on contract architecture.
status: current
tags: [decisions, register, superseded, falsification, architecture]
---

# Decision Register — Always-On Architecture

**How to read this:** Part A is settled and applied. Part B is what I believed and no longer do —
kept visible because the applied code still reflects some of it. Part C is the architecture
position, which is **measured but untested**. Part D is mechanical fact. Part E needs you. Part F
says what would prove each position wrong.

Decision IDs are durable (`DEC-01`…). Status values: `APPLIED`, `PROPOSED`, `SUPERSEDED`,
`WITHDRAWN`, `OPEN`.

---

## Part A — Settled decisions

These were decided, applied to the live suite, and verified. Record in
[../DeepReasoning/04-consolidated-patch-and-verification.md](../DeepReasoning/04-consolidated-patch-and-verification.md).

| ID | Decision | Rationale | Status |
|---|---|---|---|
| **DEC-01** | Delete duplicated **blocks** (≥8 lines: schemas, tables, JSON, catalogs); do not delete duplicated short rules in the same pass | Contradiction between large copies is the expensive failure; a restated one-line invariant is not | `APPLIED` |
| **DEC-02** | `file-architecture.md` owns the OKF frontmatter contracts; `governance-schemas.md` states the validation view only | Ownership follows the load path — `FA` is what a file-creation task loads | `APPLIED` |
| **DEC-03** | `patch_intent.v1` lives in **one artifact outside the bundle**; the spec states the operative contract and links it | The embedded copy had already drifted, dropping every `maxLength` bound the real schema enforces | `APPLIED` |
| **DEC-04** | Duplicate `FA-04` resolved by moving the second rule to `FA-13`, not renumbering `FA-05..FA-12` | Disturb one durable ID rather than eight live cross-references | `APPLIED` |
| **DEC-05** | `standard.md` §2 precedence ladder extended; the modular suite governs every subject it covers | Two documents each claiming override authority is the measured failure mode | `APPLIED` |
| **DEC-06** | A test may be rewritten only when a rule legitimately changed owner, and the replacement must test *more* than the original | `test_tas_02` now validates the authoritative schema **and** that the spec agrees with it | `APPLIED` |
| **DEC-07** | `general-informatics-router.md` stays byte-identical to baseline; its 500-token ceiling is not relaxed for a comment | Weakening a gate to admit a nice-to-have is how ceilings stop meaning anything | `APPLIED` |
| **DEC-08** | `D8` (duplicated `estimate_tokens`) deliberately **not** fixed | Creating a shared module to deduplicate a 4-line function fails `AD-25` and `AD-13` | `APPLIED` |
| **DEC-09** | Three new rules added: `WP-23` single-owner instruction reuse, `WP-24` clickable file references, `WP-25` terminal-position operative content | Two from operator lore never codified; one from positional-attention research at zero token cost | `APPLIED` |

---

## Part B — Superseded positions

**This part exists because the applied code still carries artifacts of reasoning I no longer hold.**
A future reader must not mistake those artifacts for endorsement.

### `DEC-10` — "Modules must restate universal invariants to stay self-sufficient" → `SUPERSEDED`

| | |
|---|---|
| **What I held** | Under one-gate-one-file routing, a module loaded alone must contain every rule it needs. So `AD-03` restating `EM-01`, `AD-08` restating `WP-01` etc. is correct, and the fix is to bind their wording with `Canonical:` markers. |
| **Why I held it** | True *given the architecture as it existed* — nothing guaranteed a universal invariant was in context when a module loaded. |
| **What changed it** | Discovering that `general-informatics-router.md` was never installed, and that the intended design puts the contract **inside `AGENTS.md`**, which is always loaded. Once that is true, the invariant is already in context and the restatement buys nothing. |
| **Replaced by** | `DEC-12` below. |
| **Live artifact of the old view** | 23 `Canonical: XX-NN` markers across the five modules (3 `WP`, 5 `FA`, 2 `EM`, 6 `AD`, 7 `GS`). **Harmless today** — they are accurate cross-references. Under `DEC-12` Step 2, the 8 universal ones become deletable. |

### `DEC-11` — "Apply one uniform CROSS_LINK policy to all duplicated rules" → `SUPERSEDED`

| | |
|---|---|
| **What I held** | Every short duplicated rule is retained and wording-bound, regardless of how many copies exist. |
| **What changed it** | The established practice is a **threshold**, not a uniform policy. Fowler's Rule of Three: one or two copies, leave alone; at three or more, extract. I applied the Metz/AHA half ("duplication is cheaper than the wrong abstraction") and skipped the Fowler half. |
| **Measured consequence** | 8 of 13 duplicated concepts cross the threshold: Substance Over Ceremony (5 copies), whole-file rewrite ban (5), instruction parsimony (4), step-by-step context (4), TARGET dominance (4), top-loaded primacy (3), durable IDs (3), residual name eradication (3). The remaining 5 sit at 2 copies and correctly stay. |
| **Replaced by** | `DEC-12`. |

### `DEC-W1` — "Audit the 3,031-token always-on tier" → `WITHDRAWN`

I measured `CLAUDE.md` + `.claude/CLAUDE.md` + `AGENTS.md` and called the total a problem to fix.
The operator states those files are placeholders awaiting exactly this work. **That number is not a
defect — it is the budget the new contract must fit inside.** The decision was malformed and is
withdrawn, not answered.

### `DEC-W2` — "Decide whether `index.md` is a guaranteed kernel" → `WITHDRAWN`

Malformed question. `index.md` is **not the runtime router and never was**. The prior design states
the contract block belongs embedded in `AGENTS.md` and that agents should not be told to read the
pilot file at runtime
([08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md](../../../../handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md)).
Replaced by `DEC-14`.

### Vocabulary correction

"Level 1 / Level 2 / Level 3" was imported jargon that obscured rather than explained. The
replacement, used throughout this folder:

| Term | Meaning |
|---|---|
| **always-on** | Read every session regardless of task |
| **on-demand** | Read only when a condition matches |
| **look-up** | Opened only for one specific detail |

---

## Part C — Architecture position

### `DEC-12` — Universal invariants move into an always-on contract `PROPOSED`

The 8 Rule-of-Three concepts are stated **once**, in a contract block embedded in `AGENTS.md`.
Because that file is always loaded, the invariants are already in context whenever any module
loads — so modules stop restating them. **No pointer, no hop, no copy.**

Two steps, deliberately separated:

- **Step 1 (reversible, nothing can break):** install the contract into `AGENTS.md`; stop `index.md`
  carrying invariants and IF-clauses. The five modules are **unchanged** — their copies become
  harmless redundancy rather than load-bearing redundancy.
- **Step 2 (only after Step 1 runs in practice):** delete the 8 restatements from the modules;
  rewrite `test_olt_07`, which currently asserts the duplication by name across five files.

### `DEC-13` — Reduced-form rules in the contract, not bare pointers `PROPOSED`

The always-on block carries writing and file-architecture rules **in reduced form**, not merely
links to them — because an agent writes prose and touches files on nearly every task, so those
rules earn their 253 tokens. Patch discipline, anti-drift and schema validation stay pointers
because they are genuinely conditional.

Measured: **721 tokens total** (`<always>` 303, `<writing>` 140, `<files>` 113, `<dispatch>` 133).

### `DEC-14` — `index.md` is a bundle index only `PROPOSED`

It stops carrying invariants and dispatch gates. Its job is OKF validation entry and human
navigation. Nothing reads it at runtime.

### `DEC-15` — `general-informatics-router.md` becomes a labelled portable artifact `PROPOSED`

Once `AGENTS.md` carries the live contract, the router file is explicitly a derivative kept for
embedding into *other* repositories. It is labelled as such and is not a second live router.

### `DEC-16` — Conditional branches must cross a file boundary `PROPOSED` ★ new

**This is the newest decision and the highest-leverage one.** It did not exist as an option before
the mechanical correction in `DEC-M3` below — docs 05 and 06 could not have contained it.

> A conditional branch only saves tokens when the branch target is a **separate file**. An
> IF-clause pointing at a *section* of a file the agent is already reading saves nothing.

Consequence: a monolithic on-demand file whose parts are mutually exclusive should be **split into
one file per branch**, each with its own gate.

First application — `execution-modes.md`, measured:

| Section | Tokens |
|---|---:|
| Core invariants + dispatch | 599 |
| Adapter 1 — Q&A Decision Matrix | 627 |
| Adapter 2 — Bake-Off Rubric | 444 |
| Adapter 3 — Exact-Match Patch | 713 |
| Adapter 4 — Handover | 475 |
| Adapter 5 — Iterative / MMM | 1,034 |
| Adapter 6 — Git Sync | 167 |
| **Monolithic read today** | **4,208** |

A patch task would load **713 instead of 4,208 — an 83% cut** on the heaviest module in the suite.

**Status is `PROPOSED`, with operator endorsement noted, pending
[04-empirical-test-protocol.md](04-empirical-test-protocol.md).** The token arithmetic is
deterministic and not in question. What is in question is whether an agent honours the gate. If the
read-trace test shows agents read every candidate file regardless of gating, this split buys
nothing and `DEC-16` fails. That condition is recorded in Part F so the test stays honest rather
than confirmatory.

**Not every module should be split.** `anti-drift-rules.md` is the counter-case: its rules apply
together rather than exclusively, so splitting it would add hops without removing content. The
criterion is **mutual exclusivity of the branches**, not file size.

---

## Part D — Mechanical facts established

Not opinions. These constrain every design above.

| ID | Fact | Consequence |
|---|---|---|
| **DEC-M1** | An IF-clause inside an already-loaded file saves **zero** tokens. All branches are in context regardless of which matches. | A ~1,000-token always-on budget is a hard budget. Structure cannot evade it. |
| **DEC-M2** | Gates in the always-on file still buy two real things: they prevent downstream file reads (2,400–4,200 tokens each), and they reduce the number of instructions competing for compliance. | Gating the always-on block is worth doing — for precision and downstream savings, not for its own cost. |
| **DEC-M3** | A conditional branch saves tokens **only when it crosses a file boundary**. | Basis of `DEC-16`. |
| **DEC-M4** | A functional reduced form of the whole system measures **721 tokens**. | The ~1,000-token target is achievable. |
| **DEC-M5** | A worked example is not duplication. | `execution-modes.md` §2.2 illustrates `EM-06`; deleting it would be DRY cargo-culting. `WP-17` mandates such examples. |
| **DEC-M6** | `okf_validator.py` enforces frontmatter `id:` uniqueness but is blind to in-body rule IDs. | `D1` survived a green validator and 185 tests. Pytest guard added; `RBL-06` proposes promoting it. |

### Measured cost per task type

| Task | Today | Under `DEC-12`+`DEC-13` | With `DEC-16` |
|---|---:|---:|---:|
| "Fix this bug" | 1,000 | **721** | 721 |
| "Patch a file" | 7,622 | 4,937 | **1,434** |
| "Write a spec" | 7,622 | **721** | 721 |
| "Emit a patch_intent" | 8,378 | ~1,500 | ~1,500 |

---

## Part E — Open operator decisions

| ID | Question | Options | My lean | Blocked by |
|---|---|---|---|---|
| **DEC-O1** | Install the contract into `AGENTS.md` (Step 1)? | Yes / No / After the test | **After the test** — Step 1 is reversible, but the read-trace result changes how much of it is worth doing | `04-empirical-test-protocol.md` |
| **DEC-O2** | Do Step 2 — delete the 8 restatements from modules? | Yes / Step 1 only | **Yes, after Step 1 runs in practice** | `DEC-O1` |
| **DEC-O3** | Split `execution-modes.md` into per-adapter files? | Yes / No / Only if the test passes | **Only if the test passes** | Test |
| **DEC-O4** | Should the three research threads run before or after the empirical test? | Before / After / Parallel | **Parallel** — the vector-retrieval question could change the architecture, so it should not wait on a test of the current one | — |
| **DEC-O5** | Is my reduced-form wording acceptable? | Accept / Revise / Rewrite | **Needs your eye** — every reduced rule is a lossy compression of a rule you wrote, `<always>` especially | — |
| **DEC-O6** | Does `AGENTS.md`'s existing content merge or stay? | Merge / Keep separate / Replace | **See the merge map** in [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) | — |

---

## Part F — Falsification conditions

What evidence would overturn each position. Recorded **before** the test runs.

| Position | Falsified if |
|---|---|
| `DEC-12` always-on invariants | An agent given the contract still fails to apply an invariant that a module would have enforced — i.e. the reduced form is behaviourally weaker than the restatement |
| `DEC-13` reduced-form rules | Output quality under the 721-token contract measurably degrades versus the full 2,845-token writing profile on the same authoring task |
| `DEC-16` file-boundary splitting | **The read-trace test shows agents open non-matching module files anyway.** If gates do not prevent reads, splitting creates more files and saves nothing |
| `DEC-M2` gates buy precision | Compliance with an in-scope rule is no better when sibling rules are gated out than when they are all present |
| `DEC-14` index as bundle index only | Some runtime path is found that genuinely depends on reading `index.md` |
| The whole architecture | Vector retrieval turns out to dominate static IF-dispatch for this use case — see [05-research-prompt-packets.md](05-research-prompt-packets.md) packet 2 |

**The sharpest single risk:** `DEC-16` and `DEC-M2` both assume an agent honours a gate. Nobody has
measured that in this repository. If that assumption fails, `DEC-12` survives (always-on content is
loaded unconditionally, so it does not depend on gating) but `DEC-16` collapses entirely.

---

## Provenance

| Source | What it settled |
|---|---|
| [../DeepReasoning/04-consolidated-patch-and-verification.md](../DeepReasoning/04-consolidated-patch-and-verification.md) | Part A, all `APPLIED` entries |
| [../DeepReasoning/05-architecture-and-context-budget.md](../DeepReasoning/05-architecture-and-context-budget.md) | Rule of Three analysis behind `DEC-11` |
| [../DeepReasoning/06-how-the-routing-actually-works.md](../DeepReasoning/06-how-the-routing-actually-works.md) | `DEC-14`, `DEC-15`, `DEC-W2` |
| [../DeepReasoning/07-candidate-always-on-block.md](../DeepReasoning/07-candidate-always-on-block.md) | `DEC-13`, `DEC-16`, all of Part D |
| [08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md](../../../../handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md) | The operator's original design intent; corrected `DEC-W2` |
