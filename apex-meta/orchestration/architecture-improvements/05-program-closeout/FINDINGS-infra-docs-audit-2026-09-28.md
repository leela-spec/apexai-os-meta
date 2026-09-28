---
type: Findings
title: Infrastructure-documentation audit — currency, duplication, drift, and misplaced files
description: >
  Read-only audit (3 parallel agents) of every file describing the ki-basis infrastructure across
  apexai-os-meta, Leela-Cloud-2026, and the sibling infra repos (ki-basis-shared, leela-op178,
  lika-community). Finds one live hazard, a cluster of un-bannered stale docs, verbatim duplication +
  hand-synced mirror drift, and ~197 general-infra files misplaced in the Leela product repo. Ends with
  a tiered, operator-gated remediation plan. No files were changed.
created: 2026-09-28
status: recommendation-ready — DO NOT execute remediation without per-tier operator go
method: 3 read-only sub-agent audits (apexai-os-meta docs / Leela repo / cross-repo refs + mirror diff)
parent_plan: apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md
authority_order: "LIVE runtime + code > accepted ADRs > docs. Where a doc contradicts live reality it is stale, full stop."
---

# Infrastructure-documentation audit (2026-09-28)

## 0. Ground truth (what the docs SHOULD say)
One WSL2-native "Apex" engine (Ubuntu `dockerd`); **Docker Desktop retired**. **One** shared PostgreSQL
cluster (`ki-basis-shared-postgres`, defined in `C:\GitDev\ki-basis-shared\compose.yaml`) with `priv_*`/`comm_*`
DBs + `REVOKE CONNECT`. Private + community are separate compose projects on the one engine. Private stack =
`ki-basis/compose.shared-db.yaml` (`compose.yaml` is a superseded rollback file). Private Hermes on **bind
mounts** (T10). Private OpenProject = `leela-op178-openproject` **17.8** (its own project, wired to the shared
cluster via `leela-op178/compose.shared-db.yaml`); the v14 `ki-basis-openproject` was **deleted** (D-18).
Canonical architecture doc: `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002) + the
`03-wsl2-native-stack-consolidation/` bundle.

## 1. 🔴 The one LIVE HAZARD (fix first)
There is an active routing chain that sends any agent to **retired, data-unsafe** truth:

`ki-basis/AGENT-OPERATING-CONTEXT.md` **§13** → `apex-meta/Alpine/ARCHITEKTUR-BASIS.md` → which declares
**Docker Desktop the current engine** and names **`ki-basis/compose.yaml` the "current runtime authority."**
`compose.yaml` is the exact rollback file that (pre-T10) could wipe Hermes state, and running it recreates the
private stack onto the retired local-postgres topology. An agent following AGENT-OPERATING-CONTEXT for
"stable architecture" lands here. **This is the highest-priority fix** (re-point §13 to ADR-002 §6 + the 03
bundle; banner or retire `ARCHITEKTUR-BASIS.md`).

## 2. Stale docs presented as current WITHOUT a superseded banner
| file | what it wrongly asserts |
|---|---|
| `apex-meta/Alpine/ARCHITEKTUR-BASIS.md` | Docker Desktop = current engine; `compose.yaml` = runtime authority (the §13 target above) |
| `ki-basis/STACK_ARCHITECTURE.md` | `OpenProject 14` / `ki-basis-openproject` (the **deleted** v14, D-18); single `ki-basis-net`; `ki-basis-postgres` as the shared DB |
| `ki-basis/docs/DUAL_INSTANCE_RUNBOOK.md` | two separate stacks + per-stack Postgres (two-postgres); Docker Desktop GUI |
| `apex-meta/orchestration/new_final_v4/architecture_dossier/00_ARCHITECT_EXECUTIVE_SUMMARY.md` + `.../02_DUAL_INSTANCE_RUNBOOK.md` | "All 7 containers in Docker Desktop"; Strategy-B split-daemon as live |
| `docs/AUDIT_DOSSIER_DUAL_KI_BASIS/00_ARCHITECT_EXECUTIVE_SUMMARY.md` + `.../02_DUAL_INSTANCE_RUNBOOK.md` | identical stale content (the duplicate copy — see §3) |
| `ki-basis/docs/BOT_WIRING_AND_PERSONA_HANDOVER.md` | stale community container names; also a *misplacement* (documents `lika-community` from inside apexai-os-meta) |
| `.../workflow_plans/*`, both `agent_transcripts/*` sets | pre-ADR-002 narratives, un-flagged (historical, low stakes) |

**Correct/current (for reference):** canonical `DUAL_INSTANCE_ARCHITECTURE.md` §6; the `03-`/`05-` bundles;
`CURRENT-STATE.md` body (though its frontmatter still says `status: superseded` — under-sells it); root +
`ki-basis` `CLAUDE.md`/`AGENTS.md` entrypoints.

## 3. Duplication & inefficiency (why drift keeps happening)
- **The architecture dossier is duplicated verbatim in two trees:**
  `apex-meta/orchestration/new_final_v4/architecture_dossier/` **and** `docs/AUDIT_DOSSIER_DUAL_KI_BASIS/`
  (same `00/01/02/…` + 2×11 `agent_transcripts`). Every future correction must be made twice; the stale
  `00_`/`02_` siblings sit un-flagged next to the correctly-synced `01_`.
- **Three copies of the architecture spec** (`DUAL_INSTANCE_ARCHITECTURE.md`): 1 canonical + 2 mirrors,
  "hand-synced, no automation" by the doc's own admission.
- **Mirror drift CONFIRMED (measured):** the two mirrors are byte-identical to each other (md5 `3d193a53…`,
  566 lines) but differ from canonical (583 lines) by **3 hunks / 17 lines** — they are **missing** (a) the
  YAML frontmatter (`status: amended`, `canonical:` …) and (b) the **⛔ top banner** that R2's "zero shared
  DBs" model was reversed to a shared Postgres cluster (D-07). A reader opening a mirror at §3 gets **no
  up-front warning** that the isolation model changed.
- **Six overlapping "current architecture" surfaces** that now disagree: `CURRENT-STATE.md`,
  `AGENT-OPERATING-CONTEXT.md`, `STACK_ARCHITECTURE.md`, `DUAL_INSTANCE_RUNBOOK.md`,
  `Alpine/ARCHITEKTUR-BASIS.md`, `03-…/01-architecture-and-gaps.md`.
- `GEMINI.md` and `.hermes.md` are byte-identical and both lack the current-arch pointer banner that root
  `CLAUDE.md`/`AGENTS.md` carry.

## 4. Misplaced files — general/shared infra living in the Leela product repo
`C:\GitDev\Leela-Cloud-2026\docs\ProjectMM\openproject\` (~197 files) is **shared-infra**, not Leela-product.
Ranked by how clearly they belong in apexai-os-meta:
1. `RUNBOOK-openproject-17.8-operations.md` — pure infra ops (docker start/stop, WSL keepalive `.vbs`,
   `.wslconfig`, ports for ki-basis/community/Hermes, backup scripts). Zero product content. ✅ content current.
2. `openproject\**` (~180 files) — an **AnythingLLM connector package**, explicitly "reference-only, superseded"
   (the live skill is the portable Node one). Bulk of the noise; dead reference sitting in a current-docs tree.
3. `DECISION-2026-09-28-canonical-skill-architecture.md` — its own text says a cross-cutting capability
   "shouldn't live inside one product repo (Leela-Cloud-2026)."
4. `AGENT-QUICKSTART.md`, `VERIFICATION-2026-09-28-agent-invocation.md`,
   `FUTURE-DEVELOPMENT-least-privilege-agent-identity.md`, `DECISION-2026-09-28-pilot-execution-reconciliation.md`,
   `README.md`, and the superseded pilot handovers.

**Why leela-op178 is shared infra (despite the name):** it hosts `Leela & Mastery` + PM-Infrastructure org-wide,
its DB is `priv_openproject` on the shared cluster, and **private Hermes points at it**
(`OPENPROJECT_API_URL=http://leela-op178-openproject:80`). Its operational docs are shared-infra docs.

**Reverse misplacement:** `ki-basis/docs/BOT_WIRING_AND_PERSONA_HANDOVER.md` (in apexai-os-meta) documents the
`lika-community` bot — and `lika-community` already has its own copy. That doc arguably belongs in (or should
defer to) `lika-community`.

### 4.1 References that must be updated if the Leela cluster moves (low-risk — runtime unaffected)
The **runtime skill + token already live OUTSIDE the repo** (`C:\GitDev\agent-skills\skills\openproject\`,
token `~/.config/openproject/op.env`), so moving the *docs* does not affect agent operation. Only these
pointers need editing:
- `apex-meta/.../05-program-closeout/PLAN.md:38` (pilot canonical location) and `:85` (T18 `__MACOSX/` path).
- Leela root `AGENTS.md` "OpenProject agent skill" section; the cluster `README.md`'s internal relative links.
- Broken path to fix regardless: `openproject-cli-agent-handover.md:29` →
  `C:/GitDev/apexai-os-meta/docs/DUAL_INSTANCE_ARCHITECTURE.md` should be `…/ki-basis/docs/…`.

## 5. Sibling-repo infra map (the mental model these docs should describe)
| repo | key file | role |
|---|---|---|
| `ki-basis-shared` | `compose.yaml` (`name: ki-basis-infra`) | **the shared Postgres cluster** `ki-basis-shared-postgres` on external `shared-db-net`, no host port |
| `leela-op178` | `compose.shared-db.yaml` | private OpenProject 17.8 → `priv_openproject` on the shared cluster; `0.0.0.0:8083` |
| `lika-community` | `compose.wsl.yaml` (`name: community`) | live community stack (no local pg; joins `shared-db-net`, `comm_*` DBs) |
| `apexai-os-meta/ki-basis` | `compose.shared-db.yaml` (`-p ki-basis`) | live private stack (firefly/paperless/valkey/nginx/hermes) |

**Security flag (separate from doc currency):** `leela-op178/compose.yaml` and `compose.shared-db.yaml` carry a
**hard-coded literal `SECRET_KEY_BASE`** inline (committed, not sourced from `.env`). Worth remediating on its
own track (value not reproduced here).

## 6. Recommended remediation — tiered, operator-gated
Each tier is independent; do in order. Nothing here has been executed.

- **Tier 0 — kill the live hazard (§1).** Re-point `AGENT-OPERATING-CONTEXT.md §13` to ADR-002 §6 + the 03
  bundle; add a superseded banner to (or retire) `Alpine/ARCHITEKTUR-BASIS.md`. *Smallest, highest value.*
- **Tier 1 — banner/retire the un-bannered stale docs (§2).** Add a one-line "SUPERSEDED → see ADR-002 §6 /
  03 bundle" banner to each, or move clearly-dead ones to an `_archive/`. Fix `CURRENT-STATE.md` frontmatter to
  match its current body.
- **Tier 2 — de-duplicate (§3).** Pick ONE home for the dossier; replace the other copy with a pointer.
  Collapse the 3-copy spec: either re-sync the 2 mirrors now **and** stamp them "generated — edit canonical
  only," or (cleaner) delete the mirrors and leave a one-line pointer to canonical. Add the current-arch
  pointer banner to `GEMINI.md`/`.hermes.md`.
- **Tier 3 — fix the misplacement (§4).** Relocate `Leela-Cloud-2026/docs/ProjectMM/openproject/` into
  apexai-os-meta (natural home: beside `04-leela-mastery-openproject-consolidation/`), update the few pointers
  in §4.1, optionally leave a 3-line stub in Leela. Decide the reverse-misplaced BOT_WIRING doc.
- **Tier 4 — one canonical current-infra description.** Author a single `INFRASTRUCTURE.md` (current-state:
  engine, shared PG, all four stacks + sibling repos, ports, volumes, keepalive, T10 state) as THE description,
  and make every entrypoint point to it — ending the "six overlapping surfaces" problem.
- **Separate track — security:** move the hard-coded `SECRET_KEY_BASE` in `leela-op178` compose files into an
  `.env` (§5).

## 7. Definition of done
The live §13→ARCHITEKTUR-BASIS→compose.yaml hazard is gone; no doc asserts retired topology without a banner;
there is one authoritative current-infra description that entrypoints route to; general infra no longer lives
in the Leela product repo; the spec has one maintained source (no silent-drift mirrors). Nothing changed on
the live system.
