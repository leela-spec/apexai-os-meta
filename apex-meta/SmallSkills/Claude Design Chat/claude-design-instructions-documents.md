---
type: Best Practice Guide
title: Instructing Claude — Documents (exported to HTML or PDF)
description: How another AI should brief Claude Docs when the deliverable is a written document whose final form is HTML or PDF (not a slide deck, not a website).
tags: [claude-docs, documents, pdf, html, brief-template, okf-0.2]
---

# Scope

Use this guide for written-document deliverables (reports, proposals, one-pagers, guides, specs)
produced with Claude Docs, where the final exported artifact is either HTML (viewable/shareable
page) or PDF (fixed, printable/sendable). Not for slide decks (see slides guide) or full websites
(see website guide).

# Required brief structure

1. **Role** — who Claude is writing as / for (e.g. "write as a founder addressing investors").
2. **Task** — the concrete document to produce and its purpose.
3. **Context** — source material/facts to draw from; do not let Claude invent facts, figures, or
   claims not supplied.
4. **Format** — explicit structural shape: H1 title, H2 sections, numbered steps where
   procedural, fenced code blocks with language tags if code is included, blockquote callouts for
   notes/warnings.
5. **Constraints** — stated as hard rules, not preferences: target length, banned phrases/tone,
   required sections, what must NOT be included.

Wrap mixed instructions/context/examples in clearly delimited blocks (e.g. XML-style tags) when the
brief combines several kinds of input — Claude handles long or mixed input far more reliably when
source material is clearly separated from instructions.

# Drafting workflow (draft in Markdown, finalize in the target format)

- Draft and iterate in Markdown first while content is still moving — it's the fastest format to
  revise in.
- Only convert to the final export format (HTML or PDF) once content is stable; re-drafting after
  exporting to PDF/HTML is far more friction than iterating in Markdown.
- State the final export target up front (HTML vs PDF) — this changes formatting choices Claude
  makes even during drafting (e.g. PDF implies fixed pagination/print margins; HTML implies
  scrollable, possibly interactive layout).

# Format-specific notes

**If the final target is HTML:**
- Specify whether it needs to be interactive/scrollable, single-page or multi-section, and whether
  it will be embedded or stand alone.
- State the viewing context (internal doc viewer, emailed link, embedded on a site) — this affects
  whether to request navigation, anchors, or a table of contents.

**If the final target is PDF:**
- Explicitly request "print/PDF-ready" formatting: short paragraphs, clear heading hierarchy, simple
  tables (complex nested tables often break on PDF export) — ask for this before generating, not as
  a later fix.
- State page-length expectations if it matters (e.g. "must fit on 2 pages") since PDF has fixed
  pagination unlike HTML.

# Common pitfalls to avoid in the brief

- Skipping the Markdown-draft stage and iterating directly on an exported PDF/HTML — much slower to
  revise.
- Not stating the export target before drafting, leading to a document shaped wrong for its final
  medium (e.g. a long scrolling HTML doc that doesn't paginate sensibly as PDF).
- Letting Claude invent facts/figures because source context wasn't explicitly supplied.
- Complex or deeply nested tables when PDF is the target — simplify before requesting export.
- Marketing-style filler language when the brief calls for task-first, skimmable content — state
  "no marketing language" explicitly if that's required.

# Minimal checklist before finalizing

- [ ] Role / Task / Context / Format / Constraints all stated explicitly
- [ ] Source facts/content supplied — nothing left for Claude to invent
- [ ] Export target (HTML vs PDF) decided before drafting begins
- [ ] Drafted and stabilized in Markdown before converting to final format
- [ ] Format-specific requirements applied (print-ready for PDF; nav/anchors for HTML)
- [ ] Final length/pagination constraint checked against target format

# Sources

- https://platform.claude.com/docs/en/build-with-claude/prompt-engineering/claude-prompting-best-practices
- https://academy.techpresso.co/prompts/claude-prompts-documentation
- https://theitsolutionist.com/2026/04/21/efficient-claude-usage-with-microsoft-word-documents/
- https://backrun.co/blog/claude-to-word
- https://promptbuilder.cc/blog/claude-prompt-engineering-best-practices-2026
