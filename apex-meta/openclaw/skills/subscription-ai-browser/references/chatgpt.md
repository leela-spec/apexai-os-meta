# ChatGPT

1. From the managed-browser tab list, select a tab whose URL hostname is `chatgpt.com`. If it is absent, open `https://chatgpt.com/` and use the newly opened tab.
2. Apply the exact declared session, mode, model, and reasoning settings and verify them from a fresh snapshot. For `new_conversation`, use a freshly observed new-chat control and verify that the resulting page is a new conversation before entering the prompt.
3. Snapshot the composer immediately before typing. Copy its ref verbatim and insert the immutable prompt in one operation using `{"action": "act", "targetId": "<tabId>", "request": {"kind": "type", "ref": "<fresh composer ref>", "text": "<exact prompt>"}}`.
4. In a separate snapshot, verify the prompt and submission state. The composer sends on bare Enter; submit once using `{"action": "act", "targetId": "<tabId>", "request": {"kind": "press", "key": "Enter"}}`. The installed action contract does not accept a selector or ref for `press`.
5. If submission or a keyboard dispatch times out, take a fresh snapshot before retrying. If the page shows any evidence that submission occurred, never submit the prompt twice.
6. Wait for generation to finish and capture only the response read from the page, verbatim.
