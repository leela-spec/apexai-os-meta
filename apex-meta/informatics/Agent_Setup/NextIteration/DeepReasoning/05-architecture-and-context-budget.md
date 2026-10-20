---
type: Reference
id: DR-ARCHITECTURE-BUDGET-v1.0
title: Instruction Architecture, Context Budget & Duplication Policy
description: The design model behind the Apex Informatics suite — progressive disclosure levels, measured token budget, user-story load flows, and an established-practice duplication policy with the open strategic decisions left for the operator.
status: current
tags: [architecture, context-budget, progressive-disclosure, duplication-policy, decisions]
---

# Instruction Architecture, Context Budget & Duplication Policy

**Bottom line:** the suite is a **two-level system that needs to be three-level**. Almost every
question about duplication — including the one I answered badly — dissolves once Level 3 exists.
And by the established rule for when to extract shared content, **I under-deduplicated: 8 concepts
cross the threshold and I left all of them in place.**

---

## 1. The Mental Model: these files are services, not documents

The single most useful reframe: **each module is a service, and "loading" is its deployment.**

The router dispatches a task to exactly one module. That module then has to do its job with what
it contains. This is structurally identical to a microservice handling a request with what it has
deployed — and the microservice literature has already fought out every tradeoff here.

| Microservices concept | Informatics equivalent |
|---|---|
| Service | A module file (`writing-profile.md`, `execution-modes.md`, …) |
| Independent deployability | **Independent loadability** — one gate fires, one file loads, the task completes |
| Shared library | A `Canonical: WP-07` pointer forcing a second file read |
| Bounded context | The module's domain (prose, architecture, adapters, drift, schemas) |
| Schema registry | `patch-intent-schema.json` — one artifact, many consumers, versioned outside all of them |
| API call to another service | Reading a Level 3 reference file |

The governing finding from that literature: *"Shared code libraries can break two of the rules of
microservices: bounded contexts and independent deployability"* and *"it's acceptable to accept
redundancy in order to stay independent"*
([Hamid Shahid](https://hamidshahid.blogspot.com/2018/08/the-curious-case-of-shared-libraries-in-microservice-architecture/),
[Philipp Hauer](https://phauer.com/2016/dont-share-libraries-among-microservices/)).

That is the premise I asserted and failed to justify in the review packet. Written out properly:

> **Premise:** a module that cannot complete its domain without reading a second module has lost
> independent loadability. Under a one-gate-one-file router, that costs a full extra module load
> (2,500–4,200 tokens) to save a restated line (~30 tokens). An ~80× loss.

But the same literature gives the **two exceptions**, and those are what I should have applied:

1. *"It's okay to have libraries for technical concerns… as long as the common library does not
   contain domain-specific code."* → Cross-cutting definitions (what `P2` means, the I/E/R scale)
   are technical concerns, not domain logic. Shared reference is correct for them.
2. *"If code contains shared business logic, it's best to encapsulate it in a dedicated
   microservice that exposes its functionality via an API."* → This is the registry pattern, and it
   is exactly the `patch_intent` fix: one authoritative artifact, consumed by reference.

---

## 2. Progressive Disclosure: the three-level model

The canonical structure is Anthropic's own Agent Skills design
([Engineering at Anthropic](https://www.anthropic.com/engineering/equipping-agents-for-the-real-world-with-agent-skills),
[Agent Skills docs](https://platform.claude.com/docs/en/agents-and-tools/agent-skills/overview)):

| Level | What | When loaded | Convention |
|---|---|---|---|
| **L1 Metadata** | Name + description | **Always**, in the system prompt | ~100 tokens per skill |
| **L2 Body** | The instructions | On trigger | **under ~5,000 tokens** |
| **L3 Resources** | References, scripts, schemas, examples | Only when actually read | **zero cost until opened** |

The split rule: move content to L3 when the body *"becomes unwieldy"*, when contexts are
*"mutually exclusive or rarely used together"*, or to *"reduce the token usage"* — keeping
*"the core of the skill lean"*.

### Where Apex actually sits

| Apex artifact | Intended level | Measured | Verdict |
|---|---|---:|---|
| `CLAUDE.md` + `.claude/CLAUDE.md` + `AGENTS.md` | L1 always-on | **3,031** | **50% over** the suite's own ~2,000 Control Plane orientation |
| `.claude/rules/informatics.md` | L1 scoped | 320 | Healthy |
| `index.md` | L1 domain router | 959 | Healthy |
| `writing-profile.md` | L2 | 2,845 | OK |
| `file-architecture.md` | L2 | 2,498 | OK |
| `execution-modes.md` | L2 | **4,216** | **84% of the L2 ceiling** |
| `anti-drift-rules.md` | L2 | 2,457 | OK |
| `governance-schemas.md` | L2 | 2,719 | OK (was 4,068) |
| `patch-intent-schema.json` | **L3** | 1,720 | ✅ The suite's only true L3 asset — created by this pass |

**The structural finding: there is no Level 3.** Everything that should be a reference file —
worked examples, canonical tables, data dictionaries, schema definitions — lives inline at L2.
That is why modules weigh 2.5–4.2k instead of ~1.5k, and it is why "duplicate or pointer?" felt
like a forced binary. It was a forced binary, *because the third option did not exist in this
architecture.*

---

## 3. The Token Budget, measured

### 3.1 Fixed cost, every session

```
CLAUDE.md                     1,005
.claude/CLAUDE.md             1,028
AGENTS.md                       998
                              ─────
always-on subtotal            3,031   ← before any task-specific content
.claude/rules/informatics.md    320   ← +when touching apex-meta/informatics/**
                              ─────
                              3,351
```

### 3.2 User stories — what actually loads, and what it costs

**Story A — "Write a specification for the new deployment workflow."**

```
always-on                                3,031
.claude/rules/informatics.md               320   (path matched)
index.md                                   959   (route)
  gate: writing_or_documentation
writing-profile.md                       2,845   (L2)
                                         ─────
                                         7,155 tokens before the first word is written
```

**Story B — "Patch `execution-modes.md` to add a new adapter."** The expensive path:

```
always-on + scoped + index               4,310
execution-modes.md                       4,216   (L2 — patch discipline)
                                         ─────
                                         8,526 tokens of instruction overhead
```

If that same task also needs the frontmatter contract, it trips a second gate
(`file_creation_or_structure`) and adds **2,498** → **11,024**. That is the multi-gate case, and it
is the single biggest open question in the whole design (§6, Decision 1).

**Story C — "Emit a `patch_intent.v1` document."** The L3 pattern working correctly:

```
always-on + scoped + index               4,310
governance-schemas.md                    2,719   (L2 — operative contract, 8 table rows)
                                         ─────
                                         7,029   ← sufficient for 95% of intents
patch-intent-schema.json                 1,720   (L3 — ONLY if an exact maxLength is needed)
```

Before this pass, Story C cost **8,378** unconditionally, because the 1,200-token schema copy was
inline and unavoidable — *and it was the wrong schema.* That is what L3 buys: the rare-path cost
becomes opt-in, and the artifact stops drifting.

### 3.3 The real budget constraint

Research consistently finds the **effective** usable context is far smaller than the nominal
window: utilization follows a U-shaped curve with primacy and recency favoured and the middle
neglected ([Lost in the Middle](https://teapot123.github.io/files/CSE_5610_Fall25/Lecture_12_Long_Context.pdf)),
and stacking instructions produces interference where ~12% of individually-satisfiable instruction
pairs fail together ([Instruction Stacking Collapse](https://arxiv.org/pdf/2608.02639)).

So the number to optimize is not the total — it is **instruction tokens competing for attention
with the actual work**. 8,526 tokens of standing instruction on a patch task is the figure to
drive down, and the lever is *which level content sits at*, not how tersely it is worded.

---

## 4. The Duplication Policy

### 4.1 The established rule

Software engineering settled this decades ago, and the answer is **not** "never duplicate":

| Principle | Says |
|---|---|
| **DRY** (Hunt & Thomas) | Every piece of knowledge has one authoritative representation |
| **Rule of Three** (Fowler, from Don Roberts) | *Two* instances do not justify extraction; at *three*, extract ([Wikipedia](https://en.wikipedia.org/wiki/Rule_of_three_(computer_programming))) |
| **Sandi Metz** | *"Duplication is far cheaper than the wrong abstraction"* |
| **AHA** (Kent C. Dodds) | Avoid Hasty Abstractions — prefer duplication until the right abstraction is obvious ([AHA](https://code-garage.com/en/blog/discover-the-concept-of-aha-programming)) |

The Rule of Three is the operational rule. It gives a non-negotiable threshold instead of taste.

### 4.2 Applied to this suite — and I got it wrong

Counting every file in which each concept appears as a rule:

| Concept | Sites | Rule of Three says | What I did |
|---|---:|---|---|
| Substance Over Ceremony | **5** | EXTRACT | left duplicated ❌ |
| Whole-file rewrite ban | **5** | EXTRACT | left duplicated ❌ |
| Instruction parsimony | **4** | EXTRACT | left duplicated ❌ |
| Step-by-step context | **4** | EXTRACT | left duplicated ❌ |
| TARGET dominance | **4** | EXTRACT | left duplicated ❌ |
| Top-loaded primacy | **3** | EXTRACT | left duplicated ❌ |
| Durable IDs | **3** | EXTRACT | left duplicated ❌ |
| Residual name eradication | **3** | EXTRACT | left duplicated ❌ |
| Two-strike pivot | 2 | leave | left ✅ |
| Minto BLUF | 2 | leave | left ✅ |
| Primary grounding | 2 | leave | left ✅ |
| Command-carrying claims | 2 | leave | left ✅ |
| Checkable ambiguity | 2 | leave | left ✅ |

**8 of 13 concepts cross the threshold.** I applied the Metz/AHA half of the doctrine (prefer
duplication) without applying the Fowler half (at three, extract). My `CROSS_LINK` verdict was a
single policy applied uniformly, when the established practice is a **threshold**.

### 4.3 But "extract" does not mean "pointer"

This is the part that makes it work, and the part I missed. Extraction has a destination, and
there are two good ones:

**Destination A — the shared kernel (`index.md` §1).** `index.md` is already read on every
informatics task, to route. Anything in it is therefore **already in context when the module
loads, at zero marginal cost.** `index.md` §1 already holds four P0 invariants: TARGET dominance,
strict JIT/step context, surgical mutation, substance over ceremony — four of the eight extract
candidates. The modules restate them anyway.

> If the kernel is guaranteed loaded, every restatement of a kernel invariant inside a module is
> pure waste: it pays tokens *and* risks contradiction, and buys nothing, because the rule is
> already present.

This is DDD's **Shared Kernel** pattern — a small, explicitly-agreed core that all bounded contexts
depend on, deliberately kept tiny because changing it affects everyone.

**Destination B — a Level 3 reference file.** For cross-cutting definitions that are too bulky for
the kernel: the P0–P3 tier table, the I/E/R scale, the frontmatter schemas. A module keeps its
one-line operative rule at L2 and names the reference; the agent opens it only when it actually
needs the table.

### 4.4 The resulting policy

| Sites | Nature | Destination | Module keeps |
|---:|---|---|---|
| 1 | Anything | Stays put | The full rule |
| 2 | Anything | **Leave duplicated**, bind wording to a named owner | Both full rules |
| 3+ | Short universal invariant | **Shared kernel** (`index.md` §1) | Nothing |
| 3+ | Bulky cross-cutting definition | **L3 reference file** | One-line operative rule + reference name |
| Any | Machine-readable contract (schema, JSON, config) | **Registry** — one artifact outside all modules | The operative contract in prose |
| Any | Worked example illustrating the module's own rule | Stays in the module, or L3 if bulky | — |

That last row matters: **a worked example is not duplication.** `execution-modes.md` §2.2's
Bloc/Riverpod example illustrates `EM-06`; it does not restate it. `WP-17` mandates such examples.
Deleting them would be DRY-cargo-culting.

---

## 5. What I Think Should Change

Ranked by value per unit of risk. None of this is applied — it is a proposal for your call.

### Change 1 — Strip kernel restatements from the modules `[I88/E80/R25]`

Delete the eight kernel-invariant restatements from the five modules; keep them only in
`index.md` §1. Saves ~220 tokens per module load (~5–8% of a module) and removes eight
opportunities for contradiction.

**Blocked on Decision 1 below.** This is only safe if `index.md` is genuinely always loaded.
It also requires rewriting `test_olt_07`, which currently *asserts* the duplication by name across
five files — the tests encode the old design.

### Change 2 — Introduce a real Level 3 `[I85/E90/R12]`

Create `apex-meta/informatics/reference/` holding:

| File | Content moved from | ~Tokens |
|---|---|---|
| `ranking-scale.md` | `WP-07` tier table + I/E/R dimensions | ~300 |
| `frontmatter-contracts.md` | `FA-05`/`FA-06` YAML blocks + field tables | ~450 |
| `decision-matrix-format.md` | `EM` §2.1 structure + canonical example | ~400 |
| `bakeoff-rubric.md` | `EM` §3.1 four phases + matrix format | ~350 |

Each module keeps its one-line operative rule and names the reference. Projected L2 after:
`writing-profile` ~2,550, `file-architecture` ~2,050, `execution-modes` ~3,450. Every module
comfortably inside the ceiling, and the rare-path content becomes opt-in.

This is the change that actually moves the number — roughly **−1,500 tokens per task load**, far
more than the −807 total this pass achieved, because it attacks *level placement* rather than
wording.

### Change 3 — Fix the always-on tier `[I82/E85/R20]`

`CLAUDE.md` + `.claude/CLAUDE.md` + `AGENTS.md` = **3,031 tokens on every session in the
repository**, against the suite's own ~2,000 orientation and 2026 convention of ~100 lines for a
root instruction file. Three files each at ~1,000 tokens suggests overlap worth auditing.

Highest-leverage target in the whole repository — it is paid on *every* task, not just informatics
ones. Also the highest blast radius, which is why it is a separate decision, not a drive-by.

### Change 4 — Split `execution-modes.md` `[I70/E85/R15]`

At 4,216 tokens it is at 84% of the L2 ceiling, and its six adapters are *"mutually exclusive or
rarely used together"* — Anthropic's exact stated trigger for splitting. A patch task loads the
handover protocol, the bake-off rubric and the MMM table for nothing.

Natural split: keep the `IF`-dispatch block and the two highest-frequency adapters (patch,
iteration) at L2; move Q&A matrix, bake-off, and handover to L3 references.

Subsumed by Change 2 if Change 2 is done thoroughly.

### Change 5 — Promote rule-ID uniqueness into the validator `[I78/E90/R08]`

`D1` (duplicate `FA-04`) survived a green validator and 185 tests. My new pytest guard catches it
for this bundle only. Moving it into `okf_validator.py` as `APEX-UNIQUE-RULE-ID` extends it
repository-wide. Low risk, mechanical. This is `RBL-06`.

---

## 6. Open Strategic Calls — your decision, not mine

These are genuinely undecided. I have a lean on each but not the evidence to close them.

### Decision 1 — Is `index.md` a guaranteed kernel or an optional router? `[blocks Change 1]`

**The question:** when an agent works on an informatics task, is `index.md` *always* in context, or
only sometimes?

**Why it decides everything:** if guaranteed, kernel invariants restated in modules are pure waste
and Change 1 is free. If not guaranteed, those restatements are the only thing keeping a module
self-sufficient and must stay.

**What I actually know:** `.claude/rules/informatics.md` instructs reading it, and `test_cis_01`–
`cis_05` *simulate* routing through it. Neither is a runtime guarantee. I never verified it.

| Option | Consequence |
|---|---|
| **A. Treat as guaranteed** | Change 1 proceeds; modules shed ~220 tokens each; `test_olt_07` rewritten. Risk: an agent that skips the index loses four P0 invariants. |
| **B. Treat as optional** | Current state stands. Cost: ~220 tokens per load plus eight contradiction surfaces, permanently. |
| **C. Make it guaranteed** | Add the four kernel invariants to `.claude/rules/informatics.md` (320 tokens, already path-triggered) so they load whether or not the index is read. Then strip them from modules. |

**My lean: C.** It converts an assumption into a mechanism. The scoped rule file is already
path-triggered, so the kernel genuinely becomes always-on for informatics work, and the modules can
shed the restatements safely. Costs ~120 tokens in a file that is already loaded.

### Decision 2 — How far do you want the Level 3 split to go? `[Change 2 / Change 4]`

**The tension:** every L3 extraction trades a guaranteed-present table for a conditional file read.
L3 is only free if the agent *correctly judges* when it needs the reference. If it guesses wrong,
it either wastes a read or proceeds without a contract it needed.

| Option | Profile |
|---|---|
| **A. No L3** | Status quo. Everything inline, nothing to misjudge, modules stay heavy. |
| **B. Conservative L3** — definitions only | Move tier table + frontmatter schemas. ~750 tokens off L2. These are *look-up* assets: an agent knows when it needs them. |
| **C. Aggressive L3** — definitions + examples + rubrics | ~1,500 tokens off L2. Reaches into content an agent may not realize it needs. |

**My lean: B.** Rule-of-three says extract, but AHA says do not over-abstract on first contact.
B moves the assets with the clearest "I need to look this up" signal and leaves the judgment-heavy
ones for after `RBL-01` produces data.

### Decision 3 — Do you want the always-on tier audited at all? `[Change 3]`

3,031 tokens on every session is the biggest single number in this analysis, and it is outside the
informatics bundle. Touching `CLAUDE.md` / `AGENTS.md` changes behavior for every task in the
repository, including the orchestration systems I have not examined.

| Option | Profile |
|---|---|
| **A. Leave alone** | Zero risk. The largest inefficiency stays. |
| **B. Audit, propose, do not apply** | I produce an overlap map and a proposed diff; you decide. |
| **C. Audit and apply** | Fastest, highest blast radius. |

**My lean: B.** Same shape as the work you just reviewed, and the control-plane blast radius argues
for a proposal rather than an applied patch.

### Decision 4 — Should the tests enforce the architecture, or follow it?

`test_olt_07` asserts "Substance Over Ceremony" appears in five specific files. That is a test
asserting *duplication*. It will block Change 1 by design.

| Option | Profile |
|---|---|
| **A. Tests encode current design** | Every architectural change requires a test change. Honest, but tests stop being independent evidence. |
| **B. Tests assert behavior, not placement** | Rewrite to "every module must be executable standalone" — checking that a module names its invariants *or* the kernel does. Harder to write, survives refactors. |

**My lean: B**, but it is real work and should follow Decision 1, not precede it.

---

## 7. Decision Summary

| # | Decision | My lean | Blocks |
|---|---|---|---|
| 1 | Kernel guaranteed? | **C** — make it guaranteed via the scoped rule file | Change 1 |
| 2 | How far for L3? | **B** — conservative, definitions only | Changes 2, 4 |
| 3 | Audit always-on tier? | **B** — propose, do not apply | Change 3 |
| 4 | Tests: placement or behavior? | **B** — behavior, after Decision 1 | Change 1 |

Nothing in §5 or §6 is applied. The suite currently sits at the state described in
[04-consolidated-patch-and-verification.md](04-consolidated-patch-and-verification.md).
