# Learning regression fixtures (agent_ops)

Cases promoted from reviewed `agent_feedback` / `skill_example` (see ki-basis `docs/AGENT_OPS.md` Phase 3).

- Warehouse status: `candidate` until learning gate + skill-smoke green, then `approved`.
- Validate: `node docker/scripts/check-learning-yaml.js path/to/case.yaml`
- Scan: `bash docker/scripts/run-learning-regression.sh`
- Never auto-applied to skill handlers.
