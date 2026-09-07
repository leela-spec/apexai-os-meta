# Plan: ki-basis Dual-Instance Separation & Architecture

## Objective
Architect, benchmark, and evaluate dual-instance separation for `ki-basis` infrastructure across private entrepreneurship and community operations, resolving WSL2/9p performance degradation, crash loops, and port collision risks.

## Phases

### Phase 0: Survey & Codebase Exploration
- Dispatch 3 Explorers:
  - Explorer 1 (Spec Miner): Extract requirements from ORIGINAL_REQUEST.md, identify all constraints, acceptance criteria, metrics, and contracts.
  - Explorer 2: Deep dive into existing `ki-basis` compose files, services (OpenProject, Hermes, Paperless, Firefly, PostgreSQL, Valkey, etc.), environment variables, volumes, ports, and entrypoints in `C:\GitDev\apexai-os-meta`.
  - Explorer 3: Deep dive into WSL2, storage architecture (9P vs ext4, named volumes), crash logs (OpenProject exit status 1), and headless container configurations.
- Synthesize into `PROJECT.md` (§ Architecture, § Feature Inventory, § Milestones, § Interface Contracts, § Code Layout).

### Phase 1: R1 Performance Diagnosis & Storage Architecture
- Analyze root causes of OpenProject exit status 1 crash loop and high CPU in WSL2.
- Configure ext4 native storage, Docker named volumes, and non-interactive headless runtime parameters.
- Benchmark and verify idle CPU (<5%) and stability.

### Phase 2: R2 Dual-Instance Isolation Architecture
- Design independent Compose projects: `ki-basis-private` vs `ki-basis-community`.
- Network isolation: Dedicated bridge networks, no cross-stack DNS or routing.
- Port bands: Non-overlapping port assignments (Private 8080-8089, Community 9080-9089).
- Segregated storage: Separate databases, Valkey instances, Paperless data, Firefly uploads.
- Implementation & Verification: Worker implements compose configs/env templates, Reviewers & Challengers verify zero collision and isolation.

### Phase 3: R3 Multi-Engine vs Multi-Project Strategy Evaluation
- Empirical and architectural comparison: Strategy A (Dual Compose Projects on Single Engine) vs Strategy B (Dual Daemon Split).
- Address WSL2 `localhostForwarding`, memory/CPU overhead, maintenance complexity, operational tradeoffs.
- Recommendation matrix and decision criteria.

### Phase 4: Verification, Runbook & Final Audit
- Create comprehensive operational runbook (migration, daily operations, backup/restore, maintenance).
- Independent Reviewer and Challenger verification across all acceptance criteria.
- Forensic Integrity Audit (`teamwork_preview_auditor`).
- Final synthesis and reporting to Sentinel.
