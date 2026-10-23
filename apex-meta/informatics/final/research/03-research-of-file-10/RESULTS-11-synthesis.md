---
type: Reference
id: RESULTS-11-synthesis
title: Ten-Packet Research Synthesis - Decisions, Evidence, and Tests
description: Cross-packet falsification review, token arithmetic, and evidence-led next experiment for the always-on contract candidate.
status: current
tags: [research-result, synthesis, decision-review, evidence]
---

# Ten-Packet Research Synthesis - Decisions, Evidence, and Tests

**Research period:** 2026-10-20 to 2026-10-21. **Repository:** `leela-spec/apexai-os-meta`, branch `main`. **Scope:** research only; no candidate contract, decision register, live rule, or instruction entrypoint changed. The ten packet findings are in neighboring `RESULTS-01` through `RESULTS-10` files. The source of each numerical scenario is the **original repository input**, not an independently reproduced tokenizer run. **Overall confidence:** high for observed repository text, vendor-supported loader options, and the arithmetic; medium for the recommended architecture; low for actual file-reading behavior in the operator's local harnesses.

## Executive decision - what research changes

**The architecture should be revised, not abandoned or installed as-is.** Keep essential, unconditional, operator-defined invariants always available. Separate portable *universal behavior* from repository-specific facts. Use one canonical owner and **verified tool-specific loading adapters** rather than three independently edited copies where native import or configurable loading is supported. Use native path-scoped rules or skills for conditional detail when their loader behavior can be demonstrated. Keep the custom `when=`/`deepen_when=` routing concept as an **untested hypothesis**, not runtime-enforced conditional logic.

**Token count is not the primary success variable by itself.** Current OpenAI API prompt caching discounts matching repeated prefixes, with GPT-5.6+ eligible prefixes priced differently for cache creation and reuse. But caching is not free, may miss, still consumes context, and does not correct rule interference or missed work. The correct optimization target is **specified requirements successfully delivered per total model/tool cost, agent actions, and elapsed time**, with token size as one observed component. This is a design recommendation, not measured local economics. [OpenAI prompt caching](https://developers.openai.com/api/docs/guides/prompt-caching); [ETH coding-agent context study](https://arxiv.org/abs/2602.11988).

**Do not enforce a ~1,000-token limit based on the present evidence.** The current candidate is reported at **1,622 tokens**. No tested, rule-preserving ~1,000-token replacement exists. The claim that **1,476** is a hard minimum is also unsupported: the local author measured **three rules** in alternate serializations, then projected a possible ~190-token whole-block saving. That predicts a **~1,432** table candidate; no complete table candidate was independently tokenized or behaviorally tested in this run. Neither figure is an established full-contract minimum. Sources: [`09-contract-block-v0.5.md` §4](09-contract-block-v0.5.md), [`05-research-prompt-packets.md` RP-06 and RP-09](05-research-prompt-packets.md).

## Packet-by-packet outcome (handover execution order)

| Order | Packet | Result | Evidence status / effect |
|---:|---|---|---|
| 1 | **RP-01** Gating efficacy | No controlled evidence found that custom XML `when=` prevents a coding agent from reading nonmatching files. | **Unverified**; retain A/B/C/D read-trace experiment. |
| 2 | **RP-10** Surface/loading and layering | `AGENTS.md` has real multi-tool adoption but is not automatically read in all existing five-file setups. Claude with `CLAUDE.md` defaults away from it; Gemini defaults to `GEMINI.md`. | **Vendor-documented**, not local launch-traced; revise `DEC-21`. |
| 3 | **RP-02** Vector retrieval | Retrieval can discover optional guidance but cannot assure application of every invariant; hybrid unconditional core plus native scoped detail is preferable. | **Mechanistic high confidence**, little direct production instruction-RAG measurement. |
| 4 | **RP-09** Efficiency | Caching changes repeated-input pricing; the claimed floor is unsupported; no verified ~1,000 replacement. | **Caching documented**; whole-block savings **not replicated**. |
| 5 | **RP-03** Currency | Three loading tiers remain useful, but universal 1,000-token target, positional folklore, and manual routing primacy are unproven. | **Evidence-informed**, version-specific. |
| 6 | **RP-08** `deepen_when` | A text hint to the model, not an executable switch. The actual v0.5 has **five**, not six or nine, instances. | **Literal file inspection**; claimed 99-token savings require recount. |
| 7 | **RP-06** Syntax | A three-rule local table costs 190 versus 221 XML tokens; full-block ~190 saving is **extrapolated**. Compliance unknown. | **Partial measurement only**; retain current format pending trial. |
| 8 | **RP-05** Self-authored criteria | Prefer an observable final comparison with the user's explicit requirements, not agent-authored test passing as success. | **Failure measured**, precise directive not experimentally validated. |
| 9 | **RP-07** Over-building | Product/outcome scope and legitimizing no-op when already correct are better starting points than a purely ceremonial pre-action gate. | **Controlled action-bias evidence**, local wording untested. |
| 10 | **RP-04** Communication term | The recalled color model is most probably **Insights Discovery Cool Blue**, but it is a personality descriptor, not a controlled AI writing standard. | **Term verified**, memory match inference; keep concise descriptive rule. |

Primary supporting sources: [Claude Code loader precedence](https://code.claude.com/docs/en/memory); [Gemini CLI context rules and imports](https://github.com/google-gemini/gemini-cli/blob/main/docs/cli/gemini-md.md); [GitHub Copilot instructions](https://docs.github.com/en/copilot/concepts/prompting-and-context/custom-instructions); [Gloaguen et al., 2026](https://arxiv.org/abs/2602.11988); [McMillan, 2026](https://arxiv.org/abs/2605.10039); [FixedBench](https://arxiv.org/abs/2605.07769).

## 1. Literal check against the Part F pre-registered falsification conditions

The file [`01-decision-register.md`, Part F](01-decision-register.md) pre-registers **six conditions**. Research evidence is not a substitute for the **specific experiment named in each condition**. Consequently, *not triggered* means **not falsified and not confirmed**.

| Recorded position | Pre-registered falsifier (faithful restatement) | Evidence obtained / strict outcome |
|---|---|---|
| **DEC-12** always-on invariants | Agent with candidate fails an invariant that full module restatement would enforce. | **NOT TRIGGERED.** No paired behavioral comparison of candidate vs full-module restatement. Keep proposed; do not install. |
| **DEC-13** reduced-form rules | Same authoring task performs measurably worse under the 721-token reduced contract than under the 2,845-token writing profile. | **NOT TRIGGERED.** No corresponding matched writing tasks scored. `721` describes an earlier alternative, not proof of v0.5 equivalence. |
| **DEC-16** file-boundary split | Read traces show agents open nonmatching files anyway. | **NOT TRIGGERED.** None of the A/B/C/D experimental arms have been run. The illustrative 83% read-size reduction remains conditional. |
| **DEC-M2** gating improves precision | In-scope compliance is no better when sibling rules are gated out than when present. | **NOT TRIGGERED.** `when=` has no built-in parser guarantee, but that is not a measured null effect. B-vs-C remains required. |
| **DEC-14** index is bundle index only | A real runtime path depends on reading `index.md`. | **NOT TRIGGERED.** This research did not execute every target runtime. No claimed absence proof. |
| **Whole architecture** static dispatch | Vector instruction retrieval demonstrably dominates static IF-dispatch for this use case. | **NOT TRIGGERED.** No superiority evidence for retrieval-only mandatory instructions. Native scopes are a separate architecture alternative, not proof pure vector search dominates. |

**Interpretation:** research **weakens confidence** in custom gate mechanics and finds a better-supported interoperability approach, but **does not falsify any of the six Part F hypotheses under their literal registered test conditions**. This is not a claim that the current design works. [Read-trace protocol and thresholds](04-empirical-test-protocol.md).

## 2. Every requested decision ID - surviving, revised, or awaiting experiment

| ID | Disposition | Reason and next action |
|---|---|---|
| **DEC-16** | **Unverified; hold implementation** | File-boundary token arithmetic is plausible but only realized when nonmatching files are not read. Use read traces. |
| **DEC-17** | **Operator choice survives provisionally** | Named XML tags chosen for legibility; no direct result shows materially worse rule selection. Compare full-block XML, bullet and hybrid/table on equal tasks. |
| **DEC-18** | **Unverified** | Test whether `<surgical>` remains necessary when editing detail is on demand; no evidence that gated-only avoids whole-file rewrites. |
| **DEC-19** | **Unverified** | Test repair-loop stopping in always-on vs gated form. Instructions cannot guarantee stopping. |
| **DEC-20** | **Unverified; rationale strengthened** | Action-bias evidence supports resisting needless changes, not that `<new_machinery>` / `<detour>` action gates actually fire. Measure before/after on realistic tasks. |
| **DEC-21** | **Mechanism requires revision; intent survives** | Three hand-maintained byte-identical copies are not the only viable route. Claude, Gemini and some Copilot clients offer documented imports or AGENTS loading. Existing tool-specific files remain meaningful; no deletions without loader verification. |
| **DEC-12** | **Proposed, untested** | Unconditional essential behavior does not need speculative model interpretation for activation; equivalent compliance still untested. |
| **DEC-13** | **Proposed, untested** | Reduced form must be evaluated against authoring outcome, not token count alone. |
| **DEC-14** | **Unverified** | No proven runtime dependence on index surfaced; conduct the specific runtime-path check before treating it as navigation only. |
| **DEC-15** | **Unchanged; scope-specific proposal** | Portable derivative artifact question is separate from loader mechanisms, no corresponding experiment run. |
| **DEC-M1** | **Survives in stated eager-file model** | A condition inside text already injected into context cannot retroactively subtract those input tokens. |
| **DEC-M2** | **Empirical precision claim unverified** | Gates may steer selection, but neither saved reads nor better adherence established; `B` vs `C`. |
| **DEC-M3** | **Qualify scope** | For a model that eagerly reads entire files, separately deferred material requires an actual loading boundary; native per-path/skill runtimes provide other *enforced selection mechanisms*. Do not universalize the word *only*. |
| **DEC-M4** | **Historical measurement survives, no quality proof** | 721-token earlier reduced-form candidate may exist, but must not be conflated with the 1,622-token current 22-block design or guaranteed task equivalence. |
| **DEC-M5** | **Survives unchanged** | A worked example may convey necessary behavior rather than duplicate a normative rule. Not specifically retested here. |
| **DEC-M6** | **Unaffected; not reaudited** | Prior validator limitation about in-body rule IDs was outside these research packets; no evidence to overturn original repository assertion. |

For `DEC-17`–`DEC-20`, Part G sets four additional explicit tests (tag harm, stub necessity, stop-repairing placement, and whether observable-action gates fire). **None has been run**. A literature review does not satisfy these falsifiers. [Decision register, Part G](01-decision-register.md).

## 3. Single token-consequence arithmetic ledger

**Do not add formatting alternatives to each other.** `-190` is a **projection from a three-rule test**, `-99` and `-47` are **unreplicated author-reported measures**, and the overlap among them is unknown. Each row is a **separate scenario**, not a cumulative sequence unless explicitly stated.

| Scenario / lever | Arithmetic from 1,622 | Candidate total | Evidence strength, cost or risk |
|---|---|---:|---|
| **Current v0.5; recommended operational baseline** | `1,622 - 0` | **1,622** | Repository-reported, full candidate size; already available. No behavioral test run. |
| Wording change alone | `1,622 - 47` | **1,575** | Reported local wording experiment; verify whether not already applied; risk: lost nuance. |
| Remove `deepen_when` alone | `1,622 - 99` | **1,523** | **Claimed**, five actual attributes; tokenizer effect requires remeasurement; possible missed escalation. |
| Unconditional tags to labelled bullets alone | `1,622 - 39` | **1,583** | Narrow author estimate, conflicts with operator clarity decision; **not additive** to wholesale table. |
| Wording plus depth within XML | `1,622 - 47 - 99` | **1,476** | Prior author's proposed XML scenario; verify non-overlap, counts and compliance. **Not a floor.** |
| Complete table (projection only) | `1,622 - ~190` | **~1,432** | Extrapolated from **three rules** (221 XML, 198 bullet, 190 table); **complete-block token count and compliance not measured**. |
| Full table plus wording plus depth | `1,622 - 190 - 47 - 99` | **~1,286** | **Illustrative arithmetic only**, not a verified jointly possible configuration; format and depth changes may overlap. |
| Additional gap to a 1,000-token objective from illustration | `1,286 - 1,000` | **286 still missing** | No supported, scope-preserving extra lever identified. |
| Native scoped rules or on-demand skills | **TBD**, not a justified flat subtraction | **Unknown** | Can reduce downstream material and improve scope; depends on actual loader and task. |
| Stable-prefix caching | `1,622 - 0` tokens physically | **1,622** | Can discount repeated input pricing, not context occupancy or instruction collisions; cache hit rate unknown. |
| Default-rule removal, common-condition factoring, abbreviations | **0 verified** | **Unknown** | Plausible but needs matched ablations and tokenizer checks before any real saving is claimed. |

**Recommended total now:** **1,622 reported tokens**. **Safe minimum:** **unknown**, since no smaller full candidate has won an outcome test. **Smallest quantitative projection based on a measured slice:** **~1,432**. **Lower illustrative non-additive arithmetic:** **~1,286**, **not a measured artifact**. **~1,000:** neither verified reachable nor established impossible. A hard 1,000 ceiling would be arbitrary on this evidence.

**Cache sensitivity:** On a documented GPT-5.6+ pricing example, one cache write at **1.25×** and nine cache reads at **0.1×** cost `1.25 + (9 × 0.1) = 2.15` ordinary-input equivalents instead of ten, a **78.5% reduction for that exact repeated-prefix pattern**. The result is conditional on eligibility, unchanged prefix, TTL, request pattern and provider/model. It is **not** a local measured saving and **not** a reduction in input tokens used as context. [OpenAI](https://developers.openai.com/api/docs/guides/prompt-caching).

## 4. Contradictions and tensions preserved, not smoothed over

1. **RP-06 vs RP-09 on full-table size:** RP-06 correctly identifies a **three-rule token measurement** and an extrapolation. Any wording in RP-09 implying a measured **full** 1,432-token candidate was corrected before delivery. Neither report demonstrates safe table compliance. `DEC-17` clarity choice is not invalidated by a size-only projection.
2. **RP-08 vs RP-09 on `deepen_when`:** RP-08 favors *testing without* the additional depth hint and provisionally dropping it; RP-09 recommends leaving the deployed block unchanged until behavior is known. Reconcile as **candidate ablation, not immediate live deletion**. Five actual depth attributes versus six/nine described elsewhere makes the 99-token projection unreliable until recount.
3. **RP-01 vs RP-08:** Both agree markup is text unless a harness parser implements it; RP-08 can explain a plausible semantic benefit, while RP-01 finds no demonstrated agent file-read gate. Explanation is not validation.
4. **RP-02 vs RP-03/RP-10:** Rejecting *vector-only* invariant delivery does not mean custom IF dispatch is optimal. Native path-specific loaders, skill metadata, or compile-time filters offer a third mechanism.
5. **`DEC-21` vs vendor capabilities:** Imports can avoid hand-maintained duplicates, but existing `CLAUDE.md` takes precedence over native `AGENTS.md` by default, Gemini defaults to `GEMINI.md`, and Copilot product modes vary. The **same canonical source** does not automatically imply **one physical file** or **guaranteed equivalent model input**.
6. **Instruction minimization vs safety/quality:** The [ETH context-file study](https://arxiv.org/abs/2602.11988) reports extra instructions can worsen outcomes/cost, but no paper identifies which specific `target`, `scope`, `ground` or `surgical` clause can safely disappear from *this* operator contract. Trim only after an ablation meets the actual requirement.

## 5. What to test locally next (in priority order, without implementing changes now)

1. **Loader reality check (RP-10):** Record installed `claude --version`, `gemini --version`, Codex/Copilot client variants, project settings, and the *exact loaded instruction files* in their inspection commands. Confirm root and `.claude/CLAUDE.md` precedence; Gemini `/memory show`; Claude `/context`; Copilot `/instructions`. Verify that any proposed `@AGENTS.md` import works before altering carriers. Record present `GEMINI.md` missing section as a separate defect, `D10`.
2. **Registered A/B/C/D read trace (RP-01, DEC-16, DEC-M2):** Use [`04-empirical-test-protocol.md`](04-empirical-test-protocol.md) unchanged as the pre-registration: A baseline; B gated XML; C same content/refs without gate attributes; D gated plus physical file splits. Score both unnecessary and missing reads, task outcome, token/tool cost, and reproduction. Apply its **B bloat <20% plus B>C by >15pp** success criterion; **B bloat >40%** or **D ≈ B** are registered grounds to reject the split. Do not invent a favorable new cutoff after seeing traces.
3. **Serializations and depth hint (RP-06/RP-08):** Using the *same full v0.5 source* and tokenizer, measure paired XML, IF bullets, full table, and hybrid; separately remove the five real `deepen_when` occurrences. Hold semantics and paths constant. Evaluate read decisions and completion accuracy, not just token count.
4. **Output/criteria integrity and overbuilding (RP-05/RP-07):** Provide exact operator acceptance conditions and a preexisting test suite that can pass despite an unfinished user-visible deliverable. Compare original `<target>`, positive requirement-based validation, and an evidence/acceptance matrix. Include tasks already fixed, partially fixed, and genuinely broken; score false edits **and** false abstention. [FixedBench](https://arxiv.org/abs/2605.07769); [SpecBench](https://arxiv.org/abs/2605.30314).
5. **Part G targeted ablations:** Exercise `DEC-17` (tags vs bullets), `DEC-18` (whole-file rewrite rate), `DEC-19` (stop-repairing in loops), `DEC-20` (new machinery and detour triggers) using the registered failure conditions, not agent self-reports.
6. **Behavioral equivalence of reduced forms:** Compare `DEC-12` and `DEC-13` variants on identical authoring tasks, including 2,845-token full writing profile vs earlier 721-token reduced candidate and latest 1,622-token candidate. Preserve operator requirements as ground truth.
7. **Real cost instrumentation (RP-09):** For typical repeated tasks collect actual `cached_tokens`, cache writes, full input, output, tool calls, latency and product success. Compare **cost per successful task**, distinguishing first request from subsequent reuse.

These tests must be **planned and run in the operator's actual agent environment**; the literature review does not substitute for them. Do not add permanent scripts or change the live contract merely to record this recommendation.

## 6. Proposed directions for the operator's later decision (not edits)

- **Instruction ownership:** One human-reviewable universal source, visibly separated from repository-specific facts, with tool-specific pointers/imports or generated copies only where loader compatibility justifies them. Existing P0 prohibition against eager `@path` imports requires an explicit operator exception or an alternative verified strategy; do not bypass it.
- **Selective depth:** Short unconditional requirements always present; scoped detail brought by documented loader/skill mechanisms or a tested conditional read. Tool-independent critical invariants are **not** optional nearest-neighbor search hits.
- **Target/completion:** For completion, verify each user-stated requirement with direct evidence; do not equate the passing of an agent-authored test to satisfaction of the user request. Keep permission to conclude that *no code change is required* when evidence supports it.
- **Communication:** Use concise, evidence-first, precise prose. `Cool Blue` may label the inspiration, but cannot replace the explicit writing rule across agents and cultures. [Insights Discovery](https://blog.insights.com/en-us/blog/your-guide-to-communicating-with-cool-blue-energy).
- **No token-first implementation:** A measured 190-token saving is insignificant if it reduces task success; a stable cached 100-token saving may be financially marginal next to wasted explorations. Preserve clarity until paired outcome data warrants changes.

## 7. Unknowns and out-of-scope notes

**Unknown:** reliable custom XML gate-compliance rate; local tool versions and file-precedence traces; complete retokenized alternate contract; accuracy impact of removing any current rule; actual cache hits in this repo; universal cross-client include behavior; local 22-rule minimum; causal improvement from the exact recommended anti-overbuilding or acceptance-criteria wording.

**Outside scope, reported without changing anything:** `D10` in the existing instruction-surface map: repository root `GEMINI.md` lacks `## Informatics & Knowledge Routing`, a section present in `AGENTS.md` and root `CLAUDE.md`; [source map](11-instruction-surface-architecture.md). Live-file repair is a separate implementation decision, explicitly prohibited by this research handover.

## 8. Completion check and provenance

Research packets: **10/10** in the required order; progress ledger: **one row each**; synthesized positions: Part F **6/6**, Part G **4/4**, mechanical `DEC-M1`…`DEC-M6` **6/6**; outputs: **the 10 packet files, this synthesis, and the progress ledger**. All present findings are **research results, not product changes**. No complete agent-harness empirical test has been run. The relevant pre-existing source artifacts are [`05-research-prompt-packets.md`](05-research-prompt-packets.md), [`09-contract-block-v0.5.md`](09-contract-block-v0.5.md), [`01-decision-register.md`](01-decision-register.md), [`04-empirical-test-protocol.md`](04-empirical-test-protocol.md), and [`11-instruction-surface-architecture.md`](11-instruction-surface-architecture.md). The synthesis cites these **source documents and external primary material**, not the newly authored research result files, as evidence.
