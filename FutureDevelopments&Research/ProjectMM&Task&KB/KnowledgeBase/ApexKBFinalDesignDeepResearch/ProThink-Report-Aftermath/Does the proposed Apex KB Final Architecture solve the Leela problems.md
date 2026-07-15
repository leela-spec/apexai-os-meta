# Does the proposed Apex KB Final Architecture solve the Leela problems?

## Verdict

**Partly. It is a major improvement, but it does not yet fully solve the problem we identified.**

It correctly solves:

- duplicated deterministic metadata;
- repeated full-source reading across topics;
- hand-authored ledger/atlas drift;
- combined all-topic map delivery;
- unclear Codex/browser/Git ownership;
- whole-KB rebuilds after small changes.

It only partly solves:

- large per-topic artifacts;
- browser task-packet size;
- topic isolation;
- semantic processing of many irrelevant candidates;
- acceptance cost.

Its remaining central problem is this requirement:

> Every deterministic topic candidate must receive a semantic row and a complete source-atlas account.

That preserves a stronger documentary-atlas product, but it also preserves much of the expensive semantic review that overloaded Leela.

## Problem-by-problem comparison

| Identified Leela problem | Proposed architecture | Verdict |
|---|---|---|
| `source-postings.json` and `heading-map.json` repeat headings | Replaces split heading/link/frontmatter truths with one canonical structure record | **Solved** |
| Path/hash/type repeated in downstream artifacts | One inventory owner; semantic files reference source ID | **Solved** |
| One 9.17 MB combined ten-topic map | One exhaustive map per concept plus compact projection | **Mostly solved** |
| Every topic receives zero-signal sources | Candidate-map acceptance requires every candidate to have a match or graph reason | **Solved if implemented faithfully** |
| Broad substring matches still nominate many weak sources | Better field/phrase/co-occurrence/negative-term rules, but all matched candidates remain | **Partly solved** |
| Same source reread for multiple topics | One hash-keyed source capsule reused across topics | **Strongly solved** |
| Ledger and atlas separately repeat semantic judgments | Canonical topic record; atlas rendered deterministically | **Solved** |
| Browser reads giant raw bodies in prompts | Task packet contains routes/hashes and browser opens sources directly | **Improved** |
| Browser receives an entire large topic review obligation | Default batch remains one concept plus its full atlas obligations | **Not fully solved** |
| One large topic JSON | Still proposes `ingest-analysis/topics/<topic-id>.analysis.json`; partitioning is only an unresolved probe | **Not solved yet** |
| No explicit browser size/token limit | Says “bounded” and “small enough,” but provides no hard preflight threshold | **Not solved** |
| All 197 Skill Tree candidates reviewed to find 5 material sources | Zero-signal rows disappear and duplicates reuse capsules, but every matched candidate still needs semantic disposition | **Partly solved** |
| Acceptance reads map/ledger/atlas broadly | Page-only query evaluation is narrow, but Layer 4 still requires complete atlas faithfulness | **Partly solved** |
| Raw Git blob/tree/action failure | Browser returns a bundle; Codex imports, validates, and performs Git | **Architecturally solved** |
| Small source change causes broad rebuild | Dependency/impact closure invalidates only affected artifacts | **Solved** |
| Actual dossier content gaps | Four-layer acceptance detects them and blocks promotion | **Detection solved; content still requires repair** |

## Important improvement over the current Leela map

The final design does **not** appear to intend “all files are candidates for all topics.” Its success condition says every candidate must have an inspectable match or graph reason.

Applied to the measured Leela map, that would remove the 586 zero-signal topic/source rows.

However, the current signal-bearing counts were still large:

| Topic | Current 197 rows | Rows with at least one signal |
|---|---:|---:|
| Skill Tree | 197 | 135 |
| Path | 197 | 130 |
| User Stories | 197 | 120 |
| Epic | 197 | 153 |
| Sequence | 197 | 154 |

Skill Tree ultimately retained only 5 material sources. Therefore, removing zero-signal candidates helps, but it does not by itself create a small semantic work queue.

## Where the proposed design is excellent

### 1. One deterministic fact owner

The design consolidates inventory, headings, links, frontmatter, hashes, and format facts. This directly fixes the duplicate `source-postings`/`heading-map` problem.

### 2. Hash-keyed source capsules

One source is semantically read once per content hash. Several topics reuse that capsule instead of reopening the source. This is the highest-value token-saving mechanism in the proposal.

### 3. Topic record is canonical; atlas is generated

The semantic judgment is authored once. The human-readable atlas is a deterministic rendering, so it cannot drift from the topic record.

### 4. Per-topic maps

Splitting the combined map by concept eliminates the specific 9.17 MB all-topic connector read.

### 5. File-backed orchestration

Codex performs deterministic work and Git; the browser returns bounded semantic artifacts; independent evaluation is separate. This removes the large raw Git upload assumption.

### 6. Incremental invalidation

Changed hashes affect only dependent capsules, topic rows, claims, acceptance, and retrieval chunks. This makes maintenance much more efficient.

## Where the proposal still conflicts with our modularity goal

### 1. It keeps a large single topic-analysis JSON

The planned path is:

`ingest-analysis/topics/<topic-id>.analysis.json`

That file must contain one semantic row for every candidate. The research itself calls large-topic JSON practicality an unvalidated hypothesis and says partitioning thresholds still need a technical probe.

This is not sufficient for a “no big files” architecture.

### 2. It makes the full documentary atlas a mandatory semantic product

The design requires every candidate to receive:

- snapshot;
- individual value;
- lifecycle role;
- disposition;
- authority/freshness reasoning;
- evidence pointer or blocker.

That is valuable for source-landscape research, but expensive for routine concept compilation. It turns every keyword/graph match into an LLM-authored obligation.

### 3. The task packet is bounded in prose, not by contract

The report says packets should be “bounded,” “compact,” and “small enough,” but defines no:

- maximum bytes;
- maximum estimated tokens;
- maximum sources per wave;
- automatic shard condition;
- refusal/preflight behavior.

Therefore the same browser overload can recur under a new filename.

### 4. The batch unit is still too broad

The default save batch is one concept plus the full source-atlas obligation. For a large concept, that is not a bounded semantic unit.

The better browser unit is:

`one topic + one target query + one source wave`.

### 5. Atlas acceptance can dominate knowledge acceptance

Page-only answerability and claim entailment are properly narrow. But the fourth acceptance layer requires candidate equality and individual semantic faithfulness across the entire atlas.

That can make a correct five-source Skill Tree dossier fail because an irrelevant 130th source has a weak snapshot. Documentary completeness and answer quality should remain separately visible rather than block each other by default.

## Required amendments

### Amendment A — split custody atlas from semantic atlas

Use two layers:

1. **Deterministic custody atlas:** every matched candidate, reason, pointer, extraction state, duplicate state, and blocker. Generated without LLM review.
2. **Semantic evidence atlas:** only reviewed/material/supporting/contradicting/historical sources needed by target questions.

Unreviewed candidates remain visible as `not_semantically_reviewed`; they are not silently dropped and do not require invented semantic snapshots.

This retains losslessness without forcing an LLM to explain every weak match.

### Amendment B — shard topic analysis by candidate/query

Replace:

```text
ingest-analysis/topics/<topic>.analysis.json
```

with:

```text
ingest-analysis/topics/<topic>/
├─ manifest.json
├─ queries/<query-id>.json
├─ sources/<source-id>.json
├─ claims/<claim-id>.json
└─ blockers.json
```

No browser-facing file should contain all rows.

### Amendment C — add hard size gates

Suggested initial policy:

- target browser control file: 64 KB;
- mandatory shard at 128 KB;
- work-pack metadata: 100 KB maximum;
- maximum 8 sources per semantic wave;
- estimated token preflight before delegation;
- oversize packet returns `packet_oversize`, never delegates.

These are engineering defaults to validate, not claims about a hidden connector limit.

### Amendment D — make query/source waves the semantic unit

Use:

```text
topic
  → unresolved target query
    → Wave A canonical/direct sources
      → Wave B supporting sources only if still unresolved
        → Wave C historical/contextual only when required
```

Do not send the full topic candidate universe merely because it exists.

### Amendment E — separate completion states

Track independently:

- `knowledge_accepted`: target questions answerable and claims supported;
- `documentary_atlas_complete`: configured source-landscape review complete;
- `query_ready`: accepted knowledge plus fresh retrieval;
- `atlas_query_ready`: atlas complete plus atlas retrieval canaries.

A product profile may require both, but routine topic repair should not always pay the full atlas cost.

### Amendment F — prevent retrieval pollution

Index semantic atlas rows by role:

- material/supporting/contradicting rows in normal retrieval;
- incidental/irrelevant/unreviewed custody rows only for explicit source-landscape queries.

Otherwise the exhaustive atlas can reintroduce noisy retrieval results.

## Recommended final decision

Adopt the research architecture as the baseline, but do **not** implement it unchanged.

Approve these parts:

- canonical structure map;
- per-topic maps;
- hash-keyed capsules;
- generated atlasses;
- dependency/impact maintenance;
- Codex/browser bundle boundary;
- four distinct validation concerns.

Modify these parts before implementation:

- mandatory semantic row for every matched candidate;
- one large topic-analysis JSON;
- one-concept-plus-full-atlas browser batches;
- absence of numeric size/token gates;
- atlas completeness blocking ordinary knowledge acceptance;
- unfiltered indexing of irrelevant atlas rows.

## Bottom line

```text
The proposal fixes duplication and reuse.
It fixes the 9 MB combined-map shape.
It improves topic routing and Git delivery.

It does not yet guarantee small semantic tasks.
It still risks turning 120–154 matched files into one topic-wide review obligation.
```

With the six amendments above, it would solve the Leela problems while preserving the research design's lossless custody objective.
