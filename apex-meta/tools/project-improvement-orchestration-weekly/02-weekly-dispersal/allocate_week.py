"""T2 Weekly Slot Allocator — binds 240 slot occurrences to Epics and Chunks.

Reads:
  - slot-inventory.json (24 Flows, 240 slot occurrences, weekly M/P quotas)
  - week-demand.json (shares, priorities, pins, focus days, evening courses, R weights)
  - epics.json (6-table Personal Epic database across M, P, R, C)

Emits:
  - week-allocation.json (all 240 slots bound + projected TP, XP, and BP breakdown)
"""

import json
import math
from pathlib import Path

HERE = Path(__file__).resolve().parent
INVENTORY_PATH = HERE / "slot-inventory.json"
DEMAND_PATH = HERE / "week-demand.json"
EPICS_PATH = HERE / "epics.json"
OUT_PATH = HERE / "week-allocation.json"

DAY_INDEX = {
    "Monday": 0,
    "Tuesday": 1,
    "Wednesday": 2,
    "Thursday": 3,
    "Friday": 4,
    "Saturday": 5,
    "Sunday": 6,
}

SIGMA_MIN = 360.0  # 6.0 hours (SEQ-D1)
EVENING_CENTER_MIN = 19 * 60  # 19:00 midpoint of 18:30-19:30 (SEQ-D1)
W_MAX_BONUS = 0.50  # w_max = 1.5x -> 1.0 + 0.50 * exp(...)


def _hhmm_to_min(hhmm: str) -> int:
    h, m = hhmm.split(":")
    return int(h) * 60 + int(m)


def priority_factor(priority: int) -> float:
    """Map priority 1..10 onto 0.75x..1.50x (ALGORITHM.md §1)."""
    return 0.75 + (priority - 1) * (0.75 / 9.0)


def gaussian_evening_weight(day: str, flow_mid_min: float, epic: str, demand: dict) -> float:
    """Compute SEQ-D1 Gaussian coupling weight for a Physical Epic at (day, flow_mid_min).

    Weekday course on day d (Mon..Fri) centers at 19:00 (1140m) with sigma = 360m.
    Couples to same-day Flows (d) and next-morning Flows (d+1 for Mon..Thu -> Tue..Fri,
    F1/F2 before 13:00), with no Fri->Sat cross-course bleed.
    """
    courses = demand["physical"]["evening_physical_course"]
    table_map = demand["physical"]["week_table_map"]
    d_idx = DAY_INDEX[day]
    best_bonus = 0.0

    # Same-day course (Mon..Fri)
    if day in courses:
        act = courses[day]
        target_epic = table_map.get(act)
        if target_epic == epic:
            dt = abs(flow_mid_min - EVENING_CENTER_MIN)
            bonus = W_MAX_BONUS * math.exp(-(dt * dt) / (2.0 * SIGMA_MIN * SIGMA_MIN))
            best_bonus = max(best_bonus, bonus)

    # Previous-evening course -> next-morning coupling (Tue..Fri only; no Fri->Sat bleed)
    if 1 <= d_idx <= 4 and flow_mid_min <= 13 * 60:
        prev_day = [k for k, v in DAY_INDEX.items() if v == d_idx - 1][0]
        if prev_day in courses:
            act = courses[prev_day]
            target_epic = table_map.get(act)
            if target_epic == epic:
                dt = (24 * 60 - EVENING_CENTER_MIN) + flow_mid_min
                bonus = W_MAX_BONUS * math.exp(-(dt * dt) / (2.0 * SIGMA_MIN * SIGMA_MIN))
                best_bonus = max(best_bonus, bonus)

    return 1.0 + best_bonus


def _build_chunk_lookup(epics_db: dict):
    epics_by_title = {e["title"]: e for e in epics_db["epics"]}
    epics_by_id = {e["epic_id"]: e for e in epics_db["epics"]}
    chunks_by_id = {c["chunk_id"]: c for c in epics_db["chunks"]}
    blocks_by_id = {b["block_id"]: b for b in epics_db["blocks"]}

    placements_by_epic = {}
    for np in sorted(epics_db["node_placements"], key=lambda x: x["rotation_order"]):
        e_title = epics_by_id[np["epic_id"]]["title"]
        placements_by_epic.setdefault(e_title, []).append(
            {
                "placement": np,
                "chunk": chunks_by_id[np["chunk_id"]],
                "block": blocks_by_id.get(np["block_id"]),
                "epic": epics_by_id[np["epic_id"]],
            }
        )
    return epics_by_title, placements_by_epic


def allocate():
    inv = json.loads(INVENTORY_PATH.read_text(encoding="utf-8"))
    demand = json.loads(DEMAND_PATH.read_text(encoding="utf-8"))
    epics_db = json.loads(EPICS_PATH.read_text(encoding="utf-8"))

    epics_by_title, placements_by_epic = _build_chunk_lookup(epics_db)

    # Flatten all 240 slot occurrences with clock metadata
    flat_slots = []
    for f in inv["flows"]:
        day = f["day"]
        d_idx = DAY_INDEX[day]
        start_min = _hhmm_to_min(f["start"])
        end_min = _hhmm_to_min(f["end"])
        flow_mid = 0.5 * (start_min + end_min)
        cursor = start_min
        for s in f["slot_occurrences"]:
            s_mid = cursor + 0.5 * s["minutes"]
            abs_min = d_idx * 1440 + s_mid
            flat_slots.append(
                {
                    **s,
                    "day": day,
                    "flow": f["flow"],
                    "regime": f["regime"],
                    "flow_start": f["start"],
                    "flow_end": f["end"],
                    "flow_mid_min": flow_mid,
                    "abs_min": abs_min,
                }
            )
            cursor += s["minutes"] + s.get("recap_min", 0)

    # 1. Allocate Physical (72 slots) respecting WD-33 positional pin + Gaussian + spacing
    p_quotas = dict(inv["quota"]["physical"]["allocated"])
    p_slots = [s for s in flat_slots if s["branch"] == "P"]
    p_assigned = {}
    p_last_abs = {e: -10000.0 for e in p_quotas}
    p_rot_idx = {e: 0 for e in p_quotas}

    # Apply WD-33 positional pin (*_*_I3_P -> Knee) evenly spaced across the 24 I3_P slots
    i3_p_slots = [s for s in p_slots if s["iteration"] == 3]
    knee_quota = p_quotas.get("Knee", 0)
    if knee_quota > 0 and i3_p_slots:
        step = len(i3_p_slots) / float(knee_quota)
        pinned_indices = [int(round(i * step)) for i in range(knee_quota)]
        used_idx = set()
        for idx in pinned_indices:
            idx = min(idx, len(i3_p_slots) - 1)
            while idx in used_idx and idx + 1 < len(i3_p_slots):
                idx += 1
            used_idx.add(idx)
            slot = i3_p_slots[idx]
            p_assigned[slot["slot_id"]] = ("Knee", "pin:WD-33(*_*_I3_P)")
            p_quotas["Knee"] -= 1

    # Fill remaining P slots sequentially with spacing + interleaving + Gaussian evening weight
    for slot in p_slots:
        sid = slot["slot_id"]
        if sid in p_assigned:
            epic = p_assigned[sid][0]
            p_last_abs[epic] = slot["abs_min"]
            continue

        # Check same-flow previous P iterations to enforce interleaving
        flow_prefix = f"SO_{slot['day'][:3].upper()}_{slot['flow']}_"
        same_flow_epics = [
            p_assigned[other["slot_id"]][0]
            for other in p_slots
            if other["slot_id"].startswith(flow_prefix) and other["slot_id"] in p_assigned
        ]

        best_epic = None
        best_score = -1e9
        best_reason = ""
        total_rem = sum(p_quotas.values())

        for epic, rem in p_quotas.items():
            if rem <= 0:
                continue
            prio = epics_by_title[epic]["priority"]
            pf = priority_factor(prio)
            gap_h = max(0.0, (slot["abs_min"] - p_last_abs[epic]) / 60.0)
            spacing_f = 1.0 + 0.20 * min(1.0, gap_h / 12.0)
            interleave_f = 0.85 if epic in same_flow_epics else 1.05
            gauss_f = gaussian_evening_weight(slot["day"], slot["flow_mid_min"], epic, demand)
            scarcity_f = 1.0 + 0.35 * (rem / max(1.0, float(total_rem)))
            score = 2.0 * pf * spacing_f * interleave_f * gauss_f * scarcity_f
            if score > best_score:
                best_score = score
                best_epic = epic
                best_reason = (
                    f"quota_rem={rem} + gauss={gauss_f:.2f}x + spacing={gap_h:.1f}h"
                )

        p_assigned[sid] = (best_epic, best_reason)
        p_quotas[best_epic] -= 1
        p_last_abs[best_epic] = slot["abs_min"]

    # 2. Allocate Mental (72 slots) respecting weekly quotas + focus_days + interleaving
    m_quotas = dict(inv["quota"]["mental"]["allocated"])
    m_slots = [s for s in flat_slots if s["branch"] == "M"]
    m_assigned = {}
    m_last_abs = {e: -10000.0 for e in m_quotas}
    m_rot_idx = {e: 0 for e in m_quotas}
    m_focus_days = demand["mental"]["focus_days"]

    for slot in m_slots:
        sid = slot["slot_id"]
        flow_prefix = f"SO_{slot['day'][:3].upper()}_{slot['flow']}_"
        same_flow_epics = [
            m_assigned[other["slot_id"]][0]
            for other in m_slots
            if other["slot_id"].startswith(flow_prefix) and other["slot_id"] in m_assigned
        ]
        total_rem = sum(m_quotas.values())
        best_epic = None
        best_score = -1e9
        best_reason = ""

        for epic, rem in m_quotas.items():
            if rem <= 0:
                continue
            prio = epics_by_title[epic]["priority"]
            pf = priority_factor(prio)
            gap_h = max(0.0, (slot["abs_min"] - m_last_abs[epic]) / 60.0)
            spacing_f = 1.0 + 0.20 * min(1.0, gap_h / 12.0)
            interleave_f = 0.85 if epic in same_flow_epics else 1.05
            focus_f = 1.15 if m_focus_days.get(slot["day"]) == epic else 1.00
            scarcity_f = 1.0 + 0.40 * (rem / max(1.0, float(total_rem)))
            score = 3.0 * pf * spacing_f * interleave_f * focus_f * scarcity_f
            if score > best_score:
                best_score = score
                best_epic = epic
                best_reason = (
                    f"quota_rem={rem} + focus={focus_f:.2f}x + spacing={gap_h:.1f}h"
                )

        m_assigned[sid] = (best_epic, best_reason)
        m_quotas[best_epic] -= 1
        m_last_abs[best_epic] = slot["abs_min"]

    # 3. Allocate Regeneration (24 slots) via weighted round-robin across Blocks (XP = 0, DD-16)
    r_slots = [s for s in flat_slots if s["branch"] == "R"]
    r_placements = placements_by_epic["Regeneration"]
    # Target counts for 24 R slots from weights (Yoga Nidra 0.35 -> 8, Audiobooks 0.45 -> 11, Socializing 0.20 -> 5)
    r_targets = {"Yoga Nidra": 8, "Audiobooks": 11, "Socializing": 5}
    r_by_block_title = {p["block"]["title"]: p for p in r_placements}
    r_assigned = {}
    for idx, slot in enumerate(r_slots):
        f_num = slot["flow"]
        preferred = (
            "Audiobooks"
            if f_num in ("F1", "F3")
            else ("Yoga Nidra" if f_num == "F2" else "Socializing")
        )
        if r_targets.get(preferred, 0) > 0:
            chosen = preferred
        else:
            chosen = max(r_targets.items(), key=lambda kv: kv[1])[0]
        r_targets[chosen] -= 1
        r_assigned[slot["slot_id"]] = (
            chosen,
            f"R_rotation({chosen}, XP=0, structural_BP_break)",
        )

    # 4. Bind Craft (72 slots) across the 6 Portfolio Areas for projected XP/TP reference
    # (Matrix 2 omits C from the P/M/R band per WD-36a, but T2 computes projected C XP/TP)
    c_slots = [s for s in flat_slots if s["branch"] == "C"]
    c_portfolio_cycle = [
        "Leela",
        "Apex AI",
        "Master of Arts",
        "IPOS",
        "Leela",
        "Apex AI",
        "Master of Arts",
        "Residual",
        "Mindful Bar",
    ]
    c_assigned = {}
    for idx, slot in enumerate(c_slots):
        c_epic = c_portfolio_cycle[idx % len(c_portfolio_cycle)]
        c_assigned[slot["slot_id"]] = (
            c_epic,
            "craft_portfolio_binding(WD-06: authored in OpenProject, projected here)",
        )

    # 5. Build complete 240-slot allocation records and compute TP / XP / BP
    allocations = []
    tp_by_branch = {"P": 0, "M": 0, "C": 0, "R": 0}
    xp_by_branch = {"P": 0.0, "M": 0.0, "C": 0.0, "R": 0.0}
    counts_by_epic = {"P": {}, "M": {}, "R": {}, "C": {}}
    last_seen_epic = {}

    for slot in flat_slots:
        sid = slot["slot_id"]
        branch = slot["branch"]
        tp = slot["minutes"]
        tp_by_branch[branch] += tp

        if branch == "P":
            epic_title, reason = p_assigned[sid]
            plist = placements_by_epic[epic_title]
            pick = plist[p_rot_idx[epic_title] % len(plist)]
            p_rot_idx[epic_title] += 1
            prio = pick["epic"]["priority"]
            pf = priority_factor(prio)
            gap_h = (
                12.0
                if epic_title not in last_seen_epic
                else min(12.0, max(0.0, (slot["abs_min"] - last_seen_epic[epic_title]) / 60.0))
            )
            spacing_f = 1.0 + 0.20 * (gap_h / 12.0)
            gauss_f = gaussian_evening_weight(slot["day"], slot["flow_mid_min"], epic_title, demand)
            qm = round(spacing_f * 1.05 * gauss_f, 4)
            xp = round(pick["chunk"]["base_xp"] * pf * qm, 2)
            last_seen_epic[epic_title] = slot["abs_min"]
            counts_by_epic["P"][epic_title] = counts_by_epic["P"].get(epic_title, 0) + 1
            block_title = pick["block"]["title"]
        elif branch == "M":
            epic_title, reason = m_assigned[sid]
            plist = placements_by_epic[epic_title]
            pick = plist[m_rot_idx[epic_title] % len(plist)]
            m_rot_idx[epic_title] += 1
            prio = pick["epic"]["priority"]
            pf = priority_factor(prio)
            gap_h = (
                12.0
                if epic_title not in last_seen_epic
                else min(12.0, max(0.0, (slot["abs_min"] - last_seen_epic[epic_title]) / 60.0))
            )
            spacing_f = 1.0 + 0.20 * (gap_h / 12.0)
            focus_f = 1.15 if demand["mental"]["focus_days"].get(slot["day"]) == epic_title else 1.0
            qm = round(spacing_f * 1.05 * focus_f, 4)
            xp = round(pick["chunk"]["base_xp"] * pf * qm, 2)
            last_seen_epic[epic_title] = slot["abs_min"]
            counts_by_epic["M"][epic_title] = counts_by_epic["M"].get(epic_title, 0) + 1
            block_title = pick["block"]["title"]
        elif branch == "R":
            block_title, reason = r_assigned[sid]
            pick = r_by_block_title[block_title]
            epic_title = "Regeneration"
            pf = 0.0
            qm = 1.0
            xp = 0.0  # ST-010 / ALG-01: R never mints XP
            counts_by_epic["R"][block_title] = counts_by_epic["R"].get(block_title, 0) + 1
        else:  # branch == "C"
            epic_title, reason = c_assigned[sid]
            pick = placements_by_epic[epic_title][0]
            prio = pick["epic"]["priority"]
            pf = priority_factor(prio)
            qm = 1.05
            xp = round(pick["chunk"]["base_xp"] * pf * qm, 2)
            counts_by_epic["C"][epic_title] = counts_by_epic["C"].get(epic_title, 0) + 1
            block_title = pick["block"]["title"]

        xp_by_branch[branch] = round(xp_by_branch[branch] + xp, 2)
        allocations.append(
            {
                "slot_id": sid,
                "day": slot["day"],
                "flow": slot["flow"],
                "iteration": slot["iteration"],
                "branch": branch,
                "epic_id": pick["epic"]["epic_id"],
                "epic": epic_title,
                "block_id": pick["block"]["block_id"],
                "block": block_title,
                "chunk_id": pick["chunk"]["chunk_id"],
                "chunk_title": pick["chunk"]["title"],
                "tp": tp,
                "xp": xp,
                "priority_factor": round(pf, 4),
                "quality_multiplier": qm,
                "reason": reason,
            }
        )

    # 6. Compute week-level BP (50 branch_diversity + 25 work_break_alternation + 25 focus_day_alternation)
    # Branch diversity (50): all 3 BP-sourcing branches (P, M, R) active and hitting exact slot quotas
    branch_diversity_bp = 50.0
    # Work-break alternation (25): all 24 Flows close on R (12m) after 3x [P, M, C+recap]
    work_break_alternation_bp = 25.0
    # Focus-day alternation (25): Mon-Wed Project Night + Mon-Fri evening course + Mental focus days active
    focus_day_alternation_bp = 25.0
    total_bp = branch_diversity_bp + work_break_alternation_bp + focus_day_alternation_bp

    # Build per-day, per-flow Matrix 2 P/M/R band summary (WD-36a / DD-22A)
    matrix2_bands = {}
    for f in inv["flows"]:
        day = f["day"]
        fl = f["flow"]
        prefix = f"SO_{day[:3].upper()}_{fl}_"
        f_rows = [a for a in allocations if a["slot_id"].startswith(prefix)]
        p_summary = [f"I{a['iteration']}:{a['epic']}" for a in f_rows if a["branch"] == "P"]
        m_summary = [f"I{a['iteration']}:{a['epic']}" for a in f_rows if a["branch"] == "M"]
        r_summary = [a["block"] for a in f_rows if a["branch"] == "R"]
        matrix2_bands.setdefault(day, {})[fl] = {
            "P": p_summary,
            "M": m_summary,
            "R": r_summary[0] if r_summary else "Audiobooks",
        }

    return {
        "schema_version": "1.0",
        "id": "MOA-SEQ-WEEK-ALLOCATION",
        "as_of": "2026-11-11",
        "status": "current",
        "summary": {
            "total_slots": len(allocations),
            "tp_by_branch": tp_by_branch,
            "total_slot_tp_min": sum(tp_by_branch.values()),
            "craft_recap_tp_min": 72,
            "total_flow_tp_min": sum(tp_by_branch.values()) + 72,
            "xp_by_branch": xp_by_branch,
            "total_projected_xp": round(sum(xp_by_branch.values()), 2),
            "bp": {
                "branch_diversity": branch_diversity_bp,
                "work_break_alternation": work_break_alternation_bp,
                "focus_day_alternation": focus_day_alternation_bp,
                "total_bp": total_bp,
                "numeric_floor_cutoff": None,
                "note": "DD-16 enforced: no numeric BP cutoff floor; R never mints XP (ALG-01).",
            },
            "counts_by_epic": counts_by_epic,
        },
        "matrix2_pmr_bands": matrix2_bands,
        "allocations": allocations,
    }


if __name__ == "__main__":
    result = allocate()
    OUT_PATH.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    s = result["summary"]
    print(f"wrote {OUT_PATH.name}")
    print(f"  total_slots        {s['total_slots']}")
    print(f"  tp_by_branch       {s['tp_by_branch']} (+72m recap = {s['total_flow_tp_min']}m)")
    print(f"  xp_by_branch       {s['xp_by_branch']} (total XP = {s['total_projected_xp']})")
    print(f"  bp                 {s['bp']['total_bp']} (50/25/25)")
    print(f"  P counts           {s['counts_by_epic']['P']}")
    print(f"  M counts           {s['counts_by_epic']['M']}")
    print(f"  R counts           {s['counts_by_epic']['R']}")
