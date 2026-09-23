---
okf: 0.2
type: exact_match_patch
id: c03-pilot-informatics-router
status: proposed_not_applied
target: apex-meta/handoff/universal-ai-instruction-system/08-TIER-A-XML-EMBEDDED-PILOT-v0.2.md
base_commit: 244c2d15a91d60e06f9989ae402efd00871c0700
match_count_required: 1
---

# Purpose

Replace only the C03 Informatics block with the evidence-backed router form.

## old

~~~text
  <informatics when="creating, editing, auditing, or validating formal repository knowledge, architectural documentation, or Informatics-governed artifacts"
               principles="structured-authoring,progressive-disclosure,current-truth"
               ref="apex-meta/informatics/index.md"
               deepen_when="the canonical profile, metadata, migration, or validation details are needed">
    Apply the canonical Informatics profile only when this trigger matches; otherwise respond in the form best suited to the task.
    <serialization>Use the canonical metadata and index conventions without duplicating deeper body content.</serialization>
    <information_mapping>Prefer scan-friendly single-purpose blocks, tables, and bullets when they improve comprehension; do not force them where cohesive prose is better.</information_mapping>
    <procedural_prose>Use active voice and one command per sentence for procedural instructions; apply sentence-length targets only when the canonical style profile requires them.</procedural_prose>
    <progressive_disclosure>Provide the smallest sufficient context first and load deeper specification details just in time.</progressive_disclosure>
  </informatics>
~~~

## new

~~~text
  <informatics when="creating, editing, auditing, or validating an artifact governed by the Apex Informatics Standard"
               principles="conformance,information-typing,progressive-disclosure,current-truth"
               ref="apex-meta/informatics/index.md"
               deepen_when="the artifact's canonical profile, metadata, topic structure, migration, or validation requirements are needed">
    Apply the canonical Informatics profile only to governed artifacts. Preserve the artifact's information type, authority, and current-truth boundary; load and validate only the profile details required for the task. Do not impose Informatics serialization or style on ordinary documentation, code, chat, or unmanaged history.
  </informatics>
~~~

## verify

- exact old block matched once;
- only C03 changed;
- all neighboring modules are byte-unchanged;
- no full-file regeneration;
- no whitespace or line-ending churn outside the block.
