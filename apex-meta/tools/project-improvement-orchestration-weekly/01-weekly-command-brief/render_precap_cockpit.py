#!/usr/bin/env python3
"""Canonical Precap Week Schema Validator & Multi-Surface Compiler.

Single deterministic generator for:
  1. Interactive HTML Cockpit (v0.5 UX preserved, Mon-Sun T1 clock & T2 dispersal hydrated live)
  2. OKF v0.2 Weekly Command Brief Markdown report (D1-D12 operator output standard)
  3. Standalone presentation_handoff JSON packet for PrecapNextDay

SSOT Architecture:
  - Clock & standard anchors read dynamically from ../02-weekly-dispersal/week-blueprint.json
  - Weekly inventory, P/M/R bands, TP/XP/BP & Epic shares read from ../02-weekly-dispersal/{slot-inventory,week-demand,week-allocation}.json
  - Week-specific planning payload & G1 decisions validated against ./schemas/*.schema.json
"""

from __future__ import annotations

import argparse
import datetime
import html as html_lib
import json
import posixpath
import re
import sys
from pathlib import Path
from typing import Any, Dict, List, Optional, Tuple

PORTFOLIO_ORDER: List[Tuple[str, str]] = [
    ("leela", "Leela"),
    ("ipos", "IPOS"),
    ("master_of_arts", "Master of Arts"),
    ("apex_ai", "Apex AI"),
    ("mindful_bar", "Mindful Bar"),
    ("residual", "Residual"),
]

DAY_ORDER = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]


def _resolve_ref(ref: str, root_schema: dict) -> dict:
    if not ref.startswith("#/$defs/"):
        raise ValueError(f"Unsupported $ref target: {ref}")
    key = ref.split("/", 2)[2]
    return root_schema["$defs"][key]


def _check_type(val: Any, expected: Any) -> bool:
    types = expected if isinstance(expected, list) else [expected]
    for t in types:
        if t == "null" and val is None:
            return True
        if t == "boolean" and isinstance(val, bool):
            return True
        if t == "string" and isinstance(val, str):
            return True
        if t == "integer" and isinstance(val, int) and not isinstance(val, bool):
            return True
        if t == "number" and isinstance(val, (int, float)) and not isinstance(val, bool):
            return True
        if t == "array" and isinstance(val, list):
            return True
        if t == "object" and isinstance(val, dict):
            return True
    return False


def validate_against_schema(
    instance: Any, schema: dict, root_schema: Optional[dict] = None, path: str = "$"
) -> List[str]:
    """Lightweight deterministic Draft 2020-12 JSON Schema subset validator."""
    if root_schema is None:
        root_schema = schema
    errors: List[str] = []

    if "$ref" in schema:
        schema = _resolve_ref(schema["$ref"], root_schema)

    if "type" in schema and not _check_type(instance, schema["type"]):
        errors.append(f"{path}: expected type {schema['type']}, got {type(instance).__name__}")
        return errors

    if "const" in schema and instance != schema["const"]:
        errors.append(f"{path}: expected const {schema['const']!r}, got {instance!r}")

    if "enum" in schema and instance not in schema["enum"]:
        errors.append(f"{path}: value {instance!r} not in enum {schema['enum']}")

    if isinstance(instance, str):
        if "minLength" in schema and len(instance) < schema["minLength"]:
            errors.append(f"{path}: string length {len(instance)} < minLength {schema['minLength']}")
        if "pattern" in schema and not re.search(schema["pattern"], instance):
            errors.append(f"{path}: string {instance!r} does not match pattern {schema['pattern']!r}")

    if isinstance(instance, (int, float)) and not isinstance(instance, bool):
        if "minimum" in schema and instance < schema["minimum"]:
            errors.append(f"{path}: {instance} < minimum {schema['minimum']}")
        if "maximum" in schema and instance > schema["maximum"]:
            errors.append(f"{path}: {instance} > maximum {schema['maximum']}")

    if isinstance(instance, list):
        if "minItems" in schema and len(instance) < schema["minItems"]:
            errors.append(f"{path}: length {len(instance)} < minItems {schema['minItems']}")
        if "maxItems" in schema and len(instance) > schema["maxItems"]:
            errors.append(f"{path}: length {len(instance)} > maxItems {schema['maxItems']}")
        if "items" in schema:
            for idx, item in enumerate(instance):
                errors.extend(validate_against_schema(item, schema["items"], root_schema, f"{path}[{idx}]"))

    if isinstance(instance, dict):
        props = schema.get("properties", {})
        for req_key in schema.get("required", []):
            if req_key not in instance:
                errors.append(f"{path}: missing required field '{req_key}'")
        add_props = schema.get("additionalProperties", True)
        for k, v in instance.items():
            if k in props:
                errors.extend(validate_against_schema(v, props[k], root_schema, f"{path}.{k}"))
            elif add_props is False:
                errors.append(f"{path}: unexpected additional property '{k}'")
            elif isinstance(add_props, dict):
                errors.extend(validate_against_schema(v, add_props, root_schema, f"{path}.{k}"))

    return errors


def validate_semantics(
    cockpit: dict,
    handoff_schema: dict,
    cockpit_schema: dict,
    intake: Optional[dict] = None,
    intake_schema: Optional[dict] = None,
) -> List[str]:
    """Validate schemas + cross-portfolio, Mon-Sun, and cross-repo invariants."""
    errors = validate_against_schema(cockpit, cockpit_schema)
    handoff = cockpit.get("presentation_handoff", {})
    errors.extend(validate_against_schema(handoff, handoff_schema, path="$.presentation_handoff"))

    if intake is not None and intake_schema is not None:
        errors.extend(validate_against_schema(intake, intake_schema, path="$intake"))
        if intake.get("week_id") != cockpit.get("meta", {}).get("week_id"):
            errors.append(
                f"week_id mismatch between intake ({intake.get('week_id')}) and cockpit ({cockpit.get('meta', {}).get('week_id')})"
            )

    portfolios = cockpit.get("matrix1_portfolios", [])
    actual_pairs = [(p.get("id"), p.get("name")) for p in portfolios]
    if actual_pairs != PORTFOLIO_ORDER:
        errors.append(f"matrix1_portfolios must match canonical 6-Portfolio order {PORTFOLIO_ORDER}, got {actual_pairs}")

    for pi, p in enumerate(portfolios):
        for gi, g in enumerate(p.get("goals", []) + p.get("nice", [])):
            for cr in g.get("crossRepo", []):
                tr, tg = cr["targetRepo"], cr["targetGoal"]
                if not (0 <= tr < len(portfolios)):
                    errors.append(f"matrix1_portfolios[{pi}] goal[{gi}].crossRepo targetRepo out of range: {tr}")
                elif not (0 <= tg < len(portfolios[tr]["goals"])):
                    errors.append(f"matrix1_portfolios[{pi}] goal[{gi}].crossRepo targetGoal out of range: {tg}")

    days = [d.get("day") for d in cockpit.get("matrix2_days", [])]
    if days != DAY_ORDER:
        errors.append(f"matrix2_days must be ordered Monday..Sunday, got {days}")

    h_areas = [(a.get("portfolio_id"), a.get("label")) for a in handoff.get("six_portfolio_areas", [])]
    if h_areas != PORTFOLIO_ORDER:
        errors.append(f"presentation_handoff.six_portfolio_areas must match {PORTFOLIO_ORDER}, got {h_areas}")

    meta = cockpit.get("meta", {})
    if handoff.get("week") != meta.get("week_id"):
        errors.append(f"handoff week ({handoff.get('week')}) != meta.week_id ({meta.get('week_id')})")
    if handoff.get("date_range") != {"start": meta.get("date_start"), "end": meta.get("date_end")}:
        errors.append("handoff date_range must match meta.date_start and meta.date_end")

    return errors


def _has_verified_override(item: dict) -> bool:
    return bool(
        item.get("ov")
        and item.get("sysDef")
        and item.get("opChoice")
        and item["sysDef"] != item["opChoice"]
        and item.get("srcRef")
    )


def _esc(val: Any) -> str:
    return html_lib.escape("" if val is None else str(val), quote=True)


def compute_dispersal_stats(
    blueprint: dict, demand: dict, inventory: dict, allocation: dict, meta: dict
) -> dict:
    """Compute canonical T1 clock + T2 Dispersal stats directly from 02-weekly-dispersal/."""
    summary = allocation["summary"]
    tp = summary["tp_by_branch"]
    xp = summary["xp_by_branch"]
    recap_min = int(summary["craft_recap_tp_min"])
    total_flow_tp_min = int(summary["total_flow_tp_min"])
    total_slots = int(summary["total_slots"])
    craft_slots = sum(summary["counts_by_epic"]["C"].values())
    total_flows = len(inventory["flows"])
    wkd_flows = sum(1 for f in inventory["flows"] if f["regime"] == "weekday")
    wknd_flows = total_flows - wkd_flows

    gross_hours = round(total_flow_tp_min / 60.0, 1)
    craft_hours = round(tp["C"] / 60.0, 1)
    sub_hours = float(meta.get("meeting_subtraction_hours", 0.0))
    net_craft_hours = round(max(0.0, craft_hours - sub_hours), 1)
    non_craft_min = total_flow_tp_min - tp["C"]
    non_craft_hours = round(non_craft_min / 60.0, 1)

    ft = blueprint["flow_template"]
    mins = ft["minutes"]
    anchors_by_id = {a["anchor"]: a for a in blueprint["anchors"]}
    wkd_flow_map = {f["flow"]: f for f in blueprint["weekday_flows"]}
    wknd_flow_map = {f["flow"]: f for f in blueprint["weekend_flows"]}

    return {
        "total_flows": total_flows,
        "wkd_flows": wkd_flows,
        "wknd_flows": wknd_flows,
        "total_slots": total_slots,
        "craft_slots": craft_slots,
        "tp": tp,
        "xp": xp,
        "total_projected_xp": summary["total_projected_xp"],
        "bp": summary["bp"],
        "counts_by_epic": summary["counts_by_epic"],
        "recap_min": recap_min,
        "total_flow_tp_min": total_flow_tp_min,
        "gross_hours": gross_hours,
        "craft_hours": craft_hours,
        "sub_hours": sub_hours,
        "net_craft_hours": net_craft_hours,
        "non_craft_min": non_craft_min,
        "non_craft_hours": non_craft_hours,
        "flow_mins": mins,
        "flow_duration": ft["duration_min"],
        "flow_pattern": ft["pattern"],
        "anchors": anchors_by_id,
        "wkd_flow_map": wkd_flow_map,
        "wknd_flow_map": wknd_flow_map,
        "regimes": blueprint["regimes"],
        "op_win": blueprint["operating_window"],
        "status_merge_day": blueprint["status_merge_day"]["value"],
        "pmr_bands": allocation["matrix2_pmr_bands"],
        "demand": demand,
    }


def _compact_band(band: dict) -> str:
    """Render concise DD-22A read-only P/M/R band from week-allocation.json."""
    def _short(items: List[str]) -> str:
        seen: List[str] = []
        for it in items:
            epic = it.split(":", 1)[1] if ":" in it else it
            if epic not in seen:
                seen.append(epic)
        return "/".join(seen) if len(seen) <= 3 else ", ".join(seen)

    p_str = _short(band.get("P", []))
    m_str = _short(band.get("M", []))
    r_str = band.get("R", "Audiobooks")
    return f"P: {p_str} · M: {m_str} · R: {r_str}"


def build_runtime_payload(cockpit: dict, stats: dict) -> dict:
    """Merge live T1 clock & T2 dispersal values into compact runtime state for HTML/JS."""
    meta = cockpit["meta"]
    decisions = cockpit["decisions"]
    portfolios = cockpit["matrix1_portfolios"]
    days = cockpit["matrix2_days"]
    residuals = cockpit["residuals"]

    l1_count = sum(len(p["goals"]) for p in portfolios)
    l2_count = sum(len(p["nice"]) for p in portfolios)
    ov_count = sum(1 for b in ("new", "ongoing") for it in decisions[b] if _has_verified_override(it))
    deferred_count = len(residuals["longlist_deferrals"])
    op_chip = "[OP-OFFLINE]" if meta["op_status"] == "OFFLINE_FALLBACK" else "[OP-ONLINE]"

    metrics = [
        {
            "value": f"{stats['net_craft_hours']}h / {stats['craft_hours']}h C",
            "name": "Net Craft capacity (T1)",
            "note": f"{stats['gross_hours']}h gross ({stats['total_flow_tp_min']:,}m) · minus {stats['sub_hours']}h meetings · {stats['recap_min']}m recap in {stats['non_craft_hours']}h P/M/R",
        },
        {
            "value": f"{stats['total_flows']} Flows",
            "name": "Weekly Flow blocks",
            "note": f"{stats['wkd_flows']} weekday (Mon–Fri {stats['op_win']['weekday']['start']}–{stats['op_win']['weekday']['end']}) + {stats['wknd_flows']} weekend ({stats['op_win']['weekend']['start']}–{stats['op_win']['weekend']['end']})",
        },
        {
            "value": f"{stats['craft_slots']} Sprints",
            "name": "3x3 Craft sprints",
            "note": f"3 × {stats['flow_mins']['craft_standard']}m Craft C per Flow + DD-22A P/M/R ({stats['total_slots']} slot_ids)",
        },
        {
            "value": f"6 Areas · {l1_count} L1",
            "name": "6 Portfolio areas",
            "note": f"Leela · IPOS · Master of Arts · Apex AI · Mindful Bar · Residual ({l2_count} L2)",
        },
        {
            "value": f"G1 {meta['g1_status']}",
            "name": "Gate & source readiness",
            "note": f"{op_chip} · Cal {meta['calendar_status']} · {ov_count} overrides · {deferred_count} deferrals",
        },
    ]

    # Dynamic STANDARD decision card synthesized strictly from week-blueprint.json & week-demand.json
    anchors = stats["anchors"]
    wkd = stats["wkd_flow_map"]
    wknd = stats["wknd_flow_map"]
    regs = stats["regimes"]
    mins = stats["flow_mins"]
    tp = stats["tp"]
    standard_card = {
        "key": "STANDARD",
        "cls": "ok",
        "title": "Blueprint clock & baseline",
        "previews": [
            ["Clock authority (T1)", "week-blueprint.json (Mon-Sun)"],
            ["Flow cadence", f"{regs['weekday_project']['flows_per_day']}/day Mon-Fri · {regs['weekend']['flows_per_day']}/day Sat-Sun ({stats['total_flows']}/wk)"],
            [
                "Evening regime",
                f"Mon-Wed {regs['weekday_project']['evening']['label']} · Thu-Fri {regs['weekday_plain']['evening']['label']} ({regs['weekday_project']['evening']['start']}-{regs['weekday_project']['evening']['end']})",
            ],
            [
                "Daily anchors & outro",
                f"{stats['op_win']['weekday']['start']}-{stats['op_win']['weekday']['end']} · Day Outro {stats['op_win']['weekday']['day_outro']}",
            ],
        ],
        "items": [
            {
                "name": "Canonical clock owner (T1 / D018)",
                "val": "02-weekly-dispersal/week-blueprint.json",
                "detail": (
                    f"Sole owner of timestamps: Mon-Fri {stats['op_win']['weekday']['start']}-{stats['op_win']['weekday']['end']} "
                    f"({stats['op_win']['weekday']['duration_min']}m): "
                    f"Morning {anchors['morning']['start']}-{anchors['morning']['end']}, "
                    f"F1 {wkd['F1']['start']}-{wkd['F1']['end']}, F2 {wkd['F2']['start']}-{wkd['F2']['end']}, "
                    f"Lunch {anchors['lunch']['start']}-{anchors['lunch']['end']}, "
                    f"F3 {wkd['F3']['start']}-{wkd['F3']['end']}, "
                    f"Break {anchors['afternoon_break']['start']}-{anchors['afternoon_break']['end']}, "
                    f"Finanzen/2Do {anchors['finanzen_2do']['start']}-{anchors['finanzen_2do']['end']}, "
                    f"F4 {wkd['F4']['start']}-{wkd['F4']['end']}, "
                    f"Evening Physical {anchors['evening_physical']['start']}-{anchors['evening_physical']['end']}, "
                    f"Abend {anchors['abend']['start']}-{anchors['abend']['end']}, "
                    f"{regs['weekday_project']['evening']['label']}/{regs['weekday_plain']['evening']['label']} {regs['weekday_project']['evening']['start']}-{regs['weekday_project']['evening']['end']}, "
                    f"Day Outro {anchors['day_outro']['start']}-{anchors['day_outro']['end']}, "
                    f"Freizeit {anchors['freizeit']['start']}-{anchors['freizeit']['end']}, "
                    f"Sleep Routine {anchors['sleep_routine']['start']}-{anchors['sleep_routine']['end']}."
                ),
                "gate": "BASELINE",
                "sysDef": None,
                "opChoice": None,
                "srcRef": "02-weekly-dispersal/week-blueprint.json",
                "ov": False,
            },
            {
                "name": "Weekend regime (D017 / T1)",
                "val": f"Sat & Sun {stats['op_win']['weekend']['start']}-{stats['op_win']['weekend']['end']} (2 Flows each)",
                "detail": (
                    f"Saturday & Sunday run F1 ({wknd['F1']['start']}-{wknd['F1']['end']}) "
                    f"and F2 ({wknd['F2']['start']}-{wknd['F2']['end']}). "
                    f"StatusMerge & PrecapWeek run on {stats['status_merge_day']}."
                ),
                "gate": "BASELINE",
                "sysDef": None,
                "opChoice": None,
                "srcRef": "02-weekly-dispersal/week-blueprint.json",
                "ov": False,
            },
            {
                "name": "Internal Flow anatomy & recap accounting",
                "val": f"3 x (P {mins['P']}m + M {mins['M']}m + C {mins['craft_standard']}m + {mins['recap']}m recap) + R {mins['break']}m = {stats['flow_duration']}m",
                "detail": (
                    f"{stats['total_flows']} Flows = {stats['total_flow_tp_min']:,}m ({stats['gross_hours']}h) gross = "
                    f"{tp['C']:,}m ({stats['craft_hours']}h) C + {stats['non_craft_min']}m ({stats['non_craft_hours']}h) non-Craft "
                    f"({tp['P']}m P + {tp['M']}m M + {tp['R']}m R + {stats['recap_min']}m trailing recap_min across {stats['total_slots']} slot_ids). "
                    f"Evening 18:30-19:30 Physical sits outside the 72x2m P quota (DD-39)."
                ),
                "gate": "BASELINE",
                "sysDef": None,
                "opChoice": None,
                "srcRef": "02-weekly-dispersal/slot-inventory.json",
                "ov": False,
            },
        ],
    }

    def _build_cat_card(key: str, cls: str, title: str, items: List[dict]) -> dict:
        previews = []
        for it in items[:4]:
            pk = it.get("preview_key") or it["name"]
            pv = it.get("preview_val") or it["val"]
            previews.append([pk, pv])
        return {"key": key, "cls": cls, "title": title, "previews": previews, "items": items}

    decision_cards = [
        _build_cat_card("NEW", "warn", "Weekly choices & G1 gate", decisions["new"]),
        _build_cat_card("ONGOING", "muted", "Calendar holds & standing rules", decisions["ongoing"]),
        standard_card,
    ]

    # Top-priority preview refs (first 3 critical goals, or first L1 of top 3 repos)
    top_refs: List[dict] = []
    for ri, repo in enumerate(portfolios):
        for ni, g in enumerate(repo["goals"]):
            if g.get("critical") and len(top_refs) < 3:
                top_refs.append({"ri": ri, "ni": ni, "slot": f"Priority {len(top_refs)+1} · {repo['name']}"})
                break
    for ri, repo in enumerate(portfolios):
        if len(top_refs) >= 3:
            break
        if repo["goals"] and not any(x["ri"] == ri for x in top_refs):
            top_refs.append({"ri": ri, "ni": 0, "slot": f"Priority {len(top_refs)+1} · {repo['name']}"})

    # Hydrate days with DD-22A P/M/R bands from week-allocation.json
    hydrated_days = []
    for d in days:
        day_name = d["day"]
        day_bands = stats["pmr_bands"].get(day_name, {})
        h_flows = {}
        for fid, fobj in d["flows"].items():
            band = day_bands.get(fid, {})
            h_flows[fid] = {
                "owner": fobj["owner"],
                "pmr": _compact_band(band) if band else "P/M/R bound via week-allocation.json",
                "cell_notes": fobj.get("cell_notes", []),
                "sprints": fobj["sprints"],
            }
        hydrated_days.append({
            "day": day_name,
            "short": d["short"],
            "date": d["date"],
            "role": d["role"],
            "holds": d["holds"],
            "evening_note": d["evening_note"],
            "flows": h_flows,
        })

    return {
        "source": {
            "primary": meta["source_links"]["primary"],
            "primaryLabel": meta["source_links"]["primaryLabel"],
            "secondary": meta["source_links"]["secondary"],
            "secondaryLabel": meta["source_links"]["secondaryLabel"],
            "spec": meta["source_links"]["spec"],
            "weekId": meta["week_id"],
            "dateSpanLabel": meta["date_span_label"],
            "bannerBadge": meta["banner_badge"],
            "intro": meta["intro"],
            "state": f"{meta['g1_status']} · {op_chip}",
            "opChip": op_chip,
        },
        "metrics": metrics,
        "decisionCards": decision_cards,
        "topPriorityRefs": top_refs,
        "repos": portfolios,
        "days": hydrated_days,
        "personalFocus": cockpit["personal_focus"],
    }


def _render_matrix2_rows_html(runtime: dict, stats: dict, handoff: dict) -> str:
    """Build single fit-to-width Mon-Sun timetable rows strictly from week-blueprint.json & week-demand.json."""
    days = runtime["days"]
    anchors = stats["anchors"]
    wkd = stats["wkd_flow_map"]
    wknd = stats["wknd_flow_map"]
    regs = stats["regimes"]
    courses = stats["demand"]["physical"]["evening_physical_course"]

    def _wk_flow_cell(d_idx: int, fid: str, win: str) -> str:
        d = days[d_idx]
        fo = d["flows"].get(fid, {"owner": fid, "pmr": "", "cell_notes": [], "sprints": []})
        sprints = fo["sprints"]
        title = sprints[0]["label"] if sprints else fo["owner"]
        steps_html = "".join(
            f'<div class="sprintmini"><strong>C{idx+1} &middot; {_esc(s["label"])}</strong><ol>'
            + "".join(f"<li>{_esc(st)}</li>" for st in s["steps"])
            + "</ol></div>"
            for idx, s in enumerate(sprints)
        )
        pmr_html = f'<div class="cellnote prot" style="margin-top:4px;font-size:9.5px"><b>DD-22A In-Flow:</b> {_esc(fo["pmr"])}</div>'
        notes_html = "".join(
            f'<div class="cellnote {"prot" if cn["protected"] else ""}">{_esc(cn["text"])}</div>'
            for cn in fo.get("cell_notes", [])
        )
        dday = _esc(f"{d['short']} {d['date'][:2]} · {fid} ({win})")
        return (
            f'<td data-day="{dday}"><details class="slotdet"><summary><b>{_esc(title)}</b>'
            f'<span>{_esc(fo["owner"])} &middot; 3x3 ({len(sprints)} C)</span></summary>'
            f'<div class="slotsteps">{steps_html}</div></details>{pmr_html}{notes_html}</td>'
        )

    def _wknd_flow_cell(d_idx: int, fid: str, win: str) -> str:
        d = days[d_idx]
        fo = d["flows"].get(fid, {"owner": fid, "pmr": "", "sprints": []})
        sprints = fo["sprints"]
        title = sprints[0]["label"] if sprints else fo["owner"]
        steps_html = "".join(
            f'<div class="sprintmini"><strong>{_esc(s["label"])}</strong><ol>'
            + "".join(f"<li>{_esc(st)}</li>" for st in s["steps"])
            + "</ol></div>"
            for s in sprints
        )
        pmr_html = f'<div class="cellnote prot" style="margin-top:4px;font-size:9.5px"><b>DD-22A In-Flow:</b> {_esc(fo["pmr"])}</div>'
        dday = _esc(f"{d['short']} {d['date'][:2]} · Weekend {fid} ({win})")
        return (
            f'<td class="wkndcell" data-day="{dday}"><details class="slotdet"><summary><b>{_esc(title)}</b>'
            f'<span>{_esc(fo["owner"])}</span></summary><div class="slotsteps">{steps_html}</div></details>{pmr_html}</td>'
        )

    def _span(a: dict) -> str:
        return f"{a['start']}-{a['end']}"

    def _timecol(win: str, sub: str) -> str:
        return f'<td class="timecol"><strong>{_esc(win)}</strong><span>{_esc(sub)}</span></td>'

    wknd_f1_win = _span(wknd["F1"])
    wknd_f2_win = _span(wknd["F2"])
    rows: List[str] = []

    # 1. Morning 08:00-08:30
    a_morn = anchors["morning"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_morn), f"{a_morn["label"]} · {a_morn["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_morn)}"><strong>{_esc(a_morn["label"])} ({_span(a_morn)})</strong> &middot; Protected Anchor (M non-Flow)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · Morning"><strong>Weekend pre-window</strong> (Flows run {stats["op_win"]["weekend"]["start"]}-{stats["op_win"]["weekend"]["end"]})</td></tr>'
    )

    # 2. F1 08:30-10:30
    f1_win = _span(wkd["F1"])
    rows.append(
        f'<tr class="row-flow">{_timecol(f1_win, f"Flow 1 · {wkd["F1"]["duration_min"]}m")}'
        + "".join(_wk_flow_cell(d, "F1", f1_win) for d in range(5))
        + f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {f1_win}">Weekend pre-window</td></tr>'
    )

    # 3. F2 10:30-12:30 (Wkd) / Weekend F1 12:00-14:00
    f2_win = _span(wkd["F2"])
    rows.append(
        f'<tr class="row-flow">{_timecol(f2_win, f"Flow 2 (Wkd) / {wknd_f1_win} (Wknd F1)")}'
        + "".join(_wk_flow_cell(d, "F2", f2_win) for d in range(5))
        + _wknd_flow_cell(5, "F1", wknd_f1_win)
        + _wknd_flow_cell(6, "F1", wknd_f1_win)
        + "</tr>"
    )

    # 4. Lunch + AfterLunch 12:30-13:30
    a_lunch = anchors["lunch"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_lunch), f"{a_lunch["label"]} · {a_lunch["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_lunch)}"><strong>{_esc(a_lunch["label"])} ({_span(a_lunch)})</strong> &middot; Protected midday anchor (12:30-13:00 Lunch + 13:00-13:30 AfterLunch)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {wknd["F1"]["end"]} Transition">Weekend F1 &rarr; F2 boundary at {_esc(wknd["F1"]["end"])}</td></tr>'
    )

    # 5. F3 13:30-15:30 (Wkd) / Weekend F2 14:00-16:00
    f3_win = _span(wkd["F3"])
    rows.append(
        f'<tr class="row-flow">{_timecol(f3_win, f"Flow 3 (Wkd) / {wknd_f2_win} (Wknd F2)")}'
        + "".join(_wk_flow_cell(d, "F3", f3_win) for d in range(5))
        + _wknd_flow_cell(5, "F2", wknd_f2_win)
        + _wknd_flow_cell(6, "F2", wknd_f2_win)
        + "</tr>"
    )

    # 6. Afternoon Break 15:30-16:00
    a_brk = anchors["afternoon_break"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_brk), f"{a_brk["label"]} · {a_brk["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_brk)}"><strong>{_esc(a_brk["label"])} ({_span(a_brk)})</strong> &middot; Protected recovery transition (R non-Flow)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · Post-{wknd["F2"]["end"]}">Weekend Flows complete at {_esc(wknd["F2"]["end"])}</td></tr>'
    )

    # 7. Finanzen / 2Do 16:00-16:30
    a_fin = anchors["finanzen_2do"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_fin), f"{a_fin["label"]} · {a_fin["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_fin)}"><strong>{_esc(a_fin["label"])} ({_span(a_fin)})</strong> &middot; Daily finance &amp; inbox triage (C non-Flow)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_fin)}">Weekend leisure / recovery</td></tr>'
    )

    # 8. F4 16:30-18:30
    f4_win = _span(wkd["F4"])
    rows.append(
        f'<tr class="row-flow">{_timecol(f4_win, f"Flow 4 · {wkd["F4"]["duration_min"]}m")}'
        + "".join(_wk_flow_cell(d, "F4", f4_win) for d in range(5))
        + f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {f4_win}">Weekend leisure / recovery</td></tr>'
    )

    # 9. Evening Physical Course 18:30-19:30 (from week-demand.json + holds)
    a_ep = anchors["evening_physical"]
    ep_cells = []
    for d_idx in range(5):
        d = days[d_idx]
        dname = d["day"]
        course_name = courses.get(dname, "Physical Course")
        prot_holds = [h for h in d["holds"] if "München Tanz" in h["text"] or "Protected" in h["state"]]
        ign_holds = [h for h in d["holds"] if "Ignored" in h["state"]]
        dday = _esc(f"{d['short']} {d['date'][:2]} · {_span(a_ep)}")
        if d_idx == 3 and prot_holds:
            ep_cells.append(
                f'<td data-day="{dday}"><strong>{_esc(prot_holds[0]["text"])}</strong>'
                f'<div class="cellnote prot">Replaces {_esc(course_name)} (18:15 commute buffer)</div></td>'
            )
        else:
            ign_html = "".join(f'<div class="cellnote">{_esc(ih["text"])} ignored</div>' for ih in ign_holds)
            ep_cells.append(
                f'<td data-day="{dday}"><strong>{_esc(course_name)} ({a_ep["minutes"]}m)</strong>'
                f'<div class="subdued fine">Outside 72x2m P quota (DD-39)</div>{ign_html}</td>'
            )
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_ep), f"Evening Physical / VWC · {a_ep["minutes"]}m")}'
        + "".join(ep_cells)
        + f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_ep)}">Weekend evening</td></tr>'
    )

    # 10. Abend 19:30-20:30
    a_ab = anchors["abend"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_ab), f"{a_ab["label"]} · {a_ab["minutes"]}m")}'
        f'<td colspan="3" data-day="Mon–Wed · {_span(a_ab)}">Abend / Dinner ({a_ab["minutes"]}m)</td>'
        f'<td data-day="Thu · {_span(a_ab)}"><strong>Protected offsite continues (until 21:00)</strong></td>'
        f'<td data-day="Fri · {_span(a_ab)}">Abend / Dinner ({a_ab["minutes"]}m)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_ab)}">Weekend evening</td></tr>'
    )

    # 11. Project Night / Freizeit 20:30-22:00
    ev_proj = regs["weekday_project"]["evening"]
    ev_plain = regs["weekday_plain"]["evening"]
    ev_win = f"{ev_proj['start']}-{ev_proj['end']}"
    ev_cells = []
    for d_idx in range(5):
        d = days[d_idx]
        lbl = ev_proj["label"] if d_idx < 3 else ev_plain["label"]
        dday = _esc(f"{d['short']} {d['date'][:2]} · {ev_win}")
        ev_cells.append(f'<td data-day="{dday}"><strong>{_esc(lbl)}</strong><div class="subdued fine">{_esc(d["evening_note"])}</div></td>')
    rows.append(
        f'<tr class="row-evening">{_timecol(ev_win, f"Evening Regime · {ev_proj["minutes"]}m")}'
        + "".join(ev_cells)
        + f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {ev_win}">Weekend Freizeit</td></tr>'
    )

    # 12. Day Outro 22:00-22:30
    a_do = anchors["day_outro"]
    rows.append(
        f'<tr class="row-outro">{_timecol(_span(a_do), f"{a_do["label"]} · {a_do["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_do)}"><strong>{_esc(a_do["label"])} ({a_do["minutes"]}m · {_span(a_do)})</strong> &middot; Canonical T1 daily wrap</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_do)}">Weekend wrap</td></tr>'
    )

    # 13. Freizeit 22:30-23:30
    a_fz = anchors["freizeit"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_fz), f"{a_fz["label"]} · {a_fz["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_fz)}">{_esc(a_fz["label"])} ({a_fz["minutes"]}m · rest, non-slot)</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_fz)}">Weekend wind-down</td></tr>'
    )

    # 14. Sleep Routine 23:30-24:00
    a_sl = anchors["sleep_routine"]
    rows.append(
        f'<tr class="row-anchor">{_timecol(_span(a_sl), f"{a_sl["label"]} · {a_sl["minutes"]}m")}'
        f'<td colspan="5" data-day="Mon–Fri · {_span(a_sl)}"><strong>{_esc(a_sl["label"])} ({a_sl["minutes"]}m · end of {stats["op_win"]["weekday"]["start"]}-{stats["op_win"]["weekday"]["end"]} span)</strong> &middot; R non-slot rest</td>'
        f'<td colspan="2" class="wkndoff" data-day="Sat–Sun · {_span(a_sl)}">Sleep Routine</td></tr>'
    )

    return "".join(rows)


def _render_residuals_html(cockpit: dict, stats: dict) -> str:
    res = cockpit["residuals"]
    handoff = cockpit["presentation_handoff"]
    meta = cockpit["meta"]
    tp = stats["tp"]

    coll_text = meta.get("meeting_subtraction_note", "Zero verified external meeting collisions.")
    ignored = [ev for ev in handoff["reconciled_calendar_events"] if ev["policy"] == "ignored_ongoing"]
    ign_summary = ", ".join(f"{e['date'][-2:]} {e['title']} ({e['start']}-{e['end']})" for e in ignored) or "None"

    card1 = (
        f'<article class="notebox"><h3>1. Clock &amp; capacity reconciliation (T1)</h3><ul>'
        f'<li><b>T1 Gross vs Craft Math:</b> <span class="mono">{stats["total_flows"]}</span> Flows &times; <span class="mono">{stats["flow_duration"]}m</span> = '
        f'<span class="mono">{stats["total_flow_tp_min"]:,}m ({stats["gross_hours"]}h)</span> gross = '
        f'<span class="mono">{tp["C"]:,}m ({stats["craft_hours"]}h)</span> pure Craft <span class="mono">C</span> (<span class="mono">{stats["craft_slots"]} &times; 30m</span>) + '
        f'<span class="mono">{stats["non_craft_min"]}m ({stats["non_craft_hours"]}h)</span> non-Craft '
        f'(<span class="mono">{tp["P"]}m P + {tp["M"]}m M + {tp["R"]}m R + {stats["recap_min"]}m</span> trailing <span class="mono">recap_min</span>).</li>'
        f'<li><b>Calendar Collisions &amp; Buffers:</b> {_esc(coll_text)}</li>'
        f'<li><b>Ignored Ambient Holds (Ongoing):</b> <span class="mono">{_esc(ign_summary)}</span>.</li>'
        f'</ul></article>'
    )
    card2 = (
        '<article class="notebox"><h3>2. EM-13 &amp; OpenProject readiness gaps</h3><ul>'
        + "".join(f"<li>{_esc(g)}</li>" for g in res["em13_op_gaps"])
        + "</ul></article>"
    )
    card3 = (
        '<article class="notebox"><h3>3. Longlist deferrals &amp; revisit triggers</h3><ul>'
        + "".join(
            f'<li><b><span class="mono">{_esc(d["wp"])}</span> {_esc(d["title"])}:</b> '
            f'{_esc(d["reason"])} &middot; <i>Trigger:</i> {_esc(d["trigger"])}</li>'
            for d in res["longlist_deferrals"]
        )
        + "</ul></article>"
    )
    area_labels = ", ".join(f'<span class="mono">{_esc(a["label"])}</span>' for a in handoff["six_portfolio_areas"])
    prov_rows = ", ".join(f'<span class="mono">[{_esc(p["tag"])}]</span> {_esc(p["label"])} ({_esc(p["freshness"])})' for p in res["provenance_ledger"])
    card4 = (
        f'<article class="notebox"><h3>4. 1-Hop provenance &amp; downstream handoff</h3>'
        f'<p><b>Artifact:</b> <span class="mono">{_esc(handoff["artifact_type"])} ({_esc(handoff["schema_version"])})</span> &rarr; '
        f'<b>Consumer:</b> <span class="mono">{_esc(handoff["next_consumer"])}</span></p>'
        f'<p><b>6 Portfolio Areas Exported:</b> {area_labels}</p>'
        f'<p class="fine"><b>Provenance:</b> {prov_rows}</p>'
        f'<p class="subdued">Calendar writes (<span class="mono">Q10</span>) belong strictly to <span class="mono">PrecapNextDay</span>; <span class="mono">PrecapWeek</span> is read-only.</p></article>'
    )
    return card1 + card2 + card3 + card4


def _render_sequencing_html(stats: dict) -> str:
    tp = stats["tp"]
    xp = stats["xp"]
    bp = stats["bp"]
    dem = stats["demand"]
    cnt = stats["counts_by_epic"]

    m_shares = dem["mental"]["shares"]
    m_list = ", ".join(
        f'<span class="mono">{_esc(k)}</span> ({int(round(m_shares[k]*100))}% = {cnt["M"].get(k, 0)})'
        for k in ("Intention", "ACIM", "Surrender", "Breathing")
    )
    focus_days_str = ", ".join(f"{d[:3]}={e}" for d, e in dem["mental"]["focus_days"].items())

    p_order = ["Martial Arts", "Dance", "Knee", "General", "S/BJJ"]
    p_list = ", ".join(f'<span class="mono">{_esc(k)}</span> ({cnt["P"].get(k, 0)})' for k in p_order)

    c_list = ", ".join(
        f'<span class="mono">{_esc(label)}</span> ({cnt["C"].get(label, 0)})'
        for _, label in PORTFOLIO_ORDER
    )

    r_list = ", ".join(
        f'<span class="mono">{_esc(b)}</span> ({cnt["R"].get(b, 0)})'
        for b in ("Audiobooks", "Yoga Nidra", "Socializing")
    )

    return "".join([
        (
            f'<article class="notebox"><h3>1. Mental (M &middot; {sum(cnt["M"].values())} slots = {tp["M"]}m) &amp; '
            f'Physical (P &middot; {sum(cnt["P"].values())} slots = {tp["P"]}m)</h3><ul>'
            f'<li><b>Mental Epics (WD-40):</b> {m_list}. Focus days: <span class="mono">{_esc(focus_days_str)}</span>.</li>'
            f'<li><b>Physical Epics (WD-40):</b> {p_list} (<span class="mono">Knee</span> pinned to <span class="mono">*_*_I3_P</span> up to {dem["physical"]["pins"][0]["max_slots"]} slots).</li>'
            f'</ul></article>'
        ),
        (
            f'<article class="notebox"><h3>2. Craft / Projects (C &middot; {sum(cnt["C"].values())} slots = {tp["C"]:,}m across 6 Portfolio Epics)</h3><ul>'
            f'<li><b>6 Canonical Craft Epics (WD-40 / 06-PORTFOLIO):</b> {c_list}.</li>'
            f'<li><b>Sequence vs Flow (M04 / SEQ-Q2):</b> <span class="mono">Sequence</span> remains broader than a single <span class="mono">Flow</span>; '
            f'mixed-project <span class="mono">C1/C2/C3</span> sprints inside a Flow are permitted under compression.</li></ul></article>'
        ),
        (
            f'<article class="notebox"><h3>3. Regeneration (R &middot; {sum(cnt["R"].values())} breaks = {tp["R"]}m) &amp; Gaussian Placement (T2)</h3><ul>'
            f'<li><b>Regeneration Epics (WD-40):</b> Single Epic <span class="mono">Regeneration</span> across {r_list} '
            f'(<span class="mono">XP = 0</span>, <span class="mono">DD-16</span> no numeric BP floor).</li>'
            f'<li><b>Gaussian Focus-Day Curve:</b> <span class="mono">&sigma; = 6.0h (360m)</span> centered on <span class="mono">19:00 (1140m)</span> '
            f'(<span class="mono">w_max = 1.5x</span>, no Fri&rarr;Sat bleed).</li></ul></article>'
        ),
        (
            f'<article class="notebox"><h3>4. Projected T2 Yield (TP / XP / BP &middot; week-allocation.json)</h3><ul>'
            f'<li><b>Total Time Placed (TP):</b> <span class="mono">{stats["total_flow_tp_min"] - stats["recap_min"]:,}m</span> across '
            f'<span class="mono">{stats["total_slots"]}</span> <span class="mono">slot_occurrences</span> + <span class="mono">{stats["recap_min"]}m</span> trailing '
            f'<span class="mono">recap_min</span> = <span class="mono">{stats["total_flow_tp_min"]:,}m ({stats["gross_hours"]}h)</span> gross (<span class="mono">{tp["C"]:,}m / {stats["craft_hours"]}h</span> Craft <span class="mono">C</span>).</li>'
            f'<li><b>Projected Leverage (XP) &amp; Structural BP:</b> <span class="mono">{stats["total_projected_xp"]:,.1f} XP</span> '
            f'(<span class="mono">C {xp["C"]:,.1f} &middot; M {xp["M"]:.2f} &middot; P {xp["P"]:.2f} &middot; R 0.0</span>) &middot; '
            f'<span class="mono">BP {bp["total_bp"]:.1f}</span> (<span class="mono">50/25/25</span>, numeric floor <span class="mono">null</span>).</li></ul></article>'
        ),
    ])


COCKPIT_CSS = """
:root{--bg:#eef1f3;--surface:#fff;--ink:#162b3a;--muted:#627789;--line:#dfe5e9;--mid:#a0b0bc;--night:#183548;--soft:#f7f9fa;--aqua:#e9f4f2;--teal:#29665f;--amber:#9c682a;--amsoft:#fff8e9;--blue:#2e5675;--bluebg:#eff5fa;--danger:#9b4c41;--redbg:#fff2ee;--shadow:0 4px 20px rgba(30,52,68,.04)}
*{box-sizing:border-box}html{scroll-behavior:smooth;scroll-padding-top:82px;overflow-x:clip}body{font:14px/1.45 system-ui,-apple-system,"Segoe UI",sans-serif;background:var(--bg);margin:0;color:var(--ink);overflow-x:clip}button,select{font:inherit}button{cursor:pointer}a{color:var(--blue)}button:focus-visible,a:focus-visible,summary:focus-visible{outline:3px solid #68a6bd;outline-offset:2px}.shell{max-width:1480px;margin:0 auto;padding:24px 24px 64px}.header{display:flex;gap:25px;justify-content:space-between;align-items:start;margin:0 0 18px}.kicker{font-weight:800;letter-spacing:.14em;font-size:10px;text-transform:uppercase;color:#547287}.header h1{font-size:clamp(27px,3vw,43px);letter-spacing:-.045em;margin:5px 0 2px;font-weight:800}.bigdate{font-size:18px;font-weight:550;color:#345571}.header-intro{color:var(--muted);font-size:12px;max-width:760px;margin:9px 0 0}.hlinks{display:flex;flex-wrap:wrap;gap:7px;justify-content:flex-end}.toplink{border:1px solid #cad7df;background:white;border-radius:8px;padding:7px 10px;font-size:12px;text-decoration:none;white-space:nowrap;font-weight:650}.toplink:hover{background:var(--bluebg)}.nav{position:sticky;top:0;z-index:50;display:flex;flex-wrap:wrap;gap:5px;background:#eef1f3f7;backdrop-filter:blur(12px);padding:11px 0 10px;border-bottom:1px solid #dbe2e7;margin-bottom:12px}.nav a{text-decoration:none;color:#476475;font-size:12px;font-weight:750;padding:8px 12px;border:1px solid transparent;border-radius:7px}.nav a:hover{border-color:#c7d4db;background:white}.nav .navend{margin-left:auto;color:#6b8090;font-size:11px;align-self:center}.section{margin-top:16px;background:white;border:1px solid var(--line);box-shadow:var(--shadow);border-radius:12px;scroll-margin-top:75px;overflow:hidden}.sectionhead{display:flex;align-items:center;gap:13px;flex-wrap:wrap;background:#f9fbfc;border-bottom:1px solid var(--line);padding:14px 18px}.sectionnum{display:grid;place-items:center;width:38px;height:38px;border-radius:9px;background:var(--night);color:white;font-size:13px;font-weight:850;flex-shrink:0}.sectionhead h2{font-size:18px;margin:0;letter-spacing:-.02em}.sectionhead p{font-size:11px;color:var(--muted);margin:1px 0 0}.sectionhead .headctrl{margin-left:auto;display:flex;align-items:center;gap:8px;flex-wrap:wrap}.secbtn{border:1px solid #bfd0dc;background:#fff;color:#274a63;border-radius:7px;padding:6px 11px;font-size:12px;font-weight:750;display:inline-flex;align-items:center;gap:6px}.secbtn:hover{background:var(--bluebg);border-color:#7d9fb6}.sectionbody{padding:17px 18px}.pill{display:inline-flex;align-items:center;gap:5px;border:1px solid #d6e1e7;border-radius:5px;padding:3px 7px;background:#fff;color:#466074;font-size:10px;font-weight:800;white-space:normal}.pill.muted{color:#697d8e;background:#f5f7f8}.pill.warn{background:var(--amsoft);color:#835d24;border-color:#ead7b9}.pill.critical{background:var(--redbg);color:var(--danger);border-color:#eed5ce}.pill.ok{background:var(--aqua);color:var(--teal);border-color:#b9ded6}.subdued{color:var(--muted)}.fine{font-size:11px}.small{font-size:12px}.mono{font-family:ui-monospace,SFMono-Regular,Consolas,monospace}.stats{display:grid;grid-template-columns:repeat(5,minmax(0,1fr));gap:10px}.stat{padding:12px 11px;border:1px solid #dbe4e8;border-radius:9px;min-height:92px;min-width:0;overflow-wrap:anywhere}.stat b{display:block;margin:3px 0;font-size:24px;letter-spacing:-.035em}.stat small{font-size:10px;display:block;color:#7b8a95;margin-top:4px}.stat .eyelabel{font-weight:750;font-size:10px;color:#577081;letter-spacing:.05em;text-transform:uppercase}.compassnote{margin-top:10px;font-size:11px;color:var(--muted);display:flex;flex-wrap:wrap;gap:8px;align-items:center}.varcards{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:12px}.varcard{border:1px solid var(--line);border-radius:9px;background:#fbfcfd;overflow:hidden;min-width:0}.varcardhead{display:flex;align-items:center;justify-content:space-between;gap:8px;padding:10px 12px;border-bottom:1px solid var(--line);background:#f5f8fa}.varcardhead strong{font-size:12px;letter-spacing:.04em;text-transform:uppercase}.varcard-previews{list-style:none;margin:0;padding:10px 12px;display:flex;flex-direction:column;gap:6px;font-size:12px;color:#344e61}.varcard-previews li{overflow-wrap:anywhere}.varcard-details{padding:8px 11px;background:#fff;display:flex;flex-direction:column;gap:7px}.vitem{border:1px solid #dde7ed;border-radius:7px;background:#fff}.vitem summary{padding:8px 10px;font-size:12px;cursor:pointer;list-style:none;display:flex;flex-direction:column;gap:3px}.vitem summary::-webkit-details-marker{display:none}.vitem .vhead{display:flex;align-items:center;gap:6px;flex-wrap:wrap}.vitem .vval{font-weight:700;color:#274961}.vitem .extra{padding:9px 10px;background:#f8fafb;color:#506779;font-size:11.5px;border-top:1px solid #e7ecf0}.vitem .extra p{margin:0 0 5px}.vitem .extra p:last-child{margin:0}.m1-previews{flex:1 0 100%;width:100%;display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:4px}.m1prev{border:1.5px solid #b4c6d2;background:#fff;border-radius:8px;padding:9px 11px;text-align:left;display:flex;flex-direction:column;gap:4px;min-width:0;overflow-wrap:anywhere}.m1prev:hover{background:#f4f9fb;border-color:#5e849c}.m1prev .m1meta{font-size:10px;font-weight:800;letter-spacing:.06em;text-transform:uppercase;color:#567285}.m1prev strong{font-size:13px;line-height:1.25;color:var(--ink)}.m1prev small{font-size:11px;color:#6b7e8d}.repos{display:flex;flex-direction:column}.repo{border-top:7px solid #f1f4f6}.repo:first-child{border-top:0}.repohead{display:flex;align-items:center;gap:10px;flex-wrap:wrap;background:#fbfcfd;border-bottom:1px solid var(--line);padding:12px 17px}.repohead h3{margin:0;font-size:15px}.repohead small{color:#7c90a1}.repohead .right{margin-left:auto}.levels{display:grid;grid-template-columns:75px minmax(0,1fr);border-top:1px solid #edf0f2}.levelrail{padding:14px 9px;text-align:center;background:#f8fafb;border-right:1px solid var(--line)}.levelrail b{font-size:19px;display:block;line-height:1.1}.levelrail small{display:block;margin-top:4px;font-size:10px;color:#81929e}.levelbody{padding:13px 15px;min-width:0}.cubestrip{display:flex;flex-wrap:wrap;gap:10px}.cube{flex:1 1 200px;max-width:340px;min-width:150px;text-align:left;border-radius:9px;border:1.5px solid #b4c6d2;background:white;min-height:92px;padding:11px 12px;display:flex;flex-direction:column;align-items:flex-start;gap:5px;transition:background .12s,border-color .12s;overflow-wrap:anywhere}.cube:hover{background:#f4f9fb;border-color:#5e849c}.cube[aria-expanded=true]{background:#fff9ec;border-color:#b38b51;box-shadow:inset 0 0 0 1px #ecd4ad}.cube.nice{border-style:dashed}.cube .cubehead{display:flex;gap:7px;align-items:center;font-size:9px;color:#667d8a;font-weight:800;letter-spacing:.09em;text-transform:uppercase}.cube .glyph{display:inline-block;width:15px;height:15px;border:1.6px solid #a27842;background:#fff9e8;border-radius:3px;transform:skewY(-6deg)}.cube.nice .glyph{border-color:#72899b;background:transparent}.cube strong{font-size:14px;line-height:1.25}.cube .micro{font-size:11px;color:#6b7e8d}.toggle{border:0;background:transparent;text-align:left;font-size:12px;font-weight:750;color:#315c77;padding:2px 0}.toggle span{display:inline-grid;place-items:center;border:1px solid #cbdbe3;width:18px;height:18px;border-radius:5px;margin-right:5px}.toggle[aria-expanded=true] span{transform:rotate(90deg)}.is-hidden{display:none!important}.specdisplay{margin-top:8px}.connector{width:min(690px,88%);margin:0 auto;display:flex;align-items:center;flex-direction:column;height:22px}.connector:before{content:'';height:12px;width:1px;background:#93a8b7}.connector:after{content:'';border-left:1px solid #93a8b7;border-right:1px solid #93a8b7;border-top:1px solid #93a8b7;width:90%;height:10px}.specbox{border:1px solid #bfd0dc;border-radius:9px;overflow:hidden;background:#fff}.fields{display:grid;grid-template-columns:repeat(6,minmax(0,1fr))}.field{padding:11px 10px;border-right:1px solid #e5ebef;min-height:140px;min-width:0;overflow-wrap:anywhere}.field:last-child{border-right:0}.field h4{display:flex;gap:6px;align-items:center;margin:0 0 7px;font-size:11.5px}.field h4 i{font-style:normal;background:#edf3f7;border-radius:5px;min-width:21px;padding:2px 0;text-align:center;color:#365d78}.field .sect{font-size:9.5px;text-transform:uppercase;font-weight:780;letter-spacing:.05em;color:#657c8e;margin:7px 0 3px}.field p{font-size:11px;color:#4c6173;margin:0 0 5px}.field ul{margin:3px 0 0;padding-left:14px;font-size:11px;color:#506778}.field li{margin:3px 0}.nodata{font-size:11px;color:#8a6a44;font-style:italic}.specfoot{background:#fafcfd;border-top:1px solid #e3eaef;font-size:10px;color:#6b7e8f;padding:7px 11px;display:flex;justify-content:space-between;gap:8px;flex-wrap:wrap}.emptynice{font-size:11px;color:#6f8493;padding:6px 0}.caution{font-size:11px;color:#956434;background:#fff9ed;border-top:1px solid #e6d7bb;padding:7px 11px}.hint{padding:10px 12px;border:1px solid #e4e9ed;background:#fcfdfd;border-radius:8px;font-size:11px;color:#516776}.flowwrap{width:100%;overflow-x:visible;border:1px solid #dbe5ea;border-radius:9px}.flowtable{width:100%;border-collapse:collapse;table-layout:fixed;overflow-wrap:anywhere}.flowtable th{background:#1a3850;color:#fff;font-size:11px;text-align:left;padding:8px 7px;border-right:1px solid #345169}.flowtable th:first-child{width:10%}.flowtable th:nth-child(n+2){width:12.85%}.flowtable td{border-right:1px solid #e1e8ec;border-bottom:1px solid #e1e8ec;padding:5px;vertical-align:top;font-size:11px;overflow-wrap:anywhere}.flowtable tr:last-child td{border-bottom:0}.flowtable td:last-child,.flowtable th:last-child{border-right:0}.timecol{background:#f3f7fa;padding:7px!important}.timecol strong{font-size:11px;display:block;color:#1b384f}.timecol span{font-size:10px;color:#657d8f;display:block;margin-top:2px}.row-flow .timecol{background:#edf4f9}.row-anchor td:not(.timecol){background:#f7f9fa;color:#4a6173;font-size:11px;padding:6px 8px}.row-evening td:not(.timecol){background:#faf7f2}.row-outro td:not(.timecol){background:#eef5f3;color:#275a53}.slotdet{border:1px solid #dce6ec;border-radius:6px;background:#fff;padding:5px 6px}.slotdet[open]{border-color:#448b83;background:#f4fbf8}.slotdet summary{list-style:none;cursor:pointer;display:flex;flex-direction:column;gap:2px}.slotdet summary::-webkit-details-marker{display:none}.slotdet summary b{font-size:11px;line-height:1.25;color:#1e3f55}.slotdet summary span{font-size:10px;color:#5c7485}.slotdet summary:after{content:'Inspect sprints +';font-size:9.5px;color:#2c665f;font-weight:750;margin-top:2px}.slotdet[open] summary:after{content:'Hide sprints -'}.slotsteps{margin-top:6px;padding-top:5px;border-top:1px dashed #c8dce0;display:flex;flex-direction:column;gap:5px}.sprintmini strong{display:block;font-size:10px;color:#274a62}.sprintmini ol{margin:2px 0 0;padding-left:15px;font-size:10px;color:#4e6577}.sprintmini li{margin:1px 0}.cellnote{font-size:10px;margin-top:4px;padding:3px 5px;border-radius:4px;background:#fff8e9;color:#7c5720;border:1px solid #ebd7b3}.cellnote.prot{background:#e9f4f2;color:#245e57;border-color:#baded7}.wkndcell{background:#f6f9fb!important}.wkndoff{background:#f9fafb!important;color:#677d8c;font-size:10.5px;padding:8px!important}.focusstrip{display:grid;grid-template-columns:repeat(3,minmax(0,1fr));gap:10px;margin-top:14px}.focuscard{border:1px solid #d7e2e8;border-radius:9px;background:#f9fbfc;padding:12px 13px;min-width:0;overflow-wrap:anywhere}.focuscard h3{margin:0 0 6px;font-size:13px;color:var(--night);display:flex;align-items:center;justify-content:space-between}.focuscard ul{margin:0;padding-left:16px;font-size:12px;color:#4f6678}.focuscard li{margin:3px 0}.notegrid{display:grid;grid-template-columns:repeat(2,minmax(0,1fr));gap:11px}.notebox{border:1px solid #e1e8ec;border-radius:9px;padding:13px}.notebox h3{font-size:13px;margin:0 0 8px}.notebox p{font-size:12px;color:#516779;margin:5px 0}.notebox ul{padding-left:18px;font-size:12px;color:#516779;margin:4px 0}.notebox li{margin:5px 0}.footer{font-size:11px;color:#82909a;padding-top:17px}
@media(max-width:1180px){.stats{grid-template-columns:repeat(3,minmax(0,1fr))}.fields{grid-template-columns:repeat(3,minmax(0,1fr))}.field{border-bottom:1px solid #e5ebef}.field:nth-child(3n){border-right:0}.field:nth-last-child(-n+3){border-bottom:0}}
@media(max-width:920px){.varcards,.m1-previews{grid-template-columns:1fr}.flowtable,.flowtable thead,.flowtable tbody,.flowtable tr,.flowtable td{display:block;width:100%}.flowtable thead{display:none}.flowtable tr{border-bottom:2px solid #d5e1e8;padding:6px 8px;background:#fff}.flowtable tr:last-child{border-bottom:0}.flowtable td{border:0!important;padding:4px 0!important;width:100%!important}.timecol{border-radius:6px;padding:6px 9px!important;margin-bottom:4px}.flowtable td[data-day]::before{content:attr(data-day);display:block;font-size:10px;font-weight:800;letter-spacing:.05em;text-transform:uppercase;color:#567084;margin-bottom:2px}.flowwrap{border:0;background:transparent}.focusstrip{grid-template-columns:1fr}}
@media(max-width:720px){.shell{padding:13px 11px 45px}.header{display:block}.hlinks{justify-content:flex-start;margin-top:10px}.nav{top:0}.nav a{font-size:10px;padding:6px 7px}.nav .navend{width:100%;margin-left:0}.stats{grid-template-columns:repeat(2,minmax(0,1fr));gap:7px}.notegrid{grid-template-columns:1fr}.sectionhead{padding:11px}.sectionbody{padding:12px}.levelrail{padding:9px 5px}.levels{grid-template-columns:54px minmax(0,1fr)}.levelbody{padding:10px}.cube{min-width:136px;max-width:none}.fields{grid-template-columns:1fr}.field{border-right:0!important;min-height:auto;border-bottom:1px solid #e5ebef!important}.field:last-child{border-bottom:0!important}.repohead{padding:11px}}
@media print{.nav,.hlinks,.toggle,.secbtn{display:none}.shell{max-width:none;padding:0}.section{break-inside:avoid}.is-hidden{display:block!important}.varcard-previews,.m1-previews{display:none!important}.flowwrap{overflow:visible}.flowtable{min-width:0}}
""".strip()


COCKPIT_JS = """
const $=(id)=>document.getElementById(id);
const esc=(s)=>String(s??'').replaceAll('&','&amp;').replaceAll('<','&lt;').replaceAll('>','&gt;').replaceAll('"','&quot;').replaceAll("'",'&#39;');
function list(items,empty='Not specified in saved source'){if(!items||!items.length)return '<span class="nodata">'+esc(empty)+'</span>';return '<ul>'+items.map(i=>'<li>'+esc(i)+'</li>').join('')+'</ul>'}
$('northlink').href=DATA.source.primary;$('northlink').textContent=DATA.source.primaryLabel+' ↗';
$('brieflink').href=DATA.source.secondary;$('brieflink').textContent=DATA.source.secondaryLabel+' ↗';
$('stats').innerHTML=DATA.metrics.map(m=>'<div class="stat"><div class="eyelabel">T1 Grounded / 6-Portfolio</div><b>'+esc(m.value)+'</b><strong class="small">'+esc(m.name)+'</strong><small>'+esc(m.note)+'</small></div>').join('');
function hasVerifiedOverride(it){return Boolean(it.ov && it.sysDef && it.opChoice && it.sysDef!==it.opChoice && it.srcRef);}
$('cards-01').innerHTML=DATA.decisionCards.map(c=>'<article class="varcard"><div class="varcardhead"><strong>'+esc(c.key)+'</strong><span class="pill '+c.cls+'">'+esc(c.title)+'</span></div><ul class="varcard-previews">'+c.previews.map(([k,v])=>'<li><b>'+esc(k)+':</b> '+esc(v)+'</li>').join('')+'</ul><div class="varcard-details is-hidden">'+c.items.map(it=>'<details class="vitem"><summary><div class="vhead"><span class="pill '+c.cls+'">'+esc(c.key)+'</span><b>'+esc(it.name)+'</b>'+(it.gate?'<span class="pill ok">'+esc(it.gate)+'</span>':'')+(hasVerifiedOverride(it)?'<span class="pill warn">OPERATOR OVERRIDE</span>':'')+'</div><span class="vval">'+esc(it.val)+'</span></summary><div class="extra"><p>'+esc(it.detail)+'</p>'+(hasVerifiedOverride(it)?'<p class="fine"><b>Baseline default:</b> '+esc(it.sysDef)+' &rarr; <b>Operator choice:</b> '+esc(it.opChoice)+' (<span class="mono">'+esc(it.srcRef)+'</span>)</p>':'')+'</div></details>').join('')+'</div></article>').join('');
$('toggle-01').addEventListener('click',()=>{
 const open=$('toggle-01').getAttribute('aria-expanded')!=='true';
 $('toggle-01').setAttribute('aria-expanded',String(open));
 $('toggle-01').textContent=open?'Collapse settings':'Expand settings';
 $('cards-01').dataset.open=String(open);
 document.querySelectorAll('#cards-01 .varcard-previews').forEach(el=>el.classList.toggle('is-hidden',open));
 document.querySelectorAll('#cards-01 .varcard-details').forEach(el=>el.classList.toggle('is-hidden',!open));
});
$('m1-previews').innerHTML=DATA.topPriorityRefs.map(({ri,ni,slot})=>{
 const r=DATA.repos[ri],g=r.goals[ni];
 return '<button type="button" class="m1prev" data-ri="'+ri+'" data-ni="'+ni+'"><span class="m1meta">'+esc(slot)+'</span><strong>'+esc(g.title)+'</strong><small>'+esc(g.state)+'</small></button>';
}).join('');
function cubeHTML(repoIndex,layer,n,i){
 const critBadge=n.critical?'<span class="pill critical" style="padding:1px 5px;font-size:9px">⚡ CRITICAL PATH</span>':'';
 const crossPills=(n.crossRepo||[]).map(cr=>'<span class="pill ok crosspill" data-target-r="'+cr.targetRepo+'" data-target-n="'+cr.targetGoal+'" style="padding:2px 6px;font-size:9.5px">'+esc(cr.label)+'</span>').join('');
 return '<button type="button" class="cube '+(layer==='L2'?'nice':'')+'" data-r="'+repoIndex+'" data-layer="'+layer+'" data-n="'+i+'" aria-expanded="false" aria-controls="panel-'+repoIndex+'-'+layer+'"><span class="cubehead"><span class="glyph"></span>'+layer+' &middot; '+(layer==='L1'?'PRIORITY #'+(i+1):'NICE-TO-HAVE')+'</span><strong>'+esc(n.title)+'</strong><span class="micro">'+esc(n.state)+'</span>'+(critBadge||crossPills?'<span style="display:flex;flex-wrap:wrap;gap:4px;margin-top:3px">'+critBadge+crossPills+'</span>':'')+'</button>';
}
$('repos').innerHTML=DATA.repos.map((r,i)=>'<article class="repo" id="repo-'+esc(r.id)+'"><div class="repohead"><h3>'+(i+1)+'. '+esc(r.name)+'</h3><span class="pill muted">'+esc(r.ref)+'</span><small>'+esc(r.caption)+'</small><span class="right pill">'+r.goals.length+' L1 goals</span></div><div class="levels"><div class="levelrail"><b>L1</b><small>Priority<br>goals</small></div><div class="levelbody"><div class="cubestrip">'+r.goals.map((g,j)=>cubeHTML(i,'L1',g,j)).join('')+'</div><div class="specdisplay is-hidden" id="panel-'+i+'-L1" aria-live="polite"></div></div></div><div class="levels"><div class="levelrail"><b>L2</b><small>Nice-to-<br>haves</small></div><div class="levelbody"><button type="button" class="toggle" data-expand="'+i+'" aria-expanded="false" aria-controls="nice-'+i+'"><span>&gt;</span> Nice-to-haves ('+r.nice.length+')</button><div class="is-hidden" id="nice-'+i+'" style="margin-top:10px">'+(r.nice.length?'<div class="cubestrip">'+r.nice.map((g,j)=>cubeHTML(i,'L2',g,j)).join('')+'</div><div class="specdisplay is-hidden" id="panel-'+i+'-L2" aria-live="polite"></div>':'<p class="emptynice">Zero L2 items (blocked/future-phase backlog items moved to Section 04 Longlist Deferrals).</p>')+'</div></div></div></article>').join('');
function specField(letter,title,inside){return '<div class="field"><h4><i>'+letter+'</i> '+title+'</h4>'+inside+'</div>'}
function fieldSection(name,content){return '<div class="sect">'+esc(name)+'</div>'+content}
function specHTML(r,n,layer){
 const g=fieldSection('Desired outcome','<p>'+esc(n.title)+'</p>')+fieldSection('Acceptance evidence','<p>'+esc(n.acceptance||'Unresolved')+'</p>')+fieldSection('Tasks -> Subtasks',list(n.subtasks,'No subtask decomposition supplied'));
 const inp=fieldSection('Ranked sources',list(n.inputs,'Unresolved'))+fieldSection('Upstream dependencies',list(n.upstream,'None verified (distinct from Continuation)'))+fieldSection('Explicit exclusions',list(n.exclusions,'None stated'));
 const process=fieldSection('Steps & verification (## Process)',list(n.process,'Unresolved'));
 const skills=fieldSection('Registered skills (## Skills)',list(n.skills,'No specialized skill required'));
 const out=fieldSection('Deliverables (## Output)',list(n.outputs,'Unresolved'))+fieldSection('Redraft / Example','<p class="mono" style="font-size:10.5px">'+esc(n.redraft||'None')+'</p>');
 const cont=fieldSection('Downstream successors (## Continuation)',list(n.continuation,'Unresolved'));
 return '<div class="connector" aria-hidden="true"></div><div class="specbox" role="region" aria-label="Task specification for '+esc(n.title)+'"><div class="fields">'+specField('G','Goal',g)+specField('I','Input',inp)+specField('P','Process',process)+specField('S','Skills',skills)+specField('O','Output',out)+specField('C','Continuation',cont)+'</div>'+((n.caution&&n.caution.length)?'<div class="caution">'+n.caution.map(esc).join(' | ')+'</div>':'')+'<div class="specfoot"><span><b>'+esc(r.name)+'</b> &middot; '+esc(layer)+' &middot; '+esc(n.title)+' &middot; Metadata: '+esc(n.wp||'[OP-UNRESOLVED]')+' ('+esc(r.op)+')</span><span>Evidence: '+esc(n.evidence.join(' + '))+' &middot; EM-13 Unified on G|I|P|S|O|C</span></div></div>';
}
function showSpec(button){
 const ri=Number(button.dataset.r),layer=button.dataset.layer,ni=Number(button.dataset.n),repo=DATA.repos[ri],node=(layer==='L1'?repo.goals:repo.nice)[ni],panel=$('panel-'+ri+'-'+layer);
 const already=button.getAttribute('aria-expanded')==='true';
 document.querySelectorAll('.cube[data-r="'+ri+'"][data-layer="'+layer+'"]').forEach(b=>b.setAttribute('aria-expanded','false'));
 if(already){panel.classList.add('is-hidden');panel.innerHTML='';return}
 button.setAttribute('aria-expanded','true');
 panel.classList.remove('is-hidden');
 panel.innerHTML=specHTML(repo,node,layer);
}
document.querySelectorAll('.cube').forEach(b=>b.addEventListener('click',(e)=>{
 const pill=e.target.closest('.crosspill');
 if(pill){
  e.stopPropagation();
  const tr=pill.dataset.targetR,tn=pill.dataset.targetN;
  const target=document.querySelector('.cube[data-r="'+tr+'"][data-layer="L1"][data-n="'+tn+'"]');
  if(target){if(target.getAttribute('aria-expanded')!=='true')showSpec(target);target.scrollIntoView({behavior:'smooth',block:'center'});}
  return;
 }
 showSpec(b);
}));
document.querySelectorAll('.toggle').forEach(b=>b.addEventListener('click',()=>{
 const el=$('nice-'+b.dataset.expand),newState=el.classList.contains('is-hidden');
 el.classList.toggle('is-hidden',!newState);
 b.setAttribute('aria-expanded',String(newState));
}));
$('toggle-02').addEventListener('click',()=>{
 const open=$('toggle-02').getAttribute('aria-expanded')!=='true';
 $('toggle-02').setAttribute('aria-expanded',String(open));
 $('toggle-02').textContent=open?'Collapse section 02':'Expand section 02';
 $('body-02').classList.toggle('is-hidden',!open);
 $('m1-previews').classList.toggle('is-hidden',open);
});
document.querySelectorAll('.m1prev').forEach(btn=>btn.addEventListener('click',()=>{
 const ri=btn.dataset.ri,ni=btn.dataset.ni;
 $('toggle-02').setAttribute('aria-expanded','true');
 $('toggle-02').textContent='Collapse section 02';
 $('body-02').classList.remove('is-hidden');
 $('m1-previews').classList.add('is-hidden');
 const target=document.querySelector('.cube[data-r="'+ri+'"][data-layer="L1"][data-n="'+ni+'"]');
 if(target){if(target.getAttribute('aria-expanded')!=='true')showSpec(target);target.scrollIntoView({behavior:'smooth',block:'nearest'});}
}));
$('focusstrip').innerHTML=[
 ['Mental','Operator personal mental orientation',DATA.personalFocus.mental],
 ['Physical','Operator personal physical orientation',DATA.personalFocus.physical],
 ['Regeneration','Operator personal recovery orientation',DATA.personalFocus.regeneration]
].map(([area,desc,bullets])=>'<article class="focuscard"><h3><span>'+esc(area)+'</span><span class="pill ok">Active</span></h3><p class="fine subdued" style="margin:0 0 6px">'+esc(desc)+'</p>'+(bullets&&bullets.length?list(bullets):'<p class="nodata">not yet specified</p>')+'</article>').join('');
""".strip()


def render_html(cockpit: dict, stats: dict) -> str:
    runtime = build_runtime_payload(cockpit, stats)
    meta = cockpit["meta"]
    handoff = cockpit["presentation_handoff"]
    runtime_json = json.dumps(runtime, ensure_ascii=False, separators=(",", ":")).replace("</", "<\\/")

    day_ths = "".join(f'<th>{_esc(d["short"])} {_esc(d["date"][:2])}</th>' for d in runtime["days"])
    m2_tbody = _render_matrix2_rows_html(runtime, stats, handoff)
    res_html = _render_residuals_html(cockpit, stats)
    seq_html = _render_sequencing_html(stats)
    op_badge = "[OP-OFFLINE] Snapshot Fallback" if meta["op_status"] == "OFFLINE_FALLBACK" else "[OP-ONLINE] Live OP"
    op_cls = "warn" if meta["op_status"] == "OFFLINE_FALLBACK" else "ok"
    compass_note = (
        f"Deterministic T1 clock math ({stats['total_flows']} Flows = {stats['gross_hours']}h gross / "
        f"{stats['craft_hours']}h Craft C + {stats['non_craft_hours']}h P/M/R/recap including "
        f"{stats['recap_min']}m trailing recap_min) across the 6 Portfolio Areas: "
        f"Leela · IPOS · Master of Arts · Apex AI · Mindful Bar · Residual."
    )

    return f"""<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<meta name="color-scheme" content="light">
<title>Precap Week · {_esc(meta['date_span_label'])} | Cockpit v0.5</title>
<style>
{COCKPIT_CSS}
</style>
</head>
<body><main class="shell">
<header class="header"><div><div class="kicker">Precap Week / Compiled cockpit v0.5</div><h1>Precap Week &middot; {_esc(meta['date_span_label'])}</h1><div class="bigdate">T1/T2 Compiled View <span class="pill warn">{_esc(meta['banner_badge'])}</span> <span class="pill muted">Clock: week-blueprint.json (Mon&ndash;Sun)</span></div><p class="header-intro">{_esc(meta['intro'])}</p></div><div class="hlinks"><a class="toplink" id="northlink" target="_blank" rel="noreferrer">{_esc(meta['source_links'].get('primaryLabel', 'Original Northstar'))} &nearr;</a><a class="toplink" id="brieflink" target="_blank" rel="noreferrer">{_esc(meta['source_links'].get('secondaryLabel', 'Command Brief Archive'))} &nearr;</a></div></header>
<nav class="nav" aria-label="Cockpit sections"><a href="#s00">00 Head</a><a href="#s01">01 Decisions</a><a href="#s02">02 Matrix 1</a><a href="#s03">03 Matrix 2</a><a href="#s04">04 Residual Info</a><a href="#s05">05 Sequencing</a><div class="navend">READ-ONLY PLAN / G1 {_esc(meta['g1_status'])}</div></nav>
<section class="section" id="s00"><div class="sectionhead"><div class="sectionnum">00</div><div><h2>Portfolio compass</h2><p>Five locked T1 capacity &amp; 6-Portfolio summary cards grounded in week-blueprint.json &amp; slot-inventory.json</p></div><div class="headctrl"><span class="pill ok">6 Portfolio Areas Locked</span><span class="pill {op_cls}">{_esc(op_badge)}</span></div></div><div class="sectionbody"><div id="stats" class="stats"></div><div class="compassnote"><span>{_esc(compass_note)}</span></div></div></section>
<section class="section" id="s01"><div class="sectionhead"><div class="sectionnum">01</div><div><h2>Operator decision brief</h2><p>Three-category overview (NEW &middot; ONGOING &middot; STANDARD) with G1 gate chips &amp; verified override guard</p></div><div class="headctrl"><span class="pill meta">Source + T1 clock + G1 Gate</span><button type="button" class="secbtn" id="toggle-01" aria-expanded="false" aria-controls="cards-01">Expand settings</button></div></div><div class="sectionbody"><div id="cards-01" class="varcards" data-open="false"></div></div></section>
<section class="section" id="s02"><div class="sectionhead"><div class="sectionnum">02</div><div><h2>Matrix 1 &middot; 6-Portfolio goals and G|I|P|S|O|C specifications</h2><p>6 Portfolio Areas (Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual) &middot; L1 + folded L2 (no L3) &middot; inline &#128279; Cross-Repo pills</p></div><div class="headctrl"><span class="pill meta">6 Portfolio Areas &middot; EM-13 Unified</span><button type="button" class="secbtn" id="toggle-02" aria-expanded="true" aria-controls="body-02">Collapse section 02</button></div><div class="m1-previews is-hidden" id="m1-previews" aria-label="Top priority L1 goal previews"></div></div><div id="body-02"><div id="repos" class="repos"></div><div class="sectionbody" style="border-top:1px solid var(--line)"><div class="hint"><strong>Data boundary:</strong> UI cards remain strictly L1 / L2 (zero L3 cubes); inside expanded 6-column G|I|P|S|O|C drawers, Goal &amp; Output decompose into Tasks &rarr; Subtasks with short drafts/examples (EM-13 unified). Unmapped local items carry <span class="mono">[OP-UNRESOLVED]</span>; live OP offline state carries <span class="mono">[OP-OFFLINE]</span>.</div></div></div></section>
<section class="section" id="s03"><div class="sectionhead"><div class="sectionnum">03</div><div><h2>Matrix 2 &middot; Calendar and flows</h2><p>Single fit-to-width Mon&ndash;Sun hourly timetable (08:00&ndash;24:00 weekday + 12:00&ndash;16:00 weekend via week-blueprint.json + DD-22A P/M/R band)</p></div><div class="headctrl"><span class="pill meta">T1 {stats['total_flows']} Flows &middot; 7 Days Mon&ndash;Sun</span></div></div><div class="sectionbody"><div class="flowwrap"><table class="flowtable" id="flowtable"><thead><tr><th>Time window</th>{day_ths}</tr></thead><tbody>{m2_tbody}</tbody></table></div><div class="focusstrip" id="focusstrip" aria-label="Personal focus priorities"></div></div></section>
<section class="section" id="s04"><div class="sectionhead"><div class="sectionnum">04</div><div><h2>Residual information</h2><p>Clock &amp; capacity reconciliation, EM-13/OP readiness, Longlist deferrals, and PrecapNextDay handoff</p></div></div><div class="sectionbody"><div class="notegrid">{res_html}</div></div></section>
<section class="section" id="s05"><div class="sectionhead"><div class="sectionnum">05</div><div><h2>Sequencing &amp; dispersal orientation</h2><p>Stateless weekly dispersal dials (week-demand.json), Gaussian focus-day placement (&sigma; = 6.0h around 19:00), and T2 TP/XP/BP summary</p></div><div class="headctrl"><span class="pill ok">WD-40 &middot; 4 Branches &middot; 6 Craft Epics</span></div></div><div class="sectionbody"><div class="notegrid" id="seqgrid">{seq_html}</div></div></section>
<div class="footer">Cockpit v0.5 &middot; Canonical 6-Portfolio Standard (Leela, IPOS, Master of Arts, Apex AI, Mindful Bar, Residual) &amp; T1 Mon&ndash;Sun blueprint clock.</div>
</main>
<script>const DATA={runtime_json};
{COCKPIT_JS}
</script></body></html>
"""


def _yaml_scalar(val: Any) -> str:
    if isinstance(val, bool):
        return "true" if val else "false"
    if isinstance(val, (int, float)):
        return str(val)
    s = str(val).replace('"', '\\"')
    return f'"{s}"'


def _dump_yaml_lines(obj: Any, indent: int = 0) -> List[str]:
    pad = "  " * indent
    lines: List[str] = []
    if isinstance(obj, dict):
        for k, v in obj.items():
            if isinstance(v, (dict, list)) and len(v) > 0:
                lines.append(f"{pad}{k}:")
                lines.extend(_dump_yaml_lines(v, indent + 1))
            elif isinstance(v, list):
                lines.append(f"{pad}{k}: []")
            elif isinstance(v, dict):
                lines.append(f"{pad}{k}: {{}}")
            else:
                lines.append(f"{pad}{k}: {_yaml_scalar(v)}")
    elif isinstance(obj, list):
        for item in obj:
            if isinstance(item, dict):
                first = True
                for k, v in item.items():
                    prefix = f"{pad}- " if first else f"{pad}  "
                    first = False
                    if isinstance(v, list) and not v:
                        lines.append(f"{prefix}{k}: []")
                    elif isinstance(v, dict) and not v:
                        lines.append(f"{prefix}{k}: {{}}")
                    elif isinstance(v, (dict, list)):
                        lines.append(f"{prefix}{k}:")
                        lines.extend(_dump_yaml_lines(v, indent + 2))
                    else:
                        lines.append(f"{prefix}{k}: {_yaml_scalar(v)}")
            else:
                lines.append(f"{pad}- {_yaml_scalar(item)}")
    return lines


def render_okf_brief(cockpit: dict, stats: dict) -> str:
    """Emit crisp OKF v0.2 Report obeying D1-D12 without duplicating Cockpit tables or JSON rules."""
    meta = cockpit["meta"]
    decisions = cockpit["decisions"]
    portfolios = cockpit["matrix1_portfolios"]
    residuals = cockpit["residuals"]
    handoff = cockpit["presentation_handoff"]
    pf = cockpit["personal_focus"]
    today_str = datetime.date.today().isoformat()

    l1_total = sum(len(p["goals"]) for p in portfolios)
    l2_total = sum(len(p["nice"]) for p in portfolios)
    ov_count = sum(1 for b in ("new", "ongoing") for it in decisions[b] if _has_verified_override(it))

    p_rows = []
    for rank, area in enumerate(portfolios, start=1):
        goals_str = "; ".join(
            f"{'⚡ ' if g['critical'] else ''}{g['title']} (`{g['wp']}`)"
            for g in area["goals"]
        )
        cross = [cr["label"] for g in area["goals"] for cr in g.get("crossRepo", [])]
        cross_str = ", ".join(cross) if cross else "—"
        nice_str = ", ".join(n["title"] for n in area["nice"]) if area["nice"] else "—"
        p_rows.append(f"| {rank} | **{area['name']}** | {goals_str} | {nice_str} | {cross_str} |")

    def _tag_for_item(it: dict, default_tag: str) -> str:
        s = (it.get("srcRef") or "").lower()
        if "evidence-" in s or "op-wp" in s:
            return "OP"
        if "gcal" in s:
            return "CLK"
        return default_tag

    dec_lines = []
    for item in decisions["new"]:
        ov_note = f" *(Override: `{item['sysDef']}` -> `{item['opChoice']}`)*" if _has_verified_override(item) else ""
        dec_lines.append(f"- **`{item['name']}`** — `{item['val']}` (`G1: {item['gate']}`){ov_note} `[src: {_tag_for_item(item, 'INT')}]`")
    for item in decisions["ongoing"]:
        dec_lines.append(f"- **Ongoing:** `{item['name']}` — `{item['val']}` `[src: {_tag_for_item(item, 'CLK')}]`")

    def_rows = [
        f"| `{d['wp']}` | {d['title']} | {d['reason']} | {d['trigger']} |"
        for d in residuals["longlist_deferrals"]
    ]
    prov_rows = [
        f"| `[{p['tag']}]` | `{p['ref']}` — {p['label']} | `{p['freshness']}` |"
        for p in residuals["provenance_ledger"]
    ]
    cal_rows = [
        f"| `{e['date']}` | {e['title']} | `{e['start']}–{e['end']}` | `{e['policy']}` | `{e['capacity_delta_min']}m` |"
        for e in handoff["reconciled_calendar_events"]
    ]
    phys_list = "; ".join(pf["physical"]).replace("*_*_I3_P", "`*_*_I3_P`")
    focus_lines = [
        f"- **Mental (`{stats['tp']['M']}m` in-Flow):** {'; '.join(pf['mental']) or 'not yet specified'}",
        f"- **Physical (`{stats['tp']['P']}m` in-Flow + Evening Course):** {phys_list or 'not yet specified'}",
        f"- **Regeneration (`{stats['tp']['R']}m` breaks · `0 XP`):** {'; '.join(pf['regeneration']) or 'not yet specified'}",
    ]

    handoff_yaml = "\n".join(_dump_yaml_lines({"presentation_handoff": handoff}))
    cockpit_ref = handoff["cockpit_html_ref"].replace("\\", "/")
    brief_dir = posixpath.dirname(handoff.get("brief_okf_ref", "").replace("\\", "/"))
    cockpit_rel = posixpath.relpath(cockpit_ref, brief_dir) if brief_dir else posixpath.basename(cockpit_ref)
    cockpit_name = posixpath.basename(cockpit_ref)
    op_tag = "[OP-ONLINE]" if meta["op_status"] == "ONLINE" else "[OP-OFFLINE]"
    op_state_line = f"OpenProject status uses `{op_tag}` (`{meta['op_status']}`); see Deferrals and 1-hop ledger below."

    lines = [
        "---",
        "type: Report",
        f"id: PRECAP-WEEK-BRIEF-{meta['week_id']}",
        f'title: "Weekly Command Brief — {meta["week_id"]} ({meta["date_span_label"]})"',
        f'description: "OKF v0.2 executive weekly brief for {meta["week_id"]} compiling Stage 1A intake, 6 Portfolio Areas, Mon-Sun blueprint clock, T2 dispersal totals, and PrecapNextDay handoff."',
        f"status: {'current' if handoff['operator_g1_status'] == 'APPROVED' else 'draft'}",
        f"date: {today_str}",
        "tags: [weekly-orchestration, precap-week, command-brief, okf-v02]",
        "---",
        "",
        f"# Weekly Command Brief — {meta['week_id']} ({meta['date_span_label']})",
        "",
        f"> **Result state:** `{handoff['result_state']}` · **G1 gate:** `{handoff['operator_g1_status']}`  ",
        f"> **Direction:** {meta['direction_summary']}  ",
        f"> **Next action:** `{meta['next_action']}`  ",
        f"> **Review needed:** {meta['review_needed']}  ",
        f"> **Interactive Cockpit (`v0.5`):** [{cockpit_name}]({cockpit_rel})",
        "",
        "## 00 · Portfolio Compass (`T1 / T2` Grounded)",
        "",
        "Capacity and sprint metrics derive directly from the weekly blueprint and allocation JSON.",
        "",
        "| Metric | Value | Source Basis |",
        "|---|---|---|",
        f"| **Net Craft Capacity (`T1`)** | `{stats['net_craft_hours']}h / {stats['craft_hours']}h C` (`{stats['gross_hours']}h` gross) | `{stats['total_flows']}` Flows (`{stats['recap_min']}m` trailing recap inside `{stats['non_craft_hours']}h` P/M/R) `[src: CLK]` |",
        f"| **Weekly Flows (`Mon–Sun`)** | `{stats['total_flows']}` (`{stats['wkd_flows']}` Wkd / `{stats['wknd_flows']}` Wknd) | Weekday `08:00–24:00` + Weekend `12:00–16:00` `[src: CLK]` |",
        f"| **3x3 Craft Sprints (`C1–C3`)** | `{stats['craft_slots']}` sprints (`{stats['total_slots']}` slot_ids) | `3 × 30m` Craft per Flow + `DD-22A` P/M/R bands `[src: DSP]` |",
        f"| **6 Portfolio Areas** | `6 Areas · {l1_total} L1 · {l2_total} L2` | Canonical `06-PORTFOLIO` standard `[src: OP]` |",
        f"| **G1 Readiness & Overrides** | `{handoff['operator_g1_status']}` (`{ov_count}` overrides) | OP: `{meta['op_status']}` · Cal: `{meta['calendar_status']}` `[src: INT]` |",
        "",
        "## 01 · Operator Decisions (`New` & `Ongoing` · `G1`)",
        "",
        "Standard clock windows live solely in `02-weekly-dispersal/week-blueprint.json`.",
        "",
        *dec_lines,
        "",
        "## 02 · Matrix 1 Overview (`6 Portfolio Areas`)",
        "",
        "Full `G|I|P|S|O|C` fields and `Tasks -> Subtasks` open interactively in the HTML Cockpit.",
        "",
        "| Rank | Portfolio Area | `L1` Priority Outcomes (`WP` Ref) | `L2` Nice | Cross-Repo Edges |",
        "|---|---|---|---|---|",
        *p_rows,
        "",
        "## 03 · Matrix 2 Calendar Collisions & Personal Focus",
        "",
        "The full `Mon–Sun` hourly timetable lives inside Section `03` of the HTML Cockpit.",
        "",
        "| Date | Event | Window | Policy | Capacity Delta |",
        "|---|---|---|---|---|",
        *cal_rows,
        "",
        *focus_lines,
        "",
        "## 04 · Residual Information & 1-Hop Provenance",
        "",
        op_state_line,
        "",
        "| `WP` Ref | Deferred Item | Reason | Revisit Trigger |",
        "|---|---|---|---|",
        *def_rows,
        "",
        "| Tag | Source | Freshness |",
        "|---|---|---|",
        *prov_rows,
        "",
        f"- **Confidence:** {residuals['confidence']}",
        f"- **Assumptions:** {residuals['assumptions']}",
        "",
        "## 05 · Sequencing Orientation (`T2` Allocation)",
        "",
        f"All `240` slot occurrences are bound dynamically by `allocate_week.py` (`DD-16`: zero BP floor).",
        "",
        f"- **Projected Yield (`[src: DSP]`):** `{stats['total_flow_tp_min']:,}m` TP (`2,808m` slots + `72m` recap) · `{stats['total_projected_xp']:,.1f}` XP (`C {stats['xp']['C']:,.1f}`, `M {stats['xp']['M']:.2f}`, `P {stats['xp']['P']:.2f}`, `R 0.0`) · `BP {stats['bp']['total_bp']:.1f}` (`50/25/25`).",
        f"- **Gaussian Focus Coupling:** `σ = 6.0h` centered on `19:00` (`w_max = 1.5x`, zero Fri→Sat bleed).",
        "",
        "## Compact Downstream Handoff (`PrecapWeek -> PrecapNextDay`)",
        "",
        "```yaml",
        handoff_yaml,
        "```",
        "",
    ]
    return "\n".join(lines)


def main() -> int:
    here = Path(__file__).resolve().parent
    parser = argparse.ArgumentParser(description="Validate & compile Precap Week Cockpit + OKF Brief + Handoff.")
    parser.add_argument("--data", required=True, help="Path to PRECAP-WEEK-DATA-v2.1 JSON")
    parser.add_argument("--intake", help="Optional path to OPERATOR-COMMAND-BRIEF-v1.0 JSON")
    parser.add_argument("--dispersal-dir", default=str(here.parent / "02-weekly-dispersal"))
    parser.add_argument("--schemas-dir", default=str(here / "schemas"))
    parser.add_argument("--html-out", help="Output path for v0.5 interactive HTML Cockpit")
    parser.add_argument("--okf-out", help="Output path for OKF v0.2 Weekly Command Brief (.okf.md)")
    parser.add_argument("--handoff-out", help="Output path for standalone presentation_handoff JSON")
    parser.add_argument("--validate-only", action="store_true", help="Run schema & invariant checks without writing files")
    args = parser.parse_args()

    schemas_dir = Path(args.schemas_dir)
    dispersal_dir = Path(args.dispersal_dir)

    cockpit = json.loads(Path(args.data).read_text(encoding="utf-8"))
    intake = json.loads(Path(args.intake).read_text(encoding="utf-8")) if args.intake else None

    cockpit_schema = json.loads((schemas_dir / "precap-week-cockpit.schema.json").read_text(encoding="utf-8"))
    handoff_schema = json.loads((schemas_dir / "presentation-handoff.schema.json").read_text(encoding="utf-8"))
    intake_schema = (
        json.loads((schemas_dir / "operator-weekly-command-brief.schema.json").read_text(encoding="utf-8"))
        if intake is not None
        else None
    )

    errors = validate_semantics(cockpit, handoff_schema, cockpit_schema, intake, intake_schema)
    if errors:
        print("VALIDATION FAILED:", file=sys.stderr)
        for err in errors:
            print(f"  - {err}", file=sys.stderr)
        return 1

    blueprint = json.loads((dispersal_dir / "week-blueprint.json").read_text(encoding="utf-8"))
    demand = json.loads((dispersal_dir / "week-demand.json").read_text(encoding="utf-8"))
    inventory = json.loads((dispersal_dir / "slot-inventory.json").read_text(encoding="utf-8"))
    allocation = json.loads((dispersal_dir / "week-allocation.json").read_text(encoding="utf-8"))

    stats = compute_dispersal_stats(blueprint, demand, inventory, allocation, cockpit["meta"])
    print(f"Schema + T1/T2 validation PASSED ({cockpit['meta']['week_id']}, 6 Portfolios, {stats['total_flows']} Flows, {stats['total_slots']} slots).")

    if args.validate_only:
        return 0

    if args.html_out:
        out_p = Path(args.html_out)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(render_html(cockpit, stats), encoding="utf-8")
        print(f"Wrote HTML Cockpit -> {out_p}")

    if args.okf_out:
        out_p = Path(args.okf_out)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(render_okf_brief(cockpit, stats), encoding="utf-8")
        print(f"Wrote OKF v0.2 Brief -> {out_p}")

    if args.handoff_out:
        out_p = Path(args.handoff_out)
        out_p.parent.mkdir(parents=True, exist_ok=True)
        out_p.write_text(json.dumps(cockpit["presentation_handoff"], indent=2, ensure_ascii=False) + "\n", encoding="utf-8")
        print(f"Wrote Presentation Handoff -> {out_p}")

    return 0


if __name__ == "__main__":
    raise SystemExit(main())
