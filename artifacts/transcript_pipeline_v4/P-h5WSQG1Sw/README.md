# Source Artifact Audit: P-h5WSQG1Sw

## 1. Source Metadata
- **Source ID**: `P-h5WSQG1Sw`
- **Title**: Huberman Lab Podcast: Dr. Ralph Adolphs on the Neurobiology of Emotions
- **URL**: `https://www.youtube.com/watch?v=P-h5WSQG1Sw`
- **Language**: English (`en`)
- **Format**: Long-Form Academic Stress Test Dialogue (~2.5 hours)
- **Transcript Metrics**: 1,471 lines, 23,892 words, 141.9 KB (145,305 bytes)

---

## 2. ASR Transcription Details
- **Engine / Model**: `faster-whisper` (`large-v3-turbo`, device `cpu`, compute_type `int8`, `vad_filter=True`)
- **Acquisition Tool**: `yt-dlp` extracting audio stream converted to `m4a` via `FFmpeg`
- **Output Files**:
  - `transcript.txt` — Clean UTF-8 text strip of timestamps and cue numbers.
  - `transcript.srt` — Timestamped subtitle cues.
  - `run.log` — Timestamped execution facts log.
  - `source/source.m4a` & `source/source.info.json` — Raw media and yt-dlp metadata.

---

## 3. Transformation History & Tool Comparisons

### Mechanism 1: Historical TTK / V2 Pipeline
- **Artifacts**: [`knowledge_ttk_v2_wiki.md`](./knowledge_ttk_v2_wiki.md), [`knowledge_ttk_v2_wiki.json`](./knowledge_ttk_v2_wiki.json)
- **Configuration**: Early V2 transcript-to-knowledge relay pipeline.
- **Strengths**: Extracted early functional emotion definitions.
- **Weaknesses**: Incomplete coverage of middle and late transcript sections; lost nuanced neurological double-dissociation details.

### Mechanism 2: Legacy Fabric + Ollama (`qwen3.5:9b`)
- **Execution Log**: `run.log` (recorded 60-minute timeout / memory bottleneck)
- **Outcome**: **FAILED / TIMED OUT**.
- **Weaknesses**: Local `qwen3.5:9b` CPU execution over 140k+ characters exceeded the 60-minute window, suffered severe latency, and failed to produce a valid `knowledge.md`.

### Mechanism 3: Adopted Production `obsidian-wiki` (`wiki-ingest`)
- **Target Vault**: `knowledge/transcript-wiki/`
- **Artifacts Produced**: 12 pages (1 reference, 4 entities, 7 concepts).
  - Reference: [`references/huberman-adolphs-neurobiology-of-emotions.md`](file:///c:/GitDev/apexai-os-meta/knowledge/transcript-wiki/references/huberman-adolphs-neurobiology-of-emotions.md)
  - Entities: `ralph-adolphs`, `andrew-huberman`, `david-anderson`, `patient-sm`
  - Concepts: `functional-theory-of-emotion`, `emotion-operating-features`, `emotion-vs-feeling-dissociation`, `amygdala-vs-brainstem-fear-circuits`, `temporal-persistence-in-amnesia`, `insula-and-interoception`, `cognitive-task-switching-cost`
- **Strengths**: **100% PASS (Definitive Stress Test)**. Full coverage across early (functional emotion theory), middle (Patient SM double dissociation, insula interoception), and late (task switching, 5-minute silence, Huberman tour) sections.

---

## 4. Strengths, Weaknesses & Comparative Audit

| Evaluation Dimension | Historical TTK / V2 | Legacy Fabric + Ollama | Production obsidian-wiki | Verdict |
| :--- | :--- | :--- | :--- | :--- |
| **Long-Source Capacity** | Partial extraction | **FAILED (Timed out)** | **PASSED (100% coverage)** | **obsidian-wiki Superior** |
| **Fidelity on Complex Logic** | Moderate | None (failed) | High (Patient SM double dissociation captured) | **obsidian-wiki Superior** |
| **Vault Integration** | Isolated files | None (failed) | 12 interconnected notes in cumulative vault | **obsidian-wiki Superior** |
