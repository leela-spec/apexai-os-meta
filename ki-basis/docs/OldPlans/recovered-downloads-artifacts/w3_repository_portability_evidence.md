# W3 — Repository Portability & Configuration Hardening Evidence

**Timestamp:** 2026-09-02T14:08:00+02:00  
**Phase:** W3 (Correct repository configuration for portability & independent target)  
**Status:** PASS  
**Compose Render:** 100% Validated on Windows Docker Desktop

---

## 1. Summary of Applied Corrections

### A. Plan Authority Canonicalization
- Preserved the active Antigravity implementation plan family in `apex-meta/Alpine/ImplementationPlans/`:
  - `00-START-HERE.md`
  - `01-META-IMPLEMENTATION-PLAN-ANTIGRAVITY.md` through `09-INTEGRATION-ACCEPTANCE-ANTIGRAVITY.md`
- Removed the 9 obsolete generic plan files (`00-META-IMPLEMENTATION-PLAN.md`, etc.) that duplicated execution authority.
- Repaired relative documentation links to orchestrator skill paths.

### B. Current Architecture Truth
- Updated `apex-meta/Alpine/ARCHITEKTUR-BASIS.md` to document the active runtime authority:
  - Windows 11 with Docker Desktop (Hyper-V backend).
  - Single dedicated ki-basis Docker Engine.
  - 7 canonical services on `ki-basis-net`.
  - Immutable sha256 image pinning.
  - Target-local persistence.

### C. Secret Hardening & Fail-Closed Guardrails
- Added `/ki-basis/.env` to `.gitignore`.
- Rendered required secrets in `compose.yaml` with fail-closed `${VAR:?VAR is required}` assertions.
- Removed hardcoded default passwords from `ki-basis/docker/postgres/init/01-init-databases.sh`.
- Sanitized `ki-basis/.env.example` so secret fields are blank.
- Generated local target `ki-basis/.env` (ignored by Git) containing the active parameters.

### D. Immutable Image Digest Pinning
All 7 services pinned to their exact verified source image digests:
- `postgres`: `pgvector/pgvector@sha256:ccc6e83d6e35e931dc7c5def2022729d5a6c370318d099181995567ff1fb4d6b`
- `valkey`: `valkey/valkey@sha256:f110e5df168de4cdbd17afec848c6efe88e4b5e51c5b1ec6109de0c1b6a0c60b`
- `firefly`: `fireflyiii/core@sha256:ae69fdd95cdef9038cd7a460a5aec731f14813973e4f096511d5a4ea9ff0e972`
- `paperless`: `ghcr.io/paperless-ngx/paperless-ngx@sha256:5ab4f4f9bb099a36bec3e092906ea3e611323c5f18dc5cc38c76a1d540bdca9c`
- `openproject`: `openproject/openproject@sha256:73d4ee76fb3edb33b0eb1a3a2ddc036f0a45f9083459f445e3d0b634044cf8fb`
- `nginx`: `nginx@sha256:65645c7bb6a0661892a8b03b89d0743208a18dd2f3f17a54ef4b76fb8e2f2a10`
- `hermes`: `nousresearch/hermes-agent@sha256:09d743f5e012e41503829d06ca129c7d3e87ea3f943f7228d520c5c53c6f7db5`

### E. Hermes Host Decoupling
- Replaced old WSL host mounts (`/root/.hermes`, `/root/workspaces`) with target-local persistent volumes:
  - `hermes_data` (`ki-basis-hermes-data`) -> `/opt/data`
  - `hermes_workspaces` (`ki-basis-hermes-workspaces`) -> `/root/workspaces`
- Removed unused/orphan `openproject_data` volume declaration.

### F. Verification Tooling
- Added `ki-basis/scripts/verify-stack.sh`.

---

## 2. G3 Acceptance Result
- `docker compose --env-file .env config` executed cleanly on Windows Docker Desktop target Engine without any WSL path dependencies.
