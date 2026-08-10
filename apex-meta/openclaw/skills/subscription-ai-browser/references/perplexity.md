# Perplexity

1. Require exactly one shared tab at `www.perplexity.ai`.
2. Start a new conversation when `session_policy` is `new_conversation`.
3. Open the mode control and select the exact declared `mode`, such as `Learn step by step`. Resnapshot and verify the selected label.
4. Open the model control and select the exact declared `model`. Select the declared `reasoning_mode` only through a control explicitly associated with that model.
5. Do not treat a hidden model control as proof that a prior model selection persists. If the declared mode removes the model/reasoning controls and the combined state cannot be verified, stop.
6. The composer is a `contenteditable` element (`#ask-input`), not a textarea. Snapshot it and insert the immutable prompt with one native browser `type` action targeted at that element.
7. Verify the inserted content in a separate snapshot. Submit only after it matches exactly. Never use browser JavaScript evaluation.
8. `Deep research` begins on submission; never submit a partial or multi-part prompt.
9. Wait until generation controls indicate completion. Capture the final answer verbatim, including citations.
