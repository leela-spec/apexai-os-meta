---
type: Handover
title: Program close-out — continue the remaining (deferred / optional / gated) tasks
description: The close-out program is substantially complete. This hands the small set of remaining items to the next chat, each with its status, gate, exact next action, and pointers. Nothing here is blocking; all are operator-decision, deferred, or optional.
created: 2026-09-28
status: open
owner: (next chat)
authority_order: "live runtime + code > accepted decisions/ADRs > this handover. Surface conflicts; never invent a winner."
parent_plan: apex-meta/orchestration/architecture-improvements/05-program-closeout/PLAN.md
---

# Continue the remaining close-out tasks

## What is already DONE (do not redo — verified this session, all pushed)
- **Buckets 0–2:** consolidation committed; doc-truth reconciled; infra soak green (T08/T09/T11); T10 inspected.
- **Bucket 3 (pilot):** handovers reconciled (T12), 17.8 runbook (T17), cruft cleanup (T18). T13/T16 deferred; T14 cancelled (demos stay).
- **Bucket 4 (T19):** browser keepalive done (05); Mastery taxonomy — `MoA-Content`/`MoA-Business`/`ApexAI-OS` created under `Leela & Mastery` id 4 (06); skill-standardization + agent-invocation proven (07/T15).
- **Canonical agent-skill architecture:** one source `C:\GitDev\agent-skills\` (private GitHub `leela-spec/agent-skills`), linked into every agent's global dir; token at `~/.config/openproject/op.env`; client hardened (atomic config + host guard). Reasoning: `agent-skills/README.md`, `research/FINDINGS.md`, `research/LEARNINGS.md`, and `Leela-Cloud-2026/docs/ProjectMM/openproject/DECISION-2026-09-28-canonical-skill-architecture.md`.
- **T15 done:** Codex (`axelg`), Claude (`AOG`), and Antigravity (`agy`) all autonomously invoke the canonical skill (live Prompt-A runs).

## Remaining items

### R1 — Finish the 5-account coverage (T07 optional) · gate: none (read-only)
- **Second accounts STILL OPEN:** **`agehm` (Claude)** and **`alexg` (Codex)**. Tested so far: `AOG` (Claude), `axelg` (Codex), + Antigravity.
- **Do:** in a fresh session of each, paste Prompt A (below); confirm it auto-invokes the skill and returns WP#38 (subject "User-story census — Stage-4 coverage closure verification", status Closed). If an account overrides its config dir (`CLAUDE_CONFIG_DIR` / a Codex profile with a different `HOME`), create the per-skill link in that dir too (Windows junction + WSL symlink to `C:\GitDev\agent-skills\skills\openproject`).
- **Also:** confirm whether **Antigravity multi-account** is even supported (undocumented) — or record it unsupported.
- **Prompt A:** `On the private Leela OpenProject instance, what are the subject and current status of work package 38? Please show how you retrieved it.`
- Record results in `04-…/07-handover-5account-skill-standardization-test.md`.

### R2 — Least-privilege OpenProject identity (T13) · gate: human-approval (admin + credential) · DEFERRED
- Replace the admin API token with a dedicated non-admin, project-scoped user. Operator deferred 2026-09-28 (trusted agents, single-user local). Revisit when autonomy/exposure grows.
- **Recipe + revisit triggers:** `Leela-Cloud-2026/docs/ProjectMM/openproject/FUTURE-DEVELOPMENT-least-privilege-agent-identity.md` (Item 1). The credential/account steps are operator-run.

### R3 — Write-autonomy policy (T16) · gate: operator-decision · DEFERRED
- Decide which write classes agents may run without per-action `--confirmed`; promote `agent-skills/skills/openproject/references/write-policy.md` from provisional to accepted. Operator deferred 2026-09-28 (keep confirm-everything default).
- **Decision matrix:** same FUTURE-DEVELOPMENT doc (Item 2).

### R4 — Hermes compose-drift (T10) · gate: human-approval · DEFERRED/GATED
- `ki-basis/compose.yaml` declares named volumes but live `ki-basis-hermes` runs bind mounts (`/root/.hermes` 4.4 GB + `/root/workspaces` 3.5 GB ≈ 7.9 GB). **Do NOT `docker compose up` on `ki-basis/compose.yaml`** — a naive up recreates hermes on empty volumes and wipes bot state (D-16). Live stack runs from `compose.shared-db.yaml`. Fix needs a deliberate operator-chosen migration. Evidence: `EVIDENCE-infra-soak-2026-09-28.md`. **A dedicated, research-first handover exists for exactly this → `HANDOVER-t10-hermes-compose-drift.md`** (has the verified ground truth for both Hermes and explicit anti-overcorrection rules — use it).

### R5 — `codex/separate-community-stack` branch · PARKED (keep)
- Investigation concluded **keep parked, do NOT `git merge`** (a merge would delete 9 live community scripts). Community already works consolidated and is its own repo (`lika-community`). Full analysis: `FINDINGS-codex-community-stack-2026-09-28.md`. Only delete the branch if the operator later says so, and only if nothing is merged first.

## Environment & safety (for whoever continues)
- **One WSL2-native "Apex" Docker engine** (Docker Desktop retired, ADR-002). Run docker via `wsl -d Ubuntu -u root -- docker …`; prefix `/mnt/c` commands with `MSYS_NO_PATHCONV=1`; pipe binary-ish output `| tr -d '\0'`.
- **Node:** WSL `/home/gehma/nodejs/bin/node`; Windows `…\ApexNode\…\node.exe`.
- **OpenProject skill:** canonical `C:\GitDev\agent-skills\skills\openproject\`; token auto-loads from `~/.config/openproject/op.env`; operate via the skill/API, never the browser.
- **Secrets — never print/commit:** `~/.config/openproject/op.env`, `C:\GitDev\ki-basis-shared\.env`, `C:\GitDev\leela-op178\op.env`, community bot `.env`.
- **Gates:** any `git push`, project/data deletion, `wsl --shutdown`, or `docker compose up` on `ki-basis/compose.yaml` requires explicit operator approval. Verify after every write.

## Pointers
- Master plan (statuses in place): `PLAN.md` (this bundle).
- Pilot hub: `Leela-Cloud-2026/docs/ProjectMM/openproject/README.md`.
- Canonical skill: `C:\GitDev\agent-skills\README.md`.
