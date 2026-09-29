---
okf_version: "0.2"
type: decision-record
title: OpenProject pilot — execution reconciliation (what was actually accepted vs. the handovers)
description: Records that the operator executed the DRAFT plan directly, chose a portable custom API-v3 skill over the upstream CLI, and chose a fresh 17.8 install over an in-place upgrade; reconciles the two pilot handovers and the draft's Phases A–H with reality.
tags: [openproject, antigravity, codex, pilot, decision, reconciliation]
status: accepted
date: 2026-09-28
decides_for:
  - openproject-cli-antigravity-pilot/HANDOVER.md
  - openproject-cli-antigravity-pilot/DRAFT-IMPLEMENTATION-PLAN.md
  - openproject-windows-agent-integration-v2/HANDOVER.md
program_ref: apexai-os-meta/apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md (T12)
---

# Pilot execution reconciliation (2026-09-28)

The OpenProject agent-integration pilot was **executed and proven** (read+write against the private
17.8 instance; census Work Package #38 created and reread). The path taken diverges from what the two
handovers and the draft plan prescribed. This record makes the actual, accepted path authoritative and
marks the superseded prescriptions, so no future agent re-runs the abandoned route.

## Decisions accepted (what actually happened)

### DR-1 — DRAFT plan executed directly; the required `IMPLEMENTATION-PLAN.md` is waived
The antigravity-pilot handover required a separately authored, independently reviewed
`IMPLEMENTATION-PLAN.md` before implementation (`required_deliverable: IMPLEMENTATION-PLAN.md`). The
operator instead executed `DRAFT-IMPLEMENTATION-PLAN.md` directly. **The `IMPLEMENTATION-PLAN.md`
deliverable is waived** — it will not be produced. The DRAFT plus this record and the skill itself are
the pilot's authoritative artifacts.

### DR-2 — Portable custom API-v3 skill chosen over the upstream OpenProject CLI route
The handover's preferred integration was the pinned upstream `openproject-cli` + upstream
`openproject-workpackage-crud` Agent Skill (DRAFT Phase B). That route was **rejected in execution** —
the released CLI (verb-first v0.5.5) and the skill (noun-first) never formed a stable matched pair on
Windows. Instead a **portable, self-contained Node API-v3 skill** was built at
`.agents/skills/openproject/` (`SKILL.md` router + `client/opCall.js`/`opClient.js`), discovered
natively by Antigravity and Codex (Claude Code via the `.claude/skills/openproject` junction). It
implements the needed operations directly against the OpenProject API v3 with a two-phase write gate
and identity/fingerprint verification (see `references/write-policy.md`, `references/operations.md`).

### DR-3 — Fresh 17.8 install chosen over in-place major-version upgrade
Parent-handover decision D3 accepted "upgrade private OpenProject to latest stable Community (17.8)",
and DRAFT Phase D designed a sequential `14 → 15 → 16 → 17` in-place upgrade with restore testing. In
execution the operator instead stood up a **fresh 17.8 install** (`leela-op178-openproject`, on the
shared WSL2 Postgres cluster) and **retired the old v14** (`ki-basis-openproject`, later fully deleted
— see apexai-os-meta consolidation D-05/D-18). The staged in-place upgrade path is **moot**.

## DRAFT Phases A–H disposition

| Phase | Prescription | Disposition |
|---|---|---|
| A — baseline | Antigravity surface + skill path + target identity | **done** — `agy` 1.1.15; skill at `.agents/skills/openproject/`; private 17.8 target fingerprinted. |
| B — pin upstream CLI/skill pair | offline-pin upstream `op` + upstream skill | **moot/superseded** (DR-2) — replaced by the portable custom API-v3 skill. |
| C — discovery + one read | fresh-session discovery + one verified read | **done** — skill discovered; read proven against the private 17.8 instance. |
| D — in-place upgrade 14→17 | sequential majors with restore test | **moot/superseded** (DR-3) — fresh 17.8 install; v14 retired/deleted. |
| E — dedicated identity + bounded write | least-priv identity + reread-verified writes | **partially done** — write proof done (WP #38, reread). **Open:** dedicated least-privilege identity not yet created; pilot still uses the admin token → program **T13**. |
| F — resolve required capability gaps | open retained handlers only as needed | **addressed by DR-2** — the custom skill implements the required ops (wp/project/relation/attach/type); open only if a specific accepted outcome needs more. |
| G — one real task + fresh-session resume | route a real WP + resume cold | **substantially done** — demonstrated by census WP #38. Fresh-session/cross-agent generalization proof → program **T15**. |
| H — write-autonomy policy + generalization | operator picks per-class autonomy; generalize | **open** — write-policy is provisional (all mutations confirmed) → program **T16**; Codex/Antigravity generalization → program **T15**. |

## Still open (routed to the program close-out plan)
- **T13** — create the dedicated least-privilege Leela identity; replace the admin token (DR-2/Phase E).
- **T15** — prove agent-initiated (not hand-run) invocation on Antigravity + Codex (Phase G/H generalization).
- **T16** — operator decision on write-autonomy classes; promote `write-policy.md` from provisional to accepted (Phase H).
