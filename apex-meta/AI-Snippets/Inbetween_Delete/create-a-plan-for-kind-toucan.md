# Two plans, both live

**Part A** is the repo-improvement plan — the substantive proposal, and the **hypothesis the research
must test**. It is not executed yet.

**Part B** is what we execute now: persist Part A and all its evidence into the repo, then build the
Pro Thinking prompts that submit Part A to independent external scrutiny.

Part A is a *source document* for Part B. Neither replaces the other.

---
---

# PART A — Repo improvement plan (the hypothesis)

> Status: **proposed, not executed.** Every recommendation below is my own analysis and carries my own
> confidence scores. Part B exists because those scores are unverifiable by the operator.

## A.1 Context

Three guardrails were set by the operator, and they are the acceptance criteria:

1. **Do not build a guardrail on top of something itself broken.** Fix the core problem.
2. **Do not overengineer.** The target is documentation where agents have clear orientation and indexes
   that get iteratively more precise — the original Macro/Meso/Micro intent.
3. **Everything is open.** No repo rule constrains this plan.

**The diagnosis:** the repo optimized for *proving correctness after the fact* and never built the thing
that makes the right answer *findable*. Thirteen gates certify that a corpus which is **95% unreachable
and 24% broken-linked** is internally consistent. That is guardrail #1's failure exactly.

Every failure in the preceding work session was a **discovery** failure, not a correctness failure: a
gate-pinned file found by nearly breaking it, a generator ordering bug found by breaking it,
`docs/audits/` found by accident, `SEQ-SCORE-001` referenced in 52 files and defined in none.

**Research check:** Amazon Science (Feb 2026) measured that keyword search via agentic tool use reaches
>90% of RAG-level performance without a vector DB, and Claude Code is deliberately no-index. **So the fix
is not a retrieval system — it is making the corpus navigable and grep-able.**

## A.2 The measured problem

### Orientation

| Measure | Value |
|---|---|
| Files reachable by standard markdown links from `CLAUDE.md`/`AGENTS.md` | **42 of 859 (4.9%)** |
| Root-relative links depending on an **undocumented** base (`docs/ssot/`) | **352 of 353** |
| Plain relative links **broken** | **154 of 638 (24.1%)** |
| `docs/ssot/index.md` (the "READ FIRST") map-table links that resolve | **0 of 17** |
| Directories with an index | **30 of 185 (16.2%)** |
| Mandatory onboarding before any work | **~60,800 tokens** (realistic ~85,700) |
| — of which `docs/data-architecture/STATE.md` | **142,644 bytes = 58.7%** |
| Positive placement rules in the entire repo | **1** |
| Document kinds with **no** placement rule | **4 of 5** |
| Distinct naming conventions | **11** (5 inside `docs/ssot/decisions/` alone) |

### Macro/Meso/Micro runs backwards

| File | Commits | Intended role |
|---|---|---|
| `01_MACRO_PROGRAM_MAP.md` | **24** | broadest, most stable |
| `02_MESO_WAVE_CONTRACTS.md` | **30** | middle slice |
| `03_MICRO_PACKET_PROTOCOL.md` | **6** | narrowest increment |

Macro is **61% current-state narrative** and **violates its own contract** (declares it never duplicates
product formulas, then reproduces 20 lines of XP/TP/BP lifecycle). Meso's current slice is **8.9%** of the
file. Micro has **zero** concrete content and **duplicates itself** (27.9% JSON restated as prose). **The
real narrowing happens in the packet file, which is not one of the three.**

**Conclusion: the model is sound; the files violate it.**

### Duplication

**~94 restatements vs 6 citations across six traced facts (16:1).** Three competing XP formulas. Two live
glossaries sharing 26 headwords, cross-citing *by line number*. Glossary miss rate **80%** on terms since
2026-07-24. `SEQ-B` split across two owners with interleaved numbering. Two files named
`DECISION-SHEET-07`. `D1`–`D5` and `M1`–`M3` each defined twice.

### Tooling economics

- **5 of 13 gates test the gate scripts** — 80% of the non-flutter budget.
- **8 catches in 821 commits.** Zero in the last 17 days.
- `check_mock_contracts`: **0 catches**; input frozen 15 days.
- `generate_ssot_views --check` is a **strict subset** of `check_ssot_contracts`.
- **286 warnings → ~3 actionable facts (95:1)**, grown 81 → 286 since 2026-08-03, unnoticed.
- `_generated/materialization/**`: **231 files, 2.3 MB, 98,845 lines of churn**, and `materialization.md:63`
  already calls them *"deterministic caches… may be deleted and regenerated without loss of truth."*

### What the adversarial review corrected

My first framing said the ledgers had zero readers. **Wrong:** `scripts/status_view.py` reads all six to
render `STATUS.md` (read-order item 0 in three files); production Dart cites a ledger row as authoritative
(`path_weekly_accordion.dart:271,530`); **75% of `exists` rows** state a binding no spec states; 100% carry
notes, 94.7% distinct. **Keep the ledgers, delete the cache** — opposite value profiles.

## A.3 What Part A does NOT do

- No new register, ledger, gap tracker, index system, or retrieval engine.
- No new gate validating prose — the one addition (lychee) *replaces* two bespoke validators.
- No rewrite of the three context files; they are edited to remove what doesn't belong.
- No deletion of the materialization ledgers.
- No mass renaming beyond `decisions/`, where naming actively breaks citation.

## A.4 The changes

1. **One link convention, mechanically repaired, machine-enforced.** File-relative everywhere; state it in
   `AGENTS.md`; rewrite all 991 links; replace the two divergent bespoke validators with **lychee**.
2. **A placement + naming table** — the direct fix for misfiling. Document kind → directory → filename
   convention → required frontmatter → lifecycle. Then fix `docs/ssot/decisions/` (5 conventions; two files
   share a sheet number).
3. **Split volatile status out of the stable spine.** Macro → structure only (~7.2 KB → ~2.5 KB); Meso →
   current slice only (~20.5 KB → ~3 KB); Micro → delete the prose restating its own JSON, fix the drifted
   `globalActiveMicroPackets` invariant.
4. **Stop mandating the 142 KB narrative log.** Remove from `CLAUDE.md` required reading; keep the log.
   With change 3: onboarding **~60,800 → ~20,000 tokens**.
5. **Untrack the generated materialization cache.** 231 files; keep `_generated/status/`; scope
   `check_generated_views` to `STATUS_ROOT`; delete the duplicate gate; drop `stale-bindings.json`.
   `--rule` keeps working (verified: reads memory, not disk).
6. **One glossary, current.** Merge; canon glossary becomes a pointer; add the missing terms.
7. **An ID namespace registry**, and fix the two real collisions (`SEQ-B` dual ownership; duplicate sheet 07).
8. **Rebalance the gate tiers.** (i) Retier the 5 self-tests to run on script change only. (ii) Make
   file-level freshness advisory — 207 of 286 warnings; record a warning baseline. (iii) **Park, do not
   delete,** `check_mock_contracts` — a frozen input is why it has no catches.

## A.5 Decisions taken (operator, no preference → recommendations stand)

| # | Decision | Taken |
|---|---|---|
| Q1 | Link convention | **File-relative everywhere** |
| Q2 | `STATE.md` | **Remove the reading mandate only.** No capping, no splitting |
| Q3 | Generated cache | **Untrack all of `materialization/**`**, keep `_generated/status/` |
| Q4 | Macro/Meso/Micro | **Keep three files; move volatile status out** |
| Q5 | Gates | **Retier first and measure**, then freshness advisory; **park** the mock gate |
| Q6 | Sequencing | **Four stages, checkpoint after stage 1** |

## A.6 Verification (when Part A is eventually executed)

- Reachability re-measured: must rise from 42; broken links **0** under lychee; `index.md` 17/17 resolve.
- Onboarding recomputed: target **≤ 25,000 tokens**; `grep -cE '\b[0-9a-f]{40}\b'` in the three context
  files must be **0**.
- `git ls-files docs/ssot/_generated | wc -l` drops 233 → 2; `--rule PA-B12` still returns edges;
  `STATUS.md` still fails `--check` on a hand edit.
- Glossary miss rate re-sampled on the same 15 terms — target ≤ 2.
- Fast tier under 2s; full tier below ~96s; warning count falls from 286 with a recorded baseline.
- `python scripts/gates.py --full` green before each stage.

## A.7 Sequencing

1. Links + placement/naming table (1, 2) → **checkpoint, re-measure reachability**
2. Volatile/stable split + de-mandate (3, 4)
3. Untrack cache + gate rebalance (5, 8)
4. Glossary + namespaces (6, 7)

## A.8 Sources

[llms.txt](https://www.agentpatterns.ai/standards/llms-txt/) ·
[Diátaxis](https://diataxis.fr/) ·
[AGENTS.md spec](https://asdlc.io/practices/agents-md-spec/) ·
[Write the Docs principles](https://www.writethedocs.org/guide/writing/docs-principles/) ·
[Context engineering](https://sourcegraph.com/blog/context-engineering) ·
[Semantic search vs grep](https://particula.tech/blog/semantic-code-search-vs-grep-coding-agents) ·
[lychee](https://github.com/lycheeverse/lychee) ·
[Generated files in git](https://kentcdodds.com/blog/why-i-dont-commit-generated-files-to-master)

---
---

# PART B — Persist the evidence, commission the research (execute now)

## B.1 Why

The operator's response to Part A was decisive and correct:

> *"Sadly your questions and recommendations don't mean anything to me… you have guided me into wrong
> paths for so long."*

A recommendation I score `(I88/E92/R12: 89)` is unverifiable by the operator — the score is my own
assertion about my own analysis. **The fix is independent external research that treats Part A as a
hypothesis to be tested, not a conclusion to ratify.**

## B.2 What gets written

```
docs/ssot/architecture/repo-infrastructure-research-2026-08-18/
├── 00-INDEX.md            the map — every artifact, what it holds, how to use it
├── 01-EVIDENCE.md         all four agent reports verbatim, each number with its command
├── 02-HYPOTHESIS.md       PART A in full — the proposal under test
├── 03-ANALYSIS.md         my synthesis, the six option sets with scores, and §B.4
├── 04-WEB-RESEARCH.md     searches run, findings, full source list
└── prompts/
    ├── README.md          run order; how to feed P1–P6 output into P7
    ├── P1-link-convention-and-reachability.md
    ├── P2-mandatory-context-budget.md
    ├── P3-generated-artifact-lifecycle.md
    ├── P4-progressive-disclosure-orientation.md
    ├── P5-validation-suite-economics.md
    ├── P6-placement-naming-taxonomy.md
    └── P7-MEGA-cross-cutting-synthesis.md
```

`02-HYPOTHESIS.md` is Part A verbatim — it is the primary source the prompts point at. One row added to
[`docs/ssot/architecture/index.md`](docs/ssot/architecture/index.md) so the bundle is reachable.

## B.3 The six research questions

Each reframed from an option set into something externally researchable, carrying the measurement that
motivates it. **The prompts ask the researcher to test the hypothesis, not adopt it.**

| # | Question | Measurement | Hypothesis under test |
|---|---|---|---|
| **P1** | How should a large agent-read markdown corpus handle cross-references so links survive moves and resolve for every reader? | 4.9% reachable · 352/353 undocumented base · 154/638 broken · READ-FIRST file 0/17 | File-relative everywhere |
| **P2** | How much context should be *mandatory* before an agent acts; what belongs always-loaded vs on-demand? | ~60,800 tokens mandatory · one log is 58.7% of it | Drop the mandate, keep the log |
| **P3** | When do committed derived artifacts earn their churn, and when should they be built on demand? | 231 files · 98,845 lines churn · 66 of 226 empty · documented retrieval path used 0 times in 821 commits | Untrack cache, keep human-facing view |
| **P4** | Does hierarchical progressive disclosure actually work for AI agents, and what makes such a hierarchy rot? | "Stable" file 24 commits vs "narrow" 6 · Macro 61% volatile, duplicates tier-1 semantics | Model sound, files misused |
| **P5** | How should a validation suite be sized against measured catch rate, and how is a warning channel kept credible? | 5/13 gates test gates (80% budget) · 8 catches/821 commits · 95:1 warning noise, grown unnoticed | Retier, freshness advisory, park not delete |
| **P6** | How do mature repos make "where does this go, what is it called" unambiguous for humans and agents? | 1 placement rule · 4 of 5 kinds have none · 11 conventions · duplicate sheet number | Placement + naming table by kind |

**P7 (mega)** consumes all six outputs plus `01-EVIDENCE.md` and `02-HYPOTHESIS.md`, and answers what no
single question can: the minimal coherent change set, its ordering, interaction effects between the six
answers, and **what the combination breaks that no individual answer reveals.** Explicitly authorized to
conclude that some or all of Part A is wrong.

## B.4 My known design flaws — embedded verbatim in every prompt

Each item is evidenced from this session. Each prompt instructs the researcher to check whether the
evidence supports the hypothesis **or whether one of these patterns produced it**.

1. **Guardrail on a broken foundation.** Thirteen gates validate a 95%-unreachable corpus; I extended that
   pattern twice this session rather than fixing navigation.
2. **Overengineering past the target.** The target is orientation. I proposed generated views, registries
   and checks; the operator repeatedly had to restate it.
3. **Quoting prohibitions instead of thinking.** I cited "do not touch / deferred / locked / out of scope"
   as if it were reasoning. The operator had to declare everything open.
4. **Counting `grep` matches as live assertions — four times.** 20 stale routing files (actually 3), 19
   Nowa files (actually 6), 49 B2 duplications (actually 17, and not duplication), "all 19" cards
   (actually 19 of 20). **Every inherited count inflated in the same direction.**
5. **Forgetting my own work.** Reported the ledgers as "zero readers" having personally written the script
   that reads all six. Only an adversarial pass caught it.
6. **Skim presented as read.** Classified a handover as retire-after from a skim; reading it found seven
   live findings and a root-cause diagnosis.
7. **Plausible-inference binding.** Nearly bound edges to `F5-B04` on a keyword match; it was a doc-string
   conformance finding, not an owner.
8. **Recommendation presented as verified truth.** Scores like `(I88/E92/R12: 89)` are self-assessments
   formatted as measurement. **This is the flaw that produced the rejection.**

## B.5 Prompt construction rules

Built to `01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md`. Each of P1–P6 carries:

- **Exact target** at opening and restated as closing success condition — a decision memo on one question,
  not a literature review.
- **Authority model** where measured repository facts outrank my interpretation, and my interpretation is
  the lowest tier, labelled hypothesis.
- **Named sources**: repo paths (readable via the GitHub connector, per `docs/reference-corpus/` precedent)
  **plus key numbers inline**, so each prompt works standalone if connector access fails.
- **Research questions tied to the decision**, not the topic.
- **The §B.4 block**, with instruction to test for those patterns.
- **Deliverables**: evidence-backed findings, options with trade-offs, decision matrix, an explicit verdict
  (confirm / refute / refine) on the hypothesis, and stated confidence with its basis.
- **Boundaries**: don't invent repo meaning; don't treat my analysis as authority; don't propose a new
  system where deletion suffices; separate evidence from inference.
- **Delivery**: one ZIP, concise browser summary.

P7 adds: cross-answer conflict detection, one ordered change set with a stated minimal version, and an
explicit list of what the six answers *together* would break.

The standard's own scorecard (§7 of `04_ANTI_OVERENGINEERING_AND_VALIDATION.md`) is run against each
prompt before delivery; target **21–24**.

## B.6 Verification

- Every number in `01-EVIDENCE.md` carries its command — any claim is re-runnable.
- All four agent reports stored **verbatim**, including the adversarial one refuting my framing and the
  counter-evidence it preserved (`STATE.md:72` — *"the ledger overclaimed"*).
- `00-INDEX.md` links every artifact; `architecture/index.md` links the bundle; all links file-relative and
  verified to resolve.

```bash
python scripts/gates.py --full
```

- Documentation-only: no `scripts/`, `lib/`, or existing-doc changes, so Flutter gates are untouched.
- A `STATE.md` row records the outcome, per the one placement rule that exists.
- Then **push to master**, as requested.

## B.7 What happens after

Operator runs P1–P6 externally in any order, collects the six outputs, then runs P7 with those attached.
P7 returns the change set. **Part A is not executed until that research is in hand.**
