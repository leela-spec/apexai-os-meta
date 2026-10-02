# QMD: Operational Architecture & Retrieval Learnings

- **Skill**: `SmallSkills/QMD`
- **Component**: `@tobilu/qmd` (Query Markdown by Tobi Lütke)
- **Domain**: On-device RAG, AI Agent Memory, Semantic & Keyword Retrieval
- **Status**: Active Standard

---

## 1. Engine Architecture: How QMD Works

QMD is an offline, privacy-first search engine designed to give AI agents (Hermes, Claude, Antigravity) long-term retrieval over Markdown files.

Unlike traditional naive vector databases or pure keyword search, QMD runs a **5-stage hybrid pipeline**:

```
[User / Agent Query]
        │
        ▼
1. Query Expansion (Synonyms, intent terms)
        │
        ├─────────────────────────────┐
        ▼                             ▼
2a. BM25 Keyword Search      2b. Vector Semantic Search
    (Exact term matches)          (embeddinggemma-300M-Q8_0.gguf)
        │                             │
        └──────────────┬──────────────┘
                       ▼
3. Reciprocal Rank Fusion (RRF)
   (Blends keyword + vector rankings without arbitrary weight tuning)
                       │
                       ▼
4. LLM Cross-Encoder Reranker
   (qwen2.5-coder-7b evaluates top candidate passages against query)
                       │
                       ▼
5. Context Tree Integration (qmd context add)
   (Pre-filters or biases search based on collection intent)
```

---

## 2. Standard Operational CLI Commands

```bash
# Register a folder as a searchable collection
qmd collection add "<path>" --name <collection-name>

# Add collection context (creates the context tree for agent routing)
qmd context add qmd://<collection-name> "Description of the collection's domain, purpose, and content."

# Generate / update vector embeddings
qmd embed

# Run hybrid search with LLM reranking (primary method for agents)
qmd query "how to structure a 60 second talking head video intro"

# Run exact keyword search (BM25 only)
qmd search "Conflict Resolution Fit"

# Run semantic vector search (vector similarity only)
qmd vsearch "why content is important for solo businesses"

# Refresh index after adding or modifying Markdown notes
qmd update
```

---

## 3. The Failure Mode: Metadata Over-Engineering in RAG

### The Trap
When AI assistants or developers design a knowledge base for RAG, they frequently default to "relational database thinking" — creating schemas with 10–15 strict categorical frontmatter variables:
```yaml
# ❌ OVER-ENGINEERED ANTI-PATTERN
---
persona: solo_entrepreneur
funnel_stage: top_of_funnel
framework_type: structural
target_metric: retention
content_pillar: thought_leadership
tone_voice: empathetic_analytical
target_format: short_form_video
min_duration_seconds: 45
max_duration_seconds: 60
reading_level: intermediate
---
```

### Why This Fails in Practice

1. **The Over-Filtering Blindspot**:
   If an AI is asked to *"write a client acquisition post for a business consultant"*, an agent applying rigid filters will skip high-impact frameworks simply because they were tagged `persona: solo_freelancer` or `funnel_stage: retention`. Real creative insights cross boundaries; rigid taxonomies create artificial retrieval silos.

2. **Vector Dilution (Noise in Embeddings)**:
   Embedding models (such as `embeddinggemma-300M`) encode the actual token string of the document chunk. When 25–40% of the chunk consists of bureaucratic YAML metadata, the resulting vector moves toward the *taxonomy schema* rather than the *creative insight, psychology, or formula*.

3. **Engine Mismatch**:
   QMD is **not** an SQL database executing `WHERE` clauses on frontmatter. It is a text-based hybrid retriever (BM25 + Semantic Vector + Reranker). Stuffing frontmatter with artificial variables fights the engine's core strength.

---

## 4. The Lean Best-Practice Standard

### The 3–4 Field Frontmatter Standard
Keep frontmatter strictly limited to broad, natural metadata:
```yaml
---
title: "Conflict-Resolution-Fit Storytelling Framework"
summary: "A 3-step personal story structure for solo entrepreneurs to build trust and authority."
tags: [storytelling, personal-brand, trust, client-journey]
source: "Tyson Video Creation Sprint"
---
```

### Let Headings and Prose Do the Work
- **Heading Hierarchy (`#`, `##`, `###`)**: QMD uses Markdown headings as natural semantic split points and context anchors.
- **Explain the "Why" and provide concrete examples in plain text**: Clear prose gives the embedding model and BM25 rich tokens to match against.
- **Include explicit AI Prompt Directives**: A short section at the end of each note stating: *"When prompting an AI to use this, instruct it to..."* turns the retrieved note directly into a few-shot generation template.
