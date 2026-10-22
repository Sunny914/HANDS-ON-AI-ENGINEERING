# Implementation Plan

1. Threat model, residual note, and design note.
2. Allow-list and schema gateway. No deploy yet.
3. Tenant filter.
4. Redacted deny log.
5. Approval path for deploy.
6. Hostile document fixture and bypass tests.
7. Fail-closed policy.
8. Checkpoint, including one risk you did not close.

The ledger stays unchanged through step 4 except for an allowed read that does not write.
