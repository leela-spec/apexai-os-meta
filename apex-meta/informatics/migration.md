---
type: Policy
title: Apex Informatics Migration & Onboarding Policy
description: Migration rules governing how existing, modified, and newly created repository files enter the Apex Informatics Standard.
tags: [informatics, migration, policy, okf]
generated: { by: gemini-3.7-flash, at: 2026-09-01T20:26:30Z }
status: current
---

# Apex Informatics Migration & Onboarding Policy

## 1. Governing Migration Principles

1. **Forward Default**: All newly created and actively modified knowledge files in governed targets MUST follow the [Apex Informatics Standard](standard.md).
2. **Explicit Wave Onboarding**: Existing repository knowledge zones (such as `apex-meta/orchestration/` or `apex-meta/kb/Weekly-Orchestrator/`) are onboarded into the standard only through explicit, approved implementation waves.
3. **No Mass Retrofit or Renaming**: Legacy `.okf.md` files that predate standard conformance are NOT mass-renamed or retrofitted in place.
4. **The `.okf.md` Suffix Rule**: A `.okf.md` file suffix does NOT prove OKF conformance. Conformance is determined exclusively by valid YAML frontmatter and bundle structure.
5. **Preservation of Runtime Semantics**: Migration of any zone MUST preserve semantic authority and existing entrypoint contracts.

---

## 2. Onboarding Workflow for Legacy Knowledge

When an approved wave targets a knowledge zone for migration:
1. **Pre-Migration Benchmark**: Record baseline retrieval metrics for the target zone.
2. **Bundle Scoping**: Declare the bundle root `index.md` with `okf_version: "0.2"`.
3. **Topic Normalization**: Split mixed-purpose blobs into single-subject concept files with valid YAML frontmatter.
4. **Deterministic Validation**: Execute `apex-meta/scripts/okf_validator.py --target <zone_path>` to ensure clean `OKF` and `APEX_PROFILE` conformance.
5. **Post-Migration Verification**: Re-evaluate retrieval metrics to confirm zero authority regression and reduced retrieval hops.
