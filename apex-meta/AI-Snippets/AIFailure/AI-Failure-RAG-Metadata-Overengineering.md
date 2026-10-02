# AI Failure Mode: RAG Knowledge Base Metadata Over-Engineering

- **ID**: `AIF-RAG-001`
- **Category**: Over-Engineering / Architecture Drift / RAG Failure Modes
- **Observed Date**: 2026-09-22
- **Related Doctrine**: `apex-meta/AI-Snippets/Snippets.md` (Anti-Drift / Minimalism Rule), `apex-meta/SmallSkills/QMD/`

---

## 1. Description of the Failure
When tasked with designing a knowledge base for content creation and AI retrieval (via QMD), the AI assistant generated an overly complex, 12-variable YAML frontmatter taxonomy:
- Rigid variables included: `type`, `category`, `platform`, `target_stage`, `persona`, `framework_type`, `tone_voice`, `metrics`.

The human operator correctly intervened:
> *"I wonder if what you have given me with the different standard YAML front matter is over-engineering and has the potential for an AI to not read sources because of a small variable that has been over-limited... As soon as something like that is not the case, an AI has no reason to not read through that. They don't necessarily help the AI, they confuse the AI because they have to think of so many variables instead of just thinking of the actual content and intent."*

Research into RAG architectures and empirical testing confirms the operator's diagnosis 100%.

---

## 2. Root Cause Analysis

### A. The "Relational Database" Bias in LLMs
LLMs tend to mimic enterprise database schemas (SQL/CRM patterns) when asked to organize information. However, modern RAG systems (and specifically QMD) do not operate as relational query engines; they operate on **natural language semantic similarity and lexical frequency (BM25)**.

### B. The Over-Filtering Blindspot
When an AI agent is instructed to filter by rigid metadata fields (e.g., `persona: solo_entrepreneur`), any query that uses slightly different terminology (e.g., *"give me a framework for boutique agency founders"*) risks completely excluding relevant documents due to strict schema mismatches.

### C. Vector Dilution
Small local embedding models (like Gemma 300M in QMD) calculate embeddings across all tokens in a chunk. Excessive frontmatter fills the context window with repetitive schema syntax, diluting the high-signal prose of the actual tip or framework.

---

## 3. Verified Corrective Doctrine

1. **Frontmatter Minimalism**: Restrict YAML frontmatter to a maximum of 3–4 natural fields:
   - `title`: Human-readable title
   - `summary`: One clear sentence describing the core mechanism
   - `tags`: 3–5 loose semantic keywords
   - `source`: Attribution or origin (optional)

2. **Heading-Anchored Structure**:
   Use standard Markdown headings (`#`, `##`, `###`) to create semantic chunk boundaries. Headings provide explicit structural context without metadata noise.

3. **Content Over Taxonomy**:
   Spend token budget on explaining the *mechanism* (why the tip works) and providing *concrete examples* (few-shot swipes). That is what embedding models match and what generative LLMs need to produce high-quality output.

---

## 4. Cross-Reference
- Operational Runbook: [`apex-meta/SmallSkills/QMD/00_README.md`](../SmallSkills/QMD/00_README.md)
- QMD Full Guide: [`apex-meta/SmallSkills/QMD/QMD-Knowledge-Base-And-Failure-Modes.md`](../SmallSkills/QMD/QMD-Knowledge-Base-And-Failure-Modes.md)
