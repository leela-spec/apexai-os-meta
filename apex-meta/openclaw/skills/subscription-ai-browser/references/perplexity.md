# Perplexity

1. Select the open tab whose hostname is `www.perplexity.ai` (open one if none exists).
2. Start a new conversation when `session_policy` is `new_conversation`.
3. Open the mode control and select the exact declared `mode`, such as `Learn step by step`. Resnapshot and verify the selected label.
4. Open the model control and select the exact declared `model`. Select the declared `reasoning_mode` only through a control explicitly associated with that model.
5. Do not treat a hidden model control as proof that a prior model selection persists. If the declared mode removes the model/reasoning controls and the combined state cannot be verified, stop.
6. **The composer has a known, stable CSS selector: `#ask-input`. Target it by `selector`, not by a snapshot `ref` — this is more reliable than copying a ref token.** Correct call:
   `{"action": "act", "targetId": "<tabId>", "request": {"kind": "type", "selector": "#ask-input", "text": "<exact prompt>"}}`
   Then submit with a separate `act` call: `{"action": "act", "targetId": "<tabId>", "request": {"kind": "press", "selector": "#ask-input", "key": "Enter"}}`.
   Do **not** put the text in a `values` field — `values` is for `select` dropdowns, not for typing text. `type` takes `text`; `press` takes `key`.
7. Verify the inserted content in a separate snapshot before pressing Enter. Submit only after it matches exactly. Never use browser JavaScript evaluation.
8. `Deep research` begins on submission; never submit a partial or multi-part prompt.
9. Wait until generation controls indicate completion. Capture the final answer verbatim, including citations.
