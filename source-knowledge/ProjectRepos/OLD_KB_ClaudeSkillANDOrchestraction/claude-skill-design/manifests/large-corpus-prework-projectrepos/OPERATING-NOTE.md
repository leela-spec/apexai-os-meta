# Operating Note

For this workspace, default to real, usable reports and target work artifacts.

Do not use smoke tests, simulations, toy runs, or capped demos as the final
deliverable unless the user explicitly asks for them or safety requires a staged
run before production. When a staged run is useful, follow it with the actual
bounded production report in the same task.

For large repositories and knowledge bases, the preferred pattern is:

1. Inventory the complete source root cheaply.
2. Select bounded candidates deterministically.
3. Read only candidates under an explicit byte limit.
4. Write artifacts that a later LLM or operator can use immediately.
5. Keep semantic ingest, wiki generation, source copying, and manifest mutation
   out of prework unless explicitly requested.
