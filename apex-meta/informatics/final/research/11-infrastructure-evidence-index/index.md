---
okf_version: "0.2"
type: Reference
id: REF-APEX-INFRASTRUCTURE-EVIDENCE-INDEX
title: Apex infrastructure research and decision index
description: Evidence entrypoint for designing the next repository, CLI-agent, instruction, skill, hook, routing, and verification architecture without repeating prior research.
status: current
tags: [informatics, infrastructure, research-index, decisions, agents, hooks, skills]
---

# Infrastructure research and decision index

**Run the research:** use the standalone [processing prompt](apex-meta/informatics/final/research/11-infrastructure-evidence-index/PROCESSING-PROMPT.md). Its inputs include the [ranked top-50 reading guide](apex-meta/informatics/final/research/11-infrastructure-evidence-index/06-ranked-reading-guide.md) and [current web research](apex-meta/informatics/final/research/11-infrastructure-evidence-index/07-current-web-research.md). The guide gives reasons, exact inclusive line ranges, and source hashes. It prioritizes reading without limiting the wider research scope.

All navigation paths in this index are relative to the repository root, for example `apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml`. Resolve them through the processor's authenticated repository access. The inventories use `repository_path`; no workstation prefix, hostname, or branch is required. See [path conventions and conversion](apex-meta/informatics/final/research/11-infrastructure-evidence-index/05-online-access.md).

Use this index as the evidence attachment for the next thinking prompt. It maps prior work and sources; it does not adopt a new architecture. Include [infrastructure-activation-research-brief.md](apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md) as the operator's explicit seed source. Its proposed classification and conversation claims require comparison with the underlying owners and evidence.

## Reading order

1. Read [source coverage and authority](apex-meta/informatics/final/research/11-infrastructure-evidence-index/00-source-coverage.md) to establish scope and inspection limits.
2. Read [research, decisions, and unanswered questions](apex-meta/informatics/final/research/11-infrastructure-evidence-index/01-research-and-decision-map.md) to avoid reopening solved questions without new evidence.
3. Read the live [contract](apex-meta/informatics/final/specs/apex_contract_v1.0_ultra.xml), [module router](apex-meta/informatics/final/specs/general-informatics-router.md), [carrier map](apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md), and [orchestration manifest](apex-meta/orchestration/CURRENT-SYSTEM-MANIFEST.yaml) for their respective owners.
4. Read [Handover 14](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/HANDOVER-14-APEX-RULE-REGISTRY-AND-ACTIVATION-INTEGRATION.md) and [Handover 15](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY-RESEARCH-PROMPT.md) as proposed research scope and prompt. Their remote-source provenance appears in [retrieval and gaps](apex-meta/informatics/final/research/11-infrastructure-evidence-index/03-retrieval-and-gaps.md).
5. Retrieve relevant original passages through the [file catalog](apex-meta/informatics/final/research/11-infrastructure-evidence-index/02-file-catalog.md), [complete path inventory](apex-meta/informatics/final/research/11-infrastructure-evidence-index/files.tsv), and [verbatim decision mentions](apex-meta/informatics/final/research/11-infrastructure-evidence-index/decision-evidence.tsv).

## What each artifact provides

| Artifact | Use |
|---|---|
| [Processing prompt](apex-meta/informatics/final/research/11-infrastructure-evidence-index/PROCESSING-PROMPT.md) | Standalone assignment combining repository ingestion, current web research, architecture comparison, and a complete proposed research package. |
| [Top-50 reading guide](apex-meta/informatics/final/research/11-infrastructure-evidence-index/06-ranked-reading-guide.md) | Ordered file priorities, why to read them, exact windows, and questions to answer. |
| [Machine-readable reading plan](apex-meta/informatics/final/research/11-infrastructure-evidence-index/top50-reading-plan.json) | Full file and slice hashes, line counts, section hints, and structured ranges for all 50 files. |
| [Current web research](apex-meta/informatics/final/research/11-infrastructure-evidence-index/07-current-web-research.md) | Dated primary-source findings, study limitations, and the deeper research agenda. |
| [Coverage](apex-meta/informatics/final/research/11-infrastructure-evidence-index/00-source-coverage.md) | Source priorities, inclusion rules, exclusions, and evidence limits. |
| [Research and decision map](apex-meta/informatics/final/research/11-infrastructure-evidence-index/01-research-and-decision-map.md) | Topic-specific owners, previous choices, experiment caveats, and remaining questions. |
| [File catalog](apex-meta/informatics/final/research/11-infrastructure-evidence-index/02-file-catalog.md) | Clickable file-level navigation, including every inventoried informatics file and local skill entrypoint. |
| [Files TSV](apex-meta/informatics/final/research/11-infrastructure-evidence-index/files.tsv) | Broader repository discovery tree with metadata, inspection labels, content hashes where read, and exact-byte duplicate pointers. |
| [Decision evidence TSV](apex-meta/informatics/final/research/11-infrastructure-evidence-index/decision-evidence.tsv) | Source path, exact line, enclosing heading, and verbatim decision mention; not a normalized decision registry. |
| [Inventory totals](apex-meta/informatics/final/research/11-infrastructure-evidence-index/inventory-summary.json) | Machine-readable counts and complete primary scope roots. |
| [Retrieval and gaps](apex-meta/informatics/final/research/11-infrastructure-evidence-index/03-retrieval-and-gaps.md) | Reproducible QMD searches, source snapshots, conflicts, and deferred capability checks. |
| [Verification](apex-meta/informatics/final/research/11-infrastructure-evidence-index/04-verification.md) | Requirement coverage, reproducible checks, and existing validator limitations. |

## Research handoff constraints

Treat the full chain as the unit of analysis: rule owner → applicability → activation → context delivery → execution → independent verification → maintenance. Cover conversational Q&A and rankings alongside file operations, engineering, research, compaction, and resumption.

Preserve accepted choices and their original scope. Reopen them only with a specific unresolved question or changed evidence. Compare all-references-as-skills, selective workflow skills, reference routing, scoped native rules, hooks, injection, and hybrids without assuming the winner.

Do not equate reading a rule with following it. Do not equate a design document with installed behavior. Do not generalize an Antigravity benchmark to all CLIs. Do not interpret linked research prompts as instructions to execute their research or install their proposals during this indexing task.

## Failure guards

The inventory is comprehensive within its declared discovery boundary; semantic extraction is selective. Path-only files and older sources remain discoverable, not fully adjudicated. Missing histories, unavailable traces, ignored local configuration, and installed-version compatibility remain explicit evidence gaps.
