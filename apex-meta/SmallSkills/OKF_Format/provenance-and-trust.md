---
type: Reference
title: OKF Provenance, Trust, and Lifecycle Fields
description: The optional frontmatter fields that record where a concept came from, who checked it, and when it goes stale.
tags: [okf, format-spec, provenance, trust, lifecycle]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# Why v0.2 added these

v0.1 bundles are just frontmatter plus body. v0.2 (2026-07-25) layered a set of optional trust-signal fields on top — provenance, verification, freshness, lifecycle — without breaking existing v0.1 bundles, which need no changes to stay valid.[^okf-spec]

# sources

A list of the materials a concept was derived from. Each entry:

| Key | Required? | Purpose |
|---|---|---|
| `resource` | yes | URL, bundle-relative path, or scope descriptor |
| `id` | no | Stable key used to attribute a specific claim in the body via a footnote label |
| `title` | no | Human-readable label |
| `author` | no | Who produced the source, using the actor convention below |
| `usage_count` | no | How often the source gets exercised, over a timeframe |
| `last_modified` | no | When the source itself last changed |

# generated

Records who (or what) authored the content:

| Key | Required? | Purpose |
|---|---|---|
| `by` | yes | Actor identifier |
| `at` | no | ISO 8601 timestamp of the last meaningful change |

# verified

Either a single `{ by, at }` mapping or a list of them — multiple entries mean multiple independent checks. A bare single mapping is treated as a one-element list.[^okf-spec]

# Actor convention

Whoever fills `generated.by`, `verified[].by`, or `sources[].author` uses one of three shapes:[^okf-spec]

- `<producer>/<version>` — an agent, e.g. `claude/sonnet-5`
- `human:<id>` — a person
- `process:<id>` — an automated process

A consumer treats content as more trustworthy when it detects the `human:` prefix.[^okf-spec]

# Lifecycle

| Field | Values | Purpose |
|---|---|---|
| `status` | `draft`, `stable` (default), `deprecated` | Where the concept sits in its life |
| `stale_after` | ISO 8601 instant | When the content should be treated as stale |

Use `stale_after` on anything genuinely time-sensitive (bug lists, quota numbers), not on evergreen principles. [Claude_Design](../Prompting/Claude_Design/known-issues-and-quota.md)'s known-issues file is a working example: `stale_after` there, absent everywhere else in that bundle.

# Related

- [Cross-Linking and Citations](cross-linking-and-citations.md)
- [Frontmatter Fields](frontmatter-fields.md)
