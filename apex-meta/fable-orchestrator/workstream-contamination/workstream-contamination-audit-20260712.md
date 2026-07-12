---
title: "Workstream Contamination Audit — Fable orchestration vs Weekly Orchestrator"
purpose: "Determine why an independently developed weekly orchestration system was treated as the final fable multi-agent orchestration deliverable."
created: 2026-07-12
status: evidence_based
scope:
  primary_workstream: apex-meta/fable-orchestrator/
  secondary_workstream: apex-meta/kb/Weekly-Orchestrator/ plus .claude/ weekly-loop surfaces
---

# Executive finding

The attached original weekly-orchestrator task establishes an important correction: the initial weekly chat was explicitly and correctly tasked to finalize the Weekly Orchestrator. It was a separate initiative, not an accidental detour inside the Fable multi-system build. Its stated target was the execution-ready weekly orchestration flow under `apex-meta/kb/Weekly-Orchestrator/`; it also explicitly excluded `apex-kb`, `apex-sync`, `apex-session`, and `apex-plan` from that target.

The contamination occurred later. A subsequent agent treated the completed weekly subsystem as evidence of completion for the broader Fable build, added excluded Plan/Sync capabilities into the weekly control plane, and finally promoted weekly-loop verification into Fable closure status. The repository had two active initiatives in one `main` history, but no durable boundary stating that `Weekly-Orchestrator` was excluded from the Fable build. The repository-wide `.claude/CLAUDE.md` then made the weekly loop the active operating identity, so a later agent could reasonably—but incorrectly—treat the weekly control plane as the implementation of the broader Fable target.

The final promotion from subsystem to target was a scope error. The fable plan's actual target is the merged multi-agent orchestration system and its seven story workflows; the weekly loop is a control-plane workflow that can run that system, not a substitute for it.

# Provenance timeline

| Time | Commit | Workstream evidence | Interpretation |
|---|---|---|---|
| 2026-07-11 16:55 | `21250564` | Consolidated `apex-meta/fable-orchestrator/` milestones, build plan, and stories | Fable workstream exists as a distinct target package. |
| 2026-07-11 16:58 | `665446e3` | Merge says “keep consolidated fable-orchestrator content” | Fable content is merged into `main`, not isolated in a worktree. |
| 2026-07-11 18:57 | `ecb8a5c8` | Updates Fable target log and discovery artifacts | Fable milestone work continues. |
| 2026-07-11 19:03 | `b875de12` | Adds the large Weekly Orchestrator index | Independent weekly work is now adjacent to the Fable workstream on `main`. |
| 2026-07-11 20:13 | `d645e335` | Adds Fable external research answers | Fable research resumes while weekly material remains in the same repository/head lineage. |
| 2026-07-11 20:33 | `c9900103` (weekly branch) | Weekly audit adds a synthetic `US-SEQ-01` lifecycle fixture | The weekly workstream begins consuming a Fable story identifier, creating semantic coupling between the two systems. This branch was not a clean separation of targets. |
| 2026-07-11 21:52 | `26ed183e` | Creates `.claude/agents/*`, `.claude/skills/weekly-orchestrator/`, G1–G5, and Weekly-Orchestrator architecture | The weekly subsystem is finalized as the active orchestration architecture. The commit is based on the Fable research lineage (`d645e335`) but changes the weekly control plane, not the Fable target package. |
| 2026-07-11 22:01–2026-07-12 | `6890c0c7` through `b68dceef` | Applies the requested weekly improvement/test plan | These are weekly-scoped repairs and validation work, consistent with the original weekly task. |
| 2026-07-12 13:02 | `3a5acb98` | Adds `apex-plan-ops` and `apex-sync-ops` to weekly stage routing | Direct scope expansion: the original weekly task explicitly listed Plan/Sync/Session as not targets to be connected later. |
| 2026-07-12 13:11 | `66970259` | Migrates nine old-Apex role doctrines into weekly and unrelated skill surfaces | Further expansion beyond the original weekly task's narrow informatics-design reference. |
| 2026-07-12 13:35 | `cd050000` | Marks Fable closure using a weekly-loop simulation | This is the explicit promotion error: weekly control-plane evidence is reclassified as Fable multi-system completion evidence. |

# Root-cause chain

## 1. No persisted exclusion boundary

The Fable target documents define the merged multi-agent system, the old Apex systems, `apex-plan`/`apex-sync`/`apex-session`, the Claude orchestration KB, and seven user-story workflows. They do not contain a durable rule such as:

```yaml
weekly_orchestrator:
  relationship_to_fable_build: supporting_control_plane
  in_scope_as_final_deliverable: false
```

The exclusion may have existed in the operator's chat instruction, but it was not written into the target package where later agents could reliably recover it.

## 2. Repository-wide active instructions favored the weekly system

The root `.claude/CLAUDE.md` identifies the system as:

```text
Apex: Claude-native orchestration system for Marco.
```

Its core loop is PreCapWeek → PreCapNextDay → execution → FlowRecap → StatusMerge, and it names `WeeklyOrchestrator` as the G1–G5 gate holder. It does not identify `apex-meta/fable-orchestrator/` as the active target or distinguish the weekly loop from the Fable build.

This created a precedence problem: a new agent reading repository-level instructions would see the weekly system as the current runtime authority before reading the Fable target package.

## 3. Shared vocabulary and story identifiers collapsed the boundary

Both workstreams use the same terms:

- Apex
- orchestration
- Meta Ops
- Meta Strategy
- Meta Detective
- workflows
- resilience
- `US-SEQ-01`
- Plan/Sync/Session

The weekly audit's `US-SEQ-01` synthetic lifecycle fixture is especially important. It makes the weekly system appear to have executed one of the Fable acceptance stories, even though the Fable build plan requires one actual simulation record per story and the weekly fixture belongs to the separate weekly package.

## 4. Same-main integration removed the strongest safety signal

The workstreams were not maintained in separate branches or worktrees during the critical build phase. Git history shows a single lineage where Fable research, Weekly Orchestrator indexing, weekly audit work, Fable prompt answers, and weekly architecture finalization were interleaved.

That made unrelated changes look like a continuous implementation sequence. The later agent did not need to make an explicit decision to “change the target”; the target was implicitly inferred from the repository's newest active architecture and root instructions.

## 5. The later weekly scope expansion violated the original weekly task

The original weekly task says that `apex-kb`, `apex-sync`, `apex-session`, and `apex-plan` are not targets and will be connected later. Commit `3a5acb98` nevertheless adds `apex-plan-ops` and `apex-sync-ops` to `weekly-orchestrator` routing and its shared handoff schema.

This is not evidence that the initial weekly finalization was wrong. It is evidence that a later agent expanded the completed weekly system using Fable Q2-B material. The additions are bounded and do not erase the original weekly mechanics, but they are a real target-boundary violation and increase the weekly system's surface area.

## 6. Completion evidence was measured against the wrong acceptance object

The Fable build plan requires story-level simulation records. The weekly architecture measured:

- agent frontmatter
- skill registration
- path resolution
- packet envelopes
- stage behavior
- weekly gates

Those are valid acceptance tests for the weekly control plane. They are not acceptance tests for the seven Fable workflows. The mismatch was hidden by naming the weekly verification “orchestration closure.”

# What was actually influenced by what

| Fable multi-system workstream | Weekly workstream |
|---|---|
| Source comparison and milestone artifacts | Weekly planning/status loop |
| Old Apex v1/v2 doctrine analysis | Weekly agent and skill contracts |
| Claude orchestration KB synthesis | Weekly topology, state, review, and token rules |
| Seven user stories | Mostly not implemented; one ID was reused by weekly fixture |
| Proposed Q1–Q8 answers | Used as evidence in Weekly-Orchestrator architecture |
| Final generalized multi-agent architecture | Not independently materialized |

The influence was therefore asymmetric: Fable research became design input for the completed weekly system, then the weekly system was later treated as the completed Fable implementation. The original weekly agent did not compromise Fable by doing its assigned task; the later consolidation compromised the separation between the two initiatives.

# Audit conclusion

The most probable reason is not that the weekly orchestrator was explicitly selected as the Fable target. The more likely mechanism is:

```text
two chats/workstreams
  → same repository and main branch
  → weekly system becomes repository-level active authority
  → weekly system reuses Fable vocabulary and US-SEQ-01
  → later agent sees newest “final orchestration architecture”
  → subsystem is mistaken for target system
  → weekly closure evidence is promoted into Fable closure status
```

The repository history supports this explanation. It cannot prove the hidden model context of the other chat, but it identifies the exact structural conditions that made the misinterpretation likely and the commit where it became explicit (`cd050000`, preceded by `26ed183e`).

# Required boundary repair

Before continuing the Fable build, the target package needs a durable scope contract that states:

1. `apex-meta/fable-orchestrator/` owns the final multi-agent orchestration system.
2. `apex-meta/kb/Weekly-Orchestrator/` and `.claude/skills/weekly-orchestrator/` are a separate supporting workflow/control-plane initiative.
3. Weekly artifacts cannot satisfy Fable story simulation gates unless explicitly imported as evidence for a named Fable workflow.
4. Shared IDs such as `US-SEQ-01` require a namespace prefix or explicit ownership field.
5. The Fable build is not complete until its own seven story simulations and generalized worker architecture exist.

Until that boundary is recorded, any new agent operating from the repository root remains vulnerable to repeating the same cross-workstream inference.
