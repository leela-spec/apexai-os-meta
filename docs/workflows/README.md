# Global System Workflows

This directory houses cross-repository orchestration workflows executed by the host Hermes CLI or scheduled system jobs.

## Active Workflows

| Workflow ID | File | Description | Execution Cadence |
|---|---|---|---|
| **WF-01** | [`WF01_WEEKLY_META_ORCHESTRATION.md`](WF01_WEEKLY_META_ORCHESTRATION.md) | Sunday 23:00 sweep: checks git divergence across all 4 repos, verifies Docker service health, and runs ext4 backup. | Weekly (Sunday 23:00) |
