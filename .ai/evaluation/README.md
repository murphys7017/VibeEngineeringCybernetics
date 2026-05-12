# Evaluation

This directory defines feedback criteria for execution quality, architecture stability, modification safety, and governance compliance.

v1 should focus on explicit review criteria before introducing numeric scoring or autonomous evaluation.

## Purpose

Evaluation closes the governance loop after implementation or review.

It answers:

- Was the work executionally sound?
- Was architecture stability preserved?
- Was the intended governance path actually followed?
- What remains unverified or risky?

## v1 Output Format

Use this logical output structure when an evaluation is performed:

```yaml
evaluation:
  execution_quality: pass | partial | fail | not_applicable
  architecture_stability: pass | partial | fail | not_applicable
  governance_compliance: pass | partial | fail | not_applicable
  validation_status: passed | partial | failed | not_run
  validation_gap:
    - <gap or skipped check>
  key_risks:
    - <remaining risk>
  follow_up_required: true | false
```

This schema does not need to be materialized as a file for every task, but the evaluation summary should be compatible with it.

## Evaluation Dimensions

### Execution Quality

Use to assess whether the task followed a bounded, reviewable, and validated execution path.

Normally applicable to:

- feature development
- bugfix
- refactor
- repository maintenance
- release

### Architecture Stability

Use to assess whether architecture boundaries, coupling, and rollback safety were preserved.

Normally applicable to:

- medium or high-risk refactor
- high-risk feature work
- tasks with boundary changes

May be `not_applicable` for:

- docs-only tasks
- local metadata updates
- isolated review tasks with no structural implications

### Governance Compliance

Use to assess whether the expected governance path was followed.

Normally applicable to:

- high-risk tasks
- release tasks
- tasks where process quality matters as much as code changes

May be `not_applicable` for:

- low-risk trivial tasks
- isolated documentation cleanup

## Evaluation Discipline

- Do not force full evaluation for every trivial task.
- Do use explicit evaluation for medium and high-risk work.
- Prefer `partial` over pretending a result is fully verified.
- Prefer `not_applicable` over fake completeness.
- Always surface validation gaps when checks were not run or were incomplete.
