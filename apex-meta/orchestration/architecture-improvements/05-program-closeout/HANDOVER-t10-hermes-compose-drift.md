---
type: Handover
title: T10 — Hermes compose-drift — deep research + safe resolution (data-loss-critical, anti-overcorrection)
description: Dedicated handover for one chat to resolve the private-Hermes compose/volume drift (D-16) WITHOUT losing ~7.9 GB of live bot state, understanding the full current architecture and both Hermes instances first, and explicitly guarding against the overcorrection/blind-spot failure mode. Research-and-plan only — NO infra change without operator approval.
created: 2026-09-28
status: open
owner: (next chat — treat as an infra auditor, not an implementer)
authority_order: "LIVE runtime + code > accepted decisions/ADRs > this handover. If they conflict, STOP and surface it — never invent a winner."
implementation_authority: research-and-recommend ONLY. No compose up / recreate / volume change without an explicit, per-action operator OK.
parent_plan: apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md   # task T10 / handover R4
---

# T10 — Hermes compose-drift: safe resolution (data-loss-critical)

## 0. Read this first — the failure mode we are guarding against
The operator has repeatedly been burned by exactly this pattern: an agent with a **limited view** sees a
small inconsistency, "quickly fixes" it, and the fix has a **blind spot** that breaks a working system. The
current architecture **works today**. Your job is NOT to redesign it. Your job is to make ONE marked
landmine safe, with the **smallest possible change**, after **understanding the whole picture** and
**backing up first**. **Overcorrection is the enemy.** If your plan touches more than the private Hermes
service definition, you have gone too wide — stop and reconsider.

**Hard stop rules (fail-closed):**
1. **NEVER run `docker compose up` (or `down`, `restart`, `recreate`) on `ki-basis/compose.yaml`.** It
   declares *empty named volumes* for Hermes; bringing it up would recreate the container on those empty
   volumes and **orphan/wipe ~7.9 GB of live private-bot state**. This is the entire risk (decision D-16).
2. No container recreate, no `docker volume rm`, no volume/mount change, no `wsl --shutdown`, **until** a
   written plan with a **tested backup + tested restore** is approved by the operator.
3. Everything is **read-only** until then: `docker inspect`, `docker ps`, `ls`, `du`, reading files. Never
   print/commit secrets (see §6).
4. Do **not** "harmonize" the two Hermes instances just because they differ — the difference is real and
   has a reason (§3). Consistency is not a goal that justifies data-loss risk.

## 1. Mission
Resolve the drift between the private Hermes container's **live storage** and its **checked-in compose
declaration**, so that no future `compose up` can wipe its state — **without moving or losing any data**,
and **without disturbing the community Hermes**. Produce a verified, operator-gated plan; do not execute it.

## 2. VERIFIED GROUND TRUTH (captured read-only 2026-09-28 — start here, don't re-derive blindly, but DO re-verify live before acting)

### Two engines? No — one. One WSL2-native "Apex" Docker engine (Ubuntu), Docker Desktop retired (ADR-002).
Run docker as: `wsl -d Ubuntu -u root -- docker …`.

### Private Hermes — `ki-basis-hermes`  (created 2026-09-26T12:24Z)
- **LIVE storage = BIND MOUNTS:**
  - `/root/.hermes` → `/opt/data`  (**4.4 GB** — bot memory/state; `HERMES_HOME=/opt/data`)
  - `/root/workspaces` → `/root/workspaces`  (**3.5 GB** — working files)
  - (paths are on the WSL2 ext4 filesystem, under the root user's home)
- **`ki-basis/compose.yaml` (the DRIFTED file — NOT what's running) declares NAMED volumes:**
  `hermes_data:/opt/data`, `hermes_workspaces:/root/workspaces` → **MISMATCH with live.** ← the drift.
- **`ki-basis/compose.shared-db.yaml` (the file the live stack ACTUALLY runs from) declares the BIND mounts:**
  `/root/.hermes:/opt/data`, `/root/workspaces:/root/workspaces` → **MATCHES live.** ✅
- So the *running* config is already correct; the hazard is purely the stale `compose.yaml` rollback file.
- ⚠️ Note a discrepancy to reconcile: D-16 says the container was created 2026-09-01; live inspect says
  2026-09-26 (it was recreated during the consolidation cutover). Verify the history; don't trust either
  date blindly.

### Community Hermes — `community-hermes`  (created 2026-09-26T11:34Z) — DIFFERENT model
- **LIVE storage = NAMED volumes** (Docker-managed): `community_hermes_data` → `/opt/data`,
  `community_hermes_workspaces` → `/root/workspaces`, `community_call_agenda` → `/opt/data/call-agenda`;
  **plus read-only config BIND mounts** from `C:\GitDev\lika-community\`: `SOUL.md`, `scripts/`,
  `skills/equinox-intake`, `skills/call-agenda`, `docker/hermes/run.py`.
- **`lika-community/compose.wsl.yaml` declares exactly that** (`hermes_data`/`hermes_workspaces`/`call_agenda`
  named volumes + the config binds) → **MATCHES live. Community Hermes has NO drift.** (Re-verify, but this
  is the expected finding.)
- **Separate compose project** (`-p community`), separate repo (`lika-community`), separate networks/ports
  (9642/9219). A change to the private stack must not touch it.

### Why the two differ (history, not a design ideal — understand before "fixing")
Private Hermes predates the migration and carried ~7.9 GB of real state; during consolidation it was
**recreated preserving its existing bind mounts** (via `compose.shared-db.yaml`) specifically to avoid data
loss. Community was migrated **fresh onto WSL with named volumes** (decision D-14). The asymmetry is a
consequence of migrating a live, stateful container safely — not a mistake to normalize away.

## 3. The actual risk, named precisely
- **This is a data-LOSS risk (wiping/orphaning live state), not a data-leak/exfiltration risk.** The 7.9 GB
  of private Hermes state would be stranded on the old bind paths while a fresh empty container starts on
  named volumes. (Secrets are a *separate* concern — see §6 — do not conflate.)
- It only triggers if someone brings up the wrong file (`ki-basis/compose.yaml`). Today nothing does.

## 4. Context management — read in THIS order (progressive disclosure; do not front-load everything)
1. **This handover** (you are here).
2. **ADR-002 — current architecture decision:** `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6. Why one
   engine + shared Postgres; the isolation model.
3. **The decision ledger (only these rows):**
   `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/02-decisions-log.md`
   → **D-16** (the Hermes drift itself), **D-17** (the alias-collision incident — what casual reuse already
   cost once), **D-18** (v14 deletion — the "verify identity before acting" lesson), **D-14** (community
   moved to WSL named volumes — explains the asymmetry).
4. **The three compose files (compare declaration vs the live mounts in §2):**
   `ki-basis/compose.yaml` (drifted), `ki-basis/compose.shared-db.yaml` (live/correct),
   `C:\GitDev\lika-community\compose.wsl.yaml` (community).
5. **Soak evidence (live health baseline):** `…/05-program-closeout/EVIDENCE-infra-soak-2026-09-28.md`.
6. **Only if needed:** the consolidation `05-handover.md` and `log.md` in the 03 bundle.
Do NOT preload the whole repo, unrelated bundles, or the pilot/OpenProject docs — they are not relevant to
this task.

## 5. Research assignment (be excessive, but ON-TARGET — waste nothing on the irrelevant)
Answer each with evidence (official Docker docs + the live system + the decision ledger; cite sources/dates):
1. **How Hermes persists state:** what actually lives in `/opt/data` (`HERMES_HOME`) and `/root/workspaces`
   for this Nous `hermes-agent` image — memory, sessions, skills, scheduled jobs, lazy-installed packages.
   What breaks if any of it is lost or reset.
2. **Bind mounts vs named volumes** for this case, precisely: recreate behavior, backup/restore ergonomics,
   performance on WSL2 ext4, and failure modes. What does `docker compose up` actually do to volumes when a
   service's volume declaration changes vs matches (when does it recreate, when does it reuse)?
3. **The safe options to remove the drift**, with the least-change one first. At minimum evaluate:
   - **Option A — make the file match reality:** edit `ki-basis/compose.yaml` so its Hermes service declares
     the live bind mounts (like `compose.shared-db.yaml` already does). No data moved, no `compose up`.
     Confirm this fully removes the hazard (a future up would then reuse the real data).
   - **Option B — migrate bind → named volumes deliberately:** only if named volumes are actually wanted;
     requires backup, copying 7.9 GB into the named volumes, verifying, then switching. Higher risk/effort.
   - **Option C — leave as-is + hard guard:** keep the warning; maybe rename/neutralize `compose.yaml` so it
     can't be `up`ed by accident. Lowest change, doesn't "fix" the file.
   For each: exact steps, what could go wrong, how to verify, and rollback.
4. **Backup/restore that is actually tested:** define how to back up `/root/.hermes` + `/root/workspaces`
   (and the community named volumes if community is ever touched) and how to *prove* the backup restores,
   BEFORE any change. A backup you haven't restored is not a backup.
5. **Community spillover — verify, don't assume:** confirm community Hermes has no drift; confirm the private
   fix is scoped to the private compose project and cannot affect `community-hermes`, its `community_*`
   volumes, or the `lika-community` repo binds. State explicitly whether anything about the chosen option
   changes community behavior (it should not).
6. **Blind-spot pass (required):** before recommending, list what your plan assumes and what would break if
   each assumption is wrong (e.g. the container being running during a change, the shared Postgres network,
   `restart: unless-stopped` semantics, the D-17 alias collision, secrets in env, other services depending
   on Hermes). This section is the guard against overcorrection — do not skip it.

## 6. Secrets — never print/commit
Hermes env carries secrets (`HERMES_API_SERVER_KEY`, `OPENPROJECT_API_KEY`, `HERMES_DASHBOARD_BASIC_AUTH_PASSWORD`),
sourced from `.env` files. Never cat/echo/commit: `C:\GitDev\ki-basis-shared\.env`, `ki-basis/.env`,
`ki-basis/.env.community`, community bot `.env`. Report a file+line if a secret is found in the wrong place,
never the value.

## 7. Deliverable
A findings + plan doc beside this one
(`FINDINGS-t10-hermes-compose-drift-2026-09-28.md`) containing: the verified current model of BOTH Hermes;
the answers to §5 with citations; a **recommended option (least-change, data-safe) with exact operator-gated
steps, a tested backup/restore, verification, and rollback**; the blind-spot analysis; and an explicit
"community is unaffected because …" statement. **Do not execute.** Hand the recommendation to the operator
for a go/no-go. If the safest recommendation is "leave it and just neutralize `compose.yaml`," that is a
legitimate, welcome outcome — the bar is data-safety, not tidiness.

## 8. Definition of done
The operator has a clear, evidence-backed, minimal, data-safe plan (or an explicit "keep parked" with the
hazard neutralized), the community Hermes is proven unaffected, and nothing was changed on the live system
without approval. A verified backup exists (or is the first step of the approved plan) before any mutation.
