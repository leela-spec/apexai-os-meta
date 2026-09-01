---
type: Playbook
title: Iteration Workflow Inside Claude Design
description: Concrete mechanics for fast, accurate revision cycles — comments, live sessions, and treating it as an agent.
tags: [claude-design, workflow, iteration]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: quasa-designer-tips
    resource: https://quasa.io/media/claude-design-looks-great-but-it-devours-your-token-limits-here-s-how-to-use-it-smartly
    title: 7 Pro Tips from Anthropic's design team
  - id: muzli-week-in
    resource: https://muz.li/blog/claude-design-one-week-in-hacks-best-practices-tips-from-real-world-use/
    title: Claude Design, One Week In
status: stable
---

# Point at the element, don't describe it

For a small fix, select the specific element and leave a targeted comment rather than writing a paragraph describing where the change goes. This is faster, and Claude applies the change more precisely than it does from a verbal description alone.[^quasa-designer-tips]

If a targeted comment still doesn't land correctly after one retry, stop re-prompting — for anything that reduces to a color, size, spacing value, or literal text, Edit Mode lets you change it directly with no AI in the loop at all. See [Manual Editing Modes](manual-editing-modes.md).

# Treat it as an agent, not a canvas

Claude Design is closer to an agentic tool than a pixel-pushing editor like Figma. It can generate interactive prototypes, animated flows, and even short video walkthroughs of intended behavior — ask for these directly instead of only requesting static mockups.[^quasa-designer-tips]

# Run live sessions with engineers

Because generation is near-instant, a live session with an engineer can stay focused on concepts, flows, and technical constraints instead of "I'll mock something up and show you next time" — ideas get resolved inside the same meeting.[^quasa-designer-tips]

# Always rewrite the generated copy

Placeholder copy from Claude Design is serviceable, not final. Shipping it unedited is one of the most visible slop signals in an otherwise solid design.[^muzli-week-in]

# Know when to go manual

Custom icons, spot illustrations, microcopy, and naming carry outsized weight on how a design actually feels, and are the areas most worth stepping out of agent mode to do by hand.[^quasa-designer-tips]

# Related

- [Context Persistence](context-persistence.md)
- [Known Issues and Quota](known-issues-and-quota.md)
