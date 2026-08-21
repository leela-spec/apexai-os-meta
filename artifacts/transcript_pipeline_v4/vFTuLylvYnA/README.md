# Source Artifact Audit: vFTuLylvYnA

## 1. Source Metadata
- **Source ID**: `vFTuLylvYnA`
- **Title**: Markus Koch Opening Bell Broadcast (Treasury Yields, BofA Sentiment, Tech Earnings)
- **URL**: `https://www.youtube.com/watch?v=vFTuLylvYnA`
- **Language**: German (`de`)
- **Format**: German Financial Market Monologue
- **Transcript Metrics**: 274 lines, 2,891 words, 17.5 KB (17,920 bytes)

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

### Mechanism 1: Legacy Fabric + Ollama (`qwen3.5:9b`)
- **Artifact**: [`knowledge_fabric_ollama.md`](./knowledge_fabric_ollama.md)
- **Configuration**: Fabric pattern `extract_wisdom`, vendor `Ollama`, model `qwen3.5:9b`, context length `65536`.
- **Execution Time**: ~75 seconds.
- **Strengths**: Accurately extracted German monetary terms and numerical figures (30y yield @ 5.33%, cash levels <3.5%).
- **Weaknesses**: Isolated markdown summary without cross-domain linking or integration into market structure concepts.

### Mechanism 2: Adopted Production `obsidian-wiki` (`wiki-ingest`)
- **Target Vault**: `knowledge/transcript-wiki/`
- **Artifacts Produced / Merged**: 6 new pages created + 1 page merged (`concepts/fifth-wave-characteristics.md`).
  - Reference: [`references/markus-koch-opening-bell-august.md`](file:///c:/GitDev/apexai-os-meta/knowledge/transcript-wiki/references/markus-koch-opening-bell-august.md)
  - Entities: `markus-koch`, `bank-of-america-global-research`
  - Concepts: `bofa-fund-manager-survey`, `treasury-yield-pressure`, `retail-earnings-expectations-bar`, `sell-the-news-dynamics`, `fifth-wave-characteristics` (Merged)
- **Strengths**: Demonstrated cumulative cross-source synthesis by linking Markus Koch's BofA sentiment cash depletion data (<3.5%) directly into Elliott Prechter's 5th wave terminal advance concept note.

---

## 4. Strengths, Weaknesses & Comparative Audit

| Evaluation Dimension | Legacy Fabric + Ollama | Production obsidian-wiki | Verdict |
| :--- | :--- | :--- | :--- |
| **German Domain Retention** | Preserved key German numbers | Preserved exact figures + linked macro concepts | **obsidian-wiki Superior** |
| **Concept Integration** | Standalone summary | Merged into cumulative 5th wave concept | **obsidian-wiki Superior** |
| **Auditability** | Plain markdown | Provenance markers (`^[inferred]`, `^[ambiguous]`) | **obsidian-wiki Superior** |
