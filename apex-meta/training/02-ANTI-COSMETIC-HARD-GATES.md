# Gate 0: Anti-Cosmetic Hard Gate & Structural Divergence Verification

**Document ID:** `TRAIN-002-ANTI-COSMETIC-HARD-GATES`  
**Target:** Reviewer Agents (R1–R4), Quality Assurance Hooks, CI/CD Gates  

---

## 1. Specification: Gate 0 Anti-Cosmetic Filter

Prior to scoring any artifact set on usability, aesthetic appeal, or alignment, the reviewing agent or test runner must execute **Gate 0**.

```mermaid
graph TD
    Input[Candidate Variant Set: Var A, Var B, Var C] --> Check1{DOM / Tag Tree Similarity <= 0.60?}
    Check1 -- No --> Fail1[REJECT: Identical Layout Topology]
    Check1 -- Yes --> Check2{Copy / Component Entropy >= 0.50?}
    Check2 -- No --> Fail2[REJECT: Boilerplate Placeholder Monoculture]
    Check2 -- Yes --> Check3{Functional Interaction Divergence Verified?}
    Check3 -- No --> Fail3[REJECT: Dead UI / Non-functional Buttons]
    Check3 -- Yes --> Pass[PASS GATE 0: Proceed to Qualitative Scoring]
```

---

## 2. Automated Test Rule Schema

```yaml
gate_0_anti_cosmetic_rules:
  dom_tag_tree_similarity_max: 0.60
  component_archetype_overlap_max: 0.33
  text_jaccard_distance_min: 0.55
  on_rejection:
    verdict: "FAIL_COSMETIC_VARIATION"
    halt_execution: true
    remediation_required: "Re-generate variant using an alternative layout archetype."
```
