# Acceptance Criteria

- [ ] Schema rejects a non-positive refund before the ledger function runs
- [ ] Guest cannot refund, even if the arguments contain a role
- [ ] Guest cannot read another owner's order
- [ ] Support can refund once, and a second call with the same key does not add a ledger row
- [ ] Same key with a different amount is a conflict and does not change the ledger
- [ ] Unknown tool is a result status, not an uncaught `KeyError`, unless your design says crashes are reserved for programmer errors and tests show the difference
- [ ] A raising tool becomes `tool_error` and is tested
- [ ] Default tests need no network
- [ ] Design note matches the principal source in the code
