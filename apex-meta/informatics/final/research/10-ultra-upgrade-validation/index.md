---
okf_version: "0.2"
type: Index
id: RES-INDEX-10-ULTRA-UPGRADE-VALIDATION
title: Empirical Validation & Alignment Architecture Benchmark (a4cb2b6a)
description: Pre-registered benchmark suite comparing Live Master (Arm A), Hooks + Rules (Arm B), ETH Zurich Lean Invariants (Arm C), and Two-Plane Deliberation (Arm D) across T1-T6.
status: current
tags: [informatics, research, index, benchmark, validation, arms, a4cb2b6a]
---

# Ultra Contract Validation & Alignment Arms (`research/10-ultra-upgrade-validation/`)

> **Navigation:** [Master Index](../../index.md) | [HANDOVER-12](../../operations/handovers/HANDOVER-12-TEST-UPGRADED-CONTRACT-AND-ALIGNMENT-ARMS.md) | [Ledger (`C01`–`C12`)](../09-ultra-contract-and-layers-synthesis/01-step-by-step-change-ledger.md)

## Bundle Contents

| Artifact | Purpose | Link |
|---|---|---|
| **Pre-Registration Protocol** | Locked `H1`–`H5` oracles, `Arm A`–`Arm D` specs, `T1`–`T6` criteria, isolation flags | [preregistration.md](preregistration.md) |
| **Task & Threshold Spec** | Machine-readable `T1`–`T6` prompts, arms, budget caps, target paths | [tasks.json](tasks.json) |
| **Deterministic Scorer** | Multi-CLI JSONL trace parser, git diff verifier, and Wilson `95%` CI calculator | [score_eval.py](score_eval.py) |
| **Immutable Hash Lock** | Pre-run SHA-256 manifest generated prior to any `runs/` execution | [PREREG.sha256](PREREG.sha256) |
| **Fixtures & Hook Templates** | Carrier contracts (`Arm A`–`D`), `Arm B` hook gates, and seeded `T2`/`T5`/`T6` traps | [`fixtures/`](fixtures/) |

## Fixture & Hook Manifest (`fixtures/`)

- **Arm Carrier Templates:** [armA-contract.txt](fixtures/armA-contract.txt), [armB-slim-contract.txt](fixtures/armB-slim-contract.txt), [armB-rule-closeout.txt](fixtures/armB-rule-closeout.txt), [armB-rule-informatics.txt](fixtures/armB-rule-informatics.txt), [armC-lean-contract.txt](fixtures/armC-lean-contract.txt), [armC-gemini-routing.txt](fixtures/armC-gemini-routing.txt), [armD-delib-contract.txt](fixtures/armD-delib-contract.txt).
- **Arm B Runtime Gates:** [armB_hook_pretool.py](fixtures/armB_hook_pretool.py) (`PreToolUse` / `BeforeTool`), [armB_hook_stop.py](fixtures/armB_hook_stop.py) (`Stop` / `AfterAgent`).
- **Task Seed Files:** [route0-note.md.txt](fixtures/route0-note.md.txt), [operating-rules.md.txt](fixtures/operating-rules.md.txt), [decision-notes.md.txt](fixtures/decision-notes.md.txt), [t6-target.md.txt](fixtures/t6-target.md.txt), [t6-prior-reasoning.md.txt](fixtures/t6-prior-reasoning.md.txt), [t6-dirty1.base.txt](fixtures/t6-dirty1.base.txt), [t6-dirty1.dirty.txt](fixtures/t6-dirty1.dirty.txt), [t6-dirty2.base.txt](fixtures/t6-dirty2.base.txt), [t6-dirty2.dirty.txt](fixtures/t6-dirty2.dirty.txt).
