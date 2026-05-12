# Review Workflow

Use this workflow when the primary output is assessment, findings, risk identification, or approval guidance without implementation.

## Inputs

- review target
- review scope
- relevant files or governance layers
- expected review lens

## Required Loop

1. Define review scope and assumptions.
2. Inspect relevant files and governance constraints.
3. Identify findings, risks, and gaps.
4. Prioritize findings by severity.
5. Report residual risk and validation limits.

## Default Skills

- `skills/review.md`
- `skills/architecture_review.md` when architecture is in scope
- `skills/state_management.md` only when review changes explicit project state

## Checklist Binding

Required:

- `checklists/review.md`

Optional based on scope:

- `checklists/architecture.md`
- `checklists/safety.md`

## Evaluation Binding

Optional by default:

- `evaluation/governance_compliance.md`

Required when reviewing governance execution:

- `evaluation/execution_quality.md`
- `evaluation/governance_compliance.md`

## State Expectations

- Review-only tasks normally do not update state.
- Update `risk_state.yaml` when a persistent project risk is identified.
- Update `architecture_state.yaml` when the review confirms or changes architecture assumptions.

## Exit Conditions

- findings are prioritized by severity
- assumptions and scope limits are explicit
- residual risks are stated
- no implementation occurred unless separately requested
