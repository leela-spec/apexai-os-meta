# Advanced Research & Technical Blueprint: Hybrid Transcript Knowledge Unification

**Authors:** AI Research & Engineering Pair  
**Status:** PROPOSED ARCHITECTURAL BLUEPRINT  
**Target System:** Unified Autonomous Audio-to-Knowledge Pipeline (`apex-transcribe-v2`)  
**Scope:** Resilience, Simplicity, Value Delivery, Token Efficiency, and Unification Roadmap.

---

## 1. Executive Summary & Objective

Having established fail-closed grounding, eliminated domain-specific hardcoding, and verified full Map-Reduce lifecycle execution across 4 heterogeneous benchmarks, the next imperative is **unifying the best components of all three pipelines into a single cohesive, high-performance architecture**.

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                CURRENT THREE-PIPELINE STATE                                      │
├────────────────────────────────┬────────────────────────────────┬────────────────────────────────┤
│ Pipeline 1: Frontend Ingestion │ Pipeline 2: Research Dataclass │ Pipeline 3: TTK Protocol       │
│ • yt-dlp + ffmpeg audio-only   │ • Typed Macro-Meso-Micro schema│ • Cryptographic SHA256 ledger  │
│ • Faster-Whisper CPU int8 ASR  │ • Clean Python dataclasses     │ • Bounded Map-Reduce windows   │
│ • Word timestamps & metrics    │ • Lightweight renderers        │ • Compiled Obsidian Wiki Graph │
└────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘
                                                │
                                                ▼
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                         UNIFIED HYBRID TARGET ARCHITECTURE                                       │
│                                                                                                  │
│   [Media Ingestion]  ──►  [Offline Whisper ASR]  ──►  [Semantic Windowing]  ──►  [Map-Reduce]    │
│   (yt-dlp + ffmpeg)       (int8 + Diagnostics)        (Pause/Speaker Bounded)     (Evidence Core)│
│                                                                                         │        │
│   [Obsidian PKM Vault] ◄── [Agent Handoff Event] ◄── [Deterministic Gate]  ◄────────────┘        │
│   (Graph + Wikilinks)      (pending_ai_task)         (Verbatim Grounding)                        │
└──────────────────────────────────────────────────────────────────────────────────────────────────┘
```

---

## 2. Deep Research on the Four Core Dimensions

### 2.1. Resilience: Fault Tolerance, Acoustic Integrity & Error Containment

#### A. Whisper Hallucination Pruning & Silence Filtering
Whisper models frequently suffer from acoustic hallucination loops (repeating phrases like "Thank you for watching" or subtitle author credits) during silent intervals or background music.
* **Research-Backed Solution:** Use Faster-Whisper segment diagnostics already captured in P1:
  1. `no_speech_prob > 0.60`: Drop segment immediately as non-speech.
  2. `avg_logprob < -1.00`: Flag segment as low-confidence; do not route as core evidence.
  3. `compression_ratio > 2.40`: Detect repetitive text hallucination loops and truncate.
  4. `temperature > 0.40`: Indicates the decoder had to fall back due to low confidence; flag for manual review.

#### B. Context Boundary Preservation (Dynamic Semantic Slicing)
Naive fixed-character or fixed-duration chunking slices sentences in half, causing context truncation and quote grounding failures at boundaries.
* **Research-Backed Solution:** Implement **Pause-Weighted Speaker Turn Slicing**:
  * Identify natural boundaries using a composite cost function:
    $$\text{Cost} = w_{\text{pause}} \cdot \Delta t_{\text{silence}} + w_{\text{speaker}} \cdot \mathbb{I}(\text{speaker changed}) + w_{\text{punct}} \cdot \mathbb{I}(\text{sentence end})$$
  * Keep window token sizes bounded between 700 and 1,500 words with 1–2 surrounding context segments marked as `context_only` (non-core).

#### C. Fail-Closed Validation Gates
Every stage boundary must operate as a strict contract. If an LLM or subagent produces a quote that deviates by even one word, or attempts to cite a segment outside the window, the validator rejects the packet before state persistence.

---

### 2.2. Simplicity: Zero-Token Local Contracts & Minimal Moving Parts

#### A. Zero Heavy Framework Dependencies
Many production summarization tools rely on bloated orchestration frameworks (LangChain, LlamaIndex, CrewAI) that introduce breaking changes, heavy dependencies, and implicit network calls.
* **Simplicity Standard:** Keep the entire core library restricted to **Python standard library** (`json`, `re`, `dataclasses`, `pathlib`, `hashlib`, `unittest`, `argparse`) plus standalone binaries (`ffmpeg.exe`, `yt-dlp.exe`, `faster-whisper`).

#### B. Single-Binary / Single-Command Interface
Replace multi-script invocations with a unified CLI:
```powershell
# Unified command: Ingest -> Transcribe -> Map-Reduce -> Ground -> Compile Wiki
apex-transcribe --url "https://youtube.com/watch?v=..." --model base --output-vault "artifacts/vault"
```

#### C. Clean JSON Schema Interoperability
Standardize on typed schema contracts (`MacroResult`, `MesoModule`, `MicroClaim`) compatible with standard JSON-LD and Obsidian frontmatter.

---

### 2.3. Value & Operator Utility: Epistemic Knowledge Graphs

#### A. The Macro-Meso-Micro Knowledge Hierarchy
Information value is maximized when an operator can navigate seamlessly across zoom levels:
* **Macro (Executive / 30,000-ft View):** Core thesis, global takeaways, speaker ontology, taxonomy tags.
* **Meso (Modular / Chapter View):** Discrete conceptual deep-dives, actionable step-by-step protocols, mechanisms, and caveats.
* **Micro (Forensic / Atomic View):** Atomic claims, verbatim source quotes, exact `[HH:MM:SS]` timecodes, internal confidence, and verification status.

#### B. Bi-Directional Obsidian Knowledge Graph
Rather than emitting a flat monolithic markdown file, compile a structured Obsidian vault:
* `index.md`: Master dashboard with transcluded Macro overview and Meso table of contents.
* `modules/`: Individual notes for each thematic deep dive.
* `claims/`: Atomic claim notes with backlinks to parent Meso modules and source transcript lines.
* `concepts/` & `entities/`: Auto-generated concept notes enabling network graph visualization.
* **YAML Frontmatter:** Include Dataview-compatible metadata (`claim_type`, `confidence`, `status`, `timestamp`, `speaker`).

#### C. Verification Checkworthiness Prioritization
Do not waste human or search API budgets fact-checking opinions or conversational anecdotes. Use automated routing:
* `FACT` / `ESTIMATE` with specific numeric/empirical claims $\rightarrow$ Route to `VerificationHook`.
* `OPINION` / `RECOMMENDATION` / `ANECDOTE` $\rightarrow$ Mark `VERIFICATION_SKIPPED` (retained as source opinion).

---

### 2.4. Token Efficiency: Budget Compression & Extraction Optimization

#### A. Extractive Pre-Filtering Before Abstractive Synthesis
Academic research (e.g., AFEV, Claimify, Min-Check) demonstrates that feeding raw, repetitive spoken transcripts directly into LLMs wastes 40–60% of context tokens on conversational filler ("you know", "like", "sort of", throat-clearing).
* **Efficiency Optimization:** Perform deterministic preprocessing:
  1. Remove disfluencies, filler words, and repetitive stutters.
  2. Strip non-informative speech segments (salutations, sponsorship intros, outro music).
  3. Extract candidate propositional spans using lightweight heuristic or local embedding filtering before sending to heavy synthesis models.

#### B. Bounded Map-Reduce Token Budgets
* **Map Phase:** Each 1,000-word transcript chunk is compressed into a structured ~200-word Map packet (5:1 compression ratio).
* **Reduce Phase:** Combining 10 Map packets (2,000 tokens total) fits easily within standard context windows, eliminating recursive reduce overhead and information dilution.

#### C. Near-Duplicate Claim Deduplication
In long discussions, speakers frequently repeat the same point in different words across multiple chapters.
* **Optimization:** Implement Jaccard / Levenshtein similarity clustering on candidate claims during Reduce:
  $$\text{Sim}(C_1, C_2) = \frac{|T_1 \cap T_2|}{|T_1 \cup T_2|} > 0.75$$
  Merge duplicates into a single canonical claim referencing multiple source timestamps (`00:12:30`, `01:45:10`).

---

## 3. The Unified Hybrid Architecture Blueprint

```
┌──────────────────────────────────────────────────────────────────────────────────────────────────┐
│                                 UNIFIED COMPONENT STACK                                          │
├────────────────────────────────┬────────────────────────────────┬────────────────────────────────┤
│ Component                      │ Technology / File              │ Role & Responsibility          │
├────────────────────────────────┼────────────────────────────────┼────────────────────────────────┤
│ 1. Media Acquisition           │ yt-dlp.exe + ffmpeg.exe        │ Audio-only stream extraction   │
│ 2. Offline Transcription (ASR) │ faster-whisper (int8 CTrans2)  │ Word timestamps & diagnostics  │
│ 3. Acoustic Filter & Windowing │ ttk_windows.py + ASR Pruning   │ Semantic pause-weighted chunks │
│ 4. Evidence Extraction (Map)   │ ttk_map.py + Extractive Filter │ Candidate claims with quotes   │
│ 5. Reduction & Synthesis       │ transcript_engine.py + Reduce  │ Macro-Meso-Micro distillation  │
│ 6. Verification Routing        │ ttk_verify.py + Hook           │ Fact-checking checkworthiness  │
│ 7. Grounding Validator         │ GroundingValidator (P1/P2/P3)  │ Exact verbatim quote check     │
│ 8. Vault & Agent Exporter      │ ttk_wiki.py + Exporter         │ Obsidian vault + AI trigger    │
└────────────────────────────────┴────────────────────────────────┴────────────────────────────────┘
```

---

## 4. Prioritized Recommendations for Hybrid Unification

Recommendations are ranked according to **Impact**, **Evidence**, and **Risk**:

| Rank | Recommendation / Work Item | Impact | Evidence in Codebase / Research | Risk | Recommended Action |
| :---: | :--- | :---: | :--- | :---: | :--- |
| **1** | **ASR Acoustic Quality Filtering**<br>Prune hallucination loops and silence artifacts using `no_speech_prob` and `avg_logprob`. | **HIGH** | Benchmark runs showed occasional music/outro hallucinations in raw transcripts. | **LOW** | Implement pre-filter in `transcribe_audio.py` before windowing. |
| **2** | **Merge Dataclass Schema with TTK Reduce Engine**<br>Unify `transcript_engine.py` (P2) with `ttk_compile.py` (P3) into a single typed dataclass model. | **HIGH** | P2 has clean typed dataclasses; P3 has robust Map-Reduce. Currently maintain separate representations. | **LOW** | Refactor `ttk_compile.py` to use `MacroResult`, `MesoModule`, and `MicroClaim` dataclasses directly. |
| **3** | **Automated Extractive Pre-Filtering**<br>Strip disfluencies and conversational filler before Map packet generation. | **HIGH** | Research shows 40–50% token savings and higher claim extraction accuracy on cleaned speech. | **LOW** | Add deterministic disfluency cleaner in `ttk_source.py`. |
| **4** | **1-Click Master Pipeline Orchestrator**<br>Create `Invoke-ApexTranscriptPipeline.ps1` wrapping Ingestion $\rightarrow$ ASR $\rightarrow$ TTK Lifecycle $\rightarrow$ Vault Compilation. | **HIGH** | Currently requires running PowerShell for ASR and Python for TTK lifecycle separately. | **LOW** | Build master PowerShell cmdlet orchestrating end-to-end flow with progress reporting. |
| **5** | **Obsidian Graph Frontmatter & Dataview Schema**<br>Add rich YAML frontmatter to all generated wiki markdown files. | **MEDIUM** | Enables operators to query knowledge bases via Dataview queries (e.g. `WHERE claim_type = "FACT" AND status = "CONFIRMED"`). | **LOW** | Update `ttk_wiki.py` templates to emit YAML frontmatter. |
| **6** | **Near-Duplicate Claim Deduplication in Reduce**<br>Cluster and merge identical claims cited at different timestamps. | **MEDIUM** | 2-hour Huberman video contained 3 repeated discussions of autonomic cold habituation. | **MEDIUM** | Implement Levenshtein token similarity clustering in Reduce stage. |
| **7** | **WhisperX / Diarization Upgrade**<br>Add speaker diarization and phoneme-level word alignment. | **HIGH** | Currently speaker labels are estimated from transcript cues. | **MEDIUM** | Plan as Phase 2 upgrade after hybrid unification is locked. |

---

## 5. Next Execution Steps

1. **Sprint 1 (Unification Core):** Unify P2 dataclasses with P3 Map-Reduce engine and build master orchestrator `Invoke-ApexTranscriptPipeline.ps1`.
2. **Sprint 2 (Token Compression & ASR Filtering):** Integrate Faster-Whisper diagnostic pruning and extractive disfluency filtering.
3. **Sprint 3 (Obsidian Vault & PKM Upgrade):** Add YAML frontmatter, Dataview indexing, and concept graph cross-linking.
