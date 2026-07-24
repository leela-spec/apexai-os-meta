# Plan: Apex KB — realm clarity, semantic-prompt quality, high-impact fixes, and an Apex KB operator agent

## Context (why we are doing this)

The operator's feedback raised four things:

1. **Terminology fear.** A previous **Apex KB Skill** was over-defined and, for a month, caused any driving AI to *drift* and never do what it was told. The operator then built the **Apex KB CLI** (the `apex-kb` executable), which does exactly what's wanted with no drift. They are now considering an **Apex KB agent/subagent** that operates the CLI reliably and also decides *when* to use the CLI vs Mermaid vs a code/knowledge graph. They are (rightly) afraid I will **confuse these three realms**. So the plan must define them with zero ambiguity and keep them separate throughout.

2. **Semantic-file quality doubt.** Looking at the wiki files, the operator feels the output is thin — "not a lot of pointers, not a lot of indexing, not a lot of explanations." They want the audit to specifically examine **the CLI's hardcoded prompts** (the templates the CLI hands to an AI) and judge whether *those prompts* produce valuable, usable output — and they want the "semantic acceptance was disabled" point explained in plain language.

3. **Change explanations.** For every high-impact fix, they want a plain-language explanation of *what changes at the process level* and *what value it creates* — not just a technical label.

4. **Apex KB operator agent.** They want a recommendation on whether an Apex-KB-specialized **subagent** makes sense, how much work it is to move from a *skill* to an *agent*, and a **best-practice orchestration design** (agent → skill → CLI) drawn from the repo's own orchestration KBs (`apex-meta/kb/claude-code-orchestration-design`, `apex-meta/kb/claude-orchestration-agents`).

The intended outcome of *this* plan: a precise, non-drifting definition of the three realms; an honest verdict on the semantic-prompt quality with the exact prompt/schema lines responsible; a value-explained, prioritized fix list; and a concrete design + effort estimate for an Apex KB operator agent, all grounded in the repo's orchestration best practices.

> This planning turn makes **no code/KB/source changes**. The prior audit report is already committed at
> `apex-meta/kb/therapy-narm-personal-development/audit/reports/2026-07-24-apex-kb-value-audit.md`.

---

## Part 1 — The three realms, defined precisely (anti-drift glossary)

This vocabulary is fixed for the whole plan. Every later section tags which realm it touches.

| Realm | What it literally is | Who is "in charge" | Failure mode it has | Analogy |
|---|---|---|---|---|
| **① Apex KB CLI** | The installed `apex-kb` Python executable (`apex-meta/apex-kb-cli/`). Deterministic code. Commands: `start/status/continue/drive/query/doctor/update`. | **The program.** It is the *sole lifecycle authority* — it decides the next legal step, validates, and writes state. It never "reasons." | Bugs / thin validation / non-portable paths. It does **not** drift. | The engine + gearbox. |
| **② Semantic worker (the AI doing one bounded task)** | Whatever AI executes **one** task packet the CLI produced (reads `TASK.md`, writes one Phase-1/Phase-2 JSON file). Today this is just the chat agent. | **The CLI**, via the packet. The worker only fills in the one bounded blank the CLI asked for. | Produces shallow content *if the packet's hardcoded prompt lets it*. This is the semantic-quality question. | A machinist told to cut exactly one part to spec. |
| **③ Apex KB Skill** | `.claude/skills/apex-kb/` — a text instruction file loaded into an agent's context that tells the agent *how to call the CLI*. **Not code, not an AI** — just instructions. | **The agent that reads it.** A skill has no will of its own. | **Drift** — if over-defined/contradictory (and today it documents a dead legacy command surface), the reading agent wanders. This is the month-long failure. | An operating manual taped to the machine. |
| **④ Apex KB Agent / Subagent** | A separate `.claude/agents/*.md` definition with its **own context window, own tool allowlist, own system prompt**, spawned to operate the CLI end-to-end (and decide CLI vs Mermaid vs graph). | **Itself**, within a bounded charter. | Over-reach / drift *if* its charter is vague — same risk the skill had, unless scoped tightly. | A trained operator hired to run the machine and choose the right tool. |

**The one sentence that prevents drift:** *The CLI (①) decides and validates; the worker (②) fills exactly one blank; the skill (③) is just the manual; the agent (④), if built, is a tightly-chartered operator that trusts the CLI as authority and never re-implements its logic.* The month-long failure was ③ trying to *be* ① — the manual tried to run the machine. The fix is never to let ③ or ④ re-decide what ① already decides.

*(Exploration in progress will populate Parts 2–5 below.)*

## Part 2 — Semantic quality: yes, the hardcoded prompts are the main cause (realm ① CLI prompts → ② worker output)

**Your instinct is correct, and here is the mechanism.** The Apex KB CLI (①) hands the AI worker (②) a *hardcoded task prompt* plus a *result schema*. Those two things tell the worker **which sections** to write but never **how much** — no minimum number of pointers, no instruction to cross-link/index, no depth floor. So the worker produced the thin minimum the prompt+schema allowed. This is a design gap in ①, not the worker being "bad."

**Where the thinness comes from (evidence):**
- **Phase 1 prompt** (`templates/phase1-task.md`, ~1 paragraph): "disposition every source, don't fabricate, preserve nuance." No pointer quota, no cross-link instruction, no depth requirement.
- **Phase 2 prompt** (`templates/phase2-task.md`): lists the sections (purpose, macro/meso/micro, answers, ranked sources, routes, claims, boundaries, uncertainty, reopen triggers) but says only "citations must be non-empty" (= *one* is enough). **There is no field in the schema for links to other pages** — so inter-page "indexing" is *structurally impossible* today, not just missing.
- **Schemas floor everything at `minItems: 1`** (or allow empty). Phase 1 `pointers` has **no minimum at all** (a source can be recorded with zero pointers); prose fields need only 1 character.
- **Validation** checks structure + that pointers are valid — never counts, depth, or coverage.

**The proof the richness was there and got dropped** (same topic, `narm-model-and-core-needs`):
- Dossier ranked-source #2 shows **one** pointer (`line:698`). Phase 1's own review for that exact source preserved **nine** pointers (`11, 92, 187, 254, 397, 466, 519, 606, 698`). Eight were simply not carried through.
- Dossier "Key claims" = **3** bullets; Phase 1 capsules held ~**21** claim statements across the sources.

**What "semantic acceptance was toggled off" means, plainly.** Acceptance is a **second, independent AI** (realm ②, a *different* context) that never saw the drafting. It re-reads only the finished wiki pages and checks two things: (a) can every locked question be answered *from the page alone* without reopening raw notes, and (b) is a sample of claims actually supported by the evidence. It is **off by default** (`--semantic-acceptance` flag, labeled "legacy"), and when off the CLI *records a pass anyway* (the overclaim from the first audit). **Important:** even if turned on, acceptance grades *answerability and claim support* — it would **not** force more pointers, cross-links, or deeper explanations. So it's a real but *separate* gap; it is not the cure for the "thin" feeling.

**Conclusion for the operator:** to make the wiki richer you must change the **CLI's hardcoded prompts and schemas** (realm ①) — not the worker, and not (only) the acceptance switch. The three levers are: (1) add quantitative/coverage language to the Phase 1 & Phase 2 prompts ("carry *all* preserved pointers into each ranked source," "enumerate *every* material claim," "write macro/meso/micro to a stated depth"); (2) raise the schema floors and **add a cross-link/related-pages field** so indexing becomes possible and required; (3) separately decide whether to re-enable acceptance for answerability assurance.

## Part 3 — High-impact fixes: what each changes in the *process* and what *value* it creates

Every fix is tagged with its realm so we never conflate them. Effort: S ≈ hours, M ≈ 1–3 days, L ≈ ~1 week. **Group A is the operator's felt pain (thin pages); do it first.**

### Group A — Make the wiki richer (realm ① CLI prompts + schemas). *This is the direct answer to "not enough pointers/indexing/explanations."*

| Fix | What changes in the process | What value it creates | Effort |
|---|---|---|---|
| **A1. Rewrite the Phase 1 & Phase 2 hardcoded prompts to demand coverage** (`templates/phase1-task.md`, `phase2-task.md`, and the injected contracts in `semantic/engine.py`) | Today the prompt says "cite at least one pointer." Change it to *"carry **every** pointer the Phase 1 review preserved for each ranked source; enumerate **every** material claim; write Macro/Meso/Micro to a stated minimum depth."* The worker (②) is now told to be thorough instead of minimal. | The dossier that showed **1** pointer (while 9 existed) would carry all 9. Key-claims goes from 3 bullets toward the ~21 available. Answers become traceable and defensible. | M |
| **A2. Raise the schema floors** (`schemas/phase1-result.schema.json`, `phase2-result.schema.json`) | Change `minItems: 1` / "no minimum" to realistic floors (e.g. ranked sources ≥ material count, pointers ≥1 *per claim*, no empty prose). The CLI now *rejects* thin output and issues a numbered repair. | Thinness becomes structurally impossible, not just discouraged — the machine enforces richness even if a future worker tries to cut corners. | S |
| **A3. Add a cross-link / related-pages field** (new field in `phase2-result.schema.json` + renderer + retrieval) | Today **no field exists** for links between pages, so "indexing" is impossible. Add a `related_pages`/`see_also` field the worker populates and the renderer emits as links. | The wiki becomes an actual interlinked web (concept→concept, concept→atlas), not 10 stand-alone files. This is the "indexing" the operator misses. | M |
| **A4. (Decide) Re-enable a *minimal* acceptance pass** (`--semantic-acceptance` default, or a lighter built-in) | A second, fresh AI (②, separate context) re-reads the finished pages and checks each question is answerable *from the page alone* + spot-checks claims. | Catches shallow/unanswerable pages before `query_ready`. **Note:** this checks *answerability*, not richness — A1–A3 are what make pages rich; A4 is what proves they actually answer. | M |

### Group B — Make the system tell the truth and stay usable (realms ① + ③). *Trust + no-drift.*

| Fix | Process change | Value | Realm | Effort |
|---|---|---|---|---|
| **B1. Reconcile the Apex KB *skill* to the installed CLI** — SKILL.md lists all 7 commands incl. `query`; delete the legacy `apex_kb.py control` references in `package-manifest.md` | The skill stops describing a dead command surface and starts telling any agent the KB is *searchable*. | Removes the #1 cause of the month-long drift: the manual (③) no longer contradicts the machine (①). | ③ | S |
| **B2. Fix the postflight overclaim** — stop asserting `all_semantic_acceptance_pass:true` when acceptance is off; split `import_accepted` vs `semantically_accepted` | The certificate reports what actually happened. | You can trust the state label instead of it silently overclaiming quality. | ① | S |
| **B3. Portable source-drift + surface it in `doctor`/`status`** — store repo-relative paths; compute drift live | `doctor` will say "3 sources changed since build" instead of `fresh:true`. | You (and any agent) learn the wiki is out of date *before* trusting a now-stale pointer. | ① | M |
| **B4. Canonical pointer ledger + resolve-to-real-line check** | One reconciled pointer truth; every dossier pointer must resolve to a real, non-blank source line. | Ends the capsule-vs-review disagreement and the narm-q03 mis-citation where a "correction" pointed at the wrong lines. | ① | M |

### Group C — Retrieval & future-agent value (realm ① + ③). *Do after A/B; C3 gated on a benchmark.*

| Fix | Process change | Value | Effort |
|---|---|---|---|
| **C1. Clean query output + rank an answer chunk #1** (`retrieval/engine.py`) | Stop the `[bracket]`-mangling of paths; down-rank the atlas boilerplate header. | Search results read cleanly and put the actual answer first, not atlas filler. | S |
| **C2. Ship a future-agent query contract** wired into the skill + `wiki/index.md` (retrieval policy, token budget, answer contract) | Any future AI is *told*: "search the KB first, load ≤5 answer chunks, reopen raw only if drift/absent." | The KB becomes the default context source instead of an ignorable folder. | M |
| **C3. Add a local reranker over FTS5 top-K** — *only if a benchmark shows it helps* | Re-score the top lexical hits with a small local model. | Measured retrieval-precision gain (best-practice evidence: rerank is the cheapest, still-local upgrade — not embeddings/graph). | M–L |

**Explicitly deferred/rejected (with reason):** embeddings, typed graph/GraphRAG, cross-session memory, Mermaid-in-wiki — no measured need at 10 sources, and embeddings/graph carry privacy + cost you don't need. Revisit only behind a written, measured use case.

## Part 4 — The Apex KB operator agent: recommendation, effort, and orchestration design

### 4.1 Recommendation — **Yes, build a thin persistent subagent, not a rewritten skill.**
The repo's own orchestration doctrine and the prior audit point the same way:
- The failed skill drifted because it was an **over-scoped skill that tried to own lifecycle decisions in soft prose** — the KB's named **"layer collapse"** and **"guidance is not enforcement"** anti-patterns. The cure is *not* a bigger/better skill; it is to keep the **CLI (①) as sole authority** and add a **tightly-chartered operator (④)** that trusts it.
- The documented, first-class Claude Code pattern is exactly this chain: **main agent → subagent (`skills:` preloads the thin apex-kb skill) → skill → `apex-kb` CLI.** "A subagent can preload specific skills." This is ladder-consistent, not an anti-pattern.
- A recurring, bounded "operate the Apex KB" role is a legitimate **persistent-subagent** candidate (repeated domain role + security-sensitive repo executor). *(Caveat from the KB: the persistent-agent roster doctrine is still a "working hypothesis"; we justify this one on recurrence + bounded scope + CLI-as-authority, and keep it small.)*

### 4.2 Effort — **LOW.** You do **not** "restate the architecture from a skill."
- **Author one new file** `.claude/agents/apex-kb-operator.md` (~20–30 lines), a near-clone of the existing `apex-sync-ops.md` CLI-driver template. House-style frontmatter is just 4 fields: `name`, `description` ("Use when… / Never…"), `tools: Read, Grep, Glob, Bash`, `skills: [apex-kb]` (preloads the existing contract). Body reuses the proven pattern: *"Follow the preloaded apex-kb contract; run only canonical `apex-kb <cmd> --json-output` commands; the CLI is sole authority; dry-run/`--allow-write` gated; preserve CLI output exactly; stop on any mismatch."* Add `Write` (scoped to a packet's declared output path) only if the agent is also to execute semantic packets.
- **Reconcile the thin skill** (fix B1) so the agent preloads a *correct* contract. This is a small edit, **not** a rewrite of the 280 KB / 42-file skill.
- Everything heavy (schemas, templates, contracts) **stays in the skill**; the agent just preloads it. No migration.

### 4.3 The realm-precise orchestration design (this is the anti-drift architecture)
```
Operator (you)
  → Main agent (conversation; decides intent, talks to you)
      → apex-kb-operator  [④ persistent subagent: own context, Bash]
            preloads → apex-kb skill  [③ thin launcher: the manual, corrected]
                  invokes → apex-kb CLI  [① the executable: SOLE AUTHORITY]
                        hands one packet → semantic worker  [② the AI filling one blank]
```
- **① CLI** decides the next step, validates, writes state. Never changes. Never "reasons."
- **② Worker** fills exactly one packet the CLI produced. Its *quality* is governed by Group A (prompts/schemas).
- **③ Skill** = corrected thin manual the agent preloads. Owns *nothing*; describes how to call ①.
- **④ Agent** = the new operator. **Owns:** running the lifecycle to a boundary, reporting progress/blockers in plain language, publishing per the CLI. **Does NOT own:** deciding lifecycle stages (① does), inventing commands, editing manifests/state, or expanding scope. Propose-don't-commit for anything irreversible.

### 4.4 The "which tool when" routing role — do it *bounded and phased* (KB says routing agents over-reach)
The operator wants the agent to also guide *when to use Apex CLI vs Mermaid vs code/knowledge graph*. The KB treats open-ended routing agents cautiously. So:
- **Phase 1 (now):** the operator agent does **one thing reliably** — drive the Apex KB CLI lifecycle end-to-end without drift. This alone fixes the month-long failure.
- **Phase 2 (later, gated):** add routing as a **small explicit decision-matrix reference file** the agent *consults* (e.g. "source-preserving compile/query → Apex KB CLI; architecture/flow visualization → Mermaid; typed relationships/multi-hop → a graph *only if a measured need exists*"). Routing lives as a **documented artifact** (deterministic, reviewable), not open-ended agent judgment — this is how the KB says to keep a decision role from over-reaching. The agent *recommends*, you decide.

## Part 5 — Sequencing & prerequisites
1. **B1 (reconcile skill) first** — an agent that preloads a broken skill inherits the breakage.
2. **Group A (richness)** — the operator's felt pain; makes the *next* KB run visibly better. (Existing pages can be re-compiled with `update`/a fresh run once prompts improve.)
3. **B2–B4 (truth/trust)** — cheap, high-confidence.
4. **④ operator agent (Part 4)** — low effort, once B1 lands.
5. **Group C** — after A/B; C3 only behind a benchmark.

## Verification (how we'll prove each change works)
- **Richness (A):** re-run one topic through the CLI with the new prompts/schemas; assert the dossier now carries *all* Phase-1 pointers per ranked source and ≥N claims; diff old vs new dossier to show more pointers/links.
- **Schema floors (A2):** feed a deliberately thin result; confirm the CLI *rejects* it with a numbered repair (extend `tests/test_semantic_integrity.py`).
- **Cross-links (A3):** confirm rendered pages contain resolvable `[[related page]]` links and that `query` can surface them.
- **Skill reconcile (B1):** grep the skill for `apex_kb.py`/`control` = 0 hits; confirm all 7 commands incl. `query` are listed.
- **Truth (B2/B3):** `doctor` on the current repo reports the real drifted sources (not `fresh:true`); postflight no longer asserts a vacuous acceptance pass.
- **Operator agent (④):** spawn `apex-kb-operator` on a scratch KB; confirm it runs `start→drive→query` via `--json-output`, reports progress/blockers in plain language, and **refuses** to edit state or invent commands (drift test).
- **Regression gate:** the existing 50 CLI tests plus the new richness/rejection tests must pass on every change.

## Operator decisions (captured)
1. **First focus:** Trust + skill fixes first (Group B1/B2/B3) — cheap, high-confidence, unblocks the rest.
2. **Operator-agent scope:** lifecycle-only now; routing (CLI vs Mermaid vs graph) added later as a gated, documented decision-matrix.
3. **Execution/token model (important):** *"The semantic run will be executed by me in a different chat. The deterministic runner should never consume valuable tokens for that. I want all tasks and descriptions ready for me to hand over to an unlimited AI agent."*

## Part 6 — Execution & handoff model (per operator decision 3)

This reshapes *how the plan is delivered and executed*, and it maps cleanly onto the realms:

- **Deterministic work (① CLI) = free of LLM tokens, runs anywhere.** `start / drive / status / query / doctor / update` are pure Python. Running them (including to *emit* semantic packets) costs no model tokens and can be done locally or by a cheap runner. This is also true of authoring the code/prompt/schema/agent edits themselves — mechanical.
- **Semantic work (② worker) = the only token-expensive step, and the operator runs it elsewhere.** Every semantic packet the CLI emits (`TASK.md`, `task.json`, `source-allowlist.json`, `output.schema.json`, `expected-output-path.txt`) is already a self-contained hand-off. The operator will paste these into a separate **unlimited-token AI agent** chat, which drafts the JSON; the CLI then imports/validates it. **Nothing in this plan should draft semantic content in a token-metered chat.**
- **Therefore the deliverable of this plan is a set of discrete, self-contained *hand-over task packets*** — one per fix — each stating: exact files, the precise change, the acceptance test, and whether it is a *deterministic* task (safe for any runner / cheap) or a *semantic* task (must be handed to the unlimited agent). The two are never mixed in one packet.
- **Consequence for Group A (richness) + the therapy-KB re-run:** the *deterministic* half (rewrite prompts in `templates/*.md`, raise `schemas/*.json` floors, add the cross-link field + renderer, run `apex-kb drive` to emit fresh packets) is prepared as cheap tasks. The *semantic* half (actually re-drafting the 5 richer dossiers) is delivered as a ready-to-run **execution pack** (like the existing `phase2-execution-pack/`) that the operator hands to the unlimited agent in the other chat. This directly answers the recompile question: yes, the therapy KB can be enriched, but the token-heavy drafting happens in the operator's separate chat, driven by packets this work produces.
- **This is also exactly what the future Apex KB operator agent (④) is for:** in the operator's unlimited-token chat, that agent drives the CLI, receives each packet, and executes the semantic drafting reliably — the CLI stays the cheap authority; the agent spends tokens only on the bounded semantic blanks.

**Assumption to confirm on approval:** I read "all tasks and descriptions ready to hand over" as *both* the implementation fixes *and* the semantic re-runs being packaged as self-contained hand-off packets (deterministic vs semantic clearly labeled), so you can dispatch each to the right executor. If you actually meant only the semantic KB content runs, the plan still holds — that subset is simply the semantic-labeled packets.

---

## Revision — operator feedback (2026-07-24)

Three surgical changes were applied (the actionable, revised packet list lives in the repo at
`apex-meta/kb/therapy-narm-personal-development/audit/handoffs/2026-07-24-apex-kb-improvement-tasks.md`, which is now the source of truth):

1. **Self-sufficient packets (new packet P1).** The packet the CLI emits and commits to `main` must be 100% complete — every path, allowed source (with exact pointers/excerpts), output schema, output path, *and* best-practice authoring instructions. The external unlimited-token agent **adds nothing** (no paths/files/sources); it only drafts the semantic prose into predefined blanks. An emit-time self-check refuses incomplete packets.
2. **Prompt/template optimization elevated to a KEY, research-backed step (new packet A0 → A1).** Before rewriting the Phase 1/Phase 2 templates, study best-practice KB-authoring prompts from the local llm-wiki projects, OpenKB/deepwiki, and public best practice, and capture exact new wording. A0/A1 + P1 are now the top-priority *core value* work.
3. **Anti-overengineering guardrail.** LLM-grades-LLM self-verification is demoted from a core gate to an optional, bounded check (A4), sequenced last. Deterministic structural gates (schema floors A2, pointer-resolves-to-real-line B4) are kept because they are cheap and objective. Guardrails are not removed — we simply refuse to over-invest in the self-verifying quality tests that failed for a month.

**Revised priority order:** B1 → **A0 → A1 → A2 → A3 → P1** → B2 → B3 → AG1 → O1 → C1 → C2 → B4 → PK1 → S1 → *A4 (optional)* → C3. Implementation steps from the approved plan are preserved, only reprioritized.

**Coverage completeness (2nd feedback pass).** After the operator flagged over-correction, three high-value backlog items that had been left out of the packet list were added so the set is complete: **O1** (operator-visible progress + plain-language blockers — fixes the "is it working or stuck?" confusion), **PK1** (clean-install robustness: pypdf optional + portable forward-slash paths), and **S1** (index the un-indexed 11th source or record its exclusion). Nothing was deleted in the anti-overengineering pass; only A4's priority dropped. The complete high-impact set: value/infrastructure = A0,A1,A3,P1; agent/retrieval value = AG1,C1,C2,C3; trust/usability = B1,B2,B3,O1,PK1,S1; lightweight deterministic guardrails = A2,B4 (+optional A4).
