---
type: Playbook
title: Lock a Design System Before Requesting Screens
description: Front-load brand tokens and reference screens so Claude Design stops guessing and starts executing.
tags: [claude-design, design-system, tokens, onboarding]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: mindstudio-antislop
    resource: https://www.mindstudio.ai/blog/claude-design-avoid-ai-slop-design-system
    title: How to Avoid AI Slop When Using Claude Design
  - id: quasa-designer-tips
    resource: https://quasa.io/media/claude-design-looks-great-but-it-devours-your-token-limits-here-s-how-to-use-it-smartly
    title: 7 Pro Tips from Anthropic's design team
status: stable
---

# Problem

Claude Design has no memory of your brand between fresh sessions. Without an explicit design system, it falls back on the aggregate visual style of well-designed interfaces in its training data — in practice this converges on the same look every time: same default font, same accent blue, same card grid.[^mindstudio-antislop]

# Fix

Spend the first 1–2 hours of any new project building the full design system and 2–3 core reference screens *before* asking for any feature or flow. Once colors, typography, components, spacing, and layout rules are locked, Claude stops guessing and starts respecting the established visual language — cutting the number of prompts spent re-explaining "make it match our brand" on every new screen.[^quasa-designer-tips]

This has a direct information-efficiency payoff too: with token/spacing/color decisions already fixed, Claude spends effort on execution instead of re-deriving aesthetic choices from scratch on every screen.[^mindstudio-antislop]

# Design system doc template

Keep this as its own file and paste the relevant slice into every new Claude Design session for the project:

```
# [Project Name] Design System

## Typography
- Display: <font>, <weights>
- Body: <font>, <weights>
- Never use: <banned fonts>

## Color Palette
- Primary: #xxxxxx
- Secondary: #xxxxxx
- Accent (sparing use — see anti-slop-constraints.md): #xxxxxx
- Neutrals: #xxxxxx ... #xxxxxx

## Spacing & Shape
- Base unit: <px>
- Corner radius: <px> (state exceptions)
- Shadow style: <describe, or "none">

## Component Conventions
- Buttons: <states, sizes>
- Cards: <padding, border rules>
- Forms: <input style>

## Layout Rules
- Grid: <columns, gutters>
- Breakpoints: <values>

## Do Not Use
- <fonts, colors, patterns explicitly banned>

## Personality & Reference
- Mood words: <3-5 adjectives>
- Reference inspirations: <named products/styles, not vague adjectives>

## Changelog
- <date>: <decision locked>
```

# Related

- [Anti-Slop Constraints](anti-slop-constraints.md)
- [Context Persistence](context-persistence.md)
