---
okf_version: "0.2"
title: V2 Always-On Architecture — Decision Register, Blueprint & Research Design
description: Separate version branch holding the always-on contract architecture: decision register, standalone informatics contract block, non-active AGENTS.md blueprint, empirical test protocol, and research prompt packets.
tags: [v2, always-on, architecture, decisions, blueprint, research-design]
---

# V2 Always-On Architecture

**Status: nothing here is active.** Every artifact in this folder is a candidate, a blueprint, or a
research design. No file here is loaded by any agent at runtime, and nothing here modifies the live
`AGENTS.md`, `CLAUDE.md`, or the live informatics suite.

This folder is a **separate version branch** from
[`../DeepReasoning/`](../DeepReasoning/index.md). That folder recorded the canonical-ownership pass
that was applied and is live. This folder records the architecture that emerged *after* it, which
partly supersedes it. Nothing in `DeepReasoning/` has been edited or overwritten.

## Contents

**Start at [12-status-index.md](12-status-index.md)** — a single coverage view of every finding,
decision, open question and defect, with its status and owning document.

| File | What it is | Status |
|---|---|---|
| [12-status-index.md](12-status-index.md) | **Coverage index.** Everything tracked, with status. Two items need operator action and block on nothing | **Read first** |
| [01-decision-register.md](01-decision-register.md) | Every settled decision, every superseded position, the open calls, and the falsification conditions | Record |
| [02-informatics-contract-block.md](02-informatics-contract-block.md) | The v0.3 block, 721 tokens, with per-rule provenance | **Superseded by 07.** Kept as the earlier record |
| [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) | A **copy** of the real `AGENTS.md` with the block integrated, plus the merge map and trim options | Blueprint, non-active. Updated to v0.4 |
| [04-empirical-test-protocol.md](04-empirical-test-protocol.md) | The read-trace experiment that decides whether IF-gating works at all, arms A–H | Design, not run |
| [05-research-prompt-packets.md](05-research-prompt-packets.md) | Provider-unspecified prompt packets for the three open research questions | Prompts, not executed |
| [06-contract-block-revision-proposal.md](06-contract-block-revision-proposal.md) | Answers to the operator's ten questions on v0.3, and the reasoning behind every v0.4 change | Record |
| [07-contract-block-v0.4.md](07-contract-block-v0.4.md) | The v0.4 block, 1,357 tokens, named tags and observable-action gates | **Superseded by 09.** Retained as the record |
| [08-discussion-and-open-threads.md](08-discussion-and-open-threads.md) | Operator feedback on v0.4 item by item, draft reformulations, two new rules, and the regression I introduced | Open discussion |
| [09-contract-block-v0.5.md](09-contract-block-v0.5.md) | **The current candidate block** — 1,622 tokens, operator decisions applied, three gates restored, measured token decomposition | **Current candidate** |
| [10-RESEARCH-EXECUTION-HANDOVER.md](10-RESEARCH-EXECUTION-HANDOVER.md) | **Handover for another AI** to execute the ten research packets iteratively and write eleven result files | **Ready to dispatch** |
| [11-instruction-surface-architecture.md](11-instruction-surface-architecture.md) | The five instruction surfaces, the drift measured between them (`D10`), and the universal-vs-repo-specific layering question | **Open architecture** |

## Why this folder exists

The applied pass in `DeepReasoning/` was built on an assumption that later proved wrong: that each
module must restate universal invariants because it might be loaded alone. Once the invariants move
into an always-on contract, that assumption no longer holds — and a different architecture becomes
available.

Rather than rewrite the earlier record (which was honest about what was known at the time), this
folder states the newer position and marks exactly which earlier positions it supersedes. The
superseded ones are listed in [01-decision-register.md](01-decision-register.md) Part B.

## Reading order

1. [01-decision-register.md](01-decision-register.md) — start here; it is the index of what is settled and what is not
2. [02-informatics-contract-block.md](02-informatics-contract-block.md) — the concrete artifact the decisions produce
3. [03-BLUEPRINT-agents.md](03-BLUEPRINT-agents.md) — what installing it would look like
4. [04-empirical-test-protocol.md](04-empirical-test-protocol.md) — how to find out whether it works
5. [05-research-prompt-packets.md](05-research-prompt-packets.md) — the open questions, ready to dispatch
