---
title: "Whole-Corpus LLM Wiki Repository Capability Analysis"
page_type: summary
kb_slug: "llm-wiki-project-repos"
source_refs:
  - "llm-wiki-llm-wiki-md"
  - "llm-wiki-main-readme-md"
  - "llm-wiki-main-llm-wiki-skill-md"
  - "llm-wiki-main-llm-wiki-wiki-schema-md"
  - "llm-wiki-main-llm-wiki-workflows-ingest-md"
  - "llm-wiki-main-llm-wiki-workflows-query-md"
  - "llm-wiki-main-llm-wiki-workflows-lint-md"
  - "llm-wiki-main-llm-wiki-scripts-hash-files-sh"
  - "llm-wiki-main-llm-wiki-scripts-check-stale-sh"
  - "llm-wiki-skill-main-readme-md"
  - "llm-wiki-skill-main-llm-wiki-skill-md"
  - "llm-wiki-skill-main-llm-wiki-references-schema-guide-md"
  - "llm-wiki-skill-main-llm-wiki-references-article-guide-md"
  - "llm-wiki-skill-main-llm-wiki-scripts-lint-wiki-py"
  - "llm-wiki-skill-main-audit-shared-src-anchor-ts"
  - "llm-wiki-skill-main-web-server-routes-graph-ts"
created_at: "2026-07-14T00:00:00+02:00"
updated_at: "2026-07-14T00:00:00+02:00"
confidence: "high"
claim_label: "source_backed_summary"
status: "active"
---

# Whole-Corpus LLM Wiki Repository Capability Analysis

## Executive finding

The repository evidence supports the criticism: an LLM wiki is valuable when it compiles a whole source collection into a persistent, cross-source knowledge structure. It is not valuable when it spends more effort producing shallow rewrites of a few selected files than a future AI would spend reading those files directly.

The three reviewed projects provide useful parts of a solution, but none implements the complete target by itself:

- `llm-wiki/` defines the correct compounding-wiki goal: each source is integrated into summaries, concepts, entities, contradictions, cross-links, and an evolving synthesis.
- `llm-wiki-main/` adds the strongest incremental-ingest machinery: source hashes, idempotent sentinels, a source manifest, two-phase ingest, proactive session guidance, query persistence, and semantic lint instructions.
- `llm-wiki-skill-main/` adds the strongest information architecture and human maintenance surface: hierarchical concept pages, per-source summaries, recursive navigation, a graph, structured audits, an Obsidian plugin, and a local web viewer.
- None requires a concept page to enumerate every relevant corpus file, classify each file's authority and freshness, preserve a source-specific snapshot, and explain the file's individual retrieval value.

That missing concept-to-source coverage layer is the decisive gap. Canonical-answer compilation and whole-corpus mapping are complementary views. Treating the first as a replacement for the second is the drift that made the Leela result low-value.

## Target lock

The target is a concept-centric compiled knowledge layer over the complete corpus.

For a concept such as **Skill Tree**, a future AI should be able to open one dossier and get:

1. A Macro/Meso/Micro explanation of the concept.
2. The complete set of corpus files that define, implement, update, exemplify, contradict, or historically describe it.
3. A dated snapshot of what each relevant file contributes.
4. An authority and freshness classification for every file.
5. Explicit supersession and contradiction relationships.
6. Exact source pointers for material claims.
7. A clear route to the current canonical answer without erasing historical or supporting evidence.

“Complete” does not mean that every file must appear on every concept page. It means every corpus file is inventoried, every concept candidate is evaluated, and every candidate receives a disposition: material evidence, supporting context, implementation evidence, example, historical version, proposal, duplicate, or false positive. No file disappears merely because a ranking favored another file.

## Macro / Meso / Micro conclusion

### Macro — why an LLM wiki exists

The original pattern's value proposition is persistent synthesis. Raw sources remain immutable; the wiki becomes a maintained model of the corpus; a schema tells the LLM how to ingest, query, cross-reference, and repair it. The payoff comes from avoiding repeated cross-source reconstruction and from preserving relationships that are expensive to rediscover: contradictions, supersession, implementations versus specifications, and concept-to-source coverage.

If a wiki merely paraphrases seven files, the economic argument collapses. Reading seven originals is usually cheaper and more reliable. Compilation becomes worthwhile when it converts a larger, overlapping, versioned corpus into answers and source relationships that would otherwise require repeated multi-file analysis.

### Meso — the reusable knowledge products

A useful compiled layer needs four coordinated products:

1. **Source atlas** — every file retains a unique repository-relative identity, hash, date/provenance, source type, and duplicate relationship.
2. **Concept dossiers** — Macro/Meso/Micro synthesis plus a complete per-concept source coverage table.
3. **Source snapshots** — one concise page or ledger entry per source recording its claims, concepts, authority, date, contradictions, and unique value.
4. **Retrieval routes** — an index/search layer that routes routine questions to answer-bearing dossier sections and routes provenance questions to source snapshots.

Canonical answer pages remain useful, but they sit on top of the atlas. A source can be non-canonical and still be valuable as history, implementation evidence, an example, or a contradiction.

### Micro — the minimum record needed per concept/source relationship

Each concept-source edge needs:

| Field | Purpose |
|---|---|
| `concept_id` | Stable concept identity and aliases. |
| `source_id` | Stable source identity; never basename-only. |
| `repository_path` | Exact original repository-relative path. |
| `source_hash` | Detects changed bytes and duplicate content. |
| `observed_at` / source date | Establishes the evidence time boundary. |
| `authority_role` | Current spec, implementation, contract, update, example, proposal, history, or unknown. |
| `read_status` | Complete, relevant sections reviewed, blocked, or false positive. |
| `coverage` | Definition, schema, workflow, rules, UX, examples, implementation, tests, history, or contradictions. |
| `source_snapshot` | What this individual file says about the concept. |
| `evidence_pointers` | Exact headings, passages, symbols, or line anchors. |
| `freshness_relation` | Current, superseded, partially superseded, undated, or unresolved. |
| `contradictions` | Conflicting sources and the exact disputed claim. |
| `individual_value` | Why a future AI should consult this source. |
| `canonical_effect` | Supports, qualifies, contradicts, or does not affect the current answer. |

Without these fields, a `sources:` list is only bibliography. It does not save future analysis work.

## Repository snapshots and authority

All three source trees were added to this repository by commit `4dceaa89a597c39ca657d536a48f58b2f4e4b5a9` on 2026-06-19. That commit is the local snapshot boundary, not proof that the snapshots match the latest upstream repositories.

| Repository snapshot | Local size | Authority in this analysis | Freshness assessment |
|---|---:|---|---|
| `source-knowledge/ProjectRepos/llm-wiki/` | 1 file, 11,985 bytes | Primary design-intent source | Abstract by design; no implementation version. Snapshot date is known, upstream revision is not. |
| `source-knowledge/ProjectRepos/llm-wiki-main/` | 54 files, 172,997 bytes | Primary for its own Claude Code implementation | `package.json` and `CHANGELOG.md` identify v0.1.0, released 2026-05-03. Snapshot commit is known; upstream commit is not. |
| `source-knowledge/ProjectRepos/llm-wiki-skill-main/` | 49 files, 342,347 bytes | Primary for its own skill, tooling, and audit implementation | README calls it experimental; packages identify v0.1.0. No changelog or captured upstream commit establishes newer/older status. |

For behavior claims, executable code outranks README promises. For intended workflow, the skill and reference files outrank incidental code comments. For the overall LLM-wiki purpose, the abstract `llm-wiki.md` is the direct design authority.

## Capability comparison

| Capability | Abstract `llm-wiki` | `llm-wiki-main` | `llm-wiki-skill-main` | Whole-corpus target status |
|---|---|---|---|---|
| Persistent compiled wiki | Defines the goal | Implements workflow | Implements workflow | Present |
| Immutable raw sources | Explicit | `.raw/` convention | `raw/` plus external refs | Present |
| One source updates many pages | Says 10–15 pages | Concept/person/article updates | Says 5–15 pages | Present as instruction, not coverage proof |
| Per-source summary | Recommended | Article page when warranted | Required summary page | Strongest in skill-main |
| Concept/entity pages | Explicit | Flat concept/person pages | Hierarchical concepts/entities | Present |
| Macro/Meso/Micro dossier | Not specified | Not specified | General split-by-aspect guidance | Missing |
| All relevant files per concept | Implied by comprehensive synthesis | No required inverted coverage ledger | No required inverted coverage ledger | Missing |
| Source hash and idempotency | Optional tooling idea | SHA-256 + sentinel + manifest | Not implemented in core skill | Strongest in main |
| Per-concept source-use trace | General references | Optional source fields and update note | `sources` list and source links | Incomplete |
| Source authority classification | Not specified | Confidence, contradiction review | Human schema notes | Missing as required metadata |
| Source freshness/supersession | Stale claims should be found | LLM full lint instructs drift checks | `updated` and open questions | No deterministic source freshness model |
| Contradiction preservation | Explicit | Callouts on both pages + review queue | Both claims + open question + audit | Present as instruction |
| Human feedback | Human may review | JSON review queue | Anchored audit files + UI | Strongest in skill-main |
| Query compounding | Save good answers | Synthesis pages | Query output promotion | Present |
| Retrieval | Index-first; optional qmd | 3–5 page index-first flow | Index; optional qmd | Present, no coverage guarantee |
| Graph/navigation | Obsidian suggested | D3 workflow | Recursive tree + graph APIs/UI | Strongest in skill-main |
| Structural lint | Suggested | Bash checks | Recursive Python seven-pass lint | Present |
| Semantic acceptance | LLM lint suggested | Same context performs full lint | Agent lint/audit | No independent answerability gate |

## What each repository contributes

### 1. `llm-wiki/`: the correct conceptual center

This single-file project gives the clearest statement of purpose. It rejects re-deriving knowledge from raw documents on each question. Ingest is supposed to integrate a source into the existing wiki by updating summaries, entities, concepts, contradictions, and cross-references. Lint is supposed to find stale claims superseded by newer sources, missing concepts, missing links, contradictions, and data gaps. The index is a catalog of everything in the wiki, not a shortlist of preferred sources.

Its main strength is restraint: it defines a pattern and expects the schema to be adapted to the domain. Its weakness is the same: it does not specify a custody-safe inventory, a concept-source ledger, or an objective completeness gate.

### 2. `llm-wiki-main`: incremental compilation and session automation

The most valuable mechanisms are:

- SHA-256 source hashing and per-hash ingestion sentinels.
- A source manifest recording source name, ingest date, language, and pages created or updated.
- Phase 1 analysis before Phase 2 page generation.
- “Add, do not overwrite” updates to existing concept pages.
- Dated “updated from source” notes.
- Contradiction callouts placed on both affected pages and a persistent review queue.
- Index-first queries that read a small set of compiled pages.
- Durable synthesis pages with `based_on`, contradictions, gaps, and confidence.
- Session-start guidance and a hot cache intended to keep the wiki active across conversations.
- A quick structural lint and a separate, LLM-intensive semantic lint.

Important limitations visible in the files:

- `check-stale.sh` hashes page frontmatter only. A changed page body or changed raw source can escape this freshness check.
- The source manifest is source-to-pages, not a complete concept-to-sources ledger.
- Concept frontmatter offers one optional `source_url` and `source_hash`; it does not model many source contributions, authority, supersession, or per-source snapshots.
- The deterministic scripts use `find ... -maxdepth 1`; broken-link, orphan, frontmatter, session-state, and freshness checks do not fully support a hierarchical wiki despite workflow references to `topics/`.
- Full contradiction, drift, quality, and gap lint is an LLM instruction, not an implemented independent validator.
- Staleness thresholds based on a page's `modified` date do not prove that underlying sources are current.
- The setup script configures SessionStart but not SessionStop, although the product describes both hooks as the hot-cache bridge.

Use this repository's hashing, idempotency, two-phase source integration, source-to-page manifest, proactive query route, and synthesis persistence. Do not treat its index-freshness check as source freshness or its manifest as whole-corpus concept coverage.

### 3. `llm-wiki-skill-main`: information architecture and human correction

The most valuable mechanisms are:

- A direct `compile / ingest / query / lint / audit` operating model.
- Required per-source summaries and updates to relevant concepts and entities.
- A recursive wiki structure with 400–1,200-word focused pages and folder-split concept hubs.
- A `CLAUDE.md` schema containing scope, current articles, open questions, research gaps, and audit backlog.
- Recursive tree and graph generation over nested Markdown pages.
- A seven-pass Python lint for links, orphans, index coverage, log shape, audit shape, and audit targets.
- Durable human feedback as anchored Markdown, with severity, author, source, target, exact selected text, and surrounding context.
- A shared TypeScript audit schema and anchor resolver used by both the Obsidian plugin and web viewer.
- A local browser UI for page rendering, Mermaid, KaTeX, navigation, graph viewing, and feedback filing.

Important limitations visible in the files:

- The standard concept page has a `sources` list but no per-source authority, freshness, source-specific contribution, or evidence pointers.
- Summary pages preserve takeaways but do not require a hash, repository revision, supersession relation, or concept coverage vector.
- No source inventory or source-change detector is part of the core skill.
- The lint recursively loads pages but keys lookup partly by filename stem. Repeated stems such as nested `index.md` pages can overwrite one another in the lookup map.
- “Frequently linked but no page” counts only explicit wikilinks; it is not a corpus concept-discovery pass.
- The web server defines an audit-resolution handler, but `web/server/index.ts` does not register a resolution route. Resolution remains primarily an agent-side workflow.
- Human audit is strong for correcting written pages but does not prove that all relevant source files were discovered.

Use this repository's hierarchical page architecture, concise source summaries, recursive browsing, graph, anchored audit format, and human review UI. Add source custody and concept-source coverage rather than assuming `sources: []` is sufficient.

## Why the selective Leela approach lost the value proposition

The prior Leela result optimized for a canonical-answer layer: choose a small number of ranked sources, write broad topic summaries, and mark unopened details as raw-source reopen triggers. That can be a useful *final-answer view*, but it is not a whole-corpus wiki.

It fails the target when:

- a topic page cannot list all files that materially discuss the topic;
- historical, proposal, implementation, update, and duplicate files are collapsed into silence rather than classified;
- a future AI must repeat corpus search to learn which files matter;
- summaries redirect routine domain questions back to readable raw sources;
- the process spends substantial tokens on contracts and validation while the reusable knowledge layer remains shallow.

The test is practical: if a future AI would be better off reading the selected originals, the compilation has not created enough information gain. Selecting seven sources from hundreds can identify a current answer, but it cannot support the claim that the corpus has been analyzed.

## The missing whole-corpus concept dossier

A concept dossier should be the primary unit of value. For a Leela feature such as Skill Tree, the page family should look like:

```text
wiki/concepts/skill-tree/
├── index.md                  # Macro definition, current state, navigation
├── model-and-contracts.md    # Meso architecture and relationships
├── rules-and-behavior.md     # Micro fields, rules, formulas, state changes
├── ux-and-user-flows.md      # Personas, flows, acceptance criteria
├── implementation-status.md  # Specification versus verified implementation
└── source-atlas.md           # Every relevant file and its individual value
```

This is not a mandate to create six pages for every concept. A small concept can remain one file. The invariant is the information, not the file count.

The `source-atlas.md` view should include one row per relevant file:

| Source | Date/revision | Role | What it says | Freshness | Relationship | Individual value |
|---|---|---|---|---|---|---|
| Current feature contract | Date/hash | Current specification | Exact model and required behavior | Current pending implementation check | Governs current answer | Primary field/rule authority |
| Prototype document | Date/hash | Prototype | Earlier UX and interaction model | Partially superseded | Explains design origin; conflicts on X | Useful for intent and discarded options |
| User-story file | Date/hash | Acceptance evidence | Personas, flows, permissions, success criteria | Current or unresolved | Qualifies contract behavior | Best end-to-end user view |
| Implementation file | Commit/hash | Implementation evidence | What runtime currently does | Current at captured commit | Confirms or contradicts spec | Best current-state evidence |
| Duplicate copy | Hash | Duplicate | Byte-identical or derived copy | Same as canonical copy | Consolidated, not discarded | Prevents double counting |

## Simple process that produces the dossier

The process does not need a large orchestration shell. It needs six clear stages and durable state:

1. **Inventory the whole corpus.** Preserve repository-relative paths, hashes, source dates/commits, and duplicate groups. Never flatten by basename.
2. **Build the concept candidate map.** Use deterministic headings, filenames, symbols, links, and keyword/alias scans to propose every file that may cover each concept.
3. **Review every candidate for one concept.** Read the complete file or all relevant sections; classify false positives explicitly. Record source-specific snapshots, evidence pointers, authority, dates, contradictions, and individual value.
4. **Write the dossier.** Synthesize Macro/Meso/Micro answers and the source atlas. Keep specification, proposal, history, and implementation distinct.
5. **Test retrieval.** In a clean context, answer the concept's routine and provenance questions from the dossier. A routine question should not require raw-source reopening; a forensic question may.
6. **Update incrementally.** When a file hash changes, revisit only the concepts connected to that source, refresh their source snapshots, and recalculate freshness/supersession.

This design spends semantic tokens on source interpretation and synthesis. Deterministic tools do inventory, hashes, candidate search, duplicate detection, link checks, and stale-edge detection. They should not generate pages or pretend to judge meaning.

## Current KB integrity audit

The current `llm-wiki-project-repos` KB cannot yet support a credible whole-corpus analysis from `raw/` alone.

### Source counts

- Physical source snapshots: 104 files total — 1 in `llm-wiki`, 54 in `llm-wiki-main`, and 49 in `llm-wiki-skill-main`.
- Manifest: 102 rows. The omitted files are the duplicate `llm-wiki-main/llm-wiki.md` and `.markdownlint-cli2.jsonc`.
- Current `raw/`: 87 files.
- Phase 0 corpus profile: 46 files scanned and 174,050 bytes.

### Basename collision loss

The source manifest has 11 `source_path` collision groups covering 26 logical source rows:

- `.gitignore` — 2 rows
- `package-lock.json` — 3 rows
- `package.json` — 4 rows
- `index.ts` — 2 rows
- `tsconfig.json` — 3 rows
- `SKILL.md` — 2 rows
- `main.ts` — 2 rows
- `styles.css` — 2 rows
- `README.md` — 2 rows
- `graph.ts` — 2 rows
- `tree.ts` — 2 rows

Only one physical raw file exists for each collision path. Therefore 15 manifest variants are not represented by their own file under `raw/`. The original snapshots remain available under `source-knowledge/ProjectRepos/`, which is why this analysis used those namespaced trees.

This is not a cosmetic issue. The two `SKILL.md` files describe different implementations, but `raw/refs/SKILL.md` can preserve only one of them. The four `package.json` files describe different packages, but `raw/refs/package.json` preserves one. Any semantic compiler restricted to `raw/` receives an incomplete and misleading corpus.

### Stale Phase 0

The 2026-07-06 Phase 0 report says the JSON source inventory was absent, scans 46 files, and reports no duplicate groups. The current manifest has 102 entries and the raw tree has 87 files. Phase 0 is therefore not an accurate navigation model of the current source set.

### Off-topic compiled subtree

`KB_v3/` is not a compilation of the three LLM-wiki repositories. Its own Phase 1 file states that it is scoped to `apex-meta/handoff/Apex-Kb_Lifecycle_Analysis/`, and its summary covers Apex KB lifecycle patches. It may be useful elsewhere, but inside this KB it is target drift and cannot satisfy repository-comparison or LLM-wiki knowledge goals.

## Evidence coverage of this analysis

The full 104-file source tree was inventoried by path, size, and extension, then compared with the 102-row manifest and checked for collision status. Seventy files were inspected directly at evidence level: 61 source-repository files and 9 current-KB files. Of the 61 source files, 54 were read with complete visible detail and 7 packaging/CI files were inspected structurally or in targeted sections where bulk output was truncated. All 25 TypeScript/MJS implementation units in `llm-wiki-skill-main` were additionally included in an exported-symbol and registered-route scan.

### Priority 0 — target and operating authority

- `source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md`
- `source-knowledge/ProjectRepos/llm-wiki-main/README.md`
- `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md`
- `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/WIKI_SCHEMA.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/README.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/schema-guide.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/article-guide.md`

### Priority 1 — ingest, compile, query, and maintenance workflows

- All six files under `llm-wiki-main/llm-wiki/workflows/`.
- All six files under `llm-wiki-main/llm-wiki/commands/`.
- All four files under `llm-wiki-main/llm-wiki/templates/`.
- The remaining skill-main references: `audit-guide.md`, `log-guide.md`, and `tooling-tips.md`.

### Priority 2 — deterministic and interactive implementation evidence

- Main implementation: `hash-files.sh`, `check-stale.sh`, `find-broken-links.sh`, `find-orphans.sh`, `validate-frontmatter.sh`, `init-wiki.sh`, `_utils.sh`, `setup-project.sh`, `session-start.sh`, and `session-stop.sh`.
- Skill-main Python: `scaffold.py`, `lint_wiki.py`, and `audit_review.py`.
- Audit implementation: `audit-shared/src/schema.ts`, `anchor.ts`, and `serialize.ts`; Obsidian `main.ts` and `writer.ts`.
- Web implementation: `routes/audit.ts`, `routes/tree.ts`, `routes/graph.ts`, and `routes/pages.ts`.
- Package contracts: the root main package plus audit-shared, Obsidian plugin, and web package manifests.
- Packaging/CI surfaces: main `quickstart.sh`, `install.sh`, `uninstall.sh`, and `scripts/ci-local.sh`.

### Priority 3 — provenance and current-KB truth

- Main `CHANGELOG.md`, `FAQ.md`, `WIKI.md`, and the duplicated abstract `llm-wiki.md`.
- KB `README.md`, `kb-schema.md`, source manifest, setup/Phase 0 report, corpus profile, navigation report, and index.
- `KB_v3` Phase 1 analysis, summary, and semantic compile report.

Community policy, styles, lockfiles, demo sources, and build configuration were inventoried but were not treated as semantic design authorities. They remain relevant for packaging and runtime reproduction, not for deciding what a whole-corpus wiki must know.

## Final decision

The LLM-wiki projects do not justify the selective seven-source outcome. Their shared value claim is compounding integration across a growing corpus. The local Apex KB then introduced two additional failures: lossy basename-flattened custody and a Phase 0 view that covered less than half the manifest.

The correct synthesis is:

- Keep the original pattern's persistent, whole-corpus goal.
- Reuse `llm-wiki-main` for hashes, idempotent source ingestion, update notes, contradiction workflow, and durable query synthesis.
- Reuse `llm-wiki-skill-main` for hierarchical concept dossiers, source summaries, recursive navigation, graphs, and anchored human audits.
- Add the missing concept-source atlas with authority, date, snapshot, freshness, contradiction, and individual-value fields.
- Treat canonical-answer pages as a projection of that atlas, not as permission to ignore most of the corpus.

For the Leela-sized use case, this is the difference between a wiki and a rewrite. The wiki should save the next AI from discovering which files matter, how they differ, and which one is current. If it does not save that work, it has not compiled the knowledge base.
