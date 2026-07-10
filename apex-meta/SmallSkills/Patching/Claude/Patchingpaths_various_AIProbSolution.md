Nobody magically writes bulletproof shell scripts — the answer is that AI never writes the final mutating command blind; instead you insert deterministic verification gates between AI's proposal and execution, so AI's imprecision gets caught mechanically before it touches the file.[[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]

## Why AI Corrupts Line/Hunk-Based Edits

AI hallucinates on tasks requiring exact positional or character-level accuracy because LLMs predict plausible tokens, not verified state — this is documented broadly as a structural limitation of code-generation LLMs, not a prompting failure. Line numbers and hunk offsets drift the moment file content shifts by even one line, so any AI-guessed line number is unreliable by construction.[[arxiv](https://arxiv.org/html/2404.00971v3)]

## The Countermeasure Pattern

The fix used in practice is: AI proposes, tooling verifies, only verified changes apply. Five concrete mechanisms are used together:

- Exact-match-or-fail: tools like `sed`/`yq` change nothing if the search string isn't found verbatim — silence on a miss is the actual danger, so scripts must check match count explicitly before writing.[[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]
    
- `git apply --check` as a hard gate: this validates a patch applies cleanly against the real current file _before_ any write touches disk — if it fails, nothing happens.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
- Dry-run by default: tools report the diff they would produce without writing, so a human or CI reads the diff before real mutation — this is the default behavior in the Geneclaw and Darwinian Harness safety models.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
- Rollback on failure: every automated patch happens on a dedicated branch/checkpoint; if post-patch tests fail, it auto-reverts.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
- Path/scope allowlisting: the tool rejects any AI-proposed patch that touches files outside a pre-declared scope, so a hallucinated target file or line range gets refused mechanically, not caught by review.[[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]
    

## Step-by-Step Safe Loop

1. AI states plan in plain text first: goal, files it expects to touch, files it will NOT touch.[[1devtool](https://1devtool.com/blog/trust-coding-agents-plan-first-patch-second)]
    
2. AI generates the change as a structured diff or exact-match command — never a line-number-based edit.[[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]
    
3. Tool runs the command in dry-run mode and outputs the resulting diff, nothing is written yet.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
4. A deterministic check verifies: did match count equal expected count? Does the diff touch only allowlisted files?[[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]
    
5. If checks pass, `git apply --check` confirms the patch is applicable to current file state.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
6. Only then does the real write happen, on a branch/checkpoint so it's revertible.[[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]
    
7. Post-write, `git diff HEAD` is captured as the audit artifact — the diff is the source of truth, not the AI's claim of what it did.[[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]
    

## Why Exact-Match Beats Line Numbers

|Approach|Failure mode|Countermeasure|
|---|---|---|
|AI guesses line number|File shifted since AI last saw it → wrong line edited|Never let AI specify a line number; use exact string match instead [[latchkey](https://latchkey.dev/learn/command-reference/yq-front-matter)]|
|AI writes free-form sed regex|Regex too greedy, corrupts adjacent text|Require dry-run diff review before apply [[docs.darwiniantools](https://docs.darwiniantools.com/concepts/safety-model/)]|
|AI writes multi-hunk patch|Partial apply corrupts file if one hunk fails|`git apply --check` — all-or-nothing gate [[news.ycombinator](https://news.ycombinator.com/item?id=47067488)]|
|AI silently "fixes" scope creep|Edits files not in the plan|Path allowlist rejects patch outside declared scope [[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]|

The core principle: the deterministic tool (sed, yq, git apply) is not asked to trust the AI's precision — it's asked to verify the AI's proposal against ground truth (the actual current file bytes) and refuse on any mismatch. That shifts "AI must be exact" to "AI proposes, machine verifies, machine refuses on ambiguity" — which is achievable, whereas AI positional exactness is not.[[codesignal](https://codesignal.com/learn/courses/codex-sdk-automation/lessons/safe-automation-patterns)]