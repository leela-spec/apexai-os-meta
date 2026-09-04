# KI Basis scoped agent adapter

For any task touching this directory/runtime:

1. read `AGENT-OPERATING-CONTEXT.md`;
2. read `CURRENT-STATE.md` only when current setup/progress matters;
3. inspect live Git/runtime state before mutation.

Do not create another KI Basis instruction owner here.

Core rules:

- preserve unrelated dirty work;
- prefer existing supported interfaces;
- keep `CLI reasoning agent -> Hermes -> real Hermes skills -> applications` as the control path;
- no parallel per-agent Paperless/Firefly/OpenProject implementation;
- no direct DB product control;
- no Docker socket in Hermes;
- stop at secret/operator/architecture gates;
- do not update/uninstall/move the executing CLI agent as part of KI Basis work.
