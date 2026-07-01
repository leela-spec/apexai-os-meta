# Verification & Extension Task — Apex Orchestration Repo Research

## Role
You are Gemini 3.5 Flash in Thinking mode, acting as an independent fact-checker and research extender. Use your 1M-token context window and native tool-calling/agentic capabilities to verify claims and find additional sources [web:96][web:101]. Do not trust the input report's numbers — treat every stat as unverified until you confirm it.

## Input
Below is a research report (produced by Claude Sonnet) claiming to identify star-rated GitHub repos for a personal Claude Code orchestration system called "Apex." [PASTE FULL REPORT HERE]

## Your Task — Three Phases

### Phase 1: Verification (mandatory, do first)
For every repo in the Ranked Table and Detailed Candidate Profiles, verify via live web/GitHub search:
- Exact current star count, fork count, last commit date, license
- Whether claimed file paths (`.claude/agents/`, `bmad-core/agents/`, etc.) actually exist in the repo — fetch the real GitHub file tree, do not infer from README text
- Whether the repo is still active/maintained (not archived, not abandoned)
- Flag any claim in the report that is unverifiable, outdated, or wrong

Output a **Verification Table**:
| Claim | Reported Value | Verified Value | Status (Confirmed/Corrected/Unverifiable) | Source URL |

### Phase 2: Gap-Fill Research
The original report may have missed relevant repos. Search specifically for:
- Repos updated or trending in the last 90 days (June–Sept 2026) matching: `.claude/agents`, `CLAUDE.md`, `subagents`, `agent orchestration`, `personal AI operating system`
- Non-English repos or lesser-known repos with real `.claude/` folder implementations (search GitHub code search, not just repo search)
- Any repos specifically using Gemini 3.5 Flash / Antigravity / Gemini CLI for personal orchestration, since these are new as of May 2026 and may offer patterns transferable to Claude Code
- Repos implementing "weekly workflow," "session logging," or "git-backed task state" that weren't in the original report
- Any repo claiming to be a working reference implementation of "personal AI orchestration OS" with real usage evidence (not just a README pitch)

For each new candidate found, provide the same structured profile format as Phase 1 (stars, license, last update, verified file tree, copyable patterns).

### Phase 3: Corrected Deliverable
Produce a revised version of these two sections only, incorporating verified data and any new candidates:
1. **Corrected Ranked Table** (same columns as original: Rank, Repo/System, URL, Stars, Category, Copyability, Local Viability, Orchestration Relevance, Repo Structure Value, Token-Cost Fit, Resilience, Maturity, Apex Fit, Main Usefulness, Main Risk, Verdict)
2. **Corrected Source Download Manifest** (same YAML schema as original `sources:` block)

## Hard Constraints
- Do not invent file trees, star counts, or repo structures. If you cannot verify something, mark it "unverifiable" explicitly rather than guessing.
- Every claim must carry an inline source citation with URL.
- Do not re-litigate the whole report's reasoning — focus only on factual verification and gap-filling.
- Keep the same practical filter as the original: local-first, repo-based, one-person-operable, no enterprise/Kubernetes/multi-cloud systems.
- If a repo is unmaintained (no commits >12 months) or archived, flag it as `risk_flag: too_unmaintained` regardless of star count.

## Output Format
Machine-readable first: tables and YAML blocks. Minimal prose. Flag every discrepancy explicitly rather than silently correcting it.