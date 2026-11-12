---
type: Reference
id: REF-INFRASTRUCTURE-INDEX-VERIFICATION
title: Infrastructure index verification and limitations
description: Delivery evidence for source coverage, navigable links, decision excerpts, and validator applicability limits.
status: current
tags: [informatics, infrastructure, verification, evidence]
---

# Verification

This file records checks on the delivered index. It does not replace the operator's requirements or establish the correctness of a future architecture.

## Requirement-to-deliverable check

| Requirement | Delivered artifact and verification |
|---|---|
| Include Untitled 5.md explicitly | Linked in the entrypoint, coverage, catalog, topic map, and retrieval ledger; its inventory row is marked `explicit-operator-source-reviewed` with a content hash. |
| Find prior research without repeating it | Topic routing maps each question to original owners and research. All ten informatics buckets and selected precursor KBs are indexed. |
| Find decisions and provenance | Decision-family map plus 375 verbatim source mentions with path, line, and enclosing heading; excerpts are checked against current source lines. |
| Find relevant files beyond QMD | 13,470 working-tree paths with scope labels; 1,177 clickable catalog rows cover informatics, runtime entrypoints, curated knowledge, and additional leads. |
| Preserve current versus proposed and historical authority | Authority ledger, per-topic limits, source statuses, conflict table, and provenance for three remote snapshots. |
| Support the next thinking prompt | Reading order, reusable prompt-design sources, unresolved questions, capability caveats, and explicit chat-only/negative-control evaluation needs. |
| Provide a standalone processing assignment | PROCESSING-PROMPT.md combines retained repository evidence with fresh critical web research and defines the populated research package, evaluation cases, and research-only boundaries. |
| Prioritize the top 50 with exact readings | The ranked guide and JSON plan contain 50 unique sources, reading reasons, extraction questions, inclusive ranges, section hints, and file/slice hashes. |
| Supply current research inputs | The dated web brief and 16-source primary register distinguish documented capabilities, inferred design implications, abstract-level study review, and unverified installed behavior. |
| Support repository processing | All authored navigation uses repository-root-relative destinations; inventories use `repository_path` and decision rows retain separate line numbers. The converter and named source are documented in the path guide. |
| Avoid infrastructure changes | The index bundle, its master-index link, a conversion script, and the source-file move are scoped changes. No live rule, hook, agent, skill, or runtime configuration was changed. |

## Reproduction

Run the discovery command in [coverage](apex-meta/informatics/final/research/11-infrastructure-evidence-index/00-source-coverage.md). Inspect [inventory-summary.json](apex-meta/informatics/final/research/11-infrastructure-evidence-index/inventory-summary.json) alongside [files.tsv](apex-meta/informatics/final/research/11-infrastructure-evidence-index/files.tsv). Parse the TSVs with Python's `csv.DictReader(..., delimiter='\t')` and JSON with `json.loads`.

For every decision row, compare `verbatim_evidence_line` to the stripped line at `repository_path:line`. Resolve authored navigation paths from the repository root. Remote-snapshot links retain original document context and are not normalized as live bundle navigation.

The navigation check covers authored pages and the catalog. Inventory row counts and scope counts are reconciled with the summary. The original input path for Untitled 5 is mapped to its renamed source location. Repository-path correctness is checked independently of access permissions. Repeating the converter must produce no changes.

## Existing validator findings

Command:

```powershell
python apex-meta/informatics/final/tools/okf_validator.py --target apex-meta/informatics/final/research/11-infrastructure-evidence-index --json
```

The existing validator assumes that Markdown destinations are relative to the containing document. This index deliberately uses repository-root-relative identifiers for the processing program, so its link checker does not apply directly. Validate these destinations against the repository root. The validator also classifies retained evidence and reference tables as governed records:

- The retained source brief has no YAML frontmatter. Its original bytes were preserved during the move; it is evidence, not a governed specification. The validator treats all Markdown descendants as governed concept files.
- Three decision-record findings classify the topic-routing table's `Question` column as a decision matrix being authored. That table maps questions to sources; it contains no new decision recommendation.
- Four bake-off findings classify references to historical phases and cataloged titles as new bake-off records requiring phase markers and a failure-mode column.

The detecting code is in [link extraction](apex-meta/informatics/final/tools/okf_validator.py) and [shape heuristics](apex-meta/informatics/final/tools/check_decision_bakeoff_shape.py). This task did not alter those validators, strip source titles to evade them, or add invented ratings and comparison phases. The command therefore retains a nonzero exit status; no clean validator pass is claimed.

## Failure guards

Counts describe the declared working-tree snapshot, not all files ever created or all retained conversations. Decision mentions do not establish acceptance. Source-reported benchmark outcomes were not rerun. Fresh web findings appear in the dated research brief and do not establish installed behavior. The standalone prompt is ready for execution; the full downstream architecture study, hook deployment, and skill conversion remain outside this indexing step.
