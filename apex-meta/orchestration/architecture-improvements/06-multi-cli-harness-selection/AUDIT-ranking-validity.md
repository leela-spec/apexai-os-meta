---
type: Audit
id: AUDIT-MULTICLI-RANKING-20261109
title: "Validity audit of the multi-CLI harness desk ranking"
description: "Arithmetic, scale, scope and factual defects in RESEARCH-MULTICLI-HARNESS-20261109 section 2, with the corrected ordering and the licence and cost facts the source omitted."
status: candidate
date: 2026-11-09
tags: [orchestration, audit, mcda, cli-agents]
---

# Validity audit — multi-CLI harness desk ranking

Audited artifact: `C:\Users\gehma\Downloads\2026-11-09-multi-cli-harness-operator-bakeoff.md` (RESEARCH-MULTICLI-HARNESS-20261109), section 2 table at lines 56-62.

## Verdict

Yes. Four defects invalidate the ordering and one invalidates the criterion set.

D-02 alone inverts ranks 1 and 2. D-04, D-04b and D-05 make the top row unactionable and reverse the plugin choice inside it. D-10 is a factual error that disqualifies rank 2 on the operator's host. D-07 misallocates 35% of the weight to capability the same document forbids adopting. The table should not be repaired and re-ordered; its criteria do not match this operator, so section 2 is replaced by `RANKING-per-workload.md`.

What the audit did **not** find: the weights sum to 100, four of five composites are arithmetically correct, and all seven cited GitHub issues exist with titles matching the document's characterisation. The evidence base is honest; the scoring layer on top of it is not.

## 1. Arithmetic recheck

Formula recovered from the table: composite = sum(score x weight) / 5. Verified against the CAO row: `1.5*25 + 5*20 + 5*20 + 5*15 + 2*10 + 4*10 = 372.5`, `/5 = 74.5`.

| Candidate | Stated | Recomputed | Delta |
|---|---:|---:|---:|
| Paseo + one account plugin | 78.0 | **76.0** | -2.0 |
| CAO | 74.5 | 74.5 | 0 |
| OpenMausBot | 69.5 | 69.5 | 0 |
| Orca | 64.0 | 64.0 | 0 |
| Omnigent | 61.5 | 61.5 | 0 |

**D-01** The rank-1 row is the only arithmetic error, and it runs in that row's favour. `4.0*25 + 5.0*20 + 3.0*20 + 4.0*15 + 2.0*10 + 4.0*10 = 380`, `/5 = 76.0`, not 78.0. Rank order is preserved, but the margin over CAO falls from 3.5 to 1.5 on an instrument the document itself calls "a transparent analyst assessment of documented feature-fit" (line 54).

## 2. Rank-inverting defects

### D-02 — Quota score 4.0 contradicts the primary source (inverts ranks 1 and 2)

The 25%-weighted criterion is "quota-aware continuation". `jgreys/paseo-accounts` `TESTING.md`, read today, states that real-account coverage is "On macOS 26 with Paseo 0.12, Claude Code 2.1 and several Claude Ultra accounts", and lists under **Only covered by automated tests**: "ChatGPT (Codex) accounts, beyond sign-in and usage reading" and "Linux and Windows hosts".

The operator's configuration is Windows 11 and two Codex accounts. On that configuration the capability carrying the heaviest weight has **zero real-account evidence**. The document knows this — lines 36, 113 and P0 item 6 say so — and scores it 4.0/5 anyway.

Rescored on the rubric the document applies to other rows, where "not established" earns 1.5 (CAO, Omnigent):

| Quota score | Paseo composite | Rank |
|---|---:|---|
| 4.0 (as stated) | 76.0 | 1 |
| 2.0 | 66.0 | 2, behind CAO |
| 1.5 | 63.5 | 2, behind CAO |

The inversion survives correcting CAO in the other direction as well (see D-09): CAO at Durable 4.0 scores 70.5, still ahead.

### D-04 — The top row is an unresolved disjunction

Section 1 screens `Paseo + Paseo Accounts` and `Paseo + ZeroSub` as two candidates (lines 36-37). Section 2 scores one row, "Paseo + one account plugin" (line 58). Section 4 then states that the two differ precisely on the decisive seam: ZeroSub "documents account-specific Codex continuation tabs" (line 114), while line 113 calls the Codex transition "precisely the critical unexplored seam for the user's 2 Codex logins". A single score cannot stand for two products that the same document says diverge on the criterion worth 25%.

### D-04b — The two plugins are not independent comparators

`jgreys/paseo-accounts/LICENSE` reads "MIT License / Copyright (c) 2026 Greys / **Portions copyright (c) 2026 Kapybara**". Kapybara publishes ZeroSub (`@kapybara/zerosub`). The rank-1 plugin therefore incorporates code from the plugin the document positions as its independent "Comparator to first row" (line 37). Neither the document nor the plugin's `README.md` or `OVERVIEW.md` discloses the derivation. A derivative cannot validate its own origin.

### D-05 — Maintenance evidence reverses the plugin choice

The operator's outcome contract asks for an **established** harness (line 17). Neither plugin's footprint appears anywhere in the document. Measured via the GitHub API today:

| | `jgreys/paseo-accounts` | `kapybara-org/zerosub` |
|---|---|---|
| Created | 2026-10-20 (20 days) | 2026-09-23 (47 days) |
| Last push | 2026-11-01 (8 days stale) | 2026-11-09 (today) |
| Contributors | 1 (`jgreys`, 9 commits) | 5+ (`sanjaydotpro`, 37 commits) |
| Forks / watchers / open issues | 1 / 0 / 0 | 22 / - / 8 |
| Licence | MIT (+ Kapybara portions) | MIT |
| Published downloads | not published | 1,196 / 30 days |

The document ranks the thinner, derived, staler of the two first.

## 3. Framework defects

### D-03 — The heaviest criterion has no rubric

Nothing in the table separates these three states, yet they are scored 4.0, 2.0 and 2.0:

- **implemented, untested on target** — Paseo plugin rotation, 4.0
- **reproduced and working, wrong scope** — OpenMausBot cross-provider takeover, confirmed live in issue 3892, 2.0
- **manual only** — Orca hot-swap, 2.0

Twenty-five percent of the weight rests on an undefined scale, so the rows are not comparable on it.

### D-06 — A hard gate is priced as a soft criterion

P0 items 1, 4 and 5 declare third-party Antigravity use **BLOCKED**, Paseo's Antigravity integration "Unsafe for an unrestricted live Apex repository", and CAO's defaults "dangerous". Line 54 states "Gaps cannot be compensated for by a numeric score". The table then prices a P0 block at `2.0 x 10% = 6` points out of 100 and compensates for it with feature breadth. Hard gate and weighted criterion are mutually exclusive constructions; the document asserts both.

### D-07 — The constraints contradict 35% of the weight

Line 19 forbids reimplementing an agent runtime or creating a competing canonical task database. Line 54 allocates durable task recovery 20% and orchestration/workflows/skills 15% — 35% combined — to exactly that capability. CAO's rank-2 standing is built on it.

This is not a theoretical conflict. The operator already owns two purpose-built orchestration systems, both implemented as Claude Code skills and subagents with file-backed state and operator gates: `.claude/skills/weekly-orchestrator/SKILL.md` (stages G1-G5, `execution: context_fork`) and `apex-meta/orchestration/00-START-HERE.md` (five invariants; Alfred, Meta Ops and Meta Detective lanes). A harness scored highly for supplying its own journal, its own task state and its own memory promotion is being rewarded for duplicating what exists and for breaching invariant 1 ("state lives in files") and invariant 5 ("candidate never auto-promotes").

### D-08 — Paseo's Durable 3.0 is unsourced

Line 36 says "not a proven cross-run transaction journal". Line 28 says the transcript "starts fresh after daemon restart". T06 (line 95) requires "crash after saved sub-step; completed verified sub-step never reexecuted". No cited source supplies a saved sub-step. A reset-on-restart transcript is the failure of the criterion, not a mid-grade.

### D-09 — CAO's Durable 5.0 is overstated by the document's own caveat

Line 117: CAO workflows "re-execute workflow control scripts from the start, with recorded completed step values replayed... do not confuse this with arbitrary exactly-once side-effect safety". A maximum score for durable recovery on a system explicitly described as not exactly-once is an overclaim. Correcting it lowers CAO to 70.5 and does not affect D-02's inversion.

## 4. Factual errors

### D-10 — CAO cannot run on the operator's host; it is scored 4.0 for local feasibility

`awslabs/cli-agent-orchestrator`, `src/cli_agent_orchestrator/__init__.py`, read today:

> `if sys.platform == "win32": raise ImportError("cli-agent-orchestrator does not support Windows. ... Supported: macOS (arm64, x86_64) and Linux (x86_64). On Windows, run CAO under WSL2 or a Linux container...")`

The package refuses to import on Windows. `README.md` requires tmux 3.3 or later, which has no native Windows build. The document scores CAO 4.0/5 on "Windows/local/open-source feasibility" — the same score it gives Paseo, which does publish Windows installers (`Paseo-Setup-0.15.3-x64.exe`, release v0.15.3) — and never mentions tmux or the import guard. CAO on this host is a WSL2 deployment orchestrating Linux-side CLIs, which is a materially different proposal from the one scored.

### D-14 — The evidence is version-stale and one source expires

The plugin's real-account evidence is against Paseo 0.12; the catalog entry against Paseo 0.9.1; the current release is 0.15.3. `paseo.cafe`, cited at line 143, states it "is deprecated" and that "This catalog and its API stop on 2026-12-01" — three weeks out.

## 5. Unreconciled constructions

### D-11 — Rank is not eligibility

Line 78 permits choosing Paseo only if "Windows real-CLI failover works". Lines 36, 113 and 167 establish that it is untested and that no test was performed. The rank-1 option is therefore trigger-ineligible on present evidence, while line 169 calls it "the first promising feature-complete combination". The document never states that its ranking orders candidates rather than recommendations.

### D-12 — Two instruments disagree

The composite ranks Paseo 1 on E48, the lowest evidence score of the five. Orca ranks 4 on E80 R53, the best evidence and lowest risk. Line 64 correctly forbids combining I/E/R into a formula, but the document never says which instrument governs a decision, and they disagree on three of five rows.

### D-13 — Trial order is circular

Section 1 assigns Trial 1 through Trial 4 in composite order, so the validation sequence is determined by the scores the validation exists to test.

## 6. Open source and cost — verified

All four candidates named in the request are open source and free to run locally. The only cost is the provider subscriptions already held.

| Product | Licence (verified today) | Free to self-host | Paid tier |
|---|---|---|---|
| Paseo | Apache-2.0 for its own code; third-party portions keep their own licences, so GitHub classifies the repo `NOASSERTION` | Yes | Paseo Hub, optional and separate: self-hosted free; cloud Free $0 (50 agent runs/month, 1 seat); Pro $15/seat/month. Not mentioned in the source document. |
| Paseo Accounts (`jgreys`) | MIT, plus "Portions copyright (c) 2026 Kapybara" | Yes | none |
| ZeroSub (`kapybara-org`) | MIT | Yes | none |
| CAO (`awslabs`) | Apache-2.0 | Yes, on POSIX only | none |
| OpenMausBot | Apache-2.0 (desktop and companion apps) | Yes | cloud $15-$599/month; self-hosted business $299/month; "Model usage is billed by your provider" |
| Orca (`stablyai`) | MIT | Yes | none published; Enterprise page is contact-only |
| Multica | "Multica License" — Apache-2.0 as Part II plus Part I conditions; neither part grants rights alone | - | line 119's warning is correct |

## 7. Corrected ordering

On the document's own evidence, corrected for D-01, D-02 and D-09, CAO takes rank 1. D-10 then disqualifies CAO on the operator's host, and D-07 shows that most of what earned CAO those points duplicates orchestration the operator already owns and would breach its invariants.

The ranking is therefore not recoverable by re-ordering. See `RANKING-per-workload.md`.

## 8. Evidence register

Commands run 2026-11-09 from `C:\GitDev\apexai-os-meta` on Windows 11:

- `gh api repos/{owner}/{repo}` and `.../license` — licences, stars, timestamps and contributor counts for the eight repositories named above.
- `gh api repos/{owner}/{repo}/issues/{n}` for `stablyai/orca` 20512, 35806, 40321; `milind-soni/OpenMausBot` 3092, 3892, 5030; `getpaseo/paseo` 3589 — all seven exist, all titles match the document's characterisation.
- `gh api repos/jgreys/paseo-accounts/contents/TESTING.md` — platform coverage quoted in D-02.
- `gh api repos/awslabs/cli-agent-orchestrator/contents/src/cli_agent_orchestrator/__init__.py` — Windows guard quoted in D-10.
- `gh api repos/getpaseo/paseo/releases/latest` — Windows installer assets, v0.15.3.
- `qmd search` for "Paseo orchestration harness", "cli-agent-orchestrator CAO", "ZeroSub account rotation" and "account rotation failover quota exhausted" — **no results**. `qmd collection list` shows 40 collections, of which `openmausbot` is the only indexed candidate. The repository corpus holds no prior evaluation of Paseo, CAO or ZeroSub, so nothing in it corroborates or contradicts the source document on those three.

**Limitation:** this audit verified licences, platform support, repository footprint and cited-issue integrity through the GitHub API and published pages. It executed no harness, installed nothing and consumed no provider quota, so it confirms no failover behaviour in either direction.
