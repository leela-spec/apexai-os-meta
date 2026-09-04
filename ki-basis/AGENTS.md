# KI Basis scoped agent adapter

When a task touches this directory, the local KI Basis runtime, Hermes, or the installed applications, first read and obey:

`AGENT-OPERATING-CONTEXT.md`

That file is the canonical KI Basis operating context. This adapter must stay thin and must not become a second policy owner.

## Required behavior

- inspect current Git/runtime state before mutation;
- preserve unrelated dirty files;
- use existing supported interfaces before inventing new ones;
- keep the canonical future control path `CLI reasoning agent -> Hermes -> real Hermes skills -> applications`;
- do not build a parallel per-agent Paperless/Firefly/OpenProject implementation;
- stop at secrets, consequential mutation, or architecture gates rather than bypassing them;
- do not update/uninstall/move the executing CLI agent as part of KI Basis work.

For operator onboarding/setup, follow:

`../apex-meta/Alpine/ImplementationPlans/2026-09-03-ki-basis-finalization/OPERATOR-ONBOARDING-WALKTHROUGH.md`
