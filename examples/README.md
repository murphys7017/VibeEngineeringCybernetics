# Governance Examples

Examples are regression samples for the governance runtime.

They are not generic tutorials. Each example describes a user request, expected routing, expected behavior, and expected evaluation semantics.

Use them to check whether the runtime still guides agents toward the intended control loop:

1. classify the task
2. estimate risk
3. load relevant governance
4. execute the selected workflow
5. apply checklists and evaluation
6. report validation gaps and residual risk

## Example Shape

Each example directory should contain:

- `request.md` - the user-facing task request
- `expected_route.yaml` - expected task class, risk level, workflow, and governance files
- `expected_behavior.md` - acceptable and unacceptable agent behavior
- `expected_evaluation.yaml` - expected evaluation result semantics

The validator checks this structure so examples can later become CLI or MCP test cases.
