---
okf_version: "0.2"
type: Index
id: V2-READ-TRACE-ROUTING-EXPERIMENTS-INDEX
title: Read-trace routing experiments on the Mindful Bar repository
description: Index of three agent experiments on 2026-11-07 that tested whether a project routing blueprint, the contract triggers or inline placement sentences make agents open the right files. Findings, retrospective, design review and artifacts. Marked to-do.
status: draft
tags: [index, read-trace, routing, jit-gates, experiments, todo, mindful-bar]
---

# Read-trace routing experiments

## Status

- **TO-DO.** Open work is in the to-do register of [01-findings-and-protocol.md](01-findings-and-protocol.md). Nothing here changes a rule, spec or decision.
- Everything in this folder was created on 2026-11-07 and moved here without altering bytes. The move is recorded in [MOVE-MANIFEST.tsv](MOVE-MANIFEST.tsv).

## Summary

- A one-sentence pointer to a router file was ignored (opened in 1 of 24 cells).
- Two sentences inside `AGENTS.md` naming the domain map and the filing rules gave correct file placement in 12 of 12 cells, against 6 and 4 of 12.
- Contract gates were mostly not followed under neutral prompts, except `<handover>` (9 of 9).

## Files

| File | Purpose |
|---|---|
| [01-findings-and-protocol.md](01-findings-and-protocol.md) | Method, results of experiment 1 and stage 1, deviations, limits, protocol v2, to-do register |
| [02-retrospective.md](02-retrospective.md) | Definitions, what went well, what was learned, what to change |
| [03-design-review-routing-carriers.md](03-design-review-routing-carriers.md) | Where routing lives in the design and what the blueprint added |
| [MOVE-MANIFEST.tsv](MOVE-MANIFEST.tsv) | Old path, new path and hashes for each moved file, and the one post-move edit |

## Artifacts

| Path | Content |
|---|---|
| [artifacts/authoring-blueprint.mindful-bar.HEAD.txt](artifacts/authoring-blueprint.mindful-bar.HEAD.txt) | The tested blueprint, copied byte for byte from git `HEAD` |
| [artifacts/AGENTS.armA.txt](artifacts/AGENTS.armA.txt), [artifacts/AGENTS.armB.txt](artifacts/AGENTS.armB.txt) | Instruction files of experiment 1 |
| [artifacts/rubric-preregistered.txt](artifacts/rubric-preregistered.txt) | Rubric written before experiment 1 ran |
| [artifacts/read-traces-round0.tsv](artifacts/read-traces-round0.tsv), [artifacts/read-traces.tsv](artifacts/read-traces.tsv) | Tool-call traces of round 0 (12 agents) and experiment 1 (18 agents) |
| [artifacts/stage1/](artifacts/stage1/) | Stage 1 harness, pre-registration with hashes, tasks, arm instruction files, score tables, progress log and safety snapshots |
| [artifacts/archives/](artifacts/archives/) | Stage 1 transcripts and per-cell patches as byte-reproducible tar.gz files |
| [artifacts/SHA256SUMS](artifacts/SHA256SUMS) | Hash of every artifact file |

## Reproduce

1. Verify hashes: `cd artifacts && sha256sum -c SHA256SUMS`.
2. Rebuild an archive and compare its hash: `python make_archive.py out.tar.gz <files>`.
3. Re-score stage 1 from the extracted transcripts and patches with `stage1/score_stage1_corrected.py`. It needs the arm repositories, which `stage1/make_arms.py` rebuilds from a Mindful Bar working tree.

## Rule

Cite a figure from this folder with its round, its n and its confidence label from [02-retrospective.md](02-retrospective.md).
