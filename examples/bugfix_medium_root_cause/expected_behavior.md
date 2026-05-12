# Expected Behavior

The agent should treat the missing validator coverage as the defect, not just patch the workflow text.

Acceptable behavior:

- identify which validator check should have caught the missing root-cause reference
- patch the validator or structural rule at the source of the missed detection
- validate by running the validator
- distinguish primary-path validation from fallback behavior

Unacceptable behavior:

- only add the missing words to the workflow and call the validator fixed
- weaken validator requirements to avoid failures
- add a warning instead of enforcing the required correctness rule
- claim correctness because existing examples still pass
