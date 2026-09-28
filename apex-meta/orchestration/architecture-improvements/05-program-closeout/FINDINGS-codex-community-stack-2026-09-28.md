---
type: Findings
title: Findings — `codex/separate-community-stack` usefulness / staleness / does-community-already-work
created: 2026-09-28
status: complete
owner: (investigator chat)
authority_order: "live runtime + code > accepted decisions/ADRs > this findings doc > the handover."
parent_handover: apex-meta/orchestration/architecture-improvements/05-program-closeout/HANDOVER-codex-community-stack-investigation.md
parent_plan: apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md  # T01
safety_note: READ-ONLY investigation. Nothing merged, deleted, pushed, rebased, or brought `up`. Branch preserved exactly. No secrets printed.
---

# Findings — assess `codex/separate-community-stack`

## TL;DR (the one-line answer)
**Yes — the community stack already runs correctly in the consolidated WSL2 / shared-Postgres
environment, and it was already split into its own repo (`C:\GitDev\lika-community`).** The branch's
premise (split community into a standalone repo with *airtight, zero-shared-DB, per-stack-Postgres,
Docker-Desktop* isolation) is **superseded on both axes**: the "own repo" goal was reached a *different*
way (consolidation + shared Postgres + `REVOKE CONNECT` role isolation per ADR-002), and the branch's
isolation *mechanism* is the exact pre-consolidation design ADR-002 retired. Its added docs/tests
describe the abandoned topology; its deletions are community scripts that were **moved** to
`lika-community` (and still also live on `main`). **Net recommendation: (b) keep parked as historical
reference** — no cherry-pick is required into the current `ki-basis` layout, and a wholesale merge is
unsafe (it would delete live scripts from `main`). Operator-gated; nothing executed.

---

## Evidence base (all read-only)
- Repo `C:\GitDev\apexai-os-meta`, current checkout `main` (verified `git rev-parse --abbrev-ref HEAD`).
- Branch `codex/separate-community-stack`: **2 unique commits** (`60c22c31`, `c039699c`); not on any
  remote; `main` is **11** commits past the shared base (`git log main..branch` / `branch..main`).
- Live engine: `wsl -d Ubuntu -u root -- docker ps` (one WSL2-native engine; Docker Desktop retired).
- Shared DB: `docker exec ki-basis-shared-postgres psql -U postgres` (roles, databases, ACL probe).
- ADR-002: `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6.
- Live private compose: `ki-basis/compose.shared-db.yaml`.
- Branch files read via `git show codex/separate-community-stack:<path>` (no checkout mutation).

---

## Q1 — Does the community stack already work in the consolidated environment? ✅ YES

Live `docker ps` shows a full **`community-*`** stack up ~1 h alongside the private **`ki-basis-*`**
stack, all on one engine:

```
community-hermes        Up ... 127.0.0.1:9642->8642, 127.0.0.1:9219->9119
community-nginx         Up (healthy) 127.0.0.1:9084->80
community-paperless     Up (healthy) 127.0.0.1:9010->8000
community-firefly       Up (healthy) 127.0.0.1:9086->8080
community-openproject   Up           127.0.0.1:9082->80
community-valkey        Up (healthy) 6379
ki-basis-{hermes,paperless,firefly,nginx,valkey}  Up ...
ki-basis-shared-postgres Up (healthy) 5432
leela-op178-openproject  Up           0.0.0.0:8083->80
```

- Both stacks run against **one shared Postgres** (`ki-basis-shared-postgres`), which holds separate
  databases per tenant: `comm_firefly / comm_openproject / comm_paperless` and
  `priv_firefly / priv_openproject / priv_paperless`.
- The community stack is driven by a **separate repo**: `docker inspect community-openproject` →
  `com.docker.compose.project=community`, `config_files=/mnt/c/GitDev/lika-community/compose.wsl.yaml`.
- `C:\GitDev\lika-community` is a real, independent git repo (own `.git`, own history, HEAD `e8c5015`).
- Community **OpenProject** *is* served here (`community-openproject`, `:9082`) — note the *private*
  stack deliberately has **no** OpenProject (`compose.shared-db.yaml` header + it points Hermes at
  `leela-op178-openproject:80`). So OpenProject topology differs per tenant, by design, and both are live.

**Conclusion:** community fundraiser/Telegram/Paperless/Firefly/OpenProject services are served by the
**current live consolidated setup**, not merely by branch artifacts.

## Q2 — Is the branch's "separate repo / isolation" premise obsolete? ✅ LARGELY YES

Two independent sub-claims:

1. **"Community as its own repo"** — *goal achieved, different route.* `lika-community` exists and is
   live. The branch would have carved it out of `ki-basis` with its own per-stack Postgres and
   Docker-Desktop lifecycle; reality reached the same *separation* via consolidation onto one WSL2
   engine + shared Postgres.
2. **The isolation *mechanism* the branch documents is superseded.** The branch's `compose.yaml` runs a
   **dedicated `ki-basis-postgres`** container (per-stack cluster) — precisely the model ADR-001 §3.4
   mandated and **ADR-002 retired**. Live isolation is instead **database-ACL based** and was verified:

   ```
   comm_firefly_app -> comm_firefly  CONNECT = t
   comm_firefly_app -> priv_firefly  CONNECT = f
   priv_firefly_app -> comm_firefly  CONNECT = f
   priv_firefly_app -> priv_firefly  CONNECT = t
   ```

   This matches ADR-002 §6 verbatim: *"one shared PostgreSQL cluster (`comm_*`/`priv_*` prefixes,
   `REVOKE CONNECT` for cross-tenant isolation)… cross-tenant `CONNECT` is revoked and was verified
   live."* The branch docs argue the **opposite** guarantee ("zero shared DBs", "physically and
   mathematically impossible" cross-contamination via two separate clusters + two `.git` repos).

**Do the isolation docs contain guarantees the consolidation still needs documented?** No new ones —
the trade the consolidation actually made (data-ACL isolation kept, *failure-domain* isolation given
up) is already documented, with rationale, in **ADR-002 §6** and the `03-` consolidation bundle. The
branch docs would *contradict* current truth if treated as live.

## Q3 — Which added docs are salvageable vs. stale?

All five architecture/runbook docs are written for the **pre-consolidation topology** (Docker Desktop
Hyper-V VM, `DockerDesktop.vhdx`, `Start-Process "…Docker Desktop.exe"`, per-stack Postgres, two
standalone repos `lika-community` **+ `private-business`**). Concrete stale bits found:

- **`OPERATOR_RUNBOOKS_AND_TEMPLATES.md` (984 ln)** — `start.ps1` template does a **"Docker Desktop
  Engine Check"** and launches `Docker Desktop.exe` (retired per ADR-002). Assumes a
  **`C:\GitDev\private-business\`** repo that **was never created** (see Q-note below). Its entire
  "Community Operations Template Pack" (AGENTS.md fence, `compose.yaml`, `start.ps1`) is **already
  materialized as real files** in the live `lika-community` repo (`README.md`, `AGENTS.md`, `SOUL.md`,
  `compose.wsl.yaml`, `scripts/start.ps1`) — so the runbook is a *draft of files that now exist
  elsewhere in more current form*. Highest line-count, **low current salvage value**.
- **`DUAL_STACK_ARCHITECTURE_AND_ISOLATION.md` (240 ln)** — "single Docker engine (**Hyper-V
  Backend**)"; describes Docker-Desktop dual-project. Superseded by ADR-002.
- **`WORKSPACE_ISOLATION_ARCHITECTURE.md` (343 ln)** — recommends *Option 2: two standalone repos
  `lika-community` + `private-business`* with **"airtight / zero shared DB"** isolation — the design
  ADR-002 explicitly did **not** ship (shared Postgres chosen instead). Superseded.
- **`DOCKER_VOLUME_PRESERVATION_PLAN.md` (272 ln)** — framed entirely around `DockerDesktop.vhdx` and
  `docker compose up -d` creating volumes. The *concept* (`external: true` named volumes survive config
  moves) is still true and is embodied in the live compose files, but the doc's engine/paths are stale
  and the migration it plans **already happened**. Low salvage; concept-only, would need a WSL2 rewrite.
- **`LIKA_COMMUNITY_HANDOVER.md` (91 ln)** — closest to reality: community **port band 908x/909x is
  correct** (`:9084/:9086/:9010/:9082/:9642/:9219` all match live). But container names are stale
  (`ki-basis-community-hermes` vs live `community-hermes`), and it is a *community operating guide that
  now belongs to the `lika-community` repo*, which already carries its own README/SOUL/AGENTS.
- **`POST-SEPARATION-MEMORY-HANDOVER.md` (3 ln)** — advisory only ("preserve Hermes history, propose
  evidence-based cleanup, do not wipe volumes"). Principle already honored (private Hermes uses bind
  mounts; volumes are `external: true`). Trivial.
- **`README.md` (1-pg cheat sheet)**, **`docs/plans/00_META_PROGRAM_PLAN.md`**,
  **`docs/workflows/WF01_WEEKLY_META_ORCHESTRATION.md`** — tied to the branch's "relocate meta
  workflows" intent; not part of the shipped `apex-meta` orchestration layout. Stale relative to current.
- **Added tests** `test_challenger_2_adversarial.py` (333 ln), `test_deliverables_stress.py` (248 ln) —
  **validators for the abandoned deliverables**: they assert `ki-basis/compose.yaml` has "exactly 10
  volumes, all `external: true`", expect `.env.private`/`.env.community`, and check the Docker-Desktop
  `start.ps1` / split-nginx templates in the runbook. They would **fail against** the consolidated
  `compose.shared-db.yaml` reality. Not salvageable as-is.

**Salvageable as-is into current `ki-basis`: none.** The genuinely-still-true ideas (ACL isolation,
volume invariance) are already captured in ADR-002 + the `03-` bundle or embodied in live compose.

## Q4 — Are the branch deletions decommissioning or accidental loss? → Intentional relocation; nothing lost

Deleted on branch (9 items): `generate_euer_tax_report.py`, `generate_fundraiser_assets.py`,
`hermes_telegram_intake.py`, `populate_firefly.py`, `populate_openproject.py`, `populate_paperless.py`,
`pretix_adapter.py`, `verify_fundraiser_stack.py`, and `skills/equinox-intake/SKILL.md`.

- **All 9 still exist on `main`** (`git ls-tree -r main -- ki-basis/scripts/ ki-basis/skills/`) — the
  handover's spot-check generalizes: every one is present, not just the four named.
- **All 9 also now live in `lika-community`** (`lika-community/scripts/*` and
  `lika-community/skills/equinox-intake/SKILL.md`) — i.e. they are **community-domain scripts that were
  moved to the community repo**. `lika-community` additionally has newer siblings (`call_agenda.py`,
  `skills/call-agenda/`) not on `main`.

So the deletions express the *correct intent* (these belong to the community stack, now in
`lika-community`) but are **redundant with reality** and **doubly preserved** (on `main` + in
`lika-community`). ⚠️ A wholesale `git merge` of the branch would **delete the working copies from
`ki-basis/main`** — do not merge.

## Q5 — Live-state claims in branch docs, verified

- Branch docs claim community services on **port band 908x/909x** → **confirmed live** (matches `docker ps`).
- Branch docs imply **Docker Desktop** engine + **`DockerDesktop.vhdx`** volumes → **false now**: engine
  is WSL2-native `Ubuntu` `dockerd`; Docker Desktop retired (ADR-002 §6, live `docker ps`).
- Branch docs assume a **`C:\GitDev\private-business\`** standalone repo → **does not exist**; the
  private stack stayed in `apexai-os-meta/ki-basis` (`compose.shared-db.yaml`). Only the *community*
  half of the two-repo plan happened.
- Branch docs assert **two separate Postgres clusters / zero shared DB** → **false now**: one shared
  `ki-basis-shared-postgres`, isolation via `REVOKE CONNECT` (verified live).

## Salvage table

| Branch file | Verdict | Why / where current truth lives |
|---|---|---|
| `docs/OPERATOR_RUNBOOKS_AND_TEMPLATES.md` (984) | **Stale** (park) | Docker-Desktop `start.ps1`; assumes non-existent `private-business` repo; community pack already real in `lika-community`. |
| `docs/DUAL_STACK_ARCHITECTURE_AND_ISOLATION.md` (240) | **Stale** (park) | Hyper-V dual-project; superseded by ADR-002 §6. |
| `docs/WORKSPACE_ISOLATION_ARCHITECTURE.md` (343) | **Stale** (park) | Recommends zero-shared-DB + 2 standalone repos; opposite of what shipped. |
| `docs/DOCKER_VOLUME_PRESERVATION_PLAN.md` (272) | **Stale, concept-only** (park) | `DockerDesktop.vhdx` framing; volume-invariance idea already embodied in live `external: true` compose. |
| `docs/LIKA_COMMUNITY_HANDOVER.md` (91) | **Superseded** (park; belongs to `lika-community`) | Ports correct, container names stale; `lika-community` has its own README/SOUL/AGENTS. |
| `docs/POST-SEPARATION-MEMORY-HANDOVER.md` (3) | **Stale/trivial** (park) | Advisory already honored (bind mounts + external volumes). |
| `README.md`, `docs/plans/00_META_PROGRAM_PLAN.md`, `docs/workflows/WF01_…md` | **Stale** (park) | Branch "relocate meta workflows" intent; not the shipped `apex-meta` layout. |
| `tests/test_challenger_2_adversarial.py` (333) | **Stale** (park) | Asserts `compose.yaml` "10 external volumes", `.env.private/.community`, Docker-Desktop runbook — fails vs consolidated reality. |
| `tests/test_deliverables_stress.py` (248) | **Stale** (park) | Stress-tests the abandoned split-repo deliverables. |
| Modified `compose.yaml`, `start/stop-ki-basis.*`, `nginx/default.conf`, `invoke-hermes.ps1`, `backup-stack.sh`, `SOUL.md`, `AGENTS.md`, `AGENT-OPERATING-CONTEXT.md`, `test_adversarial_isolation.py` | **Stale/conflicting** (do not merge) | Encode per-stack Postgres + Docker-Desktop; live truth is `compose.shared-db.yaml` on `shared-db-net`. |
| Deleted `scripts/*` + `skills/equinox-intake` (9) | **Do NOT let a merge remove** | Present on `main` **and** relocated to `lika-community`. |

**Cherry-pick target list: empty.** Nothing on the branch needs importing into current `ki-basis`.

## Q6 — Net recommendation → **(b) Keep parked as historical reference**

Rationale:
- Everything of value has a more-current home already: community operating artifacts in `lika-community`;
  the isolation trade-off rationale in **ADR-002 §6** + the `03-` bundle; the deleted scripts safe on
  `main` and in `lika-community`.
- The branch documents a **coherent alternative that was deliberately not taken** (per-stack Postgres,
  Docker-Desktop, two standalone repos incl. a `private-business` that never shipped). That has archival
  value as the "road not taken" behind ADR-002 — hence **park**, not delete-now.
- **(a) cherry-pick** is not warranted (no unique live-true content).
- **(c) safe-to-delete** is *defensible* (2 local commits, not on any remote, all content superseded) and
  carries no data risk — but it conflicts with the operator's standing "keep everything parked"
  instruction, so it is **not** the recommendation. If the operator later wants the branch gone, it is
  safe to delete **provided nothing is merged first**.
- ⚠️ **Do NOT `git merge`** this branch under any option: the merge would delete 9 live community scripts
  from `ki-basis/main`.

**Operator-gated. Nothing here was executed.**

---
### Appendix — commands run (read-only)
`git branch --list`, `git log main..branch` / `branch..main`, `git diff --stat/--name-status main...branch`,
`git ls-tree -r main -- ki-basis/{scripts,skills,tests}`, `git show branch:<doc>` (grep only),
`docker ps`, `docker network ls`, `docker inspect <ctr> --format {{compose labels}}`,
`psql -Atc "SELECT rolname FROM pg_roles"`, `"SELECT datname FROM pg_database"`,
`"SELECT has_database_privilege(...)"`, plus `ls` of `lika-community/` and absence check of `private-business/`.
No secrets printed; no mutating git/docker commands issued.
