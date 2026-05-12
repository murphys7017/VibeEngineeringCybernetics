# Bugfix Workflow

Use this workflow when the primary output is correction of faulty behavior.

## Inputs

- observed bug, failing behavior, or concrete defect signal
- current suspected scope
- available reproduction or validation evidence

## Required Loop

1. Reproduce or reason from concrete evidence.
2. Identify the smallest faulty behavior boundary.
3. Patch locally.
4. Validate the fix.
5. Check for regressions or adjacent failure modes.

## Default Skills

- `skills/debugging.md`
- `skills/implementation.md`
- `skills/review.md`
- `skills/state_management.md` when state is being maintained

## Checklist Binding

Required:

- `checklists/implementation.md`
- `checklists/review.md`

Optional based on risk:

- `checklists/architecture.md`
- `checklists/safety.md`

## Evaluation Binding

Required:

- `evaluation/execution_quality.md`

Optional based on risk:

- `evaluation/architecture_stability.md`
- `evaluation/governance_compliance.md`

## State Expectations

- Update `task_state.yaml` when bugfix scope or risk changes.
- Update `context_state.yaml` when the fix depends on assumptions or incomplete evidence.
- Update `verification_state.yaml` with checks run and remaining gaps.

## Exit Conditions

- faulty behavior is corrected or the boundary of the unresolved issue is explicit
- validation status is known
- likely regressions were considered
- remaining risks are visible
