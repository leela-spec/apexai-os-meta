# review.md — R-C Information Design

```yaml
reviewer_id: R-C
lens: information_design
model_profile: "ox-alpha via Hermes Agent session (openrouter/stealth-ox-alpha)"
execution_primitive: "campaign-orchestrator file-dispatched bounded packet; fresh task context, no generator conversation, no sibling reviewer access"
isolation_status: "ISOLATED per packet rules - bounded inputs only; note: same base model family as orchestrator, different task context. Recorded honestly; parent may weigh accordingly."
measurements_performed: none (no instrument available; all verdicts are structural/content inspections)
```

## a. Diagnosed root causes

1. **[F01 root] The weekly template's Matrix 2 makes layer confusion structural, not incidental.**
   Evidence: `weekly-command-brief-template.md` lines 40–45 — every flow×day cell contains `• S1: {{...}} • S2: ... • S3:` sprint goals. The skill contract (PrecapWeek SKILL.md `output_boundary.must_not_be: detailed_daily_plan`) is contradicted by its own template. Root cause: two audiences (weekly decider, daily executor) were designed into one grid.
2. **[F03 root] No delta concept exists anywhere in the daily template.**
   Evidence: `precap-next-day-brief-template.md` — closest construct is one line, `**Continuity from the week:**` (line 28). Change-information has no owned slot, so it can only appear by generator improvisation.
3. **[F04 root] Provenance is designed as an appendix, not as a property of facts.**
   Evidence: all three brief/card templates place provenance as the last-but-one section; no inline marker syntax exists for individual facts. Root cause: provenance treated as artifact metadata rather than per-claim attribute.
4. **[F05 root] Capacity deformation has semantics in doctrine but no presentation contract in templates.**
   Evidence: `calendar-planning-guidance.md` / `weekly-blueprint-meeting-example.md` define full/compressed/minimal/omitted deformation, while the weekly template reduces days to `FreeT:/Meets:` fragments and the daily template to a status enum. Nothing forces constrained days to LOOK constrained.
5. **[F09 root] Route decoration is repeated at every layer instead of owned once.**
   Evidence: Case-E baseline shows the same routing facts three times (card Prompt-access block, index table row, prompt header). Default-state and exception-state rendering are visually identical.
6. **[R-C-N1, new] Exception invisibility is systemic: statuses that matter (DEGRADED, OMITTED) use the same typographic weight as routine fields.** Evidence: Case-B daily brief buries "Status: OMITTED" mid-list; only the generator's prose ("named here so omission is explicit") saves it.

## b. Proposed information architecture

Three reading depths, each self-sufficient:

- **Depth 0 — Decision surface (top ~15 lines):** state, direction, next action, open decisions, capacity headline. Owns: nothing detailed; references down.
- **Depth 1 — Structure:** what changes (delta), what happens when (emphasis/order), what is blocked/deferred, exceptions rendered louder than defaults.
- **Depth 2 — Execution workspace:** flow cards + prompts; sprint detail lives ONLY here.

Ownership rules: change-facts own Depth-1 placement; provenance becomes a
per-fact tag `[~J1]` style resolving to a single source ledger; routing stated
once per flow with exceptions escalated to Depth 0.

## c. Redesigned example (full fidelity)

Redesign of Case-A daily brief top section (facts unchanged):

```markdown
# Next Day Brief — W36 TUE
STATE: READY_WITH_REVIEW | CAPACITY: standard (4 blocks) | CHANGES: 2
NEXT ACTION: Open F1 card → run S1 pre-flight
DECISIONS OPEN AT WEEK LEVEL: provisional-vocabulary (does not bite today)

CHANGED SINCE YESTERDAY
  F1 scope tightened   split walk main/subtree   [src ~MON-recap]
  F2 pulled earlier    fills MON spare block     [src ~MON-recap]

TODAY
  1. F1 Lika validation walk      PLANNED   → card f1
  2. F2 ACIM source mapping       COMPRESSED→ card f2
     F3                           OMITTED (Apex is a WED lane) [reason]

SOURCES: weekly=W36-brief · recap=MON-packet · freshness=1d
```

Weekly brief redesign principle (same mechanism): replace Matrix 2 grid with
the Day-emphasis table the baseline already improvised; delete all S-token
cells; keep priorities/sequence/blocked sections; add `CHANGED SINCE LAST WEEK`
block above Weekly direction.

## d. What should be removed

| Remove | From | Finding |
| :-- | :-- | :-- |
| All S1–S3 goal cells from weekly grid | weekly template Matrix 2 | F01 |
| Per-flow restatement of goals in daily brief flow blocks | daily template Flow section | F02 |
| Duplicate route lines in card + prompt headers | card/prompt templates | F09 |
| "Continuity from the week" single line (replaced by real delta block) | daily template | F03 |

## e. What moves between layers

| Content | From | To | Why |
| :-- | :-- | :-- | :-- |
| Sprint-level day plans | weekly Matrix 2 | daily layer (cards) | F01 wrong-layer |
| Change information | nowhere (implicit) | dedicated delta block, top of daily AND weekly | F03 |
| Provenance detail | terminal section | per-fact tags + one source ledger | F04 |
| Routing defaults | card+index+prompt triple | one statement per flow; exceptions escalate | F09 |

## f. Expected Q-job improvements (mechanism-based)

| Job | Mechanism | Claim |
| :-- | :-- | :-- |
| Q10/Q4 | S-cells removed from weekly → wrong-layer content structurally impossible | improves; verifiable by grep (objective) |
| Q11/Q1 | delta blocks become template-owned, first-position | improves; section-presence checkable |
| Q9 | per-fact tags put sources where facts are read → hop count to source drops to ≤1 | improves; traceable per fact |
| Q14/Q13 | exception-weighted rendering puts NEXT ACTION and DEGRADED/OMITTED above routine content | improves; requires judgment to confirm |
| Q5 | capacity headline at Depth 0 | improves on B-type weeks |
| Q2/Q7 | unchanged content, better position → neutral-to-positive | not_measured beyond structure |

## g. Risks/regressions

- Delta blocks on quiet days could become boilerplate noise → mitigate with explicit "no changes" state; detect via sampling quiet-day outputs.
- Inline provenance tags add symbol load → keep tags only on decisive facts; regression signal: operator complaints of clutter (Q7 first-screen test degrading).
- Removing route repetition risks offline execution lacking surface info → keep ONE authoritative route statement per prompt file; check Q16 stays PASS.
- Depth-0 compression may over-summarize complex weeks (C-type) → guard: decision surface must still name BOTH competing items; verify against case C.
