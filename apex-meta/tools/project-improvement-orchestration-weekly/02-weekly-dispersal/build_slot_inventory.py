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
"""

import json
from pathlib import Path

OUT = Path(__file__).with_name("slot-inventory.json")

# OD-39: three regimes, not two. The flow count and slot counts are identical
# across both weekday regimes; they differ only in the evening block.
REGIMES = {
    "weekday_project": {
        "days": ["Monday", "Tuesday", "Wednesday"],
        "flows_per_day": 4,
        "evening": {"label": "Project night", "start": "20:00", "end": "20:30",
                    "minutes": 30,
                    "time_status": "READ FROM 'from 8 to 2030' - CONFIRM (DD-33)"},
    },
    "weekday_plain": {
        "days": ["Thursday", "Friday"],
        "flows_per_day": 4,
        "evening": None,
    },
    "weekend": {
        "days": ["Saturday", "Sunday"],
        "flows_per_day": 2,
        "evening": None,
    },
}
WEEKDAYS = REGIMES["weekday_project"]["days"] + REGIMES["weekday_plain"]["days"]
WEEKEND = REGIMES["weekend"]["days"]

ITERATIONS = 3          # the second 3 in "3x3"
SLOTS_PER_ITER = 3      # the first 3: the branch triple [P, M, C]

P_MIN, M_MIN, RECAP_MIN, BREAK_MIN = 2, 3, 1, 12
FIXED_OVERHEAD = ITERATIONS * (P_MIN + M_MIN + RECAP_MIN) + BREAK_MIN  # 30

# OD-34: EVERY flow is 120 minutes. One standard, no per-flow variation.
# The live Matrix 2 spans (F2 75 min, F4 105 min) are non-conformant and the
# day must be re-cut; the proposed re-cut is below. See DD-32.
FLOW_MIN = 120

WEEKDAY_FLOWS = [
    {"flow": "F1", "start": "09:00", "end": "11:00", "duration_min": FLOW_MIN},
    {"flow": "F2", "start": "11:15", "end": "13:15", "duration_min": FLOW_MIN,
     "span_status": "re-cut from 11:15-12:30, pending DD-32"},
    {"flow": "F3", "start": "14:15", "end": "16:15", "duration_min": FLOW_MIN,
     "span_status": "re-cut from 13:30-15:30, pending DD-32"},
    {"flow": "F4", "start": "16:30", "end": "18:30", "duration_min": FLOW_MIN,
     "span_status": "re-cut from 16:00-17:45, pending DD-32"},
]

# OD-33 two flows; OD-34 the same 120-minute standard. Spans not established.
WEEKEND_FLOWS = [
    {"flow": "F1", "start": None, "end": None, "duration_min": FLOW_MIN,
     "span_status": "assumed_pending_DD-30"},
    {"flow": "F2", "start": None, "end": None, "duration_min": FLOW_MIN,
     "span_status": "assumed_pending_DD-30"},
]

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

MENTAL_EPICS = ["Intention", "ACIM", "Surrender", "Breathing"]
MENTAL_SHARES = {"Intention": 0.40, "ACIM": 0.20, "Surrender": 0.20, "Breathing": 0.20}

# OD-40: physical uses the same share mechanism as mental, superseding A-06's
# pattern-driven reading. Shares below are DERIVED from the operator week table's
# day frequency, not declared by the operator - see DD-34.
PHYSICAL_SHARES = {
    "Martial Arts": 3 / 7,   # Strikes Mon, Kicks Tue + Fri
    "Dance": 2 / 7,          # Dance Wed, Moves Thu
    "S/BJJ": 1 / 7,          # Sat
    "General": 1 / 7,        # Running + Stretch Sun
    "Knee": 0.0,             # no week-table entry at all
}

# Focus-day mental capacity, used only to break quota ties deterministically.
MENTAL_FOCUS_CAPACITY = {"Intention": 36, "Surrender": 12, "Breathing": 12, "ACIM": 6}
PHYSICAL_FOCUS_CAPACITY = {"Martial Arts": 36, "Dance": 24,
                           "S/BJJ": 6, "General": 6, "Knee": 0}

# Practice surface outside the flows. Not quota-bearing (A-08).
ANCHORS = [
    {"anchor": "morning", "start": "08:00", "end": "09:00", "minutes": 60,
     "label": "Morning Routine, Meditation & Setup", "branch_hint": "M"},
    {"anchor": "midday", "start": "12:30", "end": "13:30", "minutes": 60,
     "label": "Midday Reset, Healthy Lunch & Fresh Air Walk", "branch_hint": "R"},
    {"anchor": "shutdown", "start": "21:00", "end": "21:30", "minutes": 30,
     "label": "Daily Shutdown: Outro, Day Evidence Commit & Workspace Reset",
     "branch_hint": None, "bindable": False},
    {"anchor": "night", "start": "21:30", "end": "24:00", "minutes": 150,
     "label": "Evening Regeneration, Rest, Reading & Night Recovery",
     "branch_hint": "R", "bindable": False,
     "note": "not a slot source. R is an ordinary branch (OD-41); its slots are "
             "the 24 in-flow breaks, which carry R content such as Yoga Nidra "
             "or reading. This window is life, not schedule."},
]


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


def build():
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
        "as_of": "2026-11-09",
        "status": "working",
        "week_span": "monday_to_sunday",
        "regimes": REGIMES,
        "status_merge_day": {
            "value": "Saturday_or_Sunday",
            "note": "operator ruling: either is acceptable; propagate everywhere "
                    "that hard-codes Saturday (A-12 closed)",
        },
        "flow_template": {
            "pattern": "3x3",
            "pattern_meaning": "3 slots per iteration x 3 iterations",
            "slots_per_iteration": SLOTS_PER_ITER,
            "iterations": ITERATIONS,
            "branch_cycle": ["P", "M", "C"],
            "closing_branch": "R",
            "minutes": {"P": P_MIN, "M": M_MIN, "craft_standard": 30,
                        "recap": RECAP_MIN, "break": BREAK_MIN},
            "fixed_overhead_min": FIXED_OVERHEAD,
            "flex_rule": "only the craft block absorbs a flow's residual time",
            "grounding": ["qmd #1a447e:47-57", "qmd #46ebe0:17-27,48-49", "OD-29"],
        },
        "anchors": ANCHORS,
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
                shares_status="DERIVED from week-table day frequency, NOT declared "
                              "by the operator - confirm or replace (DD-34)",
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
