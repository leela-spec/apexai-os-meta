# BRIEFING — 2026-09-22T10:20:00Z

## Mission
Deeply inspect current Docker configuration and volume layout in ki-basis, design decoupled Hermes runtimes, and construct a Zero-Data-Loss Docker Volume Protection Plan for all named ext4 volumes inside WSL2/Hyper-V DockerDesktop.vhdx.

## 🔒 My Identity
- Archetype: explorer
- Roles: Docker Infrastructure & Storage Explorer
- Working directory: C:\GitDev\apexai-os-meta\.agents\explorer_docker_r1
- Original parent: d1e6704c-b985-442c-9101-b651e4404d1a
- Milestone: Docker & Storage Architecture Investigation

## 🔒 Key Constraints
- Read-only investigation — do NOT implement changes to production / ki-basis files
- Write only to .agents/explorer_docker_r1/
- Produce evidence-backed analysis and 5-component handoff report

## Current Parent
- Conversation ID: d1e6704c-b985-442c-9101-b651e4404d1a
- Updated: not yet

## Investigation State
- **Explored paths**:
  - `ki-basis/compose.yaml`: Cataloged 7 services, 10 named volumes per stack, bridge network.
  - `ki-basis/.env.private`, `.env.community`, `.env`: Verified Port Band 808x vs 908x, secrets, tokens.
  - `ki-basis/scripts/verify_dual_isolation.py`: Executed successfully (32/32 tests passed).
  - `C:\ProgramData\DockerDesktop\vm-data\DockerDesktop.vhdx`: Verified exact physical disk existence (33,821,818,880 bytes).
  - `ki-basis/SOUL.md`: Discovered persona bleed (LikasKinkyBot currently mounted into both stacks).
  - `ki-basis/scripts/start-ki-basis.ps1`, `stop-ki-basis.ps1`, `backup-stack.sh`: Verified dual-stack control.
- **Key findings**:
  - Physical VHDX holds all persistent ext4 database tables and named volumes; Git holds only 680 KB declarative text.
  - Moving compose files to subdirectories or external workspaces without explicit volume binding will cause Docker Compose to use directory-prefixed volume names (e.g. `private_postgres_data`), spawning empty databases and causing perceived total data loss.
  - Using `external: true` with `name: <exact_existing_name>` provides mathematical guarantee of zero data loss and fail-closed protection against empty re-initialization and `docker compose down -v` destruction.
  - Hermes runtime currently has persona bleed in `compose.yaml` (bind mounts `./SOUL.md` and `./skills/equinox-intake` unconditionally). Decoupling requires dedicated mount points.
- **Unexplored areas**: None remaining for this mission scope.

## Key Decisions Made
- Confirmed Hyper-V DockerDesktop.vhdx location and size.
- Formulated mathematical proof for `external: true` volume preservation.
- Architected decoupled Hermes runtimes and copy-paste ready Compose templates and scripts.

## Artifact Index
- DISPATCH.md — Assignment instructions
- BRIEFING.md — Situational awareness
- progress.md — Liveness heartbeat
- handoff.md — Comprehensive 5-component deliverable
