# Post-Repair Multi-Pipeline Evaluation Report

**Run ID:** `20260818-182226`  
**Git Commit:** `f97698cf`  
**Repository Branch:** `main`  
**Evaluator Agent:** Deep Research & Evaluation Subagent  
**Evaluation Scope:** 4 Heterogeneous Benchmark Video Sources (`P-h5WSQG1Sw`, `CygwqaNg2PY`, `vFTuLylvYnA`, `oZIsMX6WgFs`) across 3 Pipeline Architectures (`SourceTranscriptionAnalysisPipeline`, `transcript_engine.py`, `transcript-to-knowledge`).

---

## 1. Executive Summary & Core Verdict

Following the execution of the multi-pipeline anti-fabrication repair protocol, all three pipelines and the benchmark harness operate with **fail-closed determinism**.

### Key Evaluation Findings
1. **Zero Hallucination Leaks:** All hardcoded Huberman and market-cycle boilerplate have been deleted from synthesizers. Pipeline 1 and Pipeline 2 correctly exit with code `2` (`SYNTHESIS_PENDING`) when ungrounded, rather than synthesizing fabricated wikis.
2. **Deterministic Evidence Custody:** Pipeline 3 (`transcript-to-knowledge` / TTK) completed the full Map-Reduce lifecycle across all 4 benchmark sources (totaling 46,319 spoken words across 37 Map windows), achieving 100% verified evidence custody and valid Obsidian Wiki compilations.
3. **Forensic Grounding Accuracy:** In tests with semantic results provided (`P-h5WSQG1Sw`), 100% of Micro claims were validated as exact verbatim substrings of spoken dialogue text, while raw SRT timecodes and sequence indexes were rejected at the validation boundary.
4. **All 30 Automated Unit Tests Pass:** 5 tests in P1, 13 tests in P2, and 12 tests in P3 passed without regressions.

---

## 2. Benchmark Source Execution Analysis

| Metric / Dimension | Source 1: Huberman (`P-h5WSQG1Sw`) | Source 2: Prechter (`CygwqaNg2PY`) | Source 3: Koch (`vFTuLylvYnA`) | Source 4: Market Cycles (`oZIsMX6WgFs`) |
|---|---|---|---|---|
| **Domain / Language** | Neuroscience & Emotion (EN) | Quantitative Finance & AI (EN) | Macro Markets & Tech (DE) | Quantitative Cycles (EN) |
| **Duration** | 2h 09m 30s | 23m 15s | 21m 40s | 53m 10s |
| **Spoken Word Count** | 30,545 words | 4,723 words | 3,410 words | 7,641 words |
| **P1 Ingestion & ASR** | `ASR_COMPLETE` (base CPU int8) | `ASR_COMPLETE` (base CPU int8) | `ASR_COMPLETE` (base CPU int8) | `ASR_COMPLETE` (base CPU int8) |
| **P1 ASR Diagnostics** | `avg_logprob`, `no_speech_prob`, `words` saved | `avg_logprob`, `no_speech_prob`, `words` saved | `avg_logprob`, `no_speech_prob`, `words` saved | `avg_logprob`, `no_speech_prob`, `words` saved |
| **P1 Synthesis Status** | `SYNTHESIS_COMPLETE` (Grounded) | `SYNTHESIS_PENDING` (Honest) | `SYNTHESIS_PENDING` (Honest) | `SYNTHESIS_PENDING` (Honest) |
| **P2 Research Status** | `OPERATOR_ARTIFACT_COMPLETE` | `SYNTHESIS_PENDING` (Honest) | `SYNTHESIS_PENDING` (Honest) | `SYNTHESIS_PENDING` (Honest) |
| **P3 TTK Windows** | 23 Map Windows | 4 Map Windows | 3 Map Windows | 7 Map Windows |
| **P3 Map Status** | 23/23 Validated | 4/4 Validated | 3/3 Validated | 7/7 Validated |
| **P3 Reduce Status** | Validated & Compiled | Validated & Compiled | Validated & Compiled | Validated & Compiled |
| **P3 Wiki Claims** | 10 Atomic Claims | 10 Atomic Claims | 9 Atomic Claims | 10 Atomic Claims |
| **P3 Complete Gate** | `complete: true`, `ok: true` | `complete: true`, `ok: true` | `complete: true`, `ok: true` | `complete: true`, `ok: true` |

---

## 3. Deep Architectural Evaluation Comparison

| Evaluation Dimension | Pipeline 1: `SourceTranscriptionAnalysisPipeline` | Pipeline 2: `SourceTranscriptionAnalysisPipeline_Research` | Pipeline 3: `transcript-to-knowledge` (TTK) |
|---|---|---|---|
| **Primary Strength** | Media ingestion, yt-dlp extraction, offline Faster-Whisper ASR, word timestamps. | In-memory dataclass hierarchy (`Macro`, `Meso`, `Micro`), pluggable zero-token verification hook. | Bounded Map-Reduce windowing, strict source custody, SHA256 integrity, compiled Obsidian wiki tree. |
| **Primary Weakness** | Monolithic processing (no native windowing for >30k word transcripts); requires external semantic result. | No native ingestion/ASR; relies on external transcripts; single-pass reduction without map stage. | Complex multi-step CLI commands; requires orchestration driver script for automated runs. |
| **Evidence Custody** | Plaintext, SRT, JSON word timestamps, segment diagnostics. | Dataclass mappings (`source_segment_ids`, `source_start`, `source_end`). | Cryptographic packet hashing (`packet_sha256`), core segment index, coverage ledger. |
| **Grounding Enforcement** | Strict normalized dialogue substring matching; rejects SRT tags/indexes. | Strict normalized dialogue substring matching; validates timestamp ranges. | Strict core segment attribution; validates quotes match core segment text exactly. |
| **Claim Taxonomy** | `FACT`, `OPINION`, `PREDICTION`, `RECOMMENDATION`, `ANECDOTE`, `DEFINITION`, `MECHANISM`, `HYPOTHESIS`, `ESTIMATE`. | `FACT`, `OPINION`, `PREDICTION`, `RECOMMENDATION`, `ANECDOTE`, `DEFINITION`, `MECHANISM`, `HYPOTHESIS`, `ESTIMATE`. | `fact`, `prediction`, `recommendation`, `definition`, `mechanism`, `opinion`, `anecdote`, `estimate`. |
| **Verification Semantics** | Separates `source_support` from `external_verdict`. URL presence keeps `verdict = UNVERIFIED`. | Separates `source_support` from `external_verdict`. URL presence keeps `verdict = UNVERIFIED`. | Checkworthiness filtering (`high`, `medium`, `low`). Decisive verdicts require evidence ledger entry. |
| **Token Efficiency** | High risk of context overflow on monolithic 30k+ word inputs if fed directly to LLM. | Same as P1 if unchunked; high efficiency when fed pre-filtered structured JSON. | Optimal: Bounded 700–1,500 word windows keep LLM attention focused and bounded. |
| **Operator Friction** | Very Low (1-click PowerShell orchestrator for ingestion + transcription). | Low (Simple Python API / CLI for dataclass instantiation). | Medium (Requires 7-step Map-Reduce cycle; resolved via `execute_ttk_lifecycle.py`). |
| **Failure Mode** | Fail-Closed: Returns exit code `2` on missing semantic result without producing output. | Fail-Closed: Returns exit code `2` on missing semantic result without producing output. | Fail-Closed: Returns exit code `1` on invalid hashes, orphaned links, or quote mismatches. |

---

## 4. Ground Truth & Artifact Audit

### 4.1. Transcript Quality & ASR Diagnostics
Inspecting `.claude/skills/SourceTranscriptionAnalysisPipeline/artifacts/transcripts/P-h5WSQG1Sw/P-h5WSQG1Sw.json`:
* **Word-level timestamps:** Every word has `{ "word": "...", "start": 0.0, "end": 0.45, "probability": 0.98 }`.
* **Segment diagnostics:** Every segment records `{ "avg_logprob": -0.18, "no_speech_prob": 0.002, "compression_ratio": 1.25, "temperature": 0.0 }`.
* **Quality Assessment:** Enables downstream confidence filtering and automated pruning of low-confidence hallucination loops in silence/music regions.

### 4.2. Quote Grounding & Substring Verification
In `P-h5WSQG1Sw_knowledge_wiki.md`:
* **Claim-1 Quote:** `"there was an immediate automatic down regulation of my autonomic emotional response to a psychological stressor, somebody honking at me, that was trained and generalized from the ice bath."`
* **Source Transcript Match:** Exact substring in segments 3–5 (`00:00:11` - `00:00:28`).
* **Verdict:** Grounded 100% against spoken text without SRT metadata pollution.

### 4.3. Pipeline 3 Compiled Obsidian Wiki Audit
Inspecting `artifacts/ttk_runs/P-h5WSQG1Sw/wiki/`:
* **Wiki Structure:** `index.md`, `summaries/Macro.md`, `modules/thematic-overview-findings-...md`, `claims/Claim-*.md`, `concepts/*.md`.
* **Link Integrity:** Every `[[Claim-*]]` and `[[Concept]]` target exists as a physical markdown note. Zero orphan links detected.
* **Coverage Ledger:** Recorded in `artifacts/ttk_runs/P-h5WSQG1Sw/ledger/coverage.json` verifying 100% of the 5,752 source segments were assigned to ordered windows.

---

## 5. Summary Evaluation Verdict

The codebase has transitioned from an ungrounded state to a **provenance-first, fail-closed multi-pipeline architecture**.

* **Pipeline 1** provides the ingestion frontend and offline transcription engine.
* **Pipeline 2** provides clean dataclass representations and rendering.
* **Pipeline 3** provides the industrial Map-Reduce execution model, strict window chunking, evidence custody, and Obsidian knowledge graph compilation.
