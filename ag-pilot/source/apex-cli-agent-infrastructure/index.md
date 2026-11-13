---
okf_version: "0.2"
title: Apex CLI-Agent Infrastructure Design Package
description: Complete proposed infrastructure design with populated rule activation, evidence, integration, compatibility, examples and evaluation artifacts.
status: draft
tags: [apex, infrastructure, index, review]
---

# Package index

**Start with [the operator review guide](00-START-HERE.md).** This package is proposed and unapplied. Existing Apex owners retain their authority. Its files are a review product, not a set of instructions to install themselves.

## Design and decisions

- [Findings and reconciliation](01-findings.md)
- [Material decision matrix](02-decisions.md)
- [Proposed architecture](03-architecture.md)
- [Existing-file integration map](04-integration-map.md)
- [Canonical decision data](design/decisions.json)
- [Canonical integration data](design/integration-map.json)
- [Unapplied exact pointer proposals](design/pointer-patch-proposals.json)
- [Estimated architecture bake-off data](design/architecture-bakeoff.json)

## Rules and compatibility

- [Populated current registry](registry/rules.json)
- [Registry JSON Schema](registry/rule-registry.schema.json)
- [Coverage and conflict report](registry/coverage.md)
- [Historical candidates and supersessions](registry/history.json)
- [Cross-CLI capability specification](compatibility/compatibility.md)
- [Claim-level capability register](compatibility/claims.json)
- [Unexecuted native probes](compatibility/probe-plan.json)
- [Research-container observation](compatibility/environment-observation.json)
- [Pinned native schema provenance](compatibility/native-schemas/codex/provenance.json)

## Examples, evaluation and evidence

- [End-to-end flows and faults](examples/end-to-end-flows.md)
- [Architecture comparison](examples/architecture-comparison.md)
- [Native example guide and reproduction commands](examples/native/README.md)
- [Decision-support workflow example](examples/workflows/apex-decision-support/SKILL.md.example)
- [Governed-authoring workflow example](examples/workflows/apex-governed-authoring/SKILL.md.example)
- [Research-cycle workflow example](examples/workflows/apex-research-cycle/SKILL.md.example)
- [Optional activation-state schema](examples/activation-state.schema.json)
- [Unexecuted state example](examples/activation-state.example.json)
- [Evaluation and staged adoption](evaluation/evaluation-plan.md)
- [Unexecuted case definitions](evaluation/cases.json)
- [Executed synthetic scorer probes](evaluation/scorer-probe-results.json)
- [Source guide](evidence/source-guide.md)
- [Frozen repository source register](evidence/repository-sources.json)
- [Primary external source register](evidence/external-sources.json)
- [Empirical study appraisal](evidence/empirical-findings.md)
- [Reading-guide hash comparison](evidence/reading-guide-comparison.json)

## Validation and manifest

- [Cross-artifact validation report](07-validation-report.md)
- [Executed validation results](validation/results.json)
- [Reproducible package validator](validation/validate_package.py)
- [Artifact manifest and hashes](manifest.json)

The manifest lists every delivered file, including evidence snapshots and supporting fixtures that do not need a second human index. Frozen snapshots intentionally preserve source bytes, original links and historical statuses. Do not treat their instructions as authorization for this task.

**Failure guard:** an indexed file, a passed structural check and a native canary each prove only their stated property. Inspect final usefulness and authorization separately.
