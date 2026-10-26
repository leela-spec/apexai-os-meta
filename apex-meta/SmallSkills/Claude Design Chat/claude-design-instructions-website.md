---
type: Best Practice Guide
title: Instructing Claude Design — Website Projects
description: How another AI should brief Claude Design when the deliverable is a real website (not an app mockup).
tags: [claude-design, website, brief-template, okf-0.2]
---

# Scope

Use this guide when the deliverable is a standalone website (marketing site, portfolio/hub site,
landing page, multi-page site) that will be published and used as-is. Claude Design's native output
for this case (HTML/CSS/JS) is production-usable, not a throwaway sketch — treat the brief
accordingly: specify real content, not placeholders.

# Required brief structure (4-point, verified Anthropic recommendation)

Every brief to Claude Design must state, explicitly, in this order:

1. **Goal** — what is being built and why (e.g. "a hub site linking 4 separate business branches
   under one personal brand").
2. **Layout** — which pages/sections exist and in what order (e.g. Home → Branch A → Branch B →
   Contact). For multi-page sites, list every page up front; Claude Design supports clickable
   multi-page sites via its page/skill selection.
3. **Content** — the actual information to appear per section/page. Use real copy, not "lorem
   ipsum" — generic placeholder content measurably degrades output quality and brand fit.
4. **Audience** — who will use the result and what action they should take.

# Design system (brand consistency)

- State hex values for background/primary/accent colors and named font pairings explicitly.
  Do not say "modern and clean" — name exact values; vague adjectives produce generic output.
- If a design system already exists (logo, palette, type), supply it once at the top of the
  conversation and reference it in every subsequent prompt in that same session — Claude Design does
  not persist brand memory across separate chats.
- Before committing to a brief for real content, sanity-check the system first: run one throwaway
  generic prompt (e.g. "design a marketing landing page") and confirm the output already looks
  on-brand before spending the real brief on it.

# Navigation / IA (specific to multi-branch / hub sites)

- Instruct Claude Design to act as a UX architect: organize pages into Primary Navigation, Mega
  Menu (only if there are many branches), and Footer — do not leave menu structure implicit.
- Provide the full list of branches/destinations up front as fixed content, not to be invented by
  Claude Design. Each nav item needs: label, one-line purpose, and link target (internal page or
  external URL).
- Ask explicitly for a logical flow from Home → each branch → a target action (contact, follow,
  subscribe, etc.) for every branch, not just the home page.

# Responsiveness — decide this at the start, not as an afterthought

- Request phone, tablet, and desktop versions explicitly in the first brief, not later.
- Specify what changes at each breakpoint (stacked nav on mobile, condensed hero, etc.) — ask for a
  mobile-first layout plan, check mobile first, then desktop.

# Interaction and polish

- Specify interaction states explicitly: hover, active, error, empty, loading. Unstated states are
  usually skipped.
- Ask for 2–3 layout variations on the first pass for key pages (home, landing) before picking one
  — cheaper to compare now than to re-brief later.
- Ask Claude Design to explain its design decisions in plain language — this surfaces ambiguity in
  the brief before it compounds into further revisions.
- Request an accessibility (WCAG 2.1) review before export — accessibility also improves SEO.

# Export / handoff path (this determines downstream tooling, decide before you start)

| Need | Export |
|---|---|
| Quick visual review / sharing a link | PDF or internal URL |
| Present to stakeholders | PPTX |
| Clickable demo, no further dev needed | standalone HTML |
| Will become a real deployed product with backend/auth/db | hand off to Claude Code — do not treat exported static files as the final artifact |
| Publishing a static marketing/portfolio site as-is | native connectors (e.g. Vercel, Wix, Replit) or direct HTML export |

If the site is purely static (no backend, no auth, no database) the direct HTML/CSS/JS export IS the
production artifact — no further coding handoff is required.

# Common pitfalls to avoid in the brief

- Leaving content as placeholder text ("lorem ipsum", "Section Title Here") — always supply real copy.
- Giving vague style adjectives instead of hex/font values.
- Describing only the home page and letting Claude Design invent the rest of a multi-page site.
- Forgetting to ask for all three breakpoints up front.
- Treating a static-site export as needing a Claude Code handoff when it doesn't (wastes a step), or
  the reverse — treating a backend-dependent export as final when it needs one (ships something broken).

# Minimal checklist before finalizing

- [ ] Goal / Layout / Content / Audience all stated explicitly
- [ ] Exact hex colors + named fonts supplied
- [ ] Full page list + nav structure (all branches) supplied as fixed content
- [ ] Mobile / tablet / desktop requested
- [ ] Hover/error/empty/loading states requested where relevant
- [ ] Accessibility review requested
- [ ] Export target decided (static export vs. Claude Code handoff) before starting

# Sources

- https://www.anthropic.com/news/claude-design-anthropic-labs
- https://animaapp.com/blog/genai/how-to-publish-a-website-with-claude-design/
- https://academy.techpresso.co/prompts/claude-prompts-websites
- https://academy.techpresso.co/prompts/claude-prompts-design
- https://markusstoeger.com/en/masterai/claude-design-uebung-1
- https://aiopsschool.com/blog/claude-design-the-complete-master-guide/
