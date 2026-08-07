"""FEE -- Flow Execution Engine.

An execution substrate for step 4 of the Weekly Orchestrator loop. Not an
orchestration system (D-M0), and never to be called one: APEX OS has exactly two
orchestration systems, and FEE is a substrate for one stage of one of them.

Live authority for the seam it fills:
    .claude/skills/weekly-orchestrator/SKILL.md stage_routing.operator_execution
    {agent: none_operator_human_step, gate: G3, trigger: "operator returns evidence or skip signal"}

FEE replaces the actor at that step. It never touches G3.
"""

__all__ = ["__version__"]

__version__ = "0.1.0-candidate"
