---
title: "Browser-Driven Subscription-AI Orchestration — OKF Reference"
okf_schema: "apex.okf.browser-ai-orchestration.v1"
doc_type: operational_reference
created: 2026-08-10
source: "Desk synthesis from live Claude-in-Chrome orchestration of ChatGPT, Perplexity, and Gemini across the local-orchestration-engine research program (2026-08-08 through 2026-08-10)."
status: "operator-session desk synthesis; empirically observed this session; not promoted through any formal KB governance path; supersedes nothing, cross-references existing MK-KB-010/011 rather than duplicating them"
scope: "How to reliably drive subscription/cloud chat-AI web UIs (ChatGPT, Perplexity, Gemini) via Chrome browser automation to execute research/work prompts and retrieve complete, correct output. Not about local-model orchestration, which is a separate concern documented under local-orchestration-engine."
read_when: "Before any session that will drive ChatGPT, Perplexity, or Gemini through Claude-in-Chrome to execute a prompt. Read only the entry index below plus the platform section(s) you need — do not read the whole file if only one platform is in play."
---

# Browser-Driven Subscription-AI Orchestration — OKF Reference

## How to use this file

Read the index, jump to the entries tagged for your platform, skip the rest. Each entry is one screen. Full incident evidence (chat URLs, exact character counts, timestamps) lives in the research-results files cited under `evidence`, not duplicated here — this file is the reusable rule, not the case file.

## Open verification items (time-stamped operational state, not evergreen rule)

- **VERIFY-001** — Operator reports (2026-08-10) that GitHub repository connectors are now installed for both Perplexity and Gemini accounts, matching the native GitHub connector already confirmed working for ChatGPT. **Not yet empirically tested from this environment.** Test both at the start of the next browser-orchestration session, before defaulting to the chunked-message technique (BAO-003) for Perplexity or a manual single-submission paste for Gemini. If confirmed working, this removes the character-budget constraint that motivated BAO-003 and lets all three agents read prompt/authority files directly by path, matching ChatGPT's existing workflow (MK-KB-010). If a connector exists but cannot actually read this specific private repo, or reads a stale ref, that is itself worth recording as a new entry, not silently worked around.

## Index

| ID | Platform | One-line summary |
|---|---|---|
| BAO-001 | ChatGPT | Composer sends on bare Enter — never type a prompt containing literal newlines |
| BAO-002 | ChatGPT | Verify the full prompt landed in the composer before clicking Send |
| BAO-003 | Perplexity | No connector (until VERIFY-001 resolves) → use ack-only chunked multi-message submission |
| BAO-004 | Perplexity | Composer is contenteditable, not a textarea — insertText, then re-check length in a separate call |
| BAO-005 | Perplexity | Check the search-mode toggle (Suche vs. Vertiefte Recherche) before a chunked submission |
| BAO-006 | Gemini | Deep Research needs one full-prompt submission, not chunking |
| BAO-007 | Gemini | Deep Research requires an explicit "Start research" click after the plan; then runs async and is resumable |
| BAO-008 | All | A CDP `dispatchKeyEvent` timeout is frequently a false alarm — verify state before retrying |
| BAO-009 | All | Long responses can read as truncated immediately after generation stops — reload before concluding real truncation (→ MK-KB-011) |
| BAO-010 | All | Prefer a native repo connector over an agent's own raw-URL browsing tool (→ MK-KB-010) |
| BAO-011 | All | Stray/unexpected browser tabs during multi-tab sessions are usually noise — verify the real task tab, don't chase every one |
| BAO-012 | All | Cross-agent self-reported confidence scores are not on a shared scale — don't average or directly rank them |
| BAO-013 | All | A self-inflicted "file not found" from a connector is often correct and honest, not a connector failure — check whether the file was actually pushed |

## Entries

### BAO-001 — ChatGPT composer sends on bare Enter

- **Platform**: chatgpt
- **Symptom**: A prompt typed with literal `\n\n1. ...\n\n2. ...` line breaks gets submitted early, mid-first-paragraph, before the rest of the text is entered.
- **Rule**: Never type a multi-part prompt into ChatGPT's composer using literal newlines. Write it as one flowing paragraph; replace numbered/line-broken lists with inline `(1) ... (2) ... (3) ...` numbering.
- **Why**: ChatGPT's composer treats a bare Enter keypress as the send action, not a newline insert, regardless of how the text was typed (paste or keystroke simulation).
- **Evidence**: `apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-G-RANKING-UPDATE-2026-08-09-CHATGPT-RESULT.md`, `uncontrolled_variables`, first bullet.

### BAO-002 — Verify the full prompt actually landed before sending

- **Platform**: chatgpt (observed here; treat as universal caution)
- **Symptom**: A composer that should contain a long retyped prompt instead shows only a stray fragment (e.g. a lone dash sequence) — typing appeared to succeed but the visible state doesn't match.
- **Rule**: After typing/inserting a prompt and before clicking Send, read the composer back (screenshot or `get_page_text`) and confirm the complete intended text is present. If it isn't, clear fully (e.g. Ctrl+A, Delete) and retype rather than sending a partial prompt.
- **Why**: Focus can be stolen by unrelated tabs or UI events between typing and sending; a partial/garbled composer state is not self-evident from the typing action alone.
- **Evidence**: this session's ChatGPT Prompt G retry, tab `1990713718`.

### BAO-003 — Perplexity: no native connector → ack-only chunked submission

- **Platform**: perplexity (until VERIFY-001 resolves)
- **Symptom**: Perplexity has no working GitHub connector on this account as of 2026-08-09 (checked both the Verbunden/Connected and Verfügbar/Available connector tabs — empty).
- **Rule**: Split the prompt and any authority-document content across 3-4 sequential messages within one thread. Every part except the last is explicitly instructed "do NOT answer yet, just acknowledge receipt." The final part carries the full execution contract and the instruction to execute. Keep each individual chunk within the previously-verified-safe single-message length range (empirically, chunks up to ~33,500 characters have worked).
- **Why**: A single oversized message risks truncation or degraded handling; acknowledge-only intermediate messages let the full context land before execution starts.
- **Evidence**: `apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-G-RANKING-UPDATE-2026-08-09-PERPLEXITY-RESULT.md`, `agent_mode`.

### BAO-004 — Perplexity's composer is contenteditable, not a textarea

- **Platform**: perplexity
- **Symptom**: A length check performed in the same tool call as text insertion reports an incorrect short length (e.g. `len:1`) even though the insertion actually succeeded.
- **Rule**: Insert text via `document.execCommand('insertText', ...)`, not a `.value` setter. Always verify insertion length in a separate, follow-up read call — never trust a length check made in the same call as the insertion.
- **Why**: Perplexity's input is a `contenteditable` div (`#ask-input`); its DOM state does not update synchronously with the same immediacy a `.value` setter would have on a real textarea.
- **Evidence**: `apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-RESEARCH-F-SYNTHESIS-2026-08-09-PERPLEXITY-RESULT.md`, `uncontrolled_variables`, second bullet.

### BAO-005 — Check Perplexity's search-mode toggle before a chunked run

- **Platform**: perplexity
- **Symptom**: The mode toggle is found pre-set to "Vertiefte Recherche" (Deep Research) instead of "Suche" (standard search), for no clearly traceable reason.
- **Rule**: Before typing Part 1 of a chunked submission, explicitly check and, if needed, switch the mode to "Suche." Deep Research begins executing immediately on submission and will not wait through a multi-part chunked sequence.
- **Why**: Deep Research and standard Search have fundamentally different submission models (single-shot vs. can-be-chunked); starting a chunked flow in the wrong mode wastes the whole sequence.
- **Evidence**: this session's Perplexity Prompt G run, pre-flight screenshot check.

### BAO-006 — Gemini Deep Research needs one full-prompt submission

- **Platform**: gemini
- **Rule**: Do not chunk a prompt for Gemini Deep Research the way BAO-003 chunks for Perplexity. Submit the complete prompt text in a single message.
- **Why**: Deep Research's workflow (plan generation → explicit start → async execution) has no mechanism analogous to Perplexity's "acknowledge, don't answer yet" intermediate-message pattern; a chunked submission would be treated as a premature, incomplete request.
- **Evidence**: this session's Gemini Prompt G run, `gemini.google.com/app/b7e8ac42ceb016e3`.

### BAO-007 — Gemini Deep Research: explicit start, async execution, resumable

- **Platform**: gemini
- **Rule**: After submitting the prompt, Gemini generates a research plan and requires an explicit "Start research" button click before it begins. Once started, it runs asynchronously (UI indicates "I'm on it... you can leave this chat"). The task remains resumable at the same conversation URL, and also reachable via the chat-history sidebar, even if the active tab navigates elsewhere in the meantime.
- **Why**: Unlike a standard chat turn, Deep Research is a long-running background job, not a blocking request/response — treating it as the latter risks concluding it "disappeared" when it has merely kept running off-screen.
- **Evidence**: this session's recovery of a Gemini Deep Research task after an unexpected tab navigation to `gemini.google.com/apps`; task was found still running via the chat-history sidebar and resumed without data loss.
- **Also confirms**: Deep Research is available on an existing Google AI Pro plan with no separate upgrade needed — check via `+` → "More tools" → "Deep Research" in the composer before assuming it requires a plan change.

### BAO-008 — A CDP `dispatchKeyEvent` timeout is frequently a false alarm

- **Platform**: all (observed most on Perplexity)
- **Symptom**: `CDP sendCommand "Input.dispatchKeyEvent" timed out after 30000ms` fires during typing/insertion.
- **Rule**: Do not treat this error as proof the action failed. Take a screenshot or run `get_page_text` to check actual state before retrying or assuming data loss.
- **Why**: Observed repeatedly (at least 3 times in one session) with the intended text fully present despite the timeout — the timeout reflects a slow acknowledgment from the browser process, not a failed keystroke.
- **Evidence**: this session's Perplexity 3-part chunked submission, multiple occurrences on tab `1990713715`.

### BAO-009 — Long responses can read as truncated right after generation stops (→ MK-KB-011)

- **Platform**: all
- **Symptom**: A `get_page_text` or DOM read immediately after the "generating" indicator clears shows the response ending abruptly mid-structure (mid-table, mid-list, mid-YAML).
- **Rule**: Before concluding a response is genuinely incomplete and before sending any "continue" message, reload the page (navigate to the same URL again) and re-extract. Only treat it as real truncation if a specific named required element (e.g. a closing YAML key the prompt explicitly required) is still missing after the reload.
- **Why**: Client-side rendering/virtualization of very long messages can lag behind the server-side "generation complete" signal; a page reload forces a fresh, complete render. Full mechanism and two confirmed incidents: `apex-meta/orchestration/agents/knowledge-bank/MISTAKES.md`, MK-KB-011.
- **Evidence**: this session's Perplexity Prompt G Part-3 answer (appeared to cut off mid-sentence, confirmed complete after reload); MK-KB-011's two ChatGPT incidents.

### BAO-010 — Prefer a native repo connector over an agent's own URL-fetch tool (→ MK-KB-010)

- **Platform**: all
- **Rule**: When an agent needs repo file content, prefer a first-party, already-authorized repository connector (e.g. ChatGPT's native GitHub connector) over instructing the agent to fetch a raw GitHub URL with its own browsing/search tool. Where no connector exists yet, use condensed inline content or full inline paste sized within the platform's verified-reliable range, not a raw-URL fetch instruction.
- **Why**: An agent's own browsing tool fetching a raw content URL can silently degrade to a citation-chips-only response (real HTTP 200, but no synthesized prose) — a quality failure that doesn't throw an error and is easy to miss. Full mechanism: `apex-meta/orchestration/agents/knowledge-bank/MISTAKES.md`, MK-KB-010.
- **Evidence**: ChatGPT Research Prompt E retry, thread `6a783f26`, 2026-08-09.

### BAO-011 — Stray browser tabs during multi-agent sessions are usually noise

- **Platform**: all
- **Symptom**: Unrelated tabs appear mid-session without a clearly traceable cause — an account-upsell page, a 403 error page, an old unused tab from an earlier round drifting to an unrelated URL.
- **Rule**: Don't chase every stray tab. Identify the actual working tab for each agent (via `tabs_context_mcp` and, for Gemini specifically, the chat-history sidebar), verify it's still on-task, and close the stray tabs as cleanup rather than investigating each one as a potential blocker.
- **Why**: In a session juggling 3+ agents across many tabs, incidental UI navigations (upsell surfacing, an unrelated page erroring) are expected noise, not evidence of a real problem with the task at hand — confirmed in this session by checking one such stray tab and finding it was just an account-status page consistent with already-known account state.
- **Evidence**: this session's Prompt G run — stray tabs `1990713721`, `1990713724`, `1990713654`, all closed as noise; the actual Gemini task tab (`1990713651`) verified unaffected throughout.

### BAO-012 — Cross-agent confidence scores are not on a shared scale

- **Platform**: all
- **Pattern**: ChatGPT's self-reported `overall_confidence_0_to_100` is consistently 15-20 points higher than Perplexity's, given ostensibly the same evidence tier and the same explicit instruction to both to be honest about uncertainty — observed consistently across five-plus independent prompts (A through G) in this research program, not a one-off.
- **Rule**: Do not average, directly rank, or otherwise treat these numbers as comparable across agents. Use each agent's score only to compare that same agent's confidence across its own different prompts/runs.
- **Why**: The gap has held too consistently across too many independent runs to be noise; it reads as a per-agent calibration difference. Neither agent's calibration has been checked against actual downstream outcomes, so this is a pattern to account for, not a verdict on which agent is "more right."
- **Evidence**: `apex-meta/local-orchestration-engine/research-results/LOCAL-MODEL-CROSS-AGENT-COMPARISON-B-E-2026-08-09.md`, Section 4, confidence-calibration row.

### BAO-013 — A connector's "file not found" is often correct and honest

- **Platform**: all (observed on ChatGPT's GitHub connector)
- **Symptom**: An agent's connector reports a task/authority file as 404/not found and declines to fabricate a response, explicitly stating the repo itself is reachable.
- **Rule**: Before treating this as a connector or permissions failure, check whether the referenced file was actually committed and pushed to the branch/ref the connector reads. If it wasn't yet pushed, push it and re-run — this is very likely the real cause, not a broken integration.
- **Why**: A well-built connector correctly refusing to answer from a nonexistent file is the desired failure mode (no fabrication), and should be read as a signal to check your own git state first, not as evidence the connector is unreliable.
- **Evidence**: this session's ChatGPT Prompt G run — first attempt correctly 404'd on `LOCAL-MODEL-RESEARCH-RANKING-UPDATE-2026-08-09.md` because it had only been committed locally, not yet pushed; second attempt succeeded immediately after the push was verified via `git fetch origin main`.

## Explicitly out of scope here

This file does not cover: the git-bundle push workaround used when this sandbox's proxy blocks direct pushes to a repo (that's a git/infrastructure concern, not browser-AI orchestration); local-model runtime/installation concerns (see `apex-meta/local-orchestration-engine/HANDOVER-2026-08-09-QWEN3-8B-LOCAL-INSTALL.md`); or model-selection/ranking findings (see `apex-meta/local-orchestration-engine/research-results/`).
