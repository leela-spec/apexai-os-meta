# Pro Thinking Apex KB Final Architecture

```yaml
repository_owner: leela-spec
repository_name: apexai-os-meta
repository_full_name: leela-spec/apexai-os-meta
branch: main
research_start_commit: bc353b7f16d2c5ad74f376452ad4c1ff45278995
research_package_root: FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch
path_style: repository_relative
evidence_mode: full_repository_evidence
research_date: 2026-07-14
```

# 1. Target Lock

## 1.1 Final purpose

Apex KB is one complete, configurable knowledge-compilation architecture whose durable product is not merely a set of wiki pages. Its product is the combination of:

1. complete source custody and scope closure;
2. lossless, inspectable concept-to-source intelligence;
3. reusable semantic understanding of unique source content;
4. a Macro/Meso/Micro concept dossier for each configured concept;
5. a durable source atlas that represents every reviewed concept candidate;
6. accepted compiled knowledge and a derived retrieval layer;
7. dependency-aware incremental maintenance; and
8. execution packets that let deterministic tools, Codex, and a strong semantic model cooperate without duplicating each other's work.

The architecture must make a future AI faster and more complete than rereading the raw corpus. The source map and source atlas are first-class product surfaces, not temporary preprocessing.

## 1.2 Exact future-AI jobs

| Job | Required durable surface | Success behavior |
|---|---|---|
| Find every source that may matter to a configured concept | Exhaustive machine topic map | Returns every configured-vocabulary candidate, with exact reasons and pointers, without top-N loss. |
| Understand why a file surfaced | Topic-map match evidence and compact projection | Exposes path, filename, title, H1, heading, body, link, graph, co-occurrence, duplicate, and date/version signals separately. |
| Reconstruct the documentary landscape | Topic semantic record and source atlas | Distinguishes current, historical, prototype, implementation, contextual, duplicate, superseded, incidental, blocked, and irrelevant-after-review material. |
| Answer what the concept means | Concept dossier | Gives direct answers and Macro/Meso/Micro synthesis, with contradictions and uncertainty visible. |
| Locate exact evidence | Source capsules, atlas rows, and dossier claim pointers | Resolves to stable line, section, page, slide, paragraph, shape, sheet/cell, or asset-region pointers. |
| Avoid rereading unchanged evidence | Hash-keyed source capsules and impact graph | Reuses unchanged semantic records and rereads only changed or newly relevant evidence. |
| Diagnose omissions or bad synthesis | Inventory, exhaustive maps, semantic dispositions, acceptance artifact | Shows whether failure came from scope, extraction, candidate discovery, source review, synthesis, acceptance, or retrieval. |
| Query quickly | Accepted wiki index plus row-aware lexical retrieval | Starts from compiled dossiers and atlas rows, not raw-source search, while preserving raw reopen paths. |
| Maintain incrementally | Changed-source impact record | Invalidates only affected maps, capsules, topic analyses, pages, atlases, acceptance records, and retrieval chunks. |
| Execute across tools honestly | Run manifest and semantic task packet | Records repository commit, profile, hashes, actual model/mode, write scope, outputs, blockers, and changed paths. |

## 1.3 Durable product targets

### Concept dossier

A concept dossier must:

- answer the configured critical and routine target questions directly;
- synthesize the concept at Macro, Meso, and Micro levels;
- explain the current state, evolution, implementation reality, alternatives, and contradictions where evidence supports them;
- cite source capsule and exact evidence pointers;
- route source-location questions to the source atlas rather than duplicating its rows;
- expose uncertainty and raw-source reopen conditions; and
- use a page topology chosen by stable query value, not a mechanical word-count gate.

### Source map and source atlas

For every configured concept, the product must preserve three related but non-interchangeable surfaces:

1. **Exhaustive deterministic topic map** - every deterministic candidate and the inspectable evidence that caused inclusion.
2. **Canonical topic semantic record** - one semantic row for every deterministic candidate, including review coverage, lifecycle role, disposition, authority, freshness, snapshot, individual value, relationships, blockers, and exact pointers.
3. **Durable source atlas view** - a lossless LLM/human-facing rendering of the canonical semantic record, with stable routes and category navigation.

The compact navigation projection may be bounded. It must always point to and disclose counts from the exhaustive set; it can never replace that set.

## 1.4 Ownership lock

| Owner | Owns | Must not own |
|---|---|---|
| Operator | Corpus roots/exclusions, configured topics, policy choices, profile selection, high-risk promotion decisions | Repetitive file classification or deterministic validation |
| Deterministic runtime | Inventory, hashing, extraction status, structure spans, postings, candidate maps, duplicate evidence, graph facts, schema validation, impact calculation, retrieval rebuild, observable postflight | Semantic relevance, authority, freshness truth, contradiction resolution, conceptual synthesis |
| Semantic model | Source reading, candidate disposition, authority/freshness judgment, contradiction/supersession interpretation, source capsules, topic analysis, dossier authorship, semantic evaluation | Local lifecycle commands, Git writes, commits, pushes, deterministic completion claims |
| Codex/orchestrator | One-time scope/profile capture, deterministic commands, bounded packets, artifact import, changed-path verification, tests, Git operations | Deep-reading the corpus, shallow duplicate synthesis, semantic acceptance from insufficient context |
| Independent semantic context | Only acceptance work whose failure-prevention value is demonstrated | Re-running deterministic checks or re-authoring the same dossier |

## 1.5 Configuration lock

Configuration changes the work performed in a run, not the completeness of the architecture. A run may stop at `map_ready`, `semantic_partial`, or `compiled_unvalidated`; only the full required evidence and acceptance path may produce `query_ready`.

A capability can be:

- `keep`
- `change`
- `add`
- `merge`
- `remove`
- `configurable`
- `reject`
- `requires_evidence_probe`

No maturity-track label is part of the architecture.

## 1.6 Measurable success conditions

| Condition | Default acceptance measure |
|---|---|
| Scope closure | 100% of files below active roots appear in inventory as included, excluded-with-reason, blocked, unreadable, or profile-disabled. |
| Candidate-map losslessness | No top-N truncation; every included candidate has at least one inspectable match or graph reason and an exact pointer where technically possible. |
| Semantic disposition closure | 100% of topic-map candidates have one semantic row or an explicit blocked/unavailable state. |
| Core evidence coverage | Every current/core source is fully read or explicitly blocked; targeted reads record exact covered ranges and rationale. |
| Atlas completeness | Atlas semantic-row count equals exhaustive candidate count; every row has snapshot, individual value, lifecycle/disposition, review mode, and pointer/blocker. |
| Evidence integrity | 100% of material dossier claims resolve to accepted source pointers or are labeled inference/operator decision/uncertainty. |
| Contradiction integrity | Every material unresolved contradiction discovered in reviewed evidence is visible in the dossier or atlas. |
| Fresh-context answerability | All critical target queries pass from accepted compiled pages alone; routine queries meet the configured threshold. |
| Incremental reuse | Unchanged source hashes are not reread unless a changed target question, authority rule, or explicit evidence gap makes rereading necessary. |
| Retrieval freshness | Query-ready state requires accepted pages and atlas rows to match the retrieval input hash set. |
| Token value | On the configured canary set, the accepted compiled route must use fewer source-reading tokens than the raw-corpus baseline; the default target is at least a 50% reduction without losing required answers or source coverage. |
| Source-location utility | At least 95% of configured source-location canaries are answerable from the atlas without reopening readable raw sources. |

## 1.7 Explicit non-success proxies

The following never prove product success by themselves:

- file, page, heading, word, source, or commit counts;
- a ranked list without the exhaustive candidate set;
- a populated template whose claims are not source-grounded;
- a retrieval index over shallow pages;
- passing frontmatter or broken-link checks;
- a model's statement that it read everything;
- an independent evaluator that never checks atlas completeness;
- a source-atlas filename containing only used sources;
- a graph visualization without lossless source roles; or
- more ledgers, hooks, gates, and fields than downstream consumers require.

## 1.8 Prohibited failure modes

1. Incomplete-version drift: efficiency, priority, configuration, or token control must never become permission to design a partial product.
2. Candidate truncation: bounded projections may not remove candidates from the canonical map.
3. Deterministic-authority drift: paths, dates, filenames, scores, and links are evidence signals, not semantic verdicts.
4. Semantic compensation drift: more LLM process may not be used to compensate for incomplete deterministic discovery.
5. Atlas evaporation: candidate/source classification may not disappear after page generation.
6. Retrieval masking: retrieval readiness may not turn shallow compilation into accepted knowledge.
7. Duplicate metadata drift: one fact or schema field must have one canonical owner and generated projections elsewhere.
8. Ledger bureaucracy: run state may preserve completed work, but it may not become a second semantic knowledge base.
9. Guardrail bureaucracy: retain only checks that prevent an observed failure, protect source custody, constrain writes, or eliminate repeat work.
10. Blocked-source invisibility: unsupported, unreadable, scanned, missing, or connector-inaccessible evidence must remain visible.
11. Tool-surface fiction: browser and connected-app routes must not be described as able to mutate Git when they are read-only.
12. Model-label hard-coding: record the actual model/mode used; require the strongest suitable available reasoning mode rather than a marketing name.

# 2. Evidence Mode and Source Truth

## 2.1 Selected mode

**Mode A - `full_repository_evidence`.**

The GitHub connector opened all three sentinel files completely and preserved repository-relative identities:

| Sentinel | Result |
|---|---|
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/00-START-HERE.md` | Complete read succeeded. |
| `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/02-LIFECYCLE-COMPONENT-VALUE-MAP.md` | Complete read succeeded. |
| `.claude/skills/apex-kb/SKILL.md` | Complete read succeeded. |

`main` resolved at research start to commit `bc353b7f16d2c5ad74f376452ad4c1ff45278995` (`Reorganize Apex KB research corpus and sync orchestration docs`). The same ref was used for package files, current implementation files, LLM-Wiki blueprints, and compiled Claude/orchestration sources.

No public-page, raw-URL, or uploaded-snapshot fallback was needed. Uploaded Project Sources were used only as corroborating snapshots, not as current implementation authority.

## 2.2 Available evidence

### Current repository implementation

Read directly from current `main`:

- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/package-manifest.md`
- material files under `.claude/skills/apex-kb/references/`, `templates/`, `examples/`, and `assets/`
- `apex-meta/scripts/apex_kb.py`
- `apex-meta/scripts/apex_kb_retrieval.py`
- current command-level acceptance material and schemas

### Prepared package

Files `00` through `06` were read in numeric order. The package was treated as research intent and routing guidance, not implementation truth.

### Blueprint evidence

Read directly:

- `source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md`
- `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md`
- relevant `workflows/ingest.md`, `workflows/query.md`, and `workflows/lint.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md`
- `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/references/article-guide.md`

### Claude/skill/orchestration evidence

Read compiled current KB pages covering information design, resilient script-owned workflows, agent/subagent boundaries, hooks/rules/memory, and Apex-specific orchestration patterns.

### Current external primary evidence

Official sources were used for current Deep Research/GitHub-app behavior, Codex cloud/Git behavior, Claude Code skills/subagents/hooks/workflows, Agent Skills progressive disclosure, SQLite FTS5, Python SQLite, YAML safe loading, Markdown parsing, PDF extraction, and Office-format libraries.

## 2.3 Evidence-class rules applied

| Evidence class | Rule used in this report |
|---|---|
| Operator target | Binding unless internally contradictory; highest product authority. |
| Current implementation fact | Must come from current `main` code/files at the resolved commit. |
| Existing Apex research intent | Seed hypothesis or prior decision; verified against current code and product target. |
| LLM-Wiki blueprint evidence | Mechanism evidence, never a complete Apex solution by itself. |
| Claude/skill/orchestration evidence | Required for file, workflow, script, hook, and handoff micro-design. |
| External primary evidence | Used only for current technical/product facts and feasibility. |
| Inference | Explicitly identified when connecting evidence. |
| Recommendation | Final architecture decision in this report. |

## 2.4 Verified current implementation facts

1. `rank_topic_sources()` lowercases registry keywords, counts line-level substring occurrences, retains a single sample, sorts by hit count/path, and returns only the first 30 files. This is the decisive source-loss defect.
2. Phase 0 separates neither path, filename, title, H1, heading, body, link, and co-occurrence evidence nor strong and ambiguous vocabulary.
3. `phase0-navigation-report.md` is currently an artifact list and phase-boundary statement, not a populated corpus-navigation product.
4. Runtime artifact names and reference-contract artifact names have drifted.
5. Exact hash duplicates appear in a corpus profile but do not drive topic routing or semantic reuse.
6. Current semantic rules materially improve the stopping condition: target queries, candidate/read/used distinctions, source dispositions, page-only evaluation, and material-claim entailment are present.
7. Those semantic safeguards start downstream of the lossy candidate ranking and do not require a durable source atlas.
8. `apex_kb_retrieval.py` has a strong derived-retrieval boundary: compiled pages only, heading chunks, input hashes, runtime FTS5 probing, BM25 when available, and unconditional JSON fallback.
9. Current retrieval is not row-aware for a source atlas because that product does not yet exist.
10. Current acceptance schemas test query answerability and claim support but not deterministic candidate completeness, atlas row completeness, or atlas faithfulness.
11. The package has substantial contract/template duplication and one explicitly deprecated lifecycle file still present.
12. The inspected acceptance surface is primarily a manual command/runbook suite; no dedicated current Apex-KB automated test module was found in the searched package/runtime paths.

## 2.5 Current implementation versus old snapshot

The prepared package records an earlier implementation snapshot. That older commit remains useful provenance, but this report's implementation claims come from `bc353b7f16d2c5ad74f376452ad4c1ff45278995`. Older reports that lacked repository access are evidence of intent or alternatives only.

## 2.6 External constraints that affect the final design

- Deep Research can use uploaded files, the web, selected sites, and enabled apps; connected-app use in Deep Research is read-oriented, and the GitHub app does not write to repositories. Therefore ChatGPT web semantic work must return an artifact bundle for Codex to import unless a later write-capable integration is technically proven.
- Codex cloud can connect to GitHub, run isolated tasks, expose diffs, and open pull requests, so Git mutation and review belong on the Codex side of the boundary.
- Claude Code and Agent Skills both use progressive disclosure: metadata first, full `SKILL.md` on activation, and supporting references/scripts only as needed. This supports a short router with focused references.
- Script-owned workflows retain orchestration state outside a model context and are the stronger basis for resumable high-volume deterministic work.
- SQLite FTS5 is a local full-text engine with ranking and snippets, but availability is compile-time/runtime dependent and external-content synchronization can become inconsistent. Apex's current rebuildable-index and runtime-probe policy is therefore correct.
- PDF text extraction is not OCR; scanned/image-only evidence must have a distinct blocked or visual-semantic route.

# 3. Verified and Updated Lifecycle Component and Value Map

## 3.1 Scoring method

Dimensions are scored 1-100 in five-point bands unless direct evidence justifies a boundary value:

- `T` target contribution
- `M` current mismatch
- `G` achievable knowledge-value gain
- `S` token-saving potential
- `D` deterministic leverage
- `L` downstream leverage
- `F` failure severity if absent/wrong
- `R` resilience contribution
- `IC` implementation cost
- `RC` recurring token/compute/maintenance cost
- `C` evidence confidence

Priority orders research opportunity, not truth:

```text
opportunity = (M/100) * (G/100) * (L/100) * 100
priority = opportunity * (0.65 + 0.20*(F/100) + 0.15*(C/100))
```

Implementation cost is shown separately because a high-value component is not removed merely for being expensive.


|ID|Component|Disp.|Owner|T|M|G|S|D|L|F|R|IC|RC|C|P|Deps|
|---|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|A01|Corpus scope and explicit exclusions|add|operator+runtime|100|90|95|90|95|100|100|95|35|10|98|85.2|A03,A05|
|A02|Topic registry: questions, phrases, aliases, negatives|change|operator+LLM|100|70|95|95|85|100|95|90|40|25|97|65.5|A01|
|A03|Source intake and raw/pointer custody|keep|runtime+operator|95|20|70|70|90|95|95|95|25|20|98|13.1|A01|
|A04|Source manifest and payload custody records|merge|runtime|90|55|75|65|90|90|85|90|35|20|94|35.7|A03,A05|
|A05|Exhaustive inventory, hashes, extraction status|change|runtime|100|55|95|95|100|100|100|100|45|15|99|52.2|A01,A03|
|A06|Source-format adapter registry and blocked visibility|configurable|runtime|90|80|85|80|90|85|90|85|75|40|82|55.1|A05|
|A07|Git/path/date/lifecycle deterministic hints|add|runtime|85|90|80|75|85|90|80|80|45|20|90|61.2|A05|
|A08|Exact, normalized duplicate, and version-family evidence|add|runtime+LLM|95|85|90|95|95|95|90|90|55|20|93|70.5|A05,B01|
|B01|Structure extraction with stable section spans|change|runtime|100|60|95|95|100|100|95|95|50|20|97|56.2|A05,A06|
|B02|Field-separated term postings|add|runtime|100|100|100|100|100|100|100|95|55|15|99|99.9|A02,B01|
|B03|Negative and ambiguous term handling|add|runtime+operator|95|95|95|95|90|95|95|90|45|15|98|84.6|A02,B02|
|B04|Deterministic relationship graph|configurable|runtime|75|70|70|70|85|75|65|75|65|35|88|33.5|B01,A07|
|B05|Exhaustive per-topic candidate map|add|runtime|100|100|100|100|100|100|100|100|60|20|99|99.9|B02,B03,A08,B04|
|B06|Compact LLM navigation projection|add|runtime|95|90|95|100|95|100|90|90|35|10|98|83.5|B05|
|B07|Populated navigation and batch-planning report|change|runtime|85|95|90|95|90|90|85|85|35|10|98|74.4|B05,B06|
|B08|Inspectable sort vector and read order|add|runtime|90|95|90|95|95|90|85|85|40|15|97|74.3|B05|
|B09|Corpus profile and generic term orientation|keep|runtime|55|20|35|40|80|45|35|80|20|10|97|2.7|A05|
|C01|Hash-keyed reusable source capsule|change|LLM|100|85|100|100|70|100|95|90|60|35|96|83.6|A05,B05|
|C02|Per-topic disposition for every candidate|change|LLM|100|75|100|95|45|100|100|95|65|50|98|74.8|B05,C01|
|C03|Authority, freshness, and lifecycle judgment|change|LLM|100|65|95|85|20|95|100|90|60|45|95|58.2|C01,C02,A07|
|C04|Contradiction, duplicate, and supersession judgment|change|LLM|100|45|90|80|25|95|95|90|60|45|96|37.9|C01,C02,A08|
|C05|Macro/Meso/Micro concept dossier|change|LLM|100|60|100|95|20|100|100|95|70|50|97|59.7|C02,C03,C04|
|C06|Durable per-concept source atlas|add|LLM+runtime|100|100|100|100|55|100|100|100|65|35|99|99.9|C02|
|C07|Entity pages and dossier topology|configurable|LLM|65|35|55|50|15|60|45|65|45|35|90|10.1|C05|
|C08|External verification with source custody|configurable|LLM+operator|70|45|75|55|10|65|75|70|55|70|90|20.5|C03|
|C09|Bounded semantic task packet and output bundle|add|orchestrator+LLM|90|85|90|85|70|95|90|90|50|25|95|70.7|B07,C01|
|D01|Deterministic schema, pointer, and coverage validation|change|runtime|100|55|90|85|100|95|95|100|50|15|98|46.4|B05,C01,C02,C05,C06|
|D02|Fresh-context page-only answerability|keep|independent LLM|95|25|85|65|10|85|90|80|50|60|99|17.7|C05|
|D03|Material-claim entailment review|keep|independent LLM|100|30|90|55|10|90|100|85|65|65|98|24.2|C05,C01|
|D04|Topic-map and atlas completeness/faithfulness|add|runtime+independent LLM|100|100|100|90|75|100|100|100|65|55|99|99.9|B05,C06|
|D05|Truthful partial, blocked, accepted, and query-ready states|change|runtime+LLM|95|55|90|75|85|95|100|100|45|20|98|46.9|D01,D02,D03,D04|
|D06|Independent semantic context activation policy|configurable|orchestrator|75|20|65|35|30|70|80|75|45|55|92|8.6|D01|
|E01|Compiled wiki index|keep|runtime|85|20|65|80|95|85|75|90|25|10|98|10.5|C05,C06,D05|
|E02|SQLite FTS5/BM25 with JSON fallback|keep|runtime|85|20|70|90|100|80|70|90|40|20|99|10.5|E01|
|E03|Row/section-aware source-atlas indexing|add|runtime|95|100|95|100|95|95|90|90|45|15|97|88.0|C06,E02|
|E04|Cited query evidence packet|change|runtime+LLM|85|35|75|85|80|75|70|85|35|25|96|18.4|E01,E02|
|E05|Promotion of durable query synthesis|configurable|LLM+operator|60|25|55|60|10|55|45|55|35|35|88|6.6|E04,D05|
|E06|Raw-source fallback boundary|keep|LLM|90|15|70|75|60|80|90|90|20|20|98|8.2|E04|
|F01|Hash staleness and changed-source detection|keep|runtime|100|25|85|100|100|100|95|100|35|10|99|21.0|A05,C01|
|F02|Artifact dependency and impact graph|add|runtime|100|95|100|100|100|100|100|100|70|15|97|94.6|A05,B05,C01,C02,C05,C06|
|F03|Incremental capsule/topic/dossier/atlas update|add|runtime+LLM|100|85|100|100|85|100|95|95|70|40|96|83.6|F01,F02|
|F04|Human audit feedback lifecycle|change|operator+LLM|75|35|70|55|25|70|75|80|40|35|94|16.1|C05,C06|
|F05|Structural lint|keep|runtime|80|15|55|70|100|70|75|95|25|10|99|5.5|D01|
|F06|Impact-bounded semantic lint|change|LLM|80|70|80|70|20|80|80|80|55|55|94|42.6|F02|
|F07|Run manifest and minimal recovery state|add|orchestrator+runtime|80|75|75|80|80|85|85|90|40|15|92|45.8|C09,F02|
|G01|Independent configuration axes|add|operator+runtime|90|90|85|70|80|85|85|85|50|20|97|62.8|A01,A02|
|G02|Named run-purpose profiles|add|operator+orchestrator|85|85|80|75|70|80|80|85|45|15|96|51.9|G01|
|G03|Terminal, connector, and browser execution surfaces|add|orchestrator|85|80|80|70|50|85|85|80|55|25|93|52.2|G01,C09|
|G04|Codex orchestration and task-packet loop|add|Codex|90|100|90|85|80|95|90|90|70|30|86|82.0|C09,G03,F07|
|G05|ChatGPT web semantic authoring bundle|add|ChatGPT web|100|100|100|90|10|100|100|90|65|60|88|98.2|C09,G03|
|G06|Changed-path and Git verification|keep|Codex|90|45|75|75|95|90|90|95|35|15|95|29.5|G04|
|G07|Actual model/mode and run provenance|add|orchestrator|65|80|60|40|70|65|60|75|25|10|93|28.4|G04,G05|
|G08|Hooks and guardrails tied to demonstrated failures|change|runtime+orchestrator|65|65|55|45|80|55|70|70|35|20|96|18.4|D01,G06|
|H01|Compact SKILL router with progressive disclosure|change|skill package|90|75|80|80|60|90|80|85|45|10|99|51.8|all|
|H02|Canonical focused reference contracts|merge|skill package|90|85|85|80|70|90|85|90|55|15|98|62.9|H01|
|H03|Templates and machine schemas|merge|skill package|90|80|85|75|80|90|85|90|60|15|98|59.2|H02|
|H04|Modular deterministic runtime behind stable CLIs|change|runtime|95|70|85|70|100|95|90|95|80|20|97|55.1|A05,B05,D01,F02,E02|
|H05|Automated unit/integration fixtures and real canaries|add|runtime+evaluator|100|85|95|75|100|100|100|100|75|20|96|80.3|H04|
|H06|Compatibility and migration layer|add|runtime|85|70|75|55|90|85|85|90|60|15|94|42.9|H02,H03,H04|
|H07|Operator examples and generated command reference|change|skill package|65|55|55|60|55|60|55|75|30|10|96|16.4|H01,H02|

## 3.2 Instrument and tool map

|ID|Instrument|Disposition|T|M|G|S|D|L|F|R|IC|RC|C|Rationale|
|---|---|---|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---:|---|
|T01|Python 3 standard library|keep|95|10|80|80|100|95|90|95|20|10|99|Stable cross-platform runtime and current implementation base.|
|T02|Git metadata and hashing|keep|90|20|80|90|100|95|90|95|25|10|99|Source identity, last-change evidence, and change detection.|
|T03|ripgrep as auxiliary diagnostic|keep|55|20|45|65|80|50|35|80|15|10|98|Useful operator/debug surface; not the canonical map engine.|
|T04|State-machine Markdown parser|keep|95|35|90|95|100|95|90|90|40|20|97|Fence-aware deterministic structure with stable pointers.|
|T05|PyYAML safe loader|change|70|45|70|55|90|75|80|85|25|15|94|Use safe_load when available; malformed frontmatter remains visible.|
|T06|markdown-it-py validator|configurable|55|60|55|45|70|55|45|70|35|20|85|Activate only for demonstrated Markdown/MDX boundary failures.|
|T07|pypdf text extraction|configurable|70|80|65|60|80|65|70|65|45|30|85|Digitally born PDF support; scanned pages remain blocked/visual.|
|T08|python-docx adapter|configurable|60|100|60|55|80|60|55|70|40|25|80|Paragraph/table extraction with stable ordinal pointers.|
|T09|python-pptx adapter|configurable|60|100|60|55|80|60|55|70|45|25|80|Slide/shape text extraction; unsupported visual semantics visible.|
|T10|openpyxl + defusedxml adapter|configurable|65|100|65|60|80|65|65|65|50|30|82|Sheet/cell extraction; security dependency must be probed.|
|T11|SQLite FTS5/BM25|keep|80|20|70|90|100|80|70|90|40|20|99|Current probed backend is sound; remains derived.|
|T12|JSON lexical fallback|keep|75|10|60|75|95|70|75|95|20|15|99|Unconditional portability when FTS5 is absent.|
|T13|Vector or hybrid retrieval|requires_evidence_probe|50|100|45|35|45|45|35|45|80|70|65|Adopt only if measured lexical/atlas retrieval failures justify cost.|
|T14|Deterministic relationship graph extractor|configurable|70|70|70|70|85|75|65|75|65|35|88|Useful for path/YAML/process edges, not mandatory for every run.|
|T15|OCR engine|configurable|55|100|55|45|60|55|60|45|75|65|70|Use only for scanned/image sources; record confidence and page coverage.|
|T16|Node remark/unified stack|requires_evidence_probe|45|100|45|35|65|45|35|55|70|45|70|Only if corpus fixtures prove Python adapters inadequate.|
|T17|fd/tokei/scc/cloc corpus utilities|reject|20|100|15|15|30|15|10|30|35|25|90|Convenience statistics do not justify extra core dependencies.|
|T18|MkDocs/mdBook/static-site index|reject|25|100|20|20|35|20|15|35|70|50|90|Publishing stack duplicates retrieval without source-atlas value.|
|T19|Obsidian application/plugin|reject|20|100|15|15|20|15|10|25|65|55|90|Viewer convenience, not a lifecycle dependency or source of truth.|
|T20|Official-web verification route|configurable|70|45|75|55|10|65|75|70|55|70|95|Use for unstable claims; save durable evidence or label as transient.|

## 3.3 Corrected lifecycle

```text
Operator target and profile
  -> explicit scope and source custody
  -> exhaustive inventory and extraction visibility
  -> structure/postings/duplicate/graph evidence
  -> exhaustive per-topic candidate maps
  -> compact navigation and semantic task packets
  -> reusable hash-keyed source capsules
  -> one semantic disposition row per candidate
  -> Macro/Meso/Micro dossier plus lossless source atlas
  -> deterministic completeness checks
  -> fresh-context answerability, entailment, and atlas-faithfulness checks
  -> accepted compiled index and row-aware retrieval
  -> change detection, impact calculation, bounded refresh, and Git publication
```

### Added or materially changed components

The decisive additions are: corpus-scope closure, format-adapter visibility, field-separated postings, negative/ambiguous vocabulary, exhaustive topic maps, compact projections, populated navigation, hash-keyed capsules, canonical topic semantic records, durable atlases, map/atlas acceptance, impact graphs, named run profiles, task packets, run manifests, row-aware atlas retrieval, automated fixtures, and compatibility migration.

### Merged or removed components

- Merge duplicate custody facts; retain one source manifest and one exhaustive inventory.
- Merge overlapping lifecycle, semantic, script, query, and runbook prose into focused canonical references.
- Replace the all-purpose semantic run ledger with source capsules, topic analyses, and a small run manifest.
- Remove the deprecated lifecycle reference from the operational package after compatibility migration.
- Remove spec-only generic repo-router and historical-path guardrail files from the Apex KB package; place any retained general lint capability under a separate repository-validation owner.
- Remove global structural source-priority scoring as a topic-reading authority.
- Reject static-site builders, Obsidian, and corpus-statistics utilities as core dependencies.

# 4. Research Grouping and Priority Order

## 4.1 Groups

| Priority | Research group | Mean opportunity score | Why coherent | Focused source bundle |
|---:|---|---:|---|---|
| 1 | Source custody, deterministic corpus intelligence, and durable maps | 61.3 combined | Scope, extraction, postings, duplicate evidence, graph facts, and topic maps share the same deterministic data model and directly cause the current loss. | Package `00-03`; current `apex_kb.py`; parser/tool/graph research; LLM-Wiki hash/index mechanisms; official parser/format docs. |
| 2 | Semantic source analysis, dossier, and source atlas | 57.3 | Capsules, candidate dispositions, authority, contradictions, dossier, and atlas must share one semantic record and page plan. | Current semantic contract/templates/ledger; original LLM-Wiki; operational ingest; typed wiki/article guide; Deep Research source behavior. |
| 3 | Configurable profiles and Codex/ChatGPT/deterministic orchestration | 52.9 | Profiles, execution surfaces, task packets, save batches, and provenance govern the same cross-tool boundary. | Current SKILL/browser runbook; Claude workflows/subagents/hooks; OpenAI Deep Research, GitHub app, Codex cloud; Agent Skills. |
| 4 | Apex skill package, contracts, templates, runtime, and tests | 52.7 | Progressive disclosure, single schema ownership, stable CLI wrappers, modular code, fixtures, and compatibility migration are one implementation-surface decision. | Current package manifest and all active references/templates; compiled orchestration design; Agent Skills and Claude skills docs. |
| 5 | Incremental maintenance and impact analysis | 44.2 | Hashes, dependency edges, invalidation, bounded semantic refresh, lint, audits, and recovery all consume the same change graph. | Current manifests/status/postflight; LLM-Wiki hashing/lint/audit; script-owned workflow evidence. |
| 6 | Semantic acceptance and truthful completion | 40.6 | Deterministic completeness, page-only query tests, entailment, atlas faithfulness, and state transitions must produce one verdict. | Current semantic acceptance/quality/postflight/tests; LLM-Wiki two-phase and lint; fresh-context evaluation design. |
| 7 | Retrieval and query behavior | 23.7 | Current retrieval is comparatively strong; the main work is to index atlas rows and consume accepted products without expanding authority. | Current retrieval script/contract/query template; LLM-Wiki query workflow; SQLite/Python primary docs. |

The combined score for Group 1 is derived from the `scope` and `maps` components. The order is research opportunity order. Implementation order is dependency-driven and differs below.

## 4.2 Implementation dependency order

1. Freeze current behavior in compatibility fixtures and record the current artifact set.
2. Establish canonical config and schema ownership.
3. Modularize inventory/extraction/topic-map code behind the existing CLI.
4. Generate exhaustive maps and compact projections.
5. Migrate semantic records to hash capsules plus one topic analysis.
6. Render dossiers and source atlases.
7. Expand deterministic and semantic acceptance.
8. Add impact/invalidation and incremental execution.
9. Add row-aware retrieval and query packets.
10. Activate named profiles and Codex/ChatGPT artifact handoffs.
11. Remove superseded contracts/templates only after read compatibility and migration reports pass.

# 5. Module 1 - Source Custody, Deterministic Corpus Intelligence, and Durable Maps

## A. Module purpose and value

This module supplies the evidence universe for every later semantic decision. It prevents the demonstrated failure in which stronger semantic instructions operate on a candidate set that has already lost sources.

It supports these future-AI jobs:

- prove which files were in scope and which were not;
- find every file that may matter to a configured concept;
- understand exactly why each file surfaced;
- see duplicates, possible version families, blocked formats, and linked-only candidates;
- choose a high-signal read order without confusing that order with completeness; and
- diagnose whether an omission came from scope, extraction, vocabulary, graph coverage, or semantic review.

The primary token saving comes from replacing repeated whole-corpus search and duplicate reads with stable postings, section spans, duplicate representatives, and compact projections.

## B. Current-state mismatch

### Verified current behavior

- The current Phase 0 inventory and Markdown parser are useful deterministic foundations.
- Topic ranking is line-level substring counting over a flat keyword list.
- The result is truncated to 30 files.
- Match fields are not separated.
- Strong phrases, aliases, supporting terms, and negative/ambiguous terms are not distinct.
- Exact duplicate hashes appear in a profile but do not route source review or capsule reuse.
- Lifecycle, authority, and version evidence are largely absent from topic maps.
- The current navigation report is not populated with source bundles or gaps.
- Current reference names and runtime artifact names have drifted.

### Intended behavior from existing research

The prepared package correctly sought exhaustive inventory, inspectable topic maps, section pointers, duplicates/version evidence, and a populated navigation report. Its earlier grouping and maturity-track labels are not retained; the value-bearing mechanisms are.

### Severity

**Critical.** Better page templates, acceptance, or retrieval cannot reconstruct candidates removed before semantic review.

### Facts requiring implementation-time verification

- Actual dependency availability in the operator's execution environment for PDF and Office adapters.
- Extraction quality for representative MDX, converted PDF, scanned PDF, DOCX tables, PPTX notes/shapes, and XLSX formulas/merged cells.
- The largest real-corpus topic-map size and the compact-projection token budget.
- Whether Git history is available for every configured source root or only repository-tracked roots.

## C. Focused research and evidence

### Questions resolved

1. Can bounded navigation coexist with exhaustive candidates? Yes: make the machine map exhaustive and the projection bounded.
2. Can deterministic evidence determine authority? No: it may provide hints and rule provenance only.
3. Should one scalar relevance score be authoritative? No: expose an ordered signal vector and preserve each pointer.
4. Should graph extraction be part of the architecture? Yes, as a configurable deterministic capability with explicit consequences when disabled.
5. Should all non-Markdown formats be silently skipped until tooling exists? No: every file remains inventoried with adapter and blocked status.
6. Should generic term frequency guide topic reads? Only as corpus orientation, never as topic authority.

### Sources read

- Prepared package files `00-06`.
- Current `apex-meta/scripts/apex_kb.py`, Phase 0 functions and report generation.
- Current scope, command, and operational contracts.
- Executed Markdown parser, tool, and graph research.
- LLM-Wiki original concept and both operational packages.
- Official documentation for YAML safe loading, Markdown parsing, PDF extraction, DOCX/PPTX/XLSX libraries, Python, and SQLite.

### LLM-Wiki mechanism and Apex decision

| Blueprint mechanism | Value | Apex decision | What it lacks for Apex |
|---|---|---|---|
| Raw/wiki/schema separation | Keeps evidence distinct from compiled knowledge | **Copy and strengthen** with explicit corpus scope and custody modes | No exhaustive source map |
| SHA-256 sentinel/hash before ingest | Avoids repeated unchanged-source work | **Adapt** into the unified inventory and hash-keyed capsule identity | Path-oriented ingest; no duplicate/version routing |
| Index-first query and read narrowing | Saves routine query tokens | **Adapt** as compact projection, but never as the canonical candidate set | Index is not lossless discovery |
| Deterministic link/frontmatter/orphan scripts | Cheap structural facts | **Combine** inside one cross-platform runtime | Limited formats and Apex-specific relationships |
| Typed hierarchical wiki/source summaries | Useful downstream navigation | **Adapt** after maps; do not use page hierarchy as corpus discovery | No concept-to-all-source atlas |

### External evidence and inference

- Agent/tool documentation supports deterministic scripts for repeatable work and focused files for progressive loading.
- PDF documentation confirms that text extraction and OCR are different capabilities. Therefore scanned/image-only pages require a distinct visual route and cannot be counted as text-reviewed.
- Office-format libraries can read the formats, but their presence and pointer fidelity must be tested in the target environment.
- YAML must use a safe loader where a real parser is available; malformed frontmatter remains an extraction fact rather than disappearing.

**Inference:** A single Python runtime with adapter interfaces is lower-risk than several unrelated CLI pipelines because it can preserve one source identity, pointer vocabulary, error model, and deterministic sort order.

## D. Final module strategy

### Boundary and submodules

1. **Scope and custody**
   - Canonical `corpus-scope.json` names roots, exclusions, generated-output boundaries, format policy, and lifecycle-hint rules.
   - Canonical `source-manifest.json` records externally supplied sources/pointers, custody mode, provenance, and operator decisions.
   - The exhaustive inventory records every discovered file, including exclusions and blockers.

2. **Adapter registry**
   - Each format declares: availability, supported extraction units, pointer type, version, limitations, and failure reason.
   - Text, Markdown, code, JSON, YAML, and CSV use full-text adapters.
   - PDF, DOCX, PPTX, and XLSX are configurable adapters.
   - Images and scanned sources use inventory-only or an explicit visual-semantic adapter.

3. **Structure extraction**
   - Markdown: title, frontmatter, headings, section spans, links, fences, code blocks, and parser warnings.
   - DOCX: paragraphs, headings/styles, tables, headers/footers if configured; pointer is paragraph/table ordinal.
   - PPTX: slide, shape, notes, table text; pointer is slide and shape/paragraph ordinal.
   - XLSX: sheet, populated cell/range, formula/value mode; pointer is sheet and cell/range.
   - PDF: page and extracted text span; image-only pages remain visible.

4. **Postings and matching**
   - Unicode normalization and case folding are deterministic and recorded.
   - Primary phrases and aliases create strong candidates.
   - Supporting terms require configured co-occurrence or structural context.
   - Negative/ambiguous terms can suppress weak-only matches but never remove strong filename/title/heading/phrase evidence.
   - Each posting records field, pointer, count, and compact snippet.

5. **Duplicate and version evidence**
   - Exact duplicates by content hash.
   - Normalized-text duplicates by normalized hash.
   - Possible version families by filename/path tokens, internal titles, Git facts, and text similarity evidence.
   - Only the LLM may decide semantic supersession.

6. **Relationship graph**
   - Configurable extraction of Markdown links, wikilinks, repository paths, YAML/path fields, package manifests, process arrows, `owns`, `hands_off_to`, and similar explicit edges.
   - Graph nodes and edges carry exact evidence and deterministic/semantic-needed labels.

7. **Exhaustive topic map**
   - One row per candidate; no top-N truncation.
   - Required row facts: source identity, path, hash, format, extraction state, duplicate representative, deterministic lifecycle hints, every match signal, exact pointers, graph reasons, and an inspectable sort vector.
   - It makes no semantic relevance or authority claim.

8. **Projection and report**
   - The compact Markdown projection shows counts, direct candidates, section-primary candidates, contextual/linked candidates, duplicates, blockers, and recommended read batches.
   - The navigation report aggregates all active topics, extraction gaps, duplicate savings, and proposed semantic save batches.

### Owners, inputs, outputs, consumers

| Submodule | Owner | Inputs | Outputs | Consumers |
|---|---|---|---|---|
| Scope/custody | Operator + runtime | Roots, exclusions, source pointers | Scope, manifest, inventory | All stages |
| Adapters/structure | Runtime | Inventory rows and bytes | Structure map, extraction warnings | Postings/maps/semantic packets |
| Postings/matching | Runtime | Structure/text and registry | Term postings, topic candidates | Topic-map renderer |
| Duplicate/version | Runtime, then LLM | Hashes/names/Git/text evidence | Duplicate/family evidence | Maps, capsules, topic semantics |
| Graph | Runtime | Explicit paths/links/contracts | Relationship edges | Topic maps, impact map |
| Map/projection/report | Runtime | All deterministic facts | Exhaustive JSON/NDJSON, compact Markdown, navigation report | Semantic compiler, operator, acceptance |

### Failure behavior

- Missing adapter: inventory row remains with `blocked_adapter_unavailable`.
- Parse error: record error type, adapter/version, partial coverage, and last stable pointer.
- Unsupported embedded object: preserve parent source and embedded-object blocker.
- Missing source root: scope check fails that root but reports other roots; the run cannot claim complete scope.
- Profile-disabled capability: record `profile_disabled` and its consequence; do not pretend the evidence was reviewed.
- Map generation interruption: deterministic outputs are written atomically per artifact; completed input hashes are recoverable from the run manifest.

## E. Implementation map

### Order

1. Define scope, inventory, adapter, posting, topic-map, and duplicate schemas.
2. Preserve current CLI commands and create compatibility fixtures from current artifacts.
3. Move inventory/hash/path safety into runtime modules.
4. Add adapter registry and stable pointers.
5. Add postings, vocabulary rules, and no-truncation topic maps.
6. Add duplicate/version evidence.
7. Add compact projection and populated report.
8. Add configurable graph extraction.
9. Migrate old artifact names through explicit compatibility projections.
10. Remove old ranking authority only after parity and losslessness tests pass.

### Deterministic-semantic interface

The semantic packet receives:

- exact repository commit and KB root;
- profile axes;
- registry and map hashes;
- exhaustive candidate count;
- compact read order;
- candidate rows with pointers;
- duplicate representatives;
- blocked sources;
- required outputs and allowed write paths.

It never receives a deterministic statement that a source is authoritative or irrelevant.

### Tests and fixtures

- More than 30 valid candidates, proving no loss.
- Exact phrase in filename but low body count.
- Ambiguous supporting term in a long generic file.
- Strong H1/heading match with no body repetition.
- Linked-only candidate.
- Exact duplicate and normalized duplicate.
- Several possible version-family files without auto-supersession.
- Malformed frontmatter and fenced-code fake headings.
- MDX components.
- PDF text page, image-only page, and extraction failure.
- DOCX paragraph/table, PPTX slide/notes/shape, XLSX cell/range.
- Excluded generated-output subtree.
- Real Leela Skill Tree canary and another unrelated-concept negative canary.

### Acceptance

- Scope closure equals 100% for the fixture.
- Candidate map contains every expected candidate and no candidate lacks a reason.
- Compact view discloses total count and never alters the machine set.
- Strong evidence cannot be removed by a negative weak term.
- All blocked and excluded rows remain visible.
- Repeated runs with identical inputs are byte-stable except fields explicitly isolated as run metadata.

## F. Creation guidance

- Derive file identities, hashes, spans, postings, graph facts, duplicate evidence, counts, and sort vectors.
- Author only scope policy, topic vocabulary, exclusions, and lifecycle-hint rules.
- Do not duplicate source path, hash, bytes, format, and extraction status in semantic files; reference the inventory source ID.
- Do not duplicate topic vocabulary in templates; reference the registry hash.
- Keep the compact projection small enough for a semantic batch, but include counts and links to every omitted category.
- Keep adapter-specific detail in adapter modules and the deterministic artifact contract, not in `SKILL.md`.
- Use one error taxonomy across all formats.
- Prefer pointer stability over visually perfect extraction.

## G. Interconnectedness

### Upstream producers

- Operator scope/profile choices.
- Source intake and raw/pointer custody.
- Repository filesystem and Git metadata.

### Downstream consumers

- Source capsule authoring.
- Topic semantic disposition.
- Dossier and atlas generation.
- Deterministic acceptance.
- Impact analysis.
- Retrieval source-role indexing.

### Invalidation

- Changed file bytes invalidate its inventory hash, extracted structure, postings, duplicate groups, candidate-map rows, graph edges, capsule, affected topic analyses, dossier/atlas pages, acceptance, and retrieval chunks.
- Changed topic vocabulary invalidates postings/query assembly and topic maps for that topic, then all topic-dependent semantic artifacts.
- Changed scope invalidates inventory closure and every downstream artifact affected by added/removed roots or exclusions.
- Changed adapter version invalidates only files processed by that adapter unless pointer semantics changed globally.

## H. File and script impact

Primary affected paths:

- `apex-meta/scripts/apex_kb.py`
- proposed `apex-meta/scripts/apex_kb_runtime/inventory.py`
- proposed `apex-meta/scripts/apex_kb_runtime/extract.py`
- proposed `apex-meta/scripts/apex_kb_runtime/topic_maps.py`
- proposed `apex-meta/scripts/apex_kb_runtime/render.py`
- proposed `apex-meta/scripts/apex_kb_runtime/validate.py`
- `.claude/skills/apex-kb/references/deterministic-artifact-contract.md`
- all scope, inventory, topic-map, and impact schemas listed in the final tree
- KB-instance `manifests/` artifact families listed in the final tree
- Phase 0 and adapter fixtures under `apex-meta/tests/apex_kb/fixtures/`

Detailed file design records appear in the Final File and Script Implementation Plan.

# 6. Module 2 - Semantic Source Analysis, Knowledge Compilation, and Durable Source Atlas

## A. Module purpose and value

This module turns the exhaustive deterministic candidate set into durable meaning. It must create more value than a new raw-corpus read by preserving:

- reusable understanding of unique source content;
- topic-specific judgment for every candidate;
- documentary evolution and conflicts;
- a direct Macro/Meso/Micro concept answer; and
- a complete source atlas that explains every source's individual role and value.

It prevents shallow compilation, unopened-source citation, duplicate rereads, path-based authority guesses, and the loss of historical/prototype/contextual evidence after a page is written.

## B. Current-state mismatch

### Verified current behavior

- Current semantic rules correctly distinguish candidate, read, and used sources.
- Current main requires target-query coverage, explicit candidate dispositions, page-only evaluation, and material-claim entailment.
- The Phase 1 template is path-oriented and broad; it is not a stable content-hash capsule.
- The current ledger is one all-purpose per-topic state file with many fields, but it does not supply the full source-atlas product.
- Current page templates carry repeated fields and sections across summary, concept, and entity page types.
- Current compilation emphasizes answer-bearing pages and used sources; it does not require a source-atlas row for every deterministic candidate.
- Duplicate and version-family evidence are not integrated with semantic source reuse.

### Severity

**Critical.** Without this module, the system remains a selective summary pipeline even after deterministic discovery is fixed.

### Facts requiring implementation-time verification

- Whether JSON or a constrained Markdown/YAML record yields lower semantic-authoring error rates for very large topic analyses.
- The practical topic-atlas row count at which deterministic partitioning improves future query cost.
- The token savings from hash-capsule reuse across multiple concepts in real corpora.
- Which existing KB pages can be migrated automatically and which require semantic repair.

## C. Focused research and evidence

### Questions resolved

1. What semantic work is reusable across topics? Source-global content understanding and source-level claims, keyed by content hash.
2. What remains topic-specific? Relevance, lifecycle role for the topic, individual value, contribution, source relationships, target-query coverage, and page plan.
3. Should the source atlas be hand-authored separately? No. The semantic rows are canonical; the atlas is a lossless rendered product, avoiding duplicate semantic facts.
4. Should one source update multiple pages? Yes. A source capsule may feed several topic analyses, dossiers, entities, and contradictions.
5. Should every mention create an entity or concept page? No. Page creation requires independent recurring query value.
6. Can targeted reading support durable truth? Yes for contextual candidates when exact ranges and rationale are recorded; current/core evidence defaults to a full read.

### Sources read

- Current semantic value contract, ledger schema, templates, browser runbook, and acceptance schema.
- Original LLM-Wiki concept.
- Operational LLM-Wiki ingest and query workflows.
- Typed LLM-Wiki skill and article guide.
- Prepared artifact templates and failure analysis.
- Current Deep Research and connected-source documentation.
- Agent Skills/Claude progressive-disclosure and context-boundary evidence.

### LLM-Wiki mechanism and Apex decision

| Blueprint mechanism | Value | Apex decision | Missing relative to Apex |
|---|---|---|---|
| Persistent compiled wiki instead of query-time re-derivation | Core compounding value | **Copy** | No exhaustive documentary atlas |
| One source updates multiple concepts/entities/summaries | Preserves cross-concept contribution | **Copy and route through capsules** | No content-hash semantic reuse contract |
| Two-phase source analysis then generation | Prevents immediate shallow writes | **Adapt** into a batch-level semantic packet, not one approval pause per file | Candidate set not exhaustive; operator gate can become expensive ceremony |
| Contradiction callouts and crosslinks | Preserves disagreement | **Copy and strengthen** with lifecycle/version relationships | No authority/freshness model |
| Typed concept/entity/summary pages | Supports navigation | **Configure** by query value | Type proliferation and repeated metadata |
| Source summaries | Reusable source understanding | **Change** to hash-keyed capsules | Path identity and per-topic duplication |
| Save useful query synthesis | Compounds knowledge | **Configure** behind accepted evidence | Can create unsupported doctrine without promotion gate |

### Disagreements resolved

- Older Apex material treated the source analysis as a file-path artifact. The final design keys reusable semantic understanding by content hash while retaining path aliases in the inventory.
- Older material sometimes treated a summary page as the source map. The final design separates dossier, canonical semantic rows, and rendered atlas.
- LLM-Wiki length heuristics are useful split signals but are not semantic acceptance gates.

## D. Final module strategy

### Submodule 1: hash-keyed source capsule

Repository-relative pattern:

`ingest-analysis/sources/<sha256-prefix>/<sha256>.analysis.md`

Canonical responsibilities:

- identify the content hash and adapter coverage;
- record full or targeted review coverage and exact pointers;
- provide a concise content snapshot;
- capture source-global claims, definitions, data structures, implementation facts, and uncertainty;
- record authority/freshness evidence without converting hints into a verdict;
- record relationships to duplicate/version candidates by source ID;
- list topics to which the source may contribute; and
- expose blockers and incomplete coverage.

Non-responsibilities:

- final topic relevance;
- final source authority for every topic;
- page routing decisions;
- acceptance verdicts; or
- duplicated path/hash/format facts already owned by inventory.

Capsules are extended when later work reads additional sections. A capsule may be marked complete only for the coverage it explicitly records.

### Submodule 2: canonical topic semantic record

Repository-relative pattern:

`ingest-analysis/topics/<topic-id>.analysis.json`

Required content families:

- registry and topic-map input hashes;
- target-query coverage;
- one semantic row for every topic-map candidate;
- per-row `review_mode` and exact coverage;
- `lifecycle_role`: current, historical, prototype, implementation, contextual, or unknown;
- `disposition`: core_evidence, supporting_evidence, duplicate, superseded, incidental, blocked, or irrelevant_after_review;
- authority/freshness judgment with rationale and evidence;
- source snapshot and individual value for this topic;
- contribution, contradictions, and source relationships;
- exact evidence pointers and capsule reference;
- page plan, claim plan, unresolved questions, and raw-source reopen triggers.

The two-axis lifecycle/disposition design prevents an overloaded enum. For example, a historical source can still be core evidence for evolution, and an implementation source can be superseded.

### Submodule 3: concept dossier

Repository-relative route comes from the topic registry, normally under `wiki/concepts/`.

Required semantic content:

- direct answer and scope;
- Macro context and purpose;
- Meso components, relationships, lifecycle, and alternatives;
- Micro implementation, data, files, interfaces, commands, or behaviors where evidence supports them;
- current state versus history/prototypes;
- material claims with source pointers;
- contradictions, uncertainty, and reopen triggers;
- routes to related concepts/entities; and
- a stable link to the source atlas.

It must not repeat every atlas row.

### Submodule 4: durable source atlas

Stable route:

`wiki/source-atlases/<topic-id>/index.md`

The atlas is rendered from the canonical topic semantic record. For small topics, `index.md` may contain every row. For large topics, it contains complete counts and category navigation plus generated partition pages under the same directory. Partitioning never changes the semantic-row set.

Every candidate is visible with:

- source ID and repository-relative path;
- review mode and coverage;
- lifecycle role and disposition;
- content snapshot;
- individual value;
- authority/freshness assessment;
- duplicate/supersession/contradiction relationships;
- exact evidence pointers;
- blocker or irrelevance rationale; and
- capsule/dossier links.

### Submodule 5: optional entities and additional pages

Create an entity or separate subpage only when at least one of these is true:

- it answers independent recurring target queries;
- it has a stable identity and relationships across multiple concepts;
- splitting materially lowers routine query context; or
- the page is a canonical implementation/reference surface.

Mention frequency or word count alone is insufficient.

### Submodule 6: external verification

External research is configurable and triggered by:

- unstable current claims;
- conflicting internal evidence;
- a named evidence gap;
- a source-authority dispute; or
- an operator-selected research axis.

A durable external finding must enter source custody as a captured source record or explicit durable pointer. Transient web knowledge cannot silently become accepted doctrine.

### Submodule 7: semantic task packet and output bundle

One save batch is normally one concept plus:

- any new/expanded source capsules needed by that concept;
- the topic semantic record;
- the dossier;
- the source atlas render inputs; and
- declared blockers.

A tightly related source group may be a batch when several topics share the same small evidence context. Arbitrary partial drafts are not save batches.

### Failure and recovery

- Source unavailable: candidate remains blocked; topic can be partial but not silently complete.
- Context exhausted before a coherent batch: no partial dossier is promoted; completed capsules and semantic rows may be saved with batch status `semantic_partial`.
- Contradiction unresolved: preserve both claims and the uncertainty; do not force a winner.
- Schema-invalid semantic output: deterministic import rejects it without losing the authored bundle; the repair packet names exact failures.
- Connector/browser cannot write the repository: the semantic model returns an output bundle; Codex imports it after changed-path and schema checks.

## E. Implementation map

### Order

1. Define source-capsule and topic-analysis schemas and a migration mapping from the current ledger/template.
2. Build capsule path/hash lookup and coverage extension rules.
3. Implement topic-map-to-topic-analysis import validation.
4. Create the dossier template and atlas renderer.
5. Migrate one real concept as a canary.
6. Validate that every topic candidate becomes one semantic row.
7. Add entity/page topology rules and external-verification capture.
8. Batch-migrate existing accepted concepts with explicit compatibility reports.

### Migration from current behavior

- Existing Phase 1 analyses become candidate capsule inputs. Their path identity is resolved to current inventory hashes.
- Existing topic ledgers become topic-analysis migration inputs; missing atlas fields remain explicit repair gaps.
- Existing concept/summary/entity pages are not rewritten wholesale. They are classified as retained, dossier candidate, atlas candidate, entity, superseded, or repair-needed.
- Existing source-use sections remain evidence but do not substitute for the exhaustive atlas.
- The old approval phrase remains accepted only as a compatibility input; final flow uses run/profile and batch status rather than a universal per-file pause.

### Interfaces

- Capsule import requires a source ID, matching content hash, coverage, and pointers.
- Topic analysis import requires the exact topic-map hash and one row per candidate source ID.
- Dossier validation requires configured critical query coverage and an atlas route.
- Atlas generation requires an accepted schema-valid topic analysis, not free-form page scraping.

### Tests and fixtures

- One source contributes to several topics without duplicate full reads.
- Same hash at several paths produces one capsule and several inventory aliases.
- Targeted capsule coverage extends to full without losing prior pointers.
- Historical source remains core for evolution while not current authority.
- Duplicate source is represented but not reread.
- Superseded implementation remains visible with successor relation.
- Incidental and irrelevant-after-review candidates remain in atlas.
- Blocked image/PDF candidate remains visible.
- Dossier contains no claims unsupported by capsule pointers.
- Atlas partitioning preserves row count and stable routes.

### Measurable acceptance

- Capsule reuse rate and avoided source-read tokens are reported.
- Topic analysis candidate IDs equal topic-map candidate IDs exactly.
- Atlas row count and category counts equal topic analysis.
- Every critical query routes to at least one dossier section and accepted claim set.
- No used source lacks a read record and pointer.

## F. Creation guidance

### Derive rather than author

Derive:

- source identity/path/hash/format;
- candidate list and match reasons;
- duplicate aliases;
- atlas tables and partitions;
- category counts;
- dossier-to-atlas links;
- input/output hashes; and
- run provenance.

Author semantically:

- source snapshot;
- claims and meaning;
- authority/freshness rationale;
- lifecycle/disposition;
- individual value;
- contradiction/supersession interpretation;
- dossier synthesis; and
- uncertainty.

### Do not duplicate

- Do not repeat registry questions in every capsule.
- Do not repeat inventory facts in capsules.
- Do not author the same candidate assessment in both topic analysis and atlas.
- Do not repeat all source rows in the dossier.
- Do not place acceptance verdicts inside dossiers.
- Do not create a second semantic ledger beside topic analysis.

### Context strategy

- Load one compact topic projection, its relevant candidate rows, and only the source capsules/full sources needed for the save batch.
- Keep shared concept context in the main semantic context.
- Use isolated subcontexts only for self-contained noisy source reads; return structured capsule content rather than verbose transcripts.
- Preserve one coherent batch through dossier and atlas creation so cross-source meaning is not fragmented.

## G. Interconnectedness

### Upstream

- Exhaustive topic maps and compact projections.
- Source inventory, structure pointers, duplicate/version evidence.
- Operator target queries and profile.

### Downstream

- Semantic acceptance.
- Source-atlas and dossier retrieval.
- Impact analysis and incremental update.
- Audit and knowledge promotion.
- Query synthesis.

### Invalidation

- A changed source hash invalidates its capsule and every candidate row/claim that references it.
- A changed topic map invalidates the topic analysis and atlas; the dossier is invalidated only if added/removed candidates or claim coverage affect it.
- A changed target query invalidates query coverage and acceptance; it may not require rereading unchanged sources if existing capsules cover the answer.
- A changed authority policy invalidates affected semantic judgments, not deterministic source bytes.

## H. File and script impact

Primary affected paths:

- `.claude/skills/apex-kb/references/semantic-value-contract.md` (merge/remove after migration)
- `.claude/skills/apex-kb/references/semantic-run-ledger.schema.json` (replace)
- `.claude/skills/apex-kb/templates/ingest-analysis-template.md` (replace)
- `.claude/skills/apex-kb/templates/wiki-page-templates.md` (replace)
- proposed semantic workflow, capsule, topic-analysis, dossier, atlas, and task-packet files in the final tree
- proposed `apex-meta/scripts/apex_kb_runtime/render.py`
- proposed semantic validation in `apex-meta/scripts/apex_kb_runtime/validate.py`
- KB-instance `ingest-analysis/sources/`, `ingest-analysis/topics/`, `wiki/concepts/`, and `wiki/source-atlases/`

Detailed design records appear later.

# 7. Module 3 - Configurable Profiles and Codex/ChatGPT/Deterministic Orchestration

## A. Module purpose and value

This module lets the complete architecture execute at different scopes without turning configuration into product incompleteness. It also creates the future low-token loop in which:

- the operator answers scope/profile questions once;
- Codex runs deterministic work and owns Git;
- ChatGPT web performs deep semantic reading and authors bounded knowledge bundles; and
- an independent context performs only demonstrated-value acceptance.

It prevents the orchestrator from deep-reading the corpus, the semantic model from pretending to run local tools, and repeated context reconstruction between batches.

## B. Current-state mismatch

### Verified current behavior

- The current Apex SKILL distinguishes terminal, connector, and browser semantic routes.
- It correctly limits connector-only semantic work and caps completion before deterministic postflight.
- The current browser runbook uses one topic per context and clean-context acceptance.
- Current configuration/output tiers exist but are mixed with legacy lifecycle states and terminology.
- No complete independent-axis profile model exists.
- No canonical Codex-to-ChatGPT semantic task packet, output manifest, or import contract exists.
- Current semantic ledgers carry more run state than needed and are not optimized for cross-tool artifact exchange.
- Current GitHub connected-app behavior is read-only for Deep Research; direct semantic repo mutation is therefore not a safe assumption.

### Severity

**High.** The architecture can be implemented without this loop, but the target low-token operating model and truthful tool boundaries cannot.

### Facts requiring technical probes

1. Whether the operator's chosen Codex surface can programmatically launch or exchange files with a ChatGPT web semantic run.
2. Whether a write-capable MCP/app can safely import semantic bundles without manual transfer.
3. Which artifact formats preserve citations and structured fields most reliably across browser download/import.
4. Connector indexing delay and changed-file visibility in the actual workspace.

Until those probes pass, the final architecture uses an explicit artifact handoff; it does not claim automatic Codex-to-browser invocation.

## C. Focused research and evidence

### Questions resolved

- Should profiles define different products? No. They select operation, topics, formats, depth, and surfaces within one architecture.
- Who owns the loop? A deterministic/Codex orchestrator, because script-owned workflows preserve state outside a model context.
- Should subagents own the lifecycle? No. They are useful for self-contained noisy work; the main/shared semantic context owns cross-source synthesis.
- Can Deep Research connected apps write GitHub? Not under the current read-only GitHub app behavior.
- Can Codex own Git changes? Yes; current Codex cloud documentation supports repository environments, diffs, review, and pull requests.
- Should every semantic batch receive independent evaluation? Only where the demonstrated error risk or acceptance policy justifies it.

### Sources read

- Current Apex SKILL and browser semantic runbook.
- Current lifecycle/run-manifest-like schemas and package examples.
- Compiled Claude workflow, skill, subagent, hook, and orchestration pages.
- Current official Claude Code skills, subagents, hooks, and workflows documentation.
- Current Agent Skills specification.
- Current OpenAI Deep Research, GitHub app, Codex cloud, and Codex skills documentation.
- LLM-Wiki entrypoint, ingest workflow, hash/sentinel, and progress mechanisms.

### LLM-Wiki mechanism and Apex decision

| Mechanism | Value | Apex decision | Gap |
|---|---|---|---|
| Short SKILL entrypoint routing to workflows | Keeps ordinary context small | **Copy** | Does not define multi-surface execution |
| Hash/sentinel before ingest | Idempotency | **Adapt** into run input hashes and batch state | File-oriented, not concept-save-batch oriented |
| Two-phase analysis/generation | Separates understanding from publication | **Adapt** inside one bounded semantic batch | Per-file pauses do not scale |
| Progress/restart marker for large sources | Preserves completed work | **Adapt minimally** as batch state | Marker must not become semantic evidence |
| Index-first proactive use | Token efficiency | **Adapt** for accepted KB queries, not orchestration authority | No Codex/Git/browser boundary |

### Claude/skill/orchestration evidence

- Script-defined workflows are the repeatable and resumable owner for large orchestrations; agents and skills decide turn by turn in model context.
- Subagents are appropriate when work is self-contained, verbose, or needs tool restrictions. Shared multi-phase context belongs in the main conversation.
- Hooks are deterministic enforcement points and can be skill-scoped, but should be used only for concrete write/safety conditions.
- Progressive disclosure favors a small skill router and on-demand references.

### Inference

The strongest future design is a file-backed choreography rather than a hidden cross-product agent chain. Every handoff is inspectable, replayable, hash-addressed, and importable even when one product surface changes.

## D. Final module strategy

### Independent configuration axes

The complete axis model appears in the profile section. Each run manifest records every axis explicitly; profile names are only presets.

### Ownership split

| Owner | Responsibilities | Must not do |
|---|---|---|
| Codex/orchestrator | Ask only necessary scope/profile questions, resolve current commit, run deterministic commands, create task packets, import output bundles, validate changed paths, run tests/postflight, commit/push/open review | Deep-read raw sources or author semantic knowledge from shallow snippets |
| ChatGPT web semantic context | Read the packet and listed sources, assess meaning/authority/freshness/contradictions, author capsules/topic analysis/dossier, return the requested bundle, record actual model/mode | Claim terminal execution, mutate Git, run commits, or validate deterministic completeness from prose alone |
| Deterministic runtime | Inventory, extract, map, validate, render atlas, calculate impact, rebuild retrieval, produce observable state | Judge semantic truth or choose authoritative sources |
| Independent semantic context | Page-only queries, material-claim entailment, atlas-row faithfulness on the configured scope | Repeat source mapping, run Git, or rewrite the accepted pages during evaluation |
| Operator | Select profile and unresolved product decisions once, review high-risk blockers/promotions | Approve each ordinary source row or act as a manual scheduler |

### Run manifest

Pattern:

`manifests/runs/<run-id>/run-manifest.json`

Required field families:

- repository identity and starting commit;
- KB root and profile;
- all configuration axes;
- scope/registry/map hashes;
- requested topics and save batches;
- execution surfaces;
- allowed write paths and forbidden actions;
- actual semantic model/mode and evaluator model/mode;
- batch statuses and output hashes;
- deterministic checks, blockers, changed paths, and final state.

It is orchestration state, not semantic evidence.

### Semantic task packet

Pattern:

`manifests/runs/<run-id>/batches/<batch-id>/semantic-task-packet.md`

Required sections:

1. repository identity and commit;
2. profile/axes and batch purpose;
3. target queries and acceptance obligations;
4. exact candidate map and compact projection routes;
5. source bundle with full/targeted read requirements;
6. existing capsule routes and hashes;
7. allowed output paths;
8. required schema/contract routes;
9. explicit non-responsibilities;
10. blockers and unavailable evidence;
11. required output manifest.

The packet does not paste large source bodies when the semantic surface can open them directly.

### Semantic output manifest

Pattern:

`manifests/runs/<run-id>/batches/<batch-id>/semantic-output-manifest.json`

It lists authored files, input hashes, actual model/mode, review coverage, unresolved blockers, and whether the batch is coherent/complete. It does not duplicate the semantic contents.

### Save batch

A save batch is complete when its required capsules, topic analysis, dossier, and atlas render inputs form one coherent accepted-or-clearly-partial unit. It is not:

- a half-written dossier;
- an arbitrary token-sized slice;
- a single candidate row without its topic context; or
- a prose chat answer not captured as an artifact bundle.

### Operating loop

```text
Operator supplies scope/profile once
  -> Codex resolves commit and runs deterministic scope/inventory/maps
  -> Codex creates one semantic task packet and source bundle
  -> ChatGPT web reads sources and returns the semantic artifact bundle
  -> Codex imports only allowed paths and validates hashes/schemas/pointers
  -> independent semantic context runs configured acceptance only
  -> Codex runs atlas render, retrieval rebuild, postflight, and tests
  -> Codex commits/pushes/opens review
  -> next coherent save batch
```

### Tool-surface behavior

- **Terminal/Codex:** full deterministic and Git capability.
- **GitHub connector/Deep Research:** semantic read access and citation; no assumed repository write.
- **Browser:** strong semantic reading/research and downloadable artifact creation; no local lifecycle command execution.
- **Write-capable MCP/app:** `requires_evidence_probe` before it replaces the artifact-import boundary.

### Recovery behavior

- Deterministic commands are idempotent and atomically write outputs.
- Completed save batches remain accepted and are not recomputed after a later-batch failure.
- A minimal batch state may store completed candidate IDs and next work item when a single batch genuinely exceeds one semantic context.
- No restart protocol is added for short, coherent batches.
- A failed import preserves the returned bundle outside canonical paths and emits an exact repair report.

## E. Implementation map

### Order

1. Define profile axes, run manifest, task packet, and output manifest schemas.
2. Add deterministic packet generation from maps and existing capsules.
3. Add changed-path allowlist and output import validation.
4. Test a manual browser artifact round trip.
5. Add independent acceptance packet generation.
6. Add Codex command examples and Git verification.
7. Probe direct automation/MCP transfer; keep it disabled until proven.

### Compatibility

- Existing terminal and connector routes remain valid execution surfaces.
- Existing semantic ledger data migrates into topic analysis plus run manifest.
- Existing approval/stop phrases are parsed as compatibility inputs but no longer define the architecture.
- Existing postflight commands remain the deterministic end of the loop.

### Tests

- Packet references exact commit and hashes.
- Semantic bundle attempts an out-of-scope write and import rejects it.
- Bundle references a stale topic map and import rejects it.
- Bundle contains valid partial artifacts and preserves truthful partial state.
- Connector route cannot claim query-ready without local postflight.
- Completed batch remains stable after next-batch failure.
- Actual model/mode is required but no specific marketing name is required.

### Acceptance

- Codex never needs to read full raw sources to perform import and verification.
- Semantic model never needs local shell/Git access.
- All changed files are declared in the output manifest.
- The run is reproducible from commit, profile, input hashes, packets, and artifact bundle.

## F. Creation guidance

- Author profiles as data presets, not separate workflow documents.
- Generate packets from canonical scope/registry/maps/contracts.
- Keep packet references one level deep where possible.
- Include source bodies only when the target semantic surface cannot open them.
- Do not create a generic evaluator ledger, conversation transcript, or restart file for every batch.
- Do not use hooks to enforce semantic truth.
- Use hooks only for demonstrated deterministic needs such as out-of-root writes, destructive operations, or required post-write validation.
- Record tool limitations as facts in the run manifest.

## G. Interconnectedness

### Upstream

- Scope, registry, maps, capsules, and profile selection.

### Downstream

- Semantic compilation, acceptance, postflight, retrieval, Git publication, and maintenance.

### Invalidation

- Changed commit or input hash invalidates an unimported task packet.
- Changed profile invalidates packet obligations but not existing accepted artifacts unless the new profile changes required scope.
- Changed semantic output after acceptance invalidates that acceptance and retrieval.
- Changed tool-surface capability updates the execution-surface contract, not the semantic products.

## H. File and script impact

Primary affected paths:

- `.claude/skills/apex-kb/SKILL.md`
- `.claude/skills/apex-kb/references/browser-git-connector-semantic-runbook.md` (merge/remove)
- proposed `.claude/skills/apex-kb/references/execution-surface-contract.md`
- proposed run-manifest and task-packet schemas/templates
- proposed `apex-meta/scripts/apex_kb_runtime/profiles.py`
- proposed packet/import commands in the stable CLI
- KB-instance `manifests/runs/` artifact family

# 8. Module 4 - Apex Skill Package, Contracts, Templates, Runtime, and Tests

## A. Module purpose and value

This module turns the architecture into an implementation surface that later agents can build without rediscovering ownership, schemas, commands, or file relationships. It reduces recurring context by making `SKILL.md` a compact router, giving each fact one canonical owner, and moving deterministic behavior into tested runtime modules.

It prevents:

- duplicated lifecycle truth across entrypoint, references, examples, and deprecated files;
- template-driven field inflation;
- command/runtime drift;
- monolithic-script maintenance risk;
- manual-only acceptance regressions; and
- generic guardrail files accumulating inside the KB package.

## B. Current-state mismatch

### Verified current behavior

- The package follows a recognizable skill layout and has valuable source, semantic, retrieval, and boundary contracts.
- `SKILL.md` is capable but long and repeats material found in references.
- Several references overlap in lifecycle, command, semantic, and query responsibilities.
- `lifecycle-state-machine.md` is explicitly deprecated but remains in the active package inventory.
- Runtime artifact names and reference names have drifted.
- Page and analysis templates repeat metadata and sections.
- Two spec-only generic lint files have no executable consumer in the current package.
- `apex_kb.py` combines many lifecycle concerns in one large script.
- Current command acceptance material is valuable but is primarily a runbook, not a conventional automated test suite.

### Severity

**High.** Package duplication does not cause the primary source-loss defect, but it increases drift, context cost, and implementation ambiguity across every module.

### Facts requiring implementation-time verification

- All current callers of the two CLI scripts and every referenced artifact name.
- Which legacy KB instances use old schemas or depend on old template sections.
- Whether `.claude/skills/` remains the only Claude skill root or a mirrored Agent Skills path is needed for Codex.
- Current test runner and repository conventions for Python tests.

## C. Focused research and evidence

### Questions resolved

1. Should `SKILL.md` contain the full lifecycle contract? No. It should identify triggers, routes, ownership, high-level flow, and reference selection.
2. Should scripts live inside the skill folder? Existing Apex repo-level scripts are a valid architecture. The skill manifest must name them explicitly; do not duplicate them inside the package.
3. How many references? Enough to keep one canonical owner per decision boundary; not one file per small rule and not one giant contract.
4. Should deterministic scripts or LLM instructions own repeatable checks? Scripts.
5. Should a deprecated reference remain in the active package? No, after compatibility documentation and migration.
6. Should generic repo-routing lints remain in Apex KB? No; they are a different owner and have no demonstrated role in KB compilation.

### Sources read

- Current package manifest, SKILL, active references, schemas, templates, examples, and deprecated lifecycle file.
- Current runtime scripts and command contracts.
- Compiled Claude information-design and orchestration sources.
- Current Claude skills documentation and Agent Skills specification.
- Codex skill documentation.
- LLM-Wiki entrypoint/workflow/package structures.

### LLM-Wiki mechanism and Apex decision

| Mechanism | Value | Apex decision | Gap |
|---|---|---|---|
| Short entrypoint delegates to workflows | Progressive disclosure | **Copy** | Current Apex entrypoint still carries too much contract detail |
| `scripts/`, `references/`, templates | Clear package roles | **Adapt** to repo-level runtime and focused references | Blueprint files sometimes duplicate conventions |
| Bash/Python deterministic helpers | Observable checks | **Copy concept, retain Python** | Cross-platform and Apex-specific schemas needed |
| Typed schema guide | Page consistency | **Adapt and reduce** | Too much repeated page metadata and fixed type ceremony |
| Audit guide and scaffold | Durable feedback/bootstrap | **Keep concepts** | Must align with final atlas and run manifest |

### Skill/orchestration design evidence

- Agent Skills recommends progressive disclosure, focused reference files, relative references, scripts for deterministic work, and a main `SKILL.md` below 500 lines.
- Current Codex and Claude skill implementations similarly load metadata first and the full skill only on activation.
- Compiled Apex design evidence recommends one canonical definition for each schema/key and script-owned observable workflow state.

## D. Final module strategy

### Package boundary

`SKILL.md` becomes a concise operational router with:

1. trigger/description;
2. product target and non-negotiable source-map/atlas outputs;
3. owner boundaries;
4. profile and execution-surface selection;
5. high-level lifecycle;
6. reference loading table;
7. failure/stop rules; and
8. completion states.

It does not repeat schemas, template fields, every command flag, or long browser procedures.

### Canonical reference set

1. `lifecycle-contract.md` - product stages, ownership, states, canonical/derived classes, source custody.
2. `deterministic-artifact-contract.md` - commands, scope/inventory/maps, error taxonomy, write policy, stable artifacts.
3. `semantic-compilation-workflow.md` - capsule/topic/dossier/atlas flow and semantic rules.
4. `semantic-acceptance-contract.md` - deterministic/semantic acceptance and truthful states.
5. `query-maintenance-workflow.md` - query, retrieval, promotion, audit, impact, incremental refresh.
6. `execution-surface-contract.md` - terminal/Codex/connector/browser roles and packet handoffs.
7. `knowledge-promotion-rules.md` - retained, simplified, and linked only where doctrine promotion is relevant.

Every machine schema remains a focused JSON Schema file under `references/` and is referenced by one canonical contract.

### Templates

Templates become small creation aids, not alternate contracts. Each points to its schema/contract and contains only:

- required section order;
- one minimal example;
- semantic prompts that cannot be derived; and
- explicit non-responsibilities.

### Runtime modularization

Keep public entrypoints:

- `apex-meta/scripts/apex_kb.py`
- `apex-meta/scripts/apex_kb_retrieval.py`

Move implementation behind them into `apex-meta/scripts/apex_kb_runtime/` with bounded modules for common I/O/path safety, inventory, extraction, topic maps, rendering, validation, maintenance, retrieval, profiles, and CLI composition.

The wrappers preserve current commands and translate old artifact names during migration.

### Tests

Create a conventional automated suite under `apex-meta/tests/apex_kb/`. Manual examples remain operator documentation, not the primary regression surface.

### Generic lint disposition

- `repo-execution-router-lint-spec.md`: **remove from Apex KB package**; move only if a general repository-validation owner is created.
- `historical-path-authority-lint-spec.md`: **remove from Apex KB package**; keep historical-path evidence as a semantic lifecycle concern and generic current-path lint under repository validation if implemented.

This is not removal of useful safety. It removes unexecuted, misowned specifications that do not prevent the demonstrated KB failure.

## E. Implementation map

### Order

1. Inventory every current package file and current consumer.
2. Freeze current CLI/artifact behavior in fixtures.
3. Add new canonical references and schemas without removing old ones.
4. Implement runtime modules behind wrappers.
5. Migrate templates and examples.
6. Add schema/CLI/integration tests.
7. Generate compatibility reports for real KBs.
8. Mark old references read-only compatibility aliases.
9. Remove old files only after no current caller or KB depends on them.

### Compatibility rules

- Old topic registry and semantic acceptance compatibility identifiers are readable.
- Old runtime artifact names may be generated as compatibility projections during migration, never as canonical data.
- Old status names map explicitly to final states; ambiguous states require repair.
- No automatic semantic reinterpretation of old pages/ledgers.
- Current public CLI flags remain accepted until a documented removal decision; new functionality is added through clear subcommands/options.

### Tests

- Skill frontmatter and reference paths validate.
- No active reference chain is deeper than necessary.
- Every schema has one canonical owner and at least one valid/invalid fixture.
- CLI wrappers produce identical compatibility outputs for frozen fixtures.
- Artifact-name drift is detected.
- Deprecated files are not loaded by the final SKILL route.
- Runtime modules cannot write outside the KB root except explicitly declared repo-level test/output paths.
- Dry-run and write-mode behavior remain stable.

## F. Creation guidance

- Keep `SKILL.md` well below the recommended progressive-disclosure limit; target roughly 150-220 lines after consolidation.
- Keep reference files focused and avoid reference-to-reference chains except direct schema links.
- Generate command examples from parser/help metadata where practical so examples cannot drift.
- Put full field definitions in schemas/contracts, not templates and examples.
- Use stable reason codes for deterministic failures and concise prose for operator-facing explanations.
- Do not add a hook merely to remind the model of a rule already enforced by path validation or schema validation.
- Do not duplicate Python runtime under the skill package.

## G. Interconnectedness

### Upstream

- All architecture decisions in Modules 1-3 and 5-7.

### Downstream

- Every implementation agent, operator command, semantic model, test, and migration.

### Invalidation

- Contract changes invalidate dependent templates, examples, schemas, and tests.
- Schema compatibility changes require migration reports.
- CLI changes invalidate generated examples and command fixtures.
- Skill-router changes do not invalidate semantic knowledge unless they change product requirements.

## H. File and script impact

All current and proposed package/runtime/test paths are enumerated in the Final File and Script Implementation Plan, including explicit merge/remove mappings and design records.

# 9. Module 5 - Incremental Maintenance and Impact Analysis

## A. Module purpose and value

This module preserves the product after the first build without rereading unchanged evidence. It answers:

- what changed;
- which deterministic and semantic artifacts are affected;
- which accepted claims or source-atlas rows are stale;
- what can be reused safely; and
- what bounded work restores query readiness.

It prevents full rebuilds for small changes, stale accepted pages, duplicate semantic reads, and maintenance runs that sweep the whole wiki without evidence of impact.

## B. Current-state mismatch

### Verified current behavior

- Current source custody and retrieval use hashes and stale checks.
- Current postflight rebuilds index/retrieval and runs lint, quality, semantic acceptance, audit, status, and stale checks.
- Current duplicate hashes do not drive semantic reuse.
- No complete dependency graph links source IDs to topic-map rows, capsules, topic analyses, dossier claims, atlas rows, acceptance results, and retrieval chunks.
- Current semantic maintenance can therefore become whole-page or whole-topic rereading.
- Current logs, ledgers, status files, and Git history overlap in run-state purpose.

### Severity

**High.** The product can be built without impact analysis, but it cannot meet the incremental-maintenance and low-token target reliably.

### Facts requiring implementation-time verification

- Real change-frequency distribution and average impacted topic count.
- Whether a single repository-wide dependency map or per-KB maps are more efficient at current scale.
- Which existing KB artifacts have enough source pointers to seed impact edges automatically.
- Retention policy for historical run manifests and acceptance records.

## C. Focused research and evidence

### Questions resolved

1. What is the invalidation root? Content hash, scope/registry hash, adapter revision, semantic-record hash, and accepted-page hash.
2. Can timestamps be the primary stale signal? No. Hashes own content freshness; timestamps are supporting evidence.
3. Should every maintenance run re-lint semantically? No. Semantic lint follows the impact set unless a separately configured audit requests a wider sweep.
4. Should logs preserve semantic content? No. Semantic content belongs in capsules/topic analyses/pages; run manifests preserve operation state.
5. Can duplicate paths reuse one capsule? Yes, while retaining every path in inventory/atlas.

### Sources read

- Current hash, status, postflight, retrieval stale, audit, and quality code/contracts.
- Current source and semantic manifests.
- LLM-Wiki hash-files, check-stale, two-phase ingest, lint, review/audit, and save-synthesis mechanisms.
- Compiled script-owned workflow and resilience evidence.
- Prepared maintenance and impact templates.

### LLM-Wiki mechanism and Apex decision

| Mechanism | Value | Apex decision | Gap |
|---|---|---|---|
| Source hash/sentinel | Idempotent ingest | **Copy and generalize** into source/capsule/topic dependency hashes | Does not invalidate concept maps/atlases |
| Stale-index check | Prevents query on stale index | **Keep** | Only derived index freshness |
| Quick deterministic lint | Cheap health | **Keep and expand** | No source-map/atlas checks |
| Full semantic lint | Contradiction/quality sweep | **Change** to impact-bounded default | Whole-wiki token cost |
| Review/audit queue | Durable feedback | **Keep, simplify** | Can become a second issue system |
| Saved synthesis | Compounding knowledge | **Configure** and connect to promotion/impact | No dependency update contract |

## D. Final module strategy

### Change detection

Inputs:

- current and prior scope hash;
- inventory/source hashes and adapter revisions;
- topic registry hashes;
- source capsule hashes and coverage;
- topic-map/topic-analysis hashes;
- dossier/atlas/acceptance hashes; and
- retrieval input hash set.

Change classes:

- source added, changed, removed, moved, or newly readable;
- scope/exclusion changed;
- topic vocabulary/query changed;
- adapter behavior changed;
- semantic capsule/analysis changed;
- dossier/atlas changed;
- acceptance policy changed;
- profile requirement changed.

### Dependency map

Pattern:

`manifests/impact/dependency-map.json`

Edges include:

- source -> extracted structure/postings/duplicate groups/graph edges;
- source -> topic-map rows;
- source hash -> capsule;
- topic-map row/capsule -> topic semantic row;
- topic semantic rows -> dossier claims/sections and atlas rows;
- dossier/atlas -> acceptance cases;
- accepted page/atlas rows -> retrieval chunks;
- accepted query synthesis -> promoted knowledge page, when configured.

Every edge records reason and source/target hash. The map is deterministic where relationships are explicit; semantic claim dependencies are emitted by the semantic authoring output and validated structurally.

### Impact calculation

Pattern:

`manifests/impact/changed-source-impact.json`

It reports:

- changed facts;
- directly invalidated artifacts;
- transitively affected artifacts;
- reusable artifacts;
- required semantic batches;
- required acceptance scope;
- retrieval rebuild scope;
- blockers; and
- reasons for every edge.

### Incremental update rules

- Unchanged source hash and sufficient capsule coverage: reuse capsule.
- New path with existing hash: update inventory aliases/atlas row; do not reread content.
- Source changed but no affected topic-map membership: update deterministic artifacts only.
- Source changed and affected topic: update capsule, candidate row, topic analysis, affected dossier claims/sections, atlas row, acceptance, and retrieval chunks.
- Topic query changed but sources unchanged: reuse capsules; update topic analysis coverage, dossier/atlas if needed, acceptance, and retrieval.
- Adapter revision with changed pointer semantics: re-extract affected format and invalidate dependent pointers.

### Audit and lint

- Structural lint always remains cheap and deterministic.
- Semantic lint defaults to impacted pages/claims/atlas rows.
- A complete semantic audit is a selectable profile, not a routine gate.
- Audit files hold human feedback and resolution, not run progress.
- Promotion of audit outcomes into runtime doctrine follows the retained promotion rules.

### Recovery

- Run manifest records completed batches and reusable hashes.
- Atomic writes prevent half-valid deterministic artifacts.
- Failed semantic batch leaves prior accepted products intact and marks affected artifacts stale/partial.
- Retrieval continues to expose the last accepted version only if the query packet visibly reports the stale/impact state; strict profiles may block queries.

## E. Implementation map

### Order

1. Define dependency and impact schemas.
2. Emit source->map/capsule/topic edges during build/import.
3. Emit semantic row->dossier/atlas claim edges during semantic import.
4. Add impact command and dry-run report.
5. Add incremental packet generation.
6. Scope acceptance and retrieval rebuild to impacts.
7. Replace mandatory prose run logging with run manifests and optional generated summaries.

### Compatibility

- Current hash/stale data is reused.
- Existing logs remain historical; they are not required for final operation.
- Existing pages without claim dependencies receive conservative page-level invalidation until repaired.
- Existing retrieval rebuild remains a safe fallback when chunk-level rebuild is not yet proven.

### Tests

- Unchanged source produces zero semantic rereads.
- Same hash at a new path changes atlas/inventory but not capsule.
- One changed source affects one of several topics.
- Registry query change reuses capsules.
- Removed source leaves a historical removal record and invalidates claims.
- Adapter revision invalidates only that format.
- Failed update preserves last accepted pages and marks staleness.
- Impact report has a reason for every invalidated artifact.

### Acceptance

- No affected artifact is omitted from the transitive impact set in fixtures.
- No unrelated capsule/topic is scheduled for semantic reread.
- Accepted/query-ready state is removed when an affected accepted artifact becomes stale.
- Rebuild restores exact dependency and retrieval hashes.

## F. Creation guidance

- Derive change and dependency facts; do not ask an LLM to compare file hashes or traverse explicit edges.
- Require semantic outputs to name the source IDs supporting material claims, enabling deterministic impact edges.
- Do not preserve full chat transcripts as recovery state.
- Keep historical run manifests only as long as audit/reproducibility policy needs; Git history remains the content history.
- Use conservative invalidation when a dependency is unknown, and report why.
- Do not run full semantic lint merely because it sounds safer.

## G. Interconnectedness

### Upstream

All deterministic and semantic artifacts.

### Downstream

Profiles, semantic task packets, acceptance, retrieval, audit, and Git publication.

### Cross-module effect

This module is the mechanism that turns the complete architecture into an economical ongoing product. Without it, source capsules and atlases save query tokens but maintenance still rereads broadly.

## H. File and script impact

Primary affected paths:

- proposed `apex-meta/scripts/apex_kb_runtime/maintenance.py`
- proposed impact/run schemas
- KB-instance `manifests/impact/` and `manifests/runs/`
- `.claude/skills/apex-kb/references/query-maintenance-workflow.md`
- current audit/lint/status/postflight paths in `apex_kb.py`
- current `log/` requirement, which becomes compatibility/history rather than mandatory operational state

# 10. Module 6 - Semantic Acceptance and Truthful Completion

## A. Module purpose and value

Acceptance proves that the durable product performs the jobs in the Target Lock. It must test not only whether a page can answer questions, but also whether the source universe was preserved, source roles are faithful, material claims are entailed, and blockers remain visible.

It prevents:

- self-approved shallow pages;
- unsupported claims;
- a complete-looking dossier with an incomplete source atlas;
- retrieval over stale or unaccepted knowledge; and
- false failure when evidence is genuinely unavailable.

## B. Current-state mismatch

### Verified current behavior

- Current main has valuable page-only target-query evaluation and material-claim entailment.
- Current postflight code includes semantic acceptance in addition to deterministic checks.
- Current acceptance schema and quality checks do not require exhaustive candidate-map closure, atlas row closure, or atlas faithfulness.
- Current structural quality still includes word/section/source-count proxies that can be satisfied without documentary completeness.
- Current command documentation and actual postflight behavior have some drift.

### Severity

**High, but lower mismatch than discovery.** Existing safeguards should be preserved; the missing acceptance dimension is map/atlas completeness.

### Facts requiring implementation-time verification

- The smallest independent acceptance packet that detects the known Leela failure without rereading the whole corpus.
- Appropriate routine-query pass threshold for each KB.
- Sampling policy, if any, for very large atlas-row faithfulness checks; critical/current rows should not be sampled.
- Whether one evaluator context can assess dossier and atlas together without context loss.

## C. Focused research and evidence

### Questions resolved

1. Is page-only answerability sufficient? No. It can pass while the documentary landscape remains incomplete.
2. Is claim entailment sufficient? No. It verifies used claims, not omitted sources or source roles.
3. Should deterministic checks judge semantic truth? No. They check counts, IDs, hashes, pointers, and closure.
4. Should independent acceptance always reread every source? No. It reads the accepted pages and the smallest evidence set needed for claims/atlas rows; complete reread is reserved for a configured audit.
5. Can unavailable evidence produce an honest accepted state? It can produce accepted-with-blockers for answered scope, but not full query readiness for obligations that depend on unavailable critical evidence.

### Sources read

- Current semantic value contract, acceptance schema, query-eval schema, quality/status/postflight code, and acceptance runbook.
- Prepared failure analysis and artifact templates.
- LLM-Wiki two-phase ingest, query evidence/gap reporting, and quick/full lint split.
- Clean-context connector runbook and compiled evaluator/orchestration guidance.

### LLM-Wiki mechanism and Apex decision

| Mechanism | Value | Apex decision | Gap |
|---|---|---|---|
| Analysis-before-generation gate | Stops immediate writing | **Keep as semantic batch separation** | No independent product acceptance |
| Quick structural vs full semantic lint | Separates cheap/expensive checks | **Copy and impact-bound** | No candidate/atlas closure |
| Query answer with evidence/confidence/gaps | Tests usability | **Adapt** into target-query acceptance | Does not test omission |
| Review queue | Preserves failures | **Adapt** into reason-coded acceptance/audit | Can become ceremony without impact scope |

## D. Final module strategy

### One acceptance artifact per topic/run

Pattern:

`audit/semantic-acceptance/<run-id>/<topic-id>.json`

It references, rather than duplicates:

- scope/registry/topic-map hashes;
- topic-analysis hash;
- dossier and atlas hashes;
- evaluator identity/model/mode;
- deterministic check results;
- page-query results;
- material-claim reviews;
- atlas completeness/faithfulness results;
- contradictions/blockers; and
- final reason-coded verdict.

### Deterministic acceptance layer

Required checks:

1. Scope closure.
2. Exhaustive map schema and no truncation.
3. Candidate ID equality between map and topic analysis.
4. Required full/targeted read coverage rules.
5. Capsule hash/pointer resolution.
6. Atlas row equality and category totals.
7. Dossier critical-query route coverage.
8. Dossier/atlas link integrity.
9. Semantic output input hashes match current deterministic artifacts.
10. Retrieval input hashes match accepted pages/atlas rows.

### Semantic acceptance layer

1. **Page-only answerability** - answer configured queries using compiled pages only.
2. **Material-claim entailment** - inspect supporting source pointers and classify entailed, contradicted, uncertain, or unsupported.
3. **Atlas faithfulness** - verify current/core/high-risk rows and a configured remainder set against source/capsule evidence.
4. **Documentary completeness reasoning** - verify that current, historical, prototype, implementation, contextual, duplicate, superseded, incidental, blocked, and irrelevant-after-review categories are represented when present.
5. **Contradiction visibility** - material unresolved disagreement must remain visible.
6. **Raw-reopen discipline** - page-only queries cannot silently reopen raw sources; raw reads occur only in entailment/faithfulness subtests.

### Verdicts

- `accepted`
- `accepted_with_blockers`
- `semantic_partial`
- `compiled_unvalidated`
- `rejected_for_repair`

`query_ready` is a runtime state, not an evaluator verdict; it requires accepted semantic results plus fresh deterministic/retrieval postflight.

### Independent-context activation

Required by default for:

- new complete builds;
- complete rebuilds;
- critical concept repairs;
- batches changing material current-state claims;
- batches adding/removing many candidates; and
- prior acceptance failures.

Configurable off for low-risk incremental changes only when deterministic impact shows no material claim/atlas-role change and the profile records the consequence.

### Failure behavior

- Evaluator unavailable: remain `compiled_unvalidated`; do not claim query readiness.
- Critical source blocked: `accepted_with_blockers` only if unanswered obligations are explicit; otherwise `semantic_partial`.
- Unsupported claim: reject only affected batch/claim set, preserve previous accepted state.
- Atlas mismatch: deterministic failure before expensive semantic evaluation.

## E. Implementation map

### Order

1. Expand semantic acceptance schema with map/atlas checks.
2. Move query-eval data into the unified acceptance artifact.
3. Add deterministic pre-evaluation closure checks.
4. Create focused evaluator packet and prompt/template.
5. Add atlas-faithfulness canaries.
6. Update postflight and status transitions.
7. Migrate old acceptance records as historical compatibility evidence.

### Tests

- Page answers all target queries but omits 40% of candidate atlas rows: fail.
- Atlas has all rows but mislabels a prototype as current: semantic fail.
- Material claim has a source ID but pointer does not entail it: fail.
- Blocked critical source remains visible and prevents full query readiness.
- Incidental and irrelevant-after-review rows remain present without being cited as evidence.
- Previous accepted page remains available after failed repair, with stale/repair state visible.
- Leela Skill Tree canary prevents the observed two-source shallow compilation.

### Measurable acceptance

- 100% deterministic closure checks pass.
- 100% critical target queries pass.
- 100% material claims are entailed, explicitly uncertain/inferred, or removed.
- 100% current/core atlas rows are faithfulness-reviewed.
- No blocker is hidden.
- Query-ready is impossible before retrieval freshness succeeds.

## F. Creation guidance

- Keep acceptance records reason-coded and reference-based.
- Do not copy source snapshots or dossier prose into the acceptance JSON.
- Do not use page word counts or source counts as semantic pass criteria.
- Do not require an evaluator for unchanged low-risk content merely to create a second opinion.
- Keep deterministic and semantic failures distinguishable so repair packets are bounded.
- Use real canaries plus synthetic fixtures; do not rely only on self-generated examples.

## G. Interconnectedness

### Upstream

Scope, maps, capsules, topic analysis, dossier, atlas, profile, and impact set.

### Downstream

Query-ready status, retrieval publication, maintenance, audit, and Git release.

### Invalidation

Any accepted input hash change invalidates the relevant acceptance result. Deterministic schema/policy changes invalidate only checks whose semantics changed; they do not silently rewrite old verdicts.

## H. File and script impact

Primary affected paths:

- `.claude/skills/apex-kb/references/semantic-acceptance.schema.json` (change)
- `.claude/skills/apex-kb/references/query-eval-pack-v2.schema.json` (merge/remove)
- `.claude/skills/apex-kb/references/semantic-value-contract.md` (split/merge)
- `.claude/skills/apex-kb/references/acceptance-tests.md` (replace with contract plus automated tests)
- proposed `semantic-acceptance-contract.md` and template
- proposed acceptance and semantic artifact tests
- current postflight/status/quality code
- KB-instance `audit/semantic-acceptance/`

# 11. Module 7 - Retrieval and Query Behavior

## A. Module purpose and value

Retrieval makes accepted dossiers and source-atlas rows fast to find. It is an accelerator and routing layer, not a source of semantic authority.

It supports:

- direct concept questions;
- source-location and source-role questions;
- contradiction/history queries;
- exact evidence navigation;
- bounded query packets; and
- durable promotion of valuable synthesis after review.

It prevents raw-corpus fallback as the ordinary query path and preserves a deterministic fallback when FTS5 is unavailable.

## B. Current-state mismatch

### Verified current behavior

- Current retrieval indexes compiled wiki pages, not raw sources.
- It chunks by headings, tracks input hashes, supports JSON lexical fallback, probes FTS5 at runtime, and uses BM25 when available.
- Current query templates preserve citations, gaps, and non-mutation boundaries.
- The current retrieval layer cannot index semantic source roles as rows because no final source-atlas product exists.
- Current query readiness remains vulnerable to upstream shallow compilation, not retrieval mechanics.

### Severity

**Moderate.** Preserve the current architecture and add row-aware atlas indexing after upstream products exist.

### Facts requiring implementation-time verification

- Best FTS5 column weights for dossier headings, atlas source paths, snapshots, individual value, lifecycle/disposition, and evidence pointers.
- Whether atlas partition pages or direct topic-analysis row indexing produce better source-location results.
- FTS5 availability in each execution environment.
- The query size at which global/per-KB index strategy becomes material.

## C. Focused research and evidence

### Questions resolved

1. Should raw sources enter the routine retrieval index? No. Accepted compiled knowledge remains the primary AI read surface.
2. Should SQLite become canonical? No. It remains derived and rebuildable.
3. Should FTS5 be mandatory? No. Runtime probe plus JSON fallback remains the correct policy.
4. What new retrieval unit is needed? Atlas source rows/partitions with typed metadata.
5. Should vector retrieval be added now? No. It is `requires_evidence_probe` after lexical/atlas canaries demonstrate a material failure.

### Sources read

- Current retrieval script, contract, query template, postflight, and status logic.
- LLM-Wiki index-first query and save-synthesis mechanisms.
- Official SQLite FTS5 and Python SQLite documentation.
- Prepared retrieval research as supporting evidence, checked against current code.

### LLM-Wiki mechanism and Apex decision

| Mechanism | Value | Apex decision | Gap |
|---|---|---|---|
| Index-first selection of a few pages | Low-token query | **Keep** | No deterministic ranked backend in original pattern |
| Read selected pages fully | Prevents snippet-only synthesis | **Keep where page size permits** | Source-location questions need row-level routing |
| Evidence/confidence/gaps | Honest answer packet | **Keep and extend** with atlas roles | No source-map completeness guarantee |
| Save reusable synthesis | Compounds value | **Configure** behind promotion/acceptance | Can duplicate dossier knowledge |

### External evidence

SQLite FTS5 supplies full-text queries, BM25 ranking, snippets/highlights, column filters, and tokenizers. FTS5 support depends on the SQLite build, and external-content designs require careful synchronization. This supports the current simple rebuildable derived-index design rather than an external-content authority layer.

## D. Final module strategy

### Indexed inputs

Only accepted compiled products:

- concept dossiers and accepted supporting pages;
- source-atlas index and partition pages;
- accepted entity/reference pages;
- optionally accepted durable query syntheses.

Raw sources, topic maps, source capsules, topic analyses, audits, and acceptance JSON are not ordinary answer corpora. They remain directly addressable for audit/repair tools.

### Chunk types

- `dossier_section`
- `atlas_source_row`
- `atlas_category_summary`
- `entity_section`
- `accepted_synthesis_section`

Every chunk stores:

- KB/topic/page identity;
- chunk type;
- heading/source ID;
- lifecycle/disposition for atlas rows;
- content and pointer text;
- accepted input hash; and
- canonical page route.

### Query behavior

1. Check accepted/retrieval freshness.
2. Search dossier and atlas columns with type-aware weights.
3. Return a bounded evidence packet with page/row routes and scores.
4. The answering model reads the smallest sufficient accepted page/section set.
5. It reports contradictions, blockers, and gaps.
6. Raw sources reopen only for dispute, missing compiled answer, or exact verification.
7. Reusable synthesis may be promoted through semantic review and dependency registration.

### Backend policy

- Always generate `search-index.json` as the portable fallback.
- Generate SQLite FTS5 when runtime probe succeeds.
- Treat both as derived.
- Rebuild from accepted pages/atlas inputs, avoiding external-content synchronization complexity.
- Vector/hybrid retrieval remains disabled until a named benchmark proves lexical failure worth the cost.

### Failure behavior

- FTS5 absent: JSON fallback, visible backend metadata.
- Index stale: strict query blocks or relaxed query reports stale state according to profile.
- Atlas missing/unaccepted: source-location queries cannot claim completeness.
- No result: report gap and route to atlas/map audit; do not fabricate.

## E. Implementation map

### Order

1. Extend chunk schema with chunk type, topic/source role, and acceptance hash.
2. Add atlas renderer output to retrieval inputs.
3. Add weighted row-aware search and filters.
4. Extend query packet/template.
5. Add source-location, history, contradiction, and blocked-source canaries.
6. Benchmark lexical/FTS5/JSON behavior before considering vectors.

### Tests

- Find a source by filename/path, snapshot text, individual value, lifecycle role, and disposition.
- Retrieve a historical source without ranking it as current authority.
- Retrieve blocked and irrelevant-after-review rows for audit questions, not ordinary factual answers.
- FTS5 and JSON fallback return equivalent source identities on core fixtures.
- Stale index blocks query-ready.
- Retrieval never indexes raw or unaccepted files.

### Acceptance

- Critical concept and source-location canaries pass.
- All returned routes resolve to accepted pages/atlas rows.
- Backend choice is visible.
- Rebuild is deterministic from accepted input hashes.

## F. Creation guidance

- Extend the existing retrieval implementation; do not replace it with a new top-level skill.
- Keep ranking weights configurable but fixture-tested.
- Index semantic roles as filters/fields, not as truth inferred by the database.
- Avoid duplicating full source capsules in retrieval.
- Keep query output compact and evidence-first.
- Do not add a vector database as an architecture ornament.

## G. Interconnectedness

### Upstream

Accepted dossiers, atlas pages, entities, query syntheses, and impact state.

### Downstream

Future AI queries, audit navigation, orchestration evidence packets, and promotion candidates.

### Invalidation

Any accepted page/atlas hash change invalidates its chunks. Source changes flow through impact/acceptance before retrieval publication.

## H. File and script impact

Primary affected paths:

- `apex-meta/scripts/apex_kb_retrieval.py`
- proposed `apex-meta/scripts/apex_kb_runtime/retrieval.py`
- `.claude/skills/apex-kb/references/retrieval-contract.md` (change/rename/merge)
- `.claude/skills/apex-kb/templates/query-output-template.md`
- KB-instance `derived/search/` and `outputs/queries/`
- retrieval fixtures/tests

# Configurable Apex KB Execution Profiles

## Independent axes

Each axis is recorded explicitly in the run manifest. Profile names are presets only.

| Axis | Allowed settings | Default | Consequence when reduced/off |
|---|---|---|---|
| Operation | `new_build`, `complete_rebuild`, `incremental_update`, `targeted_repair`, `audit_verification`, `semantic_connector_batch` | Selected from operator intent | Determines invalidation baseline and allowed outputs; never changes the product definition. |
| Source-format coverage | Per-adapter `enabled`, `inventory_only`, `disabled_by_profile`, `unavailable` | Enable text/Markdown/code/data; enable installed document adapters; inventory all others | Disabled/unavailable files remain visible. Critical blocked evidence prevents full readiness. |
| Corpus-priority coverage | `all`, named source groups, explicit path set | `all` for build/rebuild; impact set for incremental | Unprocessed in-scope rows are marked profile-disabled; run cannot claim complete scope for those obligations. |
| Topic coverage | `all_active`, explicit topic IDs, impacted topics | `all_active` for build; impacted for incremental | Unselected topics retain prior state and are not claimed refreshed. |
| Semantic depth | `maps_only`, `capsules`, `topic_analysis`, `dossier_and_atlas` | `dossier_and_atlas` for product builds | Lower depth yields truthful intermediate state, never query-ready. |
| Source read mode | `full_all`, `full_core_targeted_context`, `targeted_declared` | `full_core_targeted_context` | Targeted reads require exact spans/reason; critical current/core sources still require full reads. |
| Source-atlas depth | `full`, `classification_only`, `none` | `full` | Only `full` can satisfy final product acceptance. |
| Duplicate/version handling | `exact_only`, `normalized_family`, `semantic_resolution` | `semantic_resolution` for product builds | Reduced handling reports possible missed duplicate/version savings and limits history claims. |
| Relationship graph | `off`, `links_only`, `apex_process_graph` | `apex_process_graph` when cost is acceptable | Off may miss linked-only/process-context candidates; consequence is recorded. |
| External verification | `off`, `triggered`, `broad` | `triggered` | Off preserves internal-only scope and labels unstable/gap claims accordingly. |
| Acceptance depth | `deterministic_only`, `page_queries`, `full_product_acceptance` | `full_product_acceptance` for build/rebuild/critical repair | Lower depth cannot produce query-ready. |
| Semantic evaluator | `independent_required`, `impact_policy`, `off` | Required for build/rebuild/critical repair; impact policy for incremental | Off is allowed only for non-material changes and is recorded. |
| Retrieval backend | `json`, `fts5_if_available`, `both` | `both` | JSON remains the portable baseline; FTS5 absence is not semantic failure. |
| Execution surface | `terminal_codex`, `connector_read`, `browser_semantic`, `write_capable_mcp_probe` | Split terminal/Codex plus browser/connector semantic | Surface limitations constrain actions; no surface may claim unavailable capabilities. |
| Artifact retention | `commit_all_durable`, `commit_semantic_and_maps`, `external_derived_cache` | Commit canonical and durable map/atlas artifacts; keep SQLite rebuildable | Retention policy cannot remove future-AI access to required maps/atlases. |

## Named profiles

| Profile | Purpose | Key preset | Completion ceiling |
|---|---|---|---|
| `new_build` | Build a KB from a newly scoped corpus | All active topics, full source maps, full atlas, triggered external verification, full acceptance | `query_ready` when all obligations pass |
| `complete_rebuild` | Recompute every derived and semantic product from current canonical inputs | All source roots/topics; reuse semantic capsules only when policy explicitly permits and hashes/coverage match | `query_ready` |
| `incremental_update` | Refresh changed sources and their impact closure | Changed files plus transitive impacts; reuse unchanged capsules; impact-scoped acceptance/retrieval | `query_ready` for refreshed state |
| `targeted_repair` | Repair one concept, failed claim, atlas category, or blocked source | Explicit topic/defect; full impacted evidence; acceptance focused on repaired obligations | `query_ready` for repaired topic when global prerequisites remain fresh |
| `audit_verification` | Examine accepted knowledge without ordinary rewriting | Read-only or audit-output-only; broad or sampled faithfulness checks | `accepted`/repair backlog; no automatic mutation |
| `semantic_connector_batch` | Let a browser/connector semantic context author one coherent batch | Deterministic inputs already prepared; exact allowed output paths; no local commands/Git | `compiled_unvalidated` until import and postflight |

## Defaults requiring later operator consultation

The architecture recommends these defaults but implementation should confirm them once before coding policy:

1. Commit exhaustive topic maps and semantic topic records to Git; keep SQLite derived.
2. Use `full_core_targeted_context` as ordinary semantic read policy.
3. Enable Apex process graph for complete builds unless measured cost is disproportionate.
4. Trigger external verification only for unstable/current claims, conflicts, or named gaps.
5. Require independent acceptance for builds, rebuilds, critical repairs, and material claim changes.
6. Retain run manifests long enough for reproducibility; do not retain full semantic chat transcripts.
7. Keep `raw/` source custody and permit repository-root source pointers through `corpus-scope.json`.

# Codex / ChatGPT Web / Deterministic Runtime Orchestration

## Responsibility matrix

| Owner | Responsibilities | Forbidden work |
|---|---|---|
| Codex/orchestrator | Necessary profile Q&A, current commit resolution, deterministic commands, task-packet generation, bundle import, changed-path verification, test/postflight execution, Git commit/push/review | Deep corpus reading, semantic synthesis from snippets, semantic self-acceptance |
| ChatGPT web, strongest suitable reasoning mode | Complete/targeted source reading, authority/freshness/contradiction judgment, capsule/topic/dossier authoring, semantic output manifest | Local lifecycle scripts, repository mutation through read-only GitHub app, Git operations, false deterministic completion |
| Deterministic runtime | Inventory, extraction, postings, maps, graph, duplicate facts, schema/pointer checks, impact, atlas rendering, retrieval, observable status | Semantic truth/authority/contradiction decisions |
| Independent semantic context | Configured page-query, entailment, and atlas-faithfulness checks | Reauthoring pages during evaluation, Git, deterministic map generation |

## File handoff

```text
manifests/runs/<run-id>/run-manifest.json
manifests/runs/<run-id>/batches/<batch-id>/semantic-task-packet.md
manifests/runs/<run-id>/batches/<batch-id>/semantic-output-manifest.json
manifests/runs/<run-id>/batches/<batch-id>/import-report.json
```

The semantic model returns authored files plus the output manifest as a downloadable/transferable bundle. Codex imports only declared paths. Direct ChatGPT-web-to-repository writes are not part of the accepted design because current Deep Research/GitHub-app behavior is read-only. An automated write-capable bridge is `requires_evidence_probe`.

## Task-packet structure

| Section | Required content |
|---|---|
| Identity | Repository, branch, start commit, KB root, run/batch IDs |
| Intent | Profile, axes, topic, target questions, known failure being repaired |
| Evidence | Exact map/projection/capsule/source routes and input hashes |
| Reading contract | Full-read sources, targeted ranges allowed, duplicate representatives, blockers |
| Semantic outputs | Capsule/topic analysis/dossier paths and content obligations |
| Atlas contract | One row per candidate and required role/value/pointer fields |
| Write scope | Exact allowed paths and forbidden mutations |
| Evaluation | Required acceptance depth and critical canaries |
| Provenance | Actual model/mode to record; citations/source pointers required |
| Failure | How to report unavailable evidence, context limits, and incomplete coherent unit |

## Save-batch rules

A valid batch is one concept plus its full source atlas and required source capsules, or one tightly related source group whose semantic meaning must be resolved together. The batch must be small enough to preserve shared context and large enough to avoid arbitrary partial drafts.

## Changed-scope verification

Codex verifies:

- output paths are allowlisted;
- input map/registry/source hashes are current;
- source IDs and pointers resolve;
- schemas and candidate closure pass;
- no deterministic/runtime files were semantically authored;
- no planning/session/task state was mutated;
- generated atlas and retrieval diffs are expected; and
- Git diff matches the output manifest.

Codex does not decide whether a claim is true.

## Validation needs retained because value is demonstrated

- Out-of-root/path-safety check: protects repository custody.
- Dry-run/write-intent check: prevents accidental mutation.
- Candidate-map and atlas closure: prevents demonstrated source loss.
- Source hash/pointer validation: prevents unopened or stale evidence.
- Independent acceptance for material semantic changes: prevents self-validation.
- Retrieval stale check: prevents queries over outdated compiled pages.

## Mechanisms not retained by default

- A second general-purpose run ledger beside the run manifest.
- Per-source operator approval during controlled batches.
- Full-wiki semantic evaluation after every small update.
- Generic restart files for short batches.
- Generic hooks that restate prose rules.
- A permanent separate evaluator agent that has no changed scope.

## Token implications

- Codex packets contain routes, hashes, candidate facts, and obligations, not pasted corpus bodies.
- ChatGPT reads full core sources only once per hash and targeted contextual spans where justified.
- The independent context receives accepted pages plus the smallest evidence set needed for entailment/faithfulness.
- Deterministic maps and atlas rendering consume compute, not LLM tokens.
- Completed batches are reusable; a later failure does not force earlier reauthoring.


# Final File and Script Implementation Plan

## Final target tree

The tree below is the proposed final architecture. Paths ending in a wildcard are generated artifact families governed by the named schema; they are not invitations to invent additional contract variants.

```text
.claude/skills/apex-kb/
|-- SKILL.md
|-- package-manifest.md
|-- references/
|   |-- lifecycle-contract.md
|   |-- deterministic-artifact-contract.md
|   |-- semantic-compilation-workflow.md
|   |-- semantic-acceptance-contract.md
|   |-- query-maintenance-workflow.md
|   |-- execution-surface-contract.md
|   |-- knowledge-promotion-rules.md
|   |-- corpus-scope.schema.json
|   |-- topic-registry.schema.json
|   |-- source-inventory.schema.json
|   |-- structure-record.schema.json
|   |-- duplicate-map.schema.json
|   |-- relationship-graph.schema.json
|   |-- topic-map.schema.json
|   |-- source-capsule.schema.json
|   |-- topic-analysis.schema.json
|   |-- semantic-acceptance.schema.json
|   |-- dependency-map.schema.json
|   |-- impact-record.schema.json
|   |-- run-manifest.schema.json
|   |-- semantic-task-packet.schema.json
|   `-- semantic-output-manifest.schema.json
|-- templates/
|   |-- source-capsule-template.md
|   |-- topic-analysis-template.md
|   |-- concept-dossier-template.md
|   |-- semantic-acceptance-template.md
|   |-- semantic-task-packet-template.md
|   |-- query-output-template.md
|   |-- kb-schema-template.md
|   `-- source-manifest-template.json
|-- examples/
|   |-- powershell-commands.md
|   |-- lifecycle-runbook.md
|   `-- semantic-batch-example.md
`-- assets/
    `-- repository-semantic-contract/
        |-- contract-manifest.json
        `-- semantic-execution-contract.md

apex-meta/scripts/
|-- apex_kb.py
|-- apex_kb_retrieval.py
`-- apex_kb_runtime/
    |-- __init__.py
    |-- common.py
    |-- inventory.py
    |-- extract.py
    |-- topic_maps.py
    |-- render.py
    |-- validate.py
    |-- maintenance.py
    |-- retrieval.py
    |-- profiles.py
    `-- cli.py

apex-meta/tests/apex_kb/
|-- test_cli_contract.py
|-- test_inventory.py
|-- test_extraction_adapters.py
|-- test_topic_maps.py
|-- test_semantic_artifacts.py
|-- test_acceptance.py
|-- test_incremental_maintenance.py
|-- test_retrieval.py
`-- fixtures/
    |-- scope/
    |-- source-formats/
    |-- ambiguous-topic-matching/
    |-- duplicates-and-versions/
    |-- atlas-closure/
    |-- contradictions/
    |-- incremental-impact/
    |-- acceptance/
    `-- retrieval/

apex-meta/kb/<kb-slug>/
|-- README.md
|-- kb-schema.md
|-- raw/
|   |-- articles/
|   |-- papers/
|   |-- notes/
|   |-- refs/
|   `-- other/
|-- semantic-contract/
|   |-- contract-manifest.json
|   `-- semantic-execution-contract.md
|-- manifests/
|   |-- corpus-scope.json
|   |-- topic-registry.json
|   |-- source-manifest.json
|   |-- source-inventory.ndjson
|   |-- phase0/
|   |   |-- corpus-profile.md
|   |   |-- structure-map.ndjson
|   |   |-- term-postings.ndjson
|   |   |-- duplicate-map.json
|   |   |-- relationship-graph.ndjson
|   |   |-- topic-maps/
|   |   |   |-- <topic-id>.json
|   |   |   `-- <topic-id>.md
|   |   `-- phase0-navigation-report.md
|   |-- impact/
|   |   |-- dependency-map.json
|   |   `-- changed-source-impact.json
|   `-- runs/
|       `-- <run-id>/
|           |-- run-manifest.json
|           `-- batches/
|               `-- <batch-id>/
|                   |-- semantic-task-packet.md
|                   |-- semantic-output-manifest.json
|                   `-- import-report.json
|-- ingest-analysis/
|   |-- sources/
|   |   `-- <hash-prefix>/
|   |       `-- <sha256>.analysis.md
|   `-- topics/
|       `-- <topic-id>.analysis.json
|-- wiki/
|   |-- index.md
|   |-- concepts/
|   |   `-- <topic-or-subtopic>.md
|   |-- source-atlases/
|   |   `-- <topic-id>/
|   |       |-- index.md
|   |       `-- <optional-generated-partition>.md
|   |-- entities/
|   `-- summaries/
|-- audit/
|   |-- open/
|   |-- resolved/
|   `-- semantic-acceptance/
|       `-- <run-id>/
|           `-- <topic-id>.json
|-- outputs/
|   `-- queries/
|-- derived/
|   `-- search/
|       |-- search-index.json
|       |-- search-index.ndjson
|       |-- index.sqlite
|       `-- index-meta.json
`-- log/                         # compatibility/history only; not required run state
```

## Tree-level design decisions

1. `source-inventory.ndjson` is the canonical deterministic inventory. `source-payload-manifest.json`, CSV inventories, and old profile-specific inventories become compatibility projections during migration, not independent truth.
2. The exhaustive topic map is canonical only as a derived deterministic artifact. Its Markdown projection is compact navigation, not a candidate database.
3. The topic analysis JSON is the canonical semantic source-role record. The source atlas is generated from it and may be partitioned for readability without losing rows.
4. Source capsules are keyed by content hash and retain path aliases separately. A copy at a second path does not create a second semantic reading.
5. Dossiers live under `wiki/concepts/`; atlas pages have their own `wiki/source-atlases/` namespace so source-landscape questions do not bloat concept explanations.
6. `wiki/entities/` and `wiki/summaries/` remain supported page types, but are created only when they have independent recurring query value. They are not mandatory per source or per named noun.
7. Run state lives in `manifests/runs/`; `log/` may preserve human history but is not a second state machine.
8. The two public Python scripts remain stable operator entrypoints. Internal modules improve testability without forcing command changes.
9. JSON remains the portable retrieval baseline. SQLite is derived and optional at runtime.
10. The repository-local semantic contract is a self-contained execution packet for browser/connector contexts; it references, rather than duplicates, package schemas wherever the surface can access them.

## Current package disposition matrix

| Current path | Disposition | Final owner/target | Rationale and migration |
|---|---|---|---|
| `.claude/skills/apex-kb/SKILL.md` | `change` | Same path | Keep triggers, target, owners, lifecycle, route table, failure states, and completion states. Move detailed schemas/commands/workflows to canonical references. |
| `.claude/skills/apex-kb/package-manifest.md` | `change` | Same path | Make it generated-or-validated from the final tree; remove deprecated and removed files; add schema/runtime/test relationships. |
| `references/semantic-value-contract.md` | `merge` | `semantic-compilation-workflow.md` plus `semantic-acceptance-contract.md` | Current file mixes authoring, ledgers, acceptance, and completion. Preserve target-query and source-use safeguards; separate creation from evaluation. |
| `references/browser-git-connector-semantic-runbook.md` | `merge` | `execution-surface-contract.md` | Generalize browser-only wording into explicit terminal, Codex, connector, browser, and probed write-capable surfaces. |
| `references/topic-registry-v2.schema.json` | `change` | `topic-registry.schema.json` | Compatibility identifier remains readable; canonical schema adds phrases, aliases, supporting/negative terms, expected dossier/atlas routes, and per-axis defaults. |
| `references/semantic-run-ledger.schema.json` | `merge` | `source-capsule.schema.json`, `topic-analysis.schema.json`, and `run-manifest.schema.json` | Current ledger mixes durable source meaning, topic disposition, and run progress. Split by actual consumer and remove duplicate state. |
| `references/semantic-acceptance.schema.json` | `change` | Same semantic role under `semantic-acceptance.schema.json` | Extend from query/claim checks to four-layer product acceptance, atlas faithfulness, candidate closure, and reason-coded partial states. |
| `references/query-eval-pack-v2.schema.json` | `merge` | `semantic-acceptance.schema.json` plus topic-registry target queries | Query cases already belong to registry and acceptance; avoid a separate query-test truth source. |
| `assets/repository-semantic-contract/` | `change` | Same asset family with two final files | Keep self-contained semantic authority for connector/browser execution, but generate it from canonical contract data and include a manifest/hash. |
| `references/kb-contract.md` | `merge` | `lifecycle-contract.md` plus `deterministic-artifact-contract.md` | Separate product/canonical-state boundaries from deterministic data/CLI interfaces. |
| `references/script-command-contract.md` | `merge` | `deterministic-artifact-contract.md` | Commands are part of the deterministic artifact/runtime contract and must be generated/checked against argparse behavior. |
| `references/ingest-query-lint-audit-rules.md` | `merge` | `semantic-compilation-workflow.md` and `query-maintenance-workflow.md` | Split semantic compilation from query/maintenance; eliminate old artifact-name drift. |
| `references/retrieval-contract.md` | `merge` | `query-maintenance-workflow.md` plus retrieval schemas/tests | Preserve compiled-page boundary, hash staleness, FTS probe, and JSON fallback; add atlas-row indexing. |
| `references/lifecycle-state-machine.md` | `remove` | No active replacement file; lifecycle is canonical in `SKILL.md`/`lifecycle-contract.md` | It is already marked deprecated. Preserve its Git history and a migration note, then remove it from active package inventory. |
| `references/acceptance-tests.md` | `change` | Automated suite plus concise operator examples | Move assertions into tests/fixtures. Keep only smoke commands and canary instructions in examples/contracts. |
| `references/knowledge-promotion-rules.md` | `keep` and `change` | Same path | Preserve source/candidate/doctrine/runtime separation; remove unrelated historical source lists and link to final ownership/acceptance states. |
| `references/repo-execution-router-lint-spec.md` | `remove` | Separate repository-validation owner, only if implemented | Valuable general repo safety is not Apex KB compilation. Current spec is unexecuted and misowned. |
| `references/historical-path-authority-lint-spec.md` | `remove` | General repo validation or semantic lifecycle rules | Historical/current source role belongs in topic analysis; generic write-target lint belongs elsewhere. |
| `templates/ingest-analysis-template.md` | `merge` | `source-capsule-template.md` and `topic-analysis-template.md` | Current source-oriented page mixes reusable source meaning with topic-specific use. Split by hash reuse and candidate closure. |
| `templates/wiki-page-templates.md` | `change` | `concept-dossier-template.md` | Replace all-purpose page bundle with a dossier template; entities/summaries use schema-guided optional patterns rather than mandatory generation. |
| `templates/query-output-template.md` | `keep` and `change` | Same path | Preserve cited, reusable, read-only packet; add atlas evidence type and accepted-state hash. |
| `templates/kb-schema-template.md` | `change` | Same path | Add scope/profile defaults, page topology rules, atlas policy, and source-format adapter policy without duplicating JSON schemas. |
| `templates/source-manifest-template.json` | `keep` and `change` | Same path | Keep acquisition/custody metadata; do not duplicate derived inventory/extraction fields. |
| `examples/powershell-commands.md` | `change` | Same path | Update commands and compatibility notes; examples do not define behavior. |
| `examples/lifecycle-runbook.md` | `change` | Same path | Replace maturity-style output tiers with truthful lifecycle states and named execution profiles. |
| Proposed `examples/semantic-batch-example.md` | `add` | Same path | Demonstrate one coherent concept-plus-atlas packet/import/acceptance flow without becoming a contract. |
| `apex-meta/scripts/apex_kb.py` | `change` | Stable wrapper plus runtime package | Preserve public commands; delegate inventory/maps/validation/maintenance/profile logic to tested modules. |
| `apex-meta/scripts/apex_kb_retrieval.py` | `change` | Stable wrapper plus `retrieval.py` | Preserve health/build/stale/query/export/clear; add atlas-aware chunks and accepted-state filters. |
| `log/` as required runtime path | `configurable` | Compatibility/history only | Run manifests and Git history own reproducibility. Human logs may remain but cannot gate completion. |

## Control-plane file design records

### Entrypoint and canonical references

| Target path | Type, owner, status | Purpose and final responsibilities | Explicit non-responsibilities | Inputs -> outputs -> consumers | Required sections/interfaces and flow | Loading, micro-design evidence, migration, tests, failure, cost/risks |
|---|---|---|---|---|---|---|
| `.claude/skills/apex-kb/SKILL.md` | Skill entrypoint; semantic/orchestration owner; canonical | Trigger Apex KB, lock product target, select profile/surface, state owners, route to the correct reference, expose truthful lifecycle states | No schemas, long command catalog, duplicated templates, model label, or corpus-specific policy | Operator request + KB identity -> selected route/state -> Claude/Codex | Frontmatter; target; ownership; profile/surface routing; lifecycle; reference table; stop/failure; completion | Load on activation only. Progressive-disclosure evidence: Agent Skills/Claude/Codex skill docs and compiled informatics guide. Migrate by introducing references before deleting prose. Tests: description/links/state vocabulary. Fail closed on missing canonical reference. Low recurring token cost; risk is under-specification if references are not explicit. `change`. |
| `.claude/skills/apex-kb/package-manifest.md` | Package inventory; deterministic owner; generated/validated | List every active package asset, repo-level runtime, schema owner, compatibility alias, and test relationship | No lifecycle semantics or manually drifting command descriptions | Final tree + runtime introspection -> manifest -> operator/lint | Package identity; active inventory; runtime dependencies; canonical/derived map; generated timestamp/hash if generated | Read for maintenance, not routine semantic work. Generate or compare deterministically. Migration removes deprecated rows only after consumer scan. Tests compare disk/tree. Missing path is blocking. Very low cost. `change`. |
| `references/lifecycle-contract.md` | Reference; operator + architecture owner; canonical | Define product stages, canonical/derived artifact classes, ownership, states, source custody, promotion boundary | No parser fields, semantic page template, or CLI syntax | Target Lock + ownership decisions -> lifecycle policy -> SKILL, runtime, profiles, acceptance | Scope/custody; stages; states; owners; canonical/derived; invalid transitions; truthful partial/blocked rules | Loaded for build/repair design, not simple query. Derived from operator target and current package. Migration absorbs `kb-contract` lifecycle portions. Tests validate state names/links. Missing/contradictory state blocks execution. Low tokens; high leverage. `add/merge`. |
| `references/deterministic-artifact-contract.md` | Reference; deterministic runtime owner; canonical | Define CLI, schemas, output paths, adapter states, error taxonomy, dry-run/write rules, deterministic boundaries | No semantic relevance/authority decisions | Scope/registry/source files -> deterministic artifacts/status -> semantic workflow, tests | Command table generated/checkable against CLI; each artifact owner/schema; extraction adapter interface; write policy; compatibility projections | Loaded by Codex/runtime work. Evidence: current scripts, parser research, LLM-Wiki script split. Migration absorbs command contract and deterministic parts of kb/rules. Tests bind help output, schema, fixtures. Fail with reason-coded blocked/partial artifacts. Medium maintenance; eliminates drift. `add/merge`. |
| `references/semantic-compilation-workflow.md` | Reference; semantic owner; canonical | Define source capsule, candidate review, topic record, dossier, atlas-render handoff, contradiction/supersession judgment | No deterministic inventory, Git, retrieval build, or self-acceptance | Topic map + registry + capsules + sources -> capsules/topic analysis/dossier -> renderer/acceptance | Reading policy; authority/lifecycle/disposition model; capsule reuse; topic closure; dossier topology; output manifest | Loaded only for semantic build/update. Evidence: original/operational LLM-Wiki, current semantic safeguards, Claude skill progressive disclosure. Migration absorbs semantic-value and ingest rules. Tests use valid/invalid authored fixtures and closure checks. Truthful partial on unavailable evidence. High semantic tokens only when invoked. `add/merge`. |
| `references/semantic-acceptance-contract.md` | Reference; evaluator + deterministic validator; canonical | Define four-layer acceptance, evaluator independence policy, verdicts, repair routing, canaries | No drafting instructions or generic whole-wiki evaluation mandate | Registry + maps + topic record + pages + pointers -> acceptance artifact -> postflight/state | Deterministic closure; page-query tests; claim entailment; atlas faithfulness; activation policy; verdict/reason codes | Loaded only for acceptance/repair. Evidence: current acceptance schema/runbook plus operator source-map target. Migration extends existing schema. Tests include failures per layer. Missing evidence yields insufficient/partial, never pass. Moderate LLM cost, high failure prevention. `add/merge`. |
| `references/query-maintenance-workflow.md` | Reference; deterministic + query semantic owner; canonical | Define index-first query, atlas routing, saved synthesis promotion, audit, impact, incremental repair, stale handling | No project/task/session mutation, raw-first default, or full semantic sweep by default | Accepted products + impact/retrieval state + query/change -> answer/repair packet -> agents/operator | Query route; evidence types; stale policy; promotion; dependency/impact rules; audit ownership; repair profiles | Loaded for query/maintenance only. Evidence: LLM-Wiki query/lint/save, current retrieval, script-owned workflow guidance. Migration absorbs retrieval and query/lint/audit rules. Tests cover staleness/impact/read-only. Fail transparently with last-accepted-state policy. Medium complexity. `add/merge`. |
| `references/execution-surface-contract.md` | Reference; orchestrator owner; canonical | Define terminal, Codex, connector, browser semantic, import, write-capability probe, task/output manifests | No model marketing name or assumed connector writes | Profile/run identity + maps -> task packet/bundle/import report -> Codex/postflight | Surface capability matrix; packet/output manifest; allowed paths; commit/hash checks; actual model/mode record; failure handoff | Loaded when surface is chosen. Evidence: current OpenAI Deep Research/GitHub/Codex behavior and Claude workflow design. Migration generalizes browser runbook. Tests validate packets/import scope. Surface inability produces blocked/partial. Low recurring context because route-specific. `add/merge`. |
| `references/knowledge-promotion-rules.md` | Reference; operator/promotion owner; canonical | Preserve raw -> candidate -> reviewed -> accepted doctrine -> runtime truth distinction and high-risk owner/validator route | No KB build state machine, old role mapping, or generic migration history | Accepted KB finding + target owner/operator decision -> promotion record/change -> runtime owner | State meanings; required evidence; owner/validator; target form; rollback/deprecation | Loaded only when promoting KB knowledge into runtime doctrine. Retain current strong boundary, remove corpus-specific historical list. Tests validate prohibited direct promotion. Failure leaves candidate visible. Low cost. `keep/change`. |

### Schemas and templates

| Target path/family | Type, owner, status | Responsibilities and required fields | Non-responsibilities | Inputs/outputs/consumers | Loading/design source/migration/tests/failure/cost/risks |
|---|---|---|---|---|---|
| `references/corpus-scope.schema.json` | JSON Schema; operator/deterministic; canonical | Roots, exclusions/reasons, format adapters, path hints, pointer policy, generated-output exclusions, profile overrides | No source inventory rows or semantic authority | Operator policy -> validated scope -> inventory | Loaded by runtime/config tooling. Derived from package target/templates. Invalid scope blocks inventory; migration can synthesize a draft from current raw/pointer conventions but requires operator review. Low cost. `add`. |
| `references/topic-registry.schema.json` | JSON Schema; operator + semantic; canonical | Stable topic ID/name; primary phrases; aliases; supporting/negative terms; target queries/requirements; dossier/atlas routes; defaults | No candidate sources, rankings, or completion result | Operator/topic design -> registry -> maps, semantic work, acceptance | Compatibility reader for current registry. Tests for ambiguous vocabulary and route uniqueness. Invalid critical topic blocks its map. Low cost/high leverage. `change`. |
| `references/source-inventory.schema.json` | JSON Schema; deterministic; canonical schema for derived rows | Stable source ID/path/hash/format/size/scope/extraction/pointer/date facts/lifecycle hint rules/errors | No relevance/authority verdict | Scope + filesystem/Git/adapters -> NDJSON -> all later modules | Streamable. Tests every included/excluded/blocked state. One malformed row blocks closure but not other rows. Medium storage, low token cost. `add`. |
| `references/structure-record.schema.json` | JSON Schema; deterministic; derived | Titles/frontmatter keys, section spans, links, code spans, format-specific units, parser warnings | No semantic summary | Inventory/extractor -> structure map -> postings/maps/pointers | Adapter-specific union with common pointer interface. Tests Markdown/Office/PDF/code/data. Extraction failures remain rows. Medium compute. `add`. |
| `references/duplicate-map.schema.json` | JSON Schema; deterministic; derived | Exact hash groups, normalized-text groups, possible version-family evidence, representatives, method/confidence | No semantic supersession | Inventory/text facts -> duplicate map -> topic maps/capsule reuse/topic judgment | Conservative heuristics and reasons. Tests false-positive families. Uncertain family stays possible. Low-medium compute. `add`. |
| `references/relationship-graph.schema.json` | JSON Schema; deterministic; configurable derived | Nodes/edges for links, paths, manifests, source references, owns/handoff/process edges, line/span evidence | No inferred causal/authority relation | Structure/YAML/path/process parsing -> graph -> contextual candidates/navigation | Evidence: Apex graph audit. Adapter revision recorded. Broken targets visible. Configurable compute/storage. `add`. |
| `references/topic-map.schema.json` | JSON Schema; deterministic; derived product | Topic identity, map/input hashes, one exhaustive row per candidate, field-separated signals, pointers, duplicate/graph facts, inspectable sort vector | No semantic relevance, role, or authority | Registry + inventory/postings/duplicates/graph -> JSON map + Markdown projection -> semantic compiler/audit | No top-N in canonical set. Compatibility exporter for old rankings/map names. Tests rank-31 authoritative source and generic-term floods. Missing row is blocking. High product value. `add`. |
| `references/source-capsule.schema.json` | JSON Schema; semantic; canonical semantic record | Content hash, representations/paths, read coverage, snapshot, claims, authority/freshness evidence, contradictions, pointers, topic affordances, blockers | No topic-specific final disposition or dossier prose | Source + deterministic facts -> capsule -> topic analyses | Loaded only when source needs semantic review. Hash reuse; migration from path-oriented analyses is conservative. Tests complete/targeted/blocked coverage. High one-time tokens, strong reuse. `add`. |
| `references/topic-analysis.schema.json` | JSON Schema; semantic; canonical topic record | One row per candidate; lifecycle role; disposition; snapshot/value; authority/freshness; review mode; relationships; query/claim links; dossier plan | No duplicated source-wide claims or rendered atlas formatting | Map + capsules/source reads + registry -> JSON -> dossier/atlas/acceptance/impact | Candidate closure is deterministic. Migration imports current ledgers only when source identity resolves. Missing candidate blocks readiness. Moderate semantic/storage cost. `add`. |
| `references/semantic-acceptance.schema.json` | JSON Schema; evaluator + deterministic; canonical verdict | Inputs/hashes/model context; map/topic closure; query results; claim reviews; atlas row checks; repairs; verdict | No page authoring or aggregate score pass | Accepted candidate products -> verdict -> postflight/status | Compatibility reader for existing acceptance ID. Tests every reason code and stale input. Missing layer yields partial/fail. Moderate cost. `change`. |
| `references/dependency-map.schema.json` | JSON Schema; deterministic with semantic-declared edges; derived | Source/map/capsule/topic/claim/page/atlas/acceptance/retrieval edges, reasons, hashes | No semantic inference from undeclared prose | Artifact manifests -> dependency map -> impact | Tests transitive closure and unknown dependency fallback. Unknown edges trigger conservative invalidation. Low recurring compute. `add`. |
| `references/impact-record.schema.json` | JSON Schema; deterministic; derived run artifact | Change facts; direct/transitive invalidations; reusable artifacts; required batches/acceptance/retrieval; blockers/reasons | No semantic repair content | Prior/current dependency state -> impact report -> orchestrator | Tests no false omission and bounded over-invalidation. Failure permits complete rebuild fallback. Low recurring cost. `add`. |
| `references/run-manifest.schema.json` | JSON Schema; orchestrator/deterministic; canonical run state | Commit, KB, profile/axes, input/output hashes, batches, actual model/mode, states, blockers, changed paths | No source meaning, page claims, or chat transcript | Run operations -> manifest -> recovery/audit/Git | Script-owned resumability evidence. Atomic updates. Missing manifest blocks resumption, not existing KB use. Low storage. `add`. |
| `references/semantic-task-packet.schema.json` | JSON Schema; orchestrator; generated handoff | Identity, intent, obligations, exact evidence/read/write scope, outputs, acceptance, failure reporting | No corpus body duplication or hidden instructions | Maps/profile/impact -> packet -> semantic model | Human-readable Markdown template plus machine header/manifest. Tests path allowlist/hash freshness. Stale packet blocks import. Low token overhead. `add`. |
| `references/semantic-output-manifest.schema.json` | JSON Schema; semantic author + importer; generated handoff | Declared created/updated files, source/input hashes, completion/blockers, actual model/mode | No semantic acceptance verdict | Semantic output bundle -> manifest -> Codex importer | Tests undeclared path, changed input, missing file. Import is atomic or partial-with-report. Low overhead. `add`. |
| `templates/source-capsule-template.md` | Authoring template; semantic; canonical aid | Minimal section order for source identity/coverage/snapshot/claims/relationships/pointers/blockers | No schema duplication or topic disposition | Capsule schema + source -> authored Markdown -> topic analysts | Loaded only during capsule creation. One minimal example. Tests generated artifact against schema/parser. `add/merge`. |
| `templates/topic-analysis-template.md` | Authoring template; semantic; canonical aid | Candidate closure workflow and row examples; dossier plan | No rendered atlas rows or source-wide repeated analysis | Map/capsules -> topic JSON -> renderer/acceptance | Loaded per topic. Migration replaces current ledger template. Tests candidate count/IDs. `add/merge`. |
| `templates/concept-dossier-template.md` | Authoring template; semantic; canonical aid | Direct answer; Macro/Meso/Micro; current/evolution/implementation as relevant; claims; contradictions; atlas route; uncertainty | No mandatory source-by-source table or fixed page count | Registry/topic record -> dossier -> future AI/acceptance | LLM-Wiki concept structure adapted; no word-count gate. Tests required query routes/claim pointers. `add/change`. |
| `templates/semantic-acceptance-template.md` | Evaluator template; independent semantic; canonical aid | Page-only first, then bounded entailment/atlas checks; reason-coded repairs | No drafting or self-certification | Acceptance packet -> JSON artifact -> postflight | Loaded only for evaluator. Tests no raw read before page verdict and exact input hashes. `add`. |
| `templates/semantic-task-packet-template.md` | Handoff template; orchestrator; generated aid | Visible packet section order and failure handoff | No second profile/config source | Run/profile/impact -> packet -> ChatGPT web/semantic surface | Loaded by packet generator; example separate. Tests render/parse. `add`. |
| `templates/query-output-template.md` | Query template; deterministic + answering model; generated | Answer, evidence page/atlas rows, pointers, backend/stale/accepted hashes, gaps, reuse/promotion | No task/session mutation | Query packet + synthesis -> saved answer -> operator/future AI | Preserve current structure, add atlas type. Tests read-only fields. Stale result clearly marked. `keep/change`. |
| `templates/kb-schema-template.md` | KB policy template; operator; canonical instance config | Scope summary, domain conventions, page topology policy, profile defaults, adapter policy, query/promotion rules | No copied JSON schema or run state | Operator choices -> `kb-schema.md` -> skill/runtime | Loaded at KB-level semantic work. Tests no contradiction with manifest/registry. `change`. |
| `templates/source-manifest-template.json` | Custody template; operator/deterministic; canonical instance input | Acquisition/storage/pointer/source identity and operator metadata | No hash-derived inventory fields beyond optional acquisition hash | Source intake -> source manifest -> inventory | Compatibility with current manifest. Tests IDs/storage modes. Missing custody data visible. `keep/change`. |

## Runtime and test design records

| Target path | Type, owner, status | Purpose and final responsibilities | Explicit non-responsibilities | Inputs -> outputs -> consumers | Interfaces/control flow/loading/design source | Migration/tests/failure/token-maintenance/risks/disposition |
|---|---|---|---|---|---|---|
| `apex-meta/scripts/apex_kb.py` | Public CLI wrapper; deterministic owner; canonical executable | Preserve operator-facing lifecycle commands, global flags, exit semantics, dry-run/write policy, JSON output, compatibility projections; delegate implementation | No semantic drafting, network, Git, or large embedded business logic | CLI args + KB root -> runtime calls/results -> operator/Codex | Builds parser from `apex_kb_runtime.cli`; resolves root; invokes bounded command; emits result. Loaded only when executed. Current runtime is direct evidence; modularization follows script-owned workflow evidence | Freeze help/fixture outputs first. Tests flag placement, path safety, exit codes, compatibility names. Module import/config error returns reason-coded error without partial write. Low token cost; medium code migration risk. `change`. |
| `apex-meta/scripts/apex_kb_retrieval.py` | Public retrieval wrapper; deterministic owner; canonical executable | Preserve health/build/stale/query/export/clear commands and JSON fallback; delegate to runtime retrieval | No canonical knowledge storage, semantic answer authority, or task mutation | CLI query/build args + accepted KB artifacts -> indexes/query packets -> future AI/operator | Wrapper invokes `retrieval.py`; always reports backend/staleness/accepted input hash. Current implementation and SQLite docs are source evidence | Add atlas-aware chunks behind compatibility output. Tests FTS present/absent, stale, deterministic ordering, clear-derived-only. Failure falls back to JSON where valid. Low tokens, moderate compute. `change`. |
| `apex-meta/scripts/apex_kb_runtime/__init__.py` | Python package marker; deterministic; canonical code | Expose runtime compatibility/build identifier and supported schema IDs | No command behavior | Package import -> constants -> wrappers/tests | Minimal import surface; no side effects | Tests import on supported Python. Failure blocks CLI cleanly. Negligible cost. `add`. |
| `apex-meta/scripts/apex_kb_runtime/common.py` | Shared runtime module; deterministic; canonical code | Path containment, normalized repository-relative paths, hashes, atomic writes, JSON/NDJSON I/O, stable sort, error/result types | No domain-specific candidate or semantic logic | Paths/data -> safe primitives -> all modules | Pure/helper functions; no shell/network. Evidence: current safe write/hash patterns and LLM-Wiki idempotency | Extract first with characterization tests. Any outside-root write is hard failure. Centralization reduces duplicated guards. Medium blast-radius risk, high maintenance benefit. `add`. |
| `apex-meta/scripts/apex_kb_runtime/inventory.py` | Runtime module; deterministic; canonical code | Validate scope, walk every root, apply exclusions, source custody joins, hashes, Git facts when available, extraction dispatch status, inventory output | No concept matching or semantic lifecycle verdict | Scope + source manifest + filesystem/Git -> inventory/profile -> extract/maps | Commands: inventory/build or phase0 dependency; adapter registry invocation; stable NDJSON | Migrate payload manifest and current inventory functions. Tests 100% closure, symlinks/pointers, exclusions, missing files, same hash/new path. Fail rows individually; invalid scope blocks run. High I/O, low tokens. `add`. |
| `apex-meta/scripts/apex_kb_runtime/extract.py` | Runtime module; deterministic; canonical code | Common extraction adapter protocol; Markdown/text/code/data/Office/PDF adapters; stable spans; warnings; content-normalization fingerprints | No OCR by default, no visual semantic reading, no semantic summary | Inventory rows + adapter policy -> structure records/text units -> postings/maps | Adapter interface: `probe`, `extract`, `pointer_kind`, `revision`; state-machine Markdown baseline; optional libraries feature-probed | Migrate current Markdown parsing; add adapters incrementally within final architecture. Tests golden pointers and malformed inputs. Adapter absence yields `blocked_parser_unavailable`. Medium-high maintenance; format libraries are optional and isolated. `add`. |
| `apex-meta/scripts/apex_kb_runtime/topic_maps.py` | Runtime module; deterministic; canonical code | Normalize topic vocabulary; exhaustive field-separated postings/matches; candidate inclusion; sort vector; duplicate/graph joins; Markdown projection data | No top-N canonical truncation, relevance verdict, or authority | Registry + inventory/structure/postings/duplicates/graph -> topic maps -> semantic compiler | Functions for phrase/token normalization, ambiguous-term co-occurrence, evidence pointers, candidate classes, projections | Replaces `rank_topic_sources`; compatibility exporter emits old ranking temporarily. Tests ambiguous `tree`, path/title bonuses, candidate beyond 30, linked-only, duplicate. Any omitted matched candidate is failure. Highest leverage. `add/change`. |
| `apex-meta/scripts/apex_kb_runtime/render.py` | Runtime module; deterministic; canonical code | Render corpus profile, compact topic navigation, navigation report, source atlas partitions/index, wiki index, generated summaries | No semantic content invention or manual source-role changes | Canonical JSON/NDJSON records -> Markdown views -> LLM/human/retrieval | Renderers expose input hash/schema in output; stable headings/routes; partition without row loss | Migrate current index/report writers. Tests snapshot plus row/count equality. If canonical input invalid, do not update view. Low compute/tokens; risk of view/schema drift controlled by hashes. `add`. |
| `apex-meta/scripts/apex_kb_runtime/validate.py` | Runtime module; deterministic/evaluator coordinator; canonical code | JSON Schema validation, pointer resolution, map/topic/atlas closure, claim-source linkage, accepted-input freshness, package/tree checks | No semantic entailment judgment itself | Artifacts + schemas -> reason-coded validation -> acceptance/postflight/tests | Validation registry; strict/non-strict; machine-readable reasons; invokes no model | Consolidate current lint/quality structural checks. Tests every reason code. Failure cannot be overridden by prose. Moderate code, strong integrity. `add`. |
| `apex-meta/scripts/apex_kb_runtime/maintenance.py` | Runtime module; deterministic; canonical code | Dependency map, change detection, impact closure, incremental batch plan, stale status, audit routing, run manifest updates | No semantic repair authoring or generic full-wiki LLM sweep | Prior/current hashes + declared semantic dependencies -> impact/run artifacts -> orchestrator | Commands: impact, plan-update, status/postflight integration; atomic run updates | Add after artifact schemas. Tests unchanged reuse, new path/same hash, source removal, query change, adapter revision, unknown dependency. Failure recommends complete rebuild and preserves accepted state. Low tokens; high complexity/leverage. `add`. |
| `apex-meta/scripts/apex_kb_runtime/retrieval.py` | Runtime module; deterministic; canonical code | Build JSON/NDJSON/FTS indexes from accepted dossier/atlas rows; staleness; ranked query; evidence packets | No raw-corpus default indexing, embeddings by default, or answer synthesis | Accepted pages/topic records/atlas + query -> indexes/hits -> answering model | Chunk types for dossier sections, atlas rows, optional entities/summaries; FTS probe; JSON fallback; stable filters | Extract current retrieval implementation; add acceptance and atlas metadata. Tests BM25/fallback/pointer results. Missing FTS is nonfatal; stale accepted input is visible/blocking by policy. Medium compute. `add/change`. |
| `apex-meta/scripts/apex_kb_runtime/profiles.py` | Runtime module; operator/deterministic; canonical code | Resolve named profiles and independent axes, activation criteria, consequences, completion ceiling, capability probes | No product-stage maturity tracks or silent scope reduction | Profile/config/CLI overrides -> resolved run config -> all modules | Typed axis enums; default profiles; precedence; printable resolved config | Tests every profile/axis combination and consequence. Unknown axis/value blocks run. Very low compute/tokens. `add`. |
| `apex-meta/scripts/apex_kb_runtime/cli.py` | Runtime CLI composition; deterministic; canonical code | Define subcommands/flags, bind handlers, generate help/contract metadata, normalize flag placement | No operation implementation | Wrapper args -> parsed command -> module call | Single command registry used by wrappers and manifest/contract validation | Migrate parser after modules; characterize current flags. Tests help snapshot/legacy placement. Medium change risk. `add`. |
| `apex-meta/tests/apex_kb/test_cli_contract.py` | Automated test; validator owner; canonical test | Public command/flag/help/exit/write compatibility and generated command contract | No corpus semantic quality | CLI fixtures -> assertions -> CI/local confidence | Pytest or repository-standard runner determined at implementation probe | Must run on Windows-compatible paths and POSIX CI if available. Failure blocks migration removal. Low recurring cost. `add`. |
| `apex-meta/tests/apex_kb/test_inventory.py` | Automated test; deterministic | Scope closure, exclusion reasons, hashes, path aliases, blocked/unreadable visibility | No semantic source value | Scope/source fixtures -> inventory assertions | Uses small deterministic trees | Failure pinpoints omitted path/reason. Low cost. `add`. |
| `apex-meta/tests/apex_kb/test_extraction_adapters.py` | Automated test; deterministic | Common pointer contract and golden extraction for every enabled format; malformed/unsupported states | No semantic correctness beyond extracted text/pointers | Format fixtures -> structure records -> assertions | Adapter-specific parametrization; optional dependency skips must assert blocked state | Requires legally redistributable tiny fixtures. Medium maintenance. `add`. |
| `apex-meta/tests/apex_kb/test_topic_maps.py` | Automated test; deterministic | Exhaustiveness, field signals, strong/ambiguous vocabulary, graph/duplicate joins, projection disclosure | No authority judgment | Synthetic corpus/registry -> maps -> assertions | Canary includes authoritative candidate ranked beyond 30 and generic-term flood | Any canonical truncation or unexplained candidate is hard fail. High value. `add`. |
| `apex-meta/tests/apex_kb/test_semantic_artifacts.py` | Automated structural test; deterministic | Capsule/topic schema, candidate closure, atlas render equality, dossier claim links, migration compatibility | No judgment whether prose meaning is correct | Semantic fixtures -> validation/render -> assertions | Good/bad fixture pairs | Failure routes exact row/field/pointer. Medium cost. `add`. |
| `apex-meta/tests/apex_kb/test_acceptance.py` | Automated + stored semantic-canary harness | Four acceptance layers, stale input, evaluator activation, reason-coded verdicts | No permanent model-dependent score threshold | Accepted/failed artifacts + recorded canary outputs -> assertions | Deterministic parts always; semantic canaries run when configured | Store inputs/expected classes, not brittle exact prose. Medium recurring model cost only on selected canaries. `add`. |
| `apex-meta/tests/apex_kb/test_incremental_maintenance.py` | Automated test; deterministic | Dependency/impact precision, capsule reuse, conservative unknowns, accepted-state invalidation | No semantic content update | Before/after fixture -> impact -> assertions | Multi-topic change scenarios | False omission is fail; bounded conservative over-invalidation reported. Medium complexity. `add`. |
| `apex-meta/tests/apex_kb/test_retrieval.py` | Automated test; deterministic | JSON/FTS parity of required hits, atlas-row retrieval, stale/accepted filters, derived-only clear | No answer synthesis | Accepted fixture KB -> index/query -> assertions | FTS feature-probed; fallback always tested | Missing FTS passes fallback path; lost required hit fails. Low-medium cost. `add`. |

## KB-instance artifact design records

| Repository-relative path/family | Type, owner, canonical status | Purpose/final responsibilities and non-responsibilities | Inputs -> outputs -> consumers | Required fields/flow/relationships/loading | Migration/tests/failure/token-maintenance/risks/disposition |
|---|---|---|---|---|---|
| `apex-meta/kb/<kb-slug>/README.md` | Human orientation; operator; canonical | State KB purpose, owners, scope pointer, ordinary commands, current readiness; no schemas or run log | Operator config -> orientation -> humans/agents | Links to `kb-schema`, scope, registry, index | Keep concise. Test links/identity. Missing README is warning, not product failure. `keep/change`. |
| `apex-meta/kb/<kb-slug>/kb-schema.md` | KB policy; operator; canonical | Domain conventions, topology, profile defaults, adapter/atlas/promotion policy; no duplicate machine schemas | Template + operator decisions -> policy -> skill/semantic work | References schema IDs/paths | Existing instances migrated by explicit diff. Contradiction with JSON config blocks affected operation. Low tokens. `change`. |
| `raw/**` | Source custody; operator; canonical | Preserve immutable copies/pointers and representation identity; never generated semantic content | Intake -> source files/pointers -> inventory/semantic model | Every path resolves through source manifest/scope; large binaries may be pointers | Existing custody preserved. Missing/unreadable remains visible. Storage cost corpus-dependent. `keep`. |
| `semantic-contract/contract-manifest.json` | Execution manifest; deterministic; generated canonical handoff | List contract files/schema IDs/hash/start commit/profile compatibility | No semantic instructions itself | Package/runtime config -> manifest -> browser/connector/importer | Exact file hashes and generation version | Regenerate on package changes. Stale contract blocks semantic batch import. Tiny. `add/change`. |
| `semantic-contract/semantic-execution-contract.md` | Self-contained route contract; deterministic + semantic owner; generated | Provide browser/connector semantic instructions, output paths, schemas summarized by reference, failure handoff | No local command/Git claims or duplicated full package | Canonical contracts + KB policy -> contract -> semantic surface | Target, source/map/atlas rules, output manifest, actual model/mode, blocked state | Current scaffold asset migrates. Test consistency with canonical refs. Moderate prompt tokens, justified for surface independence. `change`. |
| `manifests/corpus-scope.json` | Operator config; canonical | Define complete source universe/exclusions/adapter policy/hints | No inventory facts or authority | Operator -> scope -> inventory/profile | Schema ID/version, roots, exclusions/reasons, formats, lifecycle-hint rules | Add to existing KB through reviewed generated draft. Invalid/missing scope prevents completeness claim. Tiny. `add`. |
| `manifests/topic-registry.json` | Operator + semantic config; canonical | Define concepts/vocabulary/questions/routes | No candidates or completion state | Operator/semantic design -> registry -> maps/dossiers/acceptance | One stable topic ID; independent vocabulary/query fields | Compatibility migration from current. Missing queries block compiled acceptance for active topic. Tiny-medium. `change`. |
| `manifests/source-manifest.json` | Custody metadata; operator/deterministic; canonical | Acquisition/storage/pointer identity and source groups | No derived extraction/relevance data | Intake -> manifest -> inventory | Stable source IDs and storage mode | Preserve current IDs. Broken pointer visible. Low. `keep/change`. |
| `manifests/source-inventory.ndjson` | Deterministic product; derived authoritative evidence map | One row for every in-scope/excluded/blocked file and representation; no semantics | Scope/manifest/files/Git/adapters -> rows -> all modules | Stable path/source/hash/extraction/pointer facts | Replaces multiple inventory/payload truths; compatibility exports during migration. Closure tests. Linear storage. `add/merge`. |
| `manifests/phase0/corpus-profile.md` | Generated view; derived | Compact corpus counts, formats, blockers, duplicate summary, map coverage; no source priority truth | Inventory/maps -> report -> operator/LLM | Input hashes/count links | If render fails, canonical data remains. Low tokens. `keep/change`. |
| `manifests/phase0/structure-map.ndjson` | Deterministic product; derived | Stable extraction structure/pointers for every readable source | Inventory/adapters -> records -> postings/maps | Common pointer union + warnings | Replaces split heading/link/frontmatter maps as canonical; optional compatibility projections. Linear storage. `add/merge`. |
| `manifests/phase0/term-postings.ndjson` | Deterministic product; derived | Exhaustive configured term/phrase postings by field/section | Registry + structure/text -> postings -> topic maps/audit | Topic/term/source/field/count/pointers/normalization | Streamable; generic corpus top terms remain a separate profile summary. Missing posting breaks affected map. Potentially large but compressible. `add`. |
| `manifests/phase0/duplicate-map.json` | Deterministic product; derived | Exact/normalized/version-family evidence and representatives | Inventory/text/Git -> groups -> maps/capsules/topic judgment | Method/confidence/members/reasons | Current exact duplicates migrate. False positive remains possible family. Low-medium storage. `add/change`. |
| `manifests/phase0/relationship-graph.ndjson` | Deterministic configurable product; derived | Explicit file/process/reference edges and missing targets | Structure/YAML/path extraction -> edges -> maps/navigation | Source/target/type/evidence/pointer/confidence | Off profile records consequence. No Obsidian dependency. Medium storage. `add`. |
| `manifests/phase0/topic-maps/<topic-id>.json` | Core deterministic product; derived authoritative candidate set | Preserve every candidate and inspectable reason/sort vector; no semantic disposition | Registry + deterministic maps -> exhaustive map -> semantic compiler/acceptance | Input hashes, candidate count, one row/source, signals/pointers | Replaces top-30 rankings. Any truncation fails. Main future-AI source discovery surface. `add/change`. |
| `manifests/phase0/topic-maps/<topic-id>.md` | Compact generated projection; derived | Read order/category/count summary with links to exhaustive JSON; no hidden candidate removal | Exhaustive map -> projection -> LLM/operator | Direct/likely/context/duplicate/blocked sections; total counts and omitted-from-view disclosure | Bounded by profile but lossless route. Low token cost. `add`. |
| `manifests/phase0/phase0-navigation-report.md` | Generated multi-topic view; derived | Populated read-first batches, blockers, duplicate families, source groups, map links, profile consequences | All Phase0 facts -> report -> orchestrator/semantic model | No copied full candidate rows; links/counts/recommended batches | Replaces shell report. Empty/skeleton report fails. Low-medium tokens. `change`. |
| `manifests/impact/dependency-map.json` | Deterministic product; derived | Artifact dependency graph with reasons/hashes | All artifact manifests + semantic-declared claim edges -> map -> impact/status | Typed edges and unknown markers | Existing artifacts without edges use conservative page invalidation. Medium storage. `add`. |
| `manifests/impact/changed-source-impact.json` | Deterministic run product; derived | Explain exact invalidation/reuse/batches/acceptance/retrieval scope | Prior/current dependency state -> report -> orchestrator | Change classes, direct/transitive affected, reasons, blockers | Rebuilt each update; may also be archived under run. Low tokens. `add`. |
| `manifests/runs/<run-id>/run-manifest.json` | Run state; deterministic/orchestrator; canonical operational record | Preserve profile, commit, inputs/outputs/batches/model/mode/blockers/state | No semantic source content or acceptance substitution | Commands/import/evaluation -> manifest -> recovery/audit/Git | Atomic state transitions and hash references | Replaces mandatory semantic progress ledger/log state. Small. `add/merge`. |
| `manifests/runs/<run-id>/batches/<batch-id>/semantic-task-packet.md` | Generated handoff; derived run artifact | Bounded semantic instructions/routes/write scope/obligations | Profile/map/impact -> packet -> semantic surface | Exact paths/hashes/read policy/output contract | Stale input blocks use/import. Moderate prompt tokens but prevents rediscovery. `add`. |
| `.../semantic-output-manifest.json` | Semantic bundle manifest; generated | Declare actual output paths, hashes, completion, blockers, model/mode | Semantic work -> manifest -> importer | Exact file list/input hash/state | Undeclared file blocks import. Tiny. `add`. |
| `.../import-report.json` | Deterministic import result; generated | Record path/hash checks, imported/rejected files, changed scope, next checks | Bundle + output manifest + repo state -> report -> Codex/run manifest | Per-file result/reason and final state | Atomic import where possible. Tiny. `add`. |
| `ingest-analysis/sources/<prefix>/<sha256>.analysis.md` | Reusable semantic source capsule; canonical semantic | Content snapshot, read coverage, authority/freshness evidence, claims, contradictions, pointers, path aliases, blockers | Source + deterministic facts -> capsule -> topic analyses | Hash/schema/model/input facts; full/targeted coverage | Migrate current analyses when exact source hash resolves; otherwise leave historical and reread. High one-time tokens, strong savings. `add/change`. |
| `ingest-analysis/topics/<topic-id>.analysis.json` | Canonical topic semantic record | One row per deterministic candidate plus dossier plan/query/claim coverage | Map + capsules/source reviews -> JSON -> atlas/dossier/acceptance/impact | Candidate closure; two-axis role/disposition; snapshot/value/pointers/relationships | Replaces all-purpose ledger. Missing row prevents acceptance. Medium tokens/storage. `add/merge`. |
| `wiki/concepts/**` | Durable compiled knowledge; LLM-authored, canonical semantic product (derived from evidence) | Answer-bearing dossiers/subpages with Macro/Meso/Micro value, claims, contradictions, routes, uncertainty | Registry/topic record/capsules -> pages -> future AI/acceptance/retrieval | Page metadata includes topic/input/accepted hashes and source pointers | Existing pages migrate by topic, not wholesale rewrite; page-only acceptance. High value, moderate maintenance. `keep/change`. |
| `wiki/source-atlases/<topic-id>/**` | Durable generated semantic view; derived from canonical topic analysis | Lossless source landscape, categories, row navigation, evidence pointers | Topic analysis -> atlas view -> future AI/audit/retrieval | Row count/hash equal topic analysis; partitions generated | If topic JSON changes, atlas invalidates/re-renders. Main source-location product. `add`. |
| `wiki/entities/**` | Optional compiled knowledge; semantic; canonical product when created | Independent recurring entity value and cross-topic routes | Topic analyses/dossiers -> entity -> future AI | Must have query value and source pointers | Existing entities retained; no mandatory extraction. Configurable cost. `keep/configurable`. |
| `wiki/summaries/**` | Optional compiled source/topic summary; semantic | Concise source view only when it adds recurring value beyond capsule/atlas | Capsule/topic record -> summary -> readers | Must not duplicate capsule wholesale | Existing summaries remain; future per-source creation configurable. `keep/configurable`. |
| `wiki/index.md` | Generated navigation; derived | Route concepts, atlases, optional entities/summaries, readiness/freshness | Accepted products -> index -> queries | One route/page, topic status, atlas route, input hash | Rebuild deterministically. Stale index reported. Low tokens. `keep/change`. |
| `audit/open/**` and `audit/resolved/**` | Human feedback; canonical audit history | Preserve feedback, target anchors, decision, resolution; no run progress | Human/semantic findings -> audit -> repair/promotion | Stable target and anchor window | Never silently discard. Existing audit migrates in place. Low volume. `keep/change`. |
| `audit/semantic-acceptance/<run>/<topic>.json` | Acceptance verdict; canonical evaluation | Four-layer result, hashes, evaluator context, repairs, verdict | Products + evaluator -> verdict -> postflight/status | Schema/input hashes; reason codes | Existing artifacts compatibility-read; stale on product change. Moderate model cost. `change`. |
| `outputs/queries/**` | Saved reusable query output; derived | Cited answer/evidence/stale status/reuse/promotion decision | Retrieval hits + answering model -> packet -> operator/future AI | Page/atlas evidence and accepted hash | Never canonical source truth by default. Retention configurable. `keep/change`. |
| `derived/search/**` | Retrieval indexes; deterministic; derived/rebuildable | JSON baseline, optional SQLite FTS5, index metadata/staleness | Accepted dossiers/atlas rows -> index -> query | Chunk/source type, topic/path/row/lines, accepted input hash | Clear/rebuild safe. Missing FTS falls back. Medium disk, near-zero LLM tokens. `keep/change`. |
| `log/**` | Optional human history; operator/compatibility; canonical only as historical note | Human-readable chronology when desired | No completion state, semantic evidence, or dependency truth | Run manifest -> optional generated summary -> human | Existing logs retained. Not required for new operations. Minimal tokens/storage. `configurable`. |

## Implementation dependency order

| Order | Implementation unit | Blocking dependencies | Observable completion evidence |
|---:|---|---|---|
| 1 | Characterization and compatibility fixtures for current CLI/package/artifacts | Current `main` | Frozen help/results, current KB sample inventory, caller map |
| 2 | Final schemas, state vocabulary, profile axes, and canonical reference skeletons | Target Lock | Schemas parse; valid/invalid fixtures; no duplicate owner |
| 3 | `common.py`, `inventory.py`, and scope/inventory migration | 1-2 | 100% scope closure on synthetic and real canary KBs |
| 4 | `extract.py`, structure map, postings, duplicate facts | 3 | Golden pointers and blocked-format visibility |
| 5 | `topic_maps.py`, projections, populated navigation report | 4 | Candidate beyond rank 30 retained; no top-N loss; direct reasons visible |
| 6 | Source capsule and topic analysis contracts/templates/import validation | 2, 5 | Hash reuse and one semantic row per candidate |
| 7 | Dossier and deterministic atlas rendering | 6 | Atlas row equality; dossier routes/claims resolve |
| 8 | Expanded acceptance and canary harness | 7 | Four-layer reason-coded verdicts |
| 9 | Dependency/impact/incremental maintenance | 3-8 | Bounded impact fixtures and reuse evidence |
| 10 | Atlas-aware retrieval and query workflow | 7-9 | Required dossier/atlas queries succeed under JSON and FTS where available |
| 11 | Profile/packet/import orchestration and repository semantic contract | 2-10 | One end-to-end semantic connector batch imported and postflighted |
| 12 | Package consolidation/removal of old references and compatibility projections | All earlier units | Consumer scan clear; current real KBs pass migration/postflight |

## Migration strategy

### Migration principles

- Migrate deterministic identity before semantic meaning.
- Never infer that an old `complete` status satisfies the final product.
- Preserve old artifacts in Git history and, where necessary, a read-only `migration/` report; do not keep two active contracts.
- Generate compatibility projections from new canonical data rather than dual-writing separate truths.
- Keep public CLI wrappers and global flag placement stable while internal modules change.
- Perform semantic migration only when source IDs/hashes and target topics resolve unambiguously.

### Repository package migration

1. Generate a package/caller inventory for all current reference names, artifact paths, and CLI commands.
2. Add final references/schemas/templates and update `package-manifest.md` to mark old files as compatibility aliases.
3. Update `SKILL.md` routing to final references while old files still exist.
4. Move runtime logic behind modules, keeping old command results for frozen fixtures.
5. Update examples and generated repository semantic contract.
6. Remove deprecated/misowned files only after repository search and real KB smoke tests show no active consumer.

### KB-instance migration

1. Create and review `corpus-scope.json`; inventory all existing source/pointer representations.
2. Generate canonical inventory/structure/postings/duplicates/topic maps while retaining old Phase 0 outputs as compatibility views.
3. Map old source analyses to hashes. Reuse only those with verifiable source coverage and pointers.
4. Map old ledgers to topic candidates. Any unmapped deterministic candidate becomes `unreviewed`, never silently irrelevant.
5. Import useful old page content as a drafting input, not accepted final knowledge.
6. Build the canonical topic analysis, render atlas, repair dossier, run final acceptance, rebuild retrieval.
7. Record migration findings and unresolved blockers in a run manifest/impact report.

### Compatibility implications

- Technical schema identifiers may increment for compatibility but do not represent product maturity.
- Existing `topic-source-rankings.json`, `topic-file-map.json`, `keyword-hits.ndjson`, and similar outputs may be emitted from final canonical structures for a defined migration window.
- Existing source payload manifests may be read as custody input; final inventory remains the canonical deterministic representation.
- Existing semantic acceptance artifacts become stale when final atlas/map obligations are introduced.
- Existing wiki pages remain queryable as last-accepted legacy content only when the query packet labels their legacy acceptance state; they are not promoted to final `query_ready` automatically.

## Implementation tests and real-corpus canaries

### Synthetic fixtures

1. Dedicated filename/heading source with few body hits versus a long generic file with many ambiguous hits.
2. Relevant source at deterministic sort position greater than 30.
3. Exact duplicate, normalized duplicate, and plausible version family with contradictory current/historical roles.
4. Linked-only/process-edge candidate.
5. Unsupported binary, scanned PDF, malformed YAML, broken pointer, and adapter-unavailable source.
6. Same content hash at two paths.
7. Topic with primary phrase, alias, supporting term, and negative ambiguous term.
8. Candidate judged irrelevant after complete review, retained in atlas.
9. Material contradiction and supersession ambiguity.
10. One changed source affecting one of several topics and one dossier claim.

### Real-corpus canaries

- **Skill Tree / Leela failure canary:** prove exhaustive candidate visibility, source-role history, no unopened evidence as support, and source-location answers from atlas.
- **Claude skill design KB:** exercise Markdown/MDX/PDF conversions, official/current/source-group authority differences, and format adapter warnings.
- **Apex KB self-knowledge canary:** compare current runtime, research intent, blueprint evidence, deprecated files, and implementation paths without treating older research as runtime authority.
- **Retrieval canary:** answer a concept-definition question and a "which sources contain what" question from dossier plus atlas under JSON fallback and FTS when available.
- **Incremental canary:** change one current implementation file and verify only affected capsule/topic/page/atlas/acceptance/retrieval artifacts invalidate.

### Acceptance for implementation completion

Implementation is complete only when:

- the final package/tree is present and current package paths have explicit final dispositions;
- current public commands and compatibility projections pass frozen fixtures;
- every enabled adapter has pointer-stable fixtures or an explicit unavailable state;
- exhaustive maps have no top-N loss;
- one real concept produces a complete dossier and atlas with four-layer acceptance;
- one incremental update demonstrates unchanged-source reuse and bounded invalidation;
- query returns both conceptual and source-landscape evidence from accepted products;
- repository semantic packet/import/postflight succeeds on the supported surface split; and
- removed files have no active current consumer.

# Cost, Token, and Complexity Audit

## Cost model

Costs are stated as relative engineering/runtime classes because corpus size, source formats, number of topics, semantic-model pricing, and change frequency are operator-specific. The implementation must instrument actual values rather than present speculative currency totals.

| Cost class | Meaning | Measurement to capture |
|---|---|---|
| One-time engineering | Code, schemas, migration, fixtures, documentation, and initial real-corpus repair | Engineering hours by module; files changed; fixtures added; migration failures |
| Deterministic build | Files read, bytes parsed, hashes, postings, graph, maps, renders, validation | Wall time; peak memory; bytes/rows produced; adapter failures |
| Semantic build | Full/targeted source reads, capsules, topic analysis, dossiers, acceptance | Input/output tokens by batch; unique hashes read; candidates reviewed; evaluator tokens |
| Recurring maintenance | Changed-file processing, impacted semantic batches, scoped acceptance, retrieval rebuild | Changed files; affected topics/claims; reused capsules; update tokens; over-invalidation |
| Storage/Git | Durable maps, capsules, topic records, atlases, run/acceptance records, derived indexes | Artifact bytes by family; diff size; compression ratio; retained run count |
| Operator attention | Scope/profile decisions, blocked evidence, promotion/high-risk choices | Number and type of operator decisions; avoid per-source routine approval counts |

## One-time implementation cost by architecture unit

| Unit | Relative cost | Main work | Why the value justifies it |
|---|---:|---|---|
| Scope, inventory, and adapters | High | Schema, exhaustive walk, custody joins, adapters, pointer fixtures | Makes omission testable and preserves blocked evidence; foundation for every later guarantee. |
| Postings and exhaustive topic maps | High | Vocabulary normalization, field signals, pointers, graph/duplicate joins, compatibility export | Repairs the demonstrated source-loss defect and produces the main future-AI routing asset. |
| Hash-keyed capsules and topic analysis | High | Semantic contracts, migration, output validation, authoring workflow | Eliminates repeat source reads and creates the canonical source-role product. |
| Dossier and atlas rendering | Medium | Dossier topology, deterministic atlas partitions, index routes | Converts semantic work into reusable concept and source-landscape products. |
| Four-layer acceptance | Medium-high | Schema, deterministic checks, evaluator packets, canaries | Prevents shallow pages and faithful-looking but incomplete atlases from reaching query readiness. |
| Dependency/impact maintenance | High | Dependency edges, invalidation, incremental packets, conservative fallbacks | Required to make ongoing maintenance cheaper than rebuilding/rereading. |
| Retrieval extension | Medium | Atlas chunks, acceptance filters, tests, compatibility | Builds on a sound current backend; adds source-landscape query value without new infrastructure. |
| Package/runtime modularization | High | Characterization, modules, tests, contract consolidation | Prevents command/schema drift and makes the complete architecture implementable and maintainable. |
| Codex/browser packet loop | Medium-high | Packet/output schemas, generator/importer, surface probes, one end-to-end canary | Enables the target low-token semantic delegation while preserving deterministic/Git ownership. |
| Optional non-text/graph/OCR capabilities | Medium to high by adapter | Feature probes, fixtures, pointer semantics, security and error handling | Valuable only when in-scope corpus formats/relationships require them; architecture includes them without forcing every run to pay. |

## Recurring cost and token drivers

| Driver | Cost risk | Final control | Required telemetry |
|---|---|---|---|
| Number of unique source hashes | Full semantic read cost grows linearly | Reusable hash capsules; duplicate representatives; targeted context policy | Unique hashes, reused capsules, full/targeted tokens per hash |
| Number of candidates per topic | Topic-review and atlas-row cost | Exhaustive maps plus compact projections; duplicate/incidentals can be classified cheaply but not omitted | Candidate count by class, average tokens per disposition |
| Large current/core sources | Expensive full reads | Coherent batches, source capsule reuse, section index for navigation | Words/tokens, read coverage, reread reason |
| Contextual sources | Risk of needless full reads | Exact targeted spans with rationale; escalate when evidence is insufficient | Targeted ranges/tokens; escalation count |
| Number of active topics | Cross-topic semantic cost | Shared capsules; impacted-topic profile; registry-level scoping | Capsules reused per topic; topics affected per change |
| Independent acceptance | Extra model pass | Run only at demonstrated-risk boundaries; deterministic closure first; bounded evidence | Evaluator tokens by layer; defects caught; false alarms |
| Full semantic lint/audit | Whole-wiki token explosion | Impact-bounded default; complete audit profile only on request or canary schedule | Pages/claims checked; defects per token |
| External verification | Web/tool latency and new source custody | Triggered policy for unstable/current/conflicted claims | Verification triggers, sources added, changed conclusion count |
| Graph extraction | CPU/storage and candidate expansion | Configurable Apex process graph; explicit edge types only | Edge count/type, graph-only useful candidates, runtime |
| OCR/visual reading | High compute/model cost and uncertain pointers | Activate only for blocked relevant images/scans; preserve confidence/page coverage | Pages/assets processed, confidence, useful claims recovered |
| Atlas size | Git/storage and navigation size | Canonical JSON plus deterministic category partitions; row-level retrieval | Rows/bytes, partitions, source-location query latency |
| Run artifact retention | Repository growth | Keep canonical maps/semantic products; prune derived indexes and old run packets by policy | Bytes by family/age; reproducibility demand |

## Expected deterministic savings

The architecture creates savings in five places:

1. **Before semantic work:** field-separated postings and compact projections replace blind recursive search and opening hundreds of files.
2. **Across topics:** one hash capsule replaces repeated full reading of the same source.
3. **Within a topic:** duplicate representatives and targeted contextual spans reduce reading without deleting candidates.
4. **During maintenance:** dependency impact replaces whole-corpus or whole-wiki semantic sweeps.
5. **At query time:** dossier sections and atlas rows replace raw-corpus retrieval and source rediscovery.

The implementation must report savings as observed ratios, not assumptions:

```text
semantic_read_reuse_ratio = reused_source_capsules / eligible_unchanged_source_hashes
raw_read_avoidance_ratio = 1 - raw_source_tokens_for_query / raw_baseline_tokens_for_query
incremental_scope_ratio = impacted_semantic_artifacts / all_semantic_artifacts
atlas_source_location_success = successful_atlas_canaries / total_source_location_canaries
acceptance_defect_yield = material_defects_caught / evaluator_tokens
```

Default product targets are those in the Target Lock; they may be tightened after measurement, but not weakened to hide source loss.

## Artifact score traceability

Every material final file/script family inherits the separate 1-100 dimensions of the component(s) that own it in Section 3. This avoids a second drifting scoring table while still making every implementation record traceable.

| Artifact/script family | Governing component scores |
|---|---|
| `SKILL.md` | H01; target/ownership rules also A01-A03, G01-G05 |
| Canonical reference contracts | H02; lifecycle A01-A05, semantic C01-C09, acceptance D01-D06, retrieval E01-E06, maintenance F01-F07, orchestration G01-G08 |
| JSON Schemas and templates | H03 plus the component represented by each schema/template |
| `apex_kb.py` wrapper and runtime modules | H04; `inventory.py` A05-A07; `extract.py` A06/B01; `topic_maps.py` B02-B08; `validate.py` D01/D04; `maintenance.py` F01-F07; `profiles.py` G01-G03 |
| `apex_kb_retrieval.py`/`retrieval.py` | E01-E04 and H04 |
| Automated test suite and canaries | H05; each test also inherits the tested component's dimensions |
| Compatibility/migration paths | H06 |
| Operator examples | H07 |
| Scope/registry/custody artifacts | A01-A05 and A07 |
| Inventory/structure/postings/duplicates/graph/maps/reports | A05-A08 and B01-B09 |
| Source capsule/topic analysis/dossier/atlas | C01-C06 and C09 |
| Acceptance artifacts | D01-D06 |
| Dependency/impact/run artifacts | F01-F03 and F07 |
| Query/retrieval artifacts | E01-E06 |
| Task/output/import packets | C09, G03-G07 |

Where an implementation agent changes the responsibility of a file, it must update the governing component link and rescore the affected component rather than invent an untraceable file score.

## Files, fields, gates, and instructions to remove or merge

| Current burden | Decision | Saving and integrity effect |
|---|---|---|
| `lifecycle-state-machine.md` beside operational `SKILL.md` | Remove after migration | Eliminates a second state authority already marked deprecated. |
| All-purpose semantic run ledger | Split/merge into capsule, topic record, run manifest | Prevents semantic facts and progress state from being written twice. |
| Separate query eval pack truth | Merge into registry target queries and acceptance | One query definition and one verdict owner. |
| `kb-contract`, command contract, and operational rules overlap | Merge into focused lifecycle/deterministic/semantic/query references | Reduces repeated paths, commands, and states. |
| Browser-specific runbook | Merge into execution-surface contract | One capability matrix instead of separate surface prose. |
| Generic repo execution/historical-path lint specs in KB package | Remove/move to correct owner | Avoids unexecuted guardrail files and KB scope drift. |
| Split heading/link/frontmatter maps as canonical truths | Merge into structure-map canonical record; compatibility projections only | One extraction record and one pointer interface. |
| Source payload manifest duplicating inventory facts | Merge into canonical inventory while retaining custody manifest | Eliminates repeated path/hash/size/extraction fields. |
| Required per-source summary page | Make configurable | Capsule and atlas already preserve source value; create a summary page only for recurring query value. |
| Mandatory entity page for every named object | Make configurable | Avoids page proliferation and maintenance without query value. |
| Fixed page word-count pass/fail | Remove as acceptance gate | Page split follows query topology; density heuristics remain advisory. |
| Whole-wiki full semantic lint after routine updates | Change to impact-bounded default | Saves model tokens while retaining complete-audit profile. |
| Per-source approval in controlled batch | Remove as default | Batch-level profile/operator lock replaces repetitive pauses. |
| Generic restart/checkpoint files | Remove as default | Run manifest and coherent saved batches preserve valuable work. |
| Repeated path/hash/format metadata in semantic artifacts | Reference source ID/inventory | Reduces authoring errors and diff noise. |
| Full chat transcripts as audit/recovery | Reject | Run/output manifests and Git preserve necessary state without private/noisy context. |

## High-cost capabilities and value gates

| Capability | Final disposition | Activation/value gate | Consequence when off or unavailable |
|---|---|---|---|
| Full non-Markdown adapter coverage | `configurable` | In-scope format exists and extraction can provide stable useful pointers | Files remain inventoried as profile-disabled or blocked; critical blocked evidence limits readiness. |
| Apex relationship/process graph | `configurable` | Graph-only candidates, dependency navigation, or process analysis create measured value | Topic maps disclose graph-off consequence; explicit term/path candidates remain. |
| OCR and visual semantic reading | `configurable` | Relevant scanned/image source cannot be resolved otherwise and cost/confidence are acceptable | Blocked source remains visible; no false text review. |
| External verification | `configurable` | Current/unstable claim, material conflict, or named research gap | Internal-only conclusion is labeled and cannot claim external currency. |
| Independent semantic evaluator | `configurable` by risk policy | Build/rebuild, critical repair, material claim/source-role change, or canary schedule | Deterministic-only validation cannot produce full acceptance where policy requires evaluator. |
| Vector/hybrid retrieval | `requires_evidence_probe` | Lexical plus atlas-aware retrieval fails measured canaries after tuning | JSON/FTS remains final supported backend; no missing product capability. |
| Node/remark extraction | `requires_evidence_probe` | Golden corpus fixtures prove Python adapters lose material structure/pointers | Python extraction remains; affected files record warnings/blockers. |
| Write-capable semantic MCP/app bridge | `requires_evidence_probe` | Exact supported API, authentication, file/path fidelity, permissions, and auditability are demonstrated | Download/import bundle remains accepted orchestration path. |
| Repository-wide cross-KB index | `configurable` and separately scoped | Repeated cross-KB queries justify routing/custody complexity | Per-KB retrieval remains complete; orchestration selects KBs explicitly. |
| Complete semantic audit | `configurable` | Operator audit, major migration, canary schedule, or impact uncertainty | Ordinary updates use impact-bounded acceptance/lint. |

## Complexity boundaries

The final architecture is deliberately multifunctional, but complexity is bounded by ownership:

- one canonical source for each fact/schema;
- one stable CLI surface with internal modules;
- one exhaustive map plus generated projections;
- one reusable source capsule per content hash;
- one canonical topic record plus generated atlas;
- one run manifest rather than overlapping ledgers/logs;
- one acceptance artifact per topic/run;
- optional capabilities behind independent axes, not separate product architectures; and
- compatibility outputs generated from canonical data, never dual-authored.

The architecture rejects convenience dependencies and generic safety layers that do not improve these boundaries.

# Implementation Acceptance Model

## Acceptance principle

Apex KB is accepted only when the durable products perform the future-AI jobs in the Target Lock. Structural validity, page answerability, claim support, and source-landscape faithfulness are separate obligations. One cannot compensate for failure in another.

No aggregate score alone may pass a topic. Acceptance is a reason-coded conjunction of required checks for the resolved profile.

## Product states

| State | Meaning | Allowed uses | Prohibited claim |
|---|---|---|---|
| `scope_invalid` | Scope/config cannot establish the source universe | Repair configuration only | Any corpus completeness claim |
| `source_scoped` | Scope and custody validate; inventory/maps not complete | Inventory/extraction work | Candidate/source coverage |
| `map_ready` | Inventory, extraction, postings, duplicates/graph as configured, exhaustive topic map, projection, and navigation report pass | Semantic source review and batch planning | Semantic relevance, accepted knowledge, query readiness |
| `semantic_partial` | Some capsules/topic rows exist, with explicit remaining/blocked candidates | Continue/recover semantic batch; inspect partial evidence | Complete dossier/atlas or source-role closure |
| `compiled_unvalidated` | Dossier and atlas render, but final acceptance not complete/current | Evaluation and repair | Accepted/query-ready knowledge |
| `accepted` | All required deterministic and semantic acceptance layers pass for current input hashes | Retrieval build and direct compiled-page use | Fresh retrieval until index hashes also match |
| `query_ready` | Accepted products and retrieval/index artifacts are fresh for the current accepted hash set | Normal query and downstream read-only consumption | Mutation of planning/session/task state |
| `stale` | Previously accepted product has an affected changed dependency | Last-accepted read only when policy exposes staleness; repair | Current/full acceptance |
| `blocked` | Required evidence/tool/source is unavailable and no honest workaround exists | Gap reporting, source acquisition, profile reconsideration | Completeness or acceptance beyond available evidence |
| `failed` | A required check ran and found a material defect | Reason-coded repair | Acceptance |

A run manifest records both the KB-wide state and per-topic state. One blocked topic does not erase accepted unrelated topics, but the KB-wide state must disclose the blocked topic.

## Acceptance layers

### Layer 1 - deterministic scope and artifact integrity

| Check | Default pass condition | Failure reason examples |
|---|---|---|
| Repository/KB identity | Repository, branch/commit, KB root, schema/profile hashes are recorded and consistent | wrong repo/ref, stale packet, mismatched KB slug |
| Scope closure | Every file beneath active roots is included, excluded-with-reason, blocked, unreadable, or profile-disabled | silent omission, generated output recursively indexed |
| Custody/pointer integrity | Every included source resolves to bytes or an explicit pointer/unavailable reason | missing pointer, hash mismatch, untracked representation |
| Inventory validity | Every row validates; stable IDs/paths/hashes are unique under defined rules | duplicate source ID, invalid path, unreasoned extraction state |
| Extraction/pointer validity | Enabled readable sources have valid structure records and pointer types; failures remain visible | pointer outside source, malformed span, swallowed parser error |
| Topic-map exhaustiveness | Every configured deterministic match appears; no canonical top-N truncation; each candidate has reasons | candidate beyond 30 omitted, unexplained candidate, missing direct match |
| Projection honesty | Compact view declares total counts/categories and links to exhaustive map | projection presented as full set, hidden blocked/duplicate rows |
| Navigation report value | Report is populated with file/topic-specific routes, blockers, duplicate/version groups, and batch guidance | artifact-name-only skeleton |
| Semantic-row closure | Topic analysis candidate IDs exactly equal topic-map candidate IDs, with explicit blocked state where necessary | missing row, extra invented source, unresolved source ID |
| Atlas render fidelity | Atlas row set and semantic values are a deterministic projection of topic analysis | hand-edited role drift, lost partition row |
| Claim/pointer linkage | Every material claim/source reference resolves to current capsule/source/pointer | missing source, stale hash, invalid range |
| Dependency/impact integrity | Accepted products and retrieval inputs match current dependency hashes | affected page remains accepted, unexplained invalidation omission |
| Package/runtime contract | Active paths exist; CLI help and command contract agree; removed references are not routed | stale command example, deprecated file loaded |

Layer 1 must pass before semantic acceptance is permitted to issue a full pass.

### Layer 2 - page-only answerability

The independent semantic context initially receives accepted-candidate dossier pages and the wiki index, not raw sources, capsules, or atlas details unless the test itself is source-location focused.

| Obligation | Default measure |
|---|---|
| Critical target queries | 100% direct, materially correct, and sufficiently complete answers from compiled pages |
| Routine target queries | Configured threshold; default at least 90% pass, with every failure reason recorded |
| Macro/Meso/Micro coverage | Every level needed by the registry answer requirements is present, not merely headed |
| Current-versus-historical clarity | Current state and evolution are distinguishable where the corpus contains both |
| Contradiction visibility | Material unresolved conflicts are exposed and affect confidence/answer wording |
| Honest gaps | Missing or blocked evidence is stated rather than filled from model memory |
| Routing utility | The answer points to relevant dossier/subpage/atlas route without reopening raw evidence |

A page may pass a question while failing source-map/atlas acceptance; the topic still does not pass the complete product.

### Layer 3 - material-claim entailment and authority fidelity

After the page-only verdict is recorded, the evaluator receives only the source capsules/exact evidence spans necessary to review material claims.

Each material claim is classified:

- `entailed`
- `partially_entailed`
- `unsupported`
- `contradicted`
- `inference_labeled`
- `operator_target_or_decision`
- `unverifiable_blocked`

Pass rules:

- every critical factual claim is `entailed`, correctly labeled inference/decision, or explicitly blocked and excluded from asserted truth;
- no unsupported or contradicted material claim remains presented as fact;
- authority/freshness judgments cite the evidence used and do not derive truth from path/date alone;
- supersession is asserted only where semantic evidence supports it; and
- source pointers resolve to the reviewed representation and coverage.

### Layer 4 - source-atlas completeness and faithfulness

| Check | Default pass condition |
|---|---|
| Candidate equality | Atlas/topic-record row count and IDs equal exhaustive topic map candidates |
| Individual snapshot | Every row explains what the file contains for the topic, or why it is blocked/irrelevant after review |
| Individual value | Every row states the source's contribution or absence of topic value, not a generic class label |
| Lifecycle role | Current, historical, prototype, implementation, contextual, or unknown is explicit and evidence-supported |
| Disposition | Core, supporting, duplicate, superseded, incidental, blocked, or irrelevant-after-review is explicit; two axes are not collapsed |
| Review coverage | Full/targeted/duplicate representative/incidental/unreadable coverage is recorded with exact ranges/reason |
| Authority/freshness | Assessment and uncertainty are explicit; deterministic hints are distinguishable from semantic judgment |
| Relationships | Duplicates, versions, contradictions, supersession, corroboration, and context relations are represented where discovered |
| Evidence pointers | Relevant rows have exact pointers; blocked rows have blocker details |
| Source-location canaries | Default at least 95% answer correctly from atlas without opening readable raw sources |
| Failure diagnosis | An auditor can tell whether a missing source came from scope, extraction, mapping, semantic review, or rendering |

## Acceptance artifact

Pattern:

`audit/semantic-acceptance/<run-id>/<topic-id>.json`

Required sections/fields:

- repository/commit/KB/run/topic/profile identity;
- exact input artifact paths and hashes;
- evaluator identity and actual model/mode;
- deterministic layer results and reason codes;
- page-only query cases/results;
- material claim reviews and evidence pointers;
- atlas closure/faithfulness checks and sampled/manual semantic row checks;
- blockers and unavailable tools/evidence;
- repair actions linked to affected artifact/row/claim;
- final verdict and permissible next state; and
- evaluator independence/changed-scope statement.

The artifact stores results, not a chain-of-thought transcript.

## Evaluator activation policy

| Change/run class | Independent semantic acceptance |
|---|---|
| New build or complete rebuild | Required for every active topic |
| Critical target-query or material claim change | Required for affected topic/claims |
| New or changed current/core source | Required for affected topic/page/atlas rows |
| Source-role or supersession change | Required for affected topic/atlas and any dossier claim |
| Targeted repair of prior semantic failure | Required for repaired obligation |
| Pure deterministic renderer/index change with byte-equivalent semantic content | Deterministic regression may suffice; policy records why evaluator is skipped |
| New path alias with existing hash and unchanged role | Deterministic atlas/inventory check normally sufficient |
| Non-material formatting/link correction | Impact-policy decision; page-query canary only when query behavior may change |
| Audit-verification profile | As selected by audit scope |

The evaluator must be a fresh context for the changed semantic scope. It does not need to be a permanent named agent.

## Retrieval acceptance

Retrieval is accepted after semantic acceptance, not as a substitute for it.

Pass conditions:

1. Index metadata references the exact accepted dossier/atlas input hashes.
2. JSON baseline builds on every supported runtime.
3. FTS5 health probe reports support accurately; absence selects fallback without data loss.
4. Required concept-definition canaries return the relevant dossier section.
5. Required source-location canaries return the relevant atlas row/category with path and pointer.
6. Contradiction/current-versus-historical canaries return evidence from both relevant roles where required.
7. Stale accepted products/indexes are identified before query.
8. Query output exposes backend, staleness, accepted hash, evidence type, page/row, heading/lines, and source pointers.
9. Clear/rebuild operations touch only derived search artifacts.
10. Retrieval results never mutate planning, task, session, or sync state.

## Incremental-maintenance acceptance

| Scenario | Expected result |
|---|---|
| Unchanged source/content hash | Capsule and unaffected semantic artifacts are reused; no semantic reread |
| Same hash at new path | Inventory and atlas path aliases update; capsule is reused |
| Changed source affects one topic | Only dependent capsule/topic rows/claims/atlas/acceptance/retrieval invalidate |
| Topic query/vocabulary changes, sources unchanged | Maps/topic analysis/query coverage update; capsules reuse unless new evidence ranges are required |
| Source removed | Historical removal remains visible; dependent claims/rows invalidate; no silent deletion from documentary history |
| Adapter revision changes pointers | Affected format re-extracts; dependent semantic pointers/acceptance invalidate |
| Unknown dependency | Conservative page/topic invalidation with explicit reason; no false query-ready claim |
| Failed semantic update | Last accepted artifacts remain intact; current affected state becomes stale/partial and retrieval behavior follows policy |

The impact report must show a reason for every invalidated and every reused artifact.

## Fixtures and real-corpus canary matrix

| Failure/product obligation | Synthetic fixture | Real-corpus canary | Acceptance owner |
|---|---|---|---|
| Silent source omission | Nested roots/exclusions/generated subtree | Leela complete source scope | Deterministic |
| Generic substring distortion | `tree`, `scope`, `chunk` in long unrelated files | Skill Tree candidate landscape | Deterministic |
| Top-30 loss | Relevant candidate at position 31+ | Skill Tree historical/prototype tail | Deterministic |
| Filename/heading signal loss | Dedicated spec with low body repetition | Apex/Claude design dedicated files | Deterministic |
| Duplicate/version reread | Exact/normalized/version family | Repeated research/patch families | Deterministic + semantic |
| Unopened evidence cited | Candidate marked used without coverage | Prior Leela failure reproduction | Deterministic acceptance |
| Path/date authority inference | Newer low-authority note vs older current implementation | Current `main` vs prior research files | Semantic |
| Incomplete source atlas | Missing/incidental/blocked row | Skill Tree source-location questions | Deterministic + semantic |
| Shallow dossier | Headings present but target queries unanswered | Apex KB architecture canaries | Page-only semantic |
| Unsupported claim | Claim points to non-entailing source | Current code behavior statements | Entailment semantic |
| Contradiction hidden | Two source claims disagree | Research intent vs current runtime | Semantic |
| Blocked non-text source invisibility | Image-only PDF/unavailable adapter | Selected document-format KB sample | Deterministic |
| Incremental over-read | One source changes among many topics | Apex KB self-knowledge update | Deterministic impact |
| Retrieval hides atlas | Query returns only dossier prose | "Which files contain what?" canary | Retrieval |
| Surface capability fiction | Read-only connector packet attempts write | ChatGPT web/Codex handoff canary | Orchestrator |
| Package/command drift | Example names removed artifact | Current command/package smoke | Automated test |

## Truthful partial and blocked behavior

- A blocked source remains in inventory, topic map, topic analysis, and atlas with its blocker and possible impact.
- A profile-disabled capability/source is distinct from unsupported/unavailable; the run records the operator/config choice and consequence.
- An incomplete semantic batch leaves completed source capsules reusable and prior accepted products intact.
- A dossier may exist while the topic is `compiled_unvalidated`; UI/index/query output must expose that state.
- A failed evaluator produces repair actions and does not rewrite the artifact being evaluated.
- A missing FTS5 backend does not block query readiness when the JSON baseline and retrieval canaries pass.
- A critical blocked source may prevent a complete semantic verdict even when all readable evidence passes.
- A connector/browser outage does not invalidate deterministic maps or accepted prior artifacts; it blocks only the pending semantic batch.
- A Git push/PR failure does not change KB semantic state; run manifest/import report records publication failure separately.

## Final implementation acceptance checklist

- [ ] Target Lock is represented in `SKILL.md`/lifecycle contract without maturity-track drift.
- [ ] Every current package file has the final disposition implemented.
- [ ] Scope closure and all enabled adapters pass fixtures and real canary inventory.
- [ ] Exhaustive topic maps have no canonical truncation and compact views disclose the exhaustive set.
- [ ] Hash capsules and topic records validate, reuse unchanged content, and close every candidate.
- [ ] Dossier and source atlas pass four-layer acceptance on at least one high-risk real concept and one unrelated concept.
- [ ] Impact analysis demonstrates bounded invalidation and truthful conservative fallback.
- [ ] JSON and available FTS retrieval pass concept and source-location canaries.
- [ ] Semantic packet/import/postflight flow records actual model/mode and changed paths.
- [ ] Current public CLI compatibility tests pass.
- [ ] Removed/deprecated files have no active consumer.
- [ ] All blocked, partial, stale, and failed states are externally visible and cannot be mislabeled query-ready.

# Source Attribution Register

This register makes the report auditable without treating every source as equal authority. Repository sources were read at the research-start commit unless stated otherwise. External sources are current official primary documentation accessed on 2026-07-14.

## Operator target and prepared package

| Source ID | Evidence class | Repository-relative source | Use in this report | Authority caveat |
|---|---|---|---|---|
| OT-01 | Operator target | This Deep Research prompt | Product target, dispositions, sequence, output contract, prohibited drift, orchestration split | Binding product intent; not implementation fact |
| PK-00 | Existing Apex research intent | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/ApexKBFinalDesignDeepResearch/00-START-HERE.md` | Package mission, evidence boundary, non-negotiable design tests | Target/routing source; commit noted inside was not treated as current `main` |
| PK-01 | Existing Apex research intent | `.../01-CURRENT-APEX-KB-FAILURE-ANALYSIS.md` | Candidate-loss diagnosis and current mismatch hypotheses | Verified against current code before adoption |
| PK-02 | Existing Apex research intent | `.../02-LIFECYCLE-COMPONENT-VALUE-MAP.md` | Seed component inventory, costs, dispositions, research questions | Explicitly rescored/regrouped rather than accepted wholesale |
| PK-03 | Existing Apex research intent | `.../03-ARTIFACT-HANDOFF-TEMPLATES.md` | Candidate schemas/interfaces for scope, maps, capsules, atlas, acceptance, impact | Rough templates, not final contracts |
| PK-04 | Existing Apex research intent | `.../04-Apex-KB-Current-Research-Index.md` | Reading order and source roles | Routing aid; current code remains authority |
| PK-05 | Existing Apex research intent | `.../05-Apex_KB_Current_Research_Index.machine-readable.yaml.md` | Machine routing and source-role cross-check | Snapshot metadata may predate research-start commit |
| PK-06 | Existing Apex research intent + blueprint synthesis | `.../06-LLM-WIKI-REPOSITORY-GUIDE.md` | Blueprint mechanism comparison and missing-capability list | Verified against directly read blueprint files |

## Current implementation authority

| Source ID | Evidence class | Repository-relative source | Functions/sections used | Main finding |
|---|---|---|---|---|
| IM-01 | Current implementation fact | `.claude/skills/apex-kb/SKILL.md` | Skill contract, lifecycle, ownership, completion | Strong boundaries and semantic safeguards, but broad/repetitive package route |
| IM-02 | Current implementation fact | `.claude/skills/apex-kb/package-manifest.md` | Active inventory, canonical/derived paths, runtime policy | Confirms active/deprecated files and standard-library/no-network runtime policy |
| IM-03 | Current implementation fact | `apex-meta/scripts/apex_kb.py` | `rank_topic_sources`, Phase 0/report, source custody, semantic/postflight/status/quality paths, CLI | Line-level substring ranking, top-30 truncation, shell navigation report, artifact drift; broad monolith |
| IM-04 | Current implementation fact | `apex-meta/scripts/apex_kb_retrieval.py` | Build/stale/query/export/clear, chunking, FTS probe/BM25, JSON fallback | Sound derived compiled-page retrieval; lacks atlas-aware contract |
| IM-05 | Current implementation fact | `.claude/skills/apex-kb/references/semantic-value-contract.md` | Target queries, candidate/read/used distinctions, source-use and acceptance rules | Valuable stopping safeguards downstream of incomplete discovery |
| IM-06 | Current implementation fact | `.claude/skills/apex-kb/templates/ingest-analysis-template.md` | Phase 1 fields and source-use structure | Path/topic-heavy artifact, not reusable hash capsule |
| IM-07 | Current implementation fact | `.claude/skills/apex-kb/templates/wiki-page-templates.md` | Page topology/required value sections | Useful Macro/Meso/Micro and claim routes; metadata/section duplication and no complete atlas |
| IM-08 | Current implementation fact | `.claude/skills/apex-kb/references/kb-contract.md` | Data/source/page boundaries | Valuable boundaries overlap other contracts |
| IM-09 | Current implementation fact | `.claude/skills/apex-kb/references/script-command-contract.md` | Command/artifact behavior | Confirms drift risk between prose and argparse/runtime |
| IM-10 | Current implementation fact | `.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md` | Phase 0/semantic/query rules | Current names/operations overlap semantic/retrieval contracts |
| IM-11 | Current implementation fact | `.claude/skills/apex-kb/references/retrieval-contract.md` | Compiled-page source boundary, staleness, backends | Retained and extended rather than replaced |
| IM-12 | Current implementation fact | `.claude/skills/apex-kb/references/acceptance-tests.md` | Smoke and semantic wiring | Useful manual acceptance material, not sufficient automated suite |
| IM-13 | Current implementation fact | `.claude/skills/apex-kb/references/browser-git-connector-semantic-runbook.md` | Connector semantic execution flow | Valuable surface split but too browser-specific and overlaps lifecycle |
| IM-14 | Current implementation fact | `.claude/skills/apex-kb/references/semantic-run-ledger.schema.json` | Run/source/topic progress fields | Mixes progress and durable semantic meaning |
| IM-15 | Current implementation fact | `.claude/skills/apex-kb/references/semantic-acceptance.schema.json` | Existing evaluator artifact | Strong seed; incomplete atlas/map layer |
| IM-16 | Current implementation fact | `.claude/skills/apex-kb/references/topic-registry-v2.schema.json` | Current topic/query vocabulary | Questions exist; vocabulary lacks strong/weak/negative distinctions |
| IM-17 | Current implementation fact | `.claude/skills/apex-kb/references/knowledge-promotion-rules.md` | Source/candidate/doctrine/runtime states | Retain core promotion boundary, simplify corpus-specific history |
| IM-18 | Current implementation fact | `.claude/skills/apex-kb/references/lifecycle-state-machine.md` | Historical states/deprecation note | Explicitly deprecated; remove from active package after migration |
| IM-19 | Current implementation fact | `.claude/skills/apex-kb/references/repo-execution-router-lint-spec.md` | Status/non-goals | Spec-only, generic repo concern, no executable consumer |
| IM-20 | Current implementation fact | `.claude/skills/apex-kb/references/historical-path-authority-lint-spec.md` | Status/non-goals | Spec-only and misowned for final KB package |

## Existing Apex research and executed design evidence

| Source ID | Evidence class | Repository-relative source | Use |
|---|---|---|---|
| AR-01 | Existing Apex research intent | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex Phase 0 Corpus Intelligence Implementation Decision.md` | Phase 0 purpose/artifacts and deterministic-semantic boundary |
| AR-02 | Existing Apex research intent | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/Apex KB × Apex Orchestration Integration Map.md` | Ownership, orchestration, retrieval/tool context; repo-specific claims reverified |
| AR-03 | LLM-Wiki blueprint synthesis | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/APEX KB — LLM-Wiki Blueprint Capability Map.md` | Operational file/process comparison |
| AR-04 | Executed research | `FutureDevelopments&Research/ProjectMM&Task&KB/KnowledgeBase/DeterministicPhaseResearch/markdown-parser-spike-report.md` | Fence-aware Python parser, pointer fields, failure cases |
| AR-05 | Executed research | `.../DeterministicPhaseResearch/Pre-LLMToolStack.md` | Tool value/installability and runtime caveats |
| AR-06 | Executed research | `.../DeterministicPhaseResearch/Apex Link Graph and Process-Flow Representability Audit.md` | Apex path/YAML/process edge types and graph value |

## Direct LLM-Wiki blueprint evidence

| Source ID | Evidence class | Repository-relative source | Mechanism used | Final Apex decision |
|---|---|---|---|---|
| BW-01 | LLM-Wiki blueprint evidence | `source-knowledge/ProjectRepos/llm-wiki/llm-wiki.md` | Persistent compounding wiki, raw/wiki/schema separation, multi-page ingest, index-first query, saved synthesis, lint | Copy product idea; add exhaustive source maps, hash capsules, atlas, acceptance, impact |
| BW-02 | LLM-Wiki blueprint evidence | `source-knowledge/ProjectRepos/llm-wiki-main/llm-wiki/SKILL.md` | Short router, workflow/script delegation, hash/idempotency, proactive index-first usage | Adapt progressive disclosure; reject always-proactive context load where not needed |
| BW-03 | LLM-Wiki blueprint evidence | `.../workflows/ingest.md` | Two-phase ingest, complete source read, contradiction/crosslink/index/manifest flow | Adapt to topic batches, exhaustive candidate maps, hash reuse, no per-file pause default |
| BW-04 | LLM-Wiki blueprint evidence | `.../workflows/query.md` | Index-first page selection, evidence/confidence/gaps, saved synthesis | Copy/adapt to dossier plus atlas and deterministic retrieval |
| BW-05 | LLM-Wiki blueprint evidence | `.../workflows/lint.md` | Cheap structural versus expensive semantic lint, persistent review queue | Keep split; make semantic checks impact-bounded |
| BW-06 | LLM-Wiki blueprint evidence | `source-knowledge/ProjectRepos/llm-wiki-skill-main/llm-wiki/SKILL.md` | Typed hierarchy, source summaries, compile/query/lint/audit, raw pointers | Configure page types; retain audit/pointers; no mandatory per-source page |
| BW-07 | LLM-Wiki blueprint evidence | `.../references/article-guide.md` | Dense concept pages, split heuristics, contradiction handling, source links | Adapt topology and contradiction practice; word counts remain advisory |

## Claude/skill/orchestration design evidence

| Source ID | Evidence class | Repository-relative source | Design decision supported |
|---|---|---|---|
| CO-01 | Claude/skill/orchestration design | `apex-meta/kb/claude-code-orchestration-design/wiki/summaries/informatics-design-formats-practice-guide.md` | One canonical schema/key owner; checkable instructions; avoid duplicated contracts |
| CO-02 | Claude/skill/orchestration design | `.../agent-skill-orchestration-resilient-workflows.md` | Script-owned plan/state for resumability; bounded independent semantic contexts |
| CO-03 | Claude/skill/orchestration design | `.../agent-subagent-design-patterns.md` | Isolate verbose reads, bounded tool/spawn scope, parallel/chained semantic work where useful |
| CO-04 | Claude/skill/orchestration design | `.../agent-vs-subagent-vs-skill.md` | Skill for reusable shared-context route; subagent for isolated self-contained work |
| CO-05 | Claude/skill/orchestration design | `.../commands-hooks-rules-memory-model.md` | Hooks only for real enforcement seams; skill/component-scoped hook boundaries |
| CO-06 | Claude/skill/orchestration design | `.../apex-application-orchestration-patterns.md` | Preserve Apex KB/Plan/Sync/Session ownership separation |

## External primary evidence

| Source ID | Evidence class | Official source | Current fact used | Recommendation derived |
|---|---|---|---|---|
| EP-01 | External primary evidence | OpenAI Help, Deep Research in ChatGPT | Deep Research can use web, uploaded files, and connected apps; it creates a source-grounded report | Use it for bounded semantic reading/synthesis, not deterministic local runtime |
| EP-02 | External primary evidence | OpenAI Help, GitHub app with ChatGPT | GitHub app can read/analyze/cite repositories and is read-only | Browser/Deep Research returns artifact bundle; do not claim direct Git writes |
| EP-03 | External primary evidence | OpenAI Codex cloud documentation | Codex connects to GitHub, runs isolated tasks, exposes diffs, and can create PRs | Codex owns deterministic commands, import verification, and Git operations |
| EP-04 | External primary evidence | OpenAI Codex skills documentation | Skills use progressive disclosure and reusable packages | Keep Apex `SKILL.md` compact and route to focused references |
| EP-05 | External primary evidence | Agent Skills specification | `SKILL.md` plus optional scripts/references/assets and progressive loading | Use focused package layout and relative references |
| EP-06 | External primary evidence | Anthropic Claude Code subagents documentation | Subagents isolate context/verbose work and are suitable for self-contained tasks | Use semantic contexts for bounded batches, not lifecycle ownership |
| EP-07 | External primary evidence | Anthropic Claude Code hooks documentation | PreToolUse can control tool calls; skill-scoped hooks exist | Retain hooks only for demonstrated path/write boundaries or direct command seams |
| EP-08 | External primary evidence | Anthropic Claude Code workflows documentation | A script can own the loop/state and support resumable workflows | Run manifest/deterministic orchestrator owns the loop |
| EP-09 | External primary evidence | SQLite FTS5 documentation | FTS5 supports MATCH/BM25/snippets; compile/runtime support varies; external-content consistency needs care | Preserve runtime probe, JSON fallback, and derived-only index |
| EP-10 | External primary evidence | Python `sqlite3` documentation | Lightweight serverless SQLite access is available through Python, subject to underlying build | Keep local standard-library retrieval wrapper |
| EP-11 | External primary evidence | PyYAML documentation | `safe_load` avoids arbitrary object construction | Use safe parsing when dependency is enabled; never silently coerce malformed YAML |
| EP-12 | External primary evidence | markdown-it-py documentation | CommonMark token parsing is available as a Python library | Optional validator when fixtures show need, not hard dependency |
| EP-13 | External primary evidence | pypdf documentation | Text extraction is not OCR; scanned/image pages require separate treatment and may be memory-heavy | Preserve blocked/visual route and activate OCR selectively |
| EP-14 | External primary evidence | python-docx documentation | DOCX paragraphs/tables can be accessed programmatically | Configurable adapter with ordinal/structural pointers |
| EP-15 | External primary evidence | python-pptx documentation | Presentation slide/shape text can be inspected without PowerPoint | Configurable slide/shape adapter; visual semantics remain separate |
| EP-16 | External primary evidence | openpyxl documentation | XLSX read/write and cell/sheet access are supported; XML security caveats exist | Configurable adapter with `defusedxml`/security probe and cell coordinates |

## Inference and recommendation notation

- A statement labeled **verified current behavior** comes from IM sources at the research-start commit.
- A statement labeled **blueprint mechanism** comes from BW sources and is not proof that Apex implements it.
- A statement about present provider/tool capability comes from EP sources and must be rechecked if implementation occurs later.
- A final architecture choice is a **recommendation**, even when strongly supported; its acceptance must be demonstrated by the listed fixtures/canaries.
- Quantitative token and source-location thresholds are product targets pending measurement, not observed results.

# Research Confidence and Future Investigation

## 1. Trusted findings

Confidence is **high** in the following architecture findings:

1. The durable source map/source atlas must be a core product, because the operator target explicitly requires future AIs to recover the full documentary landscape and the current system discards or never preserves that landscape.
2. Deterministic and semantic ownership must remain separate: scripts can inventory, extract, hash, map, validate, and retrieve; only semantic reasoning can judge relevance, authority, freshness meaning, contradiction, and supersession.
3. The final product needs both an exhaustive machine representation and a compact projection. A bounded view is useful; a bounded canonical set is destructive.
4. Reusable source understanding belongs at content-hash level, while source role/value belongs at topic level.
5. The source atlas should be generated from one canonical topic semantic record to avoid duplicated semantic truth.
6. Retrieval must remain downstream of accepted compiled knowledge and must index atlas rows as well as dossier sections.
7. Hashes plus explicit dependency edges are the correct foundation for incremental maintenance; timestamps are supporting evidence.
8. A compact skill router, focused canonical references, stable CLI wrappers, modular runtime, and real tests are the appropriate micro-architecture.
9. Codex/orchestrator, browser semantic context, and deterministic runtime should have distinct responsibilities; no current read-only connector should be described as a Git writer.
10. Generic ledgers, hooks, evaluators, and guardrails are not intrinsically valuable; each retained one in this report is tied to source custody, write scope, source loss, stale evidence, unsupported claims, or repeat-work prevention.

## 2. Current implementation facts verified directly

Verified at `main` commit `bc353b7f16d2c5ad74f376452ad4c1ff45278995`:

- the current Phase 0 topic ranking counts lowercase line-level substring hits and truncates results to 30;
- filename/path/title/H1/heading/body/link/co-occurrence signals are not represented as separate candidate evidence;
- the current Phase 0 navigation report is an artifact/phase-boundary shell rather than a populated navigation product;
- runtime and reference artifact names have drifted;
- exact duplicates are reported but do not drive routing/capsule reuse;
- current semantic contracts contain valuable target-query, candidate/read/used, disposition, page-only, and entailment safeguards;
- current semantic artifacts do not require the final lossless source atlas;
- current retrieval has compiled-page custody, heading chunks, hash staleness, FTS5 probing/BM25, and an unconditional JSON fallback;
- the package includes overlapping active contracts, an explicitly deprecated lifecycle file, and two spec-only generic lint references;
- current acceptance material is substantial but not a conventional complete automated regression suite.

These facts should be rechecked if `main` moves before implementation.

## 3. Findings with limited evidence

Confidence is **medium** in these recommendations because direct architecture evidence is strong but real production measurement is incomplete:

- one topic analysis JSON plus deterministic Markdown atlas is likely more reliable than separately authored atlas prose;
- `full_core_targeted_context` is likely the best ordinary reading policy;
- Apex process-graph extraction likely creates enough contextual-candidate and dependency value to enable on complete builds;
- modularizing the current runtime behind two stable wrappers will reduce maintenance without excessive call overhead;
- row-aware atlas retrieval should materially improve source-location queries;
- run manifests can replace mandatory progress ledgers/logs without losing recovery value;
- the proposed acceptance activation policy balances token cost and failure prevention.

Confidence is **medium-low** for non-Markdown adapter fidelity until common pointers are tested on the actual corpus.

## 4. Research hypotheses not yet validated

The following are explicit hypotheses/targets, not claimed results:

1. Accepted dossier-plus-atlas query routes can reduce raw source-reading tokens by at least 50% on the configured canaries without losing required coverage.
2. At least 95% of source-location canaries can be answered from the atlas without reopening readable raw sources.
3. Hash-capsule reuse will remove most repeated full-source reads across multi-topic corpora.
4. Impact-bounded maintenance will touch a small minority of semantic artifacts for ordinary source changes.
5. A single topic-analysis JSON remains practical and authorable at the largest expected candidate counts; deterministic partitions may be needed.
6. The relationship graph will surface enough unique useful candidates or dependency edges to justify its recurring cost.
7. Independent acceptance will catch enough material defects per token to justify the proposed activation boundaries.
8. Current JSON lexical fallback plus FTS5 and atlas-aware chunks will satisfy routine retrieval without vectors.

Implementation telemetry and canaries must confirm or revise these targets without reducing the product definition.

## 5. Remaining knowledge gaps

- Actual candidate-count and unique-hash distributions across representative Apex KBs.
- Real full-read versus targeted-read token costs by source type.
- Existing KB-instance dependence on old registry, ledger, acceptance, and artifact names.
- Current repository test runner/CI conventions and Windows path behavior.
- Actual non-Markdown source mix and the proportion of scanned/image-only PDFs.
- The most stable exact-pointer representation across DOCX, PPTX, XLSX, PDF, and connector-rendered files.
- Optimal atlas partitioning and retrieval chunk size at large row counts.
- Real false-positive/false-negative rates for normalized duplicate/version-family heuristics.
- How often current/core source roles change when path/date hints disagree with semantic evidence.
- Operator-preferred retention for run manifests, old acceptance records, query outputs, and generated compatibility projections.
- Whether cross-KB retrieval is a frequent enough use case to add a routed global index.

## 6. Possible future research

Future research is useful after implementation evidence exists, not as a precondition for the final architecture:

1. Measure map-to-semantic and dossier/atlas-to-query token savings across three differently sized KBs.
2. Benchmark JSON topic-record authoring error and repair cost against constrained Markdown/YAML at high candidate counts.
3. Evaluate graph-only candidate yield and dependency-map reuse on Apex process-heavy corpora.
4. Study duplicate/version-family precision using known historical/prototype/current file families.
5. Compare PDF/OCR/visual routes on a labeled sample and define confidence/pointer acceptance thresholds.
6. Measure JSON fallback versus FTS5 recall/latency on dossier and atlas canaries.
7. Research vector/hybrid retrieval only after collecting lexical retrieval misses that matter to target queries.
8. Evaluate one controlled write-capable MCP/app bridge only after its exact current API and audit behavior are available.
9. Assess cross-KB routing and global index value from actual orchestration query logs.
10. Revisit semantic evaluator sampling after defect-yield telemetry is available.

## 7. Capabilities requiring technical probes

| Probe | Named fact to establish | Decision affected | Pass evidence |
|---|---|---|---|
| Current-`main` pre-implementation probe | Whether commit/files/callers changed after this report | All migration anchors | Resolved commit plus changed-file/current consumer report |
| Python/test environment probe | Supported Python versions, test runner, optional dependency policy, Windows/CI paths | Runtime/test design | Reproducible local/CI smoke matrix |
| FTS5 runtime probe | Whether operator Python SQLite supports FTS5 and expected BM25/snippet behavior | Backend selection | Health command and known-result fixture; fallback always remains |
| DOCX adapter probe | Paragraph/table/order/pointer fidelity on actual files | Format activation | Golden text/pointer comparison and blocked edge cases |
| PPTX adapter probe | Slide/shape/notes/order/pointer fidelity | Format activation | Golden slide/shape records and visual-only flags |
| XLSX security/fidelity probe | `openpyxl` availability, `defusedxml` policy, formula/value/merged-cell handling | Format activation | Safe load and golden cell-coordinate records |
| PDF/OCR probe | Digitally born versus scanned detection, extraction memory, page pointer accuracy, OCR route | Format activation/acceptance | Labeled pages, pointer checks, confidence and failure states |
| Graph value probe | Unique useful graph-only candidates and impact/dependency edges | Default graph profile | Measured yield/runtime/storage on two real KBs |
| Semantic-record format probe | Model authoring/repair error for large JSON topic records | Topic analysis representation/partitioning | Controlled batches with validation/error/token metrics |
| Atlas partition probe | Row count/size where partitioning improves query/context without route loss | Renderer/retrieval | Source-location latency/token comparison with exact row equality |
| Direct write-capable bridge probe | Supported MCP/app write API, authentication, path fidelity, permissions, changed-scope audit | Orchestration import path | Controlled repository sandbox write/readback/audit; otherwise reject direct writes |
| Incremental-impact probe | False omission and over-invalidation on real changes | Maintenance policy | Labeled source-change scenarios and dependency closure review |
| Vector retrieval evidence probe | Whether lexical/atlas retrieval misses material target queries | Vector disposition | Repeated meaningful misses after lexical tuning plus measured improvement/cost |

## 8. What worked well in the research process

- The three-file access probe quickly established Mode A and prevented fallback confusion.
- Resolving the live branch commit before reading separated current implementation from older embedded commit statements.
- Reading the prepared package in order supplied a strong problem map while leaving current code authoritative.
- Direct inspection of `rank_topic_sources`, Phase 0 report generation, semantic contracts, and retrieval code identified the exact causal boundary: lossy discovery upstream, stronger safeguards downstream.
- Module-specific source bundles prevented retrieval, semantic acceptance, and skill packaging from being conflated.
- Direct LLM-Wiki files supplied concrete workflow/file evidence rather than relying only on prior comparisons.
- Compiled Claude/orchestration pages provided micro-design evidence for progressive disclosure, canonical schema ownership, script-owned state, and bounded semantic contexts.
- Official external documentation was most useful for current tool-surface facts, not for defining the Apex product.
- Separate component and tool scorecards made high-value expensive capabilities visible without using cost as a reason to omit them.

## 9. Weak sources or approaches

- Older broad Apex reports that lacked repository access remain useful for ideas but are weak for current-state claims.
- Historical files with maturity-track terminology are poor design authority for this final product and were not adopted as staged architecture.
- Hit-count research indexes are useful routing hints but can reproduce the same ambiguity/length bias as the current implementation; they were not treated as semantic authority.
- Search-result snippets and commit summaries are weaker than direct file/code reads and were used only for orientation where direct reads were available.
- Tool availability observed in prior hosted runtimes does not prove availability on the operator's current environment.
- LLM-Wiki word-count heuristics, date-based confidence, and broad full-wiki lint are useful ideas but unreliable as semantic gates.
- Community examples of local memory/retrieval may show feasibility but were unnecessary for final decisions where official docs and direct blueprints existed.
- A generic score cannot resolve semantic tradeoffs; scores in this report rank opportunity and expose cost/confidence only.

## 10. What implementation agents must verify before relying on the design

1. Resolve current `main` and diff it from the research-start commit before using any line/function/path assumption.
2. Search the whole repository for every current package file, command, schema ID, artifact name, and status before merging/removing it.
3. Freeze current CLI behavior and at least one real KB before modularization.
4. Confirm repository test/CI conventions and operator runtime before selecting optional dependencies.
5. Run scope/inventory/maps on real canaries before writing semantic migration logic.
6. Validate that every source representation has a stable repository-relative identity and record which representation was actually read.
7. Do not reuse an old source analysis without verifying content hash, coverage, and pointer resolution.
8. Treat every old topic status, ledger completion, page acceptance, and retrieval-ready flag as legacy until final map/atlas obligations pass.
9. Verify the actual current browser/connector/Codex capability before generating a task packet; never assume writes from a read-only app.
10. Instrument tokens, candidates, unique hashes, reused capsules, impact size, evaluator defects, retrieval canaries, and artifact storage from the first real run.
11. Keep compatibility projections generated from final canonical artifacts and remove them only after consumer evidence permits.
12. Preserve blocked evidence and last accepted products during failures; never make cleanup or migration erase source history.
13. Re-run the Skill Tree/Leela failure canary and an unrelated negative canary before declaring the source-mapping repair successful.
14. Require the final four-layer acceptance and fresh retrieval hashes before setting `query_ready`.

The architecture is decision-complete. The technical probes above select implementations or defaults inside it; they do not reduce or postpone the final product.
