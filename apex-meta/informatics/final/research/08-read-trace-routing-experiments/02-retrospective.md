---
type: Evidence
id: EVIDENCE-ROUTING-RETROSPECTIVE-v0.1
title: Retrospective on the routing experiments - what went well, what was learned, what to change
description: Definitions, ten practices that worked, eleven learnings with confidence labels and eleven changes from three routing experiments on 2026-11-07. Marked to-do.
status: draft
tags: [retrospective, lessons, read-trace, routing, jit-gates, todo, mindful-bar]
---

# Retrospective on the routing experiments

## Status

- **TO-DO.** Open items are tracked in the to-do register of [01-findings-and-protocol.md](01-findings-and-protocol.md). Nothing here changes a rule, spec or decision.
- Written on 2026-11-07, the day of the three rounds. All counts come from transcripts, patches or the score tables in [artifacts](artifacts/).

## Definitions

| Heading | Meaning | How an entry is written |
|---|---|---|
| Went well | A practice worth keeping because it prevented or caught an error in this work | Practice, then the evidence that it worked |
| Learned | A finding about agent behavior, the harness, the scoring or the design | Finding, confidence label, evidence |
| Change | A concrete change to the method, the tooling or the design, with its reason | Change, reason, where it lands |

Confidence labels: **measured** (counted from traces, patches or score files), **observed** (seen in one run or one session), **hypothesis** (not tested).

## The three rounds

| Round | Agents and method | Result in one line |
|---|---|---|
| R0 | 12 `general-purpose` Haiku agents, plan only, `AGENTS.md` auto-loaded with a blueprint pointer and an added "read the standard first" sentence | The blueprint was opened in 6 of 11 write tasks. None opened the writing profile, file architecture, patch discipline or the domain map. One opened `handover.md`. [read-traces-round0.tsv](artifacts/read-traces-round0.tsv) |
| E1 | 18 `Explore` Haiku agents, 9 tasks, arm A contract only against arm B blueprint pointer, `AGENTS.md` read as a file, output as text | Rubric 40 against 37 of 45. No clear effect at n=1. Agents often followed the contract's gates. |
| S1 | 72 headless sessions, 3 arms, 8 tasks, 3 repetitions, neutral prompts, instructions appended to the system prompt, real writes | Blueprint ignored (1 of 24). Two inline placement sentences gave 12 of 12 correct placement against 6 and 4. Gates mostly not followed. |

## Went well

- **WW-1 Traces from transcripts, not reports.** The agents' self-reported access logs matched their transcripts for every key file in all 18 E1 agents. Evidence: [read-traces.tsv](artifacts/read-traces.tsv).
- **WW-2 Pre-registration with hashes.** Tasks, rubric, outcomes, thresholds and the decision rule were hashed before the full run. Evidence: [PREREG.sha256](artifacts/stage1/PREREG.sha256).
- **WW-3 Defects reported beside the frozen result.** Two scorer defects were found after the run. The original numbers stayed, the corrected scorer was added, and the five changed cells were listed. Evidence: [score_stage1.py](artifacts/stage1/score_stage1.py), [score_stage1_corrected.py](artifacts/stage1/score_stage1_corrected.py), both score tables.
- **WW-4 Assertions in the arm builder.** The builder asserted that every sentence it removes exists. It stopped at once on a line-ending mismatch caused by the global git setting, before any cell ran.
- **WW-5 Smoke run before the full run.** Nine cells checked the harness, the isolation flags and the scorer end to end.
- **WW-6 Isolation checks.** Each cell was a fresh clone. The real repositories were snapshotted before and after both runs and were unchanged. Evidence: [safety](artifacts/stage1/safety/).
- **WW-7 Reproducible archives.** Transcripts and per-cell patches were stored in tar.gz files that rebuild to the same hash. Evidence: [make_archive.py](artifacts/make_archive.py), [archives](artifacts/archives/).
- **WW-8 Contradictions stated, not smoothed.** The disagreement with the earlier pilot ([operations/17](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md)) and a wrong earlier claim by the author (that nobody had tested under-reading) were written into the record.
- **WW-9 Design checked before concluding.** The design already had conditional dispatch. The experiment tested a local addition against it and did not assume the addition was needed.
- **WW-10 A blocked action was not worked around.** Copying raw session transcripts out of `~/.claude` was denied by the harness classifier. Only run outputs and derived tables were archived.

## Learned

- **L-1 measured. A one-sentence router is ignored.** The blueprint pointer led to the blueprint in 1 of 24 cells. Arm B behaved like arm A. Evidence: [scores-corrected.csv](artifacts/stage1/scores-corrected.csv).
- **L-2 measured. A rule stated at the point of instruction works.** Two sentences naming the domain map and filing rules raised correct placement to 12 of 12 (A 6, B 4) and domain-map reads to 14 of 24 cells (A 4, B 1).
- **L-3 measured. Contract gates are mostly not followed under neutral prompts.** `<handover>` 9 of 9, `<authoring>` ref read before writing 1 of 36, `<editing>` 0 of 9, `<trade_off>` 0 of 9. The pilot had 0 of 2 on `<handover>` and `<trade_off>`.
- **L-4 hypothesis. Gate following depends on how the task is posed.** `<handover>` fired when the task text contained the word "handover". The other gates were not named in the task text. This is a reading of the counts, not a tested cause.
- **L-5 observed, confounded. E1 overstated gate following.** E1 differed from S1 in four factors at once: how the instructions were delivered, the agent type, the prompt wording (a sentence asked for standards and a restatement) and whether the agent could write. None of the four is isolated, so no single cause can be named.
- **L-6 observed. Existing governed files transmit the format.** In E1 arm A no agent opened the writing profile, yet the proposed files had labelled blocks and complete frontmatter. They copied sibling files.
- **L-7 measured. Run-to-run variance is large at n=3.** On the interview task arm A scored 3 of 3 and arm B 1 of 3, although the blueprint was never opened and the arms behaved alike.
- **L-8 observed. Harness facts, Claude Code 2.1.310.**
  - The `output_file` of a background subagent was empty. The transcript sits under `~/.claude/projects/<project>/<session>/subagents/agent-<id>.jsonl`, and every tool call is listed twice.
  - Restricted mode ignores the user's global instructions and the project `AGENTS.md`. `--append-system-prompt-file` delivers instruction text. `--setting-sources project,local` still loads the global file.
  - `--allowedTools` did not stop read-only shell commands under the accepted-edits mode. Agents used `cat`, `sed` and `grep` on spec files.
  - The help text lists no turn-limit flag. A budget cap and a timeout bounded each cell.
  - A headless cell took 8 to 471 seconds and cost under 0.1 USD. Stdin must be redirected from `/dev/null`.
- **L-9 measured. Scoring pitfalls.** Counting shell reads and redirects changed 5 cells. A frontmatter rule must follow the repository's own convention for `index.md`. A pooled count must use the pre-registered denominator.
- **L-10 observed. The design had the dispatch already.** Seven `when`/`ref` triggers sit in the contract and a standalone router is vendored, so the blueprint duplicated them. Detail: [03-design-review-routing-carriers.md](03-design-review-routing-carriers.md).
- **L-11 observed. The author showed the failure being measured.** In the Mindful Bar session the author wrote governed files without opening the standard that `AGENTS.md` pointed to. The experiments reproduce that behavior in Haiku.

## Change

| ID | Change | Reason | Lands in |
|---|---|---|---|
| C-1 | Add the two placement sentences to the Mindful Bar `AGENTS.md` and retire the blueprint | L-1, L-2 | Mindful Bar repository, operator decision pending |
| C-2 | Give each judgment gate that failed (`<authoring>`, `<editing>`, `<trade_off>`) one inline imperative, or add a hook that blocks a governed write until the ref was read | L-3 | Stage 2, [operations/17](../../operations/17-READ-TRACE-PILOT-AND-BASE-REF-FRAGILITY-FINDINGS.md) `DEC-O8` and `DEC-O9` |
| C-3 | Change one factor per run: delivery channel, prompt wording, agent type, write permission | L-5 | Stage 2 design |
| C-4 | Commit first and build arms from the commit SHA with the script | Stage 1 arms came from a scratch commit of an uncommitted tree | Harness |
| C-5 | Smoke-test every task type, including gate tasks that use shell commands, and freeze the scorer only after it counts shell reads, redirects and the `index.md` convention | L-9 | Harness |
| C-6 | Remove shell access for tasks that need none, or count shell reads from the start | L-8 | Harness |
| C-7 | Take placement from an allowed-path table written by someone other than the arm author, or from a blind judge | The author wrote arms, tasks and placement rule | Scoring |
| C-8 | Use 5 repetitions and a second model, and fix the denominators once | L-7 | Stage 2 design |
| C-9 | Archive transcripts from the run's own output so no copy out of `~/.claude` is needed, and agree a policy before copying subagent transcripts | WW-10 | Harness and policy |
| C-10 | Validate each task premise in a dry run | Earlier probes asked for a gate number that already existed and an edit whose phrase was absent | Task design |
| C-11 | Keep a running decision log during the run, not only a record afterward | The first record needed correction twice | Process |

## Not archived

- Raw transcripts of R0 and E1 are not in this folder. Their derived traces are: [read-traces-round0.tsv](artifacts/read-traces-round0.tsv) and [read-traces.tsv](artifacts/read-traces.tsv). Raw copies need an operator decision (see C-9).
- The scratch repositories for R0 and E1 were copied from an uncommitted working tree and cannot be rebuilt from a commit. The instruction files that differed are saved as [AGENTS.armA.txt](artifacts/AGENTS.armA.txt) and [AGENTS.armB.txt](artifacts/AGENTS.armB.txt).

## Rule

Cite any figure from these rounds with its round, its n and its confidence label. Do not cite E1 as evidence about gate following under neutral prompts.
