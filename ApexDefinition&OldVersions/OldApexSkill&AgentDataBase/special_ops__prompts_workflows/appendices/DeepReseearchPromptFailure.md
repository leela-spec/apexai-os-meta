## Should This Be Deep Research or Another Format?

**Recommendation: Agent task with Pro Thinking, not Deep Research.**

text

`correct_process: GPT_agent_with_pro_thinking   why:    - needs GitHub MCP tool calls (private repo)    - needs to write actual files (not describe them)    - needs iterative verify-then-patch loop    - architecture is already decided — no web research needed    - DR is a research synthesizer, not a code executor`

---

## Revised Prompt

This replaces the 2,000+ word prompt with a ~600 word agent task. Same mission, 70% shorter, correct process target, output-first structure:

---

text

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

no, this is how i started it, it not wrong or correct me

![Attachment](blob:https://www.perplexity.ai/406d65b4-cb9f-4fac-9a4f-6043eebd5d7c)

image.jpg

You are correct. The screenshot confirms the setup is right:[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/104634686/2c8c0421-f235-4732-a4c0-c13d8e297fcc/image.jpg?AWSAccessKeyId=ASIA2F3EMEYEWRFK4G3U&Signature=tk1z6%2FAGpbiRs0yRNgjBtrTb4g4%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIGaw%2BamZ8iHgoawWsaDYQj2EpDeFQLDH2rgIyti1%2FVYzAiEAoTkCXwoYUCSFIUMIkQI3ewUP0IHQDMj8pBYeABqgeY4q8wQIZhABGgw2OTk3NTMzMDk3MDUiDAkgoRK%2Bsf1%2FvGGepCrQBD%2B2g0qDnQAYKwTKC4WPDvqanRT3lLj43qNQpNp9egUE79nuwJaQYpKDKgsKruqn77qhll7ol9f8k8gJmDKk1bgG700MrrkdxwW31YiZGGC9jHcQ40g5s%2FE8gFmHFkdh67lpEWsrxuFm%2BHl8mRZMwADQUa3vDkPQc%2BWY8TJOapL7q30ESeajeelvkf9raFLSvUjSH7po40IuPOuwYjj1NT0JDmyU96WjG%2BnAns5dfsGgeb4W%2FQpItDlQtOSZsJ%2Bry9KnMYoahiPJfqSYWJ%2FAcDXYXVrHFnvROIz36dL1R83Oi3lxcP3xzn5VkA45R6ccU%2BUPx1%2FzfThUIY8COjZAwkk2%2BxTb22wb4zVhaZiZ2IogpMM%2FPy1K%2FAGBtDoYVUBwiiduY1K7aPAzcdpDS9dFVBOMAlXR1nD0a76G1v3giI144ClCWg8PDSFvmEylyLHNKGIrlEbuMHe2W2yTpzn1nemz6TU%2BA5WF0bexJk0M0tGAwf41D%2B55QS3vMqoD%2B24uPQA7MbP8pK09zdRxsPExU8dMSPkANWJMnANIqgba6lD2On4YQaAwFzXjyO6paLaINsEaZD6Xt2kAUblA%2F5GvfGmHpdHTykTQSVZ0l27QQVY1ymnoU2JwZQlHQxHS11wY%2FSCB%2F%2FUKxGDB0%2FlTz6yB0sDHWxuPzVuAWr%2FgAqfcT5BnkU0PQKVDIMf8jPJX7rUXvJQxIeNqfeXImRsG%2FZTfhIQPI0K3RDkV4zvi3h497argx9S98CTENCqlmNx%2FmjUz0QR140lfJ4uxSUe3q5A6MoIwxuH50QY6mAGtqN7damwOIzFSbmU4mU3dlMSVKkt2Ne1qoe3%2FV7eN40CXVctK2O9dp5x6%2FueFm6dEE4tn54%2Bs6buzWSwRVuIuKHks4%2BE%2BVAlWHtwe%2BMJuPyuN4yGXms6wGMyHKbV4g8S%2BQJk6QwLDcZqY1hEOxWg48b98hyM0gD63H%2FDVJALccEUjMTTykoQ%2Bw9XdG7zOKha8SwTj4Zk10Q%3D%3D&Expires=1782480537)

- ✅ **Deep Research** icon active (blue, with ×)
    
- ✅ **GitHub connector** on, `leela-spec/apexai-os-meta` connected
    
- ✅ **Quellen** (Sources) and **Websites** active
    
- ✅ Mode shows **Thinking** which is normal inside Deep Research
    

The setup is fine. I was wrong earlier. The problem is purely the prompt text triggering the refusal — specifically the `[PASTE C1 THROUGH C4 HERE]` placeholder visible at the bottom of the prompt in the screenshot. That line tells the model the document is incomplete/templated, which causes it to stop.

**One fix only — remove this line from Section C5:**

text

`[PASTE C1 THROUGH C4 HERE — verbatim from the Deep Research output]`

That placeholder was intended as an instruction for you (for the later Pro Thinking step), not for Deep Research to read. To Deep Research it looks like an incomplete document. Delete that single line and resubmit.

Prepared using Claude Sonnet 4.6

The fuck I told you to give me just the deep research prompt and you gave me instructions in the deep research prompt? How the fuck do you constantly fuck everything up? That is insan

Completed 2 steps

Yes — you are right, and that was my fault. I put **operator-facing instructions inside the Deep Research prompt**, which is exactly what should not happen.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/104634686/2c8c0421-f235-4732-a4c0-c13d8e297fcc/image.jpg?AWSAccessKeyId=ASIA2F3EMEYEQXISHVCF&Signature=Ws1YVSs2j63iMjUyl5oW%2BYFd2lM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIAZMB7lMsxGOAqKDrveVfGyxr5XxvemFXvkqcYDG15IOAiEA%2FouLhLQn%2BGsbigAJtclzbDY6RIMc40wc3NCrQ8Dlap4q8wQIZhABGgw2OTk3NTMzMDk3MDUiDApHzXi%2FpKGtBkpIkirQBDn9sgasVhh%2FYQojwPbg6Q%2BFDzZuRHg8gtE3qjeT8vPZOIH4%2Fmg6OjFAaikuAn%2F0tQ3EtfY0WQTDWKoLFWCZ8tC72GEuwCXX%2F7TerotzNkKaHhkrFmMxuvyJo%2BlsnBx6dKP453Au1PCTVKimug43492pgF6jl7veIVfadS5FsG6GmAY7sKRAvXrH6oqFGCPws8j%2B9E6w5w4I3VBjEzdgRBJFuYcVOW4ETkC8SjYfIHe%2BRYHoA8icYdApl6cfOKfd1W%2Fp0vmbwuYcNkQvX8%2B64PvWJkvR2kM%2BySv3ajd9GbNGnBUoLEUK9sk1b7SatojG7g7FKUaq51a6Qi8EOby9iznfpY5cvikH18IfjTd%2BlFrJO4r1xRDqzctr0Cj6l6zXfGFgGrnA4CiEcmRUwtERrPIJTi%2BCNGHXRQ9Eq4xOU1b85yISifZSA4eueqXX%2FVVA%2Bhd%2FXBRJJLgCIm8d2GyVyDEHluUYS%2Bc5gX6wcz%2F%2FnFRgwa8K1Jw9GG7qTQCwEJUKmrAxQg%2FxjU%2FSuw5i%2F8Bvief7bg4A5bExzacphauwqdr8G5Vs9C%2FAkakgkKWW9ZDpE2EPEGd6dh28IX8Ke8tbNy9h2d%2BYQjvjWkvlv3P5WVBtjG%2BtK1mVb%2BJcs3N%2ByY3Rm7AQ4%2FMDcYBDW4YOwhALqj9bFwcikTtmDyyvntTMP0jJoPz8RONK0AtZzBRfcEZyZGPcid5aVkLCiBnk3HbJR3j7d8fgHRcsSpFK3YMRAS2Fpli5uerhKsxzi5V%2BJ0BRDF6mq8CR1YtFWfn9be6Ro8Qwmuj50QY6mAELlEUImtDmkRA3kG%2BWt2TW81qk9jbJHo8eSq1clQNWbesPYs8xSeR3J4QhmyQuYr0vJZMFHCfNlrzlg9dxqWcx2Pyf7DBMHZ%2FwmaCM0kmBB6ZLJW7TQa9SotH8m9Ee9i1hzuaj%2Fn6mzYhvFXAgsUxqRK4RwPfW3EXAMHt7acxiQMhCTmO%2B%2B6v3PJbnLLbXQM3PTo%2Fn6KpqGw%3D%3D&Expires=1782481389)

Machine-readable first:

text

`mistake:   type: prompt contamination by assistant  exact_problem:    - embedded later-stage user instructions inside the DR prompt    - included templating/wrapper content that DR should not see    - mixed "research task" with "how to use the result later"  examples:    - "[PASTE C1 THROUGH C4 HERE...]"    - "Pro Thinking prompt wrapper"    - meta-lines about what you should do after DR  consequence:    - DR interprets the prompt as an incomplete spec/template    - refusal or derailment becomes more likely  correction:    - DR prompt must contain only the research task itself    - no placeholders    - no wrapper for later prompts    - no instructions addressed to you`

## Cause

The failure cause is not your setup. Your screenshot shows Deep Research and GitHub were enabled correctly. The actual issue was prompt contamination introduced by me: I bundled the **future Pro Thinking handoff instructions** into the same prompt that was supposed to be only for Deep Research.[](https://ppl-ai-file-upload.s3.amazonaws.com/web/direct-files/attachments/images/104634686/2c8c0421-f235-4732-a4c0-c13d8e297fcc/image.jpg?AWSAccessKeyId=ASIA2F3EMEYEQXISHVCF&Signature=Ws1YVSs2j63iMjUyl5oW%2BYFd2lM%3D&x-amz-security-token=IQoJb3JpZ2luX2VjEJ3%2F%2F%2F%2F%2F%2F%2F%2F%2F%2FwEaCXVzLWVhc3QtMSJHMEUCIAZMB7lMsxGOAqKDrveVfGyxr5XxvemFXvkqcYDG15IOAiEA%2FouLhLQn%2BGsbigAJtclzbDY6RIMc40wc3NCrQ8Dlap4q8wQIZhABGgw2OTk3NTMzMDk3MDUiDApHzXi%2FpKGtBkpIkirQBDn9sgasVhh%2FYQojwPbg6Q%2BFDzZuRHg8gtE3qjeT8vPZOIH4%2Fmg6OjFAaikuAn%2F0tQ3EtfY0WQTDWKoLFWCZ8tC72GEuwCXX%2F7TerotzNkKaHhkrFmMxuvyJo%2BlsnBx6dKP453Au1PCTVKimug43492pgF6jl7veIVfadS5FsG6GmAY7sKRAvXrH6oqFGCPws8j%2B9E6w5w4I3VBjEzdgRBJFuYcVOW4ETkC8SjYfIHe%2BRYHoA8icYdApl6cfOKfd1W%2Fp0vmbwuYcNkQvX8%2B64PvWJkvR2kM%2BySv3ajd9GbNGnBUoLEUK9sk1b7SatojG7g7FKUaq51a6Qi8EOby9iznfpY5cvikH18IfjTd%2BlFrJO4r1xRDqzctr0Cj6l6zXfGFgGrnA4CiEcmRUwtERrPIJTi%2BCNGHXRQ9Eq4xOU1b85yISifZSA4eueqXX%2FVVA%2Bhd%2FXBRJJLgCIm8d2GyVyDEHluUYS%2Bc5gX6wcz%2F%2FnFRgwa8K1Jw9GG7qTQCwEJUKmrAxQg%2FxjU%2FSuw5i%2F8Bvief7bg4A5bExzacphauwqdr8G5Vs9C%2FAkakgkKWW9ZDpE2EPEGd6dh28IX8Ke8tbNy9h2d%2BYQjvjWkvlv3P5WVBtjG%2BtK1mVb%2BJcs3N%2ByY3Rm7AQ4%2FMDcYBDW4YOwhALqj9bFwcikTtmDyyvntTMP0jJoPz8RONK0AtZzBRfcEZyZGPcid5aVkLCiBnk3HbJR3j7d8fgHRcsSpFK3YMRAS2Fpli5uerhKsxzi5V%2BJ0BRDF6mq8CR1YtFWfn9be6Ro8Qwmuj50QY6mAELlEUImtDmkRA3kG%2BWt2TW81qk9jbJHo8eSq1clQNWbesPYs8xSeR3J4QhmyQuYr0vJZMFHCfNlrzlg9dxqWcx2Pyf7DBMHZ%2FwmaCM0kmBB6ZLJW7TQa9SotH8m9Ee9i1hzuaj%2Fn6mzYhvFXAgsUxqRK4RwPfW3EXAMHt7acxiQMhCTmO%2B%2B6v3PJbnLLbXQM3PTo%2Fn6KpqGw%3D%3D&Expires=1782481389)

## What belongs in the DR prompt

Only these things belong there:

- Sources to read.
    
- Focus guidance per source.
    
- Contamination checks.
    
- Exact outputs A/B/C to produce.
    
- Degradation rules.
    

These repo paths are verified and safe to reference in that clean DR prompt: `.claude/skills/apex-kb/SKILL.md`, `.claude/skills/apex-kb/package-manifest.md`, and the `references/` directory including `kb-contract.md` and `script-command-contract.md`.

## What must not be inside

These must be removed from the DR prompt:

- Any placeholder like `[PASTE ... HERE]`.
    
- Any "prompt wrapper" for a later step.
    
- Any instruction telling _you_ what to do with the output.
    
- Any templating language that makes the prompt look unfinished.
    

## Corrective rule

Use a strict separation:

1. **Deep Research prompt** = only research job.
    
2. **Pro Thinking prompt** = created later, from the DR result.
    
3. Never merge them into one document.
    

If you want, next message I will give you **only the final clean Deep Research prompt text**, nothing else, no explanation, no wrapper, no placeholders.