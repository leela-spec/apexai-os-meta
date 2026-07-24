# Apex KB — Project status & roadmap

- **Date:** 2026-07-24
- **Branch:** `claude/apex-kb-audit-mz3hre` (Phase-1 commits `30182952 → 99cdde17`)
- **Tests:** 54/54 green (`python3 -m pytest -q` in `apex-meta/apex-kb-cli`)
- **Scope of work to date:** Apex KB **CLI infrastructure** (the `apex-kb` exe + its skill + a new operator agent). The therapy KB was **not** touched; all verification is on scratch/fixture KBs.

## Where the project is (plain language)
Apex KB is a working, local, offline, deterministic system that compiles Markdown notes into a source-preserving wiki with a searchable index. After Phase 1 it is now **honest about its own state**, **portable across machines**, **observable** (progress + plain-language blockers), and **discoverable by future AI agents** (the skill exposes search; an operator agent drives it without drift). What is *not yet proven* is measured answer/retrieval quality — that needs the Phase-2 benchmark. In short: the trust, usability, and integrity failures are fixed; the "is the content measurably good?" question is the next phase.

## Maturity by layer (updated for Phase 1)
| Layer | Stage | Note |
|---|---|---|
| Deterministic orchestration / state machine | reliable | atomic writes, single-legal-action, bounded numbered repair |
| Corpus intelligence (Phase 0) | reliable | exhaustive candidate maps, byte-identical rebuilds |
| Deterministic validation gate | **reliable (was functional)** | now validates ranked-source citations + route coverage (A2) and one canonical pointer ledger (B4), not just answers/claims |
| Semantic acceptance (independent quality) | prototype (opt-in) | A4 kept off by default; state no longer overclaims it (B2) |
| Update / drift | **functional+ (was functional)** | portable resolution + surfaced in status/doctor (B3) |
| Packaging | **functional/portable** | pypdf optional; clean install no longer crashes (PK1) |
| Observability | **functional (was prototype)** | progress block, plain-language blockers, `pointer_health` probe (O1/B4) |
| Retrieval engine | functional (cleaner) | FTS5 lexical; clean excerpts + answer-first ranking + future-agent contract (C1/C2); precision not yet benchmarked |
| Skill (③) + operator agent (④) | new / reliable | skill reconciled to the real CLI (B1); `apex-kb-operator` agent drives it (AG1) |

## What Phase 1 delivered (13 packets + probe)
- **B1** skill reconciled to the installed CLI (all 7 commands incl. `query`; legacy `apex_kb.py control` removed/bannered).
- **AG1** `.claude/agents/apex-kb-operator.md` — thin CLI-driving agent (CLI is sole authority; no drift).
- **A0** `docs/prompt-design-notes.md` — evidence-based prompt patterns.
- **A1** richer Phase 1/2 task templates + engine contracts (full pointer/claim coverage, paragraph depth).
- **A3** optional `related_pages` cross-link field + renderer (interlinked wiki).
- **B2** honest acceptance state in postflight (no vacuous pass).
- **B3** portable source-drift, surfaced in `status`/`doctor`.
- **O1** progress block + plain-language blocker explanations.
- **C1** clean query excerpts + answer-chunk-first ranking.
- **C2** future-agent query contract (retrieval policy / context budget / authority / answer contract).
- **PK1** `pypdf` optional.
- **A2** ranked-source citation validation + route coverage enforcement.
- **B4** one canonical pointer ledger + non-fatal `pointer_health` probe in `doctor`.

## Roadmap — Phase 2 (deferred, retained; KB-quality work)
Do **not** run these against the therapy KB casually; they are the "how we test / improve the KB content" phase, executed deliberately (semantic drafting in an unlimited-token chat).
1. **D-BENCH** — build the KB-quality benchmark: golden query set, expected-answer rubric, claim-entailment set, retrieval precision/recall set, token-savings measurement, multi-hop and raw-reopen cases. *Foundation for every quality claim; gates D-C3.*
2. **D-R1 → D-R2** — emit fresh richer packets (`apex-kb update` + `drive`, token-free) then re-draft dossier content via the `apex-kb-operator` agent in the operator's unlimited-token chat; import/validate deterministically. This is what turns A1/A3 *capability* into *realized* richer pages.
3. **D-C3** — local reranker over FTS5 top-K, adopted **only if** it beats the FTS5 baseline on D-BENCH.
4. **S1** — index the 11th source (`Integrierte Psychologiekarte & OS.md`) or record an explicit exclusion (therapy-KB-specific; Phase 2).
5. **Optional** — promote `pointer_health` from a probe to a gate once pointer formats are proven stable; write-time path normalization (`as_posix()`) to finish D8.

## Tests to come (the KB-quality test plan)
Currently the 54 tests prove lifecycle/schema/identity/determinism/rejection — **not** answer quality. Add, under D-BENCH:
- golden-query → expected-answer rubric (per locked topic);
- claim-entailment set (sampled claims → source lines);
- retrieval precision/recall set (relevance-judged);
- token-savings measurement (KB vs raw corpus per question);
- multi-hop / cross-topic synthesis cases;
- raw-source-reopen trigger cases;
- (if adopted) reranker A/B vs FTS5 baseline.

## Pointers
- Full audit + post-Phase-1 re-score: `apex-meta/kb/therapy-narm-personal-development/audit/reports/2026-07-24-apex-kb-value-audit.md` (§15).
- Task packets (Phase-1 status + Phase-2 deferred): `apex-meta/apex-kb-cli/docs/apex-kb-improvement-tasks.md`.
- Knowledge index: `apex-meta/apex-kb-cli/docs/KNOWLEDGE-INDEX.md`.
