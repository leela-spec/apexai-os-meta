# Transcript-to-Knowledge v2 — Meso Module Evaluation

This document evaluates each runtime module after the Macro architecture was fixed. Scores are project-fit engineering judgments, not external benchmark numbers.

## M0 — Optional ASR / alignment

| Option | Reliability | Simplicity | Local efficiency | Dependency risk | Decision |
|---|---:|---:|---:|---:|---|
| Pre-existing transcript | **95** | **100** | **100** | **5** | **Core default** |
| faster-whisper CPU/int8 | 90 | 80 | 75 | 30 | Recommended portable audio baseline |
| WhisperX | 92 | 55 | 70 | 60 | Optional precision/diarization |
| OpenVINO GenAI Whisper GPU | 85 | 60 | **90 potential** | 50 | Benchmark on Intel targets |
| OpenVINO NPU | 65 current | 50 | 90 potential | **75 current** | Do not default while current Lunar Lake issue remains open |
| whisper.cpp Vulkan | 75 | 55 | 80 potential | 60 | Experimental benchmark candidate |

**Decision:** the knowledge engine starts from transcript artifacts. Audio backends remain replaceable upstream adapters.

**Deterministic value:** audio chunking, file hashes, output normalization, timestamp/speaker diagnostics.

**Semantic/model value:** ASR itself, diarization/alignment models.

## M1 — Source custody / normalization

### Options

1. Pass raw SRT/VTT/JSON directly to the model.
2. Normalize into a database.
3. Normalize into a stable file ledger.

### Decision: file ledger

The CLI produces stable segment IDs and records the source hash. Missing timestamps/speakers are represented as missing, not guessed.

**Why not raw:** model prompts become format-dependent; evidence refs are fragile.

**Why not DB:** no transaction/concurrency requirement justifies a service or schema migration layer for a single-source compiler.

### Hard checks

- input format supported;
- source SHA-256;
- stable ordered segment IDs;
- timestamp monotonicity/overlaps/gaps;
- missing timing/speaker counts;
- repeated segment diagnostics;
- word-probability/low-confidence diagnostics when supplied.

## M2 — Processing-window planning

### Options

| Option | Cost | Boundary quality | Determinism | Dependency | Decision |
|---|---:|---:|---:|---:|---|
| Fixed token/word windows | **lowest** | 50 | **100** | none | fallback only |
| Lexical cohesion / TextTiling-inspired | low | 70 | **100** | none | **default** |
| Local embeddings / TreeSeg-like | medium | 82 | 90 | embedding model | optional mode later |
| LLM chaptering / PODTILE-like | high | 90 potential | 45 | semantic calls | final Meso stage, not transport chunker |

TextTiling demonstrates that vocabulary cohesion can detect subtopic changes without a domain model. Modern transcript chaptering shows semantic models can improve actual chapter labels/boundaries. The key architectural move is **not forcing one mechanism to do both jobs**.

**Default:** TF-IDF lexical left/right block dissimilarity + small pause signal + min/target/max word bounds.

**Important:** a processing window is not a knowledge chapter.

Primary TextTiling source: https://aclanthology.org/J97-1003/

## M3 — Semantic Map

### Options

1. Separate passes: one for summary, one claims, one entities, one protocols, one quotes.
2. One prose summary per chunk.
3. **One structured evidence-card pass per bounded window.**

### Decision: single structured pass

Output fields:

- subtopics;
- key points;
- mechanisms;
- protocols;
- arguments;
- candidate claims;
- entities;
- concepts;
- open questions;
- contradictions/uncertainty.

Each important item carries source segment IDs; claims additionally carry exact quote evidence and checkworthiness.

**Why:** the same source comprehension can populate all reusable evidence classes in one call/read. Separate raw passes multiply token cost and create inconsistent interpretations.

### Context halo

One neighboring segment by default can be present as `context_only`. The validator rejects any evidence that cites it. This avoids duplicate ownership while giving the model enough continuity around arbitrary processing cuts.

## M4 — Evidence validation and deduplication

### Options

| Approach | Hallucination guard | Deterministic | Model cost | Decision |
|---|---:|---:|---:|---|
| LLM self-review only | 55 | no | medium/high | reject as hard gate |
| Exact deterministic validation | **100 for structural/provenance invariants** | yes | zero | **required** |
| MiniCheck/local entailment | strong semantic support signal | model-deterministic-ish | local model | optional second guard |
| Large-LLM entailment pass | strong but expensive | no | high | exception only |

### Required deterministic gate

- packet/result schema;
- current packet hash;
- known source segment IDs;
- core ownership;
- literal quote substring in cited segment;
- vocabulary enums;
- exact duplicate merge only;
- near-duplicate warning, no silent equivalence;
- exact source core coverage.

MiniCheck is attractive as a later optional source-support checker: its EMNLP 2024 paper reports small models with GPT-4-level aggregate benchmark performance at far lower cost. It is not a core dependency because installing another model is unnecessary for hard source/quote invariants.

Primary source: https://aclanthology.org/2024.emnlp-main.499/

## M5 — Evidence ledger + Reduce

### Options

1. Reread full transcript for final synthesis.
2. Reduce prose chunk summaries.
3. **Reduce validated structured evidence cards.**

### Decision: evidence-ledger Reduce

The deterministic ledger exact-deduplicates repeated evidence, preserves source refs, and surfaces near-duplicate claim candidates. Reduce uses this compact ledger to produce the final semantic structure.

**Why this is important:** Meso boundaries must be free to merge/split processing windows. A final topic may span several windows; a single window may contain several final modules.

## M6 — Macro/Meso/Micro final semantic contract

### Macro

- thesis;
- compact summary;
- high-value global takeaways with source + Meso refs;
- taxonomy;
- speaker/context notes supported by source;
- contradictions/uncertainty.

### Meso

- semantic module title/summary;
- source refs;
- mechanisms;
- protocols;
- arguments;
- caveats;
- concepts/entities;
- Micro refs.

### Micro

- self-contained proposition;
- speech-act/claim kind;
- exact quote evidence;
- source support;
- external checkworthiness;
- topic/entity links;
- context needed to prevent misreading.

**Chain of Density:** use only as a final Macro editing heuristic if a summary is too sparse; do not run repeated CoD generations by default. Primary source: https://arxiv.org/abs/2309.04269

## M7 — Micro claim policy

### Rejected: atomize everything

FActScore/SAFE are valuable for **evaluating factual assertions**, but transcripts contain non-factual knowledge worth preserving: decisions, recommendations, definitions, estimates, predictions, anecdotes, mechanisms, hypotheses, opinions.

Recent decomposition research shows the decomposition step itself can introduce verification noise. FaStFACT explicitly integrates chunk-level extraction with pre-verification to cut calls/searches.

### Decision

- extract candidate claims during Map;
- classify claim kind immediately;
- Reduce keeps/refines only useful propositions;
- keep source-support judgment separate from world-truth judgment;
- external search only for factual claims that are worth it.

## M8 — External verification

### Options

1. Search every atomic claim.
2. Search a fixed number of URLs/snippets per claim.
3. **Route selectively by checkworthiness and gather enough document-level evidence to decide or explicitly remain unverified.**

### Decision: selective queue

Default threshold: `medium` + `high` factual claims only.

Do not send:
- opinions;
- recommendations;
- decisions;
- anecdotes;
- definitions unless explicitly checking the definition itself;
- predictions about the future;
- source-unsupported claims.

The verifier records evidence URLs, titles, publisher/date when known, stance, rationale, and verdict.

**Fail closed:** `CONFIRMED`, `CONTRADICTED`, or `MIXED` requires evidence. Otherwise use `UNVERIFIED`.

## M9 — Wiki/storage compiler

### Options

- graph DB as canonical store;
- vector DB as canonical store;
- Markdown authored directly by model;
- **structured semantic JSON -> deterministic Markdown compiler.**

### Decision: deterministic compiler

The model never chooses paths, slugs, stable claim IDs, or graph link syntax.

Generated tree:

```text
wiki/
  index.md
  compiled.json
  summaries/Macro.md
  modules/*.md
  claims/Claim-*.md
  concepts/*.md
  entities/*.md
```

Stable claim IDs are a hash of normalized proposition + speaker. Wikilinks are path-qualified.

Before rebuild, the compiler removes only compiler-owned `*.md` in its generated folders. This prevents stale pages after a semantic object disappears.

## M10 — Lifecycle / recovery

### Options

| State model | Inspectable | Resumable | Complexity | Decision |
|---|---:|---:|---:|---|
| chat memory | low | low | low | reject |
| workflow engine | medium | high | high | defer |
| SQLite state machine | high | high | medium | defer |
| **content-addressed filesystem** | **high** | **high** | **low** | **adopt** |

`status` derives progress from artifact validity. `next` identifies one exact packet/result pair. Packet hashes invalidate stale semantic outputs. The compiled manifest also records its upstream hashes; changed semantic or verification results trigger `compile_stale`.

## M11 — Downstream retrieval

**Default:** none. The compiled wiki is immediately usable and grep/search-friendly.

Possible adapters after acceptance:

- deterministic full-text/BM25/SQLite FTS;
- embeddings/vector search;
- GraphRAG/LightRAG/Graphiti;
- RAPTOR-like hierarchical retrieval;
- Apex KB import.

The criterion is a demonstrated retrieval/query need, not architectural fashion.
