# Transcript-to-Knowledge Engine — Research & Implementation Report

Date: 2026-08-18  
Target: `leela-spec/apexai-os-meta`  
Target branch: `main`

## Executive decision

Do **not** build a second knowledge-base lifecycle.

Apex KB already owns deterministic lifecycle state, source custody, semantic task packets, output validation, compiled wiki pages, and retrieval. The correct implementation is a thin transcript-preparation Skill that produces high-integrity source artifacts and bounded semantic work units, then hands them to the existing Apex KB semantic boundary.

The implementation therefore separates:

```text
DETERMINISTIC
transcript bytes
  -> parse
  -> source hash
  -> segment / word anchors
  -> speaker preservation
  -> bounded overlapping chunks
  -> semantic task plan

SEMANTIC
chunks
  -> Meso themes / mechanisms
  -> Micro atomic claims
  -> external verification when available
  -> Macro synthesis from validated Meso outputs
  -> Apex KB wiki import / retrieval
```

This is the smallest architecture that satisfies the mission without falsely claiming that summarization, thematic interpretation, claim identification, or live web fact-checking are deterministic.

## Existing Apex fit

Current Apex KB already declares the Python application as the sole lifecycle authority and its Skill as a thin launcher. The current CLI package also already contains extractors, semantic task handling, templates, schemas, and retrieval. This implementation therefore does not modify Apex KB lifecycle state or create another compiler.

New capability:

```text
.claude/skills/transcript-to-knowledge/
  SKILL.md
  agents/openai.yaml
  scripts/
    prepare_transcript.py
    prepare-transcript.ps1
    test_prepare_transcript.py
  references/
    knowledge-contract.md
    prompt-templates.md
    evals.md
```

## Research method

Primary-source inspection covered:
- GitHub repository source/readmes and current commit history;
- Hugging Face model/dataset cards;
- primary papers for RAPTOR and Chain-of-Density;
- CTranslate2 official installation/performance documentation.

Scoring formula:

```text
Composite = 0.45 * Impact + 0.35 * Evidence + 0.20 * (100 - Risk)
```

Where:
- **Impact** = direct usefulness for this mission;
- **Evidence** = maturity and quality of primary benchmark/source support;
- **Risk** = dependency, portability, token-cost, integration, and failure-surface risk.

## Upstream benchmark

| Candidate | Inspected revision / source | Mission fit | I/E/R : Composite | Decision |
|---|---|---|---:|---|
| `SYSTRAN/faster-whisper` | `ed9a06cd89a93e47838f564998a6c09b655d7f43` + official README/CTranslate2 docs | Efficient local ASR, VAD, word timestamps, quantization | **94/96/20 : 91.9** | **Adopt as recommended upstream ASR**, but do not make it a core dependency of the transcript-to-knowledge Skill. |
| `m-bain/whisperX` | `2cfd7b7c5c7bba144954364db747319b50e8232b` + README | Forced alignment, word timestamps, diarization, VAD | **91/93/32 : 87.1** | **Adopt as optional precision/diarization stage** when exact alignment or multi-speaker labeling matters. |
| `danielmiessler/Fabric` | `338b89cfe97ab2d12ce30ce8b5449857a841366d`, `extract_wisdom_with_attribution` | Modular extraction patterns, exact quotes, attributed facts/ideas | **80/84/24 : 80.6** | **Borrow pattern modularity and explicit output contracts**; reject arbitrary minimum item counts and fixed 16-word constraints for forensic KB work. |
| `parthsarthi03/raptor` | `7da1d48a7e1d7dec61a63c9d9aae84e2dfaa5767` + ICLR 2024 paper | Hierarchical multi-level abstraction/retrieval | **72/92/55 : 73.6** | **Borrow the hierarchy principle only**. Apex KB already owns retrieval; recursive LLM tree construction would duplicate architecture and add semantic/API cost. |
| Chain-of-Density | NewSum 2023 paper + `griffin/chain_of_density` dataset | Macro summary density/readability refinement | **66/86/48 : 70.2** | **Use as a QA/revision heuristic**, not a default multi-pass summarizer, because repeated passes multiply token cost. |

### Primary evidence notes

**faster-whisper**
- Uses CTranslate2; its project reports up to 4x faster inference than OpenAI Whisper at comparable accuracy with lower memory in its published benchmark configuration.
- Supports word timestamps and integrated Silero VAD, including configurable silence thresholds.
- CTranslate2 recommends `int8` on CPU.
- CTranslate2's prebuilt Windows/Linux GPU execution is CUDA-based, so Intel-only Windows systems should not assume their integrated/discrete Intel GPU will accelerate faster-whisper via the normal CTranslate2 wheel.

**WhisperX**
- Adds forced alignment through phoneme-level models and supports speaker diarization.
- Uses faster-whisper as backend in current versions.
- Project documentation reports large speedups under its benchmark setup; these numbers are hardware/model/batch dependent and should not be treated as a universal local benchmark.
- Diarization introduces extra model/access requirements, so it stays optional.

**Fabric**
- `extract_wisdom_with_attribution` demonstrates useful separation of summary, ideas, exact quotes, facts, and references.
- Its fixed output-count and fixed-word-count constraints are optimized for a specific wisdom-extraction use case, not exhaustive factual provenance. The implementation adopts modularity and exact-quote discipline, not those quotas.

**RAPTOR**
- The research result strongly supports multi-level abstraction for long-document retrieval.
- Apex already has a compiled KB/retrieval lifecycle. Re-implementing RAPTOR as another retrieval tree would create two retrieval authorities and more LLM summarization work.
- The implementation instead uses deterministic bounded chunks, Meso map outputs, and Macro reduce from Meso outputs.

**Chain-of-Density**
- The paper establishes a useful density/readability tradeoff and releases evaluation data on Hugging Face.
- The implementation uses this only as a final Macro editing heuristic; it does not require repeated generations.

## GitHub / Hugging Face / CLI scan

Verified ecosystem surfaces include:
- `SYSTRAN/faster-whisper` plus `Systran/faster-whisper-large-v3` and related CTranslate2 model conversions on Hugging Face;
- `m-bain/whisperX` and its CLI / alignment pipeline;
- `pyannote/speaker-diarization-community-1` on Hugging Face for optional diarization;
- `danielmiessler/Fabric` CLI patterns;
- `parthsarthi03/raptor` official implementation;
- `griffin/chain_of_density` dataset.

## KR1 — clone/benchmark status

**Source-level benchmark: complete. Literal local clone: blocked in this execution environment.**

The connected GitHub app can inspect public repositories and current commits, but the code-execution container has no outbound GitHub DNS and does not have `gh`. Therefore this run cannot honestly claim that the upstream repositories were cloned and executed locally.

To make the missing step reproducible, `clone-upstreams.ps1` is included beside this report and pins the inspected revisions. A normal network-enabled Windows environment can run it without changing the architecture decision.

This limitation does **not** block the new Skill's implementation or tests because the Skill has no runtime dependency on those repositories.

## KR2 — deterministic 3-tier parsing implementation

Implemented boundary:

| Layer | Deterministic code owns | Semantic worker owns |
|---|---|---|
| Source | parse JSON/SRT/VTT/text; SHA-256; preserve speaker/timing/words | none |
| Chunking | bounded word windows; overlap; stable segment IDs | decide actual thematic chapter boundaries |
| Macro | task ordering and input references | thesis, takeaways, taxonomy, speaker/context synthesis |
| Meso | chunk transport boundaries | themes, mechanisms, protocols, caveats |
| Micro | exact anchor/quote source surface | identify atomic propositions; classify speaker posture; verification judgment |
| Verification | allowed verdict vocabulary and evidence contract | live search, source evaluation, confirmed/contradicted/mixed judgment |

This is intentionally **deterministic orchestration + source grounding**, not deterministic semantic interpretation.

## KR3 — wiki artifact contract

Implemented templates require:
- `[[Topic]]`, `[[Entity]]`, and `[[Claim-<id>]]` links;
- stable `seg-XXXXXX` transcript anchors;
- exact quotes at Micro level;
- contradictions/uncertainty preserved;
- `[CONFIRMED]`, `[CONTRADICTED]`, `[MIXED]`, `[UNVERIFIED]`, `[OPINION]` statuses;
- compiled notes kept separate from normalized raw transcript evidence.

## KR4 — self-contained CLI / PowerShell package

Implemented with Python standard library only:

```powershell
.\.claude\skills\transcript-to-knowledge\scripts\prepare-transcript.ps1 `
  -InputPath .\input\episode.json `
  -OutputPath .\artifacts\episode
```

Equivalent direct CLI:

```powershell
python .\.claude\skills\transcript-to-knowledge\scripts\prepare_transcript.py prepare `
  .\input\episode.json `
  --output .\artifacts\episode `
  --chunk-words 1200 `
  --overlap-words 120
```

Supported inputs:
- Whisper/faster-whisper/WhisperX JSON;
- SRT;
- WebVTT;
- plain `.txt`/Markdown (including bracket timestamps).

Generated artifacts:
- `manifest.json`
- `transcript.json`
- `transcript.md`
- `chunk-index.json`
- `task-plan.json`
- `chunks/chunk-XXXX.md`

## Validation

Unit tests:

```text
6 tests passed
- WhisperX word timestamp + speaker preservation
- SRT cue anchoring
- untimed text never fabricates timestamps
- bounded overlap / anchor preservation
- byte-deterministic repeated preparation
- invalid overlap rejection
```

Synthetic scale test:

```text
input:       1,600 timestamped segments
words:       24,000
chunking:    1,200 target words / 120 overlap words
chunks:      23
elapsed:     0.61 s in the execution container
max RSS:     ~116 MB in the execution container
```

The synthetic timing is a sanity benchmark for the deterministic preparer only; it is not an ASR benchmark and not a prediction of any user's hardware.

## Rejected architectures

### 1. Monolithic transcript summarizer

Rejected because it loses quote-level provenance and scales poorly with long transcripts.

### 2. New RAPTOR/vector retrieval subsystem

Rejected because Apex KB already owns retrieval and compiled knowledge. Would duplicate authority and maintenance.

### 3. Fully deterministic Macro/Meso/Micro semantics

Rejected as a false claim. Theme discovery, thesis synthesis, atomic claim identification, and web fact-checking require semantic judgment and live evidence.

### 4. Always-on WhisperX diarization

Rejected as default because it adds model/access complexity when many transcripts already contain adequate speaker labels.

### 5. Repeated CoD generations

Rejected as default because it conflicts with the mission's token-efficiency goal. Density is retained as a single final QA heuristic.

## Final architecture

```text
optional local audio stage
  faster-whisper (CPU int8 portable default)
  -> optional WhisperX alignment/diarization

raw transcript artifact
  -> transcript-to-knowledge deterministic preparer
       source SHA
       exact segment/word timing
       stable anchors
       bounded chunks
       task plan
  -> Apex KB semantic boundary
       Meso map
       Micro claims + verification hooks
       Macro reduce from Meso
  -> Apex KB compiled wiki / retrieval
```

## Remaining non-blocking work

1. Run `clone-upstreams.ps1` in a network-enabled Windows environment if literal KR1 clone evidence is required.
2. Run one real transcript through the full Apex KB semantic lifecycle and compare output quality against the evaluation scenarios.
3. Only if real evidence shows weak chapter coherence, test a stronger semantic chunk-merging strategy; do not add vector/tree infrastructure preemptively.
