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

### `DEC-C1` — "The named-tag design is the operator's own" → `CORRECTED`

In [06-contract-block-revision-proposal.md](06-contract-block-revision-proposal.md) §1 I justified
adopting one-named-tag-per-rule by calling it *"your own prior design"* and said I had *"regressed
from it."*

**I did not verify that.** Checked afterwards: `08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md` is committed
under the operator's git identity, but every commit touching it follows this repository's
AI-assisted pattern (`docs(agent-contract): deepen C01 …`). It carries no authorship marker, and
`standard.md` shows the repo does mark AI generation when the convention is applied
(`generated: { by: gemini-3.7-flash }`). Absence of a marker is not evidence of human authorship.

**Correct statement:** it is a prior candidate in this repository, most likely AI-drafted, carrying
no more authority than my own draft. Appealing to it as operator design was an unverified appeal to
authority, and it is exactly what `<ground>` forbids. The design choice has to stand on evidence —
see `DEC-17`.

### `DEC-C2` — "Named tags cost ~150 tokens more than bullets" → `CORRECTED`

Also from the revision proposal. **Measured: the difference is 17 tokens**, 1.3% of the block.

The estimate was wrong because bullets still need a label (`- Target: `) which costs nearly what a
tag pair costs (`<target>` … `</target>`). Actual accounting of the v0.3 → v0.4 growth of +585:

| Source of growth | Tokens | Share |
|---|---:|---:|
| Three rules that did not exist (`product_first`, `new_machinery`, `detour`) | 226 | 39% |
| `trade_off` + `schemas` promoted from one-line pointers to full blocks | 187 | 32% |
| `editing` expanded from one line to the full protocol + overcorrection | 123 | 21% |
| `ground` expanded to carry checkable-ambiguity | 44 | 7% |
| **Named tags** | **17** | **3%** |

**The growth is new content, not formatting.** The proposal misattributed it, which would have sent
review effort at the wrong target.

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

The always-on block carries writing, file-architecture, anti-drift, and task-adapter rules **in reduced form**, not merely links to them — because an agent writes prose, touches files, and faces scope/drift boundaries on nearly every task, while deep reference files (`execution-modes.md`, `index.md`, `governance-schemas.md`) stay behind `when=` + `ref=` gates.

Measured (`v1.0` finalized): **`1,632` repo tokens (`1,350` BPE tokens)** in `v1.0-3A` ([13-candidate-3A-xml.md](13-candidate-3A-xml.md)) or **`1,586` repo tokens (`1,314` BPE tokens)** in `v1.0-3B` ([14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md)) across 12 unconditional invariants, 9 conditional rules, and 1 terminal `<pointers>` guard.

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
| **DEC-M1** | An IF-clause inside an already-loaded file saves **zero** tokens. All branches are in context regardless of which matches. | Unchanged always-on tokens are paid per session (discounted 78.5%–90% by prompt prefix caching per `RP-09`). The ~1,000-token figure is an operational heuristic, not a hard cliff (`RP-03`). |
| **DEC-M2** | Gates in the always-on file still buy two real things: they prevent downstream file reads (2,400–4,200 tokens each), and they reduce the number of instructions competing for compliance. | Gating the always-on block is worth doing — for precision and downstream savings, not for its own cost. |
| **DEC-M3** | Within plain Markdown files without runtime loader support, a conditional branch saves tokens **when it crosses a file boundary** (whereas native harness features like Claude Code `.claude/rules/` `paths:` frontmatter and on-demand Skills also defer tokens natively per `RP-03`). | Basis of `DEC-16` for mutually exclusive adapters, qualified by `RP-03` so we do not over-fragment into micro-files. |
| **DEC-M4** | The finalized `v1.0` contract block measures **`1,632` repo tokens (`1,350` BPE)** in `3A` and **`1,586` repo tokens (`1,314` BPE)** in `3B` (+`295` repo tokens for Layer 2 repo context = `1,881`–`1,927` repo tokens total). | Comfortably within the 1,024-token prefix-cache minimum and ~1,200–1,800 BPE operational band (`RP-09`). |
| **DEC-M5** | A worked example is not duplication. | `execution-modes.md` §2.2 illustrates `EM-06`; deleting it would be DRY cargo-culting. `WP-17` mandates such examples. |
| **DEC-M6** | `okf_validator.py` enforces frontmatter `id:` uniqueness but is blind to in-body rule IDs. | `D1` survived a green validator and 185 tests. Pytest guard added; `RBL-06` proposes promoting it. |

### Measured cost per task type (`v1.0` Repo Estimator `chars // 4`)

| Task | Today (No Contract + Module Reads) | Under `DEC-12`+`DEC-13` (`v1.0-3A` Always-On) | With `DEC-16` (If `execution-modes.md` Split Passes Test) |
|---|---:|---:|---:|
| "Fix this bug" (no deep module needed) | ~1,000 | **1,927** *(cached prefix)* | **1,927** *(cached prefix)* |
| "Patch a file" (inline `<editing>` sufficient) | 7,622 | **1,927** | **1,927** |
| "Patch a file" (deep `execution-modes.md` read) | 7,622 | 6,135 | **2,640** |
| "Write a spec" (inline `<authoring>` sufficient) | 7,622 | **1,927** | **1,927** |
| "Emit a `patch_intent`" (`governance-schemas.md` read) | 8,378 | **4,361** | **4,361** |

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
| `DEC-13` reduced-form rules | Output quality under the `v1.0` contract (`1,632` repo tokens / `1,350` BPE) measurably degrades versus the full `2,845`-token writing profile on the same authoring task |
| `DEC-16` file-boundary splitting | **The read-trace test shows agents open non-matching module files anyway.** If gates do not prevent reads, splitting creates more files and saves nothing |
| `DEC-M2` gates buy precision | Compliance with an in-scope rule is no better when sibling rules are gated out than when they are all present |
| `DEC-14` index as bundle index only | Some runtime path is found that genuinely depends on reading `index.md` |
| The whole architecture | Vector retrieval turns out to dominate static IF-dispatch for this use case — see [05-research-prompt-packets.md](05-research-prompt-packets.md) packet 2 |

**The sharpest single risk:** `DEC-16` and `DEC-M2` both assume an agent honours a gate. Nobody has
measured that in this repository. If that assumption fails, `DEC-12` survives (always-on content is
loaded unconditionally, so it does not depend on gating) but `DEC-16` collapses entirely.

---

## Part F2 — `DEC-21`: which instruction surfaces carry the contract

**Operator decision: all of them.** *"All AIs are going to get the same thing because this is how I
want all AIs to work."*

### My earlier objection is withdrawn

I repeatedly flagged "both would rebuild the two-copies problem" as a blocker. That framing was
wrong in two ways.

**First, the scope is five surfaces, not two:**

| Surface | Lines | Loaded by |
|---|---:|---|
| `AGENTS.md` | 50 | Codex and the `AGENTS.md` convention |
| `CLAUDE.md` | 50 | Claude Code, repo root |
| `GEMINI.md` | 38 | Gemini |
| `.claude/CLAUDE.md` | 53 | Claude Code, project scope — **different content**, orchestration routing |
| `.github/copilot-instructions.md` | 18 | Copilot — **different content**, navigation only |

The first three share headings (`Git Dispatch`, `Directness`, `Core Intent Execution`, `Scope`) and
are manual copies of one another. The last two carry different content and are not part of the same
copy set.

**Second, the problem already exists and is unmanaged.** Measured:

| Comparison | Drift found |
|---|---|
| `AGENTS.md` vs `CLAUDE.md` | Infrastructure banner diverged — different wording, different ordering, different description of the superseded files |
| `AGENTS.md` vs `GEMINI.md` | **`GEMINI.md` is missing the entire `## Informatics & Knowledge Routing` section** |

### `D10` — live defect, found while resolving `DEC-21`

`[P1 | I86/E100/R10]` **Gemini agents receive no informatics routing.** The section that points an
agent at `apex-meta/informatics/index.md` exists in `AGENTS.md` and `CLAUDE.md` and is absent from
`GEMINI.md`. Nothing detected it. This is the same class as `D2` and `D9` — a hand-maintained copy
that silently stopped agreeing — and it is live today, independent of this contract work.

### Resolution

Installing the contract into all five surfaces does **not** create the duplication problem. The
problem is already there, across three files, with no mechanism. The contract is the occasion to
add one.

| Element | Decision |
|---|---|
| **Owner** | `AGENTS.md` — the cross-tool convention, and the file the other two already mirror |
| **Carriers** | `CLAUDE.md` and `GEMINI.md` carry a byte-identical copy of the contract block |
| **`.claude/CLAUDE.md` and `.github/copilot-instructions.md`** | Out of the copy set — different content, different job. They get a pointer, not the block |
| **Mechanism** | A test asserting the contract block is byte-identical across the three carriers. Same pattern that closed `D9`: one owner, mechanical verification, no trust in discipline |

### Why a test and not `@path` imports

Imports would give one copy instead of three, which is structurally better. Rejected for three
reasons, all checkable:

1. **No instruction file in this repository uses an import today** — verified by grep. It would be a
   new mechanism, not an existing one.
2. **Not all five tools support it.** Claude Code does; Copilot and Gemini conventions do not
   reliably. An import that silently no-ops on two surfaces is worse than a verified copy.
3. **The suite's own P0 rule forbids it** — `index.md` and the router both state *"Zero eager @path
   imports."* Using one for the contract would require a carve-out in a P0 invariant, and the rule's
   intent (do not eagerly pull in knowledge modules) is sound even if an always-on contract is a
   legitimate exception.

**Remaining open:** `RP-03` should be asked whether cross-tool instruction files have a current
standard mechanism for staying in sync that this analysis has missed. If one exists, revisit.

### Standalone CLI Loader Behavior & Rejection of Naive Option C Stubs

An alternative proposal (Option C: "Carrier Role Hierarchy") suggested making `AGENTS.md` the sole master contract and reducing `CLAUDE.md` and `GEMINI.md` to pointer stubs. Empirical testing across CLI harnesses proves naive stubs fail catastrophically:
1. **Claude Code CLI Default**: In standard Claude Code CLI (>=2.1.277), `AGENTS.md` is **completely ignored** if `CLAUDE.md` exists in the repository root or `.claude/`. A pointer stub in `CLAUDE.md` strips all contract governance from Claude Code CLI agents.
2. **Gemini CLI Default**: Gemini CLI ignores `AGENTS.md` by default unless explicitly configured in `context.fileName`. A stub in `GEMINI.md` leaves Gemini agents unguided.
3. **IDE / Injector Inability**: Neither Antigravity, Cursor, Windsurf, nor VS Code Copilot execute CLI preprocessor `@import` directives.

Therefore, **Option A (byte-identical synchronization via pytest) remains the sole safe universal baseline today**.

### Dual-Carrier Injection Warning & Harness Configuration

**WARN**: Google Antigravity injects both `AGENTS.md` and `GEMINI.md` simultaneously into system context as separate `<RULE>` blocks. Under Option A byte-identical sync, this results in double-loading the contract block (~2,572 BPE tokens).
- **Harness Guidance**: For Antigravity environments, operators should configure `context.fileName: AGENTS.md` to prevent duplicate loading of `GEMINI.md`.
- **Long-term**: Multi-repo distribution should utilize build-time single-source compilers (DITA projection model) rather than runtime pointer stubs.

---

## Part G — Test queue

Everything below is **marked for testing before adoption**, at operator instruction. Status
`NEEDS_TEST` means: the reasoning is recorded, the artifact exists, and it must not be installed
until evidence exists. Test vehicle is
[04-empirical-test-protocol.md](04-empirical-test-protocol.md) unless stated otherwise.

| ID | Item | What must be shown | Falsified if |
|---|---|---|---|
| **DEC-17** | **Named tags vs bullets** — **DECIDED: named tags.** Operator decision on clarity grounds, measured cost 17 tokens. Still queued as a *confirmation* test, not a blocking one | Whether per-rule tags measurably worsen rule application | Tags measurably worse → revisit; otherwise the operator's clarity preference stands |
| **DEC-18** | `<surgical>` always-on stub | Whether the 18-token stub is needed, i.e. whether whole-file rewrites occur when patch discipline is gated only | Gated-only shows no rewrites → **drop the stub** |
| **DEC-19** | `<stop_repairing>` placement | Whether an agent inside a repair loop acts on an always-on stopping rule at all, and whether gating it would be worse | Ignored in both placements → the rule needs a different mechanism entirely, not a different location |
| **DEC-20** | `<new_machinery>` + `<detour>` as the drift replacement | Whether observable-action gates actually fire before drift, where the self-diagnosis gate could not | Agents add scripts and propose detours without the gates firing → **the observable-action principle fails** and drift needs a non-instruction mechanism |

### `DEC-17` — current evidence, pending the local test

Literature is **mixed and does not support per-rule tags here**:

- XML's measured benefit is in **separating heterogeneous content** — instructions from reference
  data — because *"when a section has no defined end, the model has to guess where your reference
  text stops and your instruction resumes"*
  ([XML vs Markdown](https://www.ud.com.hk/en/blogs/insight/article/xml-tags-prompting-2026-07-15)).
- For short homogeneous instruction content, measured results go the other way: one test found XML
  **marginally worse** on accuracy (96.4% vs 97.6%) while adding **31% input token overhead**
  ([XML Tags Don't Help Short Prompts](https://dev.to/manishramavat/xml-tags-dont-help-short-prompts-heres-when-they-actually-matter-2026-25gf)).
- Published guidance: *"Use Markdown when the prompt is mostly instruction prose, because it costs
  the fewest tokens"* ([Structured Prompting](https://www.ml4devs.com/what-is/structured-prompting/)).

**Our `<always>` content is ten homogeneous one-line rules with no embedded reference text** — the
case where the evidence says tags are not indicated. The gated blocks are the opposite case: they
carry `when` / `ref` / `deepen_when` attributes, which Markdown cannot express at all.

### `DEC-17` — RESOLVED: named tags

**Operator decision: named tags, because they read more clearly.**

The evidence above argues against tags for this content type, but it argues on **token-efficiency**
grounds — and the measured difference here is 17 tokens, 1.3% (`DEC-C2`). At that magnitude the
efficiency argument has no force, and the decision turns entirely on clarity, which is the
operator's call and which named tags win.

Recorded honestly: **this decision goes against the literature's direction while being consistent
with its magnitude.** The published results showing XML worse (96.4% vs 97.6% accuracy) came with a
31% token overhead; our overhead is 1.3%, so that trade is not the one being made here. Kept in the
test queue as a **confirmation** test rather than a blocking one — the block ships with tags unless
the test shows them actively harmful.

**Consequence:** the `v0.4` block in
[07-contract-block-v0.4.md](07-contract-block-v0.4.md) uses one named tag per rule throughout.

### Operator-verified

| Item | Status |
|---|---|
| `anti-drift-rules.md` now has **no inbound gate**; its strongest rules were promoted to the always-on tier and the file becomes a deep-review artifact rather than a runtime one | **VERIFIED by operator** — deliberate role change, accepted |

### Standing correction on "the tokens are gated, so this is fine"

Recorded here because it changes how the 1,306 figure should be read.

**Gated blocks inside an always-on file are still loaded every session.** `when=` does not defer
their cost — all 1,306 tokens are paid on every task, matching rule (`DEC-M1`). What the gate buys
is (a) the agent not opening the referenced module file, worth 2,400–4,200 tokens, and (b) fewer
instructions competing for compliance.

So "it's gated, therefore fine" holds for the **downstream** files, not for the contract itself. If
1,510–1,556 is acceptable, it must be acceptable as a flat per-session cost (mitigated by 78.5%–90% prompt-cache read discounts on unchanged prefixes per `RP-09`).

---

## Part H — Finalized `v1.0` Decisions After `ResearchOfFile10` (`DEC-22`..`DEC-24`)

Recorded after evaluating [RESULTS-01](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md) through [RESULTS-11-synthesis.md](ResearchOfFile10/RESULTS-11-synthesis.md) (see [FinalizationDossier/00-research-critique-and-architecture-design.md](FinalizationDossier/00-research-critique-and-architecture-design.md)).

| ID | Decision | Grounding & Consequence | Status |
|---|---|---|---|
| **DEC-22** | **Two-Layer Separation & `base_ref="apex-meta/informatics/"` Portability (`Option 2A` + `5A`)** | [RESULTS-09](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md) & [RESULTS-10](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-10-surface-layering.md) (Rank 1 & Rank 3). Layer 1 (`<apex_contract v="1.0" base_ref="apex-meta/informatics/">`) declares the bundle path once on the root tag and uses short relative `ref="..."` filenames inside the block (saving ~25 tokens and making Layer 1 100% portable across repositories). Layer 2 (Live Infrastructure Banner, WSL2 ext4/`/mnt/c` constraint, Completion Reporting) resides outside `<apex_contract>` in the same file ([03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md)). Also retains `DEC-21` physical byte-identical carriers across `AGENTS.md`, `CLAUDE.md`, and `GEMINI.md` (Option A) as the sole safe baseline today because naive Option C stubs fail in standalone CLIs (Claude Code CLI ignores `AGENTS.md` when `CLAUDE.md` exists; Gemini CLI ignores `AGENTS.md` by default) and IDE rule injectors ignore CLI `@import` preprocessors. Accompanied by explicit `WARN` on Antigravity dual-carrier injection and operator guidance (`context.fileName: AGENTS.md`). | `FINALIZED_V1` |
| **DEC-23** | **Ratify Candidate `3A` as Sole Production Blueprint Default & Relegate `3B` to Benchmark Arm B2** | [RESULTS-03](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-03-currency-check.md), [RESULTS-06](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-06-condition-syntax.md), [RESULTS-08](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-08-deepen-when-mechanics.md), [RESULTS-09](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-09-efficiency-audit.md), and Challenger 2 stress-test. Dropped all 5 unparsed `deepen_when=` attributes and preserved 100% of their second-threshold escalation triggers via concise inline `Open ref for ...` cues across all 6 `ref=` rules (`<editing>`, `<authoring>`, `<trade_off>`, `<handover>`, `<iterative>`, `<schemas>`). Formally ratifies [13-candidate-3A-xml.md](13-candidate-3A-xml.md) (`1,632` repo tokens / `1,350` BPE) as exclusive production blueprint default for `AGENTS.md`. Relegates [14-candidate-3B-hybrid.md](14-candidate-3B-hybrid.md) (`1,586` repo tokens / `1,314` BPE) to experimental benchmark Arm B2 in [04-empirical-test-protocol.md](04-empirical-test-protocol.md) because `3B` saves only 36 BPE tokens (2.67%) and zero prompt-cache blocks while suffering table pipe-escaping fragility (`\|`) and cell wrapping under narrow viewports. | `FINALIZED_V1` |
| **DEC-24** | **Empirical Wording Upgrades for `<target>`, `<communication>`, and `<new_machinery>` (`RP-04`, `RP-05`, `RP-07`)** | (1) `<target>` ([RESULTS-05](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-05-self-authored-criteria.md) *SpecBench* & [RESULTS-07](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md) *FixedBench*): adds positive requirement-by-requirement final validation check, treats self-authored tests as supporting evidence rather than replacement criteria, and explicitly legitimizes concluding *"no change is needed"*. (2) `<communication>` ([RESULTS-04](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-04-register-terminology.md)): adopts **Insights Discovery Cool Blue** analytical register and replaces `"No hedging"` with `"State uncertainty plainly when evidence is incomplete; avoid empty hedges"`. (3) `<new_machinery>` ([RESULTS-07](ResearchOfFile10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-07-over-building.md)): requires naming the exact requirement, blocker, or material risk before adding scripts, tests, gates, or abstractions. Synchronized into canonical library modules (`writing-profile.md` & `anti-drift-rules.md`). | `FINALIZED_V1` |

---

## Provenance

| Source | What it settled |
|---|---|
| [../DeepReasoning/04-consolidated-patch-and-verification.md](../DeepReasoning/04-consolidated-patch-and-verification.md) | Part A, all `APPLIED` entries |
| [../DeepReasoning/05-architecture-and-context-budget.md](../DeepReasoning/05-architecture-and-context-budget.md) | Rule of Three analysis behind `DEC-11` |
| [../DeepReasoning/06-how-the-routing-actually-works.md](../DeepReasoning/06-how-the-routing-actually-works.md) | `DEC-14`, `DEC-15`, `DEC-W2` |
| [../DeepReasoning/07-candidate-always-on-block.md](../DeepReasoning/07-candidate-always-on-block.md) | `DEC-13`, `DEC-16`, all of Part D |
| [08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md](../../../../handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md) | The operator's original design intent; corrected `DEC-W2` |
