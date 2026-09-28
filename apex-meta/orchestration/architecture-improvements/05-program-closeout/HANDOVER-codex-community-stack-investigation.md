---
type: Handover
title: Investigate the `codex/separate-community-stack` branch — usefulness, staleness, and whether the community stack already works in the consolidated environment
created: 2026-09-28
status: open
owner: (unassigned investigator chat)
authority_order: "live runtime + code > accepted decisions/ADRs > this handover. Surface conflicts; never invent a winner."
parent_plan: apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md  # T01 branch decision
safety: READ-ONLY investigation. Do NOT merge, delete, push, rebase, or `docker compose up`. The branch is PARKED by operator instruction.
---

# Handover — assess `codex/separate-community-stack`

## 0. Your mission (one line)
Decide, with evidence, **what on the `codex/separate-community-stack` branch is still worth keeping**, **what is outdated**, and specifically **whether the "community" stack already runs correctly in the new consolidated WSL2 / shared-Postgres environment** — because running both stacks in one consolidated environment is what was actually built, and this branch was a *different* plan (split the community stack into its own repo). Produce a recommendation; **change nothing.**

## 1. Hard safety rules (read first)
- **READ-ONLY.** No `git merge`, `git rebase`, `git branch -d/-D`, `git push`, `git checkout` that mutates working tree state you can't restore, and **no `docker compose up`** on any file (a naive up on `ki-basis/compose.yaml` can wipe ~4.4 GB of live Hermes bot state — see D-16 in the 03-bundle decisions log). Inspect with `git show`, `git diff`, `git log`, and read-only `docker ps`/`docker inspect`.
- The branch is **parked** — the operator explicitly said keep everything, nothing irreversible. Preserve it exactly.
- **Never print or commit secrets.** Do not cat: `C:\GitDev\ki-basis-shared\.env`, `ki-basis/.env`, `ki-basis/.env.community`, `C:\GitDev\leela-op178\op.env`, or any community-bot `.env`. If a branch file embeds a literal secret, report the file+line, not the value.
- One engine now: run docker via `wsl -d Ubuntu -u root -- docker …`; prefix `/mnt/c` paths with `MSYS_NO_PATHCONV=1`; pipe binary-ish output through `| tr -d '\0'`.

## 2. Current-truth anchors (what was ACTUALLY built — ground here, not in the branch)
The executed architecture is a **single WSL2-native "Apex" Docker engine** running **both** the private and community stacks against **one shared PostgreSQL** (Docker Desktop retired). Read only as needed:
- **ADR-002** — `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` **§6** (canonical architecture decision).
- **Consolidation bundle** — `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/` (`index.md`, `02-decisions-log.md` D-01…D-18, `05-handover.md`, `log.md`). This is now committed to git (commit `5636027`).
- **Live prod compose** — `ki-basis/compose.shared-db.yaml` (private stack on shared-db-net; note it deliberately has **no** openproject service; hermes uses **bind mounts** `/root/.hermes`, `/root/workspaces`).
- The close-out plan this handover serves: `…/05-program-closeout/PLAN.md` (branch decision lives in **T01**).

## 3. What the branch actually is (verified 2026-09-28)
- Local branch **`codex/separate-community-stack`**, **NOT on any remote** (origin has other `codex/*` branches, not this one).
- **Only 2 unique commits** on the branch (main has since advanced 10 commits past the shared base):
  - `60c22c31` feat(ki-basis): separate community stack to standalone repo and relocate meta workflows
  - `c039699c` docs(ki-basis): add streamlined 1-page operational cheat sheet README.md
- **Core intent of the branch:** the *opposite* direction from what shipped — physically **split the community ("Lika Community" — Safer Space e.V., Equinox 2026 fundraiser, Paperless receipts, Telegram bot) into its own standalone repo** with hard workspace/stack isolation. Main instead **consolidated** everything onto one engine + one DB. So the branch's premise may be partly or wholly obsolete — that is the central question to test.

### 3a. Files ADDED only on the branch (candidate salvage — assess each for staleness)
- `ki-basis/docs/OPERATOR_RUNBOOKS_AND_TEMPLATES.md` (~984 lines — largest; likely highest salvage value)
- `ki-basis/docs/DUAL_STACK_ARCHITECTURE_AND_ISOLATION.md` (~240 lines)
- `ki-basis/docs/WORKSPACE_ISOLATION_ARCHITECTURE.md` (~343 lines)
- `ki-basis/docs/DOCKER_VOLUME_PRESERVATION_PLAN.md` (~272 lines)
- `ki-basis/docs/LIKA_COMMUNITY_HANDOVER.md` (~91 lines — community operating guide)
- `ki-basis/docs/POST-SEPARATION-MEMORY-HANDOVER.md` (3 lines — says: preserve Hermes history/data, propose evidence-based cleanup, do NOT wipe volumes)
- `ki-basis/README.md` (1-page cheat sheet), `docs/plans/00_META_PROGRAM_PLAN.md`, `docs/workflows/WF01_WEEKLY_META_ORCHESTRATION.md`
- `ki-basis/tests/test_challenger_2_adversarial.py`, `ki-basis/tests/test_deliverables_stress.py`

### 3b. Files DELETED on the branch (⚠️ these still exist on `main` — do NOT let a merge remove them)
`ki-basis/scripts/`: `generate_euer_tax_report.py`, `generate_fundraiser_assets.py`, `hermes_telegram_intake.py`, `populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`, `pretix_adapter.py`, `verify_fundraiser_stack.py`; and `ki-basis/skills/equinox-intake/SKILL.md`.
(Several of these — `generate_fundraiser_assets.py`, `hermes_telegram_intake.py`, `pretix_adapter.py`, `verify_fundraiser_stack.py` — are confirmed still present on `main`. Confirm each; a wholesale merge would delete working code.)

### 3c. Heavily MODIFIED on the branch (conflict risk with consolidation)
`ki-basis/compose.yaml` (~203 lines changed), `ki-basis/SOUL.md`, `ki-basis/docker/nginx/default.conf`, `ki-basis/scripts/start-ki-basis.*`, `stop-ki-basis.*`, `invoke-hermes.ps1`, `backup-stack.sh`, `ki-basis/AGENTS.md`, `ki-basis/AGENT-OPERATING-CONTEXT.md`, `ki-basis/tests/test_adversarial_isolation.py`.

## 4. Investigation questions (answer each with evidence)
1. **Does the community stack already work in the consolidated environment?** Confirm which community services are defined and running now (firefly / paperless / valkey / nginx / hermes; community DB roles on shared Postgres). Is the community OpenProject/Telegram/fundraiser flow served by the current live setup, or only by branch artifacts? Anchor in live `docker ps` + `compose.shared-db.yaml` + ADR-002.
2. **Is the branch's "separate repo / isolation" premise obsolete?** Given consolidation (one engine, one DB, isolation via DB roles + `REVOKE` per D-bundle), do `DUAL_STACK_ARCHITECTURE_AND_ISOLATION.md` / `WORKSPACE_ISOLATION_ARCHITECTURE.md` describe a design that was superseded, or do they contain isolation guarantees the consolidation still needs documented?
3. **Which added docs are salvageable vs. stale?** Especially `OPERATOR_RUNBOOKS_AND_TEMPLATES.md` — are its runbooks accurate against the *current* engine/commands, or written for the abandoned split-repo topology? Flag concrete stale bits (paths, `docker compose` invocations, ports, repo names).
4. **Do the branch deletions represent intentional decommissioning or accidental loss?** For each deleted script/skill: is its function still needed, already replaced on main, or genuinely retired? (Cross-check the fundraiser/tax/telegram scripts that still live on main.)
5. **Any live-state claims to verify?** Does any branch doc assert "X is running/migrated"? Verify against live before trusting.
6. **Net recommendation:** one of — (a) cherry-pick specific docs/tests into current layout (list exact files + target paths), (b) keep parked as historical reference, or (c) safe to delete the branch. If (a) or (c), it is operator-gated; do NOT execute — just recommend.

## 5. Suggested read-only commands
```bash
cd /c/GitDev/apexai-os-meta
# Branch shape
git log --oneline --no-merges main..codex/separate-community-stack | cat
git diff --stat main...codex/separate-community-stack | cat
git diff --name-status main...codex/separate-community-stack | cat
# Read a branch file WITHOUT checking it out:
git show codex/separate-community-stack:ki-basis/docs/OPERATOR_RUNBOOKS_AND_TEMPLATES.md | less
git show codex/separate-community-stack:ki-basis/docs/DUAL_STACK_ARCHITECTURE_AND_ISOLATION.md | less
# Compare a modified file branch-vs-main:
git diff main:ki-basis/compose.yaml codex/separate-community-stack:ki-basis/compose.yaml | cat
# Confirm a "deleted" script still exists on main:
git ls-files ki-basis/scripts/ | cat
# Live environment (read-only) — one engine:
wsl -d Ubuntu -u root -- docker ps --format 'table {{.Names}}\t{{.Status}}\t{{.Ports}}'
wsl -d Ubuntu -u root -- docker network ls
# DB roles (read-only) — adjust container/role names from compose.shared-db.yaml; do NOT print passwords:
wsl -d Ubuntu -u root -- docker exec <shared-postgres-container> psql -U <admin> -c "\du"
```

## 6. Deliverable
Write findings to a NEW dated file beside this one:
`apex-meta/orchestration/architecture-improvements/05-program-closeout/FINDINGS-codex-community-stack-2026-09-28.md`
containing: per-question answers with evidence (command output snippets, file:line refs), a salvage table (file → keep/cherry-pick/stale → target path if kept), the deletion audit, and the single net recommendation (a/b/c). **Do not act on it** — hand the recommendation back to the operator, who will decide the gated action. When done, update PLAN.md T01's note to point at your findings file.
