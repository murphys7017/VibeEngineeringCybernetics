# OpenCode Adapter

Use this adapter to map project governance files into OpenCode-compatible working instructions.

Use `docs/runtime/agent_execution_protocol.md` as the shared execution protocol.

## Required Load Order

1. `AGENTS.md`
2. `.ai/constitution/core.md`
3. `.ai/invariants/core.md`
4. `.ai/router/task_classification.md`
5. `.ai/router/risk_levels.md`
6. `.ai/router/loading_rules.md`
7. task-specific policies, workflow, skills, checklists, evaluation, and state files selected by the router

## Adapter Rule

Do not bypass the router layer. OpenCode-compatible instructions should classify the task and estimate risk before selecting workflow material.
