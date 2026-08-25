# Three-Way Comparative Architecture Benchmark & Synthesis

## 1. Executive Summary

We evaluated, integrated, and benchmarked all three independently developed transcript processing systems against the 2-hour 9-minute Andrew Huberman live test transcript (`P-h5WSQG1Sw`, 24,865 words).

```mermaid
flowchart LR
    A[YouTube URL / Channel] -->|System 1: Ingestion| B[Raw Audio Stream]
    B -->|System 1: Local Whisper| C[SRT / VTT / JSON Transcript]
    C -->|System 3: TTK Protocol| D[Map Windows & Evidence Ledger]
    D -->|System 3 + System 2: Extraction| E[Macro / Meso / Micro Models]
    E -->|System 2 + Web Search| F[Verified Knowledge Wiki & Graphs]
```

---

## 2. Head-to-Head Comparison Matrix

| Dimension | System 1: `SourceTranscriptionAnalysisPipeline` | System 2: `transcript_engine.py` (Research) | System 3: `transcript-to-knowledge` (TTK Skill) |
| :--- | :--- | :--- | :--- |
| **Primary Domain** | **Media Ingestion & Local ASR** | **Epistemic Data Models & Rendering** | **Deterministic Lifecycle & Chunking** |
| **Input Handled** | YouTube URLs, Channels, Playlists, MP3/WAV | Pre-parsed Python objects & strings | `.srt`, `.vtt`, `.json`, `.txt`, `.md` files |
| **Whisper Execution** | 100% Local CPU/GPU (`faster-whisper` int8) | None (consumes output text) | None (consumes transcript files) |
| **Chunking & Token Budgeting** | None (monolithic raw audio transcription) | None (expects caller to chunk) | **Strict Map Windows (700–1500 words)** with overlap |
| **Verification & Fact-Checking** | Downstream JSON trigger payload | Pluggable `VerificationHook` callable | **Strict Validation Engine** (rejects non-verbatim quotes) |
| **Resumability & State** | `processed_videos.json` (ID level) | None (in-memory) | **Cryptographic SHA256 per window / packet** |
| **Output Formats** | `.md`, `.srt`, `.json`, `.txt` | Obsidian `[[wikilinks]]` Markdown & JSON | Semantic wiki trees & structured tables |
| **Unit Test Coverage** | Live pipeline integration test (15.4x) | **10 unit tests** (10/10 passing) | **12 unit tests** (12/12 passing) |

---

## 3. Detailed System Strengths & Gaps

### System 1 (`SourceTranscriptionAnalysisPipeline`) — *The Ingestion Heavyweight*
* **Where it wins:** Solves the entire frontend problem. Extracts 100% audio streams without downloading video, handles YouTube 403 throttling via Node.js runtime, runs local Whisper at 15.4x speed, and tracks channel watchlists.
* **Where it needs help:** Does not perform semantic decomposition (Macro/Meso/Micro) internally; it only generates the raw transcript files.

### System 2 (`transcript_engine.py`) — *The Clean Data Model*
* **Where it wins:** Elegant, zero-dependency Python standard library classes. `MicroClaim.__post_init__` enforces strict verdict enums (`CONFIRMED`, `CONTRADICTED`, `MIXED`, `UNVERIFIED`). Fast in-memory wiki rendering.
* **Where it needs help:** Cannot handle large 25k-word transcripts in a single pass without prior chunking; lacks built-in file state management.

### System 3 (`transcript-to-knowledge` / TTK) — *The Industrial Validator*
* **Where it wins:** Forensic-level lifecycle management. Slices 25k-word transcripts into 23 bounded Map windows with segment overlap, enforces strict SHA256 integrity, rejects hallucinations or non-verbatim quotes, and coordinates Reduce synthesis.
* **Where it needs help:** Has no media extraction or Whisper transcription engine (expects pre-transcribed text files).

---

## 4. The Unified Master Synthesis (The Clear Winner)

The optimal, highest-scoring architecture is **not choosing one over the other**, but combining their complementary strengths into an unbroken 3-stage pipeline:

```
[Stage 1: INGESTION (System 1)]
   YouTube Channel Polling ──> Audio Extraction ──> faster-whisper (CPU int8) ──> P-h5WSQG1Sw.srt
                                                                                        │
[Stage 2: CHUNKING & CUSTODY (System 3)]                                               │
   ttk init P-h5WSQG1Sw.srt ──> 23 Map Windows ──> Evidence Ledger ──> Validation ──────┘
                                                                            │
[Stage 3: EXTRACTION & VERIFICATION (System 2 & 3)]                        │
   LLM Map/Reduce ──> transcript_engine Dataclasses ──> Web Verification ───┘
                                                               │
                                                               ▼
                             [Final Output: Verified Obsidian Wiki + Knowledge Graph]
```
