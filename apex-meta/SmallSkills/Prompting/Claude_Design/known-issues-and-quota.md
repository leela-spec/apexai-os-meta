---
type: Reference
title: Known Issues and Quota Management
description: Documented bugs and token-burn patterns to plan around.
tags: [claude-design, quota, bugs]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: muzli-week-in
    resource: https://muz.li/blog/claude-design-one-week-in-hacks-best-practices-tips-from-real-world-use/
    title: Claude Design, One Week In
  - id: quasa-designer-tips
    resource: https://quasa.io/media/claude-design-looks-great-but-it-devours-your-token-limits-here-s-how-to-use-it-smartly
    title: 7 Pro Tips from Anthropic's design team
status: stable
stale_after: 2026-12-01T00:00:00Z
---

# Inline comments occasionally vanish

The most-cited known bug: an inline comment placed on an element occasionally does not register before Claude reads the canvas. Workaround: if a comment doesn't appear to get picked up within a few seconds, copy its text and paste it directly into the main chat panel instead — this reliably works.[^muzli-week-in]

# Design-system setup is the expensive phase

The heaviest token/quota burn happens during initial design-system and core-screen setup, not during ordinary iteration. One reported case: two full design sessions consumed roughly 58% of a weekly Pro plan allowance.[^muzli-week-in] Treat each session as a planned production run rather than an open-ended sandbox.[^muzli-week-in]

# Spend one-time credits on experiments

If a one-time launch or promotional credit is available, spend it on exploratory experiments and save the recurring weekly allowance for production work.[^muzli-week-in]

# Connectors can pre-load context cheaply

Connecting Docs/Slack lets Claude read existing meeting notes or feedback threads and produce a first-pass set of design solutions unattended — reviewed afterward with fresh eyes, rather than manually re-typing that context into a prompt.[^quasa-designer-tips]

# Related

- [Iteration Workflow](iteration-workflow.md)
