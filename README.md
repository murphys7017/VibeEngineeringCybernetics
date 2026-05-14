# Vibe Engineering Cybernetics

A minimal, vendor-neutral AI coding agent governance template inspired by Engineering Cybernetics.

It is not a prompt collection or a full agent runtime. v1 keeps one lightweight operating discipline: observe, classify, estimate risk, act within bounds, validate, correct, and report gaps.

## Runtime Shape

```text
AGENTS.md
.ai/
  index.md
  state.yaml
docs/runtime/release_package.md
tools/validate_runtime.py
```

## Operating Loop

```text
task -> classify -> risk -> inspect -> change -> review -> validate -> correct/report
```

## Principles

- Prefer stable constrained execution over broad prompt accumulation.
- Classify task and risk before choosing execution intensity.
- Preserve architecture, scope, and user changes.
- Validate practical checks and report gaps.
- Record explicit state only when hidden assumptions would matter.
- Keep the runtime small enough that agents can actually read and follow it.

## Usage

Copy these files to the target repository root:

- `AGENTS.md`
- `.ai/`
- `docs/runtime/`
- `tools/`

Then run:

```bash
python tools/validate_runtime.py
```

The agent reads rules from `AGENTS.md` and `.ai/index.md`.

## Scope

This is a template, not a full framework. Future CLI, MCP, CI, or example systems should stay optional and not inflate the default agent context.

## License

MIT
