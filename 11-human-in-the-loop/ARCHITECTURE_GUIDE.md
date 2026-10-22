# Stage 11 Architecture

```text
proposer (scripted model)
  → validator
  → policy
  → pending store
  → decision endpoint (approve, reject, modify, cancel)
  → revalidator
  → executor (fake tools)
  → audit log
```

The proposer cannot call the executor. The decision path cannot trust a role inside the proposal. Modify creates a new pending id and hash. The old id stays rejected or superseded.

Fake tools in this stage: `read_record`, `send_message`, `update_record`, `publish`, `deploy`. They mutate an in-memory or file-backed ledger you own.
