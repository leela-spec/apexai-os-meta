---
type: Reference
title: OKF Attested Computation Concept
description: The optional concept type that pairs a definition with a sanctioned, independently-verifiable computation.
tags: [okf, format-spec, attested-computation, verification]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# What it's for

Most concepts just describe something. An Attested Computation concept goes further: it's a standalone concept with `type: Attested Computation` that pairs a definition with a specific, runnable way to check it — so a claim like "this metric equals X" can be independently re-derived and confirmed rather than taken on faith.[^okf-spec]

# Fields

| Field | Required? | Purpose |
|---|---|---|
| `runtime` | yes | Execution context, e.g. `bigquery`, `dbt`, `python` |
| `parameters` | no | A list of typed, named inputs, each `{ name, type, required }` |
| `computation` | no | Either a path to an external computation file, or an inline fenced code block in the body |
| `executor` | no | `resource` — how to actually run it — plus `receipt` — the evidence fields the run is expected to return |
| `attester` | no | `resource` pointing at deterministic verification code that checks the receipt |

# When to reach for this

Nothing in this repo currently needs it — it's aimed at things like a canonical metric definition backed by a query anyone can re-run, not at prompting playbooks like [Claude_Design](../Prompting/Claude_Design/index.md). Documented here for completeness so it isn't reinvented ad hoc if a future bundle (e.g. an SSOT-style rule with a runnable check) needs it.

# Related

- [Frontmatter Fields](frontmatter-fields.md)
- [Conformance Rules](conformance-rules.md)
