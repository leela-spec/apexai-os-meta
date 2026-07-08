Here is the full research report, ranked by source reliability with confidence flags:

---

## CLAUDE_CONFIG_DIR Multi-Account Research Report — July 2026

## Q1: Is `CLAUDE_CONFIG_DIR` Officially Documented?

**Answer: YES — it is now officially documented, but with a critical macOS carve-out.**

The official Anthropic authentication docs at [docs.anthropic.com/en/docs/claude-code/iam](https://docs.anthropic.com/en/docs/claude-code/iam) state explicitly: _"If you've set the `CLAUDE_CONFIG_DIR` environment variable on Linux or Windows, the `.credentials.json` file lives under that directory instead."_ The settings page at [docs.anthropic.com/en/docs/claude-code/settings](https://docs.anthropic.com/en/docs/claude-code/settings) references it in the environment variables section.[[docs.anthropic](https://docs.anthropic.com/en/docs/claude-code/iam)]

**Contradiction flagged:** One Japanese-language blog (note.com, May 2026) testing v2.1 series wrote _"although it is not explicitly mentioned in the official documentation, I have confirmed through the CLI binary that it works reliably"_ — this appears to be outdated or reflecting a pre-documentation period. The current official docs do list it.[[note](https://note.com/taculus/n/nabdffabd62c3?hl=en)]

|Source|Status|Confidence|
|---|---|---|
|`docs.anthropic.com/en/docs/claude-code/iam`|✅ Official, lists `CLAUDE_CONFIG_DIR`|**High**|
|`docs.anthropic.com/en/docs/claude-code/settings`|✅ Official env vars reference|**High**|
|dev.to/vainamoinen (May 2026)|✅ Quotes GitHub issue #261 closed-as-completed|**Medium-High**|
|note.com blog (May 2026)|❌ Claims undocumented — now stale|**Low**|

---

## Q2: ToS Penalties / Flagging for Concurrent Multi-Directory CLI Sessions?

**No evidence of any ToS clause or support action specifically penalizing `CLAUDE_CONFIG_DIR` multi-session use under one IP.** The enforcement pattern is clearly documented elsewhere:[[grandlinux](https://www.grandlinux.com/en/blogs/claude-account-ban-risk.html)]

- Holding multiple Max accounts = **not a violation** per Anthropic's stated position (Feb 2026)[[grandlinux](https://www.grandlinux.com/en/blogs/claude-account-ban-risk.html)]
    
- What triggers suspensions: routing subscription OAuth tokens through **third-party harnesses** (OpenClaw, Cline, relay-server pattern = "Architecture A")[[dev](https://dev.to/vainamoinen/two-multi-account-claude-code-architectures-one-anthropic-accepts-one-they-ban-2om7)]
    
- Using the official Claude Code binary with `CLAUDE_CONFIG_DIR` = "Architecture B," which a dev.to analysis (May 2026) specifically characterizes as the pattern _Anthropic itself acknowledged in GitHub issue #261 (closed-as-completed, March 5, 2025)_[[dev](https://dev.to/vainamoinen/two-multi-account-claude-code-architectures-one-anthropic-accepts-one-they-ban-2om7)]
    
- Anthropic's Transparency Hub: ~1.45M suspensions Jul–Dec 2025 — attributed to OAuth token abuse and spam, not multi-directory CLI use[[grandlinux](https://www.grandlinux.com/en/blogs/claude-account-ban-risk.html)]
    

**Confidence: High.** No Reddit/GitHub reports or ToS language found targeting `CLAUDE_CONFIG_DIR` specifically. Risk only arises if multi-account use constitutes _systematic limit evasion_ (medium risk per the table), not the tooling itself.[[grandlinux](https://www.grandlinux.com/en/blogs/claude-account-ban-risk.html)]

---

## Q3: macOS Keychain Collision Risk with `CLAUDE_CONFIG_DIR`

**⚠️ Critical finding: `CLAUDE_CONFIG_DIR` does NOT fully isolate credentials on macOS.** The official IAM docs state credentials on macOS go to **the encrypted macOS Keychain** — and then specify: `"If you've set the CLAUDE_CONFIG_DIR environment variable on Linux or Windows, the .credentials.json file lives under that directory instead."`[[docs.anthropic](https://docs.anthropic.com/en/docs/claude-code/iam)]

The macOS exception is explicit: on macOS, `CLAUDE_CONFIG_DIR` controls config/history/settings isolation but **not** credential storage, which stays in the system Keychain regardless.

This is confirmed by a GitHub gist (fortunto2, April 2026) which documented a _"subtle bug: Anthropic's short-lived OAuth credentials rotate on every refresh, so a snapshot you saved to disk goes stale within hours"_ — and recommends instead using long-lived tokens via `claude setup-token` (1-year TTL) stored in flat files, combined with `direnv` for per-directory switching, and explicitly deleting the stale Keychain entry with:[[gist.github](https://gist.github.com/fortunto2/b326e4727e32f9af1742f0710dcc5f75)]

bash

`security delete-generic-password -s "Claude Code-credentials" -a "$USER" 2>/dev/null`

|Scenario|Isolation via `CLAUDE_CONFIG_DIR`|
|---|---|
|macOS — credentials|❌ Keychain collision risk; must use long-lived token workaround|
|macOS — config/history/MCP|✅ Fully isolated|
|Linux — credentials (`.credentials.json`)|✅ Isolated per dir|
|Windows — credentials|✅ Isolated per dir|

**Confidence: High** (official docs + corroborating gist from community tester).

---

## Q4: Switcher Tool Maintenance Status (July 2026)

Ranked by evidence of recent activity:

|Tool|Language|Last Known Activity|Notes|
|---|---|---|---|
|**[claude-swap](https://pypi.org/project/claude-swap/0.13.0/)**|Python|v0.13.0 published **June 11, 2026** [[pypi](https://pypi.org/project/claude-swap/0.13.0/)]|Most recently updated; PyPI-distributed|
|**[ccsw](https://lib.rs/crates/ccsw)**|Rust|Published **April 21, 2026** [[lib](https://lib.rs/crates/ccsw)]|"Run multiple Claude Code accounts concurrently with shared plugins and settings"|
|**[claude-code-swap / ccs](https://github.com/tensakulabs/claude-code-swap)**|—|Published **March 2026** [[github](https://github.com/tensakulabs/claude-code-swap)]|tensakulabs org; provider-profile focus|
|**[CCSwitcher](https://github.com/XueshiQiao/CCSwitcher)**|macOS app (Swift)|Published **March 21, 2026** [[github](https://github.com/XueshiQiao/CCSwitcher)]|GUI switcher; "switch with a click"|
|**[cc-account-switcher](https://github.com/ming86/cc-account-switcher)**|—|Published **June 30, 2025** [[github](https://github.com/ming86/cc-account-switcher)]|Oldest; 12+ months without visible update|

**Most actively maintained as of July 2026: `claude-swap` (v0.13.0, June 11 2026).** `cc-account-switcher` appears least maintained at ~12 months stale. Confidence: **Medium** (based on publish dates; internal commit frequency not fully verified).

---

## Q5: Account Suspensions Specifically Attributed to `CLAUDE_CONFIG_DIR`?

**No such reports found.** Zero Reddit or GitHub threads attribute a suspension to `CLAUDE_CONFIG_DIR` per-directory CLI use specifically.[[dev](https://dev.to/vainamoinen/two-multi-account-claude-code-architectures-one-anthropic-accepts-one-they-ban-2om7)]

The April 2026 "OpenClaw ban wave" (~1,099 HN points) and the 1.45M suspension figure are all attributable to the relay-server / OAuth-token-harvesting pattern, not per-profile official binary usage. The dev.to analysis (May 2026) explicitly argues Architecture B (CLAUDE_CONFIG_DIR) has _"effectively zero ban-wave risk"_ because each invocation is the official client running independently with its own OAuth flow.[[dev](https://dev.to/vainamoinen/two-multi-account-claude-code-architectures-one-anthropic-accepts-one-they-ban-2om7)]

**Confidence: Medium-High** (absence of evidence, but the claim is coherent with Anthropic's documented enforcement rationale).

---

## Summary Reliability Stack

text

`OFFICIAL DOCS (docs.anthropic.com)      → Q1 definitive, Q3 definitive GitHub issue #261 (closed-as-completed) → Q2 strong signal (Anthropic acknowledgment) GitHub gists (fortunto2, KMJ-007)       → Q3 technical detail, corroborating dev.to/vainamoinen (May 2026)           → Q2, Q5 analysis — well-sourced, cite primary Technical blogs (codeminer42, wmedia)   → Q1 corroboration only PyPI/crates.io timestamps               → Q4 maintenance dates Reddit/community forums                 → No relevant suspension reports found for Q5`

**The single highest-risk gap:** macOS users must not rely on `CLAUDE_CONFIG_DIR` alone for credential isolation — they need the long-lived token + `direnv` approach to avoid Keychain rotation collisions between concurrent sessions.[[gist.github](https://gist.github.com/fortunto2/b326e4727e32f9af1742f0710dcc5f75)]