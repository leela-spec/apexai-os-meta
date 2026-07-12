---
title: "Meta Ops ⇄ apex-plan / apex-sync / apex-session Integration Contract"
purpose: >
  The binding contract for how the Meta Ops accountability invokes the three-package
  mutation backbone: exact triggers, exact commands, dry-run rules, and how each
  skill's inputs/outputs map onto the shared handoff-packet schema. This is the Q2
  "layering" made operational — the skills are Meta Ops support capabilities,
  not peer systems.
created: 2026-07-11
source: >
  .claude/skills/apex-plan|apex-sync|apex-session/SKILL.md; scripts/apex_sync.py --help;
  apex-meta/orchestration/user-stories/user-stories.md §3 meta_ops_support_capabilities.
---

# Meta Ops ⇄ Three-Package Integration Contract

## Routing rule (which skill, when)

| Operator/run intent | Skill | Never route here |
|---|---|---|
| Capture a project, decompose work, propose dependencies/priorities, draft focus recommendation | **apex-plan** | ranking, score computation, status mutation |
| Compute next actions, blockers, stale tasks, registry rebuild/preview, drift check, dependency validation, scores | **apex-sync** | semantic choices, new decomposition, status mutation |
| Record session state, validate status changes, produce H6 handoff, extract state deltas, prepare next-session context, apply confirmed mutations | **apex-session** | ranking, blocker scan, decomposition |

A request spanning two boundaries is split into two packets — never handled by one skill leaking into the other's scope.

## Loop-phase binding (orchestrator-run.md)

| Phase | Skill | Exact mechanism | Packet result |
|---|---|---|---|
| 3. Meso skeleton | apex-plan | Skill invocation with operator notes/goals; produces `apex_plan_packet` | `lifecycle_stage: proposal`, `authority.state: candidate` |
| 4. Deterministic checks | apex-sync | `python3 scripts/apex_sync.py <next|blockers|drift|stall|score> --root . --json` (dry-run defaults true) | `lifecycle_stage: computed`; reproduction command recorded in `sources_evidence` |
| 4b. Registry rebuild | apex-sync | **two-step, always**: (1) `registry --json` preview + `drift --json` report → operator sees delta; (2) only after gate: `registry --dry-run false` | write step requires `operator_validation: confirmed` in the covering packet |
| 9. Confirmed mutation | apex-session | Skill invocation: status mutation records with `before_after_preview`, H1 enum validation, `operator_validation` recorded | `lifecycle_stage: confirmed` — the ONLY producer of confirmed |
| 10. Close | apex-session | H6 handoff artifact + state delta + next-session context | `confirmed` H6 under `apex-meta/handoff/` |

## Hard rules (violating any = invalid run)

1. **Dry-run first, always.** The only write flag in the entire script surface is `registry --dry-run false`; it is never the first command of a registry interaction — preview + drift report precede it.
2. **No implicit apply.** apex-session mutation records with `operator_validation` ∈ {`not_requested`, `needs_revision`, `rejected`} stay visible-but-unconfirmed; Meta Ops never "helps" them along.
3. **Authority closure before confirm.** Before presenting a canon-changing mutation at the gate, Meta Ops checks every authoritative input: `authority.state: verified`, `basis_digest` current (schemas/authority-state.schema.md). Procedural until the digest check lands in code (ARCHITECTURE.md §7.1).
4. **Computed ≠ decided.** apex-sync output ranks and flags; Meta Ops (or the operator) decides. A sync report is never quoted as an authorization.
5. **One surface.** Durable task/session state is written by apex-session records and `registry --dry-run false` — never by Meta Ops editing registry/epic status fields directly. (Creating new epic/task files from an operator-approved plan is apex-plan's documented handoff, executed by Meta Ops as file creation, `status` per H1 enum, then registry rebuilt via the two-step.)

## Failure handling

- Script non-zero exit or malformed JSON → `hold` packet with the raw stderr in `sources_evidence`; no retry-with-tweaks loop past 2 attempts — escalate to operator.
- Drift report showing unexpected delta → stop; drift is a finding for the operator, not something Meta Ops reconciles silently.
- Skill boundary conflict (a request that seems to need two skills at once) → split packets; if genuinely inseparable, escalate.
