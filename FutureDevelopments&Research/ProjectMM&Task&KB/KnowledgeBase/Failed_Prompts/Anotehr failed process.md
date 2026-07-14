``# Apex Phase 0 Corpus Intelligence — Agent Implementation Task ## Process Run as: **GPT agent with Pro Thinking enabled** GitHub connector: `leela-spec/apexai-os-meta` (branch: main) Do NOT use public GitHub web URLs for private repo files. ## Mission Implement Phase 0 deterministic corpus intelligence for Apex. Architecture is locked (see § Architecture). Do not re-research it. Produce working code and verified patches. No drafts. No placeholders. ## Output priority (execute in this order) 1. Read live repo: `.claude/skills/apex-kb/SKILL.md`, `package-manifest.md`,    `references/script-command-contract.md`, `apex-meta/scripts/apex_kb.py`,   `apex-meta/kb/claude-skill-design/` (directory listing + kb-schema.md) 2. Write `apex-meta/scripts/phase0_corpus_intelligence.py` — full file 3. Write `.claude/skills/apex-kb/references/phase0-corpus-intelligence-contract.md` — full file 4. Produce verified append patches for read files (skip if unread, label UNVERIFIED) 5. Output validation commands + rollback ## Architecture (locked — do not re-derive) ```yaml phase0_role: deterministic_pre_llm_navigation_layer primary_script: apex-meta/scripts/phase0_corpus_intelligence.py primary_kb: apex-meta/kb/claude-skill-design/ output_root: apex-meta/kb/claude-skill-design/manifests/ integration: extends apex-kb skill — read-only, never mutates task/plan state v1_outputs:   - corpus-profile.md         # file count, size, heading stats, frontmatter coverage  - heading-map.json          # {file: [{level, text, anchor, line}]}  - markdown-link-map.json    # {file: [{href, text, type: md|wiki|url}]}  - frontmatter-map.json      # {file: {key: value}}  - keyword-hits.ndjson       # {file, line, keyword, context} one per line  - topic-file-map.json       # {topic_keyword: [files]}  - source-priority-candidates.md  # ranked candidate files for LLM ingest  - phase0-navigation-report.md    # human-readable summary of all above v1_5_outputs_optional:   - search-index.sqlite       # FTS5 if available  - link-graph.json           # full directed graph  - graph-summary.md parser:   v1: stdlib state machine (no external deps)  v1_5: markdown-it-py, python-frontmatter (optional, label clearly) degradation: continue if optional packages missing; label outputs accordingly ``` ## Script contract (implement exactly)``

subcommands: profile | parse-markdown | keyword-map | priority-candidates |  
navigation-report | search-index | graph | all

flags:  
--kb-root PATH (required) KB directory to scan  
--output-root PATH (required) where to write manifest files  
--check dry-run: compute but do not write; print what would be written  
--keywords STR comma-separated keyword list (default: built-in Apex keyword set)  
--topics STR comma-separated topic list

exit codes: 0=ok, 1=error, 2=partial (some optional steps skipped)

no network calls  
no LLM calls  
stdlib only for v1; optional deps for v1.5 with graceful fallback

text

``## Degradation rule If a repo file is unreadable: continue, skip its patch, label `UNVERIFIED`. Hard abort only if: no repo access AND no project sources AND no current context. ## Required output sections (in this order) 1. **Repo read ledger** — table: path | status | key facts 2. **`phase0_corpus_intelligence.py`** — complete file, no ellipsis 3. **`phase0-corpus-intelligence-contract.md`** — complete file 4. **Patches for read existing files** — unified diff or append block per file 5. **Validation commands** (PowerShell + bash) 6. **Rollback commands** 7. **Implementation order** (6 steps max) ## Explicit non-tasks - Do not re-evaluate the SQLite FTS5 retrieval architecture - Do not produce a source-read ledger with 22 entries before writing code - Do not ask the operator to choose between stdlib and markdown-it-py — default to stdlib v1 - Do not end with "further research needed"``

---

## Change Summary

|issue|original prompt|revised prompt|
|---|---|---|
|Process format|Deep Research (wrong)|Agent + Pro Thinking|
|Length|~2,100 words|~600 words|
|Source reads required before code|22 files|6 targeted reads|
|Output section order|verdict → ledger → arch → map → tree → contract → **code**|read ledger → **code first** → patches|
|`--check` definition|undefined|defined: dry-run, print what would be written|
|Architecture re-evaluation|8 D-decisions to resolve|locked, one YAML block|
|Degradation policy|3 nested YAML blocks|2 lines|
|Hard abort guardrails|6 conditions|1 condition|
|Computational weight|stated 70% impl, actual ~40%|enforced via output order|

Prepared using Claude Sonnet 4.6 Thinking

I don't think I understand your agent and pro thinking then you need to tell me exactly what information to give it so I'm prioritize so that it can actually work well because an agent run never sadly worked for me it never did what it was supposed to it used all tokens and stuff that it wasn't supposed to do it created in excessive ledgers and decisions carried forward and thereby all token has been lost on some processes instead of actual loops. Please give me a short analysis of what I need to prepare. So that this run is actually going well also I used a lot by created a lot of new research. That I will add to the project sources and send you a link off that needs to be included and I are we need to find a way on how to connect that. yeah Especially important is the most like this file and yeah, tell me what you think about it. Apex Phase 0 Corpus Intelligence Implementation Decision.md

![Attachment](blob:https://www.perplexity.ai/ea1d98df-0010-49bc-8db3-392c62249848)

image.jpg

This is exactly what I needed. The Implementation Decision file is excellent — complete, locked, no ambiguity. Here is the full analysis:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0a7c71a1-b7df-49f6-882d-f416bbe75f9e/Apex-Phase-0-Corpus-Intelligence-Implementation-Decision.md?AWSAccessKeyId=ASIA2F3EMEYE4HX22UJQ&Signature=ynTovNkndZPM3cKxzQtq%2BadnYKs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCv%2B%2BrTExVFaEUcdkf3tY2DA9%2FkkqAVZu3%2FuYPb4P644AIgdd3eLv%2FeRSdsnbtXNvYN8bqyPpXhS9od8EG76cz62jwq8wQIZRABGgw2OTk3NTMzMDk3MDUiDCix8f0RzeJRAeE6fyrQBA4EUyQbsUv3lZ50TfXdGS4hIRIdWyp7hS8g6fbZyPfl3r2ROLDH4Chd0AS0tqP0y29J7y0Hiow6pIXhQ0ZpqKc2P6uchR5hRAT3VXaf0asoCXe%2FNHSMqjW5iT6xj600v9oEdNxwisSyN01yXKOin9XGt59mW59s%2FWVF1tEGWzW8a6A8IpY5cg0pn8%2FgGC4Ei9k3XjJLpBfEilQo79pVgmQzyCk5KibZdgVolgTf1VWU%2BFZQUF%2B87xJOO3cpL83G08sg0%2FO33pcBDEEkFlBS8WpqN6prUJXzVEmsioz951YhmsCJyQzRT0XlLYteQufIJ2J9VaX3eY0Cnh4bTzuJXLHBYzia0mnDPNVLB63R6SafRMgoaxFiwwktd4PS8kSdc5uRV4rnA3DDOu%2FLJacAKdJwi3ZjP%2FKAyzvJiodPVoTi3zCMTbXPijAmhdAXjKyVYSmo7zE172vUdTViLiZA7sTbzGnb3LtX3gw8Rekh3PbQg6Zr80Nt%2FpAoAvQrs6s7vO1CwXRmbopCEFZj6bFiIbwa6PAzh4Y%2F9C5bEnoQLxU3dzd4kTCK70ZpqAxM6Il3JHYQcAT59f1PvbnCzuL11HWFDebt6X62M%2FeLWRhR3lKWJPDdX0TniHYe0%2BCdoVHGu4mdUZSGFCNp3tuDRJCvmT2dZSSr7XxFdJSKdmE2vQaqosdwOgUOYfGqMmvrw1Rm7M%2Fqqt1DXKdshGDjAw2xs2S%2BqDjbp20gkstybUqJ7aPgYn%2BonV9Kv%2F3dawCUvnzWCdZhGk2YEaV1T5K3HCCjuokw%2BMv50QY6mAH%2Bo4ioWGEgrpHtVrsXDCIpEOCYLCSouXySVeMfW%2Ff9E7X42RwYmMdoZGrHghyoFS9o9SLXD4lVgalZQHkCp7IqIo29UBWol3QaXaNS3KiNd%2FO7%2B6P26jJ9JAuZr9WXKLFzHUYl9ONTrEmZqLEqZks7LnJN1JwEHn46IEoCfxX8Q1L1be%2BOqCIGXPGwm1MGTXQpSKRwU6JZhQ%3D%3D&Expires=1782477771)

---

## Why Agent Runs Fail for You — Root Causes

The pattern you describe (excessive ledgers, token waste, no actual output) has 3 structural causes:

1. **Front-loaded comprehension phase.** The agent reads everything before doing anything. With 22 source files in P1+P2, it burns 60–80% of context on reading + summarizing before writing a single line of code.
    
2. **Source ledger as a completion signal.** Prompts that require a source-read ledger teach the model that "logging what I read = progress." It fills the ledger, runs out of tokens, never writes the script.
    
3. **No forced first output.** Without a hard constraint like "your first output must be the complete Python script," the model defaults to architecture narration.
    

---

## What You Actually Need to Prepare

## The good news: `Apex Phase 0 Corpus Intelligence Implementation Decision.md` is your single best asset

This file already contains:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/0a7c71a1-b7df-49f6-882d-f416bbe75f9e/Apex-Phase-0-Corpus-Intelligence-Implementation-Decision.md?AWSAccessKeyId=ASIA2F3EMEYE4HX22UJQ&Signature=ynTovNkndZPM3cKxzQtq%2BadnYKs%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCv%2B%2BrTExVFaEUcdkf3tY2DA9%2FkkqAVZu3%2FuYPb4P644AIgdd3eLv%2FeRSdsnbtXNvYN8bqyPpXhS9od8EG76cz62jwq8wQIZRABGgw2OTk3NTMzMDk3MDUiDCix8f0RzeJRAeE6fyrQBA4EUyQbsUv3lZ50TfXdGS4hIRIdWyp7hS8g6fbZyPfl3r2ROLDH4Chd0AS0tqP0y29J7y0Hiow6pIXhQ0ZpqKc2P6uchR5hRAT3VXaf0asoCXe%2FNHSMqjW5iT6xj600v9oEdNxwisSyN01yXKOin9XGt59mW59s%2FWVF1tEGWzW8a6A8IpY5cg0pn8%2FgGC4Ei9k3XjJLpBfEilQo79pVgmQzyCk5KibZdgVolgTf1VWU%2BFZQUF%2B87xJOO3cpL83G08sg0%2FO33pcBDEEkFlBS8WpqN6prUJXzVEmsioz951YhmsCJyQzRT0XlLYteQufIJ2J9VaX3eY0Cnh4bTzuJXLHBYzia0mnDPNVLB63R6SafRMgoaxFiwwktd4PS8kSdc5uRV4rnA3DDOu%2FLJacAKdJwi3ZjP%2FKAyzvJiodPVoTi3zCMTbXPijAmhdAXjKyVYSmo7zE172vUdTViLiZA7sTbzGnb3LtX3gw8Rekh3PbQg6Zr80Nt%2FpAoAvQrs6s7vO1CwXRmbopCEFZj6bFiIbwa6PAzh4Y%2F9C5bEnoQLxU3dzd4kTCK70ZpqAxM6Il3JHYQcAT59f1PvbnCzuL11HWFDebt6X62M%2FeLWRhR3lKWJPDdX0TniHYe0%2BCdoVHGu4mdUZSGFCNp3tuDRJCvmT2dZSSr7XxFdJSKdmE2vQaqosdwOgUOYfGqMmvrw1Rm7M%2Fqqt1DXKdshGDjAw2xs2S%2BqDjbp20gkstybUqJ7aPgYn%2BonV9Kv%2F3dawCUvnzWCdZhGk2YEaV1T5K3HCCjuokw%2BMv50QY6mAH%2Bo4ioWGEgrpHtVrsXDCIpEOCYLCSouXySVeMfW%2Ff9E7X42RwYmMdoZGrHghyoFS9o9SLXD4lVgalZQHkCp7IqIo29UBWol3QaXaNS3KiNd%2FO7%2B6P26jJ9JAuZr9WXKLFzHUYl9ONTrEmZqLEqZks7LnJN1JwEHn46IEoCfxX8Q1L1be%2BOqCIGXPGwm1MGTXQpSKRwU6JZhQ%3D%3D&Expires=1782477771)

- ✅ All D1–D8 architecture decisions, locked
    
- ✅ Exact V1 artifact contracts (schemas, required fields, acceptance criteria)
    
- ✅ Script shape + subcommand list
    
- ✅ What to reuse (`source-inventory.json/csv`)
    
- ✅ Explicit forbidden list (no LLM, no network, no wiki gen)
    
- ✅ V1 vs V1.5 scope boundary
    

**You do not need the 21 other research files in the agent context.** They were inputs to produce this decision file. The decision file IS the extracted output. Feeding all 22 files to the agent is redundant — it just recreates the synthesis work this file already completed.

## What to prepare — 4 items only

|item|what|why|
|---|---|---|
|1|`Apex Phase 0 Corpus Intelligence Implementation Decision.md`|Single source of truth for all decisions|
|2|GitHub connector active on `leela-spec/apexai-os-meta`|Live repo read for 5 targeted files only|
|3|Confirm local Python version + `python -c "import sqlite3; print(sqlite3.sqlite_version)"`|Agent needs to know FTS5 status before V1/V1.5 boundary decision|
|4|Confirm whether `source-inventory.json` exists at `apex-meta/kb/claude-skill-design/manifests/`|If yes, agent reuses it; if no, agent generates it first|

## Targeted repo reads (5 files max, not 22)

text

`apex-meta/kb/claude-skill-design/manifests/  ← directory listing only apex-meta/kb/claude-skill-design/kb-schema.md apex-meta/scripts/  ← directory listing to check if apex_kb.py exists .claude/skills/apex-kb/references/script-command-contract.md .claude/skills/apex-kb/package-manifest.md`

That is it. No orchestration skill reads, no retrieval research re-reads, no source history.

---

## Revised Agent Prompt (tight, output-first)

text

``# Apex Phase 0 — Implement phase0_corpus_intelligence.py ## Process Agent + Pro Thinking. GitHub connector on `leela-spec/apexai-os-meta` (main). Do NOT use public GitHub URLs. Private repo. ## Architecture: already decided — do not re-derive All decisions are in the attached file: `Apex Phase 0 Corpus Intelligence Implementation Decision.md` Read it once. Then implement. Do not re-research. ## Step 1 — Repo reads (do these first, fast) Read only: 1. `apex-meta/kb/claude-skill-design/manifests/` — directory listing 2. `apex-meta/kb/claude-skill-design/kb-schema.md` 3. `apex-meta/scripts/` — directory listing 4. `.claude/skills/apex-kb/references/script-command-contract.md` 5. `.claude/skills/apex-kb/package-manifest.md` For each: record path | status | 1 key fact. Nothing more. ## Step 2 — Write these files (this is the main task) ### REQUIRED — write in full, no placeholders, no ellipsis: **A. `apex-meta/scripts/phase0_corpus_intelligence.py`** Full Python script. Subcommands: `profile | parse-markdown | keyword-map | priority-candidates | navigation-report | all` Flags: `--kb-root PATH --output-root PATH --check` `--check` = dry-run: compute but write nothing, print what would be written. Exit codes: 0=ok, 1=error, 2=partial. V1 stack: stdlib only. No LLM. No network. Reuses `source-inventory.json` if present at `--kb-root/manifests/`. Produces all 8 V1 artifacts defined in the decision file. **B. `.claude/skills/apex-kb/references/phase0-corpus-intelligence-contract.md`** Full new file. Documents the script contract + artifact schemas. ## Step 3 — Patches for read files Only if the file was actually read in Step 1. If not read: write "UNVERIFIED — required change: [description]" and stop. Do not produce diff hunks for unread files. ## Step 4 — Validation + rollback PowerShell copy-paste commands only. Include expected output for each. ## Degradation rule If any repo file is unreadable: skip its patch, label UNVERIFIED, continue. Hard abort only if: GitHub connector totally fails AND decision file is unreadable. ## Forbidden - Source ledger longer than 5 rows - Architecture re-evaluation - "Further research needed" conclusion - Placeholder functions or `# TODO` in script - Reading any file not listed in Step 1``

---

## On Your New Research Files

The 8 new files you uploaded today are the **source inputs** that were synthesized into `Apex Phase 0 Corpus Intelligence Implementation Decision.md`. The decision file already extracted everything useful from them.

**You do not need to feed them all to the agent.** The only file from this batch worth including in the agent context is `link-graph.sample.json` — attach it as a concrete example for the V1.5 graph output schema. Everything else is captured in the decision file.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/collection_bb623669-af60-464a-9150-332aff44b287/8a806427-d4e3-42d4-af8a-4eae0c630351/link-graph.sample.json?AWSAccessKeyId=ASIA2F3EMEYE4HX22UJQ&Signature=3NWm8GmxXhg4tBTYHiaqUQxhqr4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJz%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIQCv%2B%2BrTExVFaEUcdkf3tY2DA9%2FkkqAVZu3%2FuYPb4P644AIgdd3eLv%2FeRSdsnbtXNvYN8bqyPpXhS9od8EG76cz62jwq8wQIZRABGgw2OTk3NTMzMDk3MDUiDCix8f0RzeJRAeE6fyrQBA4EUyQbsUv3lZ50TfXdGS4hIRIdWyp7hS8g6fbZyPfl3r2ROLDH4Chd0AS0tqP0y29J7y0Hiow6pIXhQ0ZpqKc2P6uchR5hRAT3VXaf0asoCXe%2FNHSMqjW5iT6xj600v9oEdNxwisSyN01yXKOin9XGt59mW59s%2FWVF1tEGWzW8a6A8IpY5cg0pn8%2FgGC4Ei9k3XjJLpBfEilQo79pVgmQzyCk5KibZdgVolgTf1VWU%2BFZQUF%2B87xJOO3cpL83G08sg0%2FO33pcBDEEkFlBS8WpqN6prUJXzVEmsioz951YhmsCJyQzRT0XlLYteQufIJ2J9VaX3eY0Cnh4bTzuJXLHBYzia0mnDPNVLB63R6SafRMgoaxFiwwktd4PS8kSdc5uRV4rnA3DDOu%2FLJacAKdJwi3ZjP%2FKAyzvJiodPVoTi3zCMTbXPijAmhdAXjKyVYSmo7zE172vUdTViLiZA7sTbzGnb3LtX3gw8Rekh3PbQg6Zr80Nt%2FpAoAvQrs6s7vO1CwXRmbopCEFZj6bFiIbwa6PAzh4Y%2F9C5bEnoQLxU3dzd4kTCK70ZpqAxM6Il3JHYQcAT59f1PvbnCzuL11HWFDebt6X62M%2FeLWRhR3lKWJPDdX0TniHYe0%2BCdoVHGu4mdUZSGFCNp3tuDRJCvmT2dZSSr7XxFdJSKdmE2vQaqosdwOgUOYfGqMmvrw1Rm7M%2Fqqt1DXKdshGDjAw2xs2S%2BqDjbp20gkstybUqJ7aPgYn%2BonV9Kv%2F3dawCUvnzWCdZhGk2YEaV1T5K3HCCjuokw%2BMv50QY6mAH%2Bo4ioWGEgrpHtVrsXDCIpEOCYLCSouXySVeMfW%2Ff9E7X42RwYmMdoZGrHghyoFS9o9SLXD4lVgalZQHkCp7IqIo29UBWol3QaXaNS3KiNd%2FO7%2B6P26jJ9JAuZr9WXKLFzHUYl9ONTrEmZqLEqZks7LnJN1JwEHn46IEoCfxX8Q1L1be%2BOqCIGXPGwm1MGTXQpSKRwU6JZhQ%3D%3D&Expires=1782477771)

**For adding new research to project sources going forward:** the cleanest pattern is a short decision-file update — add a section `# 11. Updated decisions from [date] research` to the Implementation Decision file with any new locked choices. One file stays the single source of truth instead of accumulating parallel research docs.

Prepared using Claude Sonnet 4.6 Thinking

I am quite— Surprised by the way that you formulated, uh. This research project, because now I only see that it's supposed to create the actual scripts but where we wanted to have is the integration map with options, right? So. From all the research, from the APECs, what are the best things? What. Process. Needs. Which plugin, what are the alternatives? Um. How is. It going to get executed? Uh, how is it token efficient? Uh. Why are we doing this? Uh, I don't see that at all in the momentary state of the prompt. Did you drift against so badly that this is against. A. Research prompt that would have not touched the actual target? Which is, again, in my own words, we need to harm. Everything that we have done so far into. An actual truth. Full. Truthful, um, system. For example, the web research was supposed to do that. So after understanding the APECs, uh, then understanding the research and how to integrate the retrieval engine and stuff like that, uh. The web search was supposed to do. Exactly that: validate the. Whole integration setup. There was defined, I. Don't even—there's like a very short paragraph for that only. And then the integration map, I don't—I don't even—I don't even see also an output for that. We should define The tree with the options and stuff like that, uh, this. Nothing of that is in that prompt at the mom

Now I have the full picture. The prompt drifted badly — it jumped to writing scripts instead of staying as a research prompt. The actual purpose is: **validate the whole architecture, produce the options decision tree, integration map, and truth-check everything against what is real**.

Here is my honest diagnosis first, then the corrected prompt.

---

## What the prompt should do (your intent)

text

`purpose:   - synthesize ALL research done so far into a single truthful validated architecture  - produce an options decision tree: WHY this approach, what alternatives exist, what was rejected and why  - validate the retrieval engine choice with web evidence (not assume it)  - produce an integration map: what touches what, how execution flows, token efficiency impact  - anchor everything to the live repo state (what exists, what is missing, what needs to be added)  - NOT write scripts  - NOT produce implementation code  - serve as the truth document before any Pro Thinking implementation step`

## What the broken prompt did instead

text

`drift:   - jumped directly to script contracts (C1, C2, C3)  - web search was a shallow afterthought (5 narrow validation queries)  - integration map was a simple file-change table, not an architecture decision tree  - no options were evaluated, no alternatives with scores  - no "why SQLite vs alternatives" section  - no execution flow diagram (how Claude actually uses this)  - no token efficiency analysis  - no "why are we doing this" framing  - contaminated with Pro Thinking handoff wrapper`

---

## Corrected Deep Research Prompt

text

`Research and produce one validated architecture truth document for the Apex KB retrieval integration. This is a RESEARCH and VALIDATION task, not an implementation task. Do not write scripts. Do not produce code. Do not produce file contents. --- ## 0. Anti-Contamination Guard Before reading any source: 1. Newest explicit operator decision wins over older research. 2. Any constraint or limitation not traceable to an explicit operator statement must be flagged UNVERIFIED_ORIGIN. 3. Phase 0 script is generic — not bound to any specific KB. Flag every instance of claude-skill-design used as a hardcoded script target. 4. Contaminated decisions are dead. Do not carry them into outputs. --- ## 1. Sources to Read ### 1A. Project Research Files (all uploaded) Read in this priority order. For each: note file, primary thesis, and any contamination. | File | What to extract | |---|---| | Claude_Apex KB_SQLiteFTS5BM25_CCv2.md | Most recent retrieval architecture decisions. FTS5 schema, query flow, health checks. SUPERSEDES older versions. | | Claude_Apex KB_SQLiteFTS5BM25_CC.md | Older — use only if CCv2 is silent on a point. | | Claude_Apex KB_SQLiteFTS5BM25_GPT.md | Cross-model validation. Score tables. Disagreements with CC. | | KB-Researchv3_gpt_FB_claude.md | Feedback corrections to scores. Which verdicts survived correction. | | KB-Researchv3_gpt.md | Architecture options rated. Full scoring model with all options. Token efficiency analysis. MCP analysis. Hosted vs local comparison. | | DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md | Final patch decisions D1–D12. Three-memory-domain architecture. Integration map. Query flow. | | Apex Phase 0 Corpus Intelligence Implementation Decision.md | Phase 0 purpose, problem it solves, what it produces. V1 vs V1.5 scope. | | Pre-LLM Tool Stack Installability and Value Audit.md | Tool installability on Windows. What is confirmed working. What is deferred. | | Markdown Structure Parser Spike for Apex KB Phase.md | Parser decisions. Python state machine vs markdown-it-py. | | Apex Link Graph and Process-Flow Representability Audit.md | Graph decisions. What is V1 vs V1.5. | | DR_APEX_PM_KB_PD_Gem.md | PM/KB/PD process options. 15 reference implementations. | All remaining project files: scan for first-person operator statements from Marco. Extract any that affect retrieval architecture, execution model, token efficiency requirements, or forbidden behaviors. --- ### 1B. GitHub Repo — leela-spec/apexai-os-meta (main branch) Read in this order. Record path, read status, and 2–3 key current facts per file. Priority 1:`

.claude/skills/apex-kb/SKILL.md  
.claude/skills/apex-kb/package-manifest.md  
.claude/skills/apex-kb/references/kb-contract.md  
.claude/skills/apex-kb/references/script-command-contract.md  
.claude/skills/apex-kb/references/ingest-query-lint-audit-rules.md

text

`Priority 2:`

apex-meta/scripts/  
apex-meta/kb/  
.gitignore

text

`Priority 3 (orientation only, not targets):`

.claude/skills/plan/SKILL.md  
.claude/skills/synch/SKILL.md  
.claude/skills/session/SKILL.md

text

`For each unreadable file: label REPO_UNVERIFIED. Hard abort only if GitHub connector fails entirely. --- ### 1C. Web Validation Validate the following claims. These are the decisions that depend on external facts — verify them, do not assume them. | Claim to validate | Search question | |---|---| | SQLite FTS5/BM25 is available in Python 3.12/3.13 stdlib on Windows (from python.org) | Does python.org Windows installer bundle FTS5? Is it conditional on build flags? | | ripgrep is the best keyword search CLI for Windows | Current rg Windows install via winget. Any alternatives? | | markdown-it-py is the best optional parser dependency | Current version, install, Python 3.9+ compatibility, alternatives | | python-frontmatter is the best YAML parser for .md files | Current version, install, alternatives | | Qdrant local requires Docker or server process | Confirm current Qdrant local install requirements | | Chroma persistent client behavior | Confirm current Chroma persistence model (in-memory vs disk) | | LanceDB vs Chroma for file-native embedded use | Current LanceDB install requirements, no-server claim | | MCP overhead for frequent small lookups | Any benchmarks or documentation on MCP latency per tool call | For each: record verdict (confirmed / corrected / inconclusive) and impact on architecture decisions. --- ## 2. Contamination Audit After reading all sources, produce this table. Maximum 15 rows. | # | Contaminated text | Source | Type | Correct version | |---|---|---|---|---| Types: hardcoded_kb_path / invented_guardrail / version_drift / wrong_scope / unverified_score --- ## 3. Output A — Architecture Truth Document ### A1. Why we are doing this (3–5 sentences) What problem does adding a retrieval layer to Apex KB solve? What breaks without it as the corpus grows? How does token efficiency connect to this? What is the operator's specific use pattern that makes this necessary? ### A2. What exists today Based on live repo reads. What apex-kb skill currently does. What scripts exist. What artifacts are already present. What is completely missing. ### A3. Retrieval engine decision Reproduce or reconstruct the full scored options table from KB-Researchv3_gpt.md with corrections applied from KB-Researchv3_gpt_FB_claude.md. Then: - State the validated winner with score - State the #2 and #3 options with scores - State what V2 escalation looks like and when to trigger it - State what hosted escalation looks like and when to trigger it - Map each option to: local-only / requires-server / requires-cloud ### A4. Web validation verdicts | Claim | Verdict | Impact on architecture | |---|---|---| ### A5. Three-memory-domain architecture From DR_Apex KB QueryRetrieval Integration_Final Patch Pack: - Project KB domain - Personal orchestration domain - Cross-project parent memory domain For each: what it stores, where it lives in the repo, how it is indexed, how it is queried differently. ### A6. How Claude actually uses retrieval (execution flow) Step-by-step: what happens from the moment an operator asks a question until Claude returns an answer with source pointers. Show the token-cost difference with and without the retrieval layer. Use the concrete example from the research files. ### A7. MCP role and boundary When MCP is efficient. When it is not. What it should and should not own in this architecture. Final verdict from research. ### A8. Open questions and risks Maximum 8 items. Only genuine unresolved gaps or confirmed risks from the research. Not design options. --- ## 4. Output B — Integration Map ### B1. Architecture layers Produce a text diagram of the full stack from raw source to Claude answer. Show each layer, what it owns, and what calls what. ### B2. Skill and script boundaries | Component | Owns | Does not own | How it connects to retrieval | |---|---|---|---| Fill in for: apex-kb, apex-plan, apex-sync, apex-session, apex-search (if applicable), Phase 0 script, retrieval script. ### B3. File change map | Path | Status today | Required change | Priority | Risk | |---|---|---|---|---| Status values: exists-confirmed / exists-unverified / missing-confirmed / missing-unverified ### B4. Execution dependency order What must exist before what. Numbered sequence from current state to working retrieval. --- ## 5. Output C — Decision Tree for Pro Thinking A structured reference that Pro Thinking will use. No prose. ```yaml architecture_decision_tree:   v1_retrieval_engine:    winner: SQLite FTS5/BM25    score: [from corrected table]    rejected:      - option: plain Python index        reason: [from research]        when_to_reconsider: [from research]      - option: local vector DB (Qdrant/Chroma/LanceDB)        reason: [from research]        when_to_escalate: [from research]      - option: hosted file search        reason: [from research]        when_to_escalate: [from research]      - option: MCP memory server        reason: [from research]        when_to_use_instead: [from research]    fts5_availability:      status: [from web validation]      fallback_if_unavailable: [from research]   memory_domains:    project_kb:      path: [from repo read or REPO_UNVERIFIED]      index_path: [from research]    personal_orchestration:      path: [from repo read or REPO_UNVERIFIED]      index_path: [from research]    cross_project:      path: [from repo read or REPO_UNVERIFIED]      index_path: [from research]   phase0_corpus_intelligence:    purpose: [from Implementation Decision file]    v1_outputs: [list from Implementation Decision Sections 4.1–4.8]    v1_5_additions: [from Implementation Decision]    feeds_into: [what consumes phase0 outputs]   skill_boundaries:    apex_kb_owns: [from research + repo]    apex_kb_does_not_own: [from research + repo]    new_scripts_needed: [list]    new_skill_needed: [yes/no and why]   token_efficiency:    without_retrieval: [step count and token cost from research]    with_retrieval: [step count and token cost from research]    net_saving: [from research] ``` --- ## 6. Degradation Rules | Failure | Response | |---|---| | Project file missing | Continue. Note in source table. | | Repo file unreadable | Label REPO_UNVERIFIED in B3 and C outputs. Continue. | | Repo connector fails entirely | Complete project files and web. Mark all repo fields REPO_UNVERIFIED. Produce full outputs. | | Web validation inconclusive | Mark inconclusive. Note architecture impact. Do not remove the decision. | | FTS5 not confirmed available on Windows | Flag in A4. Add fallback path in C output. | | Hard abort | Only if no project files are readable AND no web AND no GitHub. |`

---

That is the corrected prompt. Key differences from what I had before:

- **A1 now explains why** — token efficiency, corpus growth, operator use pattern
    
- **A3 reproduces the full scored options table** with all alternatives
    
- **A4 is real web validation** with 8 specific claims to verify, not 5 narrow tool queries
    
- **A5 covers the three-memory-domain architecture** that was completely missing
    
- **A6 shows the actual execution flow** with token-cost comparison
    
- **A7 handles MCP explicitly** — when to use it and when not to
    
- **B1 has an architecture layer diagram** not just a file-change table
    
- **C is a YAML decision tree** for Pro Thinking — no code, no scripts, no Pro Thinking wrapper inside
    

Prepared using Claude Sonnet 4.6

create a handover for another chat to create the deep research prompt. because i dont trust you anymore as you drifted again: you were ot suppsoed to drop completly the file creation: Be. Very detailed on the actual script contracts and give but. Don't mention the Pro Thinking prompt, just give an in a really nice guidance. Uh. At best. Write scripts if possible, but this is not necessarily you know, what we need from the deep research prompt is what. Needs to change, what needs to get patched, what new files need to get created, and what are their specific contents on a macro, meso, and micro level. Whereas. The macro is a general interconnection and purpose, meso are the actual files and contents, and micro would be the actual um. Snippets and guardrails and you know. Basically already the code. Which is— Something that the other steps are going to do, but um. Which. Should. Already like maybe be at least a little bit think thought of on how this needs to be get written. So in other words, the. Macro and meso layer should be very, very definite, and the micro layer should get guidance. Um, sadly I don't trust you anymore with that task. We need to do a handover for another chat that will use your Claude. Sonnet extended thinking mode. To redo the. Uh. Prompt.

Answer skipped

Prepared using Claude Sonnet 4.6

create a handover for another chat to create the deep research prompt. because i dont trust you anymore as you drifted again: you were ot suppsoed to drop completly the file creation: Be. Very detailed on the actual script contracts and give but. Don't mention the Pro Thinking prompt, just give an in a really nice guidance. Uh. At best. Write scripts if possible, but this is not necessarily you know, what we need from the deep research prompt is what. Needs to change, what needs to get patched, what new files need to get created, and what are their specific contents on a macro, meso, and micro level. Whereas. The macro is a general interconnection and purpose, meso are the actual files and contents, and micro would be the actual um. Snippets and guardrails and you know. Basically already the code. Which is— Something that the other steps are going to do, but um. Which. Should. Already like maybe be at least a little bit think thought of on how this needs to be get written. So in other words, the. Macro and meso layer should be very, very definite, and the micro layer should get guidance. Um, sadly I don't trust you anymore with that task. We need to do a handover for another chat that will use your Claude. Sonnet extended thinking mode. To redo the. Uh. Prompt.

3 attachments

I have read all three failed prompts. I can now see exactly what they got right, what they repeatedly dropped, and what the next chat needs. Here is the full handover.

---

# Handover: Deep Research Prompt for Apex KB Phase 0 Integration

## 1. What this task is

You are being asked to write **one deep research prompt** that another Claude instance (Claude Sonnet with extended thinking) will execute. That prompt must instruct it to:

1. Read all project files, the live GitHub repo, and run targeted web validation
    
2. Produce a **contamination audit**
    
3. Produce **Output A** — Research Summary (what exists, what is decided, what is open)
    
4. Produce **Output B** — Integration Map (exact files to create, patch, and their full contents at macro/meso/micro level)
    
5. Produce **Output C** — Code-Ready Spec (YAML decision tree + script guidance)
    

**Output B is the most critical.** Every previous attempt either dropped it entirely or reduced it to a skeleton table. The next prompt must not do this.

---

## 2. What "macro / meso / micro" means — operator's exact definition

|Level|What it means|What must be produced|
|---|---|---|
|**Macro**|General interconnection and purpose — why this file exists, what it connects to, what breaks without it|Must be definite and complete|
|**Meso**|Actual files and their full contents — what each section is, what fields it has, what the structure looks like|Must be definite and complete|
|**Micro**|Actual snippets, guardrails, code patterns — the exact shape of the code, the edge cases, the validation logic|Must provide **guidance** — not necessarily final code, but enough that the implementation step can execute without re-researching|

**The macro and meso layers must be fully specified.** The micro layer provides guidance (not necessarily a complete runnable script, but enough to eliminate ambiguity).

---

## 3. What all three previous prompts got wrong

Every previous attempt failed in the same ways. The next prompt must not repeat these:

- **Dropped Output B contents** — B1/B2 tables were skeletons with `[exact heading from repo read]` placeholders that were never filled in. The prompt must instruct the model to actually fill these from repo reads, not leave them as templates.
    
- **Dropped file contents at meso level** — no file had its actual section structure defined. The prompt must require that for every new file created, the full internal structure (headings, fields, contract language) is produced.
    
- **Dropped micro guidance** — Output C became a YAML block with empty fields. It must contain actual code patterns, argument signatures, error handling guidance, and validation logic shapes.
    
- **Web search was too narrow** — only 5 tool-version queries. The prompt needs 8–10 validation queries covering FTS5 availability, parser alternatives, MCP overhead, vector DB alternatives.
    
- **Contamination audit was cosmetic** — the table existed but was never actually filled with real contamination from the files. The prompt must require it to be filled from real source reads.
    
- **Integration map had no architecture layer diagram** — just a file table. Must include a text diagram showing layers → what owns what → what calls what.
    

---

## 4. Context the next chat needs to understand

## 4.1 The project

**Apex** is a Claude Code-native personal orchestration system. It lives in the repo `leela-spec/apexai-os-meta`. It manages projects, daily/weekly flows, KB management, session recaps, and AI routing. The operator is Marco, running on Windows.

**apex-kb** is the skill that manages knowledge bases — ingestion, wiki compilation, manifests, query, lint, audit. It has a Python script (`apexkb.py`) and a skill package under `.claude/skills/apex-kb/`.

**Phase 0 Corpus Intelligence** is a new generic Python script (`phase0_corpus_intelligence.py`) that runs **before** any LLM work on a KB. It does deterministic analysis of the raw corpus — producing a corpus profile, heading map, link map, frontmatter map, keyword hits, priority candidates, and a navigation report. Its outputs are consumed by Claude as grounding context before it starts compiling wiki pages.

## 4.2 The retrieval layer

Research concluded that **SQLite FTS5/BM25** is the correct v1 retrieval engine. The architecture has three memory domains: project KB, personal orchestration, cross-project. The compiled wiki pages (not raw sources) are the primary retrieval surface. A script (`apexkbretrieval.py`) needs to be created.

## 4.3 The three-file architecture for new additions

Every new capability added to apex-kb requires three things:

1. A **script** in `apex-meta/scripts/`
    
2. A **contract reference file** in `.claude/skills/apex-kb/references/`
    
3. **Patches** to: `SKILL.md` (commands), `package-manifest.md` (registration), `script-command-contract.md` (CLI surface)
    

## 4.4 Known contamination to guard against

- `claude-skill-design` hardcoded as a script target — it is only the first test KB, the script must be generic with `--kb-root` as a parameter
    
- Invented guardrails without operator source — must be flagged UNVERIFIED_ORIGIN and excluded
    
- Version drift — `CCv2.md` supersedes `CC.md` which supersedes `GPT.md` for FTS5 decisions
    
- Wrong scope — Phase 0 is deterministic Python only, no LLM, no network
    

---

## 5. The prompt the next chat must write

The next chat must produce a single deep research prompt with this exact structure. Copy this as the brief:

---

## Brief for next chat

**Your task:** Write one deep research prompt to be executed by Claude Sonnet (extended thinking). The prompt will instruct that Claude instance to read source files, the GitHub repo, and the web — and produce three outputs.

**Non-negotiable requirements for the prompt you write:**

**On Output A (Research Summary):**

- Must extract what apex-kb currently does from live repo reads (not from research files)
    
- Must extract locked decisions D1–D8 from the Phase 0 Implementation Decision file
    
- Must flag every contamination instance with type: `hardcoded_kb_path` / `invented_guardrail` / `version_drift` / `wrong_scope`
    
- Must produce a tool validation table with FTS5 availability confirmed or denied per Python version/platform
    

**On Output B (Integration Map) — this is the main output:**

B must be complete at all three levels:

- **Macro level** (definite): For every file that needs to be created or patched — what it is for, what breaks without it, what it connects to in the system
    
- **Meso level** (definite): For every new file — its full internal structure: section headings, field names, contract language, what each section must contain. For every patched file — the exact section where the patch goes (from live repo read) and the full text of what is being added
    
- **Micro level** (guidance): For the two new scripts — argument signatures, key function shapes, error handling patterns, validation gates, CLI output contract. Not complete runnable code, but enough that an implementation step has zero ambiguity about what to write
    

B must contain:

1. An architecture layer diagram (text, showing: raw sources → manifests → compiled wiki → SQLite index → query script → Claude)
    
2. File creation table (path, action, macro purpose, meso structure, micro guidance column)
    
3. File patch table (path, exact heading anchor from live repo, full patch content, verified from repo: yes/REPO_UNVERIFIED)
    
4. Execution dependency order (numbered — what must exist before what)
    
5. PowerShell setup steps for Windows
    

**On Output C (Code-Ready Spec):**

- Must be a YAML decision tree with all fields populated from research (not left as `[from research]` placeholders)
    
- Must include token efficiency analysis: step count and approximate token cost with vs. without the retrieval layer
    
- Must include the three-memory-domain architecture with concrete paths
    
- Must include micro guidance for both scripts: argument signatures, subcommand list, key validation logic
    

**On web validation:**  
Use these 8 specific queries — not fewer:

1. Python 3.12/3.13 Windows sqlite3 FTS5 availability from python.org installer
    
2. ripgrep winget install Windows 2025
    
3. markdown-it-py current PyPI version Python 3.9 compatibility
    
4. python-frontmatter current PyPI version
    
5. Chroma persistent client disk behavior current version
    
6. LanceDB embedded no-server install requirements
    
7. MCP tool call latency overhead benchmarks 2025
    
8. SQLite FTS5 porter tokenizer unicode61 Windows behavior
    

**Contamination guard — embed this verbatim in the prompt:**

text

`Before reading any source: 1. Newest explicit decision wins. CCv2.md > CC.md > GPT.md for FTS5 decisions. 2. Operator statement overrides AI output. Any constraint not traceable to Marco must be flagged UNVERIFIED_ORIGIN. 3. Phase 0 script is generic. Any hardcoded KB name (claude-skill-design, etc.) is contamination. --kb-root is a parameter. 4. Contaminated decisions are dead. Do not carry them into B or C.`

**Degradation rules — embed these:**

text

`- Project file missing: note it, continue - Repo file unreadable: label REPO_UNVERIFIED in B and C, continue - Repo connector fails entirely: complete all project file and web work, mark all repo fields REPO_UNVERIFIED - Web query inconclusive: mark inconclusive, note impact on architecture, do not remove the decision - Hard abort only if: no project files AND no web AND no GitHub`

**What the prompt must NOT do:**

- Do not write a Pro Thinking wrapper or handoff format around the outputs
    
- Do not produce complete runnable scripts (guidance is sufficient at micro level)
    
- Do not re-invent the architecture — the research has already decided it
    
- Do not leave Output B as a skeleton with placeholder text
    
- Do not limit web search to 5 queries
    

---

## 6. Source files the next chat needs

Upload all of these to the new chat:

|File|Priority|Why|
|---|---|---|
|`Apex Phase 0 Corpus Intelligence Implementation Decision.md`|P1|Primary decision source — D1–D8|
|`DR_Apex KB QueryRetrieval Integration_Final Patch Pack.md`|P1|Integration patches and three-memory-domain architecture|
|`Claude_Apex KB_SQLiteFTS5BM25_CCv2.md`|P1|Most recent FTS5 schema decisions|
|`Pre-LLM Tool Stack Installability and Value Audit.md`|P1|Windows tool availability|
|`Markdown Structure Parser Spike for Apex KB Phase.md`|P1|Parser decisions|
|`KB-Researchv3_gpt_FB_claude.md`|P2|Score corrections and validated verdicts|
|`Claude_Apex KB_SQLiteFTS5BM25_CC.md`|P2|Older FTS5 version (fallback only)|
|`Apex Link Graph and Process-Flow Representability Audit.md`|P2|V1/V1.5 graph scope|
|`KB-Researchv3_gpt.md`|P3|Options scoring model|
|`markdown-parser-spike-report.md`|P3|Parser spike results|

GitHub repo: `leela-spec/apexai-os-meta` — connect with GitHub connector, read main branch.

---

## 7. What success looks like

The output of the deep research prompt execution must be usable as a **complete build brief** — someone reading Output B should be able to open every target file listed and know exactly what to write, where to put it, and in what order. The micro guidance in Output C must eliminate any need to re-research during implementation.

If B is still a skeleton table with placeholder headings → the prompt failed. If C still has `[from research]` empty fields → the prompt failed.