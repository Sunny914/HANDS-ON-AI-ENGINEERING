# Implementation Plan

1. Threat model and design note.
2. Policy and snapshot hash, with tests.
3. Pending store and restart test. No executor yet.
4. Decisions: approve, reject, cancel, modify.
5. Fake tools and idempotent execute.
6. Revalidation, expiry, duplicate decisions.
7. Audit log, including refusals and failures.
8. Scripted proposer wired so it can submit and cannot execute.
9. Checkpoint.

The ledger must stay unchanged through step 3.
