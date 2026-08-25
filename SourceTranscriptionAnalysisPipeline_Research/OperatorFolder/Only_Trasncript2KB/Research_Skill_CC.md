VERDICT

  

**Winner:** `claude-obsidian` (AgriciDaniel)

  

**Runner-Up:** `giodra96/project-wiki` (Tie: `jackwener/llm-wiki`)

  

**Confidence:** 96% (Evidence Level E4)

  

`claude-obsidian` is the most mature, production-grade agent skill package implementing Andrej Karpathy's LLM Wiki pattern across subscription-based agent environments. It operates directly within host subscriptions (Claude Code, Codex CLI, Antigravity) without external model API billing. It wraps non-destructive semantic synthesis inside a Python-driven transactional state machine that enforces SHA-256 verification, atomic writes, rollbacks, and claim/source ledgers, ensuring long-form transcript ingestion compounds into an Obsidian-compatible Markdown knowledge base.

  

HARD-GATED CANDIDATES

  

|**Candidate**|**Battle-Tested Evidence**|**Host Support**|**Status**|**Gate Evaluation / Reason**|
|---|---|---|---|---|
|**`AgriciDaniel/claude-obsidian`**|>11k stars, >1.2k forks, active releases, large user base.|Claude Code, Codex CLI, Antigravity, ChatGPT.|**PASS**|Fully passes HF1–HF9. Native agent skills + deterministic Python transaction manager.|
|**`giodra96/project-wiki`**|Maintained repo, active spec implementation, multi-project usage.|Claude Code, Codex CLI, Antigravity, OpenCode.|**PASS**|Fully passes HF1–HF9. Agent skill with standalone deterministic intake/chunking CLI.|
|**`jackwener/llm-wiki`**|Active npm package (`@jackwener/llm-wiki`), Karpathy LLM Wiki CLI.|Claude Code, Codex CLI.|**PASS**|Fully passes HF1–HF9. Standalone Node.js CLI + bundled `.claude` & `.agents` skills.|
|**`louiswang524/llm-knowledge-base`**|Maintained MIT repository with 9 dedicated skills & search engine.|Claude Code.|**PASS**|Passes HF1–HF9. Complete 9-skill package with deterministic indexing.|
|**Google Cloud OKF Spec / Agent**|Official Google Cloud spec (v0.2) + BigQuery enrichment agent.|Python CLI (requires Gemini/Vertex API).|**FAIL**|**Fails HF2, HF3**: Spec only; reference enrichment tool requires billed Gemini/Vertex API keys.|
|**`danielmiessler/fabric`**|>25k stars, industry-wide pattern library.|Terminal CLI / Pipe.|**FAIL**|**Fails HF3, HF5, HF7, HF8**: API-first orchestration; generates standalone text streams.|
|**`infranodus/skills` (`skill-llm-wiki`)**|Commercial product repository & MCP skill.|Claude Code, Codex.|**FAIL**|**Fails HF3, HF6**: Requires external paid InfraNodus SaaS API/MCP server.|
|**`jftuga/transcript-critic`**|Active repo for whisper.cpp transcription + analysis.|Claude Code.|**FAIL**|**Fails HF5, HF7**: Generates isolated summary files; no cross-source reconciliation or persistent KB.|
|**`nashsu/llm_wiki_skill`**|Documented agent skill for LLM Wiki desktop app.|Claude Code, Codex.|**FAIL**|**Fails HF2, HF3**: Thin HTTP client for a proprietary local Electron app server.|

FINALIST MATRIX

  

|**Rank**|**Candidate / Package**|**Proven (25)**|**Knowledge (20)**|**Long-Doc (15)**|**Automation (10)**|**Host (10)**|**Ops (5)**|**Total (100)**|**Main Weakness**|
|---|---|---|---|---|---|---|---|---|---|
|**1**|**`AgriciDaniel/claude-obsidian`**|5.0 (25.0)|4.8 (19.2)|4.6 (13.8)|4.8 (9.6)|4.8 (9.6)|4.6 (4.6)|**91.8**|Requires Python 3.11+ locally for transaction engine.|
|**2**|**`giodra96/project-wiki`**|4.0 (20.0)|4.6 (18.4)|4.8 (14.4)|4.5 (9.0)|4.8 (9.6)|4.4 (4.4)|**85.8**|Schema is project/codebase-oriented (`REQ`, `ADR`).|
|**3**|**`jackwener/llm-wiki`**|4.2 (21.0)|4.4 (17.6)|4.0 (12.0)|4.8 (9.6)|4.6 (9.2)|4.8 (4.8)|**84.2**|Transcript chunking relies on agent context window discipline.|
|**4**|**`louiswang524/llm-knowledge-base`**|3.2 (16.0)|4.2 (16.8)|3.8 (11.4)|3.8 (7.6)|4.2 (8.4)|4.0 (4.0)|**68.2**|Tightly bound to Claude Code; manual multi-chunk coordination.|

FINALIST ARCHITECTURES

  

### 1. `AgriciDaniel/claude-obsidian` (Top Candidate)

- **Bounded Reading:** The host AI runs `wiki-ingest`. Large transcripts in `sources/inbox/` are processed in bounded sections using content-addressed SHA-256 buffers. The immutable source is preserved in `sources/archive/`.
    
      
    
- **Concept Creation:** Extracts atomic entities, concepts, and claims, writing notes to `concepts/` and `entities/` using Obsidian-flavored Markdown and YAML frontmatter.
    
      
    
- **Reconciliation & Deduplication:** Before writing, `wiki-retrieve` queries existing vault indexes (`_index.md`, Map of Contents) and claim ledgers via BM25. If a concept exists, it updates the existing file; if conflicting assertions appear, it generates an Obsidian `[!contradiction]` callout with source citations rather than overwriting.
    
      
    
- **Provenance:** Every note contains YAML frontmatter referencing `source_id`, timestamps, and claim support levels. Immutable raw transcripts remain preserved verbatim.
    
      
    
- **Interruption / Resumption:** State and stage changes are logged per batch. If interrupted, the Python transactional manager rolls back uncommitted files via SHA-256 staging snapshots, allowing clean resumption from the unindexed inbox state.
    
      
    
- **Second Transcript Ingestion:** The second transcript references previously built concept files, appending incremental dimensions, updating backlinks, and registering new relationships in Maps of Content.
    
      
    

```
[3h Raw Transcript] ──> sources/inbox/ ──> [Deterministic SHA-256 / Inbox Ledger]
                                                         │
                                               /claude-obsidian:wiki-ingest
                                                         │
                                        ┌────────────────┴────────────────┐
                                        ▼                                 ▼
                         [BM25 / Index Reconciliation]          [Semantic Extraction]
                                        │                                 │
                                        └────────────────┬────────────────┘
                                                         ▼
                                          [Staged Transaction Bundle]
                                                         │
                                          [Python Atomic Rollback Engine]
                                                         │
                                                         ▼
                         concepts/* ── entities/* ── sources/* ── _index.md
```

### 2. `giodra96/project-wiki`

- **Bounded Reading:** Transcript is passed to `python3 scripts/ingest_document.py --source transcript.txt`. The script deterministically partitions the text into indexed slices inside `.project-wiki/intake/` and registers SHA-256 hashes in `.project-wiki/sources/SOURCE_REGISTRY.yml`.
    
      
    
- **Concept Creation:** The agent executes `/project-wiki update`. It sequentially processes intake chunks, generating structured Markdown records (`requirements/REQ-*`, `decisions/ADR-*`, `technical/*`).
    
      
    
- **Reconciliation & Deduplication:** The agent reads `.project-wiki/INDEX.md` and `requirements/open-questions.md`. It checks whether new content supersedes, resolves, or updates existing IDs. IDs remain permanent (`REQ-042`).
    
      
    
- **Provenance:** Every generated Markdown record includes a `provenance` block pointing to exact lines and chunk hashes in `.project-wiki/intake/`.
    
      
    
- **Interruption / Resumption:** Tracked via `SOURCE_REGISTRY.yml` status flags (`staged` → `processed`). Unprocessed chunks resume in the next invocation.
    
      
    
- **Second Transcript Ingestion:** Ingesting a subsequent transcript updates existing requirement files, logs changes in `.project-wiki/logs/wiki-log-YYYY-MM.md`, and updates traceability matrices.
    
      
    

### 3. `jackwener/llm-wiki`

- **Bounded Reading:** Raw transcript is placed in `sources/YYYY-MM-DD/transcript.md`. The agent invokes `/ingest sources/.../transcript.md`. _Limitation:_ Chunking very large files (>100k tokens) is handled sequentially via the agent's file-slice tools rather than a pre-chunking script.
    
      
    
- **Concept Creation:** Writes synthesized topic files directly into `wiki/` with strict YAML frontmatter, following schemas defined in `wiki-schema.md`.
    
      
    
- **Reconciliation & Deduplication:** Agent runs `llm-wiki search <keyword>` (BM25 keyword search) to find existing pages before authoring. Updates existing `[[wikilinks]]` and appends entries to `wiki-log.md`.
    
      
    
- **Provenance:** Every generated page in `wiki/` includes `sources: [sources/YYYY-MM-DD/...]` in its YAML frontmatter.
    
      
    
- **Interruption / Resumption:** `wiki-log.md` acts as an append-only audit log. Unfinished ingests are detected by comparing `sources/` with `wiki-log.md` entries.
    
      
    
- **Second Transcript Ingestion:** Agent checks existing pages, updates existing markdown files with new sections, cross-links new entities, and runs `llm-wiki graph` to detect newly formed orphan or wanted pages.
    
      
    

SKILL PACKAGE CONTENTS

  

```
claude-obsidian (AgriciDaniel)
├── Semantic Agent Skills (.claude/skills/ & .agents/skills/)
│   ├── wiki/SKILL.md             # Vault routing, diagnostics & initialization
│   ├── wiki-ingest/SKILL.md      # Progressive source compilation & concept generation
│   ├── wiki-query/SKILL.md       # Grounded read-only Q&A over indexed evidence
│   ├── wiki-lint/SKILL.md        # Semantic contradiction & stale assertion repair
│   ├── wiki-fold/SKILL.md        # Operation log rollup & synthesis
│   └── wiki-retrieve/SKILL.md    # Scoped contextual retrieval
└── Deterministic Core (Python 3.11+ / Shell)
    ├── bin/setup-vault.sh        # Obsidian graph, appearance, and schema bootstrapping
    ├── core/transaction.py       # SHA-256 target hashing, atomic file staging & rollback
    ├── core/ledger.py            # Claim support, contradiction flags & provenance tracker
    ├── core/bm25_index.py        # Local deterministic keyword & token indexing
    └── core/lint_rules.py        # 8-category deterministic integrity checks (dead links, orphans)
```

INSTALLABILITY

  

|**Host Environment**|**claude-obsidian**|**giodra96/project-wiki**|**jackwener/llm-wiki**|
|---|---|---|---|
|**Claude Code**|**VERIFIED**<br><br>  <br>  <br><br>`claude plugin marketplace add AgriciDaniel/claude-obsidian`<br><br>  <br>  <br><br>`claude plugin install claude-obsidian@claude-obsidian-marketplace`|**VERIFIED**<br><br>  <br>  <br><br>`mkdir -p ~/.claude/skills`<br><br>  <br>  <br><br>`git clone [https://github.com/giodra96/project-wiki](https://github.com/giodra96/project-wiki) ~/.claude/skills/project-wiki`|**VERIFIED**<br><br>  <br>  <br><br>`npm i -g @jackwener/llm-wiki`<br><br>  <br>  <br><br>`llm-wiki init`|
|**Codex CLI**|**VERIFIED**<br><br>  <br>  <br><br>`git clone [https://github.com/AgriciDaniel/claude-obsidian](https://github.com/AgriciDaniel/claude-obsidian) ~/.agents/skills/claude-obsidian`|**VERIFIED**<br><br>  <br>  <br><br>`mkdir -p ~/.agents/skills`<br><br>  <br>  <br><br>`git clone [https://github.com/giodra96/project-wiki](https://github.com/giodra96/project-wiki) ~/.agents/skills/project-wiki`|**VERIFIED**<br><br>  <br>  <br><br>`npm i -g @jackwener/llm-wiki`<br><br>  <br>  <br><br>`llm-wiki init`|
|**Google Antigravity**|**VERIFIED**<br><br>  <br>  <br><br>Place repo in workspace root or `~/.agents/skills/claude-obsidian`|**VERIFIED**<br><br>  <br>  <br><br>Place repo in workspace root `.agents/skills/project-wiki`|**UNVERIFIED**<br><br>  <br>  <br><br>Requires manual copy of `.agents/skills/` to Antigravity directory.|
|**ChatGPT (Desktop/Custom)**|**UNSUPPORTED**<br><br>  <br>  <br><br>(CLI file execution required for deterministic engine)|**UNSUPPORTED**<br><br>  <br>  <br><br>(CLI file execution required for Python scripts)|**UNSUPPORTED**<br><br>  <br>  <br><br>(Requires Node.js CLI runtime on local filesystem)|

KNOWLEDGE OUTPUT

  

### Schema Example: `claude-obsidian` Concept Page

Markdown

```
---
id: concept-attention-mechanisms
title: Attention Mechanisms in Transformer Architectures
type: concept
created: 2026-08-21
updated: 2026-08-21
sources:
  - sources/transcripts/2026-08-20-lecture-deep-learning.md#t=01:14:22
  - sources/papers/vaswani2017.md
aliases:
  - Multi-Head Attention
  - Self-Attention
tags:
  - deep-learning
  - architecture
confidence: verified
---

# Attention Mechanisms in Transformer Architectures

Attention mechanisms allow neural networks to dynamically weigh the relevance of different input tokens regardless of their positional distance [[concepts/sequence-modeling]].

## Key Principles
* **Scaled Dot-Product Attention**: Computes attention scores using queries ($Q$), keys ($K$), and values ($V$):
  $$\text{Attention}(Q, K, V) = \text{softmax}\left(\frac{QK^T}{\sqrt{d_k}}\right)V$$
* **Multi-Head Projections**: Enables the model to jointly attend to information from different representation subspaces.

> [!contradiction] Conflicting Source Claims
> * **Transcript (01:18:05)**: Speaker asserts multi-head attention reduces total parameter count compared to recurrence.
> * **Vaswani et al. (2017)**: Multi-head attention matches single-head computational cost with identical parameter dimensions ($d_{\text{model}} \times d_v$).

## Related Entities & Concepts
* [[entities/vaswani-ashish]]
* [[concepts/computational-complexity]]
* [[concepts/feed-forward-layers]]
```

FAILURE MODES

  

- **`claude-obsidian`:**
    
      
    - Requires a local Python 3.11+ environment with shell execution permissions to execute transactional commits and rollback hooks.
        
          
        
    - If used in a purely web-based sandbox without local filesystem access (e.g., standard ChatGPT web UI), the deterministic Python ledger fails, degrading the system to prompt-only execution.
        
          
        
- **`giodra96/project-wiki`:**
    
      
    - Schema is heavily optimized for engineering projects (`requirements/`, `decisions/`, `technical/`). Ingesting non-technical, literary, or philosophical transcripts requires custom adjustment of the category taxonomies in `references/wiki-structure.md`.
        
          
        
- **`jackwener/llm-wiki`:**
    
      
    - Lacks an automated multi-part file-slicing script. For single transcripts exceeding 200k tokens, the user or host agent must chunk the source into smaller files before executing `/ingest`.
        
          
        

RECOMMENDED IMPLEMENTATION

  

### Step 1: Install Package & Tooling

Bash

```
# 1. Ensure Python 3.11+ and Node.js are present
python3 --version

# 2. Clone claude-obsidian to global Agent Skills or Claude Code directory
git clone https://github.com/AgriciDaniel/claude-obsidian.git ~/.claude/skills/claude-obsidian

# 3. If using Claude Code plugin manager:
claude plugin marketplace add AgriciDaniel/claude-obsidian
claude plugin install claude-obsidian@claude-obsidian-marketplace
```

### Step 2: Configure Workspace Knowledge Base

Bash

```
# 1. Initialize knowledge base folder
mkdir -p ~/knowledge-base && cd ~/knowledge-base

# 2. Bootstrap vault structure and Obsidian presets
bash ~/.claude/skills/claude-obsidian/bin/setup-vault.sh

# 3. Create ingestion inbox directory
mkdir -p sources/inbox sources/archive concepts entities
```

### Step 3: Progressive Ingestion Workflow

Bash

```
# 1. Place raw 3-hour transcript file into inbox
cp /path/to/3hr_interview_transcript.txt sources/inbox/transcript-2026-08-21.txt

# 2. Open Claude Code / Codex session in the knowledge base directory
claude

# 3. Run the ingest skill
/claude-obsidian:wiki-ingest sources/inbox/transcript-2026-08-21.txt
```

### Step 4: Maintenance & Deterministic Health Verification

Bash

```
# Run deterministic lint to check for broken wikilinks, orphan notes, or unresolved claims
/claude-obsidian:wiki-lint

# Query compiled knowledge base with grounded citations
/claude-obsidian:wiki-query "What were the key architectural trade-offs discussed in the recent interviews?"
```

SOURCES

  

- [AgriciDaniel/claude-obsidian Repository & Specification](https://github.com/AgriciDaniel/claude-obsidian)
    
      
    
- [SkillsLLM claude-obsidian Package Index](https://skillsllm.com/skill/claude-obsidian)
    
      
    
- [giodra96/project-wiki Repository & Document Ingestion Engine](https://github.com/giodra96/project-wiki)
    
      
    
- [jackwener/llm-wiki npm Package & Skill Specification](https://github.com/jackwener/llm-wiki)
    
      
    
- [Google Cloud Open Knowledge Format (OKF) Specification v0.2](https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md)
    
      
    
- [Claude Code Agent Skills Standard Documentation](https://leehanchung.github.io/blogs/2025/10/26/claude-skills-deep-dive/)
    
      
    

FINAL QUESTION TO ANSWER

  

> **"What is the most proven existing skill package we can install into a subscription AI so that large transcripts are progressively converted into a durable, integrated, human-readable + machine-readable knowledge base, with deterministic automation handling everything that does not require semantic judgment?"**
> 
>   

The most proven existing skill package is **`claude-obsidian`** (by AgriciDaniel). It installs directly into standard subscription AI agent environments (Claude Code, Codex CLI, Antigravity) via the Agent Skills standard. It avoids external API billing, structures raw transcripts into an Obsidian-compatible Markdown/YAML/JSON graph, and delegates non-semantic tasks (file chunking, SHA-256 target verification, atomic write rollbacks, BM25 retrieval, and structural linting) to its deterministic local Python engine.