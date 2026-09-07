# Handover — align the PATH Weekly accordion with the live Skill-Tree elements

**Date:** 2026-09-07 · **For:** Claude Code (implementation) · **From:** operator corrections, 2026-09-07 · **Status:** ready to implement; three decisions confirmed by operator, two assumptions flagged for review.

## Goal

The PATH Weekly accordion must stop using its own flat/neutral elements and instead reuse the **exact Skill-Tree elements, connectors, colours and animation that are already live**. The Skill-Tree _list view_ (`../../../lib/features/skill_tree/accessible_outline_view.dart`) is the reference for how each accordion row should look. This is a **realization on the existing codebase**, not a new design — almost every element already exists and must be reused, not re-invented.

## Grounding — read these first (they already do most of this)

- **The reference list view:** `../../../lib/features/skill_tree/accessible_outline_view.dart` — renders `LeelaCube(size, state, branchColor, gridDivisions: gridDivisionsForNodeType(type))` per row, Epic 3×3 / Block 2×2 / Chunk 1×1, with branch colour, level chip, and type. Copy this row grammar.
- **The cube element:** `../../../lib/design_system/components/leela_cube.dart`
    - `../../../lib/design_system/components/leela_cube_state.dart` — the real 3D illuminated cube. `gridDivisions` 3/2/1; `branchColor`; `state` carries lifecycle/fill/progress; optional `pulseListenable` (at most ONE pulsing cube per screen — use it for the selected row only).
- **Branch colours:** `../../../lib/design_system/tokens/leela_branch.dart` — P Physical `#FF5252`, M Mental `#40C4FF`, **C Craft `#FFD54F` (yellow)**, R Regeneration `#69F0AE`.
- **The connectors:** `../../../lib/features/skill_tree/cluster_connector_painter.dart` — the illuminated animated pulse/shimmer connectors. Reuse this painter (build `ConnectorSpec`s parent-cube → child-cube); do NOT keep the bespoke `path_accordion_connector.dart` shimmer.
- **The symbols:** `../../../lib/s_t_icon_map.dart` (`activityType`, `mediaType`, `branch`, `hierarchy` maps) + `../../../lib/design_system/tokens/leela_node_icon.dart` (`leelaIconForNode` resolves activity → media → generic).
- **The content data:** `../../../assets/mock/entities/epic_c5f6f061008d/chunk_dim.csv` — columns include `branch`, `activity_types`, `media_type`, `lvl`. This is the source the join must read.
- **The bar reference:** the Aug-1 accordion (`d8249b7d`) lane instrument; reconstruction at `../../design/reconstructions/path-weekly-accordion-d8249b7d.html`.
- **Current PATH code to change:** `../../../lib/features/path/presentation/path_weekly_accordion.dart`, `../../../lib/features/path/presentation/path_weekly_projection_builder.dart`, `../../../lib/features/path/presentation/path_chunk_detail_sheet.dart`, `../../../lib/pages/s_c_r_path_main.dart`. Retire `../../../lib/features/path/presentation/path_accordion_connector.dart`.

## Confirmed decisions (operator, 2026-09-07)

1. **Realized progress = sample values for this design pass**, clearly flagged as placeholder. Branch, level, activity type and media/app are **real** (content join); only _realized/placed TP_ is sample until a Run/Stats producer lands. Do not present sample realized data as real anywhere (label it in code + UI).
2. **Bar only** for the realization-vs-plan indicator this pass. Do **not** build the ring version yet.
3. **"App" symbol = `media_type`** icon (app / website / video / book / audiobook …) from `STIconMap.mediaType`.

## Work items

### W1 — Join PATH → content so rows carry branch, level, activity, media

The projection (`../../../lib/features/path/presentation/path_weekly_projection_builder.dart`) sets `branchCode:''` and has no level/activity/media. The catalog (`../../../lib/features/path/domain/path_target_catalog.dart` `PathTargetReference`) carries only `type/id/epicId/title/ancestorBlockIds`.

- Extend `PathTargetReference` (and the fixture catalog loader `../../../lib/features/path/data/fixture_path_target_catalog.dart`) to read `branch`, `lvl`, `activity_types`, `media_type` from the same content source the Skill Tree uses (`chunk_dim.csv` / `v_skill_tree_node_list`). Reuse the Skill-Tree adapter path rather than a parallel loader if practical.
- Populate `PathWeeklyChunkRow.branchCode` (real) and add `level`, `activityType`, `mediaType` fields. Give Epic/Block their branch where the content defines one (an Epic may span branches → may stay neutral; match Skill-Tree behaviour, `STF-11`).
- Epic/Block cube subdivision comes from type (3/2/1) via `gridDivisionsForNodeType`.

### W2 — Replace the neutral cube with the real `LeelaCube`

In `../../../lib/features/path/presentation/path_weekly_accordion.dart` delete the local `_levelCube` neutral helper and render `LeelaCube` exactly as `AccessibleOutlineView` does: `branchColor: LeelaBranch.colorOrUnknown(code)`, `gridDivisions` per level, `state: LeelaNodeVisualState(...)` carrying lifecycle + progress (progress = sample). Selected row's cube may take a `pulseListenable`; all others render statically illuminated (the cube's own gradient/rim/glow). Epic 3×3, Block 2×2, Chunk 1×1.

### W3 — Reuse the Skill-Tree connectors (illuminated + animated)

Retire `../../../lib/features/path/presentation/path_accordion_connector.dart`. Reuse `../../../lib/features/skill_tree/cluster_connector_painter.dart`: build `ConnectorSpec`s from measured cube anchor points (parent cube → each child cube), branch-coloured, and drive `shimmerProgress` / `selectionPulseProgress` / `revealProgress` from accordion-owned controllers with the same cadence the cluster uses. Keep the existing reduced-motion + suite-wide freeze discipline (`debugFreeze`). The connector links the **cube elements** across levels (Epic 3×3 → Block 2×2 → Chunk 1×1), not the row edges.

### W4 — Row layout, strictly left → right

Rebuild `_PathWeeklyRow` (and the parent header row) to this order:

1. **Connector** (W3) — illuminated line from the parent cube to this element's cube.
2. **Cube** (W2) — the element, in its branch colour.
3. **Name** — e.g. "L2L German" / "Flashcards" / "Quizlet".
4. **Three symbols** — Activity Type (`STIconMap.activityType[activity_types]`), App (`STIconMap.mediaType[media_type]`), Level (the `lvl` value — reuse the Skill-Tree `lvl` chip/plate treatment). Compact, monochrome-ish, in the space between name and selectors.
5. **TP selector**, then **Priority selector** (W5), far right.

The realization Bar (W6) sits under the name/symbols row (its own line), not in the L→R strip.

### W5 — TP & priority selectors (dual input)

Each selector offers **both**:

- **− / +** buttons on the left and right of the number (keep the 48×48 targets; TP step 5, priority step 1), wired to the existing serialized/optimistic commit path in `s_c_r_path_main.dart`.
- **Tap the number → dropdown of presets** for bigger jumps without repeated taps. **Proposed presets (confirm):** TP = 15 / 30 / 45 / 60 / 90 / 120 / 180 / 240; Priority = 1…10. Commit the chosen preset the same way as a stepper change.

### W6 — Realization-vs-plan **Bar** (single, lila, pattern-coded)

One horizontal bar per chunk, in the standard lila. **Interpretation to confirm at review:**

- Track = planned TP (the target amount).
- **Solid lila** = realized (how much is already done) — the part the Aug-1 chevron got right.
- **Patterned lila** (shades / broken lines, same hue) = planned-but-not-yet-realized remainder.
- A **TimeTarget marker** on the track = where realization _should_ be by now.
- **Over-plan** (realized > planned) = a denser pattern extending past the plan boundary.
- **Never a second colour** — only pattern differentiates realized / unrealized / over / under.
- Realized values are **sample** this pass (flag in code + a subtle "sample" affordance). Bar only — no ring.

### W7 — Surprise row placement

Move the derived Surprise row to the **top** of the children of the Epic/Block that has unassigned TP (right under that parent's header, before its children), and render it **only when that parent's unassigned TP > 0**. Keep the `PA-B12` semantics (derived, never authored, no demand-line id). Remove the tail placement.

### W8 — Symbols in the detail sheet

The three symbols (Activity Type, App/media, Level) must also appear in the per-chunk detail sheet (`../../../lib/features/path/presentation/path_chunk_detail_sheet.dart`) with the "more info" the sheet already carries (status / carryover / cadence / notes / remove).

## Data availability (be honest in UI + code)

|Element|Source|Real on master?|
|---|---|---|
|Branch colour|content `branch` (join)|**Yes**|
|Level symbol|content `lvl` (join)|**Yes**|
|Activity Type symbol|content `activity_types` (join)|**Yes**|
|App symbol|content `media_type` (join)|**Yes**|
|Cube shape (3×3/2×2/1×1)|node type|**Yes**|
|Connectors (shape + animation)|Skill-Tree painter|**Yes**|
|Realized / placed progress (bar fill, cube fill)|Run/Stats|**No — sample this pass**|
|TimeTarget marker|Algorithm|**No — sample this pass**|

## SSOT / materialization follow-up (do after the code lands)

- The cube/symbols now realize `STF-15` with **real** branch/level/activity/media in PATH → update the PATH↔STF-15 materialization edge and the PA-B13 edges; the realized-progress bar stays `to_write`/sample.
- Amend or add a decision-record note under `SSOT-D-043` recording: elements/connectors now reuse the live Skill-Tree grammar; branch/level/activity/media joined from content; realized progress remains sample pending a Run producer. Rebuild the registry + regenerate views; run `scripts/gates.py --since origin/master`.

## Verification

- `flutter analyze` clean on every touched file; `flutter test` green (extend the accordion widget tests: real `LeelaCube` present per level, branch colour applied, three symbols present, Surprise at top when >0 and absent at 0, selector dropdown opens and commits, bar renders with sample realized).
- Freeze any perpetual connector animation suite-wide (as today) so `pumpAndSettle` settles.
- Verify in the running app that the accordion visually matches `AccessibleOutlineView`'s element grammar.

## Open items to confirm during review

1. **Bar semantics** (W6) — the "target vs plan vs total" reading above; confirm what "total" adds beyond plan, and the exact pattern for over- vs under-realized.
2. **Selector presets** (W5) — the proposed TP/priority preset lists.
3. **Epic/Block branch** — whether a multi-branch Epic stays neutral (Skill-Tree behaviour) or takes a dominant branch colour.