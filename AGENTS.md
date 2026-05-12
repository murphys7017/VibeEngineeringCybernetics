# Agent Entry Point

This project uses `.ai/` as the runtime governance directory for AI coding agents.

Agents should not treat this file as the full governance system. This file is only the entry point and loading guide.

For the shared Codex/OpenCode/Claude Code/Cursor execution protocol, read `docs/runtime/agent_execution_protocol.md`.

## Default Loading Order

1. Read `.ai/README.md`.
2. Read `.ai/index.md`.
3. Read `.ai/constitution/core.md`.
4. Read `.ai/invariants/core.md`.
5. Classify the task using `.ai/router/task_classification.md`.
6. Estimate risk using `.ai/router/risk_levels.md` and `.ai/router/disturbance_model.md`.
7. Load relevant policies, workflows, skills, and checklists using `.ai/router/loading_rules.md`.

## Core Behavior

- Prefer stable constrained execution over unconstrained changes.
- Build context before editing files.
- Make the smallest correct change that solves the task.
- Preserve architecture and user changes unless explicitly instructed otherwise.
- Keep important assumptions, state, and risks observable.
- Validate changes when practical.
- Create commits only when explicitly requested.
