# Hermes Multi-Repo Orchestration v2 — Decision Ledger

Status: **CURRENT DECISIONS / IMPLEMENTATION NOT AUTHORIZED**  
Date: 2026-08-24

This file records **what was decided**. It intentionally does not duplicate full reasoning. Each decision links to a separate appendix containing forces, evidence, risks, shortcomings and watch conditions.

## D01 — Apex control plane

**Status:** ACCEPTED  
**Decision:** `leela-spec/apexai-os-meta` is the durable portfolio/orchestration control plane. Managed repositories remain the canonical owners of their own project truth and files.  
**Appendix:** `decisions/D01-APEX-CONTROL-PLANE.md`

## D02 — Kanban topology

**Status:** ACCEPTED 2026-08-24  
**Decision:** use one separate Hermes Kanban board per managed repository (`apex`, `masterofarts`, `acim`, `investment`) plus an asynchronous deterministic **read-only** rollup into Apex. Do not use tenants as the repo-isolation mechanism. Do not duplicate all source tasks into Apex.  
**Appendix:** `decisions/D02-KANBAN-TOPOLOGY.md`

## D03 — Reusable role profiles

**Status:** ACCEPTED WITH CONSTRAINTS  
**Decision:** roles such as `research-strategist` and `independent-reviewer` are durable Hermes profiles reused across repositories. Initial v2 reuses the same writable profile **sequentially**, not concurrently across repo workers.  
**Appendix:** `decisions/D03-REUSABLE-ROLE-PROFILES.md`

## D04 — Learning spillover

**Status:** ACCEPTED WITH CONSTRAINTS  
**Decision:** raw profile memory remains local to the profile. Project facts remain in their source repo. Cross-repo/cross-role spillover occurs only through reviewed generalized procedures promoted as skills.  
**Appendix:** `decisions/D04-LEARNING-SPILLOVER.md`

## D05 — Shared-skill source

**Status:** ACCEPTED DIRECTION / PILOT REQUIRED  
**Decision:** after a live promotion/deployment pilot, Apex becomes the canonical Git source for reviewed project-neutral shared skills. Runtime learned-skill scratch state stays separate from the canonical reviewed source.  
**Appendix:** `decisions/D05-SHARED-SKILL-SOURCE.md`

## D06 — BMAD and domain-specific skills

**Status:** ACCEPTED  
**Decision:** BMAD remains project-local wherever used. MarketingSkills remains MasterOfArts-only until another repo has a real requirement. Apex KB remains Apex-specific. Do not invent a global BMAD linker or globalize irrelevant domain skills.  
**Appendix:** `decisions/D06-BMAD-AND-DOMAIN-SKILLS.md`

## D07 — Canonical WSL workspace

**Status:** ACCEPTED / MIGRATION NOT AUTHORIZED  
**Decision:** converge each managed repo to one canonical WSL-native checkout under a common workspace root. Windows accesses those same files through WSL interop. Migration is one repo at a time with divergence audit and rollback; old Windows copies are not automatically deleted.  
**Appendix:** `decisions/D07-WSL-CANONICAL-WORKSPACE.md`

## D08 — QMD multi-repo retrieval

**Status:** ACCEPTED / LIVE MULTI-PROFILE ACCEPTANCE PENDING  
**Decision:** use one local QMD engine with curated named collections spanning managed repositories. QMD collection selection is explicit per task. Every Hermes profile that needs QMD gets the QMD MCP declaration; project truth remains in Git repos, not the QMD index.  
**Appendix:** `decisions/D08-QMD-MULTI-REPO.md`

## D09 — External shared memory

**Status:** DEFERRED / ACCEPTED  
**Decision:** do not add an external shared-memory service until role-local memory + repo truth + QMD + reviewed skill promotion demonstrates a measured insufficiency.  
**Appendix:** `decisions/D09-EXTERNAL-MEMORY-DEFERRED.md`

## D10 — Background multi-board autonomy

**Status:** DEFERRED SAFETY GATE  
**Decision:** do not enable autonomous background dispatch across multiple repo boards in initial v2. Reconsider only after the installed Hermes version passes explicit tests for task-workspace host persistence, mount/cwd agreement, bounded sandbox scope, and machine-wide same-profile concurrency behavior.  
**Appendix:** `decisions/D10-BACKGROUND-MULTI-BOARD-AUTONOMY.md`  
**Incident:** `incidents/INC-001-HERMES-KANBAN-DOCKER-WORKSPACE-CONCURRENCY.md`

## Decision invariants

These rules apply across D01–D10:

- one repository's project facts do not become another repository's truth through memory synchronization;
- no project-content mirroring into Apex merely for orchestration visibility;
- no raw profile-memory synchronization;
- no bidirectional task synchronization in the first baseline;
- no custom infrastructure where an existing proven upstream primitive already solves the measured requirement;
- accepted architecture decisions do not authorize implementation by themselves.
