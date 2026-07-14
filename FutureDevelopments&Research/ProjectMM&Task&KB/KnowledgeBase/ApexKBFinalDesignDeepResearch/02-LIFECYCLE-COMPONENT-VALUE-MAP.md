# Apex KB Lifecycle Component and Value Map

## Rating method

Scores are rough hypotheses for Deep Research to verify.

- **Token efficiency, value, resilience:** 1 = poor, 5 = excellent.
- **Setup cost, management cost:** 1 = low, 5 = high.
- A high-cost component is not rejected automatically; it must earn the cost through measurable downstream savings or integrity.
- `Current` means present on `origin/main` at `d72f07f7b598`; `partial` means the mechanism exists but not at the required capability.

## Macro lifecycle

| Phase | Product question | Primary owner | Required output |
|---|---|---|---|
| A. Target and custody | What corpus and questions are in scope, and can every source be traced? | Operator + deterministic runtime | scope, registry, inventory, hashes, duplicate families |
| B. Corpus intelligence | Where is each concept discussed, with what explicit structural signals? | Deterministic runtime | structure maps, postings, exhaustive topic maps, navigation report |
| C. Semantic compilation | What do those files mean, how do they relate over time, and what should future AIs know? | LLM | source capsules, topic analysis, concept dossier, source atlas |
| D. Semantic acceptance | Can an independent AI answer from compiled pages, and are material claims entailed? | Fresh LLM context | reason-coded acceptance artifact |
| E. Retrieval | Can the accepted compiled layer be found quickly and reproducibly? | Deterministic runtime + answering LLM | wiki index, chunk index, ranked hits, query packet |
| F. Maintenance | What changed, what is stale, and what compiled knowledge is affected? | Deterministic runtime + bounded LLM update | impact set, refreshed capsules/pages, lint/audit/postflight evidence |

## Meso lifecycle components

| ID | Component / instruction | Input → output → next consumer | Current | Token eff. | Value | Resilience | Setup cost | Mgmt cost | Recommended disposition |
|---|---|---|---|---:|---:|---:|---:|---:|---|
| A01 | Scope lock | source roots/exclusions → `corpus-scope` → inventory | missing | 5 | 5 | 5 | 2 | 1 | **Add.** Every omitted path needs an explicit reason. |
| A02 | Topic and target-question lock | operator concepts/questions → registry → Phase 0 + semantic acceptance | current v2 for questions; weak vocabulary | 5 | 5 | 4 | 2 | 2 | **Keep and extend.** Separate primary phrases, aliases, supporting terms, and expected dossier/atlas routes. |
| A03 | Source intake/custody | files/pointers → raw tree + source manifest → hashing/analysis | current | 4 | 5 | 5 | 2 | 2 | **Keep.** Preserve pointer/copy/snapshot modes. |
| A04 | Hash inventory | scoped files → path/bytes/hash/type records → duplicates/staleness | current, split across artifacts | 5 | 5 | 5 | 1 | 1 | **Keep and unify.** One exhaustive inventory should drive all later stages. |
| A05 | Exact duplicate groups | hashes → representative/path groups → topic maps/source reads | partial in profile only | 5 | 4 | 5 | 1 | 1 | **Promote.** Integrate with routing and capsule reuse. |
| A06 | Normalized/version families | names/normalized text/Git facts → possible families → LLM version judgment | missing | 4 | 4 | 3 | 3 | 2 | **Add conservatively.** Preserve the matching evidence; never auto-supersede. |
| B01 | Corpus profile | inventory → counts, sizes, types, warnings → operator/LLM orientation | current | 5 | 3 | 5 | 1 | 1 | **Keep compact.** Useful orientation, not ranking authority. |
| B02 | Markdown structure parser | text → H1/headings/section spans/links/fences/frontmatter → postings/topic maps | current, section spans incomplete | 5 | 5 | 4 | 2 | 2 | **Improve.** Python state machine first; optional parser validation only on demonstrated failures. |
| B03 | Non-Markdown extraction | docx/pptx/xlsx/pdf/text/code → pointer-stable text/metadata → topic maps | partial/format-dependent | 4 | 4 | 3 | 3 | 3 | **Capability-gated.** Unsupported files remain visible and blocked, never silently absent. |
| B04 | Generic term profile | corpus text → top terms → topic proposal | current | 5 | 2 | 4 | 1 | 1 | **Keep secondary.** Do not use generic term volume as source priority. |
| B05 | Exhaustive term postings | configured phrases/aliases → per-field counts and pointers → topic maps | missing | 5 | 5 | 5 | 2 | 1 | **Add.** This is the intended token-saving index. |
| B06 | Field-separated topic matching | path/name/title/H1/heading/body/link signals → candidate rows → LLM navigation | missing; substring count only | 5 | 5 | 5 | 3 | 2 | **Replace current ranking.** Preserve every signal, not one score. |
| B07 | Candidate classes | deterministic signals → direct/section-primary/dense/contextual/linked/duplicate → read order | missing | 5 | 5 | 4 | 2 | 2 | **Add.** Classes are navigation labels, not semantic truth. |
| B08 | Lifecycle/authority hints | configured path rules/dates/Git history → current/prototype/historical/implementation hints → LLM review | missing | 5 | 5 | 3 | 2 | 2 | **Add with strict wording.** Hints must show their rule/evidence. |
| B09 | Explicit link/process graph | links/YAML paths/manifests/arrows → graph edges/hubs → contextual candidates | current as optional graph, partial coverage | 4 | 3 | 4 | 3 | 2 | **Keep optional V1.5.** Useful for cross-feature routes; not required for basic topic maps. |
| B10 | Exhaustive machine topic map | all B-stage signals → every candidate row → semantic classifier | missing; current top 30 | 5 | 5 | 5 | 3 | 1 | **Add as canonical derived artifact.** Never top-N truncate this set. |
| B11 | Compact topic navigation view | machine map → direct/core/context/duplicate read order → LLM startup | missing | 5 | 5 | 4 | 2 | 1 | **Add.** This is the bounded view that saves LLM tokens. |
| B12 | Populated navigation report | all topic maps/profile/warnings → read-first batches and gaps → operator/semantic route | shell only | 5 | 5 | 4 | 2 | 1 | **Implement research contract.** Remove if it merely repeats artifact names. |
| C01 | Per-source semantic capsule | unique reviewed source/hash → summary, authority, claims, topic coverage, pointers → many topics | current Phase 1 is close but path-oriented | 4 | 5 | 4 | 2 | 2 | **Refactor for hash reuse.** Full core reads; exact targeted sections for contextual sources. |
| C02 | Candidate disposition | exhaustive topic map + capsules → one status/value/snapshot per candidate → atlas/page plan | partial ledger only | 4 | 5 | 5 | 2 | 2 | **Make mandatory and lean.** Every candidate appears once. |
| C03 | Freshness/authority judgment | deterministic hints + source content → current/prototype/historical/proposal/implementation assessment → synthesis | current conceptually | 3 | 5 | 3 | 1 | 2 | **Keep LLM-owned.** Cite evidence and confidence. |
| C04 | Contradiction/supersession analysis | source claims + dates/version evidence → preserved relationships → dossier/atlas | current | 3 | 5 | 4 | 2 | 2 | **Keep.** Never infer solely from filenames or dates. |
| C05 | Target-query coverage | questions + reviewed evidence → answered/partial/blocked → source continuation/page plan | current v2 | 4 | 5 | 5 | 2 | 2 | **Keep.** Add source-atlas questions to broad concept targets. |
| C06 | Page-topology decision | recurring questions/duplication → dossier/subpages/atlas → Phase 2 | current v2 | 4 | 4 | 4 | 1 | 2 | **Simplify.** Minimum page count, complete answer and source coverage. |
| C07 | Concept dossier drafting | topic analysis/capsules → Macro/Meso/Micro answer page → future AI/query evaluator | current template, output unreliable | 3 | 5 | 3 | 1 | 2 | **Redesign around direct knowledge.** Avoid repetitive governance blocks. |
| C08 | Complete source atlas | candidate dispositions → per-file snapshot/value/freshness/pointers → future AI/source navigator | missing | 5 | 5 | 5 | 2 | 2 | **Add.** Embed only for small candidate sets; otherwise separate page. |
| C09 | Cross-page linking/index proposal | dossier relationships → routes/page catalog candidates → deterministic indexer | current | 4 | 4 | 4 | 1 | 2 | **Keep.** Deterministic index rebuild owns final catalog. |
| C10 | Durable progress recovery | completed candidate IDs/next action → context restart → next semantic context | current ledger is heavy | 4 | 3 | 4 | 2 | 3 | **Reduce.** Store only state that prevents rereads or lost decisions. |
| D01 | Page-only query evaluation | target questions + compiled pages only → answerability verdicts → repair | current v2 | 3 | 5 | 5 | 1 | 2 | **Keep mandatory and fresh-context.** |
| D02 | Claim entailment sampling | independently selected claims + source passages → support verdicts → repair | current v2 | 2 | 5 | 4 | 1 | 2 | **Keep bounded.** Risk-based sample, all claims when page is small. |
| D03 | Discovery/atlas acceptance | topic map + topic analysis + atlas → candidate completeness/one-to-one coverage → semantic completion | missing | 5 | 5 | 5 | 2 | 1 | **Add.** Deterministic consistency plus LLM review of classification quality. |
| E01 | Wiki index rebuild | accepted pages/frontmatter → `wiki/index.md` → index-first query | current | 5 | 4 | 5 | 1 | 1 | **Keep deterministic.** Do not manually duplicate the full index in prompts. |
| E02 | Heading-based chunk index | accepted pages → JSON/NDJSON chunks → lexical/FTS search | current | 5 | 5 | 5 | 2 | 1 | **Keep.** Index answer-bearing sections and source-atlas rows sensibly. |
| E03 | SQLite FTS5/BM25 | chunks + runtime probe → local ranked hits/snippets → query router | current with fallback | 5 | 4 | 4 | 3 | 2 | **Keep derived/optional.** Test technical identifiers and tie-breaking. |
| E04 | JSON lexical fallback | chunks → deterministic token score → query router | current | 4 | 4 | 5 | 1 | 1 | **Keep.** Required graceful fallback. |
| E05 | Index-first query | question + wiki index/retrieval hits → 3–5 answer pages → grounded answer | current | 5 | 5 | 4 | 1 | 1 | **Keep.** Raw reopen only for conflict/verification, not routine answers. |
| E06 | Save/promote synthesis | useful answer → query output/concept update → compounding wiki | present in LLM-Wiki, partial Apex | 4 | 4 | 3 | 1 | 2 | **Add only with evidence and review rules.** Prevent chat opinions becoming authority. |
| F01 | Structural lint | pages/index/links/frontmatter → reason-coded defects → repair | current | 5 | 4 | 5 | 2 | 1 | **Keep.** Never present as semantic proof. |
| F02 | Semantic health review | accepted pages + new evidence → contradictions/gaps/drift → audit items | partial | 2 | 4 | 3 | 1 | 3 | **Run on change/need, not every compile.** |
| F03 | Audit feedback loop | human comments + anchors → accepted/rejected corrections → pages/log | current | 4 | 4 | 4 | 2 | 2 | **Keep file-based core.** UI is optional. |
| F04 | Staleness/impact analysis | changed hashes + source/page dependencies → affected topics/pages → bounded recompile | partial | 5 | 5 | 5 | 3 | 2 | **Add as core incremental value.** |
| F05 | Postflight/status | semantic acceptance + deterministic freshness/quality → truthful state → consumers | current v2 | 5 | 5 | 5 | 2 | 1 | **Keep.** Refuse `query_ready` when either gate is stale. |
| F06 | Orchestration consumption | compact cited packets → Plan/Session/Sync reads → task reasoning | boundary defined | 5 | 4 | 4 | 1 | 1 | **Keep read-only boundary.** KB must not mutate orchestration state. |

## Tool and implementation option map

| Tool / mechanism | Creates value by | Token eff. | Value | Resilience | Setup cost | Mgmt cost | Decision guidance |
|---|---|---:|---:|---:|---:|---:|---|
| `git ls-files` / filesystem walk | exhaustive path baseline | 5 | 5 | 5 | 1 | 1 | Core; choose behavior based on scoped tracked/untracked policy. |
| `rg` | fast exact searches and implementation diagnostics | 5 | 4 | 5 | 1 | 1 | Core operator tool; script should not depend on shelling out when Python can scan deterministically. |
| Python state-machine Markdown parser | headings, links, fences, frontmatter boundaries, line spans | 5 | 5 | 4 | 2 | 2 | Core V1 from parser research. |
| `markdown-it-py` | token-boundary validation for complex Markdown | 4 | 3 | 5 | 2 | 2 | Optional when fixtures expose real parser failures. |
| `python-frontmatter` / PyYAML | robust metadata parsing | 4 | 4 | 5 | 2 | 2 | Prefer over broad regex if existing frontmatter needs full YAML. No invented stdlib-only restriction. |
| DOCX/PPTX/XLSX/PDF extractors | deterministic visibility for non-Markdown sources | 4 | 4 | 3 | 3 | 3 | Capability probe; each format needs pointer fixtures and blocked status. |
| SQLite FTS5 | local ranked chunk retrieval | 5 | 4 | 4 | 3 | 2 | Keep after runtime probe; JSON fallback mandatory. |
| Explicit graph extractor | cross-feature/path/process navigation | 4 | 3 | 4 | 3 | 2 | Optional once topic-map value is proven; no semantic graph invention. |
| `fd` | convenient file discovery | 4 | 2 | 5 | 2 | 1 | Not required when inventory walker/`rg --files` exists. |
| `tokei` or `scc` | corpus code/line statistics | 4 | 2 | 5 | 2 | 1 | Choose at most one only if stats drive a decision. |
| `cloc` | older line statistics | 3 | 1 | 4 | 2 | 2 | Defer/reject; duplicates lighter tools. |
| Node `remark/unified` | high-fidelity Markdown/MDX AST | 3 | 3 | 5 | 4 | 4 | Defer until Python parser fails material fixtures. |
| MkDocs/mdBook/Docusaurus | publishing and browser search | 2 | 1 | 3 | 4 | 4 | Reject from core lifecycle; publishing is a separate product. |
| qmd/vector/hybrid retrieval | semantic recall beyond lexical terms | 3 | 3 | 3 | 4 | 4 | Defer until measured query failures survive aliases/tags/BM25. |
| Obsidian plugin / web viewer | human browsing and anchored feedback | 3 | 3 | 3 | 4 | 4 | Optional UI; preserve simple audit-file protocol without requiring it. |

## LLM instruction pattern map

| Pattern from research/blueprints | Value to preserve | Failure if copied literally | Final design question |
|---|---|---|---|
| Two-phase ingest | Separates evidence analysis from durable synthesis. | Per-source operator stop can make large compiles impractical. | Can topic batches retain reviewability without a confirmation turn after every file? |
| One source touches 5–15 pages | Captures the original compounding-wiki value. | Unbounded writes and duplicate prose can explode cost. | How are affected pages derived and how is duplicated knowledge avoided? |
| Divide and conquer | Focused pages support selective reading and auditing. | Fixed word thresholds become proxy targets. | Use retrieval/question boundaries rather than hard word counts. |
| Index-first query | Reduces routine reads to a small page set. | A shallow index routes to shallow pages. | Gate index build on accepted dossier/atlas value. |
| Save useful answers | Prevents repeated synthesis. | Answers may be opinionated or stale. | Require source traceability, target route, and promotion review. |
| Quick deterministic lint + full semantic lint | Separates cheap structure from expensive meaning. | Full lint can reread the whole wiki routinely. | Trigger semantic health only on affected pages or explicit audits. |
| Hash sentinel/idempotency | Prevents reprocessing unchanged sources. | Path-only or sentinel-only state can miss policy/schema changes. | Include source hash plus semantic contract/capsule version. |
| Daily log/hot cache | Supports continuity. | Logs become another corpus and context burden. | Keep compact machine run records and human summaries only when useful. |
| Fresh-context evaluator | Prevents drafter self-certification. | Evaluator can still receive incomplete candidate evidence. | Add independent discovery/atlas consistency checks. |
| Browser connector runbook | Makes account Skills optional. | Too many contract files and ledger fields consume the connector context. | Reduce startup to one short contract, one topic map, capsules, and unresolved sources. |

## Handoff integrity rules

Every stage must make the next stage cheaper and more reliable:

1. Scope feeds inventory; inventory count must reconcile with inclusions and exclusions.
2. Inventory IDs and hashes are reused by all maps; no later stage invents source identity.
3. Structure/posting records carry exact pointers; topic maps point to those records rather than copying long snippets.
4. Topic maps are exhaustive machine artifacts; compact views are projections, never authoritative subsets.
5. Semantic source capsules cite inventory IDs/hashes and reviewed spans.
6. Topic analysis dispositions cover every topic-map candidate exactly once.
7. Dossier claims and atlas rows point to capsules and source passages.
8. Acceptance checks declared questions, claim entailment, and candidate/atlas completeness.
9. Retrieval indexes only accepted compiled pages and records their hashes.
10. Change detection uses hashes/dependencies to reprocess only affected capsules, topics, and pages.

If an artifact has no identified consumer, does not prevent a demonstrated failure, and does not reduce repeat work, it should be removed from the mandatory path.
