---
okf_version: "0.2"
title: Informatics Deep Reasoning Research & Backlog Sub-Bundle
description: Indexed research, evidence, decision matrices, module audits, and backlog supporting the canonical-ownership compression pass on the live Apex Informatics suite.
tags: [informatics, research, deep-reasoning, compression, backlog]
---

# Informatics Deep Reasoning Research & Backlog Sub-Bundle

This sub-bundle holds the evidence, reasoning, rejected options, and backlog that the live
specification files must never carry (`FA-01` current-truth separation). Every compression
decision applied to `apex-meta/informatics/*.md` traces to a file here.

## 1. Scope & Boundary

- **Target of study:** the 7 governed live files in `apex-meta/informatics/`.
- **Plane:** 5 (Evidence & History). Narrative, citations, rejected options, and historical
  deltas belong here, not in the live suite.
- **Validator status:** this directory is already outside root-bundle validation — `okf_validator.py`
  prunes recursion at any directory owning an `index.md`, and `Agent_Setup/index.md` is such a
  boundary. The OKF frontmatter above serves navigation, not isolation.

## 2. Research Tree

| File | Iteration | Contents |
|---|---|---|
| [00-master-matrix.md](00-master-matrix.md) | 1 | System inventory, 84-rule master matrix, Defect Register |
| [01-system-wide-overlap-and-token-audit.md](01-system-wide-overlap-and-token-audit.md) | 2 | Concept → canonical-owner map, duplication sites, token scorecard |
| [02-new-rules-discovery-and-qa-bakeoff.md](02-new-rules-discovery-and-qa-bakeoff.md) | 2 | Q&A Decision Matrices, external research citations, new rule proposals |
| [03-research-backlog-and-open-questions.md](03-research-backlog-and-open-questions.md) | 2 | `RBL-XX` prioritized research backlog |
| [M01 Routers & Index](modules/M01-routers-and-index.md) | 3 | `index.md`, router, authority precedence (**D3**, **D7**) |
| [M02 Writing Profile](modules/M02-writing-profile.md) | 3 | `WP-01..25` audit + patches (**D5**, 3 new rules) |
| [M03 File Architecture](modules/M03-file-architecture.md) | 3 | `FA-01..13` audit + patches (**D1**, **D2**, **D4**) |
| [M04 Execution Modes](modules/M04-execution-modes.md) | 3 | `EM-01..12` audit + patches |
| [M05 Anti-Drift Rules](modules/M05-anti-drift-rules.md) | 3 | `AD-01..28` audit + patches |
| [M06 Governance Schemas](modules/M06-governance-schemas.md) | 3 | `GS-01..22` audit + patches (**D6**, **D9**) |
| [04-consolidated-patch-and-verification.md](04-consolidated-patch-and-verification.md) | 4 | Patch ledger, measured scorecard, forensic report |

## 3. Rule → Research Cross-Reference

Every live rule resolves to its research record through three hops: the
[master matrix](00-master-matrix.md) §3 carries a verdict and owning module for all 96 rules; the
module file carries the applied patch and behavioral check; the
[ledger](04-consolidated-patch-and-verification.md) §1 carries the execution-order entry.

| Rule range | Owner file | Module record | Ownership decisions |
|---|---|---|---|
| `WP-01..25` | `writing-profile.md` | [M02](modules/M02-writing-profile.md) | [01](01-system-wide-overlap-and-token-audit.md) §2.1 B3, §2.2 |
| `FA-01..13` | `file-architecture.md` | [M03](modules/M03-file-architecture.md) | [01](01-system-wide-overlap-and-token-audit.md) §2.1 B2/B5, [02](02-new-rules-discovery-and-qa-bakeoff.md) Q2/Q7 |
| `EM-01..12` | `execution-modes.md` | [M04](modules/M04-execution-modes.md) | [01](01-system-wide-overlap-and-token-audit.md) §2.1 B4, [02](02-new-rules-discovery-and-qa-bakeoff.md) Q6 |
| `AD-01..28` | `anti-drift-rules.md` | [M05](modules/M05-anti-drift-rules.md) | [01](01-system-wide-overlap-and-token-audit.md) §2.2 |
| `GS-01..22` | `governance-schemas.md` | [M06](modules/M06-governance-schemas.md) | [01](01-system-wide-overlap-and-token-audit.md) §2.1 B1, §4, [02](02-new-rules-discovery-and-qa-bakeoff.md) Q4 |

### Defects and backlog

| Defect | Fixed in | Backlog item | Record |
|---|---|---|---|
| **D1** duplicate `FA-04` | [M03](modules/M03-file-architecture.md) §3 | `RBL-06` | [00](00-master-matrix.md) §4 |
| **D2** contradicting frontmatter contracts | [M03](modules/M03-file-architecture.md) §4 | — | [02](02-new-rules-discovery-and-qa-bakeoff.md) Q2 |
| **D3** root index missing `tags` | [M01](modules/M01-routers-and-index.md) §2 | — | [00](00-master-matrix.md) §4 |
| **D4** stale topology tree | [M03](modules/M03-file-architecture.md) §2 | — | [00](00-master-matrix.md) §4 |
| **D5** sentence-length reconciliation | [M02](modules/M02-writing-profile.md) §3 | — | corrected scope in M02 |
| **D6** `GS-04`/`GS-18` intra-file duplicate | [M06](modules/M06-governance-schemas.md) §2 | — | [01](01-system-wide-overlap-and-token-audit.md) §2.3 |
| **D7** dual authority with `standard.md` | [M01](modules/M01-routers-and-index.md) §2 | — | [02](02-new-rules-discovery-and-qa-bakeoff.md) Q8 |
| **D8** duplicated `estimate_tokens` | **declined** | — | [M06](modules/M06-governance-schemas.md) §7 |
| **D9** drifted patch-intent schema | [M06](modules/M06-governance-schemas.md) §3 | `RBL-08` | [01](01-system-wide-overlap-and-token-audit.md) §4 |

Open research: [`RBL-01`..`RBL-08`](03-research-backlog-and-open-questions.md). `RBL-07` flags a
plaintext credential in a tracked file and needs operator action.

### Durable guards installed

`apex-meta/informatics/tests/test_canonical_ownership.py` — 4 guard classes, all mutation-tested in
[04](04-consolidated-patch-and-verification.md) §3.2: rule-ID uniqueness, canonical-pointer
integrity, link portability, and no re-embedding of the upstream schema.

## 4. Live Suite Under Study

- [index.md](../../../index.md) · [general-informatics-router.md](../../../general-informatics-router.md)
- [writing-profile.md](../../../writing-profile.md) · [file-architecture.md](../../../file-architecture.md)
- [execution-modes.md](../../../execution-modes.md) · [anti-drift-rules.md](../../../anti-drift-rules.md)
- [governance-schemas.md](../../../governance-schemas.md)
