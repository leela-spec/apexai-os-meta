# Original User Request

## 2026-09-07T08:29:59Z

Architect, benchmark, and evaluate dual-instance separation for `ki-basis` infrastructure across private entrepreneurship and community operations, resolving the WSL2/9p performance degradation, crash loops, and port collision risks.

Working directory: C:\GitDev\apexai-os-meta

## Requirements

### R1. Performance Diagnosis & Storage Architecture
Resolve the empirical performance bottleneck observed in Ubuntu WSL2 (350% CPU usage, OpenProject crash loop `exit status 1`, 9P filesystem latency on `/mnt/c`). Establish native ext4 volume configurations and proper non-interactive headless container runtime parameters.

### R2. Dual-Instance Isolation Architecture
Design an airtight, battle-proven isolation model between Private Entrepreneurship and Community operations:
- Independent Docker Compose project namespaces (`ki-basis-private` vs. `ki-basis-community`).
- Fully isolated Docker bridge networks preventing inter-stack routing and DNS discovery.
- Non-overlapping port assignment mapping (e.g. Private on 8080–8089, Community on 9080–9089).
- Completely segregated PostgreSQL databases, Valkey instances, Paperless data, and Firefly uploads.

### R3. Multi-Engine vs. Multi-Project Strategy Evaluation
Provide an evidence-based comparison between:
- **Strategy A (Dual Compose Projects on Single Engine)**: Running both instances in Docker Desktop or native WSL2 with project namespaces (`-p`), distinct `.env` files, and port bands.
- **Strategy B (Dual Daemon Split)**: Running Private in Ubuntu WSL2 (native dockerd on ext4) and Community in Windows Docker Desktop (Alpine LinuxKit), accounting for WSL2 `localhostForwarding` conflicts.

## Acceptance Criteria

### Performance & Stability
- [ ] OpenProject, Hermes, Paperless, and Firefly all reach healthy status with steady-state CPU under 5% at idle.
- [ ] All database and persistent volumes reside on native ext4/named Docker volumes rather than 9P Windows mounts.

### Isolation Verification
- [ ] Both instances can run concurrently without port binding errors.
- [ ] Zero shared database tables or volume mounts across private and community stacks.
- [ ] Comprehensive migration and daily operation runbook for both entities.
