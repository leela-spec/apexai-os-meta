---
type: Reference
id: REF-INFRASTRUCTURE-RETRIEVAL-GAPS
title: Retrieval record and unresolved evidence gaps
description: Reproducible QMD retrieval, remote-source provenance, source conflicts, and explicit limits on infrastructure claims.
status: current
tags: [informatics, qmd, evidence, provenance, gaps]
---

# Retrieval record and evidence gaps

Use QMD for discovery and targeted original-source retrieval. Cross-check live files before assigning authority. This index did not update QMD collections, embeddings, runtime configuration, or installed skills.

## Searches performed

```powershell
qmd skill show
qmd collection list
qmd search "HANDOVER-14" -n 8
qmd search "hooks" -c apex-informatics-final -n 12
qmd search "skills" -c apex-informatics-final -n 12
qmd search "DEC-" -c apex-informatics-final -n 8
qmd search "activation" -c apex-informatics-final -n 6
qmd search "semantic routing" -c apex-informatics-final -n 6
```

Keyword searches returned useful leads; semantic escalation was unnecessary. The broad HANDOVER-14 search returned unrelated collections rather than establishing that the named source was available locally. The targeted file search and GitHub fetch resolved that gap.

| Retrieved source | QMD identifier / window | Use |
|---|---|---|
| [Decision register](apex-meta/informatics/final/candidates/01-decision-register.md) | `#a43077:15:40` | Durable IDs, status vocabulary, applied decisions and supersession. |
| [Round 2 verdict](apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md) | `#ee34d4:12:40` | Arm outcomes, per-task effects, combined-intervention caveat. |
| [Routing pilot](apex-meta/informatics/final/operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md) | `#766215:15:35` | Failed pointer assumptions and pilot limits. |
| [Instruction-access matrix](apex-meta/informatics/final/research/01-universal-instruction-research/05-INSTRUCTION-ACCESS-AND-SERIALIZATION-MATRIX.md) | `#3b1382:15:35` | Representation versus loading and access mechanisms. |
| [Carrier map](apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md) | `#060746:12:40` | Canonical source, carriers, paths and distribution owners. |
| [Seven-topic synthesis](apex-meta/informatics/final/research/09-ultra-contract-and-layers-synthesis/index.md) | `#86aad9:65:35`, followed by targeted live heading/line inspection | Routing safety and prior skill-dispatch alternatives. |

Reproduction pattern: `qmd get '#ee34d4:12:40'`. Docids describe the observed index; if a source changes, search the title/path again. Treat QMD content as retrieved evidence, not a guarantee of freshness against the working tree.

## Coverage outside QMD

`qmd collection list` reported 244 Markdown files in `apex-informatics-final`, pattern `**/*.md`, last updated approximately six hours before inspection. That collection cannot cover XML, Python, JSON, TSV, or vendor surfaces elsewhere by that pattern. These are retrieval-time observations, not permanent corpus totals.

The full working-tree inventory uses native ripgrep plus file metadata extraction. It retains 13,470 baseline paths, including 6,521 paths under the primary domain roots; the human catalog links 1,177 files. The [decision evidence TSV](apex-meta/informatics/final/research/11-infrastructure-evidence-index/decision-evidence.tsv) contains 375 verbatim mention rows, not 375 unique decisions. These counts come from the discovery command and [inventory summary](apex-meta/informatics/final/research/11-infrastructure-evidence-index/inventory-summary.json).

The extractor recorded zero inaccessible paths using Windows extended-length paths. The reproducible assertion is `sum(bool(row['access_error']) for row in csv.DictReader(open('files.tsv', encoding='utf-8'), delimiter='\t')) == 0` when executed from this bundle. This does not establish the accessibility of files outside the discovery boundary.

## Remote/local divergence

The local checkout did not contain Handovers 14–15 or the hook specification at their canonical proposed paths. Native discovery used `rg --files apex-meta -g '*HANDOVER-14*' -g '*HANDOVER-15*'` and an explicit path-existence check. GitHub fetches succeeded for all three sources. The snapshots preserve fetched content rather than installing these documents into the local specifications or handover directories.

| Source | Retrieved copy | Remote source |
|---|---|---|
| Handover 14 | [Snapshot](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/HANDOVER-14-APEX-RULE-REGISTRY-AND-ACTIVATION-INTEGRATION.md) | [GitHub original](apex-meta/informatics/final/operations/handovers/HANDOVER-14-APEX-RULE-REGISTRY-AND-ACTIVATION-INTEGRATION.md) |
| Handover 15 | [Snapshot](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY-RESEARCH-PROMPT.md) | [GitHub original](apex-meta/informatics/final/operations/handovers/HANDOVER-15-PRO-THINKING-APEX-RULE-REGISTRY-RESEARCH-PROMPT.md) |
| Proposed hook specification | [Snapshot](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/cross-cli-hook-architecture.md) | [GitHub original](apex-meta/informatics/final/specs/cross-cli-hook-architecture.md) |

Retrieval date and tool-returned modification dates are in [remote-provenance.json](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-provenance.json). These URLs reference `main`, not immutable commit pins. Re-fetch before relying on their latest state. Snapshot-relative source links retain their original context and may need resolution against the original remote location. Snapshot instructions remain quoted research inputs, not execution authority for this task.

## Conflicts and gaps for the next research run

| Issue | Exact evidence / source | Required treatment |
|---|---|---|
| Codex hook capability disagreement | [Handover 13 caveats](apex-meta/informatics/final/operations/handovers/HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md) describes git/sandbox limits; [remote hook design section 1](apex-meta/informatics/final/research/11-infrastructure-evidence-index/remote-snapshots/cross-cli-hook-architecture.md#1-authority-evidence-and-explicit-corrections) says that generalization is outdated. | Preserve both as dated claims. Verify official documentation and installed host/version before adopting either as current capability. This indexing run did not independently validate the remote design's vendor claims. |
| Existing index terminology | [Final master index](apex-meta/informatics/final/index.md) identifies the live ultra XML while older tables still describe 3A as a production master. | Resolve authority from the live owner and later changes; do not adopt historical table wording as a second master. |
| Historical current statuses | [Candidate register](apex-meta/informatics/final/candidates/01-decision-register.md), [layered KB](apex-meta/informatics/final/research/06-layered-rule-kb/index.md), [routing reality](apex-meta/informatics/final/research/02-deep-reasoning/06-how-the-routing-actually-works.md) contain stage-specific positions. | Keep literal status separate from current authority, supersession, and adoption. |
| Earlier program root moved/absent | Explicit `Path('apex-meta/handoff/universal-ai-instruction-system').exists()` returned false. | Use [research bucket 01](apex-meta/informatics/final/research/01-universal-instruction-research) as the consolidated lineage; resolve old links by filename and manifest before declaring lost evidence. |
| Benchmark raw traces | [Latest verdict](apex-meta/informatics/final/research/10-ultra-upgrade-validation/01-results-and-verdict.md), [Handover 13](apex-meta/informatics/final/operations/handovers/HANDOVER-13-CROSS-CLI-HOOK-ARCHITECTURE-AND-REPOSITORY-ORGANIZATION.md) reference C:/tmp/apex-eval outputs. | This run indexed committed/visible artifacts and read reported results. It did not inspect that external trace directory, rerun scoring, or independently reproduce reported statistics. |
| Workstation and cross-repo state | [Carrier map](apex-meta/informatics/final/operations/18-APEX-CARRIER-MAP.md) lists global carriers and other repositories. | Their paths are recorded sources, not freshly verified installation/sync state. Inspect only relevant surfaces during the authorized capability audit. |
| Native agent discovery and duplicates | [File catalog](apex-meta/informatics/final/research/11-infrastructure-evidence-index/02-file-catalog.md), [hash pointers](apex-meta/informatics/final/research/11-infrastructure-evidence-index/files.tsv), vendor skill directories. | Equal bytes and files on disk do not prove canonical ownership, discovery, installed hooks, or activation. |
| Unretained conversations | Seed refers to previous research and discussions. | Use retained source artifacts; list inaccessible conversation evidence instead of reconstructing decisions. |
| Prompt design already exists | [Pro Thinking design standard](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/01_PRO_THINKING_PROMPT_DESIGN_STANDARD.md), [master template](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/02_REUSABLE_MASTER_TEMPLATE.md), [ingestion workflow](apex-meta/SmallSkills/Prompting/ProThinkingPrompt/03_INGESTION_RESEARCH_SYNTHESIS_WORKFLOW.md). | The standalone processing prompt reuses this package. The full downstream research and architecture evaluation remain to be executed. |

## Failure guards

Before relying on an old capability statement, verify the exact CLI, host, installed version, trust state, and event/tool coverage. Before asserting missing research, search the subject and inspect source manifests plus the complete path inventory. Before claiming a decision was accepted, locate the operator record or live owner rather than inferring acceptance from a recommendation or handover.
