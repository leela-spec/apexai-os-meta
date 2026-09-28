# ⛔ THIS BRANCH IS SUPERSEDED — DO NOT MERGE

**Branch:** `codex/separate-community-stack` · **Status:** dead / historical only · **Marked:** 2026-09-28

## What this branch proposed
Split the community stack out of `ki-basis` into a standalone repo, with **per-stack Postgres**,
**Docker-Desktop** lifecycle, and **airtight "zero shared DB"** isolation (plus a `private-business`
standalone repo).

## Why it's superseded
That plan was **not taken**. What actually shipped (ADR-002, 2026-09-26) reaches the same separation a
different way and is **live and verified**:
- **One WSL2-native engine**, Docker Desktop retired.
- **One shared Postgres** (`ki-basis-shared-postgres`) with `comm_*` / `priv_*` databases + roles;
  cross-tenant `REVOKE CONNECT` (verified live: `comm_*` cannot reach `priv_*` DBs, and vice versa).
- Community **already is** its own repo: **`C:\GitDev\lika-community`** (live stack, `community-*` containers).
- `private-business` repo was never created; the private stack stays in `apexai-os-meta/ki-basis`.

## Where current truth lives
| Topic | Authoritative source |
|---|---|
| Architecture decision | `ki-basis/docs/DUAL_INSTANCE_ARCHITECTURE.md` **§6 (ADR-002)** |
| Consolidation record | `apex-meta/orchestration/architecture-improvements/03-wsl2-native-stack-consolidation/` |
| Live private compose | `ki-basis/compose.shared-db.yaml` (on `main`) |
| Community repo/stack | `C:\GitDev\lika-community/` |
| Full assessment | `apex-meta/.../05-program-closeout/FINDINGS-codex-community-stack-2026-09-28.md` (on `main`) |

## Salvage status
**Nothing to cherry-pick.** All added docs/tests describe the abandoned Docker-Desktop / two-repo /
per-stack-Postgres design. The 9 "deleted" scripts + `equinox-intake` skill are **safe** — present on
`main` **and** relocated into `lika-community`.

## ⚠️ Do NOT `git merge` this branch
A merge would **delete 9 live community scripts** from `ki-basis/main`. Keep parked as history, or delete
the branch — never merge.
