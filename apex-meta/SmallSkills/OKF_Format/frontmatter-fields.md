---
type: Reference
title: OKF Concept Frontmatter Fields
description: The required, recommended, and optional YAML fields on a non-index OKF concept file.
tags: [okf, format-spec, frontmatter, yaml]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# Shape of a concept file

Every non-reserved `.md` file is two parts: a YAML frontmatter block bounded by `---` markers, then a free-form markdown body.[^okf-spec]

# Required

| Field | Purpose |
|---|---|
| `type` | A descriptive category string (e.g. `Playbook`, `Reference`, `BigQuery Table`). Types aren't centrally registered — consumers must tolerate types they don't recognize.[^okf-spec] |

That's the only field a bundle strictly needs to be conformant. Everything below is optional but expected on any concept worth reusing.

# Recommended

| Field | Purpose |
|---|---|
| `title` | Human-readable display name |
| `description` | One-sentence summary, used for previews and search |
| `resource` | A URI uniquely identifying the underlying asset the concept describes |
| `tags` | A YAML list of categorical keywords |

# Optional provenance/trust fields

Covered in full in [Provenance and Trust](provenance-and-trust.md): `sources`, `generated`, `verified`, `status`, `stale_after`.

# Consumer tolerance

A consumer must not reject a bundle for missing optional fields, unknown `type` values, or unknown extra keys.[^okf-spec] Don't over-fit to a rigid schema when authoring — the required surface is genuinely just `type`.

# Related

- [Provenance and Trust](provenance-and-trust.md)
- [Conformance Rules](conformance-rules.md)
