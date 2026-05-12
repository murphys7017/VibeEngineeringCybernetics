# Loading Rules

Load governance material based on task class and risk.

## Default Minimum Load Set

- relevant constitution files
- core invariants
- relevant policies
- one workflow
- task-specific skills
- final checklist

## Notes

- `AGENTS.md` is the runtime entry point and should be read first.
- `constitution/core.md` and `invariants/core.md` are part of the default base for all non-trivial tasks.
- Higher risk tasks load more layers, not different philosophy.

## Loading Matrix

### documentation + low

- Constitution: `constitution/core.md`
- Invariants: `invariants/core.md`
- Policies: `policies/workflow.yaml`
- Workflow: `workflows/feature_development.md`
- Skills: `skills/implementation.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`
- Evaluation: `evaluation/execution_quality.md`
- State to inspect: `state/task_state.yaml`, `state/execution_state.yaml`
- State update expectation: optional lightweight update

### feature development + medium

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`
- Workflow: `workflows/feature_development.md`
- Skills: `skills/planning.md`, `skills/implementation.md`, `skills/review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`
- Evaluation: `evaluation/execution_quality.md`
- State to inspect: `state/task_state.yaml`, `state/context_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: recommended

### feature development + high

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`, `constitution/engineering_control.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`, `policies/permissions.yaml`
- Workflow: `workflows/feature_development.md`
- Skills: `skills/planning.md`, `skills/implementation.md`, `skills/review.md`, `skills/architecture_review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`, `checklists/architecture.md`, `checklists/safety.md`
- Evaluation: `evaluation/execution_quality.md`, `evaluation/architecture_stability.md`, `evaluation/governance_compliance.md`
- State to inspect: `state/task_state.yaml`, `state/architecture_state.yaml`, `state/risk_state.yaml`, `state/context_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: required

### bugfix + medium

- Constitution: `constitution/core.md`, `constitution/stability.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`
- Workflow: `workflows/bugfix.md`
- Skills: `skills/debugging.md`, `skills/implementation.md`, `skills/review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`
- Evaluation: `evaluation/execution_quality.md`
- State to inspect: `state/task_state.yaml`, `state/context_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: recommended

### bugfix + high

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`, `constitution/engineering_control.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`, `policies/permissions.yaml`
- Workflow: `workflows/bugfix.md`
- Skills: `skills/debugging.md`, `skills/implementation.md`, `skills/review.md`, `skills/architecture_review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`, `checklists/architecture.md`, `checklists/safety.md`
- Evaluation: `evaluation/execution_quality.md`, `evaluation/architecture_stability.md`, `evaluation/governance_compliance.md`
- State to inspect: `state/task_state.yaml`, `state/architecture_state.yaml`, `state/risk_state.yaml`, `state/context_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: required

### refactor + medium

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`
- Workflow: `workflows/refactor.md`
- Skills: `skills/planning.md`, `skills/refactor.md`, `skills/review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`, `checklists/architecture.md`
- Evaluation: `evaluation/execution_quality.md`, `evaluation/architecture_stability.md`
- State to inspect: `state/task_state.yaml`, `state/architecture_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: recommended

### refactor + high

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`, `constitution/engineering_control.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`, `policies/permissions.yaml`
- Workflow: `workflows/refactor.md`
- Skills: `skills/planning.md`, `skills/refactor.md`, `skills/review.md`, `skills/architecture_review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`, `checklists/architecture.md`, `checklists/safety.md`
- Evaluation: `evaluation/execution_quality.md`, `evaluation/architecture_stability.md`, `evaluation/governance_compliance.md`
- State to inspect: `state/task_state.yaml`, `state/architecture_state.yaml`, `state/risk_state.yaml`, `state/context_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: required

### review + low or medium

- Constitution: `constitution/core.md`, `constitution/architecture.md`
- Invariants: `invariants/core.md`
- Policies: `policies/workflow.yaml`
- Workflow: `workflows/refactor.md` if structure is being reviewed, otherwise `workflows/bugfix.md` is not loaded and review remains non-editing
- Skills: `skills/review.md`, `skills/architecture_review.md`
- Checklists: `checklists/review.md`, `checklists/architecture.md` when architecture is in scope
- Evaluation: `evaluation/governance_compliance.md` when reviewing governance use, otherwise optional
- State to inspect: `state/task_state.yaml`, `state/context_state.yaml`
- State update expectation: optional

### release + high

- Constitution: `constitution/core.md`, `constitution/stability.md`, `constitution/architecture.md`, `constitution/engineering_control.md`
- Invariants: `invariants/core.md`
- Policies: `policies/runtime.yaml`, `policies/workflow.yaml`, `policies/safety.yaml`, `policies/permissions.yaml`
- Workflow: `workflows/release.md`
- Skills: `skills/planning.md`, `skills/review.md`, `skills/state_management.md`
- Checklists: `checklists/review.md`, `checklists/safety.md`, `checklists/architecture.md` when release changes affect boundaries
- Evaluation: `evaluation/execution_quality.md`, `evaluation/governance_compliance.md`
- State to inspect: `state/task_state.yaml`, `state/risk_state.yaml`, `state/execution_state.yaml`, `state/verification_state.yaml`
- State update expectation: required

### repository maintenance + low or medium

- Constitution: `constitution/core.md`, `constitution/stability.md`
- Invariants: `invariants/core.md`
- Policies: `policies/workflow.yaml`, `policies/safety.yaml`
- Workflow: `workflows/feature_development.md` for additive setup, `workflows/refactor.md` for structural reorganization
- Skills: `skills/planning.md`, `skills/implementation.md`, `skills/review.md`, `skills/state_management.md`
- Checklists: `checklists/implementation.md`, `checklists/review.md`
- Evaluation: `evaluation/execution_quality.md`
- State to inspect: `state/task_state.yaml`, `state/execution_state.yaml`
- State update expectation: optional for low, recommended for medium

## Fallback Rule

If no exact matrix entry fits the task:

1. classify using the nearest primary task class,
2. choose the higher plausible risk level,
3. load the stricter workflow path,
4. document the assumption in `state/context_state.yaml` when state is being updated.
