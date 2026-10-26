Execute a Hermes runtime migration. First read apex-meta/AI-Snippets/AIFailure/HERMES-ARCHITECTURE-HISTORY-AND-DECISION.md for context, then follow apex-meta/orchestration/architecture-improvements/02-hermes-single-container-runtime/G0.2-MIGRATION-RUNBOOK.md exactly, gate by gate, running commands in WSL via wsl.exe. Verify each gate's check before continuing. Stop and ask me for the GitHub token at Gate 4 (or note it can be deferred). Stop at the final go/no-go. Never mount `/mnt/c` or any Leela repo. If any check fails, stop and use the Rollback section. 3. Have your GitHub token ready for Gate 4 (or tell it to defer the token).

I'll start by reading both documents to understand the context and the exact runbook I need to follow.

Read 2 files

Both documents are clear. Let me set up my task tracking and verify WSL access before starting Gate 0.

Verified WSL access, user, and docker availability

WSL is accessible as root, Docker 29.1.3 is available. Let me begin the migration.

## Gate 0 — Backup (safety net)

Gate 0: backup ~/.hermes and confirm docker

Gate 0 check passes — backup exists and Docker responds. But the backup directory **already existed** from a prior run. I need to check whether it's a stale/partial backup before relying on it as my rollback safety net, and whether a prior migration attempt left a container running.

Compared backup vs live state and listed all containers

Gate 0 findings are good:

- **Backup is valid and current** — `config.yaml` identical mtime (yesterday 22:50) in both, 5 boards in both live and backup. Safe rollback net.
- **Docker** responds.

I also see the **old Arch-2 split-setup sandbox containers**: twelve `nikolaik/python-nodejs` `sleep infinity` containers named `hermes-*` (4 running, 8 exited). These are exactly the separate ephemeral sandboxes Gate 1 tells me to stop. No container named `hermes` (the new one) exists yet.

**Gate 0 — PASS.**

## Gate 1 — Stop the old runtime

Failed to runGate 1: stop host-run hermes-agent

The `pkill -f "hermes-agent"` pattern matched my own wrapper shell (its command text contained "hermes-agent"), so the command self-terminated (exit 15) mid-run. I also now see the actual host runtime is **live and active**: a dashboard (PID 662), an MCP watchdog, a **TUI session** (PID 78095), and a **background dev server** (`npm run start -p 3101`, PID 70666) that host-Hermes launched.

Let me check the real current state cleanly — without putting the literal kill-pattern in my probe command — before completing Gate 1 deliberately.

Checked remaining host hermes processes and listeners

All host Hermes processes are now stopped (dashboard, MCP watchdog, TUI, and the dev server are gone) and nothing listens on 9119/8642/3101. Now I'll stop and remove the **old Arch-2 split-setup sandbox containers** (the `nikolaik/python-nodejs` `sleep infinity` ones). These are exactly what Gate 1 says to clear. None of them is the new `hermes` container (which doesn't exist yet).

Gate 1: remove old sandbox containers

**Gate 1 — PASS.** Host Hermes processes stopped, and all 12 old sandbox containers removed. No containers remain.

## Gate 2 — Configure for the container runtime

I need to make an exact-match edit to `terminal.backend`. Let me read the current config first.

Inspected terminal.backend in config.yaml

Exactly one `backend:` line: `backend: docker` at line 16 under `terminal:`. I'll make a precise, anchored exact-match replacement (only that line can match).

Gate 2: set terminal.backend to local

**Gate 2 — PASS.** `backend: local`, other keys untouched.

## Gate 3 — Launch Hermes as ONE container

Before launching, I must verify the mount source `/root/workspaces` contains **only the 4 canonical repos and no Leela repo** — since the mount is `/root/workspaces:/root/workspaces`, anything in that dir gets mounted. I'll also confirm the image is available.