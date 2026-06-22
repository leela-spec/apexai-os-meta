# Mutation Gate Rules

~~~yaml
mutation_gate_rules:
  file_role: canonical_mutation_gate_contract
  owns:
    - mutation_gate
    - accepted_confirm_tokens
    - status_mutation_proposal
    - before_after_mutation_preview
    - operator_validation_result

  mutation_gate:
    all_mutations_require_explicit_operator_confirmation: true
    confirmation_token:
      type: string
      allowed:
        - CONFIRM
        - CONFIRM WRITE
        - CONFIRM MUTATION
    missing_confirmation_behavior: "Keep the requested change as a proposal and do not write."

  accepted_confirm_tokens:
    - CONFIRM
    - CONFIRM WRITE
    - CONFIRM MUTATION

  status_mutation_proposal:
    purpose: "Describe a requested task status change before any write is allowed."
    required_fields:
      id:
        type: integer
      title:
        type: string
      status:
        type: string
        allowed:
          - open
          - in-progress
          - blocked
          - done
          - deferred
      source:
        type: string
      notes:
        type: string
      confirmation_token:
        type: string
        allowed:
          - CONFIRM
          - CONFIRM WRITE
          - CONFIRM MUTATION
      review_flags:
        type: string_array

  before_after_mutation_preview:
    purpose: "Show the exact before and after state for every proposed mutation."
    required_fields:
      before:
        type: markdown_or_yaml_fragment
      after:
        type: markdown_or_yaml_fragment
      source:
        type: string
      review_flags:
        type: string_array

  operator_validation_result:
    purpose: "Record whether the operator accepted, rejected, or requested revision for a mutation proposal."
    required_fields:
      confirmation_token:
        type: string
        allowed:
          - CONFIRM
          - CONFIRM WRITE
          - CONFIRM MUTATION
      review_flags:
        type: string_array
      notes:
        type: string
~~~

## 1. Mutation Lifecycle

~~~yaml
mutation_lifecycle:
  proposal:
    writes_allowed: false
    requires:
      - status_mutation_proposal
      - before_after_mutation_preview
      - review_flags

  operator_review:
    writes_allowed: false
    requires:
      - operator_validation_result
      - confirmation_token

  confirmed:
    writes_allowed: true
    requires:
      - confirmation_token
      - before_after_mutation_preview
      - operator_validation_result

  rejected:
    writes_allowed: false
    requires:
      - operator_validation_result
      - notes
~~~

## 2. Review Flags

~~~yaml
review_flags:
  allowed:
    - missing_confirmation
    - ambiguous_status_delta
    - unsupported_status_value
    - entity_update_uncertain
    - duplicate_entity_risk
    - raw_source_missing
    - planning_feed_incomplete
    - sync_required_before_final_context
    - conflict_between_sources
~~~

## 3. Status Mutation Rules

~~~yaml
status_mutation_rules:
  allowed_status_values:
    type: string
    allowed:
      - open
      - in-progress
      - blocked
      - done
      - deferred

  required_before_after_preview: true
  require_operator_confirmation_before_write: true
  proposal_language_required: true
  confirmed_language_allowed_only_after_confirmation: true

  unsupported_status_value:
    result: operator_validation_result
    review_flags:
      - unsupported_status_value

  missing_confirmation:
    result: status_mutation_proposal
    review_flags:
      - missing_confirmation
~~~

## 4. Non-Goals

~~~yaml
non_goals:
  - "Do not silently mutate task files."
  - "Do not treat approval-like prose as confirmation_token."
  - "Do not accept status values outside the canonical status enum."
  - "Do not omit before_after_mutation_preview for any mutation."
  - "Do not compute dependency eligibility before a status mutation."
  - "Do not rebuild registry after a mutation."
~~~