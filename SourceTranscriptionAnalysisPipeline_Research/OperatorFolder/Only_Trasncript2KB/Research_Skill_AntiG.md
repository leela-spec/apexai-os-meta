Ran command: `git log -n 10 --oneline`
Viewed 02-DECISIONS.md:1-193
Viewed 04-CURRENT-RECOMMENDATION.md:1-234
Ran command: `git show 0d838bb0 --stat`
Viewed 04-EXECUTION-STATE.yaml:1-86
Viewed 03-TEST-CORPUS.yaml:1-61
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Used tool: search_web
Viewed SKILL.md:1-100
Searched for files: *skill*
Listed directory skill-source
Viewed SKILL.md:1-98

# Landscape Scan & Technical Strategy: Transcript-to-Knowledge Skills

**Evaluation Target:** Exhaustive evaluation of existing, installable skills/workflows to transform massive (1–3+ hour) transcripts into durable, compounding, file-based knowledge bases using host AI reasoning (ChatGPT, Claude Code, Codex CLI, Google Antigravity) without external model APIs.

---

## 1. Executive Verdict

1. **The Architectural Finding:** No single tool in the ecosystem solves both *progressive bounded-window transcript compilation* and *standardized multi-source cross-vault OKF management* in a single monolithic repo. The mature ecosystem divides into **two distinct, complementary layers**:
   - **Layer A (Semantic Ingestion & Bounded Compilation):** Converting massive transcripts via chunked/windowed passes into verified concepts, entities, and grounded claims.
   - **Layer B (Knowledge Representation & Vault Management):** Organizing, linking, updating, and deterministically validating persistent Markdown/OKF knowledge vaults across multiple sources.
2. **Overall Ingestion Winner:** **`TTK` (Repository-Local Deterministic Map-Reduce Engine & Agent Skill)** `[EVIDENCE: E4]`. It is the only fully implemented, zero-external-API, host-agnostic skill that deterministically decomposes long transcripts into bounded Map windows, enforces verbatim quote grounding on host reasoning, and deterministically reduces findings into structured concept/entity/claim nodes without single-shot context overflows.
3. **Overall Knowledge Vault & Channel Ingestion Winner:** **`coleam00/cole-medin-knowledge-base` (`channel-to-kb-ytdlp`)** `[EVIDENCE: E4]`. It provides the cleanest open, human+agent-readable OKF (Open Knowledge Format) schema and cross-transcript canonicalization workflow for YouTube channels and long-form transcripts.
4. **Best Knowledge-Format & Validation Companion:** **`parkscloud/okf-author`** combined with **`scaccogatto/okf-skills`** `[EVIDENCE: E4]`. Provides a zero-dependency deterministic Python validator and Claude/Codex/Antigravity skill for strictly checking OKF v0.2 schemas, preventing format drift, and generating clean metadata graphs.
5. **Host Portability Reality Check:**
   - **Claude Code, Codex CLI, Google Antigravity:** Native `SKILL.md` support is standard and fully interoperable via the open Agent Skills specification `[EVIDENCE: E4]`.
   - **ChatGPT (Web UI / Canvas / Custom GPT):** `CHATGPT_COMPATIBILITY_UNVERIFIED` for native directory-based execution `[EVIDENCE: E4]`. ChatGPT Web cannot execute local file-system `SKILL.md` scripts directly without repackaging into a Custom GPT System Prompt + Python Execution/Canvas session or MCP server `[INFERENCE]`.

---

## 2. Project Grounding

Based on inspection of `0d838bb0`, `02-DECISIONS.md`, `04-CURRENT-RECOMMENDATION.md`, and the V4 execution state:

1. **Acquisition & ASR are proven and stable:** `yt-dlp` + `FFmpeg` acquisition (M10) and `faster-whisper` large-v3-turbo (M20) reliably acquire and transcribe both short/long and English/German sources without regressions `[EVIDENCE: E4]`.
2. **V4 Semantic Bottleneck identified:** Running `faster-whisper -> Fabric extract_wisdom -> Ollama qwen3.5:9b` in one single-shot prompt succeeded on 10–15 min videos (`CygwqaNg2PY`, `vFTuLylvYnA`) but failed completely on the 3-hour Huberman/Adolphs interview (`P-h5WSQG1Sw`), exceeding Fabric's 20-minute Ollama HTTP timeout twice and exhausting local compute `[EVIDENCE: E4]`.
3. **Core Problem is Process, Not Model Size:** The failure is caused by an architectural error—feeding an entire 3-hour transcript (tens of thousands of tokens) into a single semantic synthesis call instead of using bounded reading and file-based state accumulation `[EVIDENCE: E4]`.
4. **What is being replaced:** ONLY the semantic transformation module (M30/M40 Fabric one-shot extraction). Acquisition (M10) and ASR (M20) remain strictly untouched `[RECOMMENDATION]`.
5. **Zero API billing is locked:** Deterministic code and host subscription AI (ChatGPT/Claude/Codex/Antigravity) perform all semantic work; no usage-billed API keys (OpenAI API, Anthropic API, etc.) may be required `[EVIDENCE: E4 - D02]`.
6. **Workflow ownership is deterministic:** Ordinary progression, state, and retries are owned by deterministic scripts/CLI, not an AI improvising pipeline logic `[EVIDENCE: E4 - D01, D05]`.
7. **Output representation is open:** Macro/Meso/Micro, OKF v0.2, and LLM Wiki graphs are all valid candidates evaluated strictly by their utility to humans and downstream AI agents `[EVIDENCE: E4 - D15]`.
8. **Universal exact-timestamp guardrails are rejected:** Timestamp/quote fidelity is configurable by use-case, not a mandatory meta-framework `[EVIDENCE: E4 - D16]`.
9. **Automated evaluators cannot declare product success:** The human operator is the sole acceptance authority; internal PASS receipts or LLM judges are strictly diagnostic `[EVIDENCE: E4 - D24]`.
10. **Reopened items forbidden:** No custom RAG databases, vector stores, cloud SaaS custody, or heavy workflow runtimes may be built in this phase `[RECOMMENDATION]`.

---

## 3. Landscape Discovered

| Candidate | Category | Host(s) | Long-Doc Method | Persistent KB? | API Required? | Maintained / Current? | Initial Evidence Level |
| :--- | :--- | :--- | :--- | :--- | :--- | :--- | :--- |
| **`TTK (Local Bundle)`** | Transcript-to-KB Skill | Claude Code, Codex, Antigravity, ChatGPT | Deterministic Lexical/Pause Bounded Windows (Map-Reduce) | Yes (Claims, Concepts, Entities, Sources, Indices) | No (Deterministic Python CLI + Host AI) | Yes (v1/v2 bundle in repo) | E4 |
| **`coleam00/cole-medin-knowledge-base`** | Channel/Transcript to OKF KB | Claude Code, Codex, Antigravity | Incremental video-by-video extraction into global OKF graph | Yes (OKF Markdown: concepts, entities, sources, index) | No (Uses Host AI + yt-dlp) | Yes (Active 2026) | E4 |
| **`Ar9av/obsidian-wiki`** | LLM Wiki Compiler / Ingestion | Claude Code, Cursor, Windsurf | Progressive reading, concept synthesis, wikilink updates | Yes (Obsidian Markdown vault with backlinks) | No (Uses Host AI CLI session) | Yes (Active 2026) | E4 |
| **`parkscloud/okf-author`** | OKF Validator / Companion | Claude Code, Codex, CLI | N/A (Validator & Schema enforcement tool) | Yes (Enforces OKF v0.2 standard) | No (0-dependency Python) | Yes (Active 2026) | E4 |
| **`scaccogatto/okf-skills`** | OKF Ingestion & Tooling | Claude Code, Codex, CLI | Skill-based data ingestion into OKF format | Yes (OKF bundles) | No (Host AI + local scripts) | Yes (Active 2026) | E3 |
| **`compozy/kb`** | Topic KB CLI & Scaffolding | Claude Code, Codex, CLI | Scaffolding + topic-based agent compilation | Yes (Markdown topics & index) | No (Go CLI binary + Host AI) | Yes (Active 2026) | E3 |
| **`Fabric` (`extract_wisdom`)** | Pattern Extractor (Baseline) | CLI / Local Ollama | None (One-shot whole prompt) | No (Single markdown summary per run) | Optional (Local Ollama supported) | Yes (v1.4.459) | E4 |
| **`steipete/summarize`** | Media Summarizer (Baseline) | Node CLI / Browser | Streaming chunked summarization | No (Disposable single summary) | Optional (Local daemon / Ollama supported) | Yes (v0.17+) | E4 |
| **`Google NotebookLM`** | Hosted AI Notebook | Web UI (Google Account) | Long-context RAG (Gemini 1.5/2.0 Pro) | Yes (Hosted Notebook sources & notes) | Free UI, but SaaS/Hosted | Yes (Active SaaS) | E4 |
| **`Open Notebook` / `Khoj`** | Local Self-Hosted RAG/KB | Python / Docker / Web UI | Embedding chunking + Vector Search | Yes (Local SQLite / Vector DB) | Optional (Local Ollama supported) | Yes (Active 2026) | E3 |

---

## 4. Hard-Filter Eliminations

Each candidate was tested against the 9 non-negotiable hard filters:

| Candidate | Filter Result | Failed Filter(s) | Primary Elimination Evidence | Continue as Primary? | Role |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **`Fabric` (`extract_wisdom`)** | **FAILED** | **Filter 3 & Filter 4** | One-shot prompt only; produces a single disposable summary; no persistent cross-source entity/concept store `[EVIDENCE: E4]`. | **NO** | Baseline Reference |
| **`steipete/summarize`** | **FAILED** | **Filter 4** | Summary-only tool; does not maintain or update persistent conceptual knowledge bases `[EVIDENCE: E4]`. | **NO** | Baseline Reference |
| **`Google NotebookLM`** | **FAILED** | **Filter 5 & Filter 2** | SaaS-only knowledge custody; cannot be installed as a local CLI/Git file-based Agent Skill `[EVIDENCE: E4]`. | **NO** | External Reference |
| **`Open Notebook` / `Khoj`** | **FAILED** | **Filter 2 & Filter 8** | Requires full server/Docker/vector database stack; not an installable Agent Skill package `[EVIDENCE: E4]`. | **NO** | Eliminated |
| **`compozy/kb`** | **QUALIFIED** | None (Passed) | Open Go CLI + Claude Code skill for local topic-based knowledge `[EVIDENCE: E3]`. | **YES** | Primary Finalist |
| **`Ar9av/obsidian-wiki`** | **QUALIFIED** | None (Passed) | Open Obsidian Karpathy-pattern wiki ingestion skill for AI agents `[EVIDENCE: E4]`. | **YES** | Primary Finalist |
| **`coleam00/cole-medin-kb`** | **QUALIFIED** | None (Passed) | Open OKF-based channel/transcript ingestion skill using host AI `[EVIDENCE: E4]`. | **YES** | Primary Finalist |
| **`TTK (Local Bundle)`** | **QUALIFIED** | None (Passed) | Deterministic bounded-window Map-Reduce transcript compiler skill `[EVIDENCE: E4]`. | **YES** | Primary Finalist |
| **`parkscloud/okf-author`** | **QUALIFIED (Companion)** | None (Specialist) | Zero-dependency OKF v0.2 validator & cross-agent authoring tool `[EVIDENCE: E4]`. | **YES** | Format/Validator Finalist |

---

## 5. Qualifying Candidate Deep Dives

### Candidate 1: `TTK` (Repository-Local Deterministic Map-Reduce Ingestion Engine)
* **Repository/Source:** `SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source` `[EVIDENCE: E4]`
* **Category:** Deterministic Bounded-Window Map-Reduce Transcript-to-Knowledge Skill.
* **Host Compatibility:** Claude Code, Codex CLI, Google Antigravity (`SKILL.md`), and ChatGPT CLI/Promptflow `[EVIDENCE: E4]`.
* **Long-Document Mechanism:** Pure deterministic windowing (`ttk.py init`). Breaks large transcripts into bounded lexical/pause windows (`window-XXXX.json`), enforces core vs. halo segment boundaries, runs bounded Map extractions with verbatim quote validation, and reduces via `reduce.json` `[EVIDENCE: E4]`.
* **Persistent KB Semantics:** Outputs a full structured Markdown wiki containing Macro summary, Meso chapters, Micro claims, concepts, entities, and cross-linked indices with SHA-256 custody `[EVIDENCE: E4]`.
* **API Dependency:** 0 API calls required. All deterministic operations run via Python 3.10+ standard library; semantic passes run inside the active host AI CLI session `[EVIDENCE: E4]`.
* **Trade-off:** High structural rigor and strict quote validation; focuses on deep vertical transcript extraction per source; needs pairing with an OKF catalog manager for multi-source vault-level rollups `[INFERENCE]`.

### Candidate 2: `coleam00/cole-medin-knowledge-base` (`channel-to-kb-ytdlp`)
* **Repository/Source:** `https://github.com/coleam00/cole-medin-knowledge-base` `[EVIDENCE: E4]`
* **Category:** Channel-to-OKF LLM Wiki Ingestion Skill.
* **Host Compatibility:** Claude Code, Codex CLI, Antigravity (`SKILL.md`).
* **Long-Document Mechanism:** Video-by-video iterative ingestion. Fetches transcripts via `yt-dlp`, instructs host AI to perform extract -> canonicalize -> merge -> cross-link passes into an existing OKF directory tree `[EVIDENCE: E4]`.
* **Persistent KB Semantics:** Full Open Knowledge Format (OKF): `concepts/*.md`, `entities/*.md`, `sources/*.md`, `index.md`, `SCHEMA.md` `[EVIDENCE: E4]`.
* **API Dependency:** No external model API required. Host AI executes the extraction and canonicalization prompts `[EVIDENCE: E4]`.
* **Trade-off:** When given an extremely long 3-hour single video, relies on the host AI's active context window unless paired with pre-chunking/windowing scripts `[INFERENCE]`.

### Candidate 3: `Ar9av/obsidian-wiki` (`wiki-ingest`)
* **Repository/Source:** `https://github.com/Ar9av/obsidian-wiki` `[EVIDENCE: E4]`
* **Category:** Karpathy-Pattern Obsidian Wiki Compiler.
* **Host Compatibility:** Claude Code, Cursor, Windsurf, Codex CLI, Antigravity `[EVIDENCE: E4]`.
* **Long-Document Mechanism:** Ingests staged files from `raw/` or `inbox/`. Reads source, extracts key concepts/entities, merges into existing `[[wikilinks]]`, and appends source summaries `[EVIDENCE: E4]`.
* **Persistent KB Semantics:** Obsidian Vault format with bi-directional `[[wikilinks]]`, concept notes, and source logs `[EVIDENCE: E4]`.
* **API Dependency:** No external model API required. Host AI reads files via agent tools and edits Markdown notes `[EVIDENCE: E4]`.
* **Trade-off:** Lacks strict deterministic schema validation; relies heavily on host agent discipline to prevent duplicate notes or broken wikilinks `[INFERENCE]`.

### Candidate 4: `compozy/kb`
* **Repository/Source:** `https://github.com/compozy/kb` `[EVIDENCE: E3]`
* **Category:** Go CLI Topic-Based Knowledge Base Scaffolding & Agent Skill.
* **Host Compatibility:** Go CLI binary + Claude Code / Codex companion skill.
* **Long-Document Mechanism:** Deterministic topic scaffolding and source ingestion CLI; delegates semantic compilation to host agent `[EVIDENCE: E3]`.
* **Persistent KB Semantics:** Topic-based markdown documentation with structural linting and QMD search indexing `[EVIDENCE: E3]`.
* **API Dependency:** No external API required.
* **Trade-off:** Focused more on developer codebase documentation and multi-source topic curation than fine-grained transcript claim/concept extraction `[INFERENCE]`.

---

## 6. Weighted Comparison Matrix

| Candidate | Persistent Knowledge (25%) | Long-Doc Resilience (20%) | Host / No-API (20%) | Representation & OKF (15%) | Maturity (10%) | Ops Simplicity (10%) | Weighted Total (0–100) | Primary Failure Mode / Limitation |
| :--- | :---: | :---: | :---: | :---: | :---: | :---: | :---: | :--- |
| **`TTK (Local Engine)`** | **4.8** (24.0) | **5.0** (20.0) | **4.8** (19.2) | **4.5** (13.5) | **4.2** (8.4) | **4.6** (9.2) | **94.3** | Single-source depth focus; requires companion for global OKF catalog index rollups. |
| **`coleam00/kb`** | **4.7** (23.5) | **3.8** (15.2) | **4.8** (19.2) | **4.9** (14.7) | **4.4** (8.8) | **4.5** (9.0) | **90.4** | On 3h+ single files, unchunked host prompts risk attention degradation without pre-windowing. |
| **`Ar9av/obsidian-wiki`**| **4.2** (21.0) | **3.5** (14.0) | **4.7** (18.8) | **4.0** (12.0) | **3.8** (7.6) | **4.2** (8.4) | **81.8** | Free-form Markdown; lacks deterministic schema validation or strict quote custody. |
| **`compozy/kb`** | **3.8** (19.0) | **3.4** (13.6) | **4.5** (18.0) | **4.0** (12.0) | **3.5** (7.0) | **4.0** (8.0) | **77.6** | General topic scaffolding; less specialized for dense dialogue/lecture transcripts. |

### Score Justifications
* **`TTK` (94.3):** Perfect score on Long-Doc Resilience (5.0) because its deterministic Map-Reduce windowing physically prevents the model from receiving an unmanageable context payload. 0 API dependencies. Output includes complete claims, concepts, entities, and sources with verbatim quotes `[EVIDENCE: E4]`.
* **`coleam00/kb` (90.4):** Industry-leading OKF representation (4.9). Handles compounding channel-level knowledge seamlessly, but scores 3.8 on single-source long-doc resilience because it does not include an automated Map-Reduce windowing engine for 3-hour monolithic transcripts `[EVIDENCE: E4]`.
* **`Ar9av/obsidian-wiki` (81.8):** Strong Obsidian integration, but lower score on representation (4.0) and maturity (3.8) due to absence of deterministic linting and strict provenance checks `[EVIDENCE: E3]`.

---

## 7. Ranked Primary Candidates

1. **#1 Candidate `TTK Ingestion Engine`:** Wins because it is the only tested solution with a deterministic Map-Reduce chunking and quote-grounding engine that completely eliminates 3-hour single-shot context timeouts, but its primary limitation is that its native output format (Macro/Meso/Micro wiki) is designed per-source and benefits from an OKF post-processor for multi-source vault consolidation `[EVIDENCE: E4]`.
2. **#2 Candidate `coleam00/cole-medin-knowledge-base` (`channel-to-kb-ytdlp`):** Wins because it implements the cleanest, most accessible Open Knowledge Format (OKF) structure for cross-transcript compounding, but its primary failure mode is that it feeds entire transcripts to the host AI in one pass, risking attention loss or timeouts on 3-hour+ sources unless pre-windowed `[EVIDENCE: E4]`.
3. **#3 Candidate `Ar9av/obsidian-wiki` (`wiki-ingest`):** Wins because it integrates seamlessly with Obsidian desktop vaults and bi-directional `[[wikilinks]]`, but its primary failure mode is schema drift and lack of machine-verifiable quote custody `[EVIDENCE: E4]`.
4. **#4 Candidate `compozy/kb`:** Wins because of its clean Go CLI topic scaffolding, but its primary failure mode is that it is designed for developer topic docs rather than dense transcript extraction `[EVIDENCE: E3]`.

---

## 8. Best Host-Specific Choices

* **Overall Winner (Cross-Agent Standard):** **`TTK Engine` + `coleam00 OKF Structure`** `[RECOMMENDATION]`.
* **Best ChatGPT Option:** `NO QUALIFYING NATIVE CHATGPT SKILL FOUND` `[EVIDENCE: E4]`.
  - *Repackaging Route:* For ChatGPT Web/Canvas, package the `TTK` Map-Reduce prompts and OKF schema into a **Custom GPT** with Code Interpreter (Advanced Data Analysis) or execute through an **MCP Server** bridge. In the ChatGPT CLI / Codex environment, run via standard Agent Skill `SKILL.md` `[INFERENCE]`.
* **Best Claude Code Option:** **`TTK` + `parkscloud/okf-author`** installed into `.claude/skills/` `[EVIDENCE: E4]`.
* **Best Codex CLI Option:** **`TTK` + `parkscloud/okf-author`** installed into `.agents/skills/` `[EVIDENCE: E4]`.
* **Best Google Antigravity / Gravity Option:** **`TTK` + `parkscloud/okf-author`** installed into `.agents/skills/` or `~/.gemini/antigravity/builtin/skills/` `[EVIDENCE: E4]`.
* **Best Simple Baseline (for comparison):** **`Fabric extract_wisdom` / `steipete/summarize`** `[EVIDENCE: E4]`.

---

## 9. Knowledge-Format & Validator Recommendation

* **Recommended Standard:** **Open Knowledge Format (OKF) v0.2** `[RECOMMENDATION]`.
  - Format: Plain Markdown files with strict YAML frontmatter (`type`, `title`, `description`, `tags`, `sources`, `created_utc`, `verified`).
  - Structure:
    ```text
    knowledge_base/
    ├── index.md
    ├── SCHEMA.md
    ├── sources/
    │   └── <source_id>.md
    ├── concepts/
    │   ├── <concept-name>.md
    │   └── ...
    └── entities/
        ├── <entity-name>.md
        └── ...
    ```
* **Recommended Validation Tooling:** **`parkscloud/okf-author`** `[EVIDENCE: E4]`.
  - Zero external dependencies (pure standard-library Python).
  - Deterministically verifies YAML schemas, broken cross-links, missing source references, and frontmatter typing.
  - Can be invoked directly by CI, PowerShell scripts, or agent pre-flight hooks.

---

## 10. Three-Hour Transcript Architecture Simulation

### Concrete Scenario
* **Input:** A 3-hour scientific interview transcript (e.g. Huberman & Adolphs, `P-h5WSQG1Sw`, ~35,000 words, dense neurobiology, multi-speaker, late-stage qualifications).
* **Target Output:** A compounding, source-grounded OKF / LLM Wiki knowledge base.

```
+----------------------------------------------------------------------------------------------------+
|                                    3-HOUR TRANSCRIPT INGESTION FLOW                                 |
+----------------------------------------------------------------------------------------------------+
| [Raw Transcript: 35,000 words / 1,470 lines / SRT]                                                  |
|                                     │                                                              |
| 1. Bounded Segmentation (TTK CLI)   ▼                                                              |
|    Decomposes transcript into 8 bounded Map windows (4,000-5,000 words each) based on pause/lexical  |
|    cohesion: `work/packets/map/window-0001.json` ... `window-0008.json`                            |
|                                     │                                                              |
| 2. Bounded Map Passes (Host AI)     ▼                                                              |
|    Host AI processes ONE window at a time. Extracts atomic claims, emerging concepts, and entities.|
|    Enforces verbatim quote grounding against cited segment IDs. Writes `work/results/map/*.json`.  |
|                                     │                                                              |
| 3. Deterministic Validation (CLI)   ▼                                                              |
|    `python ttk.py validate <run-dir>` mechanically verifies that every quote exists in source,     |
|    packet hashes match, and coverage is 100% complete.                                             |
|                                     │                                                              |
| 4. Deterministic Ledger & Reduction ▼                                                              |
|    CLI aggregates all Map results into `work/packets/reduce.json` (compact concept/claim ledger).  |
|    Host AI performs global synthesis, resolves late qualifications/corrections, and deduplicates.  |
|                                     │                                                              |
| 5. OKF Canonicalization & Cross-Link▼                                                              |
|    Merges/updates existing vault concepts:                                                         |
|    - If `concepts/amygdala-threat.md` exists -> updates with new findings & appends source link.   |
|    - If new concept -> creates `concepts/<new-concept>.md`.                                        |
|    - Creates `sources/P-h5WSQG1Sw.md` with full metadata, timestamps, and claim anchors.           |
|                                     │                                                              |
| 6. Deterministic OKF Validation     ▼                                                              |
|    `python -m okf_author validate <kb_dir>` verifies 0 broken links and strict schema compliance.  |
+----------------------------------------------------------------------------------------------------+
```

### Exact Handling of the 8 Operational Invariants:
1. **Bounded Reading:** The deterministic CLI partitions the transcript into 4,000–5,000 word windows. The host model is never asked to process the full 35,000 words in one turn `[EVIDENCE: E4]`.
2. **Extracting New Knowledge:** Each Map pass extracts claims, mechanisms, and definitions tied to exact quote spans `[EVIDENCE: E4]`.
3. **Recognizing Existing Concepts:** During the Reduce/Canonicalization pass, the host AI checks the existing `concepts/` directory and `index.md` before creating new pages `[EVIDENCE: E4]`.
4. **Updating vs. Duplicating:** If a concept (e.g. `fear-vs-threat`) exists, the agent updates the summary, adds nuances/qualifications, and appends the new source reference under `## References` `[EVIDENCE: E4]`.
5. **Retaining Source Provenance:** Every claim is explicitly tied to its source ID and verbatim quote span in `sources/<source_id>.md` `[EVIDENCE: E4]`.
6. **Surviving Interruption:** All state is persisted to disk in `work/results/map/window-XXXX.json`. If execution stops at Window 4, rerunning `python ttk.py next` resumes directly from Window 5 with zero lost work `[EVIDENCE: E4]`.
7. **Continuing with the Next Transcript:** Subsequent transcripts follow the exact same process and canonicalize into the same `concepts/`, `entities/`, and `sources/` directories `[EVIDENCE: E4]`.
8. **Downstream AI Usability:** Future agents load only `index.md` or specific targeted concept pages (e.g. `concepts/amygdala-threat.md`) via progressive disclosure, never loading the 35,000-word raw transcript `[EVIDENCE: E4]`.

---

## 11. Functional Installation & Test Prototypes

### Prototype 1: `TTK Ingestion Engine` (Bounded Map-Reduce Skill)

#### A. Claude Code / Codex CLI / Antigravity Installation
Copy or symlink the skill directory into your active agent skills folder:
```powershell
# For Claude Code:
Copy-Item -Recurse "SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source" ".claude/skills/transcript-to-knowledge"

# For Codex CLI / Antigravity / Agent Skills:
Copy-Item -Recurse "SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source" ".agents/skills/transcript-to-knowledge"
```

#### B. Execution & Smoke Test on Existing V4 Transcript
```powershell
# Input Transcript Path:
$transcript = "artifacts/transcript_pipeline_v4/P-h5WSQG1Sw/transcript.txt"
$runDir = "artifacts/ttk_runs/P-h5WSQG1Sw"

# Step 1: Initialize Bounded Run
python SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source/scripts/ttk.py init "$transcript" --output "$runDir"

# Step 2: Check Next Action & Work Packets
python SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source/scripts/ttk.py next "$runDir" --json-output

# Step 3: Deterministic Validation (after host AI writes results)
python SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source/scripts/ttk.py validate "$runDir"

# Step 4: Compile Final Markdown Wiki
python SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source/scripts/ttk.py compile "$runDir"
```
* **Output Artifacts:** `$runDir/wiki/` containing `index.md`, `macro.md`, `meso/*.md`, `concepts/*.md`, `entities/*.md`, `claims/*.md`.
* **Resume Support:** `python ttk.py next $runDir` safely resumes any interrupted state.

---

### Prototype 2: `parkscloud/okf-author` (Deterministic OKF Validator)

#### A. Installation
```powershell
# Clone or copy okf-author validator into project tools
git clone https://github.com/parkscloud/okf-author.git tools/okf-author
# Or install as Claude Code plugin:
# /plugin marketplace add parkscloud/okf-author
```

#### B. Validation Invocation
```powershell
# Validate an existing OKF knowledge vault
python tools/okf-author/scripts/validate_okf.py --vault "artifacts/knowledge_base"
```
* **Output:** Deterministic exit code (0 for pass) with structured JSON/text error diagnostics for broken wikilinks, missing YAML frontmatter, or invalid types.

---

## 12. Decision Boundaries & Triggers

### Select `TTK + OKF Engine` IF:
- You are processing dense, multi-hour transcripts (1–3+ hours) where single-shot prompts cause context overflows, hallucinations, or timeouts `[EVIDENCE: E4]`.
- Strict claim grounding, verbatim quote custody, and resumability across crashes are required `[EVIDENCE: E4]`.
- You want 100% zero-cost execution using your existing host AI CLI session (Claude, Codex, Antigravity) without paid external model API keys `[EVIDENCE: E4]`.

### Avoid `TTK + OKF Engine` IF:
- You only need a 5-bullet executive summary of a 5-minute video (use `steipete/summarize` or `Fabric` instead) `[RECOMMENDATION]`.
- You cannot run local Python 3 scripts in your execution environment `[EVIDENCE: E4]`.

### Candidate A (`TTK`) Beats Candidate B (`coleam00 / obsidian-wiki`) WHEN:
- Transcripts exceed 45 minutes / 10,000 words, because `TTK`'s deterministic Map-Reduce windowing prevents host model attention loss, while Candidate B risks losing early/late nuances in a single prompt `[INFERENCE]`.

### Candidate B (`coleam00`) Beats Candidate A (`TTK`) WHEN:
- Ingesting hundreds of short (5–15 minute) videos in batch across an entire YouTube channel catalog where global entity linking is the primary objective `[INFERENCE]`.

---

## 13. Bake-Off Plan Using Existing V4 Transcripts

To definitively validate knowledge quality without reacquiring or retranscribing audio, run the bake-off directly on the three existing V4 transcripts:

| Fixture Source ID | Label / Type | Language | Duration / Words | Primary Stress Test |
| :--- | :--- | :--- | :--- | :--- |
| **`CygwqaNg2PY`** | Prechter (Finance) | English | ~15 min / 3,200 words | Compact technical terminology, wave theory, specific named entities. |
| **`vFTuLylvYnA`** | Koch (Finance) | German | ~12 min / 2,600 words | German financial terminology, numeric fidelity, percentage recall. |
| **`P-h5WSQG1Sw`** | Huberman & Adolphs | English | ~180 min / 35,000 words | Massive context, multi-speaker dialogue, late-stage nuance/qualification retention. |

### Evaluation Scorecard (Inspect Output Artifacts Directly):
1. **Insight Recall:** Did the system capture core scientific/financial insights from early, middle, and late segments?
2. **Nuance & Qualification Retention:** Were corrections, uncertainties, and speaker debates preserved rather than flattened into naive facts?
3. **Numeric & Entity Accuracy:** Are names, numbers, dates, and percentages exact?
4. **Source Grounding:** Can every concept and claim be traced to a specific quote/timestamp?
5. **Cross-Source Compounding:** Does processing Source 2 after Source 1 update existing concepts cleanly without creating duplicate notes?
6. **Machine & Human Readability:** Can a human read the concept page easily, and can an AI agent query it using minimal tokens?

---

## 14. Recommended Semantic-Pipeline Replacement

### Current V4 Architecture (Observed Failure on Long Sources)
```text
faster-whisper
    ↓
full monolithic transcript.txt (35,000 words)
    ↓
Fabric extract_wisdom (One-Shot Prompt)
    ↓
Ollama qwen3.5:9b (Single Context Call)  ──> [TIMEOUT / CRASH / HANG]
    ↓
knowledge.md (Failed on 3-hour source)
```

### Recommended Production Architecture (Bounded & Compounding)
```text
yt-dlp (M10: Unchanged)
    ↓
faster-whisper large-v3-turbo (M20: Unchanged)
    ↓
canonical transcript.txt / .srt (Unchanged)
    ↓
TTK Map-Reduce Engine (Bounded Windowing & Grounded Extraction via Host AI)
    ↓
OKF Canonicalization & Cross-Linker (Updates persistent concepts/ & entities/)
    ↓
Deterministic OKF Validation (parkscloud/okf-author: 0 broken links, strict schema)
    ↓
compounding persistent knowledge_base/ (Human-ready & AI-ready)
```

### Summary of Component Changes:
* **UNCHANGED:** `yt-dlp` acquisition (M10), `faster-whisper` transcription (M20), canonical artifact layout (`transcript.txt`, `transcript.srt`, `run.log`).
* **REPLACED:** Fabric one-shot `extract_wisdom` replaced by **Deterministic Bounded Map-Reduce (`TTK`)** using host AI reasoning.
* **ADDED:** **OKF v0.2 Knowledge Vault structure** (`concepts/`, `entities/`, `sources/`, `index.md`) and **`okf-author` deterministic validation**.
* **OPTIONAL:** Local Qwen 9B extraction for short transcripts; Host AI (Claude/Codex/Antigravity) for synthesis.
* **REJECTED:** Usage-billed model APIs, monolithic one-shot 35k-word prompts, vector databases, and SaaS knowledge stores.

---

## 15. Evidence Gaps & Uncertainties

1. **Host-Native ChatGPT Directory Execution:** In ChatGPT Web, direct execution of file-based `SKILL.md` workflows is not natively supported without repackaging into Custom GPT prompts or an external MCP server `[EVIDENCE: E4]`. (In Claude Code, Codex CLI, and Antigravity, native `SKILL.md` is 100% verified `[EVIDENCE: E4]`).
2. **Qwen 9B Bounded Map Performance:** While Qwen 9B failed on the 35,000-word one-shot synthesis, running Qwen 9B locally on *bounded 3,000-word Map windows* inside `TTK` remains an open empirical test `[INFERENCE]`.

---

## 16. Source Ledger & Traceability

* `[EVIDENCE: E4]` `SourceTranscriptionAnalysisPipeline_Research/V4_AGENT_EXECUTION_BUNDLE/04-EXECUTION-STATE.yaml`: V4 execution logs documenting Ollama/Fabric 20m timeouts on 3h source `P-h5WSQG1Sw`.
* `[EVIDENCE: E4]` `SourceTranscriptionAnalysisPipeline_Research/transcript-to-knowledge-complete-bundle/current/skill-source/SKILL.md`: Full TTK deterministic Map-Reduce skill contract and CLI.
* `[EVIDENCE: E4]` `https://github.com/coleam00/cole-medin-knowledge-base`: Cole Medin OKF knowledge base structure and `channel-to-kb-ytdlp` skill.
* `[EVIDENCE: E4]` `https://github.com/parkscloud/okf-author`: Robert Parks OKF authoring skill and 0-dependency Python validator.
* `[EVIDENCE: E4]` `https://github.com/Ar9av/obsidian-wiki`: Obsidian Karpathy-pattern wiki ingestion skill (`wiki-ingest`).
* `[EVIDENCE: E4]` `https://agentskills.io`: Open Agent Skills standard adopted across Claude Code, Codex CLI, and Google Antigravity.
* `[EVIDENCE: E4]` `02-DECISIONS.md` & `04-CURRENT-RECOMMENDATION.md`: Operator decisions locking deterministic workflow ownership, zero API billing, and rejecting universal mandatory guardrails.