# Architectural Consensus & Zero-Data-Loss Workspace Isolation Plan

## Objective
Execute an exhaustive multi-perspective architectural research run with an independent multi-agent consensus team to converge on the definitive architecture for isolating AI agent workspaces, instruction files (AGENTS.md, SOUL.md), and Docker environments between Community Operations (Safer Space e.V. / Equinox / @LikasSlave_bot) and Private Business, with 100% Docker ext4 volume preservation.

## Phases

### Phase 1: Survey & Multi-Perspective Research Dispatch (Parallel)
Dispatch 3 specialized Explorers to independently research and benchmark the four candidate architectural topologies (Subfolder separation, Decoupled standalone directories outside repo, Workspace profile switching, Git worktrees/multi-root):
1. **Explorer 1 (Security & Isolation Specialist)**: Evaluates OWASP Top 10 for AI Agents (context poisoning, prompt injection, cross-tenant data exfiltration), zero context bleeding, persona leakage risks between `@LikasSlave_bot` and Executive Business persona.
2. **Explorer 2 (Antigravity & DX Specialist)**: Evaluates Antigravity workspace root mechanisms, prompt injection overhead, token consumption, cognitive load, switching friction, Git hygiene, and editor ergonomics.
3. **Explorer 3 (Docker Infrastructure & Storage Specialist)**: Analyzes current `ki-basis` Docker Compose files, named ext4 volumes inside WSL2/Hyper-V `DockerDesktop.vhdx` (PostgreSQL, Paperless, OpenProject, Firefly III ~33.4 GB), Compose project namespaces, and port band allocations (808x vs 908x).

### Phase 2: Synthesis & Convergence into Architecture Blueprint
Orchestrator synthesizes findings from all 3 Explorers, resolving trade-offs, building the objective multi-criteria comparison matrix, defining the Hermes dual-runtime specs, and producing the mathematical Docker volume preservation mapping.

### Phase 3: Deliverable Authoring via Worker
Dispatch `teamwork_preview_worker` to author comprehensive documentation in `ki-basis/docs/` and operator templates/scripts:
- `ki-basis/docs/workspace-isolation-architecture.md`: Full architectural report, benchmarks, OWASP evaluation, consensus decision.
- `ki-basis/docs/docker-volume-preservation-plan.md`: Zero-data-loss ext4 volume mapping, compose project names, migration commands, and Hyper-V VHDX safety guarantees.
- `ki-basis/docs/hermes-dual-runtime-spec.md`: Independent container configurations, port allocations, environment isolation, persona/skill separation.
- Operator templates & scripts: clean, copy-paste ready `AGENTS.md`, `README.md`, `start.ps1`, `stop.ps1`, and verification scripts.

### Phase 4: Review, Adversarial Challenge, and Forensic Integrity Audit
1. Dispatch `teamwork_preview_reviewer` to verify completeness against all requirements R1-R4 and acceptance criteria.
2. Dispatch `teamwork_preview_challenger` to stress-test the volume preservation mapping, port collisions, and token leakage vectors.
3. Dispatch `teamwork_preview_auditor` for binary forensic integrity audit (no hardcoded cheats, authentic volume mappings, valid syntax).

### Phase 5: Synthesis, Handoff, and Completion Reporting
Compile final gate status, write `handoff.md`, and report back to parent Sentinel (`b88167dc-532c-495e-b142-b418b38f5188`).
