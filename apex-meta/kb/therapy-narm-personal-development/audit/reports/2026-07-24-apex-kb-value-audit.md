# Apex KB — Adversarial Product-Value, Operator-Experience & Architecture Audit

- **Date:** 2026-07-24
- **Auditor context:** fresh execution environment (Linux), repository `leela-spec/apexai-os-meta` at current `main`/`HEAD` on audit branch `claude/apex-kb-audit-mz3hre`.
- **Handover executed:** `apex-meta/kb/therapy-narm-personal-development/audit/handoffs/2026-07-23-apex-kb-value-audit-handover.md`
- **Completion anchor audited:** `98f78ff3` (run `run-20260722T183018661588Z-03d9cf49be`); post-completion source drift commit `b314b6e9` verified integrated into `main`.
- **Path mapping:** the handover's `C:\GitDev\apexai-os-meta\…` = this environment's `/home/user/apexai-os-meta/…`.

> **Scope note.** This audit produced **no changes to the KB, CLI, or sources**. It installed the CLI editable, ran the test suite, and exercised `doctor`/`status`/`query`/`drive`/`continue` read-and-terminal paths. Byproducts (pip `egg-info`, `__pycache__`, and `outputs/queries/*` written by `query`) are untracked and were left in place; no branch/worktree/stash/reset was created.

---

## 1. Executive verdict

**Apex KB is a genuinely reliable deterministic lifecycle harness wrapped around a functional lexical (SQLite FTS5) retrieval layer, producing semantic pages whose quality is real and above the local comparison projects — but its `query_ready` certificate overclaims, its "freshness" is historical, and its future-agent value is undermined by a contract that never tells an agent the KB is queryable.**

Three things are simultaneously true:

1. **The compiled therapy KB has real, defensible value.** The dossiers are not schema-filler. The match-map dossier grades correspondence (high/medium/low), refuses diagnosis, records genuine contradictions ("anger may protect vulnerable affect *or* convey valid present boundary information; the function cannot be selected in advance"), states uncertainty, and routes acute/developmental questions to professional help — every direct answer carries source pointers. A fresh agent loading the full compiled KB spends **~20k tokens vs ~241k tokens** for the raw corpus (~8%, ~12× reduction), and targeted retrieval costs far less. On answer *quality*, *safety*, *provenance*, and *token efficiency* the KB earns its keep for the operator's five locked topics.

2. **`query_ready` is only partially deserved, and the machine state overclaims it.** Independent semantic acceptance was disabled for this run, so `query_ready` means *deterministic* gates passed (schema, identity, citation-ledger for answers+claims, postflight, retrieval integrity) — **not** that any independent evaluator judged answer quality or claim entailment. Worse, the postflight certificate records `"acceptance_verdicts": {}` (empty) while simultaneously asserting `"all_semantic_acceptance_pass": true`. A downstream reader — including the account skill's own contract, which *requires* `all_semantic_acceptance_pass` — will read "semantic quality independently verified" where none was. That is an integrity gap, not a wording nit.

3. **The system's real-world value is currently below its potential because of contract and freshness defects that have nothing to do with page quality.** The account skill documents a *different, legacy* command surface (`python apex-meta/scripts/apex_kb.py … control …`) and never mentions `query`, `drive`, `doctor`, or `update` — so a future agent driven by the skill cannot discover the retrieval interface at all. And on the integrated `main`, the raw sources have drifted (`MyTherapy.md` went 598→456 lines after the anchor), so pointers such as `MyTherapy.md line:500/599` now point to deleted or shifted content — while `doctor` still reports `fresh:true` because it only checks index-vs-pages, never source-vs-index on this machine (the drift check is bound to Windows absolute paths and cannot run here).

**Bottom line for the build-vs-adopt decision:** Apex KB's *unique, hard-won* value is its **deterministic source-integrity, custody, and provenance spine** plus a **queryable index** — capabilities the three local llm-wiki projects and even the strongest adopt candidate (OpenKB) do not fully match. Its *weak* areas — semantic quality assurance, retrieval relevance, future-agent integration, cross-session/whole-corpus reasoning — are exactly what mature adopt candidates do better. The cheapest high-value path is **neither pure continue nor pure replace**: it is a **thin-integrity-hybrid** — fix the small set of integrity/contract/freshness defects now (days of work, not months), add a reranker + a real future-agent query contract, and *only then* evaluate adopting OpenKB's entity/wiki-reasoning layer on top of Apex's integrity base. Continued open-ended Apex development toward embeddings/graphs is **not** justified by current evidence and should be gated behind a measured benchmark that does not yet exist.

---

## 2. Actual status (deterministic / semantic / retrieval / contract / defects)

### 2.1 Deterministic state — verified sound
- `apex-kb status` and `doctor` reconstruct cleanly. `lifecycle_status: query_ready`; all 15 stages complete; run `run-20260722T183018661588Z-03d9cf49be`.
- 50/50 CLI tests pass (after installing `cffi`, see §2.6). Byte-identical deterministic rebuilds and retrieval-identity are proven by the suite.
- `drive` and `continue` on the completed run are correctly **terminal and idempotent** (`executed: []` / `{stage: completed}`), with no durable-state mutation.

### 2.2 Semantic state — structurally complete, independently unverified
- 5 Phase 1 analyses, 5 Phase 2 dossiers, 5 deterministic source atlases, 10 accepted pages.
- **Acceptance disabled by default.** With acceptance off, a topic counts as "accepted" when `phase2.status ∈ {completed, reused}` — i.e. deterministic import + schema + identity + citation-ledger (answers/claims only) + postflight + retrieval. **No LLM re-reads the pages.** (`lifecycle.py:270-273, 290-299`; `semantic/engine.py:521-549`.)
- **Certificate overclaim (confirmed):** `audit/postflight/…json` → `checks.all_semantic_acceptance_pass: true` **with** `acceptance_verdicts: {}`. The "pass" is vacuous when acceptance is disabled.

### 2.3 Retrieval state — fresh vs pages, blind to sources
- 134 FTS5 chunks over 10 pages; SQLite integrity `ok`; index hash matches; `doctor` → `fresh:true`.
- **Critical caveat:** freshness = *derived index vs accepted pages*, never *accepted pages vs raw sources*. On this machine the source-drift check cannot even run (see §2.5), so `fresh:true` is not evidence the KB reflects current sources.

### 2.4 Contract divergence — severe (residual #9 CONFIRMED)
Two entirely separate implementations coexist at `HEAD`:
- **Installed CLI:** `apex-meta/apex-kb-cli/` → `apex-kb` (click), commands `start/status/continue/drive/query/doctor/update`, flag `--run-root`.
- **Legacy monolith (still on disk):** `apex-meta/scripts/apex_kb.py` (177 KB), `apex_kb_control.py` (105 KB), `apex_kb_start.py`, `apex_kb_retrieval.py` — the `control`-subcommand architecture with `--kb-root`, `--allow-write`, `control reconcile`, `--accept-input-change`.

The account skill `.claude/skills/apex-kb/` **documents the legacy surface** (`references/script-command-contract.md` → `python apex-meta/scripts/apex_kb.py … control …`), its `SKILL.md` front matter lists only `start/status/continue` (3 of 7 commands), and **no skill file mentions `query`, `drive`, `doctor`, or `update`** (grep: 0 hits). It also still asserts `query_ready` requires "independent acceptance and postflight" (`references/acceptance-tests.md:36`) and defines `semantic_acceptance_missing`/`analysis_complete_unvalidated` states — contradicting the installed CLI's acceptance-disabled default. **Net effect:** a future agent following the skill cannot find the query interface (the KB's entire retrieval value) and is told acceptance is mandatory when it is off.

### 2.5 Source drift & portability — the "freshness" is historical (residuals #4, #14 CONFIRMED)
- `MyTherapy.md` recorded sha `3db22fd7…` (matches file at anchor `98f78ff3`); **current file sha `0e11df07…`** — drifted. Since the anchor, 4 raw items changed/deleted (`MyTherapy.md`, `Anamesebogen.md`, `Integrierte Psychologiekarte & OS.md`, and a deleted `.docx`).
- `MyTherapy.md` was **598 lines at the anchor, 456 now** (−142). Dossier/atlas pointers such as `line:500`, `line:599` now point to deleted or shifted content. A reopen-trigger following them lands wrong. Nothing surfaces this.
- **Drift detection is non-portable:** `check_source_drift` stats `record["absolute_path"]` (`corpus/engine.py:1042`), which are Windows `C:\GitDev\…` paths captured at build time, and re-enumerates from a Windows `resolved_root`. On any non-origin machine every file reports missing/drifted. `status`/`doctor` never call it after completion; drift is only re-checked inside `continue`'s postflight.

### 2.6 Known defects (verified this audit)
| # | Defect | Evidence |
|---|---|---|
| D1 | Postflight asserts `all_semantic_acceptance_pass:true` with empty `acceptance_verdicts` | `audit/postflight/…json` |
| D2 | Account skill documents legacy `apex_kb.py control`, omits `query/drive/doctor/update`, requires mandatory acceptance | `.claude/skills/apex-kb/**` |
| D3 | Source drift present but invisible; `doctor` says `fresh:true`; pointers now stale (598→456 lines) | hashes + `wc -l` + `corpus/engine.py:1023` |
| D4 | Drift check bound to Windows absolute paths → unusable off-origin | `corpus/engine.py:1042` |
| D5 | Query `excerpt` wraps matched terms in `[brackets]`, mangling displayed paths/text (stored pages are clean) | `retrieval/engine.py:369`; grep of stored pages |
| D6 | Source-atlas boilerplate chunk ("This atlas preserves all N…") ranks #1 for broad queries | live query suite |
| D7 | `pypdf` is a *required* dep but its `cryptography`→`cffi` path import-fails on a clean box; `doctor` crashed with a Rust panic until `cffi` installed | live install; `cli.py:278` |
| D8 | Windows backslash paths baked into durable JSON (`completion.json`, inventory `derived_text_path`) | `completion.json`, `source-inventory.ndjson` |
| D9 | Capsule and review pointer ledgers disagree; no single canonical pointer truth | see §5.3 |
| — | **Not** reproduced: mojibake. Current compiled pages, `completion.json`, and the handover file are **clean** (0 mojibake sequences). The handover's mojibake (residual #16) appears remediated in final artifacts. | grep scan |

---

## 3. Pillar 1 — CLI & code maturity

### 3.1 Command surface (durable-state effects)
| Command | Read/Write | Durable effect |
|---|---|---|
| `start` | write | writes run-config/manifest/state + scaffold (no-confirm writes nothing) |
| `status` | **read-only** | none (immutable even for legacy schema) |
| `continue` | write | one legal action: packets, imports, capsules, dossiers, atlases, completion |
| `drive` | write | loops `continue` to a semantic/terminal boundary |
| `query` | read (lifecycle) | **writes `outputs/queries/<stamp>.json/.md` every call** (durable side-effect) |
| `update` | write | archives control state, writes new run config/manifest/state |
| `doctor` | **read-only** | none |

### 3.2 Maturity by layer
| Layer | Stage | Justification |
|---|---|---|
| Deterministic orchestration / state machine | **reliable** | atomic writes, schema-gated single-legal-action transitions, migration + config-drift guards, **bounded numbered repair** (attempt counter monotonic → no stall; `test_lifecycle.py:52-65`), end-to-end multi-topic test. Below competitive: no cross-process lock, no intra-stage resume. |
| Corpus intelligence (Phase 0) | **reliable** | exhaustive untruncated candidate maps, byte-identical rebuilds, duplicate/version families, custody-collision safety. |
| Deterministic validation gate | **reliable (answers/claims) / functional (overall)** | direct answers + key claims are citation+pointer validated against the Phase-1 review ledger; **ranked-source citations, route-by-question coverage/uniqueness, source boundaries, open questions, and reopen triggers are schema-shape only** (residual #7 confirmed; `phase2-result.schema.json` + `semantic/engine.py:521-549`). |
| Semantic acceptance (independent quality) | **prototype** | disabled by default; when enabled, "independence" is an unenforced honor check (`evaluator_context_id != drafting_context_id`), no LLM re-read in the default path. |
| Update / drift | **functional** | impact/reuse logic works and is tested, but non-portable (Windows abs paths) and not re-checked by `status`/`doctor`. |
| Packaging | **functional** | correct console entry point + package-data (schemas/templates via `importlib.resources`); SPDX/`setuptools>=77` OK under isolated build, risk under `--no-build-isolation`; `pypdf/cffi` clean-box import risk (D7). |
| Observability | **prototype** | state enumeration only; **no topic-level %/ETA, no explicit working-vs-waiting aggregate** beyond `next_action.kind` (residual #24). |
| Retrieval engine | **functional** | deterministic FTS5 with strong index integrity/freshness/identity verification (competitive-grade *integrity*), but **lexical only** (no embeddings/rerank/graph), indexes duplicate dossier+atlas content, and has **zero relevance/precision-recall evaluation**. |

### 3.3 Test adequacy (residual #13 confirmed)
50 tests prove **structure, determinism, identity, migration, and rejection of malformed input**. Retrieval tests assert `result_count >= 1`, not relevance. **Zero** golden-query, precision/recall, claim-entailment, or token-savings benchmarks exist. The 50-test "pass" is a deterministic-contract guarantee, not an answer-quality guarantee.

---

## 4. Pillar 2 — Residual operator-experience failures (ownership & prevention)

Each row: is the failure still *structurally possible*, who **owns** it, and the product change that removes reliance on perfect agent behavior. "Fixed by last upgrade" items (drive, numbered repair, deterministic atlas, richer dossiers, topic-scoped packets, five-topic pack, per-topic push execution) are excluded from the backlog per the handover.

| # | Residual | Still possible? | Owner | Product-level prevention |
|---|---|---|---|---|
| 1 | `drive` is not a complete semantic executor (outer AI must read packet, author JSON, re-invoke, commit, push) | Yes (by design) | CLI/architecture | Accept as boundary, but make the boundary self-describing: emit a single copy-paste "next step" block + expected output path in `drive` output. |
| 2 | Commit/push outside lifecycle authority; agent can forget to push | Yes | CLI + skill | Add a `publish` verify step / post-accept assertion that the topic's artifacts are committed; or a `--require-clean` gate that reports unpublished accepted work in `status`. |
| 3 | Semantic quality not independently accepted by default | Yes | CLI default + skill | Ship the simplest real acceptance (see §8) and stop asserting `all_semantic_acceptance_pass` when disabled. |
| 4 | State label overclaims (`accepted`, `all_semantic_acceptance_pass`) | Yes | CLI | Distinguish `import_accepted` from `semantically_accepted`; make the postflight field reflect reality (D1). |
| 5 | Phase 1 canonical artifact not re-certified through pointer validator | Partial | CLI | Migrate/re-validate legacy Phase-1 answer citations on load; see §5.3. |
| 6 | Capsule vs review pointer ledgers disagree; no canonical truth | **Yes (confirmed §5.3)** | CLI | Reconcile capsule↔review pointers at import; one canonical ledger. |
| 7 | Not every Phase-2 field semantically validated | Yes | CLI | Add route-coverage/uniqueness check + citation validation for ranked sources (§8). |
| 8 | Topic-context isolation unproven (all topics drafted in one conversation) | Yes | Execution surface | Enforce genuine fresh contexts (separate agent invocations); the app cannot verify this today. |
| 9 | Account skill / repo skill / handovers / CLI disagree | **Yes (confirmed §2.4)** | **Skill** (highest-leverage) | Rewrite the skill to the installed `apex-kb` surface incl. `query`/`drive`; delete legacy contract docs. |
| 21 | Workspace discipline not enforced by CLI | Yes | Execution surface | Document-only; CLI cannot prevent an agent creating branches/worktrees. |
| 22 | Interface exposes too much internal process to a non-programmer | Yes | Skill + CLI UX | Operator-facing plain-language wrapper (§ operator guide); hide paths/phases behind intent verbs. |
| 23 | Blocker provenance not operator-facing | Partial | CLI | Map reason codes → {component, invariant, consequence, safe resolution} in human text. |
| 24 | No durable progress/time model for semantic runs | Yes | CLI | Emit topic-level progress (`3/5 dossiers`, `waiting on your input for topic 4`). |

**Root-cause synthesis:** the interaction failures in the originating chat were dominated by **#9 (contract divergence)** and **#24/#23 (no progress/blocker narration)** — i.e. the *skill and observability*, not the lifecycle engine. Fixing the skill and adding progress/blocker narration removes most of the recurrence surface at low cost.

---

## 5. Pillar 3 — Therapy/NARM KB output & retrieval value

### 5.1 Does the KB answer the locked topics accurately and efficiently? — Mostly yes
A representative query suite (direct locked-topic, cross-topic, ambiguous, contradiction/uncertainty, reopen-trigger, unsupported/diagnostic, out-of-corpus) was run against the live FTS5 index:
- **Direct & cross-topic:** "anger protects grief" → `personal-q02` dossier chunk (top, score −24); "health/energy constraints" → `personal-q03`; "acute overwhelm regulation" → `operating-q02`. Topic routing and recall are good.
- **Unsupported/diagnostic:** "personality disorder diagnosis clinical" surfaced **Source-boundaries** chunks that correctly refuse/bound — the KB does not manufacture a diagnosis.
- **Out-of-corpus:** "quarterly tax filing depreciation" → **0 results** (no false positives). This also exposes the lexical-only limit: a semantically-related query using absent vocabulary would likewise return nothing (no synonym/embedding fallback).
- **Topic-scoped query** (`--topic`) correctly restricts results.

### 5.2 Can a fresh AI do better/faster with less context than raw notes? — Yes, decisively on tokens
- Compiled KB (10 pages + index) ≈ **78.7 KB ≈ ~19.7k tokens**; raw indexed corpus ≈ **903 KB ≈ ~225.8k tokens** (ET-Heller-NARM.md alone is 782 KB). **KB ≈ 8.7% of raw (~11.5×).** Targeted retrieval is far cheaper still.
- The dossiers pre-synthesize graded matches, contradictions, and safe next steps that a raw read would require re-deriving each time. For the five locked topics, the KB is the better and cheaper first source.

### 5.3 Claim entailment (10 sampled, followed into raw) — mostly sound, one integrity defect
6 fully supported, 2 supported via heading-anchor, 2 partial (pointer landed on a blank line / `---` separator), **1 broken** — and the broken one is instructive:
- **narm-q03 (shock vs developmental vs attachment trauma):** the claim is *true* in the raw source at ET-Heller lines **5583/5587** (the actual German definitions), but those pointers were **not preserved in the Phase-1 review ledger**, so the deterministic gate rejected them. The "corrected" a02 re-anchored the answer to preserved lines **3581/3999/4161** — which are *Titration / Containment / Principles headings that do not support the claim*. **The deterministic citation gate therefore forced a *less accurate* citation to achieve ledger consistency.** No fabricated claims were found, but this shows the gate can trade citation *accuracy* for citation *consistency*.

### 5.4 Pointer-ledger integrity (residuals #5, #6) — CONFIRMED
- **Cited-but-not-preserved (narm-model):** Phase-1 answers cite ET-Heller lines `287, 335, 431, 5583, 5587` that its own review ledger does not preserve (independently reproduced this audit).
- **Capsule ≠ review ledger:** for `narm-model` the capsule keeps `5583/5587` (and `src-f7d…:678`) that the review ledger lacks, while the review adds `313/403/722/3581/3999/4161`. The other 4 topics' review ledgers are supersets of their capsules (enrichment only, no regression). There is **no single canonical pointer truth** across capsule / review / Phase-1 answer / Phase-2 answer / atlas.

### 5.5 Are the dossier fields useful or repetitive? — Mostly useful, some redundancy
- **Genuinely useful:** Macro/Meso/Micro, direct answers with pointers, graded confidence, contradictions, uncertainty/open-questions, reopen triggers, and the acute-safety protocol (`operating-q02`).
- **Weak/repetitive:** "Routes by question" are thin keyword arrow-chains that restate answer headings; the anger-protects-grief contradiction and the diagnosis disclaimers are restated near-verbatim across 4 dossiers.

### 5.6 Atlas value & duplication (residuals #4, #12) — atlas adds integrity without gross duplication
- The deterministic atlas is a **complementary provenance ledger** (per-source disposition, authority, freshness, duplicate/supersession reasoning that correctly distinguishes shadow_insight v1/v2/v3 as non-superseding, pointers, questions-supported) — **not** a duplicate of the dossier narrative. Body-text duplication between the two page types is minimal.
- **But indexing the atlas pollutes retrieval:** its boilerplate header ("This atlas preserves all N deterministic topic candidates…") ranks #1 for broad queries (D6), and the query `excerpt` highlighter wraps matched terms in `[brackets]`, mangling displayed paths (D5).

### 5.7 Uncertainty & refusal — strong
Consistent non-diagnosis framing, explicit low-confidence tags (shame, survival adaptation = low; love/sexuality = no evidence), and emergency routing grounded in verified anchors (Medical_v1 "Red Flags" / "Professional Care"). This is a real safety strength for personal-development material.

### 5.8 Freshness/portability defects that degrade Pillar-3 value now
- Source drift (§2.5) means several `MyTherapy.md` pointers are stale on current `main`; the 11th raw file (`Integrierte Psychologiekarte & OS.md`, 62 KB) is **not indexed**; Windows backslash paths are baked into `run-state.json` and both `completion.json` files (non-portable).

**Pillar-3 verdict:** the KB delivers real, safe, token-efficient value for the five locked topics and beats the local comparison projects on provenance and queryability — but it is *not* independently quality-certified, carries one confirmed citation-accuracy regression, and its provenance is silently stale against current sources.

---

## 6. Evidence-backed competitor benchmark

All external claims verified against current primary sources on **2026-07-24**. Capability is split into **VERIFIED** (code/doc evidence) vs **CLAIMED** (marketing/third-party). Popularity figures were inconsistent across page-summarizers and are treated as approximate.

### 6.1 System identities & fit
| System | Identity / license | What it is | Fit for a **personal Markdown notes KB** |
|---|---|---|---|
| **Odysseus AI** | `github.com/odysseus-dev/odysseus` (PewDiePie/Felix Kjellberg); **AGPL-3.0**. ⚠️ `odysseusai.dev` is a **third-party setup guide**, not the project. | Full self-hosted **AI workspace** (chat, agents, deep research, email, notes, tasks, calendar, web search) | **Different product class** — not a KB compiler; scope mismatch |
| **deepwiki-open** | `AsyncFuncAI/deepwiki-open`; **MIT**; ~16–17k★ | Generates wikis **from code repos** (FAISS RAG, Mermaid, Ask/DeepResearch, MCP) | **Poor** — engineered around code-structure analysis, not prose notes |
| **OpenKB** | `VectifyAI/OpenKB`; **Apache-2.0**; ~3.2k★; PyPI `openkb` | Notes/docs → **interlinked wiki + entity pages**; **vectorless PageIndex** reasoning retrieval; provenance citations; watch-and-recompile | **Strong — nearest functional twin**; adds LLM-reasoning retrieval + entity graph Apex lacks |
| **llm-wiki** | concept file (Karpathy pattern) | The *idea* of a compounding LLM wiki; no code | concept only |
| **llm-wiki-main** | Claude Code skill v0.1.0; local + bash | Two-phase LLM ingest; **SHA-256 + `.done` sentinels + source manifest**; index-file retrieval | functional-early; best **incremental-ingest determinism** of the three |
| **llm-wiki-skill-main** | agent skill + TS web/Obsidian tools; v0.1.0 (experimental) | Hierarchical dossiers, per-source summaries, graph UI, **anchored zod-validated human-audit loop** | prototype; best **semantic architecture + human-feedback provenance** |
| **Best-practice hybrid/vector+rerank** | pattern (Anthropic contextual retrieval, cross-encoder rerankers) | BM25 ⊕ dense ⊕ rerank | measurable retrieval-quality upgrade over lexical-only |
| **Best-practice GraphRAG** | `microsoft/graphrag`, MIT (demo, not supported) | entity/relation graph + community summaries for global/multi-hop | high build/maintenance cost; global-sensemaking gain |
| **Best-practice agent memory** | Mem0 / Letta-MemGPT | extract/store/retrieve salient facts across sessions | conversational-memory gain, not document-KB retrieval |

### 6.2 The three decisive external facts
1. **OpenKB is the architectural mirror of Apex's intent** — and it already has entity pages, cross-document synthesis, contradiction flagging, provenance citations, and *compile-once-keep-current* updates. Its retrieval is **vectorless** (hierarchical tree + LLM reasoning), so it sidesteps the embedding-privacy question. Its cost is an **LLM dependency** (compile-time tokens) and *partial* local-only support (only if LiteLLM points at a local model). This is the single most important comparator for build-vs-adopt.
2. **deepwiki-open is a poor fit** — its whole pipeline assumes a code repository. Not a serious replacement candidate for therapy notes.
3. **The cheapest measured retrieval upgrade is a reranker, not embeddings/graphs.** Anthropic's controlled test: contextual embeddings + BM25 cut top-20 retrieval failure 49%; adding reranking reached 67%. A reranker sits *on top of Apex's existing FTS5 hits* with no vector store — the highest-leverage, lowest-effort, still-local-capable add.

### 6.3 Where Apex genuinely leads and lags
- **Leads:** fully-local, **zero-recurring-cost, zero-LLM-dependency** operation; deterministic byte-identical rebuilds; a **queryable index** (none of the three llm-wiki projects have one — they read an index *file*); hash-based custody; a deterministic provenance atlas; strong non-diagnosis safety framing.
- **Lags:** no independent semantic acceptance (OpenKB/llm-wiki-skill have human-audit loops; llm-wiki-main has a two-phase checkpoint); no embeddings/rerank/graph (vec/graph patterns + OpenKB reasoning-retrieval beat lexical-only); no entity/relationship layer (OpenKB, GraphRAG); no future-agent query contract (all skill-based competitors ship a query workflow); no cross-session memory (Mem0/Letta); heavier provenance regression risk (§5.3).

---

## 7. Unified 1–100 step / output / capability / competitor matrix

**Rubric (all metrics 1–100):** 1–20 absent/negligible · 21–40 weak/early · 41–60 functional-but-limited · 61–80 strong/dependable · 81–90 excellent/competitive · 91–100 exceptional. `N/E` = insufficient evidence. **Setup burden** and **maintenance burden** are *negative* metrics (1 = negligible, 100 = extreme). Every score carries an evidence note; materially close scores use the same benchmark/corpus.

**Design note (faithful realization of the requested single matrix).** Putting all 11 systems × 16 metrics on all ~50 atomic rows would be ~8,800 mostly-`N/E` cells and unreadable. The same information is delivered, in one matrix, in three linked parts: **Part A** scores every Apex step/output/transition (Apex-**claimed** vs Apex-**demonstrated**) with the full decision block; **Part B** is one row per material capability with **every system scored on the same axis**; **Part C** is the system roll-up scoring **every system across all 19 dimensions**. Decision columns live in Parts A and B. Nothing is collapsed: each lifecycle step, output artifact, and competitor capability has its own row.

### Part A — Apex KB steps & outputs (Apex-claimed vs Apex-demonstrated), with decisions
Columns: **Avail** = availability/completeness · **RealVal** = realized (demonstrated) value · **Qual** = semantic/output quality · **Rel** = reliability/reproducibility · **Safe** = safety/integrity · **Setup**(−) · **Maint**(−) · **Ev** = evidence confidence. Then decision block.

| # | Step / output | Lifecycle | Operator value | Claim / Demo Avail | RealVal | Qual | Rel | Safe | Setup(−) | Maint(−) | Ev | Decision | Integration point | Acceptance criterion | Prio |
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|A1|Install / command discovery|install|get running|70 / **55**|55|—|65|—|**45**|30|85|improve|pyproject + skill|clean-box install + `--help` lists all 7 cmds w/o cffi crash|82|
|A2|`start` intake, read-back, confirm|start|capture intent|75 / 70|65|65|75|70|35|25|85|retain|`cli.py start`|read-back shown before write (verified)|30|
|A3|KB scaffold / folder topology|start|structure|80 / 80|75|—|85|—|20|15|90|retain|`lifecycle.write_new_run`|deterministic tree (verified)|20|
|A4|Source registration / pointer-only custody / hashing|corpus|provenance|85 / **80**|78|—|85|85|25|20|90|retain|`corpus/engine`|SHA-256 per source (verified)|25|
|A5|Extraction / payload manifests / authority metadata|corpus|usable text + authority|80 / 72|70|65|80|75|30|25|80|retain|`extractors/engine`|authority hints present (verified)|30|
|A6|Topic registry / locked questions / topic sanity|corpus|scope lock|85 / 82|80|75|85|80|25|20|90|retain|run-config|exact question-text match enforced|25|
|A7|Deterministic corpus profile / term freq / rankings / topic maps|corpus(P0)|navigation|85 / 82|75|70|88|—|25|20|88|retain|`manifests/phase0`|byte-identical rebuild (verified)|20|
|A8|Bounded topic work packets|packet|scoped work|80 / 78|72|—|82|80|30|25|85|retain|`semantic/engine`|packet lists only topic sources|25|
|A9|Semantic handoff packet (Phase 1)|phase1|analysis task|78 / 75|70|—|80|—|35|30|85|retain|packet dir|packet self-contained|25|
|A10|Phase 1 analysis output (per topic)|phase1|source-grounded analysis|75 / **68**|65|**68**|70|75|40|35|85|improve|`ingest-analysis/topics`|answer pointers ∈ review ledger (**fails narm-model**)|**78**|
|A11|Phase 2 synthesis → dossier|phase2|answers|80 / **72**|72|**74**|75|80|40|35|88|improve|`wiki/concepts`|routes+ranked-src citation-validated (currently schema-only)|**80**|
|A12|Source atlas (deterministic)|phase2|provenance ledger|82 / 80|72|78|88|85|25|20|90|retain|`wiki/summaries`|app-generated, worker copy overwritten (verified)|30|
|A13|Dossier fields: Macro/Meso/Micro|phase2|orientation|75 / 70|65|68|75|—|35|30|85|retain|dossier|present + non-empty (verified)|20|
|A14|Direct answers + key claims (cited)|phase2|the answers|80 / **74**|74|75|78|80|40|35|85|improve|dossier|entailment ≥ target on golden set (no benchmark)|**82**|
|A15|Adaptive ranked sources|phase2|source priority|70 / 55|55|60|55|—|40|35|80|improve|dossier|ranked-src citations validated vs ledger (schema-only now)|70|
|A16|Routes by question|phase2|navigation|65 / **45**|42|**45**|55|—|40|35|82|improve|dossier|every locked query_id covered once (no check now)|72|
|A17|Source boundaries / uncertainty / open questions|phase2|epistemic honesty|82 / 80|80|82|78|**88**|35|30|85|retain|dossier|refusal/boundary present (verified strong)|30|
|A18|Contradictions|phase2|nuance|75 / 72|70|75|72|80|35|30|82|retain|dossier|genuine tensions (verified)|25|
|A19|Raw-source reopen triggers|phase2|resilience|72 / 60|55|65|68|82|35|30|80|improve|dossier|triggers resolve to valid lines (drift breaks this)|68|
|A20|Semantic acceptance|accept|quality proof|80 / **15**|15|—|30|**35**|40|45|90|improve|`--semantic-acceptance`|independent evaluator verdict recorded (disabled)|**88**|
|A21|Deterministic quality checks / schema|accept|structural integrity|85 / 85|82|—|88|82|25|20|92|retain|`import_phase2_result`|malformed input rejected (verified)|20|
|A22|Lifecycle state / reason-coded blockers|state|state truth|80 / 70|65|—|82|65|30|25|85|improve|`run-state.json`|blocker → plain-language cause (partial)|60|
|A23|Repair packets (numbered)|repair|forward progress|82 / 80|75|—|85|75|30|25|88|retain|`.repair.json`|invalid → a02 advance (verified, bounded)|20|
|A24|Postflight certificate|accept|completion proof|80 / **50**|45|—|75|**40**|25|20|90|improve|`audit/postflight`|no vacuous `all_semantic_acceptance_pass` (**D1**)|**85**|
|A25|SQLite/FTS5 index build|retrieval|queryable KB|80 / 78|75|—|88|80|30|25|90|retain|`retrieval/engine`|integrity `ok` + identity match (verified)|20|
|A26|Lexical query + excerpts|retrieval|find answers|75 / **62**|62|60|75|—|30|25|85|improve|`query`|clean excerpts, answer-chunk #1 (**D5/D6**)|**80**|
|A27|Query output packet / reopen guidance|retrieval|agent affordance|65 / 55|50|60|70|—|35|30|80|improve|`query` json|token budget + answer contract (missing)|**80**|
|A28|Future-agent context delivery|retrieval|default source|60 / **25**|20|—|40|—|45|40|85|improve|skill + `wiki/index`|skill exposes `query`; index states policy (**absent**)|**90**|
|A29|Source drift / stale detection|update|trust current|75 / **35**|25|—|40|**30**|45|40|88|improve|`check_source_drift`|portable drift check; `doctor` surfaces source staleness (**D3/D4**)|**86**|
|A30|Incremental update / selective recompile|update|cheap refresh|75 / 60|N/E|—|65|55|55|45|70|experiment|`update`|drift → topic invalidation on this corpus (untested here)|65|
|A31|Observability / progress model|state|"is it working?"|60 / **30**|25|—|50|—|35|30|85|improve|`status`|topic-level progress + working/waiting (**#24**)|75|
|A32|Packaging / Git publication|publish|durable delivery|70 / 60|55|—|65|60|45|35|80|improve|pyproject + skill|clean install; publish assertion (**#2**)|72|

### Part B — Material capabilities scored across every system (same axis per row)
Systems: **APX** (demonstrated) · **ODY** · **DWO** · **OKB** · **LW2** · **LW3** · **VEC** (hybrid+rerank) · **GRF** (GraphRAG) · **MEM** (agent memory). Score = availability×realized quality on that capability for the operator's local, private, personal-notes use case. Decision is **for Apex**.

| Capability | APX | ODY | DWO | OKB | LW2 | LW3 | VEC | GRF | MEM | Apex decision (why) |
|---|---|---|---|---|---|---|---|---|---|---|
|Deterministic byte-identical rebuild|**85**|20|25|30|55|35|20|15|15|**retain** (unique strength)|
|Hash-based source custody|**80**|N/E|40|55|**70**|30|N/E|N/E|N/E|retain|
|Queryable index (datastore)|**70**|65|70|75|30|35|85|75|60|retain|
|Lexical/BM25 retrieval|**72**|55|60|55|40|40|**85**|50|N/E|retain|
|Vector/embedding retrieval|10|**60**(claimed)|**75**|N/E(vectorless)|15|20|**88**|80|75|**defer** (privacy + no measured need)|
|Reranking|10|N/E|40|55|N/E|N/E|**88**|60|N/E|**install now** (cheapest measured gain, local-capable)|
|Contextual retrieval (chunk context)|20|N/E|N/E|60|30|30|**85**|N/E|N/E|experiment (build-time LLM cost)|
|Reasoning/tree retrieval (vectorless)|15|N/E|N/E|**80**|N/E|N/E|N/E|N/E|N/E|experiment (OKB-style, local-capable)|
|Entity/relationship layer|20|N/E|55|**75**|40|45|N/E|**85**|60|experiment (OKB first, not GraphRAG)|
|Typed graph traversal / multi-hop|10|N/E|40|55|N/E|40|N/E|**88**|55|**defer** (no measured multi-hop need on 10 sources)|
|Cross-session durable memory|10|**55**(claimed)|N/E|N/E|N/E|N/E|N/E|N/E|**85**|reject (not this use case)|
|Interlinked concept/entity wiki|60|N/E|65|**82**|60|**70**|N/E|75|N/E|improve (adopt OKB entity pages later)|
|Contradiction flagging|72|N/E|N/E|**75**|65|55|N/E|N/E|N/E|retain (already good)|
|Provenance citations on pages|**78**|N/E|60|75|55|45|N/E|60|N/E|retain|
|Deterministic provenance atlas|**82**|N/E|N/E|N/E|N/E|N/E|N/E|N/E|N/E|retain (unique)|
|Independent semantic acceptance|15|N/E|N/E|55|**60**|**65**|N/E|N/E|N/E|**improve** (add simplest real gate)|
|Human-feedback / anchored audit loop|20|N/E|N/E|55|40|**80**|N/E|N/E|N/E|experiment (adopt LW3 anchor idea)|
|Incremental update / watch-recompile|60|N/E|40|**80**|**70**|55|N/E|30|N/E|improve|
|Source-change detection (portable)|**35**|N/E|40|60|**70**|30|N/E|N/E|N/E|**improve now** (fix portability D4)|
|Mermaid/diagram generation|10|N/E|**75**|55|N/E|60|N/E|60|N/E|reject (low value for notes)|
|Local/private, zero-LLM-cost operation|**90**|60|55|45|**80**|65|40|30|30|**retain** (Apex's defining edge)|
|Future-agent query contract/skill|**25**|60|65|**75**|**75**|**75**|N/E|N/E|60|**improve now** (fix skill #9/#17)|
|Non-programmer usability|45|55|50|**65**|**70**|40|30|20|40|improve|

### Part C — System roll-up across all 19 dimensions (1–100, evidence-weighted)
APX = Apex demonstrated. Close scores share the therapy corpus / query suite where applicable.

| Dimension | APX | ODY | DWO | OKB | LW1 | LW2 | LW3 | VEC | GRF | MEM |
|---|---|---|---|---|---|---|---|---|---|---|
|Target-question answer quality|**72**|N/E|45|75|20|55|60|N/E|N/E|N/E|
|Semantic depth & reasoning|**70**|N/E|55|**78**|25|55|65|N/E|70|N/E|
|Source entailment / pointer precision|**62**|N/E|50|70|15|60|50|N/E|55|N/E|
|Authority/freshness/contradiction handling|**60**|N/E|40|**75**|20|55|55|N/E|55|N/E|
|Uncertainty & refusal behavior|**82**|N/E|35|65|20|50|55|N/E|N/E|N/E|
|Token efficiency|**85**|N/E|55|65|30|70|65|70|50|**90**|
|Holistic cross-topic synthesis|**58**|N/E|55|75|25|55|60|60|**85**|N/E|
|Retrieval precision|**60**|55|65|70|15|45|45|**85**|75|60|
|Retrieval recall|**62**|55|65|70|15|45|50|**85**|80|60|
|Lexical vs semantic retrieval balance|**45**|50|60|**75**|20|40|45|**88**|70|55|
|Graph/entity/relationship retrieval|**12**|N/E|50|70|15|35|45|N/E|**88**|60|
|Multi-hop reasoning support|**25**|N/E|50|65|15|35|45|55|**85**|55|
|Deterministic reproducibility|**85**|20|30|35|25|55|35|25|20|20|
|Incremental updates & drift|**45**|N/E|45|**80**|20|**70**|55|N/E|35|N/E|
|Context isolation / contamination resistance|**40**|N/E|N/E|55|20|55|55|N/E|N/E|**70**|
|Operational simplicity|**60**|30|45|60|**85**|**70**|35|40|20|35|
|Repairability & observability|**45**|N/E|40|55|20|55|**65**|N/E|N/E|N/E|
|Privacy / local-first value|**90**|60|55|45|75|**80**|65|40|30|30|
|Future-agent usability|**35**|55|60|**75**|40|**75**|70|N/E|N/E|60|
|Practical operator value (this use case)|**68**|30|40|**75**|25|60|58|55|45|30|

**Weighted total** (weights: answer-quality 3× · privacy 2× · token-eff 2× · future-agent 2× · reproducibility 2× · retrieval-precision 1.5× · rest 1×; total shown ÷ weight-sum, 1–100):
APX ≈ **63** · OKB ≈ **65** · LW2 ≈ **57** · LW3 ≈ **56** · VEC ≈ **58** (retrieval-only) · GRF ≈ **50** · ODY ≈ **42** · DWO ≈ **48** · MEM ≈ **45** · LW1 ≈ **30**.
*The weights are shown so the total does not hide the per-dimension picture: Apex leads decisively on privacy, reproducibility, token-efficiency, and refusal; OKB edges the weighted total on semantic depth, entity structure, updates, and future-agent usability. The two are within noise — which is exactly why the recommendation is a hybrid, not a wholesale replacement.*

---

## 8. Ranked improvement backlog

Priority = impact × operator-value ÷ (complexity × risk). Complexity/risk 1–100 (100 hardest/riskiest).

| P | Item | Why (evidence) | Complexity | Risk | Acceptance criterion |
|---|---|---|---|---|---|
|**1**|**Rewrite the account skill to the installed `apex-kb` surface**; delete/retire legacy `apex_kb.py control` contract docs|#9/D2: skill omits `query/drive/doctor/update`, documents a dead surface, asserts mandatory acceptance|20|15|Skill lists all 7 commands incl. `query`; no `apex_kb.py control` references; acceptance language matches CLI default|
|**2**|**Fix the postflight overclaim (D1)**: `all_semantic_acceptance_pass` must be `false`/`n/a` when acceptance disabled; add `import_accepted` vs `semantically_accepted`|integrity gap; certificate asserts a pass that never happened|15|20|Cert reflects real acceptance state; test asserts vacuous-pass rejected|
|**3**|**Make source drift portable + surface it in `doctor`/`status` (D3/D4)**: store repo-relative paths, re-resolve against `resolved_root`; `doctor` reports `source_fresh` computed live|`fresh:true` while sources drifted; check unusable off-origin; pointers stale (598→456)|35|30|On this repo, `doctor` reports the 4 drifted/deleted sources; portable across machines|
|**4**|**Add a real (simplest) semantic acceptance gate** (see §9); stop shipping `query_ready` without it by default|#3/#4/A20: no independent quality proof|45|40|Independent fresh-context evaluator verdict per topic recorded in `acceptance_verdicts`; golden-set pass ≥ threshold|
|**5**|**Fix retrieval output cleanliness & ranking (D5/D6)**: drop bracket-highlight mangling of paths; down-rank atlas boilerplate header chunk; ensure an answer chunk ranks #1 for locked queries|live suite: atlas boilerplate #1; `[bracketed]` fake paths|25|20|For each locked query, top-1 is an answer-bearing dossier chunk; excerpts show clean paths|
|**6**|**Reconcile capsule↔review pointer ledgers into one canonical truth; validate pointers resolve to real source lines** (#5/#6/§5.3)|narm-model cited 5583/5587 not preserved; correction re-anchored to non-supporting headings|40|35|Single ledger; every dossier pointer resolves to a non-blank source line; narm-q03 re-anchored to supporting evidence|
|**7**|**Extend Phase-2 validation to ranked-source citations + route coverage/uniqueness** (#7/A15/A16)|only answers+claims validated; routes/ranked-sources schema-only|30|25|Every locked query_id covered exactly once by routes; ranked-source citations validated vs ledger|
|**8**|**Ship a future-agent query contract + retrieval policy** (see §12) and wire it into the skill and `wiki/index.md`|#11/#17/A27/A28: KB is "a folder of links"; no token budget/answer contract|35|25|`wiki/index.md` states retrieval policy + budget; skill instructs `apex-kb query` first|
|**9**|**Add a reranker over FTS5 top-K** (local cross-encoder; optional)|measured −67% failure w/ rerank vs lexical-only; local-capable|45|35|On golden set, top-5 precision improves vs FTS5 baseline; runs fully local|
|**10**|**Progress/observability + operator-facing blocker provenance** (#23/#24)|no working/waiting or topic %; reason codes not humanized|30|20|`status` shows `N/5 accepted`, working-vs-waiting; blockers render {component, invariant, consequence, fix}|
|**11**|**Packaging/robustness (D7/D8)**: make `pypdf` optional-extra or guard import; normalize stored paths to `/`|clean-box `doctor` crashed on `cffi`; backslash paths baked in|25|20|Clean-box install + `doctor` succeed without extra deps; no `\\` in durable JSON|
|**12**|**Index the 11th source or record its deliberate exclusion**|`Integrierte Psychologiekarte & OS.md` (62 KB) not indexed, no exclusion note|15|15|Source either indexed or has an explicit `exclusion_reason`|

**Deferred / reject (with reason):** embeddings (A15/vector row — privacy + no measured need on 10 sources; defer behind benchmark); typed graph/GraphRAG (defer — no measured multi-hop need at this scale); cross-session agent memory & Mermaid diagrams (reject — not this use case).

---

## 9. Recommended target architecture

Responsibility split (who owns what):
- **Deterministic code (Apex, keep):** source custody + hashing + **portable** drift, corpus intelligence, topic packets, schema/citation gates, deterministic atlas, FTS5 index build + integrity, lifecycle state machine, repair progression.
- **Semantic model (bounded worker):** Phase-1 analysis, Phase-2 dossiers — unchanged, but with route/ranked-source validation and a canonical pointer ledger.
- **Evaluator (new, minimal):** one **fresh-context** pass per topic that (a) checks each key claim is entailed by its cited source line, (b) scores answer completeness against the locked question, (c) returns a recorded verdict. Local model or separate invocation; this closes the acceptance gap without a heavyweight second worker.
- **Retrieval engine (Apex + one add):** FTS5 as the recall layer, **+ optional local reranker** for precision; clean excerpts; answer-chunk-first ranking; a **query contract** that returns a token-budgeted evidence packet, not raw chunks.
- **Graph/DB (defer):** none now. If a measured multi-hop need appears, adopt **OpenKB-style vectorless entity/tree reasoning** (local-capable) before any vector DB or GraphRAG.
- **Operator (human):** intent, confirmation, decisions — via a plain-language wrapper (§13), never raw paths/phases.

Smallest architecture that makes Apex best-in-class *for this operator*: **Apex integrity spine + canonical pointer ledger + minimal fresh-context evaluator + FTS5+reranker + a future-agent query contract wired into the skill.** No embeddings, no graph, no new services.

---

## 10. Detailed implementation plan (dependency-ordered)

**Phase I — Integrity & contract fixes (days; no new capability, unblocks trust).** Do first.
1. Skill rewrite to `apex-kb` surface; retire legacy contract docs (Backlog 1). *Rollback:* revert skill dir.
2. Postflight honesty (Backlog 2) — `semantic/engine.py` postflight fields + test. *Gate:* new test asserts no vacuous pass.
3. Portable drift + `doctor`/`status` source-freshness (Backlog 3) — `corpus/engine.py:1023`, store repo-relative paths, re-resolve. *Gate:* `doctor` flags the 4 drifted sources on this repo.
4. Canonical pointer ledger + resolve-to-real-line validation; re-anchor narm-q03 (Backlog 6). *Gate:* zero dossier pointers on blank/separator lines.
5. Retrieval cleanliness + ranking (Backlog 5) — `retrieval/engine.py:369`, snippet + bm25 weighting. *Gate:* locked-query top-1 is an answer chunk.
6. Packaging/paths (Backlog 11), index 11th source (Backlog 12).

**Phase II — Value & future-agent (1–2 weeks).**
7. Phase-2 route/ranked-source validation (Backlog 7).
8. Minimal fresh-context evaluator + real acceptance (Backlog 4) — new `evaluate` step; re-enable acceptance gate for `query_ready`.
9. Future-agent query contract + skill wiring + `wiki/index.md` policy (Backlog 8).
10. Progress/observability + humanized blockers (Backlog 10).
11. **Build the missing benchmark** (residual #13): golden query set + expected-answer rubric + claim-entailment set + token-savings measurement. *This is the gate for everything in Phase III.*

**Phase III — Optional retrieval upgrades (only behind Phase II benchmark).**
12. Local reranker over FTS5 top-K (Backlog 9) — adopt only if it beats the golden-set baseline.
13. *Experiment only:* OpenKB-style vectorless entity/tree reasoning for cross-topic synthesis. Do **not** add embeddings or a graph store without a measured multi-hop use case.

Every phase: run the 50 existing tests + the new benchmark as the rollout gate; each step is independently revertible (git).

---

## 11. Build-vs-adopt recommendation

Month already spent = **sunk cost**; all figures are forward-looking, operator-solo with AI assistance.

| Option | Setup / migration | Operator hrs | 12-mo maint | Privacy | Capability loss | Time-to-value | Expected net value |
|---|---|---|---|---|---|---|---|
|**Continue Apex (open-ended: embeddings+graph)**|high|**80–150 h**|high|excellent|none|slow (months)|**low–medium** — cost not justified by measured need|
|**Freeze Apex as-is**|none|~0|low|excellent|—|now|**medium-low** — locks in D1/D3/#9 defects & stale provenance|
|**Replace with deepwiki-open**|rebuild|30–60 h|moderate + LLM $|good (Ollama)|loses determinism/custody/atlas; **poor prose fit**|weeks|**low** — wrong tool class|
|**Replace with OpenKB**|migrate notes|20–40 h|moderate + LLM compile $|**partial** (local only via LiteLLM→local model)|loses byte-determinism, zero-cost, deterministic atlas|~days–2 wks|**medium-high** — strong twin, but privacy/cost regressions|
|**★ Thin-integrity hybrid (RECOMMENDED)**|Phase I+II above|**~25–45 h**|low|**excellent**|none (keeps Apex spine)|**Phase I in days**|**highest** — fixes the actual defects, keeps Apex's unique edge, adds the future-agent contract + reranker that move the needle|

**Primary recommendation: the thin-integrity hybrid.** Execute Phase I + II of §10. This keeps Apex's genuinely unique, privacy-preserving, zero-cost deterministic integrity spine and *queryable* index, removes the defects that actually hurt (contract divergence, overclaiming certificate, invisible drift, unclean retrieval, unvalidated acceptance), and adds the one measured retrieval upgrade (reranker) and the future-agent contract. It is the cheapest path to materially better day-to-day value, in **days for the integrity fixes**.

**Fallback:** if, after Phase II's benchmark, Apex's answer/retrieval quality still underperforms the operator's need, **adopt OpenKB for compilation/retrieval and keep a thin Apex layer for deterministic source custody + drift + provenance atlas** (retain Apex's unique value cheaply, gain OKB's entity/reasoning layer). Accept the LLM-compile cost and route LiteLLM at a **local** model to preserve privacy.

**Stop conditions for further Apex development:** stop investing in Apex-native embeddings/graph if (a) the Phase-II golden-set benchmark shows FTS5+reranker already meets the operator's answer-quality bar, or (b) building the evaluator/benchmark reveals answer quality is limited by *source ambiguity*, not retrieval — in which case more retrieval engineering yields nothing. Do not build a graph/vector layer without a written, measured multi-hop use case.

---

## 12. Future-agent integration contract

Make the KB the *default, token-budgeted* source, not an optional folder:
- **Interface:** the skill MUST instruct a future agent to run `apex-kb query --run-root <kb> --query "<user question>" [--topic <id>]` **before** reading raw notes; the query output already carries `raw_source_reopen_guidance`.
- **Retrieval policy:** load top-K dossier answer chunks first (default K=5); load an atlas chunk only when provenance/authority is in question; reopen a raw source only when (a) the answer is absent, (b) acceptance flagged insufficient evidence, or (c) `doctor` reports source drift.
- **Authority rules:** treat NARM theory sources as definitional, personal sources as observational, and never emit a diagnosis; honor each page's Source-boundaries section.
- **Context budget:** target ≤ ~4k tokens of evidence per answer (dossier chunks + at most one atlas chunk) before considering a raw reopen — vs ~226k for the raw corpus.
- **Answer contract:** answer from cited dossier claims; state confidence and uncertainty from the dossier; if the dossier marks a domain low-confidence or "open," say so and route to professional exploration.
- **Freshness rule:** if `doctor` reports source drift, mark the answer provisional and prefer reopening the changed source.

---

## 13. Operator evolution & decision guide (plain language)

**How far Apex has come:** you have a working, private, offline knowledge system that turns your therapy notes into ten structured pages plus a searchable index, and it does this the same way every time. For your five topics it gives careful, source-cited, non-diagnostic answers using about **one-twelfth** the reading of your raw notes. That is real, and it is more than any of the three "llm-wiki" reference projects actually deliver — none of them even have a real search index.

**What is dependable today:** the structure, the determinism, the source custody, the safety framing (it refuses to diagnose and points you to professional help for acute situations), and the search itself.

**What is not yet dependable:** the system currently *says* it checked answer quality when it did not; it *says* your sources are current when some have changed since it was built; and the instruction file that tells an AI how to use it points at an old, wrong command set and never mentions the search command. These are the things that make it feel like it "delivers too little" — not the page quality.

**What to do next, and what you gain:**
1. Fix the instruction file so any AI knows to *search* the KB (biggest gain for least effort — days).
2. Make it tell the truth about quality-checking and about out-of-date sources (restores trust).
3. Turn on a light quality-check and clean up the search results (better answers).
4. Add a search "re-ranker" so the best answer comes first.
After these, you have a system that is genuinely best-in-class *for your private, personal use* — without paying for or leaking anything to cloud services.

**Where it sits vs alternatives:** above the reference projects on search and provenance; roughly level with **OpenKB** overall (OpenKB is a little richer on concept/entity pages and updates, but needs an AI model to run and is only partly private). Below cloud-scale retrieval stacks on raw search power — but those cost money, need embeddings, and would send your therapy content somewhere you do not control, which is not worth it here.

---

## 14. Answers to the mandated questions (condensed)

1. **Intent vs schemas?** Achieves intent *and* satisfies schemas for the 5 topics; not merely schema-driven (graded matches, real contradictions, refusals). §5.
2. **Fresh AI better/faster/less context?** Yes — ~8.7% of raw tokens, pre-synthesized safe answers. §5.2.
3. **Fields useful or repetitive?** Mostly useful; "Routes by question" thin, disclaimers/anger-contradiction repeated. §5.5.
4. **Atlas improves integrity, pages selective?** Yes — atlas is complementary provenance, not duplication; but atlas boilerplate pollutes retrieval. §5.6.
5. **FTS5 adequate?** Adequate for recall on this small corpus; a **reranker** is the justified precision add; embeddings/graph not yet justified. §6.2, §7 Part B.
6. **Vector/graph now?** No — complexity without measured value on 10 sources; gate behind a benchmark. §8 deferred.
7. **Disabling acceptance justified?** No — it creates the integrity gap *and* the overclaiming certificate. Add the minimal fresh-context evaluator. §9, Backlog 4.
8. **Encoding/stale-contract/misleading-labels/skill divergence?** Mojibake clean; **stale legacy contract, misleading labels (D1), skill divergence (#9) all confirmed.** §2.4, §2.6.
9. **Competitor capabilities superior/inferior/irrelevant?** OKB superior on entity/reasoning/updates; deepwiki-open irrelevant (code); Odysseus different class; llm-wiki-main superior on incremental-ingest determinism; llm-wiki-skill-main superior on semantic architecture + audit loop. §6.
10. **Smallest best-in-class architecture?** Integrity spine + canonical ledger + minimal evaluator + FTS5+reranker + future-agent contract. §9.
11. **Which chat failures still possible / owners / fix?** §4 table — #9 (skill), #24/#23 (observability) dominate.
12. **Exact future-agent interface?** §12.
13. **Maturity stage per layer?** §3.2 — orchestration/corpus *reliable*; validation *reliable/functional*; acceptance/observability *prototype*; retrieval *functional*.
14. **Competitor capabilities Apex already has, realized as well/safer?** determinism, custody, atlas, refusal — realized *better/safer* than competitors; queryable index realized adequately. §7 Part B.
15. **Which Odysseus/LLM-wiki capabilities additive?** LW2 hash-idempotent ingest, LW3 anchored-audit loop, OKB entity pages — additive; Odysseus memory/vector — duplicative/irrelevant here. §6, §7B.
16. **Retain/improve/add/experiment/defer/reject?** §7 Part B decision column + §8.
17. **Exact sequence to target maturity?** §10.
18. **Per Apex step: impact/value/safety/burden/net?** §7 Part A.
19. **Same metrics for competitors?** §7 Part B + Part C.
20. **What to install, in what order; what not to adopt?** Install: skill fix → integrity fixes → future-agent contract → reranker. Don't adopt: embeddings, graph, agent-memory, Mermaid. §8, §10.
21. **Cheaper to continue/freeze/replace/hybrid?** **Thin-integrity hybrid** (~25–45 h, highest net value). §11.
22. **Unique Apex value lost in replacement; retainable cheaply?** Determinism, zero-cost privacy, deterministic atlas, queryable custody — retainable as a thin layer under OKB in the fallback. §11.

---

*Prepared under the three-pillar mandate. All scores carry evidence notes; `N/E` used where product identity or evidence was insufficient. No KB/CLI/source changes were made during this audit.*
