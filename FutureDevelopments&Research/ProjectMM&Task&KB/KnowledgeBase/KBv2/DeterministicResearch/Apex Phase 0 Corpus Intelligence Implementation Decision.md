# Apex Phase 0 Corpus Intelligence Implementation Decision

## 1. Decision

Apex should build a **Phase 0 deterministic corpus-intelligence layer** before any LLM semantic ingest.

The implementation target is:

```
apex-meta/kb/claude-skill-design/
```

Primary output root:

```
apex-meta/kb/claude-skill-design/manifests/
```

This layer should **not** create wiki pages, semantic ingest analyses, embeddings, or vector stores. It should create compact navigation artifacts so the later LLM phase can choose high-signal files instead of blindly reading the whole corpus.

The evidence is strong enough to proceed: the corpus is already large at **599 source files** and **16,810,931 bytes**, and existing deterministic inventories already exist at `source-inventory.csv` and `source-inventory.json`.

---

## 2. What is already proven

|Area|Proven state|Decision implication|
|---|---|---|
|Corpus size|Large enough to justify preprocessing: 599 files / 16.8 MB.|Do not let the LLM inspect everything directly.|
|Existing inventory|`source-inventory.csv/json` already exist and include paths, extensions, sizes, and SHA-256 hashes.|Reuse as base input. Do not recreate blindly.|
|Tool stack|`git`, `rg`, Python, Node/npm, `markdown-it-py`, and Python `sqlite3` were present in the prior runtime; some tools were missing there, and that runtime was **not** the operator’s Windows machine.|V1 should depend only on likely-stable tools: inventory + `rg` + Python stdlib.|
|Markdown parser|Best V1 parser is a simple Python state-machine parser; V1.5 can add `markdown-it-py`; Node/remark is deferred.|Build the first parser locally and simply.|
|Graph usefulness|Graph is useful now but partial; strongest edges are YAML/path/process fields, not normal Markdown links.|Graph extraction belongs in V1.5, and it must be Apex-specific.|
|Obsidian|Obsidian app is not required.|Build graph artifacts, not an Obsidian workflow.|

---

## 3. What is still uncertain

|Rank|Uncertainty|Practical resolution|
|---|---|---|
|1|Whether one consolidated script or several scripts is better|Use one consolidated script first: `phase0_corpus_intelligence.py`. Internally split into clear functions/subcommands.|
|2|Whether SQLite FTS5 works in the operator’s local Python build|Test during V1.5. If unavailable, export JSON/NDJSON keyword maps first.|
|3|Whether simple parsing is enough for MDX-heavy files|Start with Python state machine. Add `markdown-it-py` only where parser warnings show actual failures.|
|4|How much graph extraction belongs in V1|Keep ordinary Markdown/wikilink extraction in V1; defer Apex-specific manifest/process graph to V1.5.|
|5|Whether authority ranking can be deterministic enough|Use path/source rules only. Mark semantic authority as “LLM review needed.”|

---

# 4. Minimal V1 artifact contract

V1 should produce **read-first navigation artifacts**. These files are deterministic and can be regenerated.

```
apex-meta/kb/claude-skill-design/manifests/  corpus-profile.md  heading-map.json  markdown-link-map.json  frontmatter-map.json  keyword-hits.ndjson  topic-file-map.json  source-priority-candidates.md  phase0-navigation-report.md
```

## 4.1 `corpus-profile.md`

Purpose: human/LLM overview of the corpus before ingest.

Required sections:

```
required_sections:  - source_inventory_status  - file_count_by_extension  - byte_size_by_source_group  - largest_files  - likely_generated_or_noise_files  - duplicate_hash_groups  - source_group_summary  - parser_warning_summary
```

Decision: base this on the existing `source-inventory.json/csv`.

## 4.2 `heading-map.json`

Purpose: table of contents for the corpus.

Required fields:

```
record:  path: string  source_type_guess: string  h1_title: string_or_null  headings:    - level: integer      text: string      line: integer  parser_warnings: array
```

The parser spike already confirms this is the core useful V1 extraction target.

## 4.3 `markdown-link-map.json`

Purpose: extract ordinary Markdown links and file references.

Required fields:

```
record:  path: string  markdown_links:    - text: string      target: string      line: integer      target_type: relative_file | absolute_url | anchor | unknown      normalized_target: string_or_null
```

## 4.4 `frontmatter-map.json`

Purpose: detect metadata-bearing files.

V1 only needs delimiter detection and basic field extraction when safe.

```
record:  path: string  has_frontmatter: boolean  start_line: integer_or_null  end_line: integer_or_null  raw_field_keys: array  parse_status: detected | parsed | malformed | none
```

Full YAML validation can wait for V1.5.

## 4.5 `keyword-hits.ndjson`

Purpose: deterministic topic narrowing through explicit keyword matches.

Each line:

```
hit:  query_group: string  keyword: string  path: string  line: integer  snippet: string
```

Suggested initial keyword groups:

```
keyword_groups:  skill_design:    - skill    - SKILL.md    - frontmatter    - description    - allowed-tools    - examples    - scripts  validation:    - validate    - lint    - eval    - test    - failure mode  source_authority:    - official    - docs    - Anthropic    - Agent Skills  corpus_structure:    - manifest    - source    - index    - README
```

## 4.6 `topic-file-map.json`

Purpose: compact LLM routing map.

This should not claim semantic meaning. It should only say:

```
topic_file_map:  topic_key:    evidence_type:      - heading_match      - keyword_hit      - path_rule      - frontmatter_title    candidate_files:      - path: string        reasons: array        deterministic_score: integer
```

## 4.7 `source-priority-candidates.md`

Purpose: propose likely read-first sources for Phase 1.

Allowed deterministic ranking factors:

```
ranking_factors:  - official_or_curated_path_bonus  - source_inventory_size_signal  - heading_density  - title/frontmatter_presence  - keyword_hit_count  - markdown_link_degree  - duplicate_or_generated_penalty  - converted_pdf_noise_penalty
```

Forbidden:

```
forbidden:  - conceptual_truth_claims  - final_authority_claims  - contradiction_resolution  - canonical_page_decisions
```

## 4.8 `phase0-navigation-report.md`

This is the main LLM-facing file.

Required sections:

```
phase0_navigation_report:  - executive_summary  - corpus_profile_snapshot  - read_first_files  - read_later_files  - likely_noise_or_generated_files  - topic_bundles  - source_authority_candidates  - parser_warnings  - missing_or_broken_references  - recommended_phase1_batches  - explicit_uncertainties
```

This report should be the first file read by any Phase 1 semantic-ingest chat.

---

# 5. V1.5 artifact contract

V1.5 adds search and graph intelligence.

```
apex-meta/kb/claude-skill-design/manifests/  search-index.sqlite  search-index-export.json  link-graph.json  graph-summary.md  process-flow-graph-audit.md
```

## 5.1 `search-index.sqlite`

Purpose: local full-text lookup.

Use Python `sqlite3`; only enable FTS5 if local support is confirmed.

Fallback:

```
search-index-export.jsonkeyword-hits.ndjson
```

## 5.2 `link-graph.json`

This must not be a pure Obsidian graph.

It should include these edge types:

```
edge_types:  markdown_link:    source: file    target: parsed_markdown_target  wikilink:    source: file    target: wikilink_target  explicit_path_reference:    source: file    target: path_string  manifest_file_list:    source: package_manifest    target: file_list.path  supporting_file:    source: skill_or_manifest    target: supporting_files.path  canonical_source:    source: file    target: canonical_source_value  script_path:    source: file    target: script_path_value  process_ownership:    source: file    target: owns | hands_off_to | does_not_own values  process_arrow:    source: file    target: sequence_stage
```

This follows the graph audit’s core finding: useful Apex graph signals are in explicit paths, manifests, `canonical_source`, `script_path`, `hands_off_to`, `owns`, `does_not_own`, and process sequence text—not mainly in Markdown links.

## 5.3 `graph-summary.md`

Required sections:

```
graph_summary:  - graph_usefulness_verdict  - top_hub_files  - orphan_candidates  - missing_target_candidates  - dense_package_boundaries  - weak_or_missing_process_nodes  - graph_extraction_limitations
```

## 5.4 `process-flow-graph-audit.md`

Required focus:

```
process_flow_graph_audit:  must_answer:    - Can PreCapWeek, PreCapNextDay, FlowRecap, status merge, Apex KB, Apex Sync, Apex Session, contracts, templates, scripts, and manifests be represented as a useful graph?  must_report:    - strong_edges    - weak_edges    - missing_nodes    - ambiguous_relationships    - graph_policy
```

---

# 6. Script/module design options

## Recommended design

Use one consolidated script:

```
apex-meta/scripts/phase0_corpus_intelligence.py
```

With subcommands:

```
profileparse-markdownkeyword-mappriority-candidatesnavigation-reportsearch-indexgraphall
```

## Why one script first

|Reason|Explanation|
|---|---|
|Operator simplicity|One file and one command surface is easier to run and inspect.|
|Less repo clutter|Avoids scattering small scripts before the design stabilizes.|
|Shared normalization|Path normalization, inventory loading, exclusions, and output formatting stay consistent.|
|Easy later split|Once stable, subcommands can become separate modules if needed.|

## Suggested CLI shape

```
python apex-meta\scripts\phase0_corpus_intelligence.py all `  --kb-root apex-meta\kb\claude-skill-design `  --output-root apex-meta\kb\claude-skill-design\manifests
```

Dry-run/check mode:

```
python apex-meta\scripts\phase0_corpus_intelligence.py all `  --kb-root apex-meta\kb\claude-skill-design `  --check
```

## Implementation boundary

The script may:

```
may:  - read source-inventory.json  - list files  - count files/bytes/lines  - parse headings  - parse links  - detect frontmatter  - detect code fences  - run keyword searches  - build deterministic scores  - write manifest artifacts  - report parser uncertainty
```

The script must not:

```
must_not:  - write semantic ingest-analysis  - generate wiki pages  - decide conceptual truth  - resolve contradictions  - classify final canonical concepts  - use embeddings  - call an LLM  - use network access
```

---

# 7. Operator-readable explanation

The practical model is:

```
Phase 0 asks:“What files exist, how are they structured, and where are the explicit references?”Phase 1 asks:“What do the important files mean?”Phase 2 asks:“How should the durable wiki explain this knowledge?”
```

Phase 0 is cheap and repeatable. It should feel like running an indexer, not like asking an AI to understand the corpus.

The first useful success state is not a perfect graph or perfect search engine. It is this:

```
The next LLM chat can read phase0-navigation-report.md and know which 20–50 files to inspect first instead of opening hundreds blindly.
```

---

# 8. Exact acceptance criteria

## V1 must pass

```
phase0_v1_acceptance:  inventory:    - reuses_existing_source_inventory_if_present    - reports_inventory_missing_if_not_present  outputs:    - corpus-profile.md exists    - heading-map.json exists    - markdown-link-map.json exists    - frontmatter-map.json exists    - keyword-hits.ndjson exists    - topic-file-map.json exists    - source-priority-candidates.md exists    - phase0-navigation-report.md exists  quality:    - deterministic_output_order    - stable_paths    - no_llm_semantic_claims    - explicit_uncertainty_markers    - generated_files_are_human_readable_or_json_readable    - parser_warnings_are_reported_not_hidden  boundaries:    - no_phase1_ingest_analysis    - no_wiki_generation    - no_vector_db    - no_obsidian_app_dependency    - no_static_site_generator_requirement
```

## V1.5 must pass

```
phase0_v1_5_acceptance:  search:    - search-index.sqlite exists or unavailability is explained    - search-index-export.json exists    - example_queries_are_documented  graph:    - link-graph.json exists    - graph-summary.md exists    - process-flow-graph-audit.md exists    - explicit_edge_policy_exists    - parses_markdown_links    - parses_wikilinks    - parses_explicit_path_references    - parses_manifest_file_lists    - parses_supporting_files    - parses_canonical_source    - parses_script_path    - parses_owns_hands_off_to_does_not_own  reporting:    - hubs_reported    - orphan_candidates_reported    - missing_targets_reported    - process_flow_edges_reported    - graph_limitations_reported
```

---

# 9. Open question ranking

|Rank|Question|Decision now|
|---|---|---|
|1|Single script or several scripts?|Single consolidated script for V1.|
|2|Exact `phase0-navigation-report.md` contract?|Use the contract above. It is the main read-first artifact.|
|3|Should artifacts be written?|Yes, under `manifests/`, after local repo check.|
|4|How to determine source authority?|Path/source rules only; semantic authority deferred to Phase 1.|
|5|Should existing inventory be base input?|Yes. Reuse it.|
|6|SQLite FTS5 in V1 or V1.5?|V1.5 unless trivial locally.|
|7|Graph in V1 or V1.5?|V1 extracts simple links; V1.5 builds Apex graph.|
|8|Parse non-Markdown files?|V1 mostly Markdown/MDX plus inventory; V1.5 selectively parse YAML/JSON/Python path references.|
|9|Include semantic candidates?|Only as “LLM review needed,” never as deterministic truth.|
|10|Test Node/remark now?|No. Revisit only after parser failures.|

---

# 10. Final implementation recommendation

```
final_decision:  build_phase0: true  implementation_shape: "one deterministic local script plus manifest artifacts"  first_script: "apex-meta/scripts/phase0_corpus_intelligence.py"  first_target_kb: "apex-meta/kb/claude-skill-design/"  first_output_root: "apex-meta/kb/claude-skill-design/manifests/"  base_input: "existing source-inventory.json/csv"  v1_stack:    - source_inventory_reuse    - ripgrep_keyword_hits    - python_stdlib_parser    - heading_map    - markdown_link_map    - frontmatter_detection    - keyword_topic_map    - source_priority_candidates    - phase0_navigation_report  v1_5_stack:    - sqlite_fts5_if_available    - markdown_it_py_optional_validation    - apex_specific_link_graph    - graph_summary    - process_flow_graph_audit  deferred:    - Node_remark_unified    - MkDocs    - mdBook    - Docusaurus    - Obsidian_app    - vector_database    - embeddings
```

The next concrete step is **not** more research. It is to define the V1 script contract and then implement the deterministic artifact generator against the existing `claude-skill-design` inventory.