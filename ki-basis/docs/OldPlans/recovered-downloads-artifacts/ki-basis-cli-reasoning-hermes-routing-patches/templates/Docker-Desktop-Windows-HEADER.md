# Docker Desktop Windows — Research Input and Current Disposition

> **Status:** NON-AUTHORITATIVE RESEARCH INPUT / provenance preserved.  
> **Runtime authority:** `ki-basis/compose.yaml`, live runtime behavior, `ARCHITEKTUR-BASIS.md`, and `04A-DOCKER-BACKGROUND-RUNTIME.md`.

## Current disposition

The supplied analysis correctly motivates avoiding unnecessary Docker Desktop Dashboard/UI use and measuring host overhead before per-service tuning.

Technical clarification:

- Current supported target: Docker Desktop **background runtime** + Hyper-V Linux VM + Docker Engine, Dashboard closed.
- Not equivalent: fully quit/stop Docker Desktop and expect its Linux Docker Engine to continue independently.
- True no-Desktop Linux Engine: separate Linux VM + independently managed Docker Engine, which would be a runtime migration.

Adopted now:

- CLI-first/background operation;
- Dashboard closed/not auto-opened;
- control-plane restart guard after sleep/resume failures;
- measure before service-level tuning;
- no `.wslconfig` on the Hyper-V target.

Not adopted now:

- manual Linux-VM migration solely to remove the Dashboard;
- Windows-native `dockerd.exe` for the Linux stack;
- speculative worker/memory/Postgres/Valkey tuning.

---

## Original supplied analysis

