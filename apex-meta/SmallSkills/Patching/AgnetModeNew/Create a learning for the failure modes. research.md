<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# Create a learning for the failure modes. research the web for what has happened here and why something so basic is failiing without beeing able to be repaired

Confirmed via research: this is not a mystery bug, it's a well-documented, structural limitation of connector-based file access in agent systems — and it's the actual root cause behind most of the 14 prior failures, not a series of unrelated bugs.

## The core finding

A Reddit thread describing the *exact* symptom you hit states: pasting a ~2000-line file directly into ChatGPT works fine, but accessing the same file through a GitHub connector "truncate[s] or only partially reveal[s] it, making it feel more like an advanced code search rather than complete repository access". That is precisely what happened to your Section 7 fetch — the connector never guarantees full-file delivery, it silently returns partial content dressed up as if it were complete.[^1]

This pairs with a second documented mechanism: tools apply a **silent truncation cap** (commonly ~8KB by default) and the agent "reasons over" the cut content without knowing it was cut — "drop the overflow and continue" is the default behavior, not an error state. Nothing in the tool output tells the model "this was truncated" — it just looks like a complete response, so the agent proceeds confidently on partial data.[^2]

## Why every fix created a new failure

This maps directly to what's called **context debt** and the **memory wall** in current agent-architecture research: long-running agents accumulate a gap between what they know and what they need to know, and by the time they're many steps deep, they "follow the loudest recent context instead of the goal you set". Each patch you and I made fixed one visible symptom (ZIP loss, fabrication, naming) but the underlying mechanism — silent partial reads compounding over a long single session — was never addressed, so it kept resurfacing in a new shape.[^3][^4]

## The Learning — for the record

| Failure \# | Symptom | Root layer |
| :-- | :-- | :-- |
| 1-9 | Repo-discovery loops, fabrication, ZIP loss, naming, unnecessary git checks | Downstream — task ambiguity |
| 10-13 | Large-file fetch thrashing, wrong write path | Downstream — undefined edge-case handling |
| 14 | Zero patches produced, Section 7 "read" but empty | **Root cause** — silent connector truncation feeding false-complete reads into a long single-session agent with no checkpointing |

The documented fix pattern for this exact class of failure is **explicit checkpointing to disk plus verified reads, not longer or smarter single-session prompts**. One practitioner's rule is blunt and directly applicable here: *"Don't let the model read the file"* through a lossy intermediary when the content is load-bearing  — meaning for anything like Section 7 that the whole task depends on, the read must be verified byte-for-byte (e.g., length check against a known source, or split into guaranteed-small chunks) rather than trusted on the first pass.[^5][^6][^7]

## What this means going forward

Stop adding rules that assume the agent can reliably self-report "I read the whole section." It cannot detect its own truncation — that's the documented mechanism, not a training gap. Two structural changes, not another patch:[^2][^1]

- Never let a single connector fetch be the sole source of a load-bearing section — require a length/checksum check against something independently known (e.g., ask the plan file's line count upfront and verify the fetch returned that many lines).
- Split any file over roughly 200-300 lines into pre-chunked artifacts *before* the agent run starts, rather than asking the agent to chunk it live — live chunking is exactly what produced the duplicate-mirror disaster in failure \#14.

This isn't a 15th patch to the prompt — it's a change to how the source plan itself is prepared and delivered, which is the only thing that stops this specific mechanism from recurring.
<span style="display:none">[^10][^11][^12][^13][^14][^15][^16][^8][^9]</span>

<div align="center">⁂</div>

[^1]: https://www.reddit.com/r/ChatGPT/comments/1qnspj9/is_there_a_github_app_connection_limitation/

[^2]: https://tianpan.co/blog/2026-05-10-silent-tool-truncation-8kb-default-agent-reasons-blind

[^3]: https://tallyfy.com/ai-agent-context-drift/

[^4]: https://www.mindstudio.ai/blog/ai-agent-memory-wall-long-running-jobs

[^5]: https://understandingdata.com/posts/dont-let-the-model-read-the-file/

[^6]: https://dev.to/the_bookmaster/why-your-ai-agent-keeps-losing-context-and-how-to-fix-it-3afk

[^7]: https://dev.to/bobrenze/ai-agent-context-window-management-how-i-handle-tasks-that-take-longer-than-my-memory-4b47

[^8]: ChatHistoryClaudeConstantFailures.md

[^9]: https://www.arkeoai.com/ai-in-business/chatgpt-agent-mode-reddit

[^10]: https://delx.ai/agents/agent-context-overflow-solutions

[^11]: https://www.betterclaw.io/blog/agent-losing-context-fix-guide

[^12]: https://community.openai.com/t/persistent-issues-with-gpt-model-loss-of-contextual-understanding-and-continuity-in-conversations/600365

[^13]: https://www.reddit.com/r/ChatGPTcomplaints/comments/1oidk60/pro_tip_if_your_chatgpt_gets_stupid_in_long_chats/

[^14]: https://github.com/openai/codex/issues/3997

[^15]: https://blog.jroddev.com/context-window-management-in-agentic-systems/

[^16]: https://help.openai.com/en/articles/11752874-chatgpt-agent

