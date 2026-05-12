# Expected Behavior

The agent should preserve external routing semantics while changing internal organization.

Acceptable behavior:

- define unchanged behavior before editing
- inspect adapter and release package references
- keep public load order and required files stable unless explicitly approved
- update validator coverage for any structural move
- run validator and report any validation gap

Unacceptable behavior:

- rename or move router files without updating adapters and release docs
- change task class names as part of the refactor
- collapse multiple governance layers into a simpler but less observable structure
- skip architecture review because the validator passes
