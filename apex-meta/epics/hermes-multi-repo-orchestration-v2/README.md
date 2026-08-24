# Hermes Multi-Repo Orchestration v2 — Operator & Agent Index

Status: **ARCHITECTURE DECISIONS ACCEPTED / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24  
Repository: `leela-spec/apexai-os-meta`  
Branch: `main`

## Authority order

Future agents must read in this order:

1. `README.md` — navigation and authority order.
2. `DECISIONS.md` — compact accepted/deferred decision ledger D01–D10.
3. `state.yaml` — machine-readable current state after the pending patch is applied.
4. `decisions/Dxx-*.md` — decision-specific reasoning/risk appendices.
5. `11-IMPLEMENTATION-ROADMAP.md` — phased implementation plan.
6. `12-RISK-REGISTER.yaml` — machine-readable operational risks.
7. `13-SOURCE-VERIFICATION-MATRIX.md` — claim-to-source verification grades.
8. `incidents/` — upstream/runtime incidents that constrain decisions.
9. `02-MASTEROFARTS-SOURCE-MIGRATION-MANIFEST.md` — pilot provenance that must survive re-homing.
10. `FUTURE-DEVELOPMENT.md` — explicitly deferred capabilities.

Independent pre-implementation validation launcher:

- `14-INDEPENDENT-PREIMPLEMENTATION-VALIDATION-HANDOVER.md` — adversarial handover/prompt for double/triple-checking the accepted architecture, tools, agent orchestration, risks, simulations, and current upstream contracts before implementation authorization.

The D02/D10 decision patch has landed. `README.md` is the current entrypoint and `state.yaml` is the current machine-readable state. Continue to use `patches/` for future edits to existing control files.

## Decision ledger and appendices

| ID | Decision | Status | Appendix |
|---|---|---|---|
| D01 | Apex AIOS Meta is the durable portfolio/control plane; project truth remains in source repos | ACCEPTED | `decisions/D01-APEX-CONTROL-PLANE.md` |
| D02 | Separate Hermes Kanban board per repo + asynchronous read-only Apex rollup | ACCEPTED | `decisions/D02-KANBAN-TOPOLOGY.md` |
| D03 | Reusable durable role profiles are reused sequentially across repos | ACCEPTED WITH CONSTRAINTS | `decisions/D03-REUSABLE-ROLE-PROFILES.md` |
| D04 | Raw memory stays profile-local; spillover happens through reviewed generalized skills | ACCEPTED WITH CONSTRAINTS | `decisions/D04-LEARNING-SPILLOVER.md` |
| D05 | Apex becomes canonical reviewed source for generic shared skills after a controlled promotion/deployment pilot | ACCEPTED DIRECTION / PILOT REQUIRED | `decisions/D05-SHARED-SKILL-SOURCE.md` |
| D06 | BMAD stays repo-local where needed; MarketingSkills remains MasterOfArts-only for now; Apex KB remains Apex-specific | ACCEPTED | `decisions/D06-BMAD-AND-DOMAIN-SKILLS.md` |
| D07 | Managed repos converge to one canonical WSL checkout each under a common workspace root | ACCEPTED / MIGRATION NOT AUTHORIZED | `decisions/D07-WSL-CANONICAL-WORKSPACE.md` |
| D08 | One local QMD engine serves curated cross-repo collections; every Hermes profile needing retrieval gets QMD MCP config | ACCEPTED / LIVE MULTI-PROFILE TEST PENDING | `decisions/D08-QMD-MULTI-REPO.md` |
| D09 | External shared-memory service is deferred until a measured built-in-memory gap exists | DEFERRED / ACCEPTED | `decisions/D09-EXTERNAL-MEMORY-DEFERRED.md` |
| D10 | Background autonomous multi-board execution stays disabled until current Kanban/Docker/concurrency failure modes are proven fixed on the installed Hermes version | DEFERRED SAFETY GATE | `decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md` |

## D10 incident

D10 is directly constrained by:

- `incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`

This incident record is separate from the decision appendix so that the decision can remain stable while upstream issue status changes over time.

## Existing subject files

The decision appendices do not replace the deeper subject research. They point back to it:

- `03-MULTI-REPO-EFFICIENCY-RISKS-AND-SAFETY.md`
- `04-KANBAN-TOPOLOGY-AND-APEX-ROLLUP.md`
- `05-REUSABLE-PROFILES-LEARNING-AND-MEMORY.md`
- `06-SHARED-SKILL-PROMOTION-AND-CRON.md`
- `07-APEX-CROSS-PROJECT-EXCHANGE-CONTRACT.md`
- `08-QMD-MULTI-REPO-RETRIEVAL.md`
- `09-WSL-CANONICAL-WORKSPACE-MIGRATION-PLAN.md`
- `10-BMAD-AND-DOMAIN-SKILL-POLICY.md`

## Patch law

Existing files are not directly edited during this decision-pack update.

Any required modification to an existing file must be represented under `patches/` using exact-match old/new blocks copied from the live file. New files may be written directly.

## Current implementation boundary

Accepted architecture does **not** equal implementation authorization.

Still forbidden until a separate implementation execution is authorized:

- repo migration/deletion;
- runtime reconfiguration;
- scheduler installation;
- autonomous background multi-board dispatch;
- raw memory synchronization;
- bidirectional task synchronization;
- external shared-memory service;
- custom global BMAD linker.
