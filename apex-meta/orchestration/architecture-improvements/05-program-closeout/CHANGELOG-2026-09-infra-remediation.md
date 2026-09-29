---
type: Changelog
title: Infra work log — T10 Hermes drift + infra-docs remediation (Sept 2026)
description: >
  Single index of what changed, why, how, and where it is recorded, for the two Sept-2026 infrastructure
  efforts — the T10 Hermes compose-drift fix and the infra-documentation remediation (R1–R7). Includes every
  commit hash across both repos, links to the detailed records, and the current canonical entrypoint.
created: 2026-09-29
canonical_current_state: ki-basis/docs/INFRASTRUCTURE.md
principle: "Every change here was gated per-step: intent-checked vs the LIVE system, independently adversarial-reviewed, health-tested (infra-health-test.sh GREEN 29/29), committed atomically, and is git-reversible."
---

# Infra work log — September 2026

**Read `ki-basis/docs/INFRASTRUCTURE.md` for the current state.** This file explains how we got there.
All work verified against the live system; nothing on the running stack was changed except the two guarded
lifecycle scripts and the compose.yaml text edits in T10 (the live containers were never recreated).

## Effort 1 — T10: Hermes compose-drift (data-loss risk) → resolved
**What:** the checked-in `ki-basis/compose.yaml` declared **named volumes** for Hermes, but the live
`ki-basis-hermes` runs on **bind mounts** (~7.9 GB of bot state). A `docker compose up` on that file (which the
old `start-ki-basis.*` scripts actually did) would have recreated Hermes onto empty volumes and **wiped** the
state.
**Why:** remove the data-loss landmine with the smallest safe change; do not disturb the working system.
**How:** backed up + restore-proved 7.9 GB first; edited `compose.yaml`'s Hermes stanza to the live bind
mounts; added fail-closed guards to the stale `start-/stop-ki-basis.{sh,ps1}`; wrote correct
`start-/stop-ki-basis-shared-db.ps1`. Live container never recreated.
**Commits (apexai-os-meta / main):** `4d1e852a` (fix + guards + FINDINGS-t10), `f4efb436` (correct start/stop scripts).
**Records:** `HANDOVER-t10-hermes-compose-drift.md`, `FINDINGS-t10-hermes-compose-drift-2026-09-28.md` (§9 execution record).

## Effort 2 — Infra-docs remediation (R1–R7) → done; SEC open
**Why:** infra docs were scattered/duplicated/stale, one routing chain led agents to retired+dangerous truth,
and shared-infra docs lived in the Leela product repo. Root cause: no single source of truth.
**How:** audited (3 read-only agents) → ranked + dependency-ordered plan → executed each tier gated.

| step | what changed | commit(s) |
|---|---|---|
| audit + plan + tests | read-only audit, ranked plan, 2 saved re-runnable tests | `0af38fb0` |
| **R1** | live hazard fixed: `AGENT-OPERATING-CONTEXT §13` repointed off retired `ARCHITEKTUR-BASIS.md`/`compose.yaml`; that file bannered SUPERSEDED | `d0fafc5c` |
| **R2** | **created the single source of truth `ki-basis/docs/INFRASTRUCTURE.md`** (built from the live system + ADR-002) | `99b335c4` |
| **R3** | 6 stale docs bannered → point to INFRASTRUCTURE.md | `d5707786` |
| **R4** | OpenProject shared-infra cluster (197 files) moved out of the Leela product repo → `ki-basis/docs/openproject/`, refs repointed, broken link fixed, redirect stub left | apexai `93700253` + `c99a3571`; **Leela-Cloud-2026/master `4e9a48a4`** |
| **R5** | fixed spec-mirror drift (reversal banner added to both `01_DUAL_INSTANCE_ARCHITECTURE.md` mirrors) | `a5d64e1f` |
| **R6** | pre-2026-09-26 Docker-Desktop-era history bannered as SUPERSEDED HISTORY | `a5d64e1f` |
| **R7** | pointers wired: `GEMINI.md`/`.hermes.md` current-infra banner; `BOT_WIRING…` scoped to community; `CURRENT-STATE.md` `current:` → INFRASTRUCTURE.md | `a5d64e1f` |
| plan status | remediation plan marked R1-R7 done + execution log | `2ff0c8e9` |

**Records:** `FINDINGS-infra-docs-audit-2026-09-28.md` (the audit), `PLAN-infra-docs-remediation-2026-09-28.md`
(ranked plan + §8 execution log), `tests/infra-health-test.sh`, `tests/doc-integrity-lint.sh`.

## Open item
- **SEC** — OpenProject `SECRET_KEY_BASE` sits inline in `leela-op178`'s two compose files. Verified
  **low-urgency**: `leela-op178` is not a git repo, so the secret is local-only (not committed/exposed).
  Handover: `HANDOVER-SEC-openproject-secret-2026-09-29.md`. "Leave as-is" is acceptable; if moved, the value
  must stay byte-for-byte identical (changing it logs everyone out).

## Where things live now (quick map)
- **Current infra description (start here):** `ki-basis/docs/INFRASTRUCTURE.md`
- **Why/decisions:** `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` §6 (ADR-002) + `03-…/02-decisions-log.md` (D-01…D-18)
- **OpenProject infra docs:** `ki-basis/docs/openproject/` (moved here from the Leela repo, R4)
- **Repos:** apexai-os-meta (`main`) = infra/meta; Leela-Cloud-2026 (`master`) = Leela product (now clean of infra);
  siblings `ki-basis-shared`, `leela-op178`, `lika-community` (not git repos except lika-community).
- **Tests to re-verify anytime:** `…/05-program-closeout/tests/`.
