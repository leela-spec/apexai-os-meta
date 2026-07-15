# Leela deterministic-run diagnostic audit

Audit date: 2026-07-15. Scope: read-only inspection of `LeelaAppDevelopment/LeelaApp-Index-KB-Wiki` in the supplied candidate worktree, excluding the expressly prohibited legacy `raw/` mechanism. No semantic compilation, acceptance, repair, Git mutation, or repository write was performed.

## Executive conclusion

- The deterministic artifact set is structurally valid: all 66 JSON files parse, the 9,172,513-byte map parses, and all ten projections name its exact SHA-256 and contain their declared 197 entries.
- The combined topic map is genuinely very large for browser-mediated semantic work: 9,172,513 bytes / 9,147,233 characters / 277,484 lines, estimated 2,293,129 readable tokens by the conservative `ceil(UTF-8 bytes / 4)` method.
- A topic projection is only 86.4–86.6 KB (about 21.6K estimated tokens). It preserves the 197 candidates for one topic and is the appropriate custody-facing entry point; it does **not** reduce the underlying 197-source candidate universe.
- The same 197 paths are represented for each of ten topics: 1,970 map rows and 1,970 projection rows, with 197 distinct paths and 167 distinct source IDs. This repetition is expected exhaustive coverage, not corruption.
- Ledgers and source atlases repeat the candidate universe again for provenance: roughly 260–270 KB and 193–213 KB per topic respectively. Their repetition becomes harmful only when a browser task eagerly reads several representations together.
- Local evidence strongly suggests a browser connector retrieval/action-size problem for the false “empty map” observation and the reported raw Git blob/tree failure. It does not prove a particular service limit or timeout value.
- Semantic acceptance currently fails/partials for content-specific missing requirements. Those results establish remaining contract/quality gaps, but local artifacts cannot apportion how much execution failure was caused by transport versus reasoning.
- Smallest safe change: retain the full map as deterministic machine evidence, delegate with one verified per-topic projection and a bounded source subset, preflight the read fan-out, and use topic-scoped commits/normal connected editing rather than large raw blob/tree batches.

## 1. Architecture snapshot

```
KB root
├─ manifests
│  ├─ corpus/source manifests; phase0 maps and projections; topic ledgers
├─ ingest-analysis
│  └─ Phase 1 source analyses
├─ wiki
│  ├─ topic dossiers and source atlases; concepts/entities
├─ audit / semantic-contract / outputs
│  └─ acceptance records, contract, query evaluation
└─ derived
   ├─ extracted manifest
   └─ search JSON/NDJSON/SQLite index
```

| Layer | Producer → primary consumer | Browser-semantic input? | Repeats source/candidate data? | Authority |
|---|---|---:|---:|---|
| Corpus scope, source manifest, payload manifest, registry | deterministic intake → validators/operators | metadata only | source identifiers/hashes | derived custody metadata; canonical material remains in `LeelaAppDevelopment` |
| Phase 0 postings, headings, links, duplicates/version families | deterministic scanner → ranking/navigation | selectively | source paths, headings, hashes | derived index evidence |
| Topic-source map and rankings | deterministic mapper → topic compiler | full map should be machine-only; projection is suitable | 197 paths per topic | derived, exhaustive custody |
| Navigation and acceptance projections | deterministic mapper → browser semantic task | yes, bounded | topic routing and 197 candidate records | derived dispatch/custody |
| Phase 1 analyses | semantic executor → dossier author/reviewer | yes, per source/topic | source refs and claims | derived analysis, review-needed |
| Topic ledgers | semantic executor → atlas/dossier/acceptance | yes, preferably scoped | 197 reviewed dispositions/topic | derived provenance |
| Dossiers and source atlases | semantic executor → readers/retrieval/acceptance | yes, one topic at a time | claims/source references; atlas has all candidates | derived semantic output |
| Semantic acceptance/audit | evaluator → release decision | evaluator output | query/claim observations | audit evidence, not source authority |
| Derived extraction/search | deterministic indexer → retrieval runtime | machine retrieval, not prompt payload | wiki chunks | derived index |

The required runtime checks succeeded: Apex health reports Python 3.11.9, `rg`, Git, SQLite 3.45.1 and FTS5 available; retrieval health likewise succeeds. Semantic-acceptance status is `fail` (19 records): canary entries are incomplete/partial and manual-browser records include concrete partial/missing query requirements, so no existing canary was treated as a pass.

## 2. Complete file-type inventory and snapshots

Text measures below are exact UTF-8 file measures. Token figures are estimates only: local `tiktoken` could not load `o200k_base` because its encoding download failed certificate verification, so this report uses `ceil(UTF-8 bytes / 4)`. Browser/API input, output, billing, and hidden-reasoning tokens are **unobservable** locally.

| Type | Files | Total bytes | Characters | Lines | Median bytes | Max bytes (largest path) | Est. tokens | Purpose / primary reader |
|---|---:|---:|---:|---:|---:|---|---:|---|
| `.json` | 66 | 16,488,352 | 16,018,422 | 424,808 | 20,235 | 9,172,513 `manifests/phase0/topic-source-map.json` | 4,122,088 | manifests, ledgers, acceptance, extraction/search metadata; runtimes and semantic tools |
| `.md` | 123 | 2,780,254 | 2,737,195 | 39,908 | 3,776 | 213,314 `wiki/summaries/feature-interconnections-source-atlas.md` | 695,064 | analyses, contract, dossiers/atlasses; people and semantic tasks |
| `.ndjson` | 1 | 121,588 | 121,111 | 150 | 121,588 | `derived/search/search-index.ndjson` | 30,397 | line-oriented derived search index; retrieval runtime |
| `.ps1` | 2 | 5,337 | 5,233 | 106 | 2,669 | `Materialize-ApexKBCorpus.ps1` | 1,335 | operational scripts; excluded from source-payload audit because the legacy mechanism is out of lifecycle scope |
| `.sqlite` | 1 | 200,704 | — | — | 200,704 | `derived/search/index.sqlite` | — | derived FTS5 index; retrieval runtime |
| no extension | 1 | 2 | 1 | 2 | 2 | `audit/resolved/.gitkeep` | 1 | empty-directory marker |

Total text: 193 files, **19,395,533 bytes**, **18,881,962 characters**, **464,974 lines**, estimated **4,848,885 tokens**. The SQLite file is binary; its inspected metadata is a 49-page × 4,096-byte database with `documents` and FTS5 `chunks_fts` tables.

Representative structural snapshots (redacted/shortened):

| Type | Representative path | Actual structure snapshot |
|---|---|---|
| JSON | `manifests/phase0/topic-source-map.json` | Top keys: `schema`, `topics`; topic: `{slug, name, discovery_terms, candidate_count:197, candidates:[…]}`; candidate: `{candidate_id:"cand-…", classification:"direct", content_pointer:{path, headings:[{level,line,text}]}, path:"LeelaAppDevelopment/…", sha256:"…", source_id:"src-…", text_readable:true}`. |
| Markdown | `wiki/summaries/skill-tree-source-atlas.md` | Grammar: front matter → `# … Source Atlas` → 197 `### Candidate cand-…` blocks. Block fields include Source ID/path, read scope, content snapshot, distinctive value, authority/freshness and contradiction/supersession relation. |
| Markdown | `ingest-analysis/phase1-user-stories-101-chunks-102-epics.md` | Grammar: front matter → `## 1. Source Identity` through `## 11. Decision`; `## 8. Key Claims` is a `Claim | Evidence pointer | Confidence` table (representative claim: “Topic-related context.”, confidence `mixed`). |
| NDJSON | `derived/search/search-index.ndjson` | One JSON record per line: `{chunk_id, claim_label, confidence, start_line, end_line, heading, rel_path, page_type, status, text, …}`; representative record indexes a wiki concept heading. |
| SQLite | `derived/search/index.sqlite` | Binary, hence no text snapshot. Schema records document metadata and FTS5 fields `chunk_id`, `title`, `heading`, `body`, tokenizer `unicode61`. |
| PowerShell / no extension | operational scripts / `.gitkeep` | No data snapshot: scripts are operational and excluded from analysis of the prohibited legacy source mechanism; `.gitkeep` is an empty marker. |

### Largest 25 files

| Path | Type | Bytes | Lines | Est. tokens | Role |
|---|---|---:|---:|---:|---|
| `manifests/phase0/topic-source-map.json` | JSON | 9,172,513 | 277,484 | 2,293,129 | exhaustive topic map |
| `manifests/phase0/process-flow-graph.json` | JSON | 938,329 | 18,862 | 234,583 | phase0 flow graph |
| `manifests/phase0/source-postings.json` | JSON | 721,859 | 25,298 | 180,465 | source headings/links postings |
| `manifests/phase0/heading-map.json` | JSON | 532,795 | 22,722 | 133,199 | heading index |
| `manifests/source-manifest.json` | JSON | 476,681 | 6,489 | 119,171 | source custody manifest |
| `manifests/phase0/topic-source-rankings.json` | JSON | 419,742 | 10,037 | 104,936 | ranked candidates |
| `manifests/topic-ledgers/epic.json` | JSON | 270,018 | 3,557 | 67,505 | topic ledger |
| `…/topic-ledgers/feature-interconnections.json` | JSON | 269,669 | 3,577 | 67,418 | topic ledger |
| `…/topic-ledgers/user-stories.json` | JSON | 267,497 | 3,578 | 66,875 | topic ledger |
| `…/topic-ledgers/algorithm.json` | JSON | 265,323 | 3,577 | 66,331 | topic ledger |
| `…/topic-ledgers/sequence.json` | JSON | 265,273 | 3,577 | 66,319 | topic ledger |
| `…/topic-ledgers/rhythm.json` | JSON | 264,640 | 3,577 | 66,160 | topic ledger |
| `…/topic-ledgers/stats.json` | JSON | 264,498 | 3,578 | 66,125 | topic ledger |
| `…/topic-ledgers/skill-tree.json` | JSON | 262,141 | 3,560 | 65,536 | topic ledger |
| `…/topic-ledgers/path.json` | JSON | 260,886 | 3,577 | 65,222 | topic ledger |
| `…/topic-ledgers/creator-epic-content.json` | JSON | 260,573 | 3,557 | 65,144 | topic ledger |
| `wiki/summaries/feature-interconnections-source-atlas.md` | MD | 213,314 | 2,768 | 53,329 | source atlas |
| `…/user-stories-source-atlas.md` | MD | 211,168 | 2,768 | 52,792 | source atlas |
| `…/algorithm-source-atlas.md` | MD | 208,930 | 2,768 | 52,233 | source atlas |
| `…/sequence-source-atlas.md` | MD | 208,906 | 2,768 | 52,227 | source atlas |
| `…/rhythm-source-atlas.md` | MD | 208,242 | 2,768 | 52,061 | source atlas |
| `…/stats-source-atlas.md` | MD | 208,088 | 2,768 | 52,022 | source atlas |
| `…/skill-tree-source-atlas.md` | MD | 206,011 | 2,770 | 51,503 | source atlas |
| `…/path-source-atlas.md` | MD | 204,595 | 2,770 | 51,149 | source atlas |
| `…/epic-source-atlas.md` | MD | 201,999 | 2,567 | 50,500 | source atlas |

## 3. Token and volume accounting

| Artifact class | Files | Bytes | Characters | Lines | Est. tokens |
|---|---:|---:|---:|---:|---:|
| Corpus/source manifests | 5 | 724,041 | 710,485 | 10,289 | 181,011 |
| Phase0 maps/navigation/projections | 24 | 13,043,944 | 12,629,634 | 374,649 | 3,260,986 |
| Topic ledgers | 10 | 2,650,518 | 2,612,581 | 35,715 | 662,630 |
| Phase1 analyses | 68 | 316,810 | 308,653 | 7,647 | 79,203 |
| Wiki dossiers/atlasses/concepts/entities | 32 | 2,208,757 | 2,176,747 | 29,418 | 552,190 |
| Semantic acceptance/audit/log | 32 | 82,154 | 79,844 | 2,268 | 20,539 |
| Semantic contract | 7 | 12,772 | 12,453 | 326 | 3,193 |
| Derived extraction/search | 5 | 499,347 | 294,343 | 3,606 | 124,837 |
| Outputs | 1 | 15,908 | 15,468 | 441 | 3,977 |

The combined map is about **106×** a typical 86.5 KB projection (2.293M vs. about 21.6K estimated tokens). Per-topic projection + ledger + atlas + dossier is 558,242–578,385 bytes (139.6K–144.6K estimated tokens); the Skill Tree set is 561,245 bytes / about 140,312 estimated tokens.

Each topic currently enumerates the same 197 canonical paths: 1,970 candidate rows in the combined map, 1,970 in ten projections, 1,970 in ten ledgers, and 1,970 atlas candidate blocks. Within the combined map there are 1,970 distinct candidate IDs but only 197 paths and 167 source IDs (hash-level duplicate identities account for the difference). The map contains pointers/headings/hashes, not embedded source text snapshots or capsules.

Likely Skill Tree browser read fan-out before opening any canonical sources: registry 7,734 + projection 86,469 + navigation 180,227 + existing ledger 262,141 + atlas 206,011 + dossier 6,624 = **749,206 bytes** (~187K estimated tokens). The 197 referenced source files total 30,479,519 bytes (146 text-readable; ~654,842 tokens by text bytes). That source total is an upper bound: it applies only if the browser eagerly opens every candidate, not if it opens a selected evidence subset.

## 4. Duplication and access shape

Repetition has a custody purpose: the map establishes exhaustive candidate coverage per topic; projections make one topic self-contained; ledgers record reviewed disposition; atlasses make provenance navigable. It does not copy canonical source bodies into the map. However, path/hash/headings, candidate disposition, and short textual summaries are repeated across these layers.

| Access shape | Deterministic custody required | Semantic evaluator actually needs | Measured consequence |
|---|---|---|---|
| Full combined map | all 10 topic × 197 candidate relationships | normally no: one topic’s routing is enough | 9.17 MB / ~2.29M estimated tokens before navigation, outputs, or source reads |
| One projection + navigation + selected sources | one topic’s 197 candidate custody and map hash | yes: topic terms, candidate paths/pointers, selected canonical evidence, existing topic output | 86.4–86.6 KB projection (~21.6K tokens); navigation/output/source reads still need explicit limits |

Therefore, keep the exhaustive map as a machine artifact. The harmful condition is not its existence but passing it to a browser semantic operation that also reads duplicated ledger/atlas data or all sources.

## 5. Failure-cause assessment

| Hypothesis | Assessment | Direct evidence | Counter-evidence / unknown |
|---|---|---|---|
| H1 invalid/corrupt deterministic content | **not supported** | all 66 JSON parse; map SHA-256 is `e47a…32b2ec`; all ten projections match it and declare/contain 197 candidates | parsing/hash linkage does not prove every semantic claim is correct |
| H2 combined map too large/poorly shaped for reliable browser-connector retrieval | **strongly suggested** | map is 9.17 MB / ~2.29M estimated tokens; a fresh browser reportedly called it empty while local parsing succeeds | no connector telemetry or published size threshold was available, so causality cannot be confirmed |
| H3 repeated representations inflate browser prompt/tool payloads enough to harm completion | **strongly suggested** | same 197 paths recur in four topic-level forms; fixed Skill Tree fan-out is 749 KB before sources; all-source upper bound is 30.5 MB | a bounded task need not read all forms or sources, so repetition alone does not establish failure |
| H4 raw Git blob/tree upload and connector action-time limits caused Codex-managed failure | **strongly suggested** | reported large atomic Skill Tree raw blob/tree failure contrasts with successful topic-scoped browser commits | local files do not expose action duration, server response, or exact timeout/limit |
| H5 remaining failures are mainly content/contract gaps rather than size failures | **possible** | acceptance records name concrete unmet requirements, e.g. Skill Tree lacks display-state semantics; status is fail/partial | a size/transport failure could have prevented adequate review/repair, so local evidence cannot determine the main cause |

## 6. Minimal corrective recommendations

1. Retain `topic-source-map.json` unchanged as machine custody evidence; supply the matching one-topic projection (verified by its `source_map_sha256`) to browser work.
2. Add a read-only preflight to every browser delegation: bytes, `ceil(bytes/4)` estimate, planned files, source count, and separate upper bounds for selected vs. all-source reads. Mark browser/API token telemetry as unobservable unless actually supplied.
3. Preserve Phase 1 analyses, ledgers, and atlasses, but instruct each semantic task to read one representation for its purpose and a bounded, named set of canonical sources—never an undifferentiated all-candidate batch.
4. Keep topic-scoped commits and local deterministic validation before repair prompts. Do not combine the ten-topic map, all outputs, and a large semantic change into one browser action.
5. Avoid raw Git blob/tree upload for large files; prefer a normal connected edit/commit or complete-file return when available. This changes delivery mechanics, not custody or canonical-source placement.

No embeddings, vector database, copied corpus, or second corpus architecture is warranted by this audit.
