# Architecture: Standalone Evidence-Ledger Pipeline

## Objective

Transform a long, noisy transcript into reliable Macro/Meso/Micro knowledge without making a brittle knowledge-base framework the prerequisite for success.

The design goal is not “maximum AI sophistication.” It is the smallest pipeline that makes semantic work bounded, inspectable, resumable, source-grounded, and cheap to retry.

## Runtime architecture

```text
transcript bytes
  |
  v
[deterministic source custody]
  parse -> SHA-256 -> stable seg IDs -> diagnostics
  |
  v
[deterministic processing-window planner]
  lexical cohesion + pause cue + size bounds
  no overlapping core; optional context halo
  |
  v
[semantic MAP: raw source read once]
  each bounded core window -> evidence card
    subtopics / key points / mechanisms / protocols
    arguments / entities / concepts / uncertainty
    candidate Micro claims + exact quotes
  |
  v
[deterministic evidence gate]
  packet freshness -> source refs -> exact quotes
  exact dedupe -> near-duplicate warnings -> coverage
  |
  v
[semantic REDUCE: compact evidence only]
  final Meso modules + Macro synthesis + refined Micro claims
  source-support judgment, no web truth yet
  |
  v
[deterministic verification router]
  factual + supported enough + check-worthy only
  |
  v
[optional semantic/web verification]
  document-level primary evidence where possible
  |
  v
[deterministic compiler]
  wiki index / Macro / modules / claims / concepts / entities
```

## Why this beats the main alternatives for this use case

### One-shot full transcript

Useful as a short-input shortcut, but not the reliability baseline. Long-context models can omit or underweight dispersed evidence, and a one-shot result gives weak local failure isolation. Exact quote/source validation also becomes harder when every semantic task is mixed into one enormous response.

### Flat fixed-size map-reduce prose summaries

More robust than one-shot, but a prose summary throws away too much structure before downstream claim extraction. If Micro claims are derived from summaries rather than source evidence, provenance degrades.

### Atomic-facts-first everywhere

Atomic decomposition is useful for factuality, but decomposing every utterance into atomic facts creates noise and cost. A conversation also contains arguments, questions, definitions, recommendations, decisions, anecdotes, mechanisms, and uncertainty that should not all become factual propositions. Extract candidate claims as one field of the Map evidence card, then refine only the valuable ones.

### Graph-first / GraphRAG / LightRAG / Graphiti

Powerful for multi-document retrieval and corpus question answering, but they add entity extraction, graph construction, embeddings, storage, and retrieval infrastructure before the transcript compiler has proved basic source-grounded output. Graph indexing can be added downstream after the Markdown/wiki artifacts work reliably.

### Recursive RAPTOR-style abstraction tree

Strong for retrieval across abstraction levels, but recursively summarizing a single transcript adds model calls and another derived layer. The evidence-ledger Map/Reduce gives the needed two levels without building a retrieval tree.

## Design rules that reduce failure surface

1. **Files are the workflow state.** No database is required to resume.
2. **Every semantic packet is content-bound.** A result echoes the packet SHA-256; stale results fail.
3. **Core coverage is exact and non-overlapping.** Every source segment is semantically owned by exactly one Map packet.
4. **Boundary context is read-only.** Neighbor segments can orient the model but cannot be cited as evidence in that packet.
5. **The raw transcript is semantically processed once by default.** Map extracts all reusable evidence classes together.
6. **Reduce reads validated evidence cards, not the whole transcript.** Reopen source only to resolve a specific gap or contradiction.
7. **Transcript support and world truth are separate axes.** A speaker can be accurately quoted and factually wrong.
8. **External verification is selective.** Route high/medium check-worthy factual claims; do not browse for every sentence.
9. **Compilation is deterministic.** Models do not author filesystem paths, slugs, stable claim IDs, or link graphs.
10. **Optional systems remain adapters.** Apex KB, Obsidian, vector indexes, and graph stores may consume compiled artifacts but do not own this pipeline.

## Processing-window algorithm

The CLI uses a TextTiling-inspired lexical-cohesion signal because it is cheap, deterministic, and dependency-free:

1. Tokenize each transcript segment.
2. Compute segment-level inverse-document-frequency weights.
3. At every segment gap, compare a bounded left/right block using cosine similarity.
4. Convert low similarity to lexical dissimilarity.
5. Add a small normalized pause score when timestamps provide a real inter-segment gap.
6. Within `min_words..max_words`, prefer a high boundary score near `target_words`.
7. Force a cut at the max size if no better boundary exists.
8. Add `context_segments` before/after as `context_only` while keeping core ownership non-overlapping.

This is intentionally a transport heuristic. It does not claim to discover final topic chapters.

## Optional enhancements, deliberately not required

- **Embedding/TreeSeg boundary mode:** useful if a local embedding model is already available and multilingual semantic segmentation materially improves results.
- **MiniCheck/local entailment:** useful as a second source-support validator when model installation cost is acceptable.
- **YAKE/RAKE candidate concepts:** useful as deterministic/statistical hints, but the semantic worker is already extracting concepts in the same Map pass, so defaulting them on would add complexity without clear value.
- **OpenVINO/faster-whisper/WhisperX:** optional upstream audio stage only. The core skill accepts transcripts and does not depend on ASR.
- **Graph/vector export:** downstream retrieval optimization only after the compiled wiki is accepted.

## Failure policy

Fail closed on structural/provenance violations; remain explicit rather than failing on semantic uncertainty.

**Hard failure examples:** stale packet, unknown segment ID, context-only citation, quote not found verbatim, invalid result schema, unsupported final claim under strict compile, decisive external verdict without evidence.

**Allowed uncertainty examples:** no timestamp, unknown speaker, ambiguous source support, no external evidence, unresolved contradiction, empty protocol list.
