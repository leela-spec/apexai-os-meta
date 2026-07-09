# Hook Policy

This document defines policies for hooking into the deterministic
patching workflow.  Hooks are extension points where additional
behaviour can be inserted before or after key phases of patch
execution.  Proper use of hooks improves transparency and error
handling without compromising determinism.

## Hook Points

The following hook points are recognised:

1. **Pre‑execution** – Invoked immediately before the patch executor
   performs any action.  Use this hook to log the intent, validate
   input parameters or prepare environment variables.  Do not modify
   the target file at this stage.
2. **Post‑replacement** – Called after a replacement has been
   applied but before validation.  Use this hook to collect metadata
   about the change (e.g., timestamp, user ID) or to trigger side
   effects such as refreshing caches.  Do not modify the patched file.
3. **Post‑validation** – Invoked after scope validation and diff
   generation.  Use this hook to record the diff, update audit logs or
   notify downstream systems.  If validation fails, this hook should
   be skipped.
4. **On‑error** – Executed when the executor encounters an error.
   This hook receives the error message and stack trace.  It may be
   used to alert operators or perform cleanup.  Do not attempt to
   recover silently; propagate the error back to the caller.

## Hook Implementation

Hooks must be implemented as Python callables that accept a single
context dictionary.  The context contains information relevant to the
hook point, such as the intent, file paths, diff, timestamp and
error message.  Hook functions must avoid side effects beyond logging
and notification; they must never modify the file or patch intent.

Example hook signature:

```python
def pre_execution_hook(context: dict) -> None:
    """Called before the patch executor runs."""
    # Log the intent
    intent = context.get("intent")
    print(f"Starting patch intent: {intent}")
```

## Registration and Invocation

Hooks are registered by passing a dictionary of hook names to the
patch executor.  Each key corresponds to a hook point (e.g.,
`pre_execution`, `post_replacement`, `post_validation`, `on_error`) and
its value is a callable.  If a hook is not provided, the executor
proceeds without calling it.

During execution the patch executor calls the appropriate hook at
each point, passing the context dictionary.  Hook execution errors
are logged but do not interrupt the patch unless the hook raises
an exception intentionally.  Hooks should be idempotent.

## Restrictions

* Hooks must never modify the target file or alter the patch intent.
* Hooks must not perform network requests or execute arbitrary
  commands.  Logging and simple notifications (e.g., writing to a
  local log file) are permitted.
* Hooks must be deterministic; they should not depend on external
  state that could change between runs.
* When an error occurs, the `on_error` hook may be used to perform
  cleanup, but the original error must still be propagated to the
  caller.  Silent failure is not permitted.