---
plan_id: PLAN-2026-09-28-program-closeout
title: Program close-out — remaining work across the ki-basis consolidation + Leela OpenProject pilot
status: not_started            # not_started | in_progress | blocked | done
updated: 2026-09-28
current_task: T01              # the single next task to execute
blocked_by: null
owner: operator + takeover-agent
authority_order: "live runtime + code > accepted decisions/ADRs > this plan. Surface conflicts; never invent a winner."
---

# Program close-out plan

**One-line:** the big work (WSL2-native consolidation) is executed and the OpenProject pilot is functionally proven — but almost none of it is committed to git, several docs are internally stale/contradictory, and a set of pilot + adjacent tasks remain. This plan enumerates every remaining item so another agent can finish it safely.

> Built on verified best practice for AI-executable plans (spec→plan→tasks→implement, EARS acceptance,
> DAG ordering, validation gates, human gates on destructive steps). See [research index](#9-research-index).

## 1. Goal & non-goals
- **Goal:** bring both repos to a committed, internally-consistent, discoverable state and close the remaining pilot/infra/adjacent tasks — with every destructive or irreversible step behind a human gate.
- **Non-goals:** re-running the (already-completed) consolidation migration; re-architecting anything; broad refactors. Guard against overcorrection — edit surgically.

## 2. Current state (update in place; never fork)
- **Consolidation (apexai-os-meta):** runbook Phases 0–9 reported **DONE** by a continuation session (per `03-wsl2-native-stack-consolidation/log.md`): both stacks on the single WSL2-native "Apex" engine against one shared PostgreSQL; Docker Desktop uninstalled; ADR-002 written; v14 duplicate deleted; OneDrive bind eliminated; Hermes re-wired. **Reported, not independently re-verified here** → T11 soak test verifies.
- **OpenProject pilot (Leela):** 17.8 instance live at `:8083`; portable skill built + proven (read+write, census WP #38); v14 retired; keepalive + `.wslconfig` cap in place.
- **The problem:** ~51 uncommitted/untracked paths in apexai-os-meta (incl. **live prod `compose.shared-db.yaml`** and both bundles); Leela `master` unpushed + skill uncommitted; multiple stale doc cross-references; no entry-point pointing agents at current truth; pilot loose ends; an adjacent `04-leela-mastery-openproject-consolidation` workstream with 3 open tasks.
- **Blockers/open questions:** none blocking T01–T07; several later tasks are operator-gated (see `gate:`).

## 3. Immediate next action
> Execute **T01** (commit the consolidation work — live prod config is not in git). Do not skip ahead.
> Stop at every step marked `gate: human-approval` and wait for the operator.

## 4. Context-loading rules (progressive disclosure — link, don't inline)
- Read this file fully first. Then load only the doc a task cites, when you start that task.
- Detailed truth lives in the linked bundles — do **not** duplicate it here:
  consolidation = `../03-wsl2-native-stack-consolidation/` (index, 02-decisions-log **D-01…D-18**, 03-execution-plan, 05-handover, log.md);
  adjacent = `../04-leela-mastery-openproject-consolidation/`;
  pilot = `C:\GitDev\Leela-Cloud-2026\docs\ProjectMM\openproject\**` + the skill `C:\GitDev\Leela-Cloud-2026\.agents\skills\openproject\`.
- ADR-002 (current architecture decision) = `C:\GitDev\apexai-os-meta\ki-basis\docs\DUAL_INSTANCE_ARCHITECTURE.md` §6.
- Do NOT preload completed work or unrelated research.

## 5. Environment & safety facts
- **Two engines? No — one now.** Single WSL2-native "Apex" engine (Ubuntu 26.04). Run `wsl -d Ubuntu -u root -- docker …`; prefix `/mnt/c` commands with `MSYS_NO_PATHCONV=1`; pipe `| tr -d '\0'`.
- **Secrets** (never print/commit): `C:\GitDev\ki-basis-shared\.env`, `C:\GitDev\leela-op178\op.env`, community bot `.env` backup. Backups at `C:\GitDev\leela-op178\backups\community-2026-09-26\`.
- **Destructive/irreversible actions require `gate: human-approval`:** any `git push`, deleting projects/data, `wsl --shutdown`, `docker compose up` on `ki-basis/compose.yaml` (its hermes service drifts from live bind mounts — a naive up can wipe ~4.4 GB bot state, D-16), uninstalls.
- Verify after every write (reread/compare). A partial/unexpected result is a stop.

## 6. Task list (DAG — deps are load-bearing; `[P]` = parallel-safe)

### Bucket 0 — Version-control recovery (URGENT)
**T01 — Commit the consolidation work to git (apexai-os-meta).** `gate: human-approval`
- deps: [] · **why urgent:** live private prod runs on **untracked** `ki-basis/compose.shared-db.yaml`.
- scope: the `03-` and `04-` bundles; `ki-basis/compose.shared-db.yaml`; modified `ki-basis/compose.yaml`, `ki-basis/docker/postgres/init/01-init-databases.sh`, the 3 stale docs + 2 ADR-002 mirrors, `BOT_WIRING_AND_PERSONA_HANDOVER.md`. Decide the `codex/separate-community-stack` branch (merge or delete).
- acceptance: WHEN `git ls-files ki-basis/compose.shared-db.yaml` runs THE SYSTEM SHALL list it; `git status` shows no untracked consolidation paths. Preserve unrelated dirty files.
- rollback: n/a (additive). · status: not_started · evidence: —

**T02 — Update write-policy, then commit + push the skill (Leela).** `gate: human-approval` (push)
- deps: [] · scope: add `project.delete` (Destructive), `wp.attach`, `project.update` to `references/write-policy.md`; commit the 5 modified skill files; **push `master`** (currently ahead 1, unpushed).
- acceptance: write-policy lists every mutating op incl. `project.delete`; `git status -sb` shows not-ahead; skill files clean.
- status: not_started

### Bucket 1 — Doc-truth reconciliation (apexai-os-meta) — no destructive gate
**T03 — Fix stale cross-references in the `03-` bundle + banners.** deps: []
- Fix: banner/index "D-01…D-12" → "D-01…D-18 (incl. incident decisions D-13–D-18)"; `04-open-questions.md` "→ D-10 (pending)" → ADR-002 **written**; clear the `[UNVERIFIED]` extension marker (resolved by D-15); `05-handover` "D-01…D-17" → include D-18.
- acceptance: no `D-01…D-12`, `pending` ADR, or `[UNVERIFIED]` stale strings remain in the bundle or the three redirect banners.
- status: not_started
**T04 — Update `CURRENT-STATE.md` BODY (not just its banner).** deps: [] — body still describes "one Docker Engine / Docker Desktop runtime"; rewrite to single WSL2 engine + shared Postgres. acceptance: body has no pre-migration topology as current.
**T05 — Add machine-readable `status:` frontmatter to the 3 stale ki-basis docs.** deps: [] — `status: superseded|amended`, `superseded_by:`/`current:` pointer. acceptance: a gate/agent can detect staleness from frontmatter, not just the banner.
**T06 — Wire the entry point.** deps: [] — make root `apexai-os-meta/AGENTS.md` + `CLAUDE.md`, `apex-meta/orchestration/00-START-HERE.md`, and `ki-basis/AGENTS.md` point to the current-truth `03-` bundle + ADR-002 + this PLAN. acceptance: a fresh agent from any root entry discovers current architecture without opening a stale doc. *(A minimal root-AGENTS.md pointer is added by this plan's author as a starting point — extend it.)*
**T07 — ADR-002 mirror-drift guard.** deps: [] — mark the canonical copy (`ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6) and note the 2 mirrors are hand-synced. acceptance: each of the 3 copies states which is canonical.

### Bucket 2 — Non-blocking infra follow-ups (apexai-os-meta)
**T08 — Confirm WSL memory ceiling 16 GB.** deps: [] — `.wslconfig` shows `memory=16GB` (appears DONE). acceptance: `.wslconfig` = 16GB AND live `docker stats` limit ≈16 GiB after next restart. If a change is needed it requires `wsl --shutdown` → `gate: human-approval`. status: likely_done — verify.
**T09 — Postgres connection/buffer tuning (monitor-only).** deps: [] — act only if a role sustains >80% of its `CONNECTION LIMIT` (`pg_stat_activity`). acceptance: baseline recorded; no change unless threshold crossed. status: open-monitor.
**T10 — Hermes compose-drift fix (D-16).** `gate: human-approval` — deps: [] — `ki-basis/compose.yaml` hermes declares named volumes but the live container runs bind mounts (`/root/.hermes`, `/root/workspaces`, ~4.4 GB). **Do NOT `docker compose up` on this file until reconciled.** Check spawned `task_95c691df` status first. acceptance: `docker compose config` shows hermes mounts == live mounts; a dry run changes no volume.
**T11 — Post-retirement soak smoke test.** deps: [] `[P]` — verify all live containers healthy, `docker.exe` gone (Docker Desktop uninstalled), both OpenProject (17.8) + Hermes reachable, cross-DB `REVOKE` isolation still holds. acceptance: all green; evidence saved. gate: none (read-only).

### Bucket 3 — Leela OpenProject pilot loose ends (Leela repo)
**T12 — Reconcile the pilot handovers with what was actually accepted.** deps: [] — record a decision that the operator (a) executed `DRAFT-IMPLEMENTATION-PLAN.md` directly and **waived** the required `IMPLEMENTATION-PLAN.md`, (b) chose a **portable custom API-v3 skill** over the draft's upstream-CLI route, (c) chose **fresh 17.8 install** over in-place upgrade. acceptance: a dated decision record exists; the 2 pilot handovers carry a "superseded/executed-directly → see …" pointer; draft Phases A–H marked done/moot/open accordingly.
**T13 — Create dedicated least-privilege Leela identity (D2); replace the admin token.** `gate: human-approval` (admin + credential) — deps: [] — non-admin OpenProject user + API token scoped to Leela projects; update `op.env`. acceptance: `whoami` shows the dedicated non-admin identity; test-scope writes still pass.
**T14 — Delete the demo Demo/Scrum projects on 17.8.** `gate: human-approval` (destructive; classifier-blocked for the agent) — deps: [T02, T13] — needs `project.delete` policy + the dedicated identity. acceptance: `project.list` shows only real Leela projects; demo gone; identity/target verified first.
**T15 — Verify Antigravity live invocation + generalize to Codex (D4).** deps: [] `[P]` — prove `agy` autonomously invokes the skill for a read; confirm Codex discovery/invocation. acceptance: evidence of an agent-initiated (not hand-run) read via the skill on each.
**T16 — Resolve write-autonomy policy (D6 / OQ-01).** `gate: operator-decision` — deps: [] — operator picks the risk-class policy; promote `write-policy.md` from provisional to accepted; record in the program owner. acceptance: an accepted policy exists; the skill's provisional table is replaced.
**T17 — Author the 17.8 operations runbook.** deps: [] `[P]` — start/stop/health, keepalive (Startup VBS), `.wslconfig`, recovery, ports, gaps — beside the pilot bundle. acceptance: runbook exists and a fresh agent can operate the instance from it.
**T18 — Cruft cleanup.** deps: [] `[P]` — remove `docs/ProjectMM/openproject/__MACOSX/` and tracked `.DS_Store`; add to `.gitignore`. acceptance: gone; ignored.
- *(Real task + fresh-session resume, draft Phase G/H: substantially demonstrated by census WP #38 — treat as satisfied; T15 covers the fresh-session/generalization proof.)*

### Bucket 4 — Adjacent workstream (apexai-os-meta `04-` bundle)
**T19 — Close the 3 operator-gated tasks in `04-leela-mastery-openproject-consolidation`.** `gate: operator` — deps: [] — (05) OpenProject browser idle-sleep keepalive; (06) Mastery-of-Arts sub-project taxonomy (design live with operator); (07) 5-account skill-standardization test. acceptance: per that bundle's own criteria; update its state.

## 7. Definition of done (whole program)
- [ ] Both repos committed; Leela `master` pushed; apexai-os-meta consolidation + live compose tracked.
- [ ] No stale cross-references; entry point routes agents to current truth; `CURRENT-STATE.md` body current.
- [ ] Soak smoke test green (T11); Hermes compose drift resolved or explicitly deferred with data-safety noted.
- [ ] Pilot: dedicated identity in use, demo projects removed, write-autonomy decided, runbook exists, handovers reconciled.
- [ ] 04-workstream tasks closed or explicitly parked with the operator.

## 8. Dependency summary
- Ready now (no deps, no gate): T03, T04, T05, T07, T09, T11, T12, T15, T17, T18.
- Ready now but gated: T01, T02, T06(min pointer done), T08(if change), T10, T13, T16, T19.
- Blocked: T14 → [T02, T13].

## 9. Research index (detailed, linked not inlined)
| Ref | File | Covers |
|---|---|---|
| R1 | [research/01-token-efficient-architecture-docs.md](research/01-token-efficient-architecture-docs.md) | AI-friendly, token-efficient architecture documentation (single source of truth, progressive disclosure, deprecation/redirect pattern, MADR/arc42/C4, AGENTS.md, llms.txt) |
| R2 | [research/02-ai-executable-plans.md](research/02-ai-executable-plans.md) | Machine-executable handoff plans (spec→plan→tasks→implement, EARS, DAG, validation gates, continuation files, the per-task template this plan uses) |
| R3 | `../03-wsl2-native-stack-consolidation/03-execution-plan.md` | The consolidation migration best-practice + runbook (already executed) |
