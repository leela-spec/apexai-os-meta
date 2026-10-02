---
type: Research
title: Research handover — adaptive extraction-schema selection for LangExtract
status: open question, not started
created: 2026-09-30
---

# Problem

LangExtract (google/langextract) requires the caller to supply `prompt_description` +
few-shot `ExampleData` up front — it has no built-in way to decide what's worth extracting
from an arbitrary document. A medical interview and an investment-research call need
different extraction categories. The operator wants this chosen **automatically per
document/domain**, and wants the choice to **improve/accumulate over time** rather than
being re-derived from scratch on every single file, without assuming there's one clean
off-the-shelf product for this — verify first.

# What this conversation already ruled in/out (2026-09-30 research pass)

No single established tool does "auto-detect what to extract + learn across domains over
time." Confirmed findings, each independently real:

| Piece | What it actually is | What it does NOT do |
|---|---|---|
| **DSPy** (stanfordnlp/dspy) | Real, maintained. `BootstrapFewShot`/`MIPROv2` optimize few-shot examples/instructions for a *fixed* task | Needs a `trainset` + a metric function to know what "correct" looks like — cannot discover the category labels themselves from raw documents |
| **GLiNER2** (fastino-ai/GLiNER2) | Real, maintained, zero-shot — give it a list of label *strings* (no full examples) and it extracts matching spans locally, no API cost | Still needs someone/something to name the labels first; no documented pairing with LangExtract anywhere |
| **OntoGPT/SPIRES**, **AutoSchemaKG** | Real, installable OSS for LLM-driven schema/ontology induction | Narrow/research-stage, not wired to LangExtract, not "accumulates over time" out of the box |
| **KATE** (Liu et al. 2021) | Real, cited, foundational technique: embed past (input → good examples) pairs, retrieve k-nearest for a new input | An algorithm, not a packaged library — someone has to implement the embed/store/retrieve loop |
| **langextract-rs `suggest-schema`** | Real, working, *unofficial* third-party (Rust) reimplementation with a one-shot "LLM drafts a YAML schema from sample files" command | Exactly the "ask once, no persistence" pattern — not iterative, not official Google |

Bottom line from that research pass: *"If this were built, it would be a genuine assembly:
GLiNER2 (cheap candidate labels) → LLM one-shot schema drafting → KATE-style retrieval to
reuse schemas across similar future documents → LangExtract for final grounded extraction."*
Nobody has published that pipeline as one tool.

# Pragmatic default already in the parent plan (not a final answer — a placeholder)

The main plan (`Transcription2KnowledgeBase` in this same folder) currently just does the
cheapest real option: one LLM call reads the transcript and drafts a schema fresh, every
single run, no memory of past runs. This works but never gets smarter and re-spends effort
on domains it's already seen (e.g. a second Long-COVID interview re-derives the same
"diagnostic_test_statement" category from nothing).

# What a fresh chat should actually investigate

1. **Is a QMD-backed schema library the right lightweight fix, or overkill?** This repo
   already has QMD (hybrid BM25+vector search over Markdown) running for the Obsidian vault
   (`apex-meta/SmallSkills/QMD/`). A candidate cheap design: store each domain's *proven*
   schema (categories + examples that worked) as its own small Markdown file with minimal
   frontmatter (per `apex-meta/AI-Snippets/AIFailure/AI-Failure-RAG-Metadata-Overengineering.md`
   — do not violate that doctrine here either), and before drafting a fresh schema, query
   QMD for the closest existing schema profile by the transcript's title/topic. If a good
   match exists, reuse/extend it instead of drafting blind. This is literally the KATE
   pattern, implemented with a tool already present in this environment instead of a new
   vector store. **Verify this is actually sound before building it** — check whether QMD's
   embedding model (`embeddinggemma-300M`) is good enough at distinguishing "medical
   interview about Long COVID" from "medical interview about a different condition" at the
   granularity needed, or whether that's too coarse and would misfire.
2. **Is GLiNER2 worth adding as a real cost/quality lever?** It's free, local, zero-shot,
   and could plausibly run as a cheap first pass to propose candidate labels before the LLM
   schema-drafting call, cutting one LLM round-trip per document. Check actual local-CPU/GPU
   feasibility on the operator's WSL2 "Apex" host before recommending it — this needs a real
   benchmark, not an assumption.
3. **Does this even need solving now, or later?** The operator's first real test case is a
   single domain (Long COVID / ME/CFS interviews) — confirm whether "adaptive per-domain
   schema selection" is in scope for a v1, or whether v1 should ship with the dumb
   draft-every-time default and this becomes a v2 concern once there's evidence multiple
   domains are actually in regular use.
4. Do **not** re-litigate whether LangExtract itself is the right extraction engine — that
   was already decided (see `04-CURRENT-RECOMMENDATION.md` in
   `SourceTranscriptionAnalysisPipeline_Research/current-decision-workspace/` and this
   conversation's own research). This handover is scoped strictly to the schema-selection
   sub-problem, not the extraction engine choice.

# Related files

- `Transcription2KnowledgeBase/` (this folder) — the parent plan this sub-problem belongs to.
- `apex-meta/SmallSkills/QMD/QMD-Knowledge-Base-And-Failure-Modes.md` — QMD's real capabilities/limits.
- `apex-meta/AI-Snippets/AIFailure/AI-Failure-RAG-Metadata-Overengineering.md` — the frontmatter/schema doctrine any solution here must respect.
- `SourceTranscriptionAnalysisPipeline_Research/current-decision-workspace/` — the repo's own prior (unrelated to this sub-problem, but same parent project) decision authority.
