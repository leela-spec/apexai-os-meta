## What I actually executed

### Repository inspection through connector

- Confirmed repo access to `leela-spec/apexai-os-meta`.
- Found active `claude-skill-design` KB files, including:
    - `kb-schema.md`
    - `sources/README.md`
    - `manifests/source-inventory.json`
    - `manifests/source-inventory.csv`
    - existing Phase 1 prep/run reports
    - existing wiki/index and previous ingest-analysis files.
- Confirmed `phase0-tool-audit.md` does **not** currently appear in the repo search results.
- Fetched the existing source inventory and prep report.

### Runtime tool checks executed here

These are **not your Windows machine**, but this execution runtime:

```
git: installed — 2.47.3rg: installed — ripgrep 14.1.1fd: missingtokei: missingscc: missingcloc: missingpython: installed — 3.13.5node: installed — v22.16.0npm: installed — 10.9.2sqlite3 CLI: missingpython-frontmatter: missingmarkdown-it-py: installedpython sqlite3: installed
```

### Existing repo evidence relevant to this audit

The existing Phase 1 prep report already confirms a **large source corpus**: 599 files, 16,810,931 bytes, with curated and operator-supplied groups. It also confirms curated groups such as academic, official docs, official PDFs, official repos, repo extracts, and secondary sources. The report says `source-inventory.csv` and `source-inventory.json` already exist. The inventory itself contains per-file paths, extensions, sizes, and SHA-256 hashes.

I did **not** write to the repo because your original task explicitly prohibited GitHub connector writes and asked for local repo file-tree work. I cannot write into `C:\GitDev\apexai-os-meta` from this runtime.

---

# `apex-meta/kb/claude-skill-design/manifests/phase0-tool-audit.md`

```
# Phase 0 Tool Audit — Claude Skill Design KB## 1. Executive verdictThe best Phase 0 stack for `apex-meta/kb/claude-skill-design/` is a **small deterministic corpus-intelligence stack**, not a static-site generator and not an LLM semantic ingest process.The active corpus is large enough to justify this layer: the existing Phase 1 prep report counted **599 source files** and **16,810,931 bytes** under `apex-meta/kb/claude-skill-design/sources/`. It also confirmed that deterministic source inventories already exist at:```textapex-meta/kb/claude-skill-design/manifests/source-inventory.csvapex-meta/kb/claude-skill-design/manifests/source-inventory.json
```

The immediate V1 stack should use:

```
git ls-filesripgrep / rgPython standard libraryPython sqlite3 / FTS5 if availablesmall custom Python parsers for headings, links, frontmatter-ish blocks, and wikilinks
```

Add `fd`, `tokei`/`scc`, `python-frontmatter`, and `markdown-it-py` in V1.5 if they are available or easy to install.

Defer Node `remark/unified`, MkDocs search index, and mdBook search index unless Markdown AST fidelity or static-docs publishing becomes a real requirement.

This audit was partially executed from ChatGPT’s runtime, not from the operator’s Windows machine. Runtime checks here are useful but not definitive for `C:\GitDev\apexai-os-meta`.

---

## 2. Already observed in this runtime

|Check|Result|
|---|---|
|`git --version`|installed: `git version 2.47.3`|
|`rg --version`|installed: `ripgrep 14.1.1`|
|`fd --version`|missing|
|`tokei --version`|missing|
|`scc --version`|missing|
|`cloc --version`|missing|
|`python --version`|installed: `Python 3.13.5`|
|`node --version`|installed: `v22.16.0`|
|`npm --version`|installed: `10.9.2`|
|`sqlite3 --version`|CLI missing|
|`python -c "import frontmatter"`|missing|
|`python -c "import markdown_it"`|installed|
|`python -c "import sqlite3"`|installed|

## 3. Ranked tool table

|Rank|Tool/component|What it does in plain language|Install needed?|CLI-only?|Needs custom script?|Runs without LLM?|Output artifact|Install difficulty 1-5|Maintenance 1-5|Runtime speed 1-5|Resilience 1-5|Token-saving value 1-5|Keep / test / reject|Reason|
|---|---|---|---|---|---|---|---|---|---|---|---|---|---|---|
|1|`git_ls_files`|Lists tracked repo files deterministically.|No, Git already present in most repos.|Yes|No|Yes|file inventory baseline|5|5|5|5|5|Keep|Best stable baseline for repo-tracked files.|
|2|`ripgrep_rg`|Fast recursive search and file listing.|Maybe; installed in this runtime.|Yes|No|Yes|keyword hits, file lists, source narrowing|5|5|5|5|5|Keep|Strongest CLI search tool for local corpus navigation.|
|3|`simple_python_heading_link_parser`|Extracts headings, Markdown links, approximate anchors, and code-block boundaries.|No if implemented with Python stdlib.|No|Yes|Yes|`heading-map.json`, `markdown-link-map.json`|5|4|4|4|5|Keep|Highest practical token-saving value with minimal dependency.|
|4|`SQLite_FTS5`|Builds a local full-text search index for deterministic keyword lookup.|Maybe; Python sqlite3 exists here, sqlite3 CLI missing.|No|Yes|Yes|`search-index.sqlite`|4|4|4|4|5|Keep/test|Strong value if Python’s SQLite build supports FTS5.|
|5|`obsidian_style_wikilink_graph_parser`|Extracts `[[wikilinks]]`, backlinks, orphan candidates, and graph hubs.|No if implemented in Python.|No|Yes|Yes|`wikilink-graph.json`, backlinks report|5|4|4|4|4|Keep|Important if sources or generated KB use wiki-style links.|
|6|`markdown_it_py`|Parses Markdown into tokens instead of fragile regex.|Maybe; installed in this runtime.|No|Yes|Yes|heading/link/token map|4|4|4|5|4|Test|Better than regex for complex Markdown; still lightweight.|
|7|`python_frontmatter`|Reads YAML/TOML/JSON frontmatter from Markdown files.|Yes here; missing in this runtime.|No|Yes|Yes|`frontmatter-map.json`|4|4|4|4|4|Test|Useful if many files contain metadata headers.|
|8|`fd`|Fast, ergonomic file discovery.|Yes here; missing in this runtime.|Yes|No|Yes|file lists by extension/folder|4|5|5|5|3|Test|Nice convenience, but `rg --files` can cover most V1 needs.|
|9|`tokei`|Fast file/language/line count statistics.|Yes here; missing in this runtime.|Yes|No|Yes|corpus profile stats|3|5|5|5|3|Test|Good corpus profile utility; not essential if custom counts exist.|
|10|`scc`|Code/file statistics similar to tokei/cloc.|Yes here; missing in this runtime.|Yes|No|Yes|corpus profile stats|3|4|5|4|3|Test|Good alternative to tokei; choose one, not all three.|
|11|`cloc`|Older standard for line/file/language counts.|Yes here; missing in this runtime.|Yes|No|Yes|line-count report|3|4|3|4|2|Reject/defer|Battle-tested but slower and less useful than tokei/scc for V1.|
|12|`remark_unified_node`|Node Markdown AST ecosystem for very accurate Markdown processing.|Yes; Node/npm present here, packages not checked/installed.|No|Yes|Yes|rich Markdown AST-derived maps|2|2|3|5|4|Defer|Powerful but heavier dependency chain; only needed if Python parsing is insufficient.|
|13|`MkDocs_search_index`|Builds a static-site search index for docs.|Yes|Mostly CLI, but needs site config|Possibly|Yes|`search_index.json`|2|2|3|3|2|Reject V1|Useful pattern, but too indirect unless building a docs site.|
|14|`mdBook_search_index`|Builds a book-style search index from Markdown.|Yes|Mostly CLI, but needs book structure|Possibly|Yes|mdBook search index|2|3|3|3|2|Reject V1|Requires adapting corpus into book format; unnecessary first.|

## 4. Which tools are already installed

Confirmed in this runtime:

```
gitrgpythonnodenpmmarkdown-it-pypython sqlite3
```

Likely already available on many Windows developer machines, but must be checked locally:

```
gitpythonnodenpm
```

`rg` is already available in the prior local Phase 1 prep report: the report records successful use of `rg --files` and `rg` inspection commands during the previous deterministic prep run.

## 5. Which tools would need installation

Missing in this runtime:

```
fdtokeisccclocsqlite3 CLIpython-frontmatter
```

Expected installation routes, not executed:

|Tool|Expected install route|
|---|---|
|`fd`|Windows package manager, Scoop, Chocolatey, winget, or Rust/cargo|
|`tokei`|Windows package manager or Rust/cargo|
|`scc`|Windows package manager, Go install, or release binary|
|`cloc`|Windows package manager or Perl-based install|
|`sqlite3` CLI|SQLite release binary or package manager|
|`python-frontmatter`|`pip install python-frontmatter`|
|`markdown-it-py`|`pip install markdown-it-py` if missing locally|
|`remark/unified`|`npm install unified remark-parse remark-frontmatter ...`|

Do not install all of these. Pick the smallest useful stack.

## 6. Which options are pure CLI

Pure CLI or CLI-first:

```
git ls-filesrgfdtokeisccclocsqlite3 CLIMkDocs search buildmdBook build
```

Best pure CLI V1:

```
git ls-filesrg
```

Optional V1.5 CLI:

```
fdtokei or scc
```

## 7. Which options require a small script

Small script required:

```
simple_python_heading_link_parserobsidian_style_wikilink_graph_parserSQLite_FTS5 index builder if using Python sqlite3python_frontmatter integrationmarkdown_it_py integrationremark/unified integration
```

Best script targets:

```
scripts/phase0_corpus_profile.pyscripts/phase0_markdown_map.pyscripts/phase0_search_index.py
```

or a single consolidated script:

```
apex-meta/scripts/phase0_corpus_intelligence.py
```

## 8. Which options are excluded for now

Exclude from V1:

```
MkDocs_search_indexmdBook_search_indexremark_unified_nodecloc
```

Reason:

- MkDocs and mdBook are publishing systems, not direct KB-prep systems.
- `remark/unified` is powerful but adds Node dependency complexity.
- `cloc` is useful but weaker than `tokei`/`scc` for this specific fast-profile use case.
- The corpus already needs navigation artifacts, not a static docs build.

## 9. Final recommended V1 stack

```
v1_stack:  purpose: "Minimal deterministic corpus intelligence before LLM semantic ingest."  tools:    - git_ls_files    - ripgrep_rg    - python_standard_library    - python_sqlite3_if_fts5_available    - simple_python_heading_link_parser    - obsidian_style_wikilink_graph_parser  outputs:    - manifests/corpus-file-inventory.json    - manifests/corpus-profile.md    - manifests/heading-map.json    - manifests/markdown-link-map.json    - manifests/wikilink-graph.json    - manifests/search-index.sqlite    - manifests/source-priority-candidates.md
```

Why this is best:

- It is deterministic.
- It avoids LLM calls.
- It uses tools already likely available.
- It reduces token waste before Phase 1.
- It is inspectable by a non-programmer through Markdown/JSON outputs.

## 10. Final recommended V1.5 stack

```
v1_5_stack:  add:    - fd    - tokei_or_scc    - markdown_it_py    - python_frontmatter  purpose: "Improve speed, metadata extraction, and Markdown structure fidelity."
```

Recommended choices:

```
Use one of: tokei or scc.Do not use tokei + scc + cloc unless comparing tools.Use markdown-it-py if regex heading/link extraction proves brittle.Use python-frontmatter if many source files have YAML headers.
```

## 11. Final recommended V2 stack

```
v2_stack:  possible_additions:    - remark_unified_node    - MkDocs_search_index_as_pattern    - mdBook_search_index_as_pattern  use_only_if:    - Python Markdown parsing is insufficient    - the KB needs a static docs site    - search index generation needs browser-facing output    - AST precision becomes more valuable than dependency simplicity
```

V2 should not be started until V1 artifacts have been generated and tested against the corpus.

## 12. Suggested Phase 0 output artifacts

Recommended artifacts:

```
apex-meta/kb/claude-skill-design/manifests/corpus-file-inventory.jsonapex-meta/kb/claude-skill-design/manifests/corpus-profile.mdapex-meta/kb/claude-skill-design/manifests/heading-map.jsonapex-meta/kb/claude-skill-design/manifests/frontmatter-map.jsonapex-meta/kb/claude-skill-design/manifests/markdown-link-map.jsonapex-meta/kb/claude-skill-design/manifests/wikilink-graph.jsonapex-meta/kb/claude-skill-design/manifests/search-index.sqliteapex-meta/kb/claude-skill-design/manifests/source-priority-candidates.md
```

The existing repo already has:

```
apex-meta/kb/claude-skill-design/manifests/source-inventory.csvapex-meta/kb/claude-skill-design/manifests/source-inventory.json
```

Those should be reused, not recreated blindly.

## 13. What this means for a non-programmer

There are three categories:

### Simple command-line tools

These are like small utilities you run in the repo.

```
git ls-filesrgfdtokeiscccloc
```

They do not “understand” the documents. They list, count, and search files very fast.

Best ones for you:

```
git ls-filesrgtokei or scc later
```

### Small scripts

These are short deterministic programs that turn the files into useful maps.

Examples:

```
heading-map.jsonmarkdown-link-map.jsonwikilink-graph.jsonsearch-index.sqlite
```

This is where most of the value is. The LLM can read these small maps instead of blindly opening hundreds of files.

### Heavy systems

These are bigger ecosystems:

```
remark/unifiedMkDocsmdBook
```

They can be useful, but they are not the first thing to add. They create more setup and maintenance than necessary for the first working Phase 0.

## 14. Final recommendation

The next implementation should not start with MkDocs, mdBook, or a Node AST stack.

Start with:

```
git + rg + Python stdlib + sqlite3 + small Markdown parsers
```

Then test whether the produced artifacts actually help the LLM choose the right files for semantic ingest.

If yes, keep it.  
If no, add `markdown-it-py`, `python-frontmatter`, and one stats tool.

```
---## Bottom lineThe audit conclusion is:```yamlrecommended_now:  v1:    - git_ls_files    - ripgrep_rg    - python_standard_library    - python_sqlite3    - small_heading_link_parser    - small_wikilink_graph_parser  v1_5:    - markdown_it_py    - python_frontmatter    - tokei_or_scc    - fd  defer:    - remark_unified_node    - MkDocs_search_index    - mdBook_search_index    - cloc
```

I did not create `phase0-tool-audit.md` in the repo because that would require a connector write or access to your local Windows file tree. I did execute the repository inspection and tool checks that are possible here, and the report above is ready to save as:

```
apex-meta/kb/claude-skill-design/manifests/phase0-tool-audit.md
```