---
type: Research
title: "Research validation and limitations"
description: "Research validation and limitations for the APEX OpenMausBot adoption research."
status: candidate
date: 2026-09-27
---

# Research validation and limitations

## Validation outcome

The bundle is candidate research with explicit evidence and unresolved decisions.
Final checks cover 23 files: 20 Markdown documents and three JSON evidence files.
Local links, JSON parsing, question/decision uniqueness, and placeholder checks passed.
No OpenMausBot integration pilot or independent Detective review was performed.

## Checks actually performed

| Check | Method | Actual result | What it proves |
|---|---|---|---|
| Repository instructions | Read root AGENTS and informatics standard | Scope and format applied | Correct authoring route |
| Official project identity | Official website/docs linked to GitHub project/releases | Official sources used | Product identity and source provenance |
| Upstream pin | git rev-parse HEAD in acquired sparse checkout | 1d8808b62fb38ead913e1bc4210858509b141ee0 | Exact inspected source basis |
| Local APEX revision | git rev-parse HEAD | bf5eee796c709b513fcfd726a9f47e0742af5c4c | Checkout baseline, not full dirty-tree snapshot |
| Source fingerprints | SHA-256 of 64 selected source files | Manifest saved | Exact local bytes for later comparison |
| Installer integrity | GitHub release digest versus Get-FileHash | Exact match | Local installer matches official asset |
| Installed product | Executable version metadata | 0.1.88.0 | App executable present |
| CLI presence | Get-Command | Claude/Codex discovered | Executable paths, not sign-in |
| Python availability | python --version | Python 3.12.10 | Local checker can execute |
| Existing negative fixtures | Six checker commands | 6/6 expected outcomes | Current covered checks behave as recorded |
| Missing-sidecar probe | Synthetic gate in memory; real harmless input digest | No violation despite nonexistent sidecar | Current checker does not enforce this requirement |
| Informatics conformance | Repository okf_validator.py | Final validation: 0 OKF / 0 Apex errors / 0 advisories | Structural conformance only |
| Local Markdown links | Resolve relative paths in all bundle Markdown | No broken targets across 20 Markdown files | Local path integrity only |
| Placeholder scan | Search skeleton markers | No skeleton placeholders remain | Research topics populated |

## Permanent receipts

- [Source fingerprints](evidence/source-fingerprints.json).
- [Local readiness observations](evidence/local-readiness.json).
- [Checker results](evidence/checker-results.json).

The fingerprint method is raw-byte SHA-256.
It is intentionally distinct from the APEX checker's LF-normalized digest.
Neither is mislabeled as a verified authority closure.

## Reproduction commands

Run from C:\GitDev\apexai-os-meta.

```powershell
python apex-meta/scripts/okf_validator.py --target apex-meta/orchestration/openmausbot-adoption-research --json
python scripts/orchestration_check.py --json packet apex-meta/orchestration/tests/negative/f1-candidate-to-canon.md
python scripts/orchestration_check.py --json canon-write apex-meta/orchestration/tests/negative/f2-stale-digest.md
python scripts/orchestration_check.py --json packet apex-meta/orchestration/tests/negative/f3-missing-evidence.md
python scripts/orchestration_check.py --json verdict apex-meta/orchestration/tests/negative/f4-reviewer-mutation.md
python scripts/orchestration_check.py --json canon-write apex-meta/orchestration/tests/negative/f5-unauthorized-write.md
python scripts/orchestration_check.py --json canon-write apex-meta/orchestration/tests/negative/p0-positive-control.md
```

The first five fixture checks should exit 1.
The positive fixture should exit 0.
These expected failures are successful negative tests, not broken research execution.

## Missing-sidecar probe design

The test imported the existing checker module.
It calculated the digest of the existing idea simulation artifact.
It supplied a synthetic gate string through an in-memory read_text replacement.
The string declared state verified and named deliberately-nonexistent-review.md.
check_canon_write returned an empty violation list.
No gate file was saved and no mutation routine was invoked.

This is evidence of a specific checker gap.
It is not evidence that a real unapproved canonical write occurred.
It also does not prove every other mutation path has the same gap.

## Scope of source inspection

Core APEX entrypoint, architecture, role definitions, workflows, and schemas were inspected directly.
The weekly skill and all ten later workflow-plan files were inspected.
The user-story portfolio and relevant sections supplied the seven-story mapping.
Later migration and OpenProject handovers were used as dated first-party records.

Official product guides were read alongside targeted source implementations.
The entire product codebase was not audited.
Upstream tests were not installed or run.
Descriptions of tests in vendor docs are vendor statements, not local test passes.

## Not verified

- Engine authentication or subscription entitlement.
- Actual bot settings, enabled connectors, conversations, and account assignments.
- Installed-build parity with the newer inspected source.
- Native APEX skill/subagent execution inside OpenMausBot.
- Fresh reviewer context or enforced read-only access in the product.
- Full dependency-closure enforcement elsewhere in APEX.
- Current live WSL/container/database topology.
- Real service ingestion, invoice compliance, broker restrictions, or external business outcomes.
- Backup restore, sleep catch-up, or duplicate suppression in a live workflow.
- Independent two-lens acceptance of this research bundle.

## Source and credential handling

Only official external sources support product claims.
Local APEX plans are treated as requirements or recorded outcomes, not independently proven vendor facts.
No credentials or personal conversations were copied into the project.
The credential-like WF07 sample is recorded as a location-only finding.

## Changes made

Created this research folder, its index, topic files, operator workbook, and evidence manifests.
Preserved existing role definitions, skills, schemas, registry, service configuration, and dirty worktree changes.
No app installation, configuration, external write, scheduled job, commit, or push was performed in this research turn.

## Completion meaning

The requested research project and prioritized decision material are delivered.
Deployment and production adoption remain future work with clearly listed prerequisites.
The project is not empty scaffolding and does not claim that unperformed pilot tests passed.
