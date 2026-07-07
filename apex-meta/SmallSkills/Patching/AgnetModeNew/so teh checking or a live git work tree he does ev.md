<img src="https://r2cdn.perplexity.ai/pplx-full-logo-primary-dark%402x.png" style="height:64px;margin-right:32px"/>

# so teh checking or a live git work tree he does everytime even though the infrastructre can not by defualt and design?

Yes — and that's a deliberate, low-cost design choice, not a leftover mistake. Let me separate what's actually happening from what would be a real regression.

## What the prompt does

Step 0 says: check `live_git_worktree_present` via `pwd; git rev-parse --show-toplevel` — **run once only**. Every fresh run of this prompt will execute that check once, get `false`, and move on. It happened again in your latest run because it's a new conversation/session — the agent has no persistent memory of last time's result.[^1]

## Why this is not the failure pattern we fixed

The actual problem we eliminated was **repeated checking within a single run** — 11+ `find`/`env`/`ls` commands hunting for a repo that already returned "not found" once. What you're describing now — checking once per new run — is structurally different and is not wasteful in the way the fixed bug was.[^2][^3]

## But you're pointing at a real, separate question

Should the prompt even bother checking for something the infrastructure can never provide by design? That's fair to ask. Two ways to look at it:


| View | Argument |
| :-- | :-- |
| Keep the check | This container type has been consistent so far, but you have no hard guarantee OpenAI never changes Agent Mode's connector/mount behavior. One cheap check (two commands) is a trivial cost against that risk. |
| Remove the check | If you're certain this infrastructure will never have a live worktree, hardcode `mode_selected: "api_mirror"` and skip Step 0 entirely — saves two tool calls per run, zero downside since the outcome is deterministic. |

Given what we've confirmed across every run so far — this container type never has a live worktree — removing the check entirely and hardcoding `mode_selected: "api_mirror"` is the more honest, minimal version. Keeping a check for something structurally impossible is exactly the kind of unnecessary ceremony the "guard against overengineering" instruction was meant to prevent.

**Recommended fix:** collapse Step 0 to a single fixed declaration instead of a live check:

```
## Step 0 — Mode Declaration (fixed for this environment)
mode_selected: "api_mirror"
(This Agent Mode container has no live git worktree and no clone capability by design — confirmed across multiple prior runs. Do not re-check this.)

ACCESS_DECLARATION:
  github_connector_available: true|false  (checked via one list_resources call — run once only)
  source_plan_readable: true|false        (checked via one fetch attempt)

If github_connector_available is false: mode_selected = "blocked". Stop and report.
```

This removes the pointless `git rev-parse` check while keeping the two checks that actually vary (connector availability, plan readability). Want me to fold this into a full updated prompt version?

<div align="center">⁂</div>

[^1]: create-a-solid-version-with-all-the-best-pracitce.md

[^2]: ThinkinProcessWorkingAgentMode.md

[^3]: ThinPRocessFailPrompt_claude.md

