---
type: Reference
id: SPEC-CARRIER-LAYER2-SHARED
title: Shared Layer 2 Text for Every Global Agent Carrier
description: The workstation sections every global carrier (Claude, Codex, Gemini/Antigravity) must hold word for word, owned here so apex_carrier_sync.py can compare and repair them.
status: current
tags: [apex, carriers, layer-2, sync]
---

# Shared Layer 2 Text

Sections below must appear unchanged in `~/.claude/CLAUDE.md`, `~/.codex/AGENTS.md` and `~/.gemini/GEMINI.md`. Edit them here, then run `tools/apex_carrier_sync.py --sync`. Environment-specific sections (OpenProject routing, harness facts) stay per carrier and are not listed here. The contract block is separate: see `specs/apex_contract_v1.0_ultra.xml`.

## Personal Windows development defaults

- On Windows, Developer Mode permits non-elevated symbolic-link creation. When a new project, package manager, or build tool reports missing symlink support, check Developer Mode before requiring an elevated terminal.
- For Flutter projects, run `flutter doctor` before diagnosing a target-toolchain issue. Android, web, and Windows desktop have independent prerequisites.

## Knowledge Retrieval & Evidence Tooling (QMD Speed Protocol)

- Run `qmd search` (FTS5 BM25, ~0.3s) first. Escalate to `qmd query` (hybrid AI, 20s+) only when keyword search returns zero results (`DEC-QMD-01`).
- Direct CLI execution only. Background daemons (`--daemon`) are prohibited (`DEC-QMD-02`).
- Fetch 20-40 line windows via `qmd get <path:line:count>` or `#docid:from:count`. Never bulk-read entire files (`DEC-QMD-04`).
- Search the subject itself, never your own explanation of it. A query phrased as your theory returns nothing and falsely confirms absence.

## Workstation & Host Environment

- Windows 11 host, projects under `c:\GitDev\`. Isolated from external server harnesses.
- The `ki-basis` Linux Docker/WSL2 stack runs in a separate VM. Windows workstation agents must not invoke, touch, or reintroduce it.

## Completion Reporting

- Never describe a proposed block as applied. Completion requires the executor's exact-match result plus the required test evidence.
- Current user requests, higher-priority instructions, and native permissions govern conflicts with this contract. Instructions never grant additional access.
- Report baseline failures separately from introduced defects. A written validation instruction is not an enforced gate.
