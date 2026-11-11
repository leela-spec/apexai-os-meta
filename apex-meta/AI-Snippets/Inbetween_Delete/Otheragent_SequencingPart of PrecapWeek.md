### First: I was not building in the wrong place

The files have always been in `C:\GitDev\MasterOfArts\Sequencing\dispersal` — the MasterOfArts repo. What’s wrong is the _session’s_ working directory, which is `C:\Quasi Desktop\Master Of Arts Business`. Relative links resolve against that, so `index.md` pointed into a folder where no such file exists. Same root cause both times, and my second fix didn’t take because a shell `cd` doesn’t move the session.

I’ve now moved the session itself to the dispersal folder. **It takes effect when this turn ends**, so links in _this_ message would still break. Plain paths for now:

C:\GitDev\MasterOfArts\Sequencing\dispersal\

Next turn the links will work. Page: **[claude.ai/artifact/4QEZffC7rxdqwKxVC9hcax](https://claude.ai/artifact/4QEZffC7rxdqwKxVC9hcax)** (v5).

### The new day

08:00-08:30  Morning Routine
08:30-10:30  Flow 1
10:30-12:30  Flow 2
12:30-13:30  Frühstück
13:30-15:30  Flow 3
15:30-16:00  Mittag              ← 30 min, was 60
16:00-18:00  Flow 4              ← held at 16:00, not shifted
18:00-19:30  physical focus      90 min
19:30-20:15  Abend               45 min
20:15-21:45  project night       90 min
21:45-22:45  Freizeit
22:45-23:15  Day Outro

**Your two instructions collided, and I had to pick.** A 30-minute later start pushes Flow 4 to 16:30–18:30, but you declared the evening chain as absolute clock times starting at 18:00. Both cannot hold. A Flow is fixed at 120 minutes, so only the meal anchors can absorb 30 minutes — and I gave it to Mittag. **That is my inference, not your instruction** (`DD-39`). Frühstück could absorb it instead; say the word and it moves.

Your evening numbers are internally consistent, which is how I knew to treat them as fixed: 19:30 + 45 = 20:15, and 20:15 + 90 = 21:45. I read “19:13” as 19:30.

### Making the focus block count breaks the quota

You said the 90 minutes count toward the physical quota with pre-designed per-day content. I applied that — and it makes the declared shares impossible:

|Epic|Entitled|Pre-bound|Balance|
|---|---|---|---|
|Martial Arts|208 min|**270**|+62 over|
|Dance|149 min|**180**|+32 over|
|S/BJJ|59 min|0|59 owed|
|General|89 min|0|89 owed|
|Knee|89 min|0|89 owed|

Strikes, Kicks and Kicks give Martial Arts 270 minutes against a 208 entitlement before the solver starts. Dance and Moves do the same to Dance. The other three are owed **238 minutes and only 144 in-Flow minutes exist**.

This is invisible in slot counts — a 90-minute block and a 2-minute slot both count as one — so `physical_budget()` checks it in minutes. Either the shares move or the block stops counting. I’m not choosing that for you; the shares are your dial. It is `DD-40`, and it blocks the allocator.

### The repo split — drafted, not executed

Your rule, applied: **the Flow is a Sequencing object; where Flows sit on a clock is Precap Week.** The current single spec mixes them.

**→ MasterOfArts (`Sequencing/dispersal/`) — the mechanism**

|What|Why|
|---|---|
|`SPEC-SEQUENCING-DISPERSAL.okf.md`|branches, XP/TP/BP, the 3×3 Flow contract, shares and the 5% ladder, the pre-bound check, binding notation, Epic/Block/Chunk conformance. **No clock times.**|
|`build_slot_inventory.py`, `slot-inventory.json`|Sequencing structure, instantiated|
|`ASSUMPTIONS-AND-DECISIONS-REGISTER.md`|the mechanism’s working record|
|Epic database, `week-demand.json`, the allocator|all Sequencing|

**→ apexai-os-meta (`...orchestration-weekly/02-weekly-dispersal/`) — the calendar and the operator surface**

|What|Why|
|---|---|
|`SPEC-WEEK-GEOMETRY.okf.md`|the three regimes, every clock time, Mon–Sun span, the Matrix 2 band|
|`week-geometry.json`|the machine-readable calendar — **an input to the generator, owned here**|
|`render_blueprint.py`, `week-blueprint.html`|the operator’s weekly view|
|`PRECAP-INTEGRATION-ANALYSIS.md`|entirely about Precap Week|

**The consequence you should weigh before saying yes:** this inverts one dependency. Today MasterOfArts hard-codes the clock and mirrors everything outward. After the split, apexai-os-meta owns the geometry and MasterOfArts _reads_ it — so `sync_dispersal.py` stops being one-way-per-repo and becomes one-way-per-file, each file flowing from its owner. That is more correct and slightly more machinery. The alternative is to keep the geometry vendored in MasterOfArts and accept that the calendar has two homes.

Committed so far: `0f316cf` and the index follow-up in MasterOfArts, `12832f77` and its follow-up in apexai-os-meta. Nothing pushed. Ten decisions open.