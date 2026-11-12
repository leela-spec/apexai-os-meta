---
type: Reference
id: REF-INFRASTRUCTURE-SOURCE-COVERAGE
title: Source coverage and authority boundaries
description: Discovery boundary, source priorities, exclusions, and inspection limits for infrastructure research.
status: current
tags: [informatics, infrastructure, evidence, coverage]
---

# Source coverage

The operator approved an evidence index on 2026-11-12. The explicit source is [Untitled 5.md](apex-meta/informatics/final/research/11-infrastructure-evidence-index/sources/infrastructure-activation-research-brief.md). This step creates navigation and evidence extracts; it does not select infrastructure or execute the linked thinking prompt.

## Reproducible boundary

Baseline checkout: `main`, commit `58e50fad60c0d55dd116aac7460b2e4ca5316d50`, verified with `git branch --show-current` and `git rev-parse HEAD`. Working-tree files may differ from that commit.

Discovery command:

```powershell
rg --files --hidden -g '!.git/**' -g '!ki-basis/**' -g '!**/node_modules/**'
```

The inventory excludes this output bundle to avoid self-reference, except that the explicitly requested source is retained as an inventory row after its move into the bundle. It includes visible untracked files and hidden vendor directories. Ripgrep's normal ignore rules remain in force. It is a working-tree discovery inventory, not a claim that every path is committed or reachable on GitHub.

Exact counts and complete primary roots are in [inventory-summary.json](apex-meta/informatics/final/research/11-infrastructure-evidence-index/inventory-summary.json). The corresponding rows are in [files.tsv](apex-meta/informatics/final/research/11-infrastructure-evidence-index/files.tsv). These are generated from the command above, not estimated counts. Use the TSV's classifications:

| Scope | Coverage meaning |
|---|---|
| `domain-corpus` | All visible files under informatics, the selected predecessor knowledge bases, local orchestration engine, Hermes orchestration epic, Pro Thinking Prompt package, and orchestration tree. |
| `runtime-surface-or-work-record` | Root carriers, skills lock, skill template, and visible .agents/.claude/.cursor/.kiro/.windsurf/.pi descendants. Work records are not live agent definitions. |
| `discovery-candidate` | The explicitly included Untitled 5 source plus additional paths matching hook, always-on, instruction, agent, orchestration, skill, routing, carrier, prompt, or context-engineering vocabulary. |
| `outside-primary-scope` | Remaining discovered paths retained for follow-up discovery; not excluded by a full semantic review. |

## Input priority ledger

| Priority | Source | Purpose | Authority limit |
|---|---|---|---|
| 1 | Live XML, module owners, root instructions, carrier map, orchestration manifest | Establish current normative rules and ownership. | A historical file's literal `current` status cannot override a later operating owner. |
| 2 | Explicit operator decisions | Preserve approvals, non-goals, pilot requirements, and rejections. | Preserve each decision's date, domain, and conditions. |
| 3 | Original benchmark protocols, fixtures, results, and traces | Establish observed behavior and confounds. | Reported results do not become new reruns or cross-CLI proof. |
| 4 | Research buckets 01–10 and predecessor KBs | Recover origins, alternatives, and questions already studied. | Research recommendations require adoption evidence before becoming live rules. |
| 5 | Untitled 5, Handovers 13–15, proposed hook design | Capture latest intent and integration questions. | Proposed instructions authorize neither deployment nor mutation of existing rules. |
| 6 | Other discovery candidates | Detect relevant work omitted by older indexes. | Read source content before relying on a filename match. |

## Inspection depth and duplicate detection

`metadata-and-decision-extraction` means eligible text files below 1,500,000 bytes were parsed for title, literal status, and decision mentions. It does not mean their arguments were reviewed. `path-only` means the inventory retains the filename without substantive extraction. `inaccessible` records an operating-system access failure in `access_error`.

SHA-256 covers bytes actually read. `exact_duplicate_of` points to an earlier equal-byte file in the inventory. It neither establishes canonical ownership nor detects paraphrases. Large files and binary contents remain path-level leads. Decision extracts omit raw and derived directories to reduce repetitive mentions, while their files remain in the full inventory.

Targeted content review informed the topic map: the supplied seed, informatics indexes and standards, task and close-out adapters, candidate decision register, instruction-access matrix, routing-reality analysis, carrier map, routing pilot, seven-topic synthesis, latest benchmark verdict, Handover 13, remote Handovers 14–15 and hook design, Claude project router/settings, orchestration manifest, precursor mechanism summary/operator decisions, Hermes decisions, and local-model decision-lock headings. This is not a full-content audit of every inventoried file.

## Exclusions and failure guards

Git internals, node_modules, normally ignored files, conversations outside the repository, and workstation-global configuration are outside the baseline. The Windows environment boundary excludes the ki-basis tree and stack. Existing historical WSL links remain evidence pointers, not execution instructions.

The selected precursor KBs include raw evidence and source manifests in the TSV. The human catalog favors curated pages and entrypoints. Its omission of a raw payload row is not an inventory omission.

The index does not claim that metadata extraction yields every decision, that repeated IDs represent unique rules, or that every source marked current is authoritative. Before changing a decision, retrieve its original context and later owner. Before claiming runtime behavior, inspect the installed configuration and run an appropriate probe.
