---
type: Reference
title: OKF Cross-Linking and Citation Conventions
description: How concepts link to each other, and how an inline footnote marker maps back to a frontmatter source.
tags: [okf, format-spec, linking, citations, footnotes]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: okf-spec
    resource: https://github.com/GoogleCloudPlatform/knowledge-catalog/blob/main/okf/SPEC.md
    title: Open Knowledge Format v0.2 Specification
status: stable
---

# Linking between concepts

Concepts link to each other with plain markdown links. A bundle-relative link starting with `/` is the recommended, most stable form; an ordinary relative path also works.[^okf-spec] A broken link is tolerated rather than treated as an error — it may simply point at knowledge that hasn't been written yet.[^okf-spec]

Any path-valued field — not just links in the body — accepts an absolute URL, a bundle-relative path starting with `/`, or a relative path.[^okf-spec]

# Footnote citations

A claim in the body is attributed to a specific source by a markdown footnote label that matches that source's `id` in the frontmatter `sources` list — e.g. `[^okf-spec]` pairs with a `sources` entry whose `id` is `okf-spec`.[^okf-spec] The frontmatter entry itself carries the actual resource/title, so the inline marker is all that needs to appear in the body — there's no separate `[^okf-spec]: ...` footnote-definition block to maintain, unlike plain markdown footnotes.

Two things worth checking whenever a citation is added or removed:

- Every `sources[].id` should be cited by at least one `[^id]` in the body — an uncited source is dead weight. (Caught and fixed in this repo's [Claude_Design](../Prompting/Claude_Design/manual-editing-modes.md) bundle, where an orphaned `pandaitech-4ways` source was removed for exactly this reason.)
- Every `[^id]` in the body should resolve to a real `sources[].id` — a dangling marker cites nothing.

# Related

- [Provenance and Trust](provenance-and-trust.md)
- [Conformance Rules](conformance-rules.md)
