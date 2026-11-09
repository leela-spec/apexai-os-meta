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

# OD-39: three regimes, not two. The flow count and slot counts are identical
# across both weekday regimes; they differ only in the evening block.
REGIMES = {
    "weekday_project": {
        "days": ["Monday", "Tuesday", "Wednesday"],
        "flows_per_day": 4,
        "evening": {"label": "Project night", "start": "20:00", "end": "21:30",
                    "minutes": 90,
                    "time_status": "DECLARED by the operator 2026-11-09 (DD-33 closed)"},
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
# The live Matrix 2 spans (F2 75 min, F4 105 min) were non-conformant; the
# operator declared the re-cut on 2026-11-09 and DD-32 is closed.
FLOW_MIN = 120

# OD-45: the operator re-cut the weekday on 2026-11-09. The morning anchor loses
# 30 minutes and everything after it moves 30 minutes earlier. F1 and F2 run
# back-to-back with no turnaround between them; the 12-minute in-flow break
# closes each flow regardless, so adjacency removes only the inter-flow gap.
WEEKDAY_FLOWS = [
    {"flow": "F1", "start": "08:30", "end": "10:30", "duration_min": FLOW_MIN,
     "span_status": "declared: morning anchor shortened to 30 min (OD-45)"},
    {"flow": "F2", "start": "10:30", "end": "12:30", "duration_min": FLOW_MIN,
     "span_status": "declared: adjacent to F1, no turnaround (OD-46)"},
    {"flow": "F3", "start": "13:45", "end": "15:45", "duration_min": FLOW_MIN,
     "span_status": "DERIVED: prior 14:15 shifted 30 min earlier (OD-45); the "
                    "15-min turnaround after the midday anchor is preserved"},
    {"flow": "F4", "start": "16:00", "end": "18:00", "duration_min": FLOW_MIN,
     "span_status": "DERIVED: prior 16:30 shifted 30 min earlier (OD-45)"},
]

# OD-47: weekend flows start at noon and run back-to-back, no pause between.
WEEKEND_FLOWS = [
    {"flow": "F1", "start": "12:00", "end": "14:00", "duration_min": FLOW_MIN,
     "span_status": "declared 2026-11-09 (DD-30 closed)"},
    {"flow": "F2", "start": "14:00", "end": "16:00", "duration_min": FLOW_MIN,
     "span_status": "declared: adjacent to F1, no pause (DD-30 closed)"},
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
# pattern-driven reading.
# OD-49 (DD-34 closed): the operator raised Knee to 15% and said to reduce the
# others. The remaining 85% keeps the week-table day-frequency proportions
# 3:2:1:1, so one declared number drives the whole table and no second
# transformation is invented on top of the operator's instruction.
KNEE_SHARE = 0.15
_REST = {"Martial Arts": 3 / 7, "Dance": 2 / 7, "S/BJJ": 1 / 7, "General": 1 / 7}
PHYSICAL_SHARES = {k: v * (1 - KNEE_SHARE) for k, v in _REST.items()}
PHYSICAL_SHARES["Knee"] = KNEE_SHARE

# Focus-day mental capacity, used only to break quota ties deterministically.
MENTAL_FOCUS_CAPACITY = {"Intention": 36, "Surrender": 12, "Breathing": 12, "ACIM": 6}
# Knee stays at 0 capacity: it has no focus day in the week table, so it holds
# no concentrated block and wins quota ties, which is the intended compensation.
PHYSICAL_FOCUS_CAPACITY = {"Martial Arts": 36, "Dance": 24,
                           "S/BJJ": 6, "General": 6, "Knee": 0}

# Practice surface outside the flows. Not quota-bearing (A-08).
ANCHORS = [
    {"anchor": "morning", "start": "08:00", "end": "08:30", "minutes": 30,
     "label": "Morning Routine, Meditation & Setup", "branch_hint": "M",
     "span_status": "declared: reduced from 60 min (OD-45)"},
    {"anchor": "midday", "start": "12:30", "end": "13:30", "minutes": 60,
     "label": "Midday Reset, Healthy Lunch & Fresh Air Walk", "branch_hint": "R",
     "span_status": "DERIVED: held at 12:30 because F2 now ends there. The "
                    "30-minute shift would have put it at 12:00, inside F2 "
                    "(OD-46 adjacency wins)"},
    {"anchor": "evening", "start": "19:00", "end": "20:00", "minutes": 60,
     "label": "Evening Block", "branch_hint": None, "bindable": False,
     "span_status": "declared 2026-11-09 (OD-48); content not yet specified"},
    {"anchor": "shutdown", "start": "21:30", "end": "22:00", "minutes": 30,
     "label": "Daily Shutdown: Outro, Day Evidence Commit & Workspace Reset",
     "branch_hint": None, "bindable": False,
     "span_status": "DERIVED: follows the 20:00-21:30 project night (DD-33)"},
    {"anchor": "night", "start": "22:00", "end": "24:00", "minutes": 120,
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
                shares_status="Knee 15% DECLARED by the operator 2026-11-09 "
                              "(DD-34 closed); the remaining 85% keeps the "
                              "week-table proportions 3:2:1:1 (OD-49)",
                open_question="DD-35: 'optimized to 5-minute iterations' is not "
                              "yet applied - see the spec ledger for the two "
                              "candidate readings",
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
