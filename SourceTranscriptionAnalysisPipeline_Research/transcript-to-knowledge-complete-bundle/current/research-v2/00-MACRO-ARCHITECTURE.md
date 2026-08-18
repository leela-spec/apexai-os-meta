# Transcript-to-Knowledge v2 — Macro Architecture Decision

Date: 2026-08-18  
Repository target: `leela-spec/apexai-os-meta`  
Status: **v2 supersedes the Apex-KB-dependent v1 architecture**

## 1. Objective

Build a transcript-to-knowledge pipeline that works even if every downstream KB framework is absent or broken.

The acceptance target is not “a sophisticated knowledge platform.” It is:

1. accept a real transcript;
2. preserve source custody and exact evidence anchors;
3. bound semantic work so failures are local and resumable;
4. extract Macro/Meso/Micro knowledge without rereading raw source unnecessarily;
5. distinguish transcript support from external factual truth;
6. selectively verify claims that are worth the cost;
7. deterministically compile inspectable Markdown/wiki artifacts;
8. recover from interruption or changed inputs without trusting chat memory;
9. require no graph DB, vector DB, workflow engine, Apex KB, or hosted LLM SDK for the happy path.

The runtime uses a capable reasoning model/agent for semantic work, but the control plane never calls an LLM or the network. That permits the semantic worker to be the current subscription AI session rather than an API integration.

## 2. Macro problem decomposition

```text
SOURCE
  raw transcript / caption file
       |
       v
M0 source custody + diagnostics
       |
       v
M1 processing-window planning
       |
       v
M2 semantic MAP (bounded raw-source pass)
       |
       v
M3 deterministic evidence gate / ledger
       |
       v
M4 semantic REDUCE
       |             \
       |              -> Macro thesis/taxonomy/takeaways
       |              -> Meso semantic modules
       |              -> Micro source-grounded claims
       v
M5 selective external verification
       |
       v
M6 deterministic Markdown/wiki compiler
       |
       v
OPTIONAL ADAPTERS
  Obsidian / search index / vector index / graph / Apex KB / other consumers
```

**Design/research order** is Macro -> Meso -> Micro. **Runtime semantic order** is Map -> Reduce because the system must gather source evidence before it can responsibly synthesize final global structure.

## 3. Architecture classes evaluated

Scores are **project-fit engineering assessments**, not published benchmark results. Each dimension is 0–100.

Weights:

- reliability/provenance: 30%
- token/compute efficiency: 20%
- operational simplicity: 15%
- resumability/recovery: 15%
- deterministic leverage: 10%
- evidence/ecosystem maturity: 10%

| Architecture | Reliability | Efficiency | Simplicity | Recovery | Deterministic leverage | Evidence maturity | Weighted fit | Decision |
|---|---:|---:|---:|---:|---:|---:|---:|---|
| One-shot full-context summary | 55 | 70 | **95** | 35 | 25 | 75 | **60.0** | Shortcut for short inputs only |
| Hierarchical prose map-reduce | 75 | 65 | 70 | 80 | 45 | 85 | **71.0** | Good baseline, but prose intermediates discard too much evidence structure |
| Atomic-facts-first | 82 | 35 | 55 | 75 | 55 | 90 | **65.6** | Useful factuality technique, rejected as the universal representation |
| Graph-first / GraphRAG-style | 88 | 25 | 30 | 80 | 35 | 90 | **60.4** | Optional downstream retrieval/indexing only |
| **Evidence-ledger hybrid** | **94** | **85** | 82 | **95** | **90** | **90** | **89.8** | **Adopt** |

### 3.1 One-shot full context

**What works:** minimal orchestration and modern models can accept very large contexts.

**Why it is not the reliability baseline:** long context capacity is not equivalent to reliable context utilization. “Lost in the Middle” demonstrated strong position sensitivity in long-context retrieval tasks. A one-shot transcript prompt also combines segmentation, extraction, synthesis, claim generation, and quote provenance into one enormous failure domain.

**Use:** if the normalized transcript is small enough and the operator explicitly wants a quick summary rather than forensic KB output.

Primary evidence: https://arxiv.org/abs/2307.03172

### 3.2 Hierarchical prose map-reduce

**What works:** bounded chunks localize failures; map-reduce is a proven long-document pattern.

**Failure mode:** a prose chunk summary is lossy. If final Micro claims are extracted from prose summaries, exact source evidence and non-summary content can disappear before the claim stage.

**Borrow:** hierarchical execution and bounded retries.

**Change:** Map produces a structured **evidence card**, not only prose.

### 3.3 Atomic-facts-first

FActScore and SAFE show why atomic facts are useful for fine-grained factuality. But newer evidence is a warning against making decomposition the first and universal operation: decomposition itself can introduce noise, and FaStFACT reduces work by extracting claims at chunk level and pre-filtering which ones deserve expensive verification.

**Borrow:** self-contained candidate claims, source evidence, selective verification.

**Reject:** atomize every sentence, then search every atom.

Primary evidence:
- https://arxiv.org/abs/2305.14251
- https://arxiv.org/abs/2403.18802
- https://arxiv.org/abs/2510.12839
- https://aclanthology.org/2025.naacl-long.320/

### 3.4 Graph-first / GraphRAG

Microsoft GraphRAG performs LLM entity/relationship extraction, graph/community construction, community reports and embeddings. Its current documentation states that graph extraction is roughly 75% of indexing cost in the standard method; claim extraction is optional/off by default because it needs task-specific prompt tuning.

This is appropriate when the central problem is **retrieval across a corpus**. It is overpowered for proving that one transcript can be turned into source-grounded knowledge reliably.

**Borrow:** bounded TextUnits, fine-grained source references, cached structured intermediates, multi-level synthesis.

**Reject for core:** graph database, relationship extraction, community detection, vector storage.

Primary evidence:
- https://microsoft.github.io/graphrag/index/overview/
- https://microsoft.github.io/graphrag/index/methods/
- https://microsoft.github.io/graphrag/config/yaml/

### 3.5 RAPTOR / recursive abstraction

RAPTOR recursively embeds, clusters, and summarizes chunks into a retrieval tree. This is valuable for query-time retrieval across abstraction levels, but a single-transcript compiler does not need recursive clustering before basic output correctness is proven.

**Borrow:** final synthesis should consume compact lower-level representations rather than rereading all source.

**Reject for core:** recursively generated tree and its extra model calls.

Primary evidence: https://arxiv.org/abs/2401.18059

### 3.6 Evidence-ledger hybrid — selected

The selected architecture combines the robust parts without inheriting their infrastructure:

- deterministic source custody;
- bounded processing units;
- one semantic raw-source Map pass per core segment;
- structured evidence cards carrying claims, mechanisms, protocols, arguments, entities, concepts and uncertainty;
- exact deterministic quote/source validation;
- deterministic evidence ledger + dedup candidates;
- one compact semantic Reduce for final Macro/Meso/Micro;
- selective external factual verification;
- deterministic Markdown/wiki compilation;
- files + content hashes as resumable state.

## 4. Core invariants

1. **A source segment has exactly one Map owner.** Context halos can be read but never cited by the neighboring Map packet.
2. **Semantic results are content-bound.** Every result echoes the exact packet SHA-256.
3. **Hard provenance is code-validated.** Segment refs, quotes, packet hashes and link targets are not trusted to an LLM.
4. **Raw transcript is semantically read once by default.** Themes, claims, quotes, entities, protocols and uncertainty are captured together in Map.
5. **Reduce uses the validated ledger.** Reopen source only for an explicit gap/correction, not as the normal path.
6. **Processing windows are not chapters.** Cheap lexical/pause segmentation is transport; final Meso structure is semantic.
7. **Transcript support != world truth.** `SUPPORTED` can coexist with external `CONTRADICTED`.
8. **Verification is selective.** Only check-worthy factual claims enter the external queue.
9. **Files are workflow state.** `status`/`next` derive progress from artifacts, not conversation memory.
10. **Compiled outputs are content-bound.** Changed Reduce/verification results make the wiki `compile_stale` until rebuilt.
11. **No silent semantic equivalence.** Exact duplicate claims may merge mechanically; near duplicates are warnings for semantic review.
12. **Optional systems are adapters.** Core correctness never depends on Apex KB, vector search, graph storage, or a proprietary API.

## 5. Token-efficiency model

The expensive resource is semantic context, not deterministic file processing.

### Default semantic reads

- Map: each core source segment appears in exactly one semantic packet.
- Context halo: small repeated neighbor context only; it cannot become evidence from the wrong packet.
- Reduce: reads structured validated evidence, not the full transcript.
- Verification: reads only routed facts, then external sources needed for those facts.

This is deliberately different from multi-pass pipelines that separately reread raw text for topics, entities, claims, quotes, and summaries.

## 6. Storage decision

**Chosen:** plain JSON + Markdown files with deterministic hashes.

**Why:** inspectable, diffable, recoverable, portable, zero service dependency, easy to test, easy to delete/rebuild derived output.

**Not chosen:** SQLite/workflow engine for v2. A database becomes justified only if concurrent workers, very large multi-source corpora, transactional cross-run querying, or scheduling prove that files are insufficient.

## 7. Optional audio stage

Audio transcription is upstream, not part of core correctness.

Candidates:

- faster-whisper CPU/int8: mature portable baseline;
- WhisperX: optional forced alignment/diarization when exact speaker/word timing is worth the dependencies;
- OpenVINO GenAI Whisper: attractive for Intel CPU/GPU/NPU and supports word timestamps;
- whisper.cpp/Vulkan: attractive in principle for broad local hardware but Windows/Vulkan packaging/issue state should be benchmarked rather than assumed.

Current OpenVINO evidence also shows why v2 must not hardwire one backend: a July 2026 Lunar Lake NPU Whisper issue is open, and a March 2026 long-audio issue reports extreme memory growth unless audio is chunked before `WhisperPipeline`.

Primary evidence:
- https://docs.openvino.ai/2026/api/genai_api/_autosummary/openvino_genai.WhisperPipeline.html
- https://github.com/openvinotoolkit/openvino.genai/issues/4222
- https://github.com/openvinotoolkit/openvino.genai/issues/3501

**Decision:** accept transcripts as the stable core input. If audio is added, benchmark OpenVINO GPU against faster-whisper CPU/int8 on the target machine and manually chunk long audio until upstream behavior proves otherwise.

## 8. Rejected overengineering

Do not add any of these until a measured requirement appears:

- graph DB;
- vector DB;
- embeddings solely for chunking;
- workflow engine;
- agent framework inside the CLI;
- hosted LLM SDK;
- all-claim web search;
- repeated Chain-of-Density passes;
- recursive RAPTOR trees;
- an Apex KB lifecycle dependency.

## 9. Exit criterion for Macro phase

Macro architecture is accepted only if every Meso module can be independently tested and replaced without changing the source custody contract. v2 satisfies that condition: segmentation, semantic Map, ledger, Reduce, verification, compiler, and optional ASR are separable modules connected by files with explicit schemas/hashes.
