# Apex KB — prompt/task-template design notes (A0)

**Purpose.** Evidence-based patterns for the hardcoded Phase 1 / Phase 2 task prompts the CLI hands to the semantic worker, so the compiled pages are rich (pointers, cross-links, depth) instead of the schema minimum. This is the design that packet **A1** applies to `templates/phase1-task.md`, `templates/phase2-task.md`, and the injected contracts in `semantic/engine.py`. Sources are local-first; no private content leaves the machine.

## Problem the notes fix (from the audit)
The old prompts named *which* sections to produce but never *how much*. Result: a dossier ranked-source carried **1** pointer while Phase 1 had preserved **9**; "Key claims" had **3** bullets while capsules held ~**21**. The schema floors (`minItems:1`) let the worker stop at the minimum. Richness must be demanded by the prompt **and** enforced by the schema (A2).

## Patterns extracted

### 1. Pointer coverage — "carry ALL, not a sample"
- **Evidence:** the audit's 1-of-9 drop; llm-wiki's model treats immutable raw sources as the citation substrate and expects the wiki to point back to them (`source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md`).
- **Template language:** *"For every ranked source, include **every** pointer Phase 1 preserved for it — not a representative sample. Every direct answer must cite **all** supporting pointers."*

### 2. Cross-linking / indexing — the wiki is a graph, not a folder
- **Evidence:** llm-wiki: *"a single source might touch 10–15 pages"*; llm-wiki-main `workflows/ingest.md` regenerates `index.md` and cross-links concept/entity pages; llm-wiki-skill-main query follows one hop of wikilinks. Apex today has **no** cross-link field.
- **Template language:** *"List every related topic/page and the relationship (e.g. 'theory feeds the match map'). Emit these as links."* Pairs with the new `related_pages` field (A3).

### 3. Per-source summaries + depth
- **Evidence:** llm-wiki-skill-main **requires** `wiki/summaries/<slug>.md` per source; its dossiers are 400–1200 words. Apex's Macro/Meso/Micro currently accept one sentence.
- **Template language:** *"Write Macro/Meso/Micro as substantive paragraphs (≥3 sentences each) that stand on their own."* (Chunk-standalone rationale mirrors Anthropic **Contextual Retrieval**, anthropic.com/news/contextual-retrieval, 2024 — each unit should carry enough context to be understood alone.)

### 4. Enumerate every material claim
- **Evidence:** capsules held ~21 claim statements; dossier emitted 3.
- **Template language:** *"Enumerate **every** material key claim the sources support, each with its evidence state and all citations — do not summarize to a token few."*

### 5. Contradiction / uncertainty callouts on both sides
- **Evidence:** llm-wiki-main flags contradictions on both pages + a `review.json` queue; llm-wiki-skill-main has an anchored audit loop.
- **Template language:** keep Apex's contradictions/uncertainty/open-questions sections but require them to be **populated when the sources warrant**, not left empty.

### 6. Evidence-first, refuse beyond evidence
- Keep Apex's existing strength (non-diagnosis boundaries, reopen triggers). Instruct: *"Never assert beyond the cited evidence; mark low-confidence and open items explicitly."*

## Ready-to-paste template language (A1 applies these)
- **Phase 1 add:** *"For every source you open, record **all** material line pointers (not a sample) and **every** distinct key claim it supports. Answer each locked question completely and cite every supporting pointer."*
- **Phase 2 add:** *"Each ranked source must carry **all** pointers Phase 1 preserved for it. Enumerate **every** material key claim. Each direct answer cites every supporting pointer. Write Macro/Meso/Micro as ≥3-sentence paragraphs. Add a Related-pages section linking every related topic with its relationship. Populate contradictions/uncertainty/open-questions whenever the sources warrant."*

## Sources
- Local: `source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md`, `.../llm-wiki-main/{README.md,workflows/ingest.md,WIKI_SCHEMA.md}`, `.../llm-wiki-skill-main/{SKILL.md,references/schema-guide.md}` (v0.1.0 snapshots).
- Public: Anthropic, "Introducing Contextual Retrieval," anthropic.com/news/contextual-retrieval (accessed 2026-07-24) — chunk-standalone context principle. VectifyAI/OpenKB and AsyncFuncAI/deepwiki-open (interlinked concept/entity pages with citations) as corroborating design references.
