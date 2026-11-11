"""Generate slot-inventory.json for the weekly dispersal slice.

Why a generator: the week holds 240+ slot occurrences with stable identifiers.
Hand-authoring that JSON is not viable and would not stay consistent with the
flow template. Edit the constants here, re-run, commit both files.

Grounding:
  Flow template         qmd #1a447e:47-57  (branch/label/minutes/lp_role arrays)
  3x3 = slots x iters   qmd #46ebe0:17-27, 48-49
  Weekday flow spans    SPEC-PRECAP-WEEK-ITERATIONS.okf.md (live Matrix 2)
  Operator minutes      OD-29  (M 3, P 2, C 30 standard, recap 1, break 12)
  Weekend flow count    OD-33  (two flows)
  Weekday re-cut        OD-45..OD-48  (declared 2026-11-09, DD-32/DD-33 closed)
  Weekend spans         OD-47  (12:00-16:00 back-to-back, DD-30 closed)
  Knee share            OD-49  (15%, DD-34 closed)

Spans marked DERIVED in span_status were computed from the operator's
"everything else half an hour earlier" rule, not declared one by one (WD-46).
"""

import json
from pathlib import Path

OUT = Path(__file__).with_name("slot-inventory.json")
DEMAND_PATH = Path(__file__).with_name("week-demand.json")
BLUEPRINT_PATH = Path(
    "C:/GitDev/apexai-os-meta/apex-meta/tools/"
    "project-improvement-orchestration-weekly/02-weekly-dispersal/week-blueprint.json"
)
BLUEPRINT = json.loads(BLUEPRINT_PATH.read_text(encoding="utf-8"))
DEMAND = json.loads(DEMAND_PATH.read_text(encoding="utf-8"))

REGIMES = BLUEPRINT["regimes"]
WEEKDAYS = REGIMES["weekday_project"]["days"] + REGIMES["weekday_plain"]["days"]
WEEKEND = REGIMES["weekend"]["days"]

FT = BLUEPRINT["flow_template"]
ITERATIONS = FT["iterations"]
SLOTS_PER_ITER = FT["slots_per_iteration"]

P_MIN = FT["minutes"]["P"]
M_MIN = FT["minutes"]["M"]
RECAP_MIN = FT["minutes"]["recap"]
BREAK_MIN = FT["minutes"]["break"]
FIXED_OVERHEAD = ITERATIONS * (P_MIN + M_MIN + RECAP_MIN) + BREAK_MIN  # 30

FLOW_MIN = FT["duration_min"]
WEEKDAY_FLOWS = BLUEPRINT["weekday_flows"]
WEEKEND_FLOWS = BLUEPRINT["weekend_flows"]

# OD-35: the physical Epic set and the week-table mapping.
PHYSICAL_EPICS = ["Martial Arts", "Dance", "S/BJJ", "General", "Knee"]
WEEK_TABLE_MAP = {
    "Strikes": "Martial Arts",
    "Kicks": "Martial Arts",
    "Dance": "Dance",
    "Moves": "Dance",
    "S/BJJ": "S/BJJ",
    "Running": "General",
    "Stretch": "General",
    "EFX": None,  # dropped by the operator
}

MENTAL_EPICS = list(DEMAND["mental"]["shares"].keys())
MENTAL_SHARES = DEMAND["mental"]["shares"]

KNEE_SHARE = DEMAND["physical"]["knee_share"]
SHARE_STEP = DEMAND["physical"]["share_step"]

_REST = DEMAND["physical"]["remaining_proportions"]


def _tie_order(epics):
    """Deterministic order for breaking a rounding tie on the 5% ladder.

    The Epic covering more week-table activities takes the spare step: it has
    more ground to cover in the same allocation. Name breaks a remaining tie so
    the result never depends on dict order.
    """
    breadth = {e: 0 for e in epics}
    for _, epic in WEEK_TABLE_MAP.items():
        if epic in breadth:
            breadth[epic] += 1
    return sorted(epics, key=lambda e: (-breadth[e], e))


def round_shares_to_step(shares, fixed_keys, tie_order):
    """Snap declared shares onto the 5-percentage-point ladder (OD-51).

    Largest remainder again, the same rule the slot quota uses (DD-27), but in
    units of 5 points rather than whole slots. Fixed keys keep their declared
    value exactly; the rest divide what is left, preserving their proportions.
    """
    step_units = round(1 / SHARE_STEP)
    fixed = {k: round(shares[k] / SHARE_STEP) for k in fixed_keys}
    rest = [k for k in shares if k not in fixed_keys]
    rest_units = step_units - sum(fixed.values())
    weight = sum(shares[k] for k in rest)
    raw = {k: shares[k] / weight * rest_units for k in rest}
    out = {k: int(v) for k, v in raw.items()}
    short = rest_units - sum(out.values())
    order = sorted(rest, key=lambda k: (-(raw[k] - out[k]), tie_order.index(k)))
    for k in order[:short]:
        out[k] += 1
    out.update(fixed)
    if sum(out.values()) != step_units:
        raise ValueError(f"5% ladder does not sum to 100%: {out}")
    return {k: out[k] * SHARE_STEP for k in shares}


_PHYS_EXACT = {k: v * (1 - KNEE_SHARE) for k, v in _REST.items()}
_PHYS_EXACT["Knee"] = KNEE_SHARE
PHYSICAL_SHARES = round_shares_to_step(
    _PHYS_EXACT, fixed_keys=("Knee",), tie_order=_tie_order(_PHYS_EXACT)
)

# Mental already sits on the ladder (40/20/20/20). Assert it rather than
# re-derive it, so a future edit off the ladder fails here instead of shipping.
for _epic, _share in MENTAL_SHARES.items():
    if abs(_share / SHARE_STEP - round(_share / SHARE_STEP)) > 1e-9:
        raise ValueError(
            f"mental share {_epic}={_share} is off the {SHARE_STEP:.0%} ladder (OD-51)"
        )

# Focus-day capacities loaded from week-demand.json, used to break quota ties deterministically.
MENTAL_FOCUS_CAPACITY = DEMAND["mental"]["focus_capacity"]
PHYSICAL_FOCUS_CAPACITY = DEMAND["physical"]["focus_capacity"]

# Practice surface outside the flows. Loaded from canonical week-blueprint.json.
ANCHORS = BLUEPRINT["anchors"]


def allocate_quota(total, shares, tie_capacity):
    """Largest remainder at the week (DD-27).

    Ties go to the Epic with the least focus-day capacity: the one the weekend
    reduction penalises most is compensated first. Deterministic, so moving a
    focus day moves the allocation with it.
    """
    raw = {k: v * total for k, v in shares.items()}
    out = {k: int(v) for k, v in raw.items()}
    short = total - sum(out.values())
    order = sorted(raw, key=lambda k: (-(raw[k] - out[k]), tie_capacity.get(k, 0)))
    for k in order[:short]:
        out[k] += 1
    return {
        "denominator": total,
        "declared_shares": {k: round(v, 4) for k, v in shares.items()},
        "raw": {k: round(v, 2) for k, v in raw.items()},
        "allocated": out,
        "realized_share": {k: round(v / total, 4) for k, v in out.items()},
        "rounding_rule": "largest remainder at the week (DD-27); ties to the "
                         "Epic with the least focus-day capacity",
        "tie_capacity": tie_capacity,
    }


# DD-39 / DD-40 resolved: the 18:30-19:30 evening physical course (60m) is
# an external course/VWC block and does NOT share the 72 x 2m in-Flow P slot
# denominator.
FOCUS_BLOCK_MIN = 0
FOCUS_DAY_ACTIVITY = DEMAND["physical"]["evening_physical_course"]


def physical_budget(inflow_min):
    """Verify physical minute budget once DD-40 is resolved (evening physical outside quota)."""
    prebound = {e: 0 for e in PHYSICAL_EPICS}
    for day, activity in FOCUS_DAY_ACTIVITY.items():
        epic = WEEK_TABLE_MAP.get(activity)
        if epic is None:
            raise ValueError(f"focus activity '{activity}' ({day}) maps to no Epic")
        prebound[epic] += FOCUS_BLOCK_MIN

    total = inflow_min + sum(prebound.values())
    entitlement = {e: PHYSICAL_SHARES[e] * total for e in PHYSICAL_EPICS}
    over = {e: prebound[e] - entitlement[e]
            for e in PHYSICAL_EPICS if prebound[e] > entitlement[e]}
    free_need = sum(max(0.0, entitlement[e] - prebound[e]) for e in PHYSICAL_EPICS)

    return {
        "basis": "72 x 2-min in-flow P slots (144 min); 18:30-19:30 evening course excluded from P quota denominator (DD-39 / DD-40 resolved)",
        "inflow_min": inflow_min,
        "focus_block_min_per_day": FOCUS_BLOCK_MIN,
        "focus_day_activity": FOCUS_DAY_ACTIVITY,
        "prebound_min": prebound,
        "total_physical_min": total,
        "entitlement_min": {e: round(v, 1) for e, v in entitlement.items()},
        "over_allocated_min": {e: round(v, 1) for e, v in over.items()},
        "free_minutes_available": inflow_min,
        "free_minutes_needed": round(free_need, 1),
        "feasible": not over and free_need <= inflow_min,
        "verdict": (
            "INFEASIBLE: the pre-bound focus blocks alone exceed the declared "
            "shares for " + ", ".join(sorted(over)) + ", and the Epics that are "
            f"still owed minutes need {free_need:.0f} against {inflow_min} "
            "available in-flow."
        ) if (over or free_need > inflow_min) else "feasible (DD-39 / DD-40 resolved: evening course outside 72x2m in-Flow P denominator)",
    }


def craft_block_min(duration_min):
    """Every flow is the same length (OD-34), so this is always 30.

    Kept as a function so a non-conformant duration fails loudly instead of
    silently producing a ragged flow.
    """
    if duration_min != FLOW_MIN:
        raise ValueError(
            f"flow duration {duration_min} != the {FLOW_MIN}-minute standard (OD-34)"
        )
    craft_total = duration_min - FIXED_OVERHEAD
    if craft_total % ITERATIONS:
        raise ValueError(
            f"{duration_min} min flow leaves {craft_total} craft min, "
            f"not divisible by {ITERATIONS} iterations"
        )
    return craft_total // ITERATIONS


def build_flow(day, regime, spec):
    craft = craft_block_min(spec["duration_min"])
    occurrences = []
    for i in range(1, ITERATIONS + 1):
        base = f"SO_{day[:3].upper()}_{spec['flow']}_I{i}"
        occurrences += [
            {"slot_id": f"{base}_P", "branch": "P", "role": "physical_micro",
             "minutes": P_MIN, "lp_role": "precap" if i == 1 else "main",
             "iteration": i, "quota_bearing": True},
            {"slot_id": f"{base}_M", "branch": "M", "role": "mental_micro",
             "minutes": M_MIN, "lp_role": "main",
             "iteration": i, "quota_bearing": True},
            {"slot_id": f"{base}_C", "branch": "C", "role": "craft_block",
             "minutes": craft, "lp_role": "main", "iteration": i,
             "quota_bearing": False, "binds": "openproject_work_package",
             "recap_min": RECAP_MIN,
             "recap_note": "trailing minute of this block, lp_role=recap; "
                           "not a separate slot (DD-29)"},
        ]
    occurrences.append(
        {"slot_id": f"SO_{day[:3].upper()}_{spec['flow']}_BREAK",
         "branch": "R", "role": "flow_break", "minutes": BREAK_MIN,
         "lp_role": "recap", "iteration": None, "quota_bearing": False,
         "note": "corpus annotates this slot 'Light snack & audiobook'"}
    )
    out = {
        "day": day, "regime": regime, "flow": spec["flow"],
        "start": spec.get("start"), "end": spec.get("end"),
        "duration_min": spec["duration_min"],
        "craft_block_min": craft,
        "fixed_overhead_min": FIXED_OVERHEAD,
        "slot_occurrences": occurrences,
    }
    if "span_status" in spec:
        out["span_status"] = spec["span_status"]
    return out


def _min_of_day(hhmm):
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def check_day_geometry(regime_key):
    """Fail loudly if two placed day elements overlap.

    The operator moves these times by voice ("half an hour earlier"), and the
    first such shift already drove the midday anchor into F2. Without this the
    inventory would generate a day that cannot be lived, and nothing downstream
    would notice.
    """
    regime = REGIMES[regime_key]
    specs = WEEKEND_FLOWS if regime_key == "weekend" else WEEKDAY_FLOWS
    spans = [(s["start"], s["end"], s["flow"]) for s in specs if s.get("start")]
    if regime_key != "weekend":
        spans += [(a["start"], a["end"], a["anchor"]) for a in ANCHORS]
    if regime["evening"]:
        e = regime["evening"]
        spans.append((e["start"], e["end"], e["label"]))

    spans.sort(key=lambda s: _min_of_day(s[0]))
    for (s1, e1, n1), (s2, e2, n2) in zip(spans, spans[1:]):
        if _min_of_day(s2) < _min_of_day(e1):
            raise ValueError(
                f"{regime_key}: '{n1}' ({s1}-{e1}) overlaps '{n2}' ({s2}-{e2})"
            )
    if regime_key != "weekend":
        total_min = sum(_min_of_day(e) - _min_of_day(s) for s, e, _ in spans)
        if total_min != 960 or spans[0][0] != "08:00" or spans[-1][1] != "24:00":
            raise ValueError(
                f"{regime_key}: expected 960 min across 08:00-24:00, got {total_min} min ({spans[0][0]}-{spans[-1][1]})"
            )
    return [{"start": s, "end": e, "element": n} for s, e, n in spans]


def build():
    timeline = {k: check_day_geometry(k) for k in REGIMES}
    flows = []
    for day in WEEKDAYS:
        for spec in WEEKDAY_FLOWS:
            flows.append(build_flow(day, "weekday", spec))
    for day in WEEKEND:
        for spec in WEEKEND_FLOWS:
            flows.append(build_flow(day, "weekend", spec))

    counts = {"P": 0, "M": 0, "C": 0, "R": 0}
    minutes = {"P": 0, "M": 0, "C": 0, "R": 0}
    for f in flows:
        for s in f["slot_occurrences"]:
            counts[s["branch"]] += 1
            minutes[s["branch"]] += s["minutes"]

    mental = allocate_quota(counts["M"], MENTAL_SHARES, MENTAL_FOCUS_CAPACITY)
    physical = allocate_quota(counts["P"], PHYSICAL_SHARES, PHYSICAL_FOCUS_CAPACITY)

    return {
        "schema_version": "1.0",
        "id": "MOA-SEQ-SLOT-INVENTORY",
        "blueprint_owner": BLUEPRINT["owner"],
        "as_of": BLUEPRINT["as_of"],
        "status": "working",
        "week_span": BLUEPRINT["week_span"],
        "operating_window": BLUEPRINT["operating_window"],
        "regimes": REGIMES,
        "status_merge_day": BLUEPRINT["status_merge_day"],
        "flow_template": BLUEPRINT["flow_template"],
        "anchors": ANCHORS,
        "day_timeline": {
            "note": "every placed element per regime in clock order; generated "
                    "and overlap-checked, so a shifted time cannot silently "
                    "collide with a flow",
            **timeline,
        },
        "flows": flows,
        "totals": {
            "slots_per_week": counts,
            "minutes_per_week": minutes,
            "flows_per_week": len(flows),
            "weekday_slots_per_day": {"P": 12, "M": 12, "C": 12, "R": 4},
            "weekend_slots_per_day": {"P": 6, "M": 6, "C": 6, "R": 2},
        },
        "quota": {
            "basis": "slot occurrences, not minutes (A-03, DD-02)",
            "note": "shares are operator dials and will change; the mechanism is "
                    "identical for both branches (OD-40)",
            "mental": dict(epics=MENTAL_EPICS, **mental),
            "physical": dict(
                epics=PHYSICAL_EPICS,
                week_table_mapping=WEEK_TABLE_MAP,
                dropped=["EFX"],
                budget=physical_budget(minutes["P"]),
                shares_status="Knee 15% DECLARED by the operator 2026-11-09 "
                              "(DD-34 closed); the remaining 85% keeps the "
                              "week-table proportions 3:2:1:1 (OD-49)",
                ladder_rule="DD-35 closed: declared shares snap to 5% steps "
                            "via round_shares_to_step() -> 35/25/10/15/15",
                **physical,
            ),
        },
    }


if __name__ == "__main__":
    data = build()
    OUT.write_text(json.dumps(data, indent=2) + "\n", encoding="utf-8")
    t = data["totals"]
    print(f"wrote {OUT.name}")
    print(f"  flows/week    {t['flows_per_week']}")
    print(f"  slots/week    {t['slots_per_week']}")
    print(f"  minutes/week  {t['minutes_per_week']}")
    for branch in ("mental", "physical"):
        q = data["quota"][branch]
        print(f"  {branch:9} {q['allocated']}  sum {sum(q['allocated'].values())}")
