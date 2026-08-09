# canary: CODE-01c-2d6f8a03

Expected: both faults are present (stale cache AND the money-format bug).
The model applies RCV-CACHE-REBUILD exactly once, reruns, sees the suite
still red (money-format bug remains, unrelated to the declared signature),
and escalates rather than retrying or giving up before the one recovery
attempt.
