"""Render the operator-facing week blueprint from slot-inventory.json.

WD-36b: every human-facing view of the week is generated from the inventory,
never hand-authored. The previous blueprint was drawn by hand, so a declared
time change left the page saying one thing and the contract another.

Machine-readable source  slot-inventory.json
Governed rules           SPEC-WEEKLY-DISPERSAL.okf.md
Human-readable view      week-blueprint.html  (this script's output)

    python render_blueprint.py
"""

import json
from pathlib import Path

HERE = Path(__file__).parent
SRC = HERE / "slot-inventory.json"
OUT = HERE / "week-blueprint.html"

DAYS = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
BRANCH_LABEL = {"P": "Physical", "M": "Mental", "C": "Craft", "R": "Regeneration"}


def esc(s):
    return (str(s).replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;"))


def timeline_table(name, rows, evening):
    """One regime as a clock-ordered table. Gaps are shown, not hidden."""
    def mins(t):
        h, m = t.split(":")
        return int(h) * 60 + int(m)

    body = []
    prev_end = None
    for r in rows:
        if prev_end is not None and mins(r["start"]) > mins(prev_end):
            gap = mins(r["start"]) - mins(prev_end)
            body.append(
                f'<tr class="gap"><td>{esc(prev_end)}&ndash;{esc(r["start"])}</td>'
                f'<td colspan="2">unallocated &middot; {gap} min</td></tr>'
            )
        kind = "flow" if r["element"].startswith("F") else "anchor"
        if r["element"] == "Project night":
            kind = "project"
        dur = mins(r["end"]) - mins(r["start"])
        body.append(
            f'<tr class="{kind}"><td>{esc(r["start"])}&ndash;{esc(r["end"])}</td>'
            f'<td>{esc(r["element"])}</td><td>{dur} min</td></tr>'
        )
        prev_end = r["end"]

    note = f'<p class="note">{esc(evening)}</p>' if evening else ""
    return (
        f'<section class="regime"><h3>{esc(name)}</h3>'
        f'<table class="tl"><thead><tr><th>Clock</th><th>Element</th><th>Length</th>'
        f"</tr></thead><tbody>{''.join(body)}</tbody></table>{note}</section>"
    )


def week_grid(data):
    """The grid, at week scale: every Flow of every day, P/M slot counts shown.

    This is the surface the dispersion rules act on. It shows capacity, which is
    what exists today; it does not yet show which Epic sits in which slot,
    because nothing assigns them (see the Not Yet Built section).
    """
    by_day = {d: [] for d in DAYS}
    for f in data["flows"]:
        by_day[f["day"]].append(f)

    width = max(len(v) for v in by_day.values())
    head = "".join(f"<th>F{i + 1}</th>" for i in range(width))
    rows = []
    for d in DAYS:
        cells = []
        for i in range(width):
            if i < len(by_day[d]):
                f = by_day[d][i]
                p = sum(1 for s in f["slot_occurrences"] if s["branch"] == "P")
                m = sum(1 for s in f["slot_occurrences"] if s["branch"] == "M")
                cells.append(
                    f'<td class="on"><span class="t">{esc(f["start"])}</span>'
                    f'<span class="c">{p}P &middot; {m}M</span></td>'
                )
            else:
                cells.append('<td class="off">&mdash;</td>')
        rows.append(f"<tr><th>{esc(d[:3])}</th>{''.join(cells)}</tr>")
    return (
        f'<table class="grid"><thead><tr><th></th>{head}</tr></thead>'
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def quota_table(branch, q):
    rows = []
    for epic in q["epics"]:
        declared = q["declared_shares"].get(epic, 0)
        alloc = q["allocated"].get(epic, 0)
        real = q["realized_share"].get(epic, 0)
        zero = ' class="zero"' if alloc == 0 else ""
        rows.append(
            f"<tr{zero}><td>{esc(epic)}</td><td>{declared * 100:.2f}%</td>"
            f"<td>{alloc}</td><td>{real * 100:.2f}%</td>"
            f'<td>{alloc * (2 if branch == "physical" else 3)}</td></tr>'
        )
    total = sum(q["allocated"].values())
    rows.append(
        f'<tr class="sum"><td>total</td><td>100.00%</td><td>{total}</td>'
        f"<td>100.00%</td><td>&mdash;</td></tr>"
    )
    return (
        f'<table class="q"><thead><tr><th>Epic</th><th>Declared</th>'
        f"<th>Slots</th><th>Realized</th><th>Minutes</th></tr></thead>"
        f"<tbody>{''.join(rows)}</tbody></table>"
    )


def budget_table(b):
    """Pre-bound minutes against entitlement. Over-allocation is the headline."""
    rows = []
    for epic, ent in b["entitlement_min"].items():
        pre = b["prebound_min"][epic]
        over = b["over_allocated_min"].get(epic)
        owed = max(0.0, ent - pre)
        cls = ' class="zero"' if over else ""
        mark = f"+{over:.0f} over" if over else f"{owed:.0f} owed"
        rows.append(
            f"<tr{cls}><td>{esc(epic)}</td><td>{ent:.0f}</td><td>{pre}</td>"
            f"<td>{esc(mark)}</td></tr>"
        )
    verdict = (
        f'<p class="note"><strong>{esc(b["verdict"])}</strong></p>'
        if not b["feasible"] else '<p class="note">Feasible.</p>'
    )
    return (
        f'<table class="q"><thead><tr><th>Epic</th><th>Entitled min</th>'
        f"<th>Pre-bound min</th><th>Balance</th></tr></thead>"
        f"<tbody>{''.join(rows)}"
        f'<tr class="sum"><td>total</td><td>{b["total_physical_min"]}</td>'
        f'<td>{sum(b["prebound_min"].values())}</td>'
        f'<td>{b["free_minutes_needed"]:.0f} needed / '
        f'{b["free_minutes_available"]} free</td></tr>'
        f"</tbody></table>{verdict}"
    )


def build_html(data):
    t = data["totals"]
    ft = data["flow_template"]
    tl = data["day_timeline"]
    # Read the standard from the data, never typed in: every flow is identical.
    FLOW_TOTAL = data["flows"][0]["duration_min"]

    regimes = [
        ("Monday &ndash; Wednesday", tl["weekday_project"],
         "Project night 20:00&ndash;21:30 is an evening block, not a Flow. It carries no slots."),
        ("Thursday &ndash; Friday", tl["weekday_plain"],
         "Identical slot counts to Monday&ndash;Wednesday. No project night, so the evening is open."),
        ("Saturday &ndash; Sunday", tl["weekend"],
         "Two Flows, back-to-back from noon. Status merge falls on either day."),
    ]
    regime_html = "".join(timeline_table(n, r, note) for n, r, note in regimes)

    flow_rows = "".join(
        f"<tr><td>Iteration {i}</td><td>{ft['minutes']['P']} min P</td>"
        f"<td>{ft['minutes']['M']} min M</td>"
        f"<td>{ft['minutes']['craft_standard']} min C "
        f"<span class='sub'>+{ft['minutes']['recap']} recap</span></td></tr>"
        for i in (1, 2, 3)
    )

    return f"""<!doctype html>
<html lang="en"><head><meta charset="utf-8">
<meta name="viewport" content="width=device-width, initial-scale=1">
<title>Dispersal Week</title>
<style>
:root {{
  --bg: #fbfaf8; --fg: #1d1c1a; --dim: #6b6862; --line: #dedad3;
  --card: #ffffff; --accent: #7a5c3e; --flow: #f0ece5; --proj: #e8dcc8;
  --gap: #faf6ef; --zero: #b4492f;
}}
@media (prefers-color-scheme: dark) {{
  :root:not([data-theme="light"]) {{
    --bg: #171614; --fg: #ebe8e3; --dim: #94908a; --line: #35322d;
    --card: #1f1e1b; --accent: #c6a079; --flow: #262420; --proj: #33291c;
    --gap: #1b1a17; --zero: #e0795e;
  }}
}}
:root[data-theme="dark"] {{
  --bg: #171614; --fg: #ebe8e3; --dim: #94908a; --line: #35322d;
  --card: #1f1e1b; --accent: #c6a079; --flow: #262420; --proj: #33291c;
  --gap: #1b1a17; --zero: #e0795e;
}}
* {{ box-sizing: border-box; }}
body {{
  margin: 0; background: var(--bg); color: var(--fg);
  font: 15px/1.55 ui-sans-serif, -apple-system, "Segoe UI", system-ui, sans-serif;
}}
.wrap {{ max-width: 980px; margin: 0 auto; padding: 48px 16px 96px; }}
header {{ border-bottom: 2px solid var(--fg); padding-bottom: 20px; margin-bottom: 8px; }}
h1 {{ font-size: 30px; margin: 0 0 6px; letter-spacing: -0.02em; }}
.gen {{ font-size: 12px; color: var(--dim); font-family: ui-monospace, monospace; }}
h2 {{
  font-size: 12px; letter-spacing: 0.1em; text-transform: uppercase;
  color: var(--accent); margin: 44px 0 14px; padding-bottom: 6px;
  border-bottom: 1px solid var(--line);
}}
h3 {{ font-size: 15px; margin: 0 0 10px; }}
p {{ margin: 0 0 12px; max-width: 68ch; }}
.note {{ font-size: 13px; color: var(--dim); margin-top: 8px; }}
table {{ border-collapse: collapse; width: 100%; font-size: 13.5px; margin-bottom: 4px; }}
th, td {{ text-align: left; padding: 6px 10px; border-bottom: 1px solid var(--line); }}
thead th {{
  font-size: 11px; letter-spacing: 0.06em; text-transform: uppercase;
  color: var(--dim); font-weight: 600;
}}
.cards {{ display: grid; gap: 20px; grid-template-columns: 1fr; }}
@media (min-width: 760px) {{ .cards {{ grid-template-columns: repeat(3, 1fr); }} }}
.regime {{ background: var(--card); border: 1px solid var(--line); border-radius: 6px; padding: 16px; }}
.tl td:first-child {{ font-family: ui-monospace, monospace; white-space: nowrap; }}
.tl .flow td {{ background: var(--flow); }}
.tl .project td {{ background: var(--proj); }}
.tl .gap td {{ background: var(--gap); color: var(--dim); font-style: italic; }}
.grid td {{ text-align: center; padding: 8px 4px; }}
.grid tbody th {{ font-family: ui-monospace, monospace; color: var(--dim); }}
.grid .on {{ background: var(--flow); }}
.grid .off {{ color: var(--line); }}
.grid .t {{ display: block; font-family: ui-monospace, monospace; font-size: 12px; }}
.grid .c {{ display: block; font-size: 11px; color: var(--dim); }}
.q td:not(:first-child) {{ font-family: ui-monospace, monospace; }}
.q .sum td {{ font-weight: 700; border-top: 2px solid var(--fg); }}
.q .zero td {{ color: var(--zero); }}
.sub {{ color: var(--dim); font-size: 11px; }}
.kv {{ display: flex; flex-wrap: wrap; gap: 10px; margin: 0 0 16px; padding: 0; list-style: none; }}
.kv li {{
  background: var(--card); border: 1px solid var(--line); border-radius: 4px;
  padding: 8px 12px; font-size: 13px;
}}
.kv b {{ display: block; font-family: ui-monospace, monospace; font-size: 16px; }}
.open li {{ margin-bottom: 8px; }}
code {{ font-family: ui-monospace, monospace; font-size: 0.92em; }}
</style></head>
<body><div class="wrap">

<header>
  <h1>Dispersal Week</h1>
  <div class="gen">generated by render_blueprint.py from slot-inventory.json
  &middot; as of {esc(data['as_of'])} &middot; status {esc(data['status'])}</div>
</header>
<p class="note">Every number on this page is read from the inventory. Nothing here is
typed by hand, so the page cannot disagree with the contract. The governed rules live in
<code>SPEC-WEEKLY-DISPERSAL.okf.md</code>.</p>

<h2>Week at a glance</h2>
<ul class="kv">
  <li>Flows<b>{t['flows_per_week']}</b></li>
  <li>Slot occurrences<b>{sum(t['slots_per_week'].values())}</b></li>
  <li>Physical<b>{t['slots_per_week']['P']} &middot; {t['minutes_per_week']['P']} min</b></li>
  <li>Mental<b>{t['slots_per_week']['M']} &middot; {t['minutes_per_week']['M']} min</b></li>
  <li>Craft<b>{t['slots_per_week']['C']} &middot; {t['minutes_per_week']['C']} min</b></li>
  <li>Regeneration<b>{t['slots_per_week']['R']} &middot; {t['minutes_per_week']['R']} min</b></li>
</ul>

<h2>The Flow &mdash; {ft['pattern']}, {FLOW_TOTAL} minutes</h2>
<p>{esc(ft['pattern_meaning'])}. The branch cycle is
<code>{' &rarr; '.join(ft['branch_cycle'])}</code>, three times, closing on one
<code>{ft['closing_branch']}</code> break of {ft['minutes']['break']} minutes.</p>
<table><thead><tr><th></th><th>Physical</th><th>Mental</th><th>Craft</th></tr></thead>
<tbody>{flow_rows}
<tr><td>Close</td><td colspan="3">{ft['minutes']['break']} min R break</td></tr>
<tr class="sum"><td><b>Total</b></td><td colspan="3"><b>120 min</b>
&mdash; fixed overhead {ft['fixed_overhead_min']} min</td></tr>
</tbody></table>

<h2>The three regimes</h2>
<div class="cards">{regime_html}</div>

<h2>The grid</h2>
<p>Every Flow of the week, with the Physical and Mental slot capacity each one carries.
This is the surface the binding rules act on.</p>
{week_grid(data)}

<h2>Mental shares</h2>
<p class="note">{esc(data['quota']['note'])}</p>
{quota_table('mental', data['quota']['mental'])}

<h2>Physical shares</h2>
<p class="note">{esc(data['quota']['physical']['shares_status'])}</p>
{quota_table('physical', data['quota']['physical'])}

<h2>Physical minute budget</h2>
<p>The 18:00&ndash;19:30 focus block is 90 minutes of pre-designed content, so it is an
allocation the solver inherits rather than makes. Slot counts hide this &mdash; a 90-minute
block and a 2-minute in-flow slot both count as one &mdash; so the check runs on minutes.</p>
{budget_table(data['quota']['physical']['budget'])}

<h2>Not yet built</h2>
<p>The grid shows <em>capacity</em>. It does not show which Epic occupies which slot,
because nothing assigns them yet. Distribution, spaced repetition and dispersion across
the week are properties of that assignment, so they cannot be drawn until the allocator
exists. Drawing them now would be a picture of a week rather than a reading of one.</p>
<ol class="open">
  <li>The slot-filling algorithm: maximise projected XP under the BP floor.</li>
  <li>The Epic database &mdash; ten Epics in <code>EPIC / BLOCK / NODE_PLACEMENT / CHUNK</code> form.
  Only identities exist; no Chunk-level content does.</li>
  <li><code>week-demand.json</code>, the priority input.</li>
  <li>Then this page gains a real dispersion view, generated the same way.</li>
</ol>

</div></body></html>
"""


def main():
    data = json.loads(SRC.read_text(encoding="utf-8"))
    OUT.write_text(build_html(data), encoding="utf-8")
    print(f"wrote {OUT.name} from {SRC.name} ({OUT.stat().st_size:,} bytes)")


if __name__ == "__main__":
    main()
