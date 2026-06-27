# Pre-LLM Corpus Intelligence Research Report

## 1. Verdict

- **Is the target possible without LLM calls?** Yes. Most of the requested artifacts can be produced deterministically: file inventory, corpus profile, line/word/byte counts, heading map, frontmatter map, Markdown link map, wikilink graph, duplicate hashes, noise filters, keyword reports, and a local search index.
    
- **Is it broader than scripts/Python?** Yes. The strongest existing patterns come from documentation systems, Markdown processors, code-search tools, static-site search indexes, and repo-intelligence utilities—not just custom Python.
    
- **What category fits best?** A **local-first deterministic corpus profiler + Markdown structure mapper + lightweight search index builder**, optionally borrowing patterns from MkDocs/mdBook/Docusaurus/LLM-Wiki/Obsidian-style graph tools.
    
- **Should Apex KB add this before semantic bundle creation?** Yes. It should be added **before** LLM semantic ingest-analysis. This is exactly the layer that prevents the LLM from blindly rereading the entire corpus.
    

Apex already has the correct conceptual boundary: the project records define `apex_kb.py`/script contracts as deterministic helpers for scaffold, hashing, preflight, manifest checks, machine index generation, lint, and audit—not semantic synthesis. Semantic extraction, contradiction interpretation, page drafting, and query synthesis remain LLM-owned. The existing Apex KB test evidence also shows the installed `apex-kb` package can run scaffold/hash/preflight/manifest/index/lint/audit and produce a script-validated KB pipeline.

---

## 2. Best Real-World Patterns

|Pattern|Example implementation|What it gives Apex|Fit|
|---|---|---|---|
|Static docs search index|MkDocs / Material for MkDocs search index|`search-index.json`, local/offline search, document titles/text/locations|High|
|Local docs search plugin|Docusaurus local search plugins|Offline index for docs without external search service|Medium|
|mdBook generated search index|mdBook search index generation|Markdown book → generated searchable document corpus|Medium|
|Markdown AST processor|remark / unified|Deterministic heading/link/frontmatter extraction from Markdown ASTs|High|
|Frontmatter parser|gray-matter|YAML/TOML/JSON frontmatter map|High|
|Markdown link validator|markdown-link-validator / markdown-link-check|Relative links, anchors, external links, broken link detection|High|
|Obsidian-style vault graph|Obsidian vault graph tools|Wikilink graph, backlinks, orphan notes, hub notes|High|
|Fast recursive search|ripgrep + fd|File discovery, keyword reports, topic hints, fast source narrowing|High|
|Corpus/code stats|tokei / cloc|File type stats, line counts, language breakdown|High|
|Symbol/code map|Universal Ctags / tree-sitter|Code symbol maps if the KB contains scripts/repos|Medium|
|Local full-text index|SQLite FTS5 / Lunr / Tantivy|Deterministic keyword search index without embeddings/vector DB|Medium-high|
|Existing Apex KB pattern|`apex-kb` + LLM-Wiki-derived design|Source manifest, hashes, index-first query, lint/audit split|High|

MkDocs/Material explicitly ships a client-side search index to the browser and uses Lunr-style local search, avoiding a third-party search service. ([github.com](https://github.com/squidfunk/mkdocs-material/blob/master/docs/plugins/search.md?utm_source=chatgpt.com "mkdocs-material/docs/plugins/search.md at master - GitHub")) mdBook similarly has a build-time search-index pattern, where the build serializes corpus content for local browser search. ([DeepWiki](https://deepwiki.com/rust-lang/mdBook/4.4-search-functionality?utm_source=chatgpt.com "Search Functionality | rust-lang/mdBook | DeepWiki")) remark/unified is directly relevant because it parses Markdown into ASTs, making structural extraction—headings, links, lists, blocks—programmatic rather than LLM-dependent. ([github.com](https://github.com/remarkjs/remark?utm_source=chatgpt.com "GitHub - remarkjs/remark: markdown processor powered by plugins part of ..."))

---

## 3. Candidate Evidence

### Candidate: MkDocs / Material for MkDocs search plugin

- **Category:** static-site indexer / search index
    
- **Repository/docs:** Material for MkDocs search documentation.
    
- **Relevant implementation evidence:** The docs state that the search index is shipped to the browser and made queryable locally with Lunr; no third-party search service is required. ([github.com](https://github.com/squidfunk/mkdocs-material/blob/master/docs/plugins/search.md?utm_source=chatgpt.com "mkdocs-material/docs/plugins/search.md at master - GitHub"))
    
- **What it produces:** Search index over documentation pages, titles, text, and locations.
    
- **Why comparable:** Apex KB needs a local `search-index.json` so later LLM work can ask “which files mention X?” before reading full sources.
    
- **Adaptation for Apex:** Copy the pattern, not the whole static-site system. Generate `manifests/search-index.json` from Markdown/plain text.
    
- **Risks:** Search index is lexical, not semantic. That is acceptable for Phase 0/1.
    

**Apex fit:** High.  
**Effort:** Low-medium.  
**What to copy:** build-time local search index.  
**What not to copy:** full website theme/build pipeline.

---

### Candidate: Docusaurus local search plugins

- **Category:** static-site indexer / search index
    
- **Repository/docs:** `cmfcmf/docusaurus-search-local`, `easyops-cn/docusaurus-search-local`.
    
- **Relevant implementation evidence:** Public plugin descriptions emphasize offline/local search that works behind a firewall; one active fork supports Docusaurus v2/v3 and local indexing. ([github.com](https://github.com/cmfcmf/docusaurus-search-local?utm_source=chatgpt.com "Offline / Local Search for Docusaurus v3+ - GitHub"))
    
- **What it produces:** Local docs search index integrated into Docusaurus.
    
- **Why comparable:** Same pattern: deterministic build creates an index from a docs corpus before query-time use.
    
- **Adaptation for Apex:** Use as conceptual precedent for `search-index.json`; do not add Docusaurus.
    
- **Risks:** Node/Docusaurus stack is unnecessary for Apex V1.
    

**Apex fit:** Medium.  
**Effort:** Medium if copied directly; low if adapted conceptually.  
**What to copy:** local/offline docs index principle.  
**What not to copy:** Docusaurus dependency tree.

---

### Candidate: mdBook search index

- **Category:** static-site indexer / Markdown documentation builder
    
- **Repository/docs:** rust-lang/mdBook; mdBook search-functionality documentation.
    
- **Relevant implementation evidence:** mdBook search is described as build-time index generation plus browser-side search execution; another source describes generated `searchindex.js` and `searchindex.json`. ([DeepWiki](https://deepwiki.com/rust-lang/mdBook/4.4-search-functionality?utm_source=chatgpt.com "Search Functionality | rust-lang/mdBook | DeepWiki"))
    
- **What it produces:** Search files from Markdown chapters.
    
- **Why comparable:** Apex’s `claude-skill-design` KB is closer to a Markdown book/source corpus than to a database.
    
- **Adaptation for Apex:** Generate a compact `search-index.json` with file path, title/headings, terms, snippets, and source authority.
    
- **Risks:** mdBook’s book/chapter model may not match loose KB folders.
    

**Apex fit:** Medium-high.  
**Effort:** Low to adapt as pattern.  
**What to copy:** build-time search serialization.  
**What not to copy:** book rendering pipeline.

---

### Candidate: Sphinx inventory / search index

- **Category:** static docs indexer / inventory system
    
- **Repository/docs:** Sphinx `objects.inv`; sphobjinv.
    
- **Relevant implementation evidence:** `objects.inv` is a structured inventory format with project/version metadata and object records; sphobjinv exposes tooling to inspect/manipulate these inventories. ([sphobjinv.readthedocs.io](https://sphobjinv.readthedocs.io/en/stable/syntax.html?utm_source=chatgpt.com "Sphinx objects.inv v2 Syntax — sphobjinv 2.4 documentation"))
    
- **What it produces:** Cross-reference inventory, object lookup metadata.
    
- **Why comparable:** Apex can emulate the “inventory before prose” idea for source authority and document objects.
    
- **Adaptation for Apex:** Use a simpler JSON inventory; no need to adopt Sphinx.
    
- **Risks:** Too code/API-doc oriented for a Markdown skill-design KB.
    

**Apex fit:** Medium.  
**Effort:** Medium.  
**What to copy:** explicit inventory discipline.  
**What not to copy:** Sphinx build stack.

---

### Candidate: remark / unified Markdown AST

- **Category:** Markdown processor
    
- **Repository/docs:** remark/unified.
    
- **Relevant implementation evidence:** remark is an ecosystem around Markdown as structured data via ASTs; plugins inspect and change syntax trees. ([github.com](https://github.com/remarkjs/remark?utm_source=chatgpt.com "GitHub - remarkjs/remark: markdown processor powered by plugins part of ..."))
    
- **What it produces:** Programmatic AST access to headings, links, lists, code blocks, paragraphs, etc.
    
- **Why comparable:** Apex needs deterministic heading maps, link maps, and frontmatter maps.
    
- **Adaptation for Apex:** Either use Node/remark or reproduce a minimal Python equivalent; for Apex V1, Python regex/markdown-it-py may be simpler.
    
- **Risks:** Node dependency if copied directly.
    

**Apex fit:** High.  
**Effort:** Medium if using Node; low-medium if reimplemented minimally in Python.  
**What to copy:** AST-first extraction model.  
**What not to copy:** broad plugin ecosystem.

---

### Candidate: gray-matter

- **Category:** frontmatter extractor
    
- **Repository/docs:** gray-matter.
    
- **Relevant implementation evidence:** gray-matter parses frontmatter from strings/files and supports YAML by default plus JSON/TOML variants. ([github.com](https://github.com/jonschlinkert/gray-matter?utm_source=chatgpt.com "GitHub - jonschlinkert/gray-matter: Smarter YAML front matter parser ..."))
    
- **What it produces:** Parsed frontmatter + content body.
    
- **Why comparable:** Apex needs `frontmatter maps` and source authority metadata.
    
- **Adaptation for Apex:** If Apex stays Python-only, implement a narrow YAML-frontmatter parser or use Python stdlib-compatible fallback.
    
- **Risks:** Node dependency; YAML edge cases.
    

**Apex fit:** High.  
**Effort:** Low.  
**What to copy:** frontmatter extraction contract.  
**What not to copy:** npm package if Python-only is binding.

---

### Candidate: markdown-link-validator / markdown-link-check

- **Category:** Markdown link validator
    
- **Repository/docs:** markdown-link-validator, markdown-link-check.
    
- **Relevant implementation evidence:** markdown-link-validator verifies relative URLs and can validate heading anchors; markdown-link-check extracts hyperlinks and checks live/dead status. ([github.com](https://github.com/webhintio/markdown-link-validator?utm_source=chatgpt.com "GitHub - webhintio/markdown-link-validator: Validate markdown links"))
    
- **What it produces:** Broken-link reports, anchor validation, relative path checks.
    
- **Why comparable:** Apex needs link maps, broken link detection, noise/asset detection, and later wiki integrity checks.
    
- **Adaptation for Apex:** Implement local-only link validation first; avoid network link checking by default.
    
- **Risks:** External URL checks can be slow/noisy; skip for first test.
    

**Apex fit:** High.  
**Effort:** Low.  
**What to copy:** local relative-link + heading-anchor validation.  
**What not to copy:** mandatory network link checks.

---

### Candidate: Obsidian vault graph tools

- **Category:** markdown knowledge graph / wikilink graph
    
- **Repository/docs:** Obsidian vault graph CLI examples.
    
- **Relevant implementation evidence:** A local zero-dependency Obsidian vault graph CLI parses Markdown and wikilinks to answer backlinks, outbound links, hub notes, orphans, broken wikilinks, and graph-neighborhood questions. ([github.com](https://github.com/kartikkabadi/obsidian-vault-graph?utm_source=chatgpt.com "kartikkabadi/obsidian-vault-graph - GitHub"))
    
- **What it produces:** Link graph, backlinks, orphan nodes, hubs, broken wikilinks.
    
- **Why comparable:** Apex needs `link-graph.json` and high-signal navigation artifacts.
    
- **Adaptation for Apex:** Copy the graph concepts: nodes, edges, backlinks, orphan files, hubs, broken references.
    
- **Risks:** Obsidian-specific syntax may overfit; Apex should support both `[[wikilinks]]` and Markdown links.
    

**Apex fit:** High.  
**Effort:** Low-medium.  
**What to copy:** graph artifact model.  
**What not to copy:** Obsidian plugin runtime.

---

### Candidate: ripgrep + fd workflows

- **Category:** CLI / repo search and inventory
    
- **Repository/docs:** ripgrep, fd.
    
- **Relevant implementation evidence:** ripgrep recursively searches directories, respects gitignore, and skips hidden/binary files by default; fd recursively finds filesystem entries and also respects ignore behavior by default. ([github.com](https://github.com/BurntSushi/ripgrep?utm_source=chatgpt.com "GitHub - BurntSushi/ripgrep: ripgrep recursively searches directories ..."))
    
- **What it produces:** Fast file lists, keyword hits, topic candidate reports, grep-style evidence.
    
- **Why comparable:** This is the simplest way to avoid blind LLM inspection.
    
- **Adaptation for Apex:** Use `git ls-files` or Python equivalent for manifest; use ripgrep-like semantics for keyword reports.
    
- **Risks:** CLI availability on Windows; Python implementation may be more portable.
    

**Apex fit:** High.  
**Effort:** Low.  
**What to copy:** ignore-aware recursive discovery and keyword reporting.  
**What not to copy:** making shell tooling mandatory if Apex wants Python-only.

---

### Candidate: cloc / tokei

- **Category:** corpus statistics
    
- **Repository/docs:** cloc, tokei.
    
- **Relevant implementation evidence:** cloc counts blank/comment/source lines across many languages; tokei displays files, total lines, code, comments, and blanks by language. ([github.com](https://github.com/AlDanial/cloc?utm_source=chatgpt.com "GitHub - AlDanial/cloc: cloc counts blank lines, comment lines, and ..."))
    
- **What it produces:** File counts, language/type breakdown, LOC stats.
    
- **Why comparable:** Apex needs corpus profile: counts, sizes, likely heavy files, generated/noise candidates.
    
- **Adaptation for Apex:** Implement approximate counts directly in `apex_kb.py`.
    
- **Risks:** Code metrics are less useful for prose-heavy Markdown but still helpful for scripts/repos.
    

**Apex fit:** High.  
**Effort:** Low.  
**What to copy:** count/report output shape.  
**What not to copy:** language-specific complexity metrics unless needed.

---

### Candidate: Universal Ctags / tree-sitter

- **Category:** repo/code intelligence
    
- **Repository/docs:** Universal Ctags JSON output; tree-sitter queries.
    
- **Relevant implementation evidence:** Universal Ctags supports JSON output with structured tag records; tree-sitter provides syntax trees and query pattern matching for code structures. ([docs.ctags.io](https://docs.ctags.io/en/stable/man/ctags-json-output.5.html?utm_source=chatgpt.com "ctags-json-output — Universal Ctags 0.3.0 documentation"))
    
- **What it produces:** Symbol maps, code structure, function/class/entity maps.
    
- **Why comparable:** Useful if the KB contains scripts, tools, validators, or source repo mirrors.
    
- **Adaptation for Apex:** Optional for code-containing source folders; not necessary for first `claude-skill-design` text corpus pass.
    
- **Risks:** Overkill for Markdown-only KB.
    

**Apex fit:** Medium.  
**Effort:** Medium-high.  
**What to copy:** JSON symbol map concept.  
**What not to copy:** full multi-language AST pipeline in V1.

---

### Candidate: SQLite FTS5 / Lunr / Tantivy

- **Category:** local full-text search index
    
- **Repository/docs:** SQLite FTS5, Lunr, Tantivy.
    
- **Relevant implementation evidence:** SQLite FTS5 lets users create full-text virtual tables; Lunr indexes JSON documents and supports client-side search; Tantivy is a Rust full-text search engine library inspired by Lucene. ([sqlite.org](https://sqlite.org/fts5.html?utm_source=chatgpt.com "SQLite FTS5 Extension"))
    
- **What it produces:** Full-text search index.
    
- **Why comparable:** Apex needs lexical retrieval before semantic synthesis.
    
- **Adaptation for Apex:** For V1, prefer **JSON search index** or **SQLite FTS5** only if Python stdlib `sqlite3` with FTS5 is available locally.
    
- **Risks:** Tantivy/Rust is too heavy for first test; Lunr implies JS; SQLite FTS availability may vary.
    

**Apex fit:** Medium-high.  
**Effort:** Low for JSON, medium for SQLite FTS5, high for Tantivy.  
**What to copy:** inverted-index principle.  
**What not to copy:** vector DB / server search infrastructure.

---

## 4. Capability Coverage Matrix

|Capability|Existing real implementation found?|Best candidate|Apex fit|Notes|
|---|--:|---|---|---|
|Recursive file inventory|Yes|fd / ripgrep / git-ls-files pattern|High|Apex can implement in Python with ignore rules.|
|File type/extension stats|Yes|tokei / cloc|High|Add to `corpus-profile.json`.|
|Word/line/byte counts|Yes|cloc / tokei / custom Python|High|For Markdown, custom Python is enough.|
|Markdown heading extraction|Yes|remark / unified / markdown-it|High|Use AST or conservative regex.|
|Frontmatter extraction|Yes|gray-matter|High|Python-only minimal parser acceptable.|
|Markdown link extraction|Yes|markdown-link-check / remark|High|Needed for link map and broken links.|
|Wikilink graph|Yes|Obsidian vault graph tools|High|Support `[[page]]`, aliases, embeds.|
|Keyword frequency map|Yes|ripgrep / local indexers / SQLite FTS|High|Deterministic candidate-topic layer.|
|Topic-to-file map|Partially|keyword rules + search index|High|Deterministic heuristic, not semantic truth.|
|Source authority/path rules|Yes, pattern-based|Apex KB / docs systems|High|Rules from path/source class, not LLM judgment.|
|Duplicate/hash detection|Yes|LLM-Wiki hash helpers / SHA-256|High|Already aligned with Apex KB.|
|Noise/asset filtering|Yes|ripgrep/fd ignore behavior; static site excludes|High|Filter binaries, generated files, assets.|
|Search index generation|Yes|MkDocs / mdBook / Lunr / SQLite FTS|High|Produce `manifests/search-index.json` first.|
|Compact LLM navigation report|Yes, as pattern|LLM-Wiki index-first query + static search|High|Generated MD report should be LLM-first.|

---

## 5. Recommended Apex KB Pre-LLM Layer

Minimal, composable, no overengineering:

```yaml
apex_pre_llm_layer:
  scope:
    kb_root: "apex-meta/kb/claude-skill-design/"
    source_roots:
      - "apex-meta/kb/claude-skill-design/sources/"
    output_root: "apex-meta/kb/claude-skill-design/manifests/"
    owner: "deterministic tools / local processes / generated metadata"
    requires_llm: false

  step_1_file_manifest:
    output:
      - "manifests/corpus-profile.json"
      - "manifests/corpus-profile.md"
    includes:
      - recursive_file_inventory
      - extension_counts
      - file_size_counts
      - line_word_byte_counts
      - hash_per_file
      - duplicate_hash_groups
      - noise_asset_flags

  step_2_markdown_structure_map:
    output: "manifests/heading-link-frontmatter-map.json"
    includes:
      - markdown_headings
      - frontmatter_fields
      - markdown_links
      - wikilinks
      - outbound_links
      - broken_internal_links
      - orphan_candidates

  step_3_keyword_topic_map:
    output: "manifests/topic-file-map.json"
    includes:
      - deterministic_topic_rules
      - keyword_hit_counts
      - high_signal_snippets
      - topic_to_file_candidates
      - topic_confidence_by_rule_not_semantics

  step_4_priority_report:
    output: "manifests/source-priority-list.md"
    includes:
      - official_first
      - examples_second
      - local_operator_notes_flagged
      - academic_secondary_flagged
      - duplicate_or_noise_downranked
      - read_first_list
      - read_later_list
      - exclude_or_ignore_list

  step_5_optional_search_index:
    output: "manifests/search-index.json"
    includes:
      - file_id
      - path
      - title
      - headings
      - normalized_text_excerpt
      - terms
      - source_class
      - authority_score
      - byte_offsets_or_line_ranges_if_available

  step_6_optional_link_graph:
    output: "manifests/link-graph.json"
    includes:
      - nodes
      - markdown_edges
      - wikilink_edges
      - backlinks
      - orphan_nodes
      - hub_nodes
      - broken_edges
```

This aligns with the Apex/LLM-Wiki capability map already recorded: the blueprint files support hash, frontmatter validation, broken-link detection, orphan detection, stale-index detection, index-first query, and durable graph/navigation artifacts. The existing Apex decision layer already treats Python as owner of deterministic structure while the LLM owns semantic extraction and synthesis.

---

## 6. Minimal Schema

### 6.1 `corpus-profile.json`

```json
{
  "schema_version": "0.1",
  "kb_slug": "claude-skill-design",
  "generated_at": "YYYY-MM-DDTHH:MM:SSZ",
  "source_roots": [],
  "file_inventory": [
    {
      "file_id": "sha256:path-or-stable-id",
      "path": "string",
      "extension": ".md",
      "mime_guess": "text/markdown",
      "source_class": "official | example | secondary | academic | operator_note | script | asset | unknown",
      "bytes": 0,
      "lines": 0,
      "words": 0,
      "sha256": "string",
      "is_binary": false,
      "is_generated": false,
      "is_noise_candidate": false,
      "noise_reasons": []
    }
  ],
  "aggregate_stats": {
    "files_total": 0,
    "bytes_total": 0,
    "lines_total": 0,
    "words_total": 0,
    "by_extension": {},
    "by_source_class": {}
  },
  "duplicate_groups": [
    {
      "sha256": "string",
      "paths": []
    }
  ]
}
```

### 6.2 `heading-link-frontmatter-map.json`

```json
{
  "schema_version": "0.1",
  "kb_slug": "claude-skill-design",
  "files": [
    {
      "path": "string",
      "frontmatter": {},
      "headings": [
        {
          "level": 1,
          "text": "string",
          "slug": "string",
          "line": 1
        }
      ],
      "markdown_links": [
        {
          "text": "string",
          "target": "string",
          "kind": "relative | absolute | anchor | external",
          "line": 1,
          "resolved_path": "string | null",
          "status": "ok | broken | unchecked"
        }
      ],
      "wikilinks": [
        {
          "raw": "[[Skill design]]",
          "target": "Skill design",
          "alias": null,
          "line": 1,
          "resolved_path": null,
          "status": "ok | broken | unresolved"
        }
      ]
    }
  ]
}
```

### 6.3 `topic-file-map.json`

```json
{
  "schema_version": "0.1",
  "kb_slug": "claude-skill-design",
  "topic_rules": [
    {
      "topic_id": "agents-vs-skills",
      "keywords": ["agent", "skill", "subagent", "routing"],
      "path_boosts": ["official", "references"],
      "negative_patterns": ["changelog", "asset"]
    }
  ],
  "topics": [
    {
      "topic_id": "agents-vs-skills",
      "topic_label": "Agents vs skills",
      "candidate_files": [
        {
          "path": "string",
          "score": 0,
          "matched_terms": [],
          "matched_headings": [],
          "source_class": "official",
          "authority_score": 0,
          "recommended_read_order": 1
        }
      ]
    }
  ]
}
```

### 6.4 `source-priority-list.md`

```md
# Source Priority List — claude-skill-design

## Read First

| Rank | Path | Source class | Reason | Related topics |
|---:|---|---|---|---|

## Read Selectively

| Rank | Path | Source class | Reason | Related topics |
|---:|---|---|---|---|

## Likely Noise / Assets

| Path | Reason |
|---|---|

## Duplicate Groups

| Hash | Paths | Recommendation |
|---|---|---|

## Topic Bundles

| Topic | Read first | Optional | Exclude |
|---|---|---|
```

### 6.5 `search-index.json`

```json
{
  "schema_version": "0.1",
  "kb_slug": "claude-skill-design",
  "documents": [
    {
      "id": "string",
      "path": "string",
      "title": "string",
      "source_class": "official",
      "headings": [],
      "text_excerpt": "string",
      "terms": {
        "skill": 12,
        "agent": 4
      },
      "line_ranges": [
        {
          "start": 1,
          "end": 80
        }
      ]
    }
  ]
}
```

### 6.6 `link-graph.json`

```json
{
  "schema_version": "0.1",
  "kb_slug": "claude-skill-design",
  "nodes": [
    {
      "id": "string",
      "path": "string",
      "title": "string",
      "source_class": "official",
      "in_degree": 0,
      "out_degree": 0,
      "is_orphan": false,
      "is_hub": false
    }
  ],
  "edges": [
    {
      "source": "path-a.md",
      "target": "path-b.md",
      "kind": "markdown_link | wikilink | frontmatter_link",
      "line": 1,
      "status": "ok | broken | unresolved"
    }
  ]
}
```

---

## 7. Compare Against Existing Apex / LLM-Wiki Repo State

Based on the accessible project records, not a live local filesystem inspection:

### Already present

- `apex-kb` package concept and boundaries are already present.
    
- `apex-meta/scripts/apex_kb.py` is already defined as a deterministic Python helper with subcommands such as `scaffold`, `hash`, `preflight`, `manifest`, `index`, `lint`, and `audit`; Codex test evidence shows those commands ran successfully in a later test.
    
- Local LLM-Wiki blueprints were inspected earlier: `llm-wiki-main` and `llm-wiki-skill-main`, including ingest/query/lint/graph/review workflows and hash/link/orphan/stale-check helpers.
    
- The blueprint map already records the right Python/LLM split: deterministic waste to scripts, semantic extraction to the LLM.
    

### Partially present

- Hashing, scaffold, preflight, manifest, index, lint, and audit exist in `apex_kb.py`, but the current request needs a **pre-semantic corpus intelligence mode** specifically for `claude-skill-design`.
    
- The LLM-Wiki-derived `index-first query` model exists, but the target artifacts requested here are more granular: `corpus-profile.json`, `topic-file-map.json`, `source-priority-list.md`, `search-index.json`, `link-graph.json`.
    
- The existing KB package can validate/maintain a KB, but the requested layer is a **Phase 0/Phase 1 preparation report** for a large source corpus before LLM ingest-analysis.
    

### Missing

- A dedicated command/mode like:
    

```text
python apex-meta/scripts/apex_kb.py corpus-profile --kb-root apex-meta/kb/claude-skill-design --source-root ...
```

- Dedicated output artifacts:
    

```text
apex-meta/kb/claude-skill-design/manifests/corpus-profile.json
apex-meta/kb/claude-skill-design/manifests/corpus-profile.md
apex-meta/kb/claude-skill-design/manifests/topic-file-map.json
apex-meta/kb/claude-skill-design/manifests/source-priority-list.md
apex-meta/kb/claude-skill-design/manifests/search-index.json
apex-meta/kb/claude-skill-design/manifests/link-graph.json
```

- A deterministic topic-rule file for Claude Skill Design topics.
    
- A source authority/path rules file for official vs example vs secondary/operator-supplied sources.
    
- A compact LLM navigation report designed specifically for the next semantic-analysis chat.
    

### Should not reimplement

- Do not reimplement full MkDocs, Docusaurus, mdBook, Sphinx, Obsidian, Tantivy, or Sourcegraph.
    
- Do not build embeddings/vector DB for the first test.
    
- Do not move semantic classification into Python beyond rule-based topic hints.
    
- Do not make Codex generate semantic ingest-analysis files if the current workflow decision remains: **Codex = deterministic prep; ChatGPT = LLM semantic analysis**. The project files explicitly identify this split: deterministic helpers exclude concept extraction, entity synthesis, contradiction interpretation, wiki prose drafting, query synthesis, and operator-review decisions.
    

### Should integrate or adapt

- Adapt LLM-Wiki’s hash, manifest, link validation, orphan detection, stale index, index-first navigation, and audit principles.
    
- Adapt MkDocs/mdBook/Docusaurus-style static search-index generation.
    
- Adapt remark/gray-matter-style Markdown/frontmatter extraction.
    
- Adapt Obsidian-style wikilink graph metrics.
    
- Keep everything local, deterministic, and JSON/Markdown-first.
    

---

## 8. Deterministic vs LLM-Assisted vs Full Semantic

```yaml
classes:
  deterministic_pre_llm:
    description: "No LLM; scans, counts, indexes, hashes, maps, and ranks by explicit rules."
    examples:
      - corpus-profile.json
      - file inventory
      - heading map
      - frontmatter map
      - markdown link map
      - wikilink graph
      - keyword map
      - topic-file candidate map
      - source authority path rules
      - duplicate hash groups
      - search-index.json
      - compact navigation report

  low_token_llm_assisted:
    description: "Uses minimal LLM calls only after deterministic narrowing."
    examples:
      - summarize top 20 high-signal files selected by deterministic topic map
      - validate source-priority-list.md
      - generate first semantic bundle plan from topic-file-map.json

  full_semantic_llm:
    description: "LLM reads selected sources and creates meaning-based synthesis."
    examples:
      - concept extraction
      - contradiction interpretation
      - final wiki page drafting
      - bundle synthesis
      - source authority judgment beyond path rules
```

The research target should stay in `deterministic_pre_llm`. The next step after that can be `low_token_llm_assisted`, but only after the corpus profile and source-priority map exist.

---

## 9. What Not To Do

Do **not** add vector DBs.  
Do **not** add embeddings for the first test.  
Do **not** build a big orchestration framework.  
Do **not** make the deterministic layer responsible for semantic truth.  
Do **not** block LLM analysis forever waiting for a perfect index.  
Do **not** introduce Docusaurus/MkDocs/mdBook as runtime dependencies just to copy their search-index idea.  
Do **not** spend Codex tokens on semantic analysis if ChatGPT is intended to own LLM synthesis.

---

## 10. Final Yes/No

```yaml
recommendation:
  build_pre_llm_corpus_intelligence_layer: true
  use_existing_tool_directly: false
  adapt_existing_patterns: true

  likely_best_stack:
    - "Python stdlib-only extension to apex-meta/scripts/apex_kb.py"
    - "git-ls-files or Python recursive inventory with ignore rules"
    - "SHA-256 file/directory hashing"
    - "Markdown heading/frontmatter/link extraction"
    - "Wikilink graph extraction"
    - "Rule-based keyword/topic mapping"
    - "JSON search-index artifact"
    - "Markdown source-priority navigation report"

  expected_token_saving: "high"
  expected_reliability_gain: "high"
  expected_complexity: "low-to-medium"
```

**Bottom line:** build this as a **Phase 0 deterministic corpus intelligence layer** before semantic ingest-analysis. It should generate compact navigation artifacts for `claude-skill-design`, then the LLM phase should read those artifacts first and only open the high-signal files selected by the deterministic layer.