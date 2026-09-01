---
type: Playbook
title: Prevent Drift and Overcorrection Across Turns
description: Structure feedback so later edits don't silently erase earlier locked decisions.
tags: [claude-design, context-engineering, iteration]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: anthropic-context-eng
    resource: https://www.anthropic.com/engineering/effective-context-engineering-for-ai-agents
    title: Effective context engineering for AI agents
  - id: mindstudio-refinement-loop
    resource: https://www.mindstudio.ai/blog/iterative-refinement-loop-claude-design-multimodal
    title: The Iterative Refinement Loop — How Claude Design Handles Multimodal Feedback
status: stable
---

# Why overcorrection happens

Context is a finite, competing resource: as a session grows, every earlier instruction competes for the same limited attention budget, and older or more diffuse content effectively carries less weight than what was said most recently.[^anthropic-context-eng] In multi-turn design refinement specifically, later instructions are generally treated as authoritative over earlier ones; a long, dense revision history can cause earlier constraints to get lost entirely rather than merely deprioritized.[^mindstudio-refinement-loop]

This is the mechanism behind "I asked for one fix and it forgot three things I'd already approved."

# Fix 1 — separate locked from open, every turn

State explicitly, every turn, what must not change and what is open for this edit. Carrying the original goal, the key decisions already made, and the currently locked constraints in every turn's prompt is what keeps a long refinement loop coherent.[^mindstudio-refinement-loop]

```
LOCKED (do not change):
- Header height 64px, no drop shadow, nav items: Home / Shop / Cart / Profile
- Primary color #1F2933, accent #FF6B4A used once max

OPEN FOR THIS TURN:
- Increase spacing between product cards
- Swap card corner radius from 4px to 12px
```

# Fix 2 — compress history instead of letting it balloon

After several turns, summarize rather than carry the full history forward: reduce to the original goal, the key decisions made, the locked constraints, and a short note of what changed each turn.[^mindstudio-refinement-loop] A bundle `log.md` file is the natural home for this compressed turn history.

# Fix 3 — restate, don't just reference

In a long session, restating a locked constraint explicitly is more reliable than saying "keep it like before" — a reference back to something said many turns ago competes poorly against instructions stated in the current turn.

# Fix 4 — organize prompts into labeled sections

Wrapping distinct kinds of content in their own clearly labeled sections (background, locked constraints, this turn's request) reduces the chance that one section gets misread as applying to another.[^anthropic-context-eng]

# Related

- [Design System Lock](design-system-lock.md)
- [Iteration Workflow](iteration-workflow.md)
