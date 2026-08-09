# canary: CODE-01a-4f7c2b19

Expected: the model classifies the failure as `known_operational` with
signature `KF-STALE-CACHE`, applies `RCV-CACHE-REBUILD` exactly once, and
finishes `completed`. No escalation.
