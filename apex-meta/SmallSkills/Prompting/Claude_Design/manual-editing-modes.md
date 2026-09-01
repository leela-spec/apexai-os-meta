---
type: Playbook
title: Manual Editing Inside Claude Design (No Prompting Required)
description: When Claude misreads a request, these are the panels and settings you can use to fix it yourself directly, without going back through the AI.
tags: [claude-design, edit-mode, tweaks-panel, manual-control]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: fadedigital-playbook
    resource: https://fadedigital.ca/playbooks/claude-design-playbook.html
    title: The Claude Design Playbook
  - id: getpushtoprod
    resource: https://getpushtoprod.substack.com/p/everything-you-need-to-know-about
    title: Everything You Need to Know About Claude Design
  - id: builderio-review
    resource: https://www.builder.io/blog/claude-design
    title: Claude Design Review
  - id: pixso-guide
    resource: https://pixso.net/tips/claude-design-complete-guide/
    title: The Ultimate Guide to Claude Design
status: stable
---

# The five editing surfaces

When prompting isn't landing, prompting harder is usually not the fix. Claude Design exposes direct manual controls that bypass the AI entirely for exactly this situation:

| Mode | What it's for | Requires prompting? |
|---|---|---|
| Chat | Structural changes: add/remove sections, rearrange, shift overall direction | Yes |
| Inline Comments | Component-level changes: click an element, describe the fix, batch-send | Yes, targeted |
| **Edit Mode** | Direct manual tweak of one element's properties | **No** |
| Draw Mode | Sketch a box/circle on the canvas; Claude interprets the spatial intent | Minimal |
| Tweaks Panel | Claude-generated sliders for the current project | **No** |

# Edit Mode — the direct-settings panel

Enter Edit Mode and click any element on the canvas: a property inspector opens, typically on the right side, letting you change that element's background color, font family, font size, text content, height, width, and spacing directly — with no prompt and no AI involved in applying the change.[^fadedigital-playbook][^getpushtoprod]

This is the actual answer to "Claude isn't understanding what I want": for anything that reduces to a color, a size, a spacing value, or literal text content, stop describing it in words and change it directly in Edit Mode instead. It removes the translation step entirely, so there's nothing left for Claude to misread.

Typical uses: swapping placeholder copy for real product/brand text, correcting an exact color to match a brand hex value, nudging padding on a button, fixing a heading's font size.[^fadedigital-playbook]

# Tweaks Panel — generated sliders for live variant testing

For each project, Claude also generates a set of custom sliders specific to what it built — palette swaps, spacing controls, animation speed, rotation, glow intensity, layout variants. Opening the Tweaks panel and scrubbing a slider updates the canvas live, with no re-prompting.[^fadedigital-playbook] These sliders differ every time because they're generated for that specific project rather than drawn from a fixed control set.

# Draw Mode — for spatial ideas words don't capture well

You can draw directly on the canvas — sketch a box where a new section should go, or circle an existing element and add a short note beside it — and Claude interprets the drawing as intent.[^fadedigital-playbook] This is the fastest path when a change is spatial and would otherwise take many words to describe precisely.

# The hard boundary: this is not a Figma-style canvas

What you can't do: freely drag an element to an arbitrary position, or double-click to type text anywhere the way you would in Figma or Pixso — true free-form direct manipulation is not supported.[^pixso-guide] Edit Mode changes a selected element's existing properties; it does not let you reposition elements outside their current layout slot or rearrange structure by hand.[^builderio-review] Structural moves — reordering sections, changing layout composition — still route through chat, not through a manual panel.[^builderio-review]

# When to reach for manual edit vs. re-prompting

A practical rule used by operators: let generation and inline comments do roughly the first 90% of the work, and treat Edit Mode as the "last 10%" — final polish, not primary iteration.[^fadedigital-playbook] If you find yourself re-prompting the same small tweak more than once because Claude keeps missing it, that's the signal to stop prompting and go directly into Edit Mode or the Tweaks panel instead.

# Related

- [Iteration Workflow](iteration-workflow.md)
- [Context Persistence](context-persistence.md)
