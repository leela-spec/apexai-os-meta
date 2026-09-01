---
okf_version: "0.2"
---

# OKF 0.2 Format — Reference Bundle

* [Bundle Structure](bundle-structure.md) - Directory layout, reserved filenames, and where index.md/log.md fit.
* [Frontmatter Fields](frontmatter-fields.md) - Required vs. recommended YAML fields on every concept file.
* [Provenance and Trust](provenance-and-trust.md) - Sources, generation, verification, and lifecycle/staleness signals.
* [Cross-Linking and Citations](cross-linking-and-citations.md) - How concepts link to each other and how footnote markers map back to frontmatter sources.
* [Attested Computation](attested-computation.md) - The optional concept type for pairing a definition with a verifiable computation.
* [Conformance Rules](conformance-rules.md) - What makes a bundle conformant, and what consumers must tolerate.
* [Adoption Project](adoption-project/index.md) - Research, open decisions, and next steps for rolling this out as the repo standard.

# Scope

This bundle documents Google Cloud's Open Knowledge Format (OKF) v0.2 — the format used by [Claude_Design](../Prompting/Claude_Design/index.md) and any other knowledge bundle in this repo. It exists so future work here can ground format decisions in a local reference instead of re-deriving the spec from a websearch each time. Read only the file(s) the current task needs; each is independently loadable.

This is a working summary in our own words, built from the primary source cited in each file's frontmatter — not a verbatim copy of that source. Where this bundle and the primary source disagree, the primary source wins.
