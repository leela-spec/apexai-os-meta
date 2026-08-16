# OpenClaw execution inbox

This directory is the repository handoff for the Option 1 pilot.

The planning AI publishes one complete `apex.execution-request/v2` file as
`inbox/<execution-id>.request.json`. OpenClaw Cron runs the deterministic inbox
processor every 15 seconds. The processor claims the file by moving it to
`processing/`, invokes the existing dispatcher once, then moves the unchanged
request and a `apex.execution-inbox-receipt/v1` receipt to either `completed/`
or `failed/`.

Only names ending in `.request.json` are eligible. Publish through a temporary
name first and rename only after the final bytes are present. An existing file
in `processing/` is reconciled before a new inbox file. A queue lock prevents
overlapping Cron ticks from dispatching the same request twice.

File placement is the trigger; the processor does not use an AI model for
polling, routing, validation, or retry. The existing request validator,
dispatcher, and evidence verifier remain authoritative for execution.

The first real provider request remains blocked until its normal external-submit
approval is represented by the approved request handoff. Empty-inbox Cron runs
are safe canaries and submit nothing.
