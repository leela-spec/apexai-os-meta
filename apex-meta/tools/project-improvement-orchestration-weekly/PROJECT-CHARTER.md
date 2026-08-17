# Project Charter — Weekly Orchestration Improvement

This charter uses the project-capture and epic logic of `apex-plan`: goal, scope, constraints, dependencies, acceptance criteria, definition of done, review flags and handoff boundaries. It intentionally does not create task-level micro records yet; those will emerge through bounded module work.

## Project capture

**Project:** Weekly Orchestration Improvement

**Goal:** Repair the existing Apex Weekly Orchestration so that its real runtime contracts encode the intended workflow and produce repeatable, human-usable weekly planning, daily planning, flow execution, prompt preparation, evidence, recap and state-update behavior without unnecessary architectural overhead.

**Source:** Operator review on 2026-08-17; recovered operator-output design under `apex-meta/operator-output-design/`; current production skills/agents under `.claude/`; W34 generated artifacts under `artifacts/`.

## Why this project exists

The repository contains a real Weekly Orchestrator and stage skills, but the current runtime behavior has drifted from previously verified operator-facing design. The recovered design was promoted into files but not effectively wired into active skill/agent entrypoints. Current run artifacts show schema-first output, duplicated metadata, placeholder prompt packs, artificial ratings and a complex gate/packet lifecycle whose current value must be revalidated.

The failure is therefore not only cosmetic. The project must verify and, where necessary, repair the global orchestration spine before optimizing individual outputs.

## Scope

### In scope

- complete Weekly Orchestrator lifecycle and stage topology;
- stage ownership and interfaces;
- AI vs deterministic vs operator responsibilities;
- state authority and data transactions;
- handoff/persistence rules;
- gates and review triggers;
- Session, Sync and ProjectStatus interaction where they touch the weekly loop;
- weekly, daily, flow, prompt, evidence, recap and status-merge outputs;
- human/machine presentation boundary;
- fresh-session runtime reproducibility;
- archive of superseded architecture so active paths remain unambiguous.

### Out of scope unless the project proves necessity

- a second production orchestration framework;
- a universal replacement schema;
- new scoring/ranking systems;
- new databases/registries;
- unrelated Apex project-management redesign;
- unrelated project work execution;
- speculative future automation.

## Constraints

1. Production truth is repository files, not conversational memory.
2. The Master Orchestrator is a project/development role, not a competing runtime control plane.
3. Existing components have no presumption of necessity.
4. Existing verified human-facing design is starting evidence, not an untouchable schema.
5. Replaced information is archived rather than silently discarded.
6. Detailed module design is delegated to fresh module chats through bounded handovers.
7. Every module returns to the Master for cross-system verification before testing.
8. Testing occurs after real production integration and in a fresh context.
9. The W34/example run is the initial regression fixture.

## Epic-level outcomes

### E1 — Orchestration spine is coherent

The repository has one clear production Weekly Orchestrator lifecycle whose stages, owners, transactions, authority boundaries and gates are understandable and justified.

### E2 — Operator surfaces match intent

Weekly Brief, Next Day Brief, Flow Execution Card, prompts and recap/change surfaces are human-usable and do not expose unnecessary machine plumbing.

### E3 — Machine infrastructure is minimal and explicit

Deterministic helpers, Sync, Session, evidence normalization, reviews and status projections exist only where they provide concrete value, with clear inputs/outputs and no duplicated truth.

### E4 — Fresh-session behavior is repeatable

A fresh runtime session can invoke the real production path using encoded skills/contracts and W34/example inputs without relying on design-chat memory.

### E5 — Improvement process is itself resilient

A long-running Master chat can recover its exact project position from this folder, delegate bounded module work, verify returns, and survive compaction or a replacement Master chat without reconstructing the project from scratch.

## Acceptance criteria

- Master can explain the complete production lifecycle and every remaining major component's value.
- Active Weekly Orchestrator files encode the intended global design rather than stale historical assumptions.
- Each completed module has an approved operator output and production implementation.
- Master integration verification passes after each module.
- Fresh test chat produces the output through the actual production skill path.
- Operator can inspect the result without reading internal contracts.
- No known stale authority remains active beside its replacement.

## Definition of done

The project is done only when a fresh weekly run can proceed through the intended lifecycle using repository-defined skills/agents, the W34 regression fixture has passed each relevant module test, the operator has accepted the human-facing outputs, and the Master records no unresolved architecture contradiction that affects normal operation.

## Current dependencies

- Module 00 precedes detailed output modules because global interfaces/gates may change their requirements.
- Module output tests depend on production integration, not isolated mock rendering.
- State-update modules depend on clear evidence and authority boundaries.

## Review flags

- Current `.claude/skills/` organization is compositional rather than hierarchical; whether any physical reorganization is useful must be decided in Module 00, not assumed.
- Current Weekly Orchestrator requires several gates/envelopes and Sync reads whose necessity remains unproven.
- ProjectStatus may currently duplicate or transform canonical state unnecessarily.
- Prompt materialization behavior is currently incomplete/degraded in W34 artifacts.
