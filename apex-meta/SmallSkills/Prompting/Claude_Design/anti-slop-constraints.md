---
type: Playbook
title: Anti-Slop Constraints for Claude Design
description: Name the generic-AI-aesthetic fingerprint and ban it with explicit negative constraints.
tags: [claude-design, anti-slop, visual-design]
generated: { by: claude/sonnet-5, at: 2026-09-01T00:00:00Z }
sources:
  - id: buildwithangga
    resource: https://buildwithangga.com/tips/tips-claude-design-biar-hasil-desainmu-nggak-terlihat-generik-di-2026
    title: Anti-generic tips for Claude Design
  - id: mywestlord-skills
    resource: https://x.com/MyWestLord/article/2068064010600108267
    title: 45 Claude Design skills that target AI slop
  - id: mcpmarket-antislop
    resource: https://mcpmarket.com/tools/skills/design-anti-slop
    title: Design Anti-Slop skill description
status: stable
---

# The slop fingerprint

Absent constraints, generated interfaces converge on a recognizable set of patterns: a default sans font (commonly Inter, Roboto, or Arial), a purple-to-white or purple-to-cyan gradient hero, a three- or four-card grid, roughly 8px rounded corners, a subtle drop shadow, overused glassmorphism, floating 3D shapes, and marketing copy built from buzzwords like "empower" or "seamless."[^buildwithangga][^mcpmarket-antislop] The combination is distinctive enough that other designers can spot it at a glance.[^buildwithangga]

# Fix: force a committed aesthetic, then ban the fingerprint explicitly

Before any CSS gets written, require Claude to answer four questions and commit to an answer for each: purpose, tone, constraints, and differentiation — then pick one deliberate aesthetic extreme (brutalist, editorial, retro-futuristic, luxury, maximalist) instead of a safe middle ground.[^mywestlord-skills]

Then add an explicit negative-constraint block to the prompt or design-system doc. Negative constraints are easier for a model to evaluate than vague positive guidance because they reduce to a yes/no check rather than a judgment call. Example (values are illustrative — replace with your own locked choices):

```
Anti-slop constraints:
- One subtle gradient maximum, in one place only — never on every section
- Accent color used exactly once as a highlight — never as a full background
- No purple-to-cyan mesh gradients
- No Inter, Roboto, or Arial — use <your locked fonts> only
- No generic icon packs — custom-drawn glyphs only
- No stock photography or stock app screenshots — CSS-drawn or real content only
- No glassmorphism unless explicitly requested
- No buzzword copy ("empower", "seamless", "elevate") — write concrete, specific copy
```

# Exact values beat descriptive words

Passing exact hex codes produces consistent results across every component; passing a color name like "dark blue" gets interpreted inconsistently from one component to the next. The same logic applies to font names (name the exact typeface) and spacing (name the exact base unit) rather than descriptive words like "airy" or "tight."

# Related

- [Design System Lock](design-system-lock.md)
