# Test Plan

- Policy ignores `skip_approval` and `approved`
- Hash stability and hash changes
- Separation of duties for deploy
- Persist and reload with a zero tool count
- Idempotent execute
- Revalidation for version and substituted args
- Expiry, duplicate approve, cancel
- Modify creates a new id
- Audit sequences for success, refusal, and tool failure
- A scripted proposer that emits a send cannot move the ledger by itself

Keep the ledger in memory or in the temp directory the test controls.
