# Archive / History Policy

## Goal

Keep prior architecture recoverable without allowing stale files to remain ambiguous active authority.

## Rule

When the project replaces an active architecture file, contract, template or instruction that should no longer be discoverable as current authority:

1. preserve it under an explicit archive/history path;
2. retain enough path/date/context to reconstruct what it replaced;
3. remove it from active runtime references;
4. update links that previously treated it as current;
5. record the replacement decision in `DECISIONS.md`.

## Preferred location

Use the repository's existing `apex-meta/archive/` as the durable history area for retired production Weekly Orchestration material. Create a weekly-orchestration-specific subfolder when Module 00 performs the first real archive migration.

Project-only superseded planning/handover material may be kept under this project's own future `archive/` subfolder if it never participated in production runtime.

## Do not

- leave old and new contracts beside each other with no precedence marker;
- delete historically useful architecture solely to reduce clutter;
- keep archived files referenced by active skills as if they were current;
- duplicate an archived file into several history locations.

Git history remains the ultimate change record; the archive exists because prior architecture is often useful for human/AI comparison and rediscovery.
