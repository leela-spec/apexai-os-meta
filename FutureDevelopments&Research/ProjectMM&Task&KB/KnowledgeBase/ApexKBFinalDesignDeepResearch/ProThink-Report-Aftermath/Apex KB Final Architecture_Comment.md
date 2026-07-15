# Apex KB Final Architecture — Research Export

[Download the complete decision-ready research report](sandbox:/mnt/data/Apex_KB_Final_Architecture_Deep_Research_Report.md)

The Markdown export is approximately **251 KB across 3,244 lines**. It contains the complete Target Lock, verified lifecycle map, seven priority-ordered module reports, configuration strategy, orchestration design, exact final tree, file-by-file design records, migration plan, cost audit, acceptance model, source register, confidence analysis, and technical probes. It contains implementation guidance rather than repository patches or finished scripts.

## Executive result

The research ran in **Mode A — `full_repository_evidence`**. The package, current Apex KB implementation, LLM-Wiki blueprints, compiled orchestration knowledge, and current primary documentation were all accessible. The latest `main` commit remained:

`bc353b7f16d2c5ad74f376452ad4c1ff45278995`  
`Reorganize Apex KB research corpus and sync orchestration docs`

The final architecture is not a larger wiki generator. It is a **lossless knowledge-compilation system with two equally important durable products**:

|Durable product|Purpose|
|---|---|
|**Concept dossier**|Explains each concept at Macro, Meso, and Micro levels, including current state, evolution, implementation reality, contradictions, uncertainty, and evidence.|
|**Source atlas**|Preserves the complete documentary landscape: every candidate file, its individual contribution, lifecycle role, disposition, authority/freshness assessment, relationships, review coverage, blockers, and exact evidence locations.|

This directly implements the package mission that future AIs should gain both compiled knowledge and a complete map of where that knowledge came from.

## Decisive current-state finding

The live system’s central defect is now verified directly in code:

- `rank_topic_sources()` performs lowercase, line-level substring counting.
    
- It does not preserve filename, path, title, H1, heading, body, link, or co-occurrence evidence separately.
    
- It returns only `file_hits[:30]`.
    
- Therefore, semantic safeguards operate on a candidate universe that may already have lost relevant sources.
    

The current `phase0-navigation-report.md` generator reinforces the problem: it lists artifact names and the deterministic/semantic boundary but provides no actual concept-specific reading guidance, duplicate/version families, blockers, source classes, or batch plan.

The report therefore ranks the highest-value corrections as:

1. field-separated deterministic postings;
    
2. exhaustive, non-truncated topic maps;
    
3. durable source atlases;
    
4. map/atlas completeness and faithfulness acceptance;
    
5. artifact dependency and impact analysis;
    
6. atlas-row-aware retrieval; and
    
7. automated fixtures and real-corpus canaries.
    

## Final architecture decisions

### Deterministic corpus intelligence

The final Phase 0 produces:

- one exhaustive source inventory;
    
- pointer-stable structure records;
    
- configured term and phrase postings;
    
- exact and normalized duplicate evidence;
    
- possible version-family evidence;
    
- a configurable Apex relationship/process graph;
    
- one exhaustive JSON topic map per configured concept;
    
- one compact Markdown projection per concept; and
    
- a populated multi-topic navigation and batch-planning report.
    

The canonical topic map is never top-N truncated. Bounded views remain allowed because they point back to and disclose the exhaustive set.

### Semantic compilation

Reusable source meaning moves to:

`ingest-analysis/sources/<hash-prefix>/<sha256>.analysis.md`

Topic-specific meaning moves to:

`ingest-analysis/topics/<topic-id>.analysis.json`

The latter contains exactly one semantic row for every deterministic candidate. It separately represents:

- **lifecycle role:** current, historical, prototype, implementation, contextual, or unknown;
    
- **disposition:** core, supporting, duplicate, superseded, incidental, blocked, or irrelevant-after-review.
    

The source atlas is rendered deterministically from that canonical topic record. It is not separately hand-authored, preventing semantic drift.

This preserves LLM-Wiki’s strongest compounding mechanism—sources update persistent concept knowledge rather than being re-retrieved on every query—while adding the exhaustive source-landscape capability missing from the blueprints. LLM-Wiki’s multi-page ingest behavior and index-first query model are retained and adapted rather than copied wholesale.

### Four-layer acceptance

A topic becomes accepted only when all required layers pass:

1. **Deterministic integrity:** scope, inventory, extraction, map, topic-row, atlas, pointer, dependency, and hash closure.
    
2. **Page-only answerability:** critical and routine target questions answered from compiled pages.
    
3. **Material-claim entailment:** critical claims supported, labeled inference/operator decision, or explicitly blocked.
    
4. **Atlas completeness and faithfulness:** every deterministic candidate retained with an accurate individual account.
    

Retrieval readiness is a separate final state requiring fresh indexes over the accepted input hashes.

### Incremental maintenance

A dependency map connects:

```text
source
-> extraction and topic-map rows
-> source capsule
-> topic semantic row
-> dossier claims and atlas rows
-> acceptance cases
-> retrieval chunks
```

A changed source therefore invalidates only its transitive impact closure. An unchanged hash reuses its capsule. A new path containing an existing hash updates source aliases and atlas rows without rereading the content.

### Retrieval

The current retrieval foundation is retained:

- compiled-page-only indexing;
    
- heading-based chunks;
    
- input hashes and stale checks;
    
- runtime-probed SQLite FTS5/BM25; and
    
- unconditional JSON fallback.
    

The final change is to index **source-atlas rows as first-class chunks**, allowing future AIs to answer both:

- “What is this concept?”
    
- “Which files discuss it, and what does each file contribute?”
    

SQLite remains derived rather than authoritative, and JSON remains the portable baseline. Atlas-aware lexical retrieval is implemented before any vector mechanism is considered.

### Package and runtime

The final package uses:

- a compact `SKILL.md` router;
    
- seven focused canonical reference contracts;
    
- machine schemas with one owner each;
    
- small templates that do not duplicate contracts;
    
- stable public CLI wrappers;
    
- a modular `apex_kb_runtime/` implementation package; and
    
- an automated test suite with synthetic fixtures and real-corpus canaries.
    

This follows the evidence that canonical schema definitions should exist once and long-running workflow state should be owned by scripts/files rather than model context.

## Codex and ChatGPT web orchestration

The accepted operating split is:

```text
Operator selects scope/profile once
-> Codex runs deterministic mapping
-> Codex generates one bounded semantic task packet
-> ChatGPT web reads evidence and returns an authored artifact bundle
-> Codex validates and imports declared paths
-> independent semantic context performs required acceptance
-> Codex rebuilds retrieval and performs Git operations
-> next coherent saved batch
```

The design does not pretend that the current ChatGPT GitHub app can write to the repository. Current official behavior is read-only for repository analysis, while Codex is the Git-capable execution and review surface. ([OpenAI Help Center](https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt "https://help.openai.com/en/articles/11145903-connecting-github-to-chatgpt")) ([OpenAI Developers](https://developers.openai.com/codex/cloud "https://developers.openai.com/codex/cloud"))

A direct write-capable MCP or app bridge remains `requires_evidence_probe`. It is not needed for the architecture to function.

## Main removals and consolidations

The report recommends:

- removing the already-deprecated lifecycle-state file after migration;
    
- replacing the all-purpose semantic ledger with source capsules, topic records, and a small run manifest;
    
- merging the separate query-evaluation truth into the topic registry and acceptance artifact;
    
- consolidating overlapping lifecycle, command, semantic, and query contracts;
    
- removing two unexecuted generic repository-lint specifications from the Apex KB package;
    
- replacing split heading/link/frontmatter truths with one canonical structure map;
    
- making per-source summary and entity pages conditional on recurring query value;
    
- replacing whole-wiki semantic lint with impact-bounded review by default; and
    
- rejecting static-site builders, Obsidian, miscellaneous corpus-statistics dependencies, and generic checkpoint bureaucracy as core requirements.
    

## Technical probes that remain

The architecture is complete; these probes select implementations or defaults inside it:

- actual operator Python/test/CI environment;
    
- DOCX, PPTX, XLSX, PDF, OCR, and visual-pointer fidelity;
    
- graph-only candidate and dependency yield;
    
- large-topic JSON authoring and atlas partition thresholds;
    
- real token savings and capsule-reuse ratios;
    
- direct write-capable MCP/app feasibility;
    
- incremental-impact precision on real changes; and
    
- evidence of material lexical retrieval failures before considering vectors.
    

## Evidence provenance

The uploaded Project Source material was used as corroborating research/snapshot evidence, while current implementation conclusions were grounded in the live repository. Source-access and prompt guidance were cross-checked against the uploaded materials.

Architecture, failure, lifecycle, and handoff evidence included the prepared plans and decision reports.

Blueprint and source-routing evidence included the human and machine-readable indexes, LLM-Wiki capability work, and repository guide.

Tooling, retrieval, implementation-plan, feedback, and feasibility snapshots were treated as historical or supporting evidence according to their stated limitations.

**Final export:** [Apex_KB_Final_Architecture_Deep_Research_Report.md](sandbox:/mnt/data/Apex_KB_Final_Architecture_Deep_Research_Report.md)