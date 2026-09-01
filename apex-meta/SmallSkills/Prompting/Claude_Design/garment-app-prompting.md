---
type: Playbook
title: Translating Garment References Into UI Specs
description: Why picture-plus-prose fails for clothing-app UI, and the fix specific to garment design work.
tags: [claude-design, fashion, garment, spec-extraction]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: aiacademy-claude-design
    resource: https://academy.techpresso.co/prompts/claude-prompts-design
    title: 35 Claude Design Prompts
  - id: promptguide-ui
    resource: https://prompt-guide.com/en/prompts/claude-pour-creer-un-design-ui
    title: Prompt Claude for UI Design Creation
status: stable
---

# Why picture + vague description fails

Claude is not well suited to pure visual-taste judgment calls — whether a layout "feels right" or a silhouette reads correctly from a photo — since that requires human visual perception; it is strongest at structured specification and consistent execution of a written brief.[^aiacademy-claude-design] Handing over a reference photo plus prose like "make it look like this but more modern" asks for the weak capability instead of the strong one, which is where instructions tend to get lost or misapplied.

# Fix: extract the spec from the image yourself, then hand over the spec

Before prompting, convert the picture into concrete written values:

- Exact garment terms, not descriptive adjectives — "raglan sleeve," "empire waist," "drop shoulder," not "flowy" or "relaxed."
- Exact color values pulled from the reference, not color names — see [Anti-Slop Constraints](anti-slop-constraints.md) for why exact values beat descriptive words.
- Exact proportions and measurements where they drive the UI (card aspect ratio for a garment thumbnail, swatch size, size-chart grid).
- Real example content (actual product names, actual copy) rather than placeholder filler text, since real content forces a more accurate layout than generic filler does.[^promptguide-ui]

# Component-level locking for a garment app

Break the UI into named, independently locked components rather than re-describing the whole screen every time: a garment card, a measurement input, a color/fabric swatch picker, a size-chart table. Lock each one individually in the design-system doc once approved, and reference it by name in later prompts instead of redescribing it from scratch.

# Related

- [Design System Lock](design-system-lock.md)
- [Anti-Slop Constraints](anti-slop-constraints.md)
