---
type: Reference
title: OKF Conformance Rules
description: What a bundle must do to be conformant, and what a consumer must tolerate rather than reject.
tags: [okf, format-spec, conformance, validation]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# The three conformance requirements

A bundle is conformant when:[^okf-spec]

1. Every non-reserved `.md` file has parseable YAML frontmatter.
2. That frontmatter includes a non-empty `type` field.
3. The two reserved filenames (`index.md`, `log.md`) follow their specified structure — see [Bundle Structure](bundle-structure.md).

That's the entire bar. Everything else in this reference bundle — sources, generated, verified, lifecycle, attested computation — is optional richness on top of a genuinely minimal core.

# What a consumer must NOT reject a bundle for

- Missing optional fields
- An unrecognized `type` value
- Unknown additional frontmatter keys
- A broken cross-link
- No `index.md` at some directory level[^okf-spec]

# Practical checklist when authoring a new bundle

- [ ] Every concept file has `type` at minimum
- [ ] Root `index.md` has `okf_version: "0.2"` and nothing else in frontmatter
- [ ] Every `sources[].id` is cited by a `[^id]` somewhere in that file's body
- [ ] `stale_after` is set only where content is genuinely time-sensitive
- [ ] A `log.md` exists if the bundle expects to change over time

# Related

- [Bundle Structure](bundle-structure.md)
- [Frontmatter Fields](frontmatter-fields.md)
