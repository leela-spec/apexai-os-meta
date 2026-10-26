---
type: Best Practice Guide
title: Instructing Claude Design — Slide Decks / Presentations
description: How another AI should brief Claude (Design/Slides/PowerPoint) when the deliverable is a presentation deck, including a reusable brand master.
tags: [claude-design, claude-slides, slide-master, brief-template, okf-0.2]
---

# Scope

Use this guide for any slide-deck deliverable: pitch decks, one business-branch deck, or a shared
"master" template reused across several decks. Applies to Claude Design's presentation mode, Claude
Slides, and Claude for PowerPoint — all three read the same underlying template/brand signal.

# Master/template-first workflow (do this before generating any content)

- Apply the brand template BEFORE asking for content. Claude reads the slide master, layouts,
  fonts, and color scheme already present in a deck and reuses them automatically — so the master
  must exist first, content generation second. This is Anthropic's own stated first best practice.
- A reusable "slide master" in practice means: one deck (or one uploaded template) containing — the
  background/accent colors, the heading/body font pairing, logo placement rule, and a header/footer
  convention — that every subsequent deck is generated into or copied from.
- If there are several business branches, each with their own deck: build ONE master first, then
  generate each branch deck from that same master in the same session, rather than re-describing
  brand rules per deck.

# Required brief structure per deck

1. **Goal** — purpose of this deck and the single outcome it should produce (e.g. "board-ready
   update", "sales pitch for branch X").
2. **Length / shape** — state an explicit slide count range (e.g. "8 to 12 slides") built from
   provided notes/content; do not leave this open-ended.
3. **Content** — supply the real source notes/content to turn into slides. Do not ask Claude to
   invent facts or numbers.
4. **Constraints per slide** — state hard limits as rules, not preferences: one action-oriented
   title under 12 words, no more than 4 bullets per slide, each bullet under 15 words.

# Brand/template fidelity

- Reference the master/template explicitly in every deck-generation prompt within the session
  ("use the applied template/brand, do not introduce new colors or fonts").
- Be specific about what must NOT change: logo position, footer text, color values — state these as
  fixed constraints, not assumptions.

# Editing and iteration

- Always review changes before finalizing — do not treat the first draft as final.
- For revision requests, name the specific slide and specific change (e.g. "tighten slide 4 to one
  title + 3 bullets") rather than asking Claude to "improve" the deck generally — vague revision
  requests produce vague, unpredictable edits.

# Export / handoff path

| Need | Export |
|---|---|
| Live meeting presentation | PPTX |
| Static review / sharing without edit access | PDF |
| Interactive version with animation/motion | standalone HTML |
| Raw files / backup | .zip download |

Decide the export target before generating, since interactive HTML decks are generated differently
from a PPTX-ready deck (HTML can use animation/motion that PPTX/PDF cannot represent).

# Common pitfalls to avoid in the brief

- Asking for content before a template/master exists — produces generic, off-brand slides that then
  need brand-retrofitting.
- Leaving slide count unbounded — produces bloated, inconsistent decks.
- Giving vague revision instructions ("make it better") instead of naming the slide and the change.
- Mixing decks from different brand lines in one session without re-applying the correct master —
  carries the wrong branch's branding into the wrong deck.
- Treating an HTML export as if it were an editable PPTX file (it is not — pick the export format
  for the actual downstream use before generating).

# Minimal checklist before finalizing

- [ ] Master/template applied before any content prompt
- [ ] Slide count range stated explicitly
- [ ] Real source notes supplied (no invented content)
- [ ] Per-slide constraints (title length, bullet count/length) stated as rules
- [ ] Fixed brand elements (logo position, footer, colors) explicitly protected
- [ ] Export format decided per use case (PPTX / PDF / HTML / zip)
- [ ] Final review pass done slide-by-slide before distribution

# Sources

- https://support.claude.com/en/articles/13521390-use-claude-for-powerpoint
- https://academy.claude.com/tutorials/using-claude-design-for-presentations-and-slide-decks
- https://www.smithstephen.com/p/how-to-get-claude-to-create-powerpoint
- https://claudelab.net/en/articles/claude-ai/claude-powerpoint-guide
- https://2slides.com/blog/how-to-use-claude-to-make-presentations-guide
