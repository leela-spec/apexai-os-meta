---
type: Evidence
id: EVIDENCE-ROUTING-EXPERIMENT-MINDFUL-BAR-v0.1
title: Read-trace routing experiment on the Mindful Bar repository - contract triggers alone against a project routing blueprint
description: Eighteen Haiku agents on nine Mindful Bar tasks in two arms, measured by transcript read traces. No clear effect of the blueprint at n=1 per cell, a conflict with the earlier pilot, and an improved protocol. Marked to-do.
status: draft
tags: [evidence, read-trace, routing, jit-gates, todo, mindful-bar, pre-registered, protocol-v2]
---

# Read-trace routing experiment, Mindful Bar, 2026-11-07

## Status

- **TO-DO.** This is a research record with open work. It is not a conclusion. The to-do register is below.
- It extends the pilot in [operations/17](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md). It does not replace it, and it does not change `DEC-O7` to `DEC-O10`.
- n=1 per cell in the first experiment and n=3 per cell in stage 1. Treat every difference as a lead, not a rate.
- Companion files: [02-retrospective.md](02-retrospective.md) (what went well, learned, to change) and [03-design-review-routing-carriers.md](03-design-review-routing-carriers.md). Folder index: [index.md](index.md).

## Summary

- **Question:** does a project-level routing file (the "authoring blueprint") make agents open the right specs, compared with the contract's own `when=`/`ref=` triggers alone?
- **Answer so far:** no clear effect. Arm A (contract only) scored 40 of 45 pre-registered rubric points. Arm B (blueprint pointer) scored 37 of 45. Both arms opened at least one governed spec in 6 of 9 tasks.
- **What the blueprint alone changed:** it was the only route to the project's domain map (`design/02`), and agents reached that map in 3 of 9 tasks in arm B and 2 of 9 in arm A, mostly by searching.
- **Conflict with the pilot:** `operations/17` found `<handover>` and `<trade_off>` followed 0 of 2 times each. This experiment found `<handover>` followed in both arms and `<trade_off>` in arm A only. The method differences below may explain it.
- **Correction:** an earlier statement in the Mindful Bar session that nobody had tested under-reading of gated modules was wrong. `operations/17` tested it. The research summary [RESULTS-01](../03-research-of-file-10/Apex_Informatics_Research_Results_2026-10-21/RESULTS-01-gating-efficacy.md) says only that no public study exists.
- **Stage 1 (72 headless runs, same day):** the blueprint pointer was ignored (opened in 1 of 24 cells). Two placement sentences inside `AGENTS.md` raised correct file placement from 6 of 12 (arm A) and 4 of 12 (arm B) to 12 of 12 (arm C). Contract gates were mostly not followed under neutral prompts, which contradicts the first experiment. See "Stage 1 results".

## Method

| Item | Setting |
|---|---|
| Repository under test | Mindful Bar, commit `c91f8f3` plus uncommitted working-tree changes. The arms were copied from the dirty working tree, so they are not rebuildable from a commit. |
| Arm A | `AGENTS.md` with the APEX contract triggers only. The blueprint file and every pointer to it were removed. [AGENTS.armA.txt](artifacts/AGENTS.armA.txt) |
| Arm B | `AGENTS.md` as committed, with a one-sentence pointer to the blueprint, and the blueprint file present. [AGENTS.armB.txt](artifacts/AGENTS.armB.txt) |
| Blueprint tested | Copied byte for byte from git `HEAD`, blob `94cf6dc8`. [authoring-blueprint.mindful-bar.HEAD.txt](artifacts/authoring-blueprint.mindful-bar.HEAD.txt) |
| Agents | 18 Claude Code subagents of type `Explore`, model Haiku, one per task and arm. `Explore` agents receive no auto-loaded instructions, so the only instruction surface was the `AGENTS.md` the prompt told them to read. |
| Tasks | 9 repository tasks: brand names, allergen note, interview record, decision record, handover, one-phrase edit, OpenProject task, one-vs-two-flavor trade-off, Notion export ingest. |
| Deliverable | Agents could not write. The deliverable was the full path and content of each file they would write. |
| Scoring | Rubric written and saved before any run: [rubric-preregistered.txt](artifacts/rubric-preregistered.txt). Reads come from transcript tool calls. |
| Trace extraction | [extract_read_traces.py](artifacts/extract_read_traces.py) produced [read-traces.tsv](artifacts/read-traces.tsv). Hashes are in [SHA256SUMS](artifacts/SHA256SUMS). |
| Transcripts | `~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`, 11 MB for the 18 runs. They are not archived. Copying raw session transcripts into a repository was blocked by the auto-mode classifier as a sensitive-source copy, and the block was respected. The extracted traces are in [read-traces.tsv](artifacts/read-traces.tsv). Mapping of agent to arm and task: [agent-map.tsv](artifacts/agent-map.tsv). |

Every agent's self-reported access log matched its transcript on the blueprint, the writing profile, `file-architecture.md`, `design/02`, `patch-discipline.md`, `handover.md`, `bake-off.md` and `qa-decision-matrix.md`, for all 18 agents.

## Results

### Governed files opened, from transcripts

| Task | Arm A opened | Arm B opened |
|---|---|---|
| T1 brand names | file-architecture, patch-discipline | blueprint, writing-profile, file-architecture, design/02, design/03, patch-discipline |
| T2 allergen note | file-architecture, design/02, design/03 | blueprint, writing-profile, file-architecture, design/02 |
| T3 interview | file-architecture, design/02, design/03 | blueprint, file-architecture, design/02 |
| T4 decision record | none | blueprint |
| T5 handover | handover, bake-off | blueprint, file-architecture, handover |
| T6 one-phrase edit | none | none |
| T7 OpenProject task | none | blueprint |
| T8 trade-off | bake-off, qa-decision-matrix | none |
| T9 ingest | file-architecture | blueprint, file-architecture, patch-discipline |

### Gate followed, by contract trigger

| Trigger and target | Tasks where it should fire | Arm A followed | Arm B followed | Pilot `operations/17` |
|---|---|---|---|---|
| `<authoring>` to `file-architecture.md` | 6 (create a governed file) | 4 | 5 | not tested |
| `<editing>` to `patch-discipline.md` | 7 (change an existing file) | 1 | 2 | not tested |
| `<handover>` to `handover.md` | 1 | 1 | 1 | 0 of 2 |
| `<trade_off>` to `bake-off.md` or `qa-decision-matrix.md` | 1 | 1 | 0 | 0 of 2 |

### Rubric score, 5 points per task, scorer not blind to arm

| Task | A | B | Difference that decided it |
|---|---|---|---|
| T1 | 4 | 5 | A filed under `brand-and-sales/naming/`, a folder the design lacks. B found `identity/` through `design/02`. |
| T2 | 5 | 4 | B wrote a normative MUST and cited an EU regulation from memory, flagged unverified. |
| T3 | 5 | 5 | None. |
| T4 | 4 | 5 | A changed "three flavors" to "two flavors" in the validation plan although the decision concerned recipe variants. |
| T5 | 5 | 3 | B typed the file `Plan`, not `Handover`, and listed sources as plain paths. |
| T6 | 4 | 4 | Neither opened `patch-discipline.md`. Both edits were exact. |
| T7 | 3 | 3 | Neither opened the OpenProject skill. |
| T8 | 5 | 3 | B opened no module and gave no I/E/R estimates for its own options. |
| T9 | 5 | 5 | None. |
| Total | 40 | 37 | Within noise at n=1. |

## Findings

- **Contract triggers work on rich in-repo tasks.** Arm A reached `handover.md` and the trade-off modules from the tag alone.
- **The blueprint adds one thing the contract cannot carry.** It leads to the project's domain map. The map was also reached by search when the task text matched, as in T2 and T3.
- **The blueprint can become a stopping point.** Of 7 arm-B tasks that opened it, 5 went on to a spec file. In T4 and T7 it ended the reading.
- **Existing governed files teach the format by imitation.** No arm A agent opened the writing profile, yet their files carry labelled blocks and complete frontmatter. They copied sibling files written to the standard.
- **Pure edits skip the editing module in both arms.** `patch-discipline.md` was opened in 1 of 7 edit tasks in arm A and 2 of 7 in arm B. The edits were still exact because the tasks were small.

## Why this may disagree with the pilot

| Hypothesis | Mechanism | How to test |
|---|---|---|
| H1 delivery | Here the prompt told agents to read `AGENTS.md` as a file and follow it. In the pilot the contract was auto-loaded into context. An explicit read may raise attention to the tags. | Run the same gate tasks with the contract auto-loaded and with an explicit read instruction. |
| H2 task richness | Here agents explored the repository through README and index links, averaging 6 to 20 tool calls. Pilot agents made 2 calls. Exploration exposes the specs. | Compare gate-follow rate against the number of repository files read before the first write. |
| H3 prompt wording | The prompt said "Hold the deliverable to the repository's own standards". That sentence nudges an agent to look for standards. | Remove the sentence. Give neutral task text only. |
| H4 agent type | `Explore` agents carry a search-oriented system prompt and cannot write. The pilot used `general-purpose` agents that wrote files. | Run headless cells with real writes. |

## Limits

- n=1 per cell, one model, one repository, one scorer who knew the arm.
- The prompt told every agent to write down the align restatement, so the `<align>` trigger is untested.
- Arms were built from an uncommitted tree. The G8 gate already existed when the first probe round asked for it, which shows that task premises were not validated before running.
- Agents could not write, so the read-before-write ordering was not measured.

## Improved test design

Protocol v2 changes the cell, the tasks, the scoring and the arms. Options for the next step:

| Option | Mechanism | Grounding | Raw (I/E/R) |
|---|---|---|---|
| 1 Replicate as run | Same Explore agents, 3 repetitions per cell | Cheapest way to see variance. Keeps H3 and H4 confounds. | I40/E55/R20 |
| 2 Headless cells with real writes (stage 1) | Each cell is one `claude -p --model haiku --permission-mode acceptEdits --output-format stream-json` run with the arm copy as working directory. The arm `AGENTS.md` loads naturally. Arms A, B and C, 8 tasks, 3 repetitions, 72 runs. | The CLI exists on this machine (version 2.1.310). It removes H1, H3 and H4 and measures read-before-write. Measured subagent cost was 48k to 127k tokens per run; headless cost is not measured. | I85/E70/R35 |
| 3 Full protocol 04 matrix | 10 arms, 16 tasks, full n | Publication-grade rates. `operations/17` estimated 18 to 30 execution hours. | I90/E75/R55 |

**Recommendation:** option 2 for stage 1. It fixes the confounds this record found at modest cost.
**Rejected:** option 1 repeats the confounds. Option 3 costs far more before the cheaper design has shown which question matters.

### Protocol v2 rules

1. **Build arms from a commit.** Use `git archive <sha>` and a patch script per arm. Record the SHA.
2. **Neutral task text.** Identical across arms. No restate instruction, no "read AGENTS.md first", no "hold to standards". Validate each task premise in a dry run.
3. **Arms.** A contract only. B blueprint pointer. C a placement table of at most six lines inside `AGENTS.md` Layer 2, naming `design/02` and the filing rules. Stage 2 adds D, which is C plus a `PreToolUse` hook that blocks a write to a governed path until the matching spec was read ([DEC-O8](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md)).
4. **Tasks.** One per contract trigger (align, editing, authoring, trade_off, handover, iterative, schemas), three placement tasks that need the domain map, and two no-gate controls for bloat.
5. **Primary metric.** Gate ref opened before the first Write or Edit, from transcript order. Also gate precision, recall and bloat as defined in [protocol 04](../../candidates/04-empirical-test-protocol.md). Record whether each opened path came from a Grep result, a link in a read file, or the agent's own guess.
6. **Deterministic scoring first.** Placement against an allowed-path set per task, `okf_validator.py` error delta against the baseline, link resolution, hash equality for copies, and a `git diff` check that exactly the intended lines changed. A blind judge scores only what code cannot, with arm labels removed and the order randomized.
7. **Replication and reporting.** 3 repetitions per cell, two models (Haiku and Sonnet). Report counts with Wilson 95 percent intervals. Do not report p-values at n=3.
8. **Delivery factor.** Run the handover and trade-off tasks with the contract auto-loaded and with an explicit read instruction, to test H1 against the 0 of 2 pilot result.
9. **Pre-register.** Freeze tasks, rubric, thresholds and analysis before the run. Hash and commit them. Archive the raw stream-json transcripts with SHA-256, because the `~/.claude` paths are not durable.
10. **Provisional adoption thresholds, unmeasured.** Keep an arm only if placement-correct is at least 7 of 9 on placement tasks, gate refs are read before the first write in at least 80 percent of gate tasks, and bloat is at most 20 percent.

## Stage 1 results (protocol v2, 2026-11-07)

Stage 1 ran 72 headless Claude Code sessions: 3 arms, 8 tasks, 3 repetitions, Haiku. Tasks, rubric, outcomes, thresholds and decision rule were frozen by hash before the first cell ran ([stage1-preregistration.txt](artifacts/stage1/stage1-preregistration.txt), [PREREG.sha256](artifacts/stage1/PREREG.sha256)). All 72 cells finished without a timeout or budget abort. The real repositories were unchanged before and after. Total cost was 1.03 USD.

| Arm | Instruction surface |
|---|---|
| A | Contract triggers only |
| B | Contract plus a one-sentence pointer to the authoring blueprint, blueprint present |
| C | Contract plus two sentences naming the domain map `design/02` and the filing rules `design/03` |

### Outcomes (corrected scorer)

| Outcome | A | B | C |
|---|---|---|---|
| Gate ref read before the first write (21 cells) | 3 | 4 | 3 |
| Correct placement on T1, T2, T3, T7 (12 cells) | 6 | 4 | 12 |
| Deterministic check passed (24 cells) | 15 | 11 | 19 |
| Governed specs opened in the lookup control (3 cells) | 0 | 0 | 0 |
| Cells that opened `design/02` (24 cells) | 4 | 1 | 14 |
| Cells that touched the blueprint | not present | 1 | not present |

Placement with Wilson 95 percent intervals: A 6 of 12 (0.25 to 0.75), B 4 of 12 (0.14 to 0.61), C 12 of 12 (0.76 to 1.00). The frozen scorer gave 1, 3 and 3 gate reads and 15, 11 and 17 passed checks.

| Gate | Cells per arm | A | B | C | Pilot `operations/17` |
|---|---|---|---|---|---|
| `<handover>` to `handover.md` (T4) | 3 | 3 | 3 | 3 | 0 of 2 |
| `<authoring>` to `file-architecture.md` before writing (T1 T2 T3 T7) | 12 | 0 | 1 | 0 | not tested |
| `<editing>` to `patch-discipline.md` (T6) | 3 | 0 | 0 | 0 | not tested |
| `<trade_off>` to `bake-off.md` or the matrix (T5) | 3 | 0 | 0 | 0 | 0 of 2 |

### Where the arms differed

- **T1 brand names.** A and B filed under `brand-and-sales/naming/` or `positioning/`. C filed under `brand-and-sales/identity/` in 3 of 3.
- **T2 allergen note.** A and B edited existing files (decisions register, validation plan). C created `compliance/obligations-register.md` in 3 of 3. Two C cells first failed the frozen check only because an `index.md` carried no frontmatter, which is this repository's convention.
- **T3 interview.** A 3 of 3 correct, B 1 of 3, C 3 of 3. A and B behave alike here, so the gap shows run-to-run variance at n=3.
- **T5 trade-off.** C passed the check (at least two I/E/R tags and a recommendation) in 2 of 3 cells without opening a module. A and B passed in 0 of 3.

### Findings

1. **A one-sentence router is ignored.** The blueprint pointer led to the blueprint in 1 of 24 cells. Arm B behaved like arm A.
2. **Stating the placement rule inline works.** Two sentences in `AGENTS.md` took placement to 12 of 12 and made 14 of 24 cells open the domain map.
3. **Contract gates are mostly not followed under neutral prompts.** `<handover>` was followed 9 of 9. `<authoring>` 1 of 36, `<editing>` 0 of 9 and `<trade_off>` 0 of 9. This matches the pilot on `<trade_off>` and contradicts it on `<handover>`.
4. **The first experiment overstated gate following.** There, agents read `AGENTS.md` as a file under a prompt that said to hold the output to the repository's standards. Gate following there was far higher. This supports hypotheses H1 and H3.
5. **Thresholds.** No arm reached 17 of 21 gate reads. Only C reached 10 of 12 placement. All arms met the lookup-control threshold. The blueprint did not exceed both other arms, so the pre-registered rule gives "no demonstrated advantage" for B.

### Deviations and scorer defects, reported as agreed in the pre-registration

- The scorer's printed placement figure pools 15 cells because it also scored T4. The pre-registered figure uses 12 cells and is the one shown above.
- The frozen scorer counted spec reads only through the `Read` tool. Agents also read files with `cat`, `sed` and `grep` through Bash. The corrected scorer ([score_stage1_corrected.py](artifacts/stage1/score_stage1_corrected.py)) counts those, and also counts shell redirects as writes.
- The frozen scorer required frontmatter on `index.md` files. The corrected scorer exempts them.
- Five cells changed: gate reads for A T4 (two cells) and B T3 (one cell), and passed checks for C T2 (two cells). No placement result changed.
- Bash was not limited to `cp`, `sha256sum` and `cmp` as planned. Read-only commands ran under the accepted-edits mode. All 72 cells used identical settings.

### Limits

- One model, three repetitions, one repository. Arm instructions arrived through the system prompt, not as a project file.
- Tasks and the placement rule were written by the same author as the arms. Placement was judged against the domain design, not against an independent reader.
- Raw stage 1 transcripts are in [stage1-runs.tar.gz](artifacts/archives/stage1-runs.tar.gz) and the file changes each cell made are in [stage1-cell-patches.tar.gz](artifacts/archives/stage1-cell-patches.tar.gz). Both rebuild to the same hash with `make_archive.py`. Hashes are in [SHA256SUMS](artifacts/SHA256SUMS).

## To-do register

| ID | Item | Owner | Depends on |
|---|---|---|---|
| TD-1 | Operator reads this record and decides whether it changes the lean on `DEC-O8` or `DEC-O9` | not assigned | none |
| TD-2 | Stage 1 of protocol v2 ran on 2026-11-07 (72 cells, results above). Done. Stage 2 below is not run | not assigned | none |
| TD-7 | Stage 2: add arm D (placement sentences plus one inline sentence for each gate that failed, and a hook arm), 5 repetitions, a second model, and the auto-load against explicit-read factor | not assigned | operator decision on cost |
| TD-3 | Test hypothesis H1 (auto-load against explicit read) to explain the 0 of 2 against 1 of 1 gap | not assigned | TD-2 harness |
| TD-4 | Extend the extractor to report read-before-write order and the source of each opened path | not assigned | none |
| TD-5 | Decide whether raw subagent transcripts of round 0 and experiment 1 (7.1 MB and 11 MB) may be copied from `~/.claude` into this repository. The copy was blocked by the auto-mode classifier on 2026-11-07. Stage 1 transcripts are archived from the run's own output | operator | none |
| TD-6 | Mindful Bar side: decide the blueprint file's fate after stage 1 | Mindful Bar operator | TD-2 |

## Rule

Cite the 40 against 37 score only with the words "n=1, scorer not blind". Do not cite it as evidence that either arm is better until stage 1 has run.
