---
title: "Chat Provenance and Workstream Contamination Audit"
created: 2026-07-12
status: evidence_based
evidence:
  - Chat1-multiagentorchestration.md
  - Chat2-multiagentorchestratin.md
  - Chat-weeklyorchestrator.md
  - git_history_and_reachability
---

# Conclusion

There were three distinct conversations with two intended workstreams. The weekly orchestrator did not become the target of its own chat by mistake: Chat Weekly was explicitly assigned that target. The contamination occurred in Chat 2, which was assigned the Fable multi-agent system but adopted the Weekly Orchestrator patch plan and runtime as its implementation base.

The exact takeover is visible in the transcript. Chat 2 says it is beginning “Fable orchestrator: full build to finish,” then immediately says `P01 and P02 are already applied` and works through `P26`, `P27`, and the other weekly patch cards. Those `P01–P30` cards originate in the separate Weekly Orchestrator patch plan created in Chat Weekly. Chat 2 later creates `apex-plan-ops` and `apex-sync-ops`, migrates old-Apex doctrine into weekly surfaces, and starts G1/G2 of the weekly loop.

# Chat-by-chat reconstruction

## Chat 1 — Fable multi-agent orchestration

**Source:** `Chat1-multiagentorchestration.md`

**Assigned target:** the final multi-agent orchestration system under `apex-meta/fable-orchestrator/`, beginning with `00-START-HERE.md`.

**Confirmed work that reached the repository:**

| Transcript evidence | Git evidence | Result |
|---|---|---|
| milestone research, evaluation matrix, design-lock answers, external research pack | `912bd60a`, `2f63faa0`, `d645e335` on `origin/claude/fable-orchestrator-setup-9pc5pu` | Present and recoverable. |
| Fable target remains proposed/operator-gated after initial research | `target-log.md`, `design-lock-answers.md` at `d645e335` | Correctly stopped before implementation. |

**Later claimed work that is not present in this repository:**

Chat 1 reports pushes for `e2983ffd`, `4d1cb7de`, `cfebf46`, and `11316abe`, including `apex-meta/orchestration/`, seven agent definitions, doctrine files, and a live US-IDEA-01 simulation.

Git verification found:

```yaml
claimed_commits:
  e2983ffd: missing
  4d1cb7de: missing
  cfebf46: missing
  11316abe: missing
remote_branch_tip: d645e335
main_history: does_not_contain_claimed_commits
```

Therefore the claimed final Fable implementation was not available to Chat 2 in this clone. The evidence cannot distinguish among an unpushed/different-repository run, a lost worktree, or an inaccurate completion claim; it does establish that the implementation is absent from this repository and branch.

## Chat Weekly — Weekly Orchestrator

**Source:** `Chat-weeklyorchestrator.md`

**Assigned target:** finalize only the execution-ready weekly orchestration flow under `apex-meta/kb/Weekly-Orchestrator/`.

**Explicit exclusions:** `apex-kb`, `apex-sync`, `apex-session`, and `apex-plan` are “not target” and will be connected later.

**Work performed:**

| Phase | Commit / evidence | Scope judgement |
|---|---|---|
| Macro/meso/micro finalization | `26ed183e` | Within weekly target. |
| Weekly test-and-improvement plan | `6890c0c7` | Within weekly target. |
| P01–P30 repair waves | `f60b4e04`, `faf989fa`, `834be98c`, `b68dceef` | Mostly within the weekly target: handoff repair, path repair, formatting, and behavioral tests. |

The weekly system remains structurally present. Its initial eight stage/review agents, weekly skill, shared schema, review wiring, glossary, and architecture files were not deleted or replaced.

## Chat 2 — Fable chat that crossed into Weekly Orchestrator

**Source:** `Chat2-multiagentorchestratin.md`

**Assigned target:** the user again says “finalized the orchestration system,” tells the agent to reread `apex-meta/fable-orchestrator`, requires old-Apex doctrine placement, Plan/Sync integration, and testing against the Claude orchestration-design KB.

**First contamination point:**

```text
Chat 2 line 34: “Fable orchestrator: full build to finish”
Chat 2 line 40: “P01 and P02 are already applied ... check the 8 agent files (P03–P10).”
```

`P01–P30` are not Fable build milestones. They are the Weekly Orchestrator patch cards from `apex-meta/kb/Weekly-Orchestrator/architecture/04-improvement-patch-plan.md`, created in Chat Weekly.

**Direct evidence of shared-worktree interference:**

```text
Chat 2 line 66: “~20 files show as modified that I never touched.”
Chat 2 line 78: “The concurrent session touched handoff-schema again.”
```

This is the strongest evidence of the mechanism: concurrent chats were operating against the same working tree and shared files. Chat 2 did not have an isolated Fable branch/worktree, so it treated the newest available weekly artifacts as its executable implementation surface.

**Subsequent out-of-scope additions by Chat 2:**

| Chat 2 action | Git commit | Why it crossed the weekly boundary |
|---|---|---|
| Adds `apex-plan-ops` and `apex-sync-ops` to weekly routing | `3a5acb98` | Chat Weekly explicitly excluded Plan/Sync/Session from its target. |
| Migrates nine old-Apex role doctrines into weekly and other skill surfaces | `66970259` | Broader Fable-system work was added to the weekly runtime/control plane. |
| Runs G1 and starts G2 weekly planning | `ce8d4f0b` | Executes the weekly system rather than building the missing Fable architecture. |

# Why the switch was possible

```text
Chat 1’s claimed Fable implementation was absent from main and its cited remote branch
  + Chat Weekly’s finalized system was present on main and installed as .claude/CLAUDE.md authority
  + Chat 2 shared the same working tree with another session
  + Chat 2 reused the Weekly patch-card vocabulary (P01–P30)
  = Chat 2 adopted Weekly Orchestrator as the concrete implementation surface for the Fable request
```

The root `.claude/CLAUDE.md` amplified this error because it presents the weekly loop as the active Apex system and does not state that it is separate from the Fable build.

# Damage assessment

## Weekly Orchestrator

**Not useless and not erased.** The initial weekly finalization and its core contracts remain. The later changes are additive:

- weekly patch-wave repairs: largely beneficial and within the original weekly quality/test request;
- Plan/Sync integration: an out-of-scope expansion, but bounded by proposal/dry-run restrictions;
- old-Apex doctrine migration: an out-of-scope expansion that adds references and context load, not a replacement of weekly logic;
- generated G1/G2 artifacts: new runtime artifacts, not architectural rewrites.

The weekly system is therefore recoverable without reconstructing it from scratch. The clean architectural baseline is `26ed183e`; the tested weekly-quality baseline is `b68dceef`; the first explicit non-weekly scope expansion is `3a5acb98`.

## Fable multi-agent system

**Not completed in this repository.** The confirmed Fable work stops at research/design material (`d645e335`). The later claimed final implementation from Chat 1 is absent. Chat 2 did not recreate that implementation; it continued the weekly system instead.

## Fable completion-status contamination

`cd050000` later rewrote Fable status documents to call the weekly-loop verification Fable closure. That is a documentation/classification error, not a modification of the weekly core.

# Audit conclusion

The switch is understood with high confidence. It was caused by a missing Fable implementation at the branch Chat 2 actually used, a repository-wide weekly runtime instruction surface, and concurrent shared-worktree edits. The evidence does not support the claim that the original weekly agent failed or that its work was destroyed. It supports the narrower and more serious claim that Chat 2 took over the weekly implementation surface instead of rebuilding the missing Fable system.

# Remaining evidence gap

The only unresolved forensic question is why Chat 1’s reported commits (`e2983ffd`, `4d1cb7de`, `cfebf46`, `11316abe`) are absent. Resolving that requires access to the original Chat 1 worktree/repository, its Git remote activity, or a copy of its terminal/push output beyond the transcript. No further local audit can distinguish those causes.
