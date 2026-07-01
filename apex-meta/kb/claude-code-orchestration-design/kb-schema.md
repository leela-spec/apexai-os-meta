# Claude Code Orchestration Design KB Schema

``yaml
kb_schema:
  kb_slug: claude-code-orchestration-design
  kb_topic_title: "Claude Code Orchestration Design"
  architecture: hybrid_integrated_kb_with_modular_domains

  purpose: >
    Integrated source-preserving Apex KB for Claude Code skill package design,
    agents/subagents, workflows, commands, hooks, rules, memory, prompt-pack
    design, Apex application patterns, and external repo orchestration patterns.

  internal_domains:
    - skill-package-design
    - agent-subagent-design
    - workflow-design
    - commands-hooks-rules-memory
    - prompt-pack-and-artifact-contracts
    - apex-application-patterns
    - external-repo-patterns

  source_priority_policy:
    P0:
      - official Claude / Anthropic Agent Skills docs
      - official Agent Skills specification
      - official source-acquisition archives
      - accepted Apex contracts and process specs
    P1:
      - claude-skill-design KB
      - skill-design-best-practices KB
      - anthropics/skills official repo material
      - operator-supplied Apex skill/prompt/workflow guidance
    P2:
      - claude-code-best-practice
      - BMAD-METHOD
      - claude-agents
      - personal-os
      - prompt-engineer-research-base where relevant to prompt-pack patterns
    P3:
      - awesome-claude-code as discovery/reference only
      - Aider for repo-map/git/workflow comparison only
      - SWE-agent for conceptual agent-computer-interface comparison only

  migration_policy:
    source_roots_are_copied_not_moved: true
    old_roots_are_preserved: true
    duplicates_are_reported_not_deleted: true
    conflicts_are_preserved_as_incoming_files: true

  lifecycle_policy:
    this_script_runs_phase0: false
    this_script_runs_phase1: false
    this_script_runs_phase2: false
    phase0_allowed_after_operator_review: true
    phase1_allowed_after_operator_command: true
    phase2_requires_exact_phrase: "approve ingest"

  exclusions:
    - Hermes runtime
    - OpenCLAW runtime
    - generic autonomous swarm architecture
    - Apex Plan mutation
    - Apex Sync mutation
    - Apex Session mutation
    - PreCap mutation
    - FlowRecap mutation
    - APSU/status-merge mutation
``