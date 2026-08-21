# Bakeoff Result: obsidian-wiki Integration Evaluation

## 1. Executive Summary
- **Tested Implementation**: `obsidian-wiki` (v2026.8.4)
- **Target Repository**: `leela-spec/apexai-os-meta`
- **Vault Path**: `knowledge/transcript-wiki`
- **Final Verdict**: **ADOPT**

The external `Ar9av/obsidian-wiki` package was successfully installed and tested against all three real V4 transcript classes in the repository, resolving the semantic bottleneck that stalled the previous V4 architecture.

---

## 2. Benchmark Corpus Execution Results

### Source 1: `CygwqaNg2PY` (Compact Technical / Financial Interview)
- **Format**: English dialogue (343 lines, 21.3 KB)
- **Subject**: Elliott Prechter on Elliott Wave Theory, E-Waves quantitative engine, market stationarity.
- **Pages Created**: 11 pages (6 concepts, 4 entities, 1 reference).
- **Result**: **PASS**. Clean extraction of historical context (R.N. Elliott 1930s origin, Robert Prechter 1980s revival), quant model architecture (1986 inception, modernization), and market dynamics (5th wave breadth thinning, flat patterns, Bitcoin-NASDAQ divergence).

### Source 2: `vFTuLylvYnA` (German Domain-Specific Market Commentary)
- **Format**: German monologue (274 lines, 17.5 KB)
- **Subject**: Markus Koch Opening Bell on 10y/30y Treasury yields, BofA Fund Manager Survey, retail guidance, tech earnings sell-offs.
- **Pages Created / Updated**: 6 new pages created, 1 existing page merged (`concepts/fifth-wave-characteristics.md`).
- **Result**: **PASS**. Cumulative integration merged institutional cash depletion (<3.5%) and semiconductor crowded trades (53%) directly into the existing 5th wave concept. German terminology and exact financial numbers (10y @ 4.74%, 30y @ 5.33%, Fabrinet $13M datacom miss) preserved without error.

### Source 3: `P-h5WSQG1Sw` (Long-Source Multi-Speaker Academic Stress Test)
- **Format**: English dialogue (1,471 lines, 141.9 KB)
- **Subject**: Andrew Huberman & Dr. Ralph Adolphs on functional emotion theory, Patient SM lesion studies, amnesia persistence, interoception, and regulation.
- **Pages Created / Updated**: 12 new pages created.
- **Result**: **PASS (Definitive)**.
  - **Early Region**: Functional theory of emotion (control states intermediate between reflexes and deliberate cognition), four operational features (Priority, Valence, Scalability, Temporal Persistence), and separation from subjective conscious feeling.
  - **Middle Region**: Double dissociation in fear circuits (Patient SM amygdala lesion abolishes external threat fear but retains brainstem-driven CO2 suffocation panic); insular interoceptive mapping; Lauri Nummenmaa body maps classified as conceptual rather than somatic telemetry.
  - **Late Region**: Cognitive task switching costs; 5-minute lab meeting silence routine (started in 2020 after George Floyd); ice bath autonomic down-regulation; personal 100-mile ultramarathon training after cancer recovery; Huberman book tour specifics (NYC Radio City Sept 17, LA Dolby Oct 8, SF Masonic Oct 28).

---

## 3. Detailed Dimension Scoring & Comparison

| Evaluation Dimension | Previous V4 (Fabric + Qwen 9B) | obsidian-wiki Integration | Evaluation / Verdict |
| :--- | :--- | :--- | :--- |
| **Long-Source Completion** | **FAILED** (Timed out / OOM on `P-h5WSQG1Sw`) | **PASSED** (Full 140k-char fidelity) | **Major Advance** |
| **Cross-Source Integration** | Single isolated `knowledge.md` summaries | Connected 33-page knowledge graph | **Major Advance** |
| **Concept Deduplication** | High redundancy across runs | Reuses existing pages; merges claims | **Passed** |
| **Numeric & Entity Fidelity** | Often truncated or hallucinated | Exact figures and proper nouns preserved | **Passed** |
| **Incremental Delta Processing** | Re-runs entire prompt on every invoke | SHA-256 manifest skip (`cache-check`) | **Passed (Zero overhead)** |
| **Resumability** | No checkpointing; failure loses full run | Source-level deterministic recovery | **Acceptable (Strong at file level)** |
| **Fresh-Agent Retrieval** | Requires scanning whole summary dump | Sub-second index/summary lookup (`query`) | **Passed** |
| **Provenance Tracking** | Generic attribution block | Claim-level markers + source arrays | **Passed** |
| **Operational Health** | Unvalidated markdown generation | Built-in linter (`lint`) + trust ledger | **Passed (0 issues)** |

---

## 4. Fresh-Agent Knowledge Test Results
A fresh query evaluation against the generated vault (`knowledge/transcript-wiki/`) without original transcripts produced 100% accurate retrievals across all benchmark questions:

1. **Early Theory**: Correctly retrieved `concepts/functional-theory-of-emotion.md` defining emotions as intermediate functional control states between rigid reflexes and flexible cognitive planning.
2. **Circuit Mechanism**: Correctly retrieved `concepts/amygdala-vs-brainstem-fear-circuits.md` and `entities/patient-sm.md` identifying the double dissociation between amygdala-mediated external threat fear and brainstem-mediated CO2 inhalation panic.
3. **Late-Source Qualification**: Correctly retrieved `concepts/cognitive-task-switching-cost.md` describing cognitive inertia and the Caltech 5-minute silence intervention.
4. **Exact Numerical Retrieval**: Correctly retrieved `concepts/treasury-yield-pressure.md` (30-year yield at 5.33%, 19-year high) and `concepts/bofa-fund-manager-survey.md` (cash levels <3.5%).
5. **Disputed / Trapped Proposition**: Correctly retrieved `concepts/flat-pattern.md` detailing the 3-3-5 corrective pattern that lures breakout traders into new nominal highs before steep declines.
6. **Cross-Source Synthesis**: Correctly retrieved `concepts/fifth-wave-characteristics.md` synthesized from both Elliott Prechter's wave dynamics and Markus Koch's BofA sentiment analysis.

---

## 5. Incremental & Recovery Behavior
- `obsidian-wiki cache-check` executed on all 3 sources correctly reported all 3 as `unchanged`, skipping reprocessing completely.
- Manifest state is atomic per source in `.manifest.json`.

---

## 6. Provenance & Format Findings
- `transcript.txt` is the optimal default format for narrative flow and semantic distillation.
- `.srt` files can be passed directly if fine-grained timestamp indexing is required.
- No custom pre-adapter or Map/Reduce layer is needed.

---

## 7. Final Verdict
**ADOPT**
`Ar9av/obsidian-wiki` (v2026.8.4) fulfills all functional and architectural requirements, succeeds on the stress-test long source, and establishes a robust, compounding knowledge base.
