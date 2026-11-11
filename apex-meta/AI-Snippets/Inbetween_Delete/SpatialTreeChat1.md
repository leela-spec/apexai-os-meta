ecember 14. Move this project to Claude to keep working on it.

[](https://claude.ai/design/?noredir=1)

Skill tree third layer expansion

I want to extend the skill tree design from one layer (parent to child) to a third layer, so the grandchildren. use the principles as tehy are defined in the skill tree to build that

Start from code

Leela Visual System (design system)

I'll start by orienting myself — reading the repo and the design system.

Read repo README + explore structure

Find skill tree source files

Explore Leela design system

Ask user questions

Recreate skill tree screen pixel-perfectly

Extend to third layer (grandchildren)

Write github.md

Form's up — I'm asking how the third layer should unfold (own crown vs. expand-on-demand), grandchild size, what metadata survives at depth 3, and overflow handling. Meanwhile I'll keep reading the screen shell so I can recreate the current cluster exactly.

You answered

depth_model: Second crown — grandchildren form their own arc above each child, same grammar scaled down, Always-on full tree — every visible child shows its grandchildren at once, Radial sub-fan — grandchildren f…

metadata: Path membership marker, Branch colour only — no pills

overflow: Page the grandchild set like children do

breadcrumb: Adds the drilled child

viewport: Desktop/tablet ≥1024

notes: I did not understand a lot of the options

Picked three different models and said the options weren't clear — so I'll build them as real candidates you can look at. First, reading the screen shell.

Building the three candidates now.

Overlap and a missing done-state knockout. Fixing the layout math.

Three candidates, all built on the real cluster — the layout math, cube geometry, state table and tokens are ported from `bounded_cluster_layout.dart`, `leela_cube.dart` and the semantic-colour tokens, and the content is the actual `skill_tree_fixture_v1` subtree (LL German → 6 blocks → their sub-blocks and chunks).

- **1a Nested crowns** — every child becomes a stem with its own 42px equal-arc-length crown.
- **1b Focused unfold** — only the drilled child opens, at 52px with name pills; siblings drop to 45%; breadcrumb gains the child.
- **1c Radial sub-fan** — grandchildren orbit their child on a short arc with Direct-Tension connectors.

One extension was unavoidable to make any of them work: a child's _visual footprint_ in the crown is now its whole subtree's width, not just its cube plus metadata — otherwise nested crowns collide. Grandchildren carry no Lvl/Cnt pills (Branch colour + Path marker only) and overflow pages at five, per your answers.

Tell me which one and I'll take it to a single resolved screen.

Found issues — fixing…

Now binding it in the three `sc-for` blocks.

Metadata now recedes with its sibling in 1b (0.45 on labels, Lvl/Cnt pills and Path markers), while the opened Entertainment branch and the focus stem stay at full strength; 1a and 1c are unaffected.

Fixed — in 1b the recessed siblings now carry their name pills, Lvl/Cnt pills and Path markers down to 45% with the cube, so only the opened Entertainment branch and the focus stem read at full strength.

Edited Skill Tree - Third Layer.dc.html

Found issues — fixing…