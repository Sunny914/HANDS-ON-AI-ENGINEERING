# Implementation Plan

1. Choice, ADR, baseline contract.
2. Baseline: propose send, store pending, assert ledger empty.
3. Restart test.
4. Approve, reject, cancel, and one execute.
5. Hash, expiry, and idempotency.
6. Audit and request id.
7. Eval cases and a gate command.
8. Health and config. Optional container and runbook.
9. Checkpoint.

Do not expose execute on the propose route.
