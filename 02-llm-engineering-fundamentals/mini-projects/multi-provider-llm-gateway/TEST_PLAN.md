# Test Plan

- Message and sampling validation
- Both fixture parsers if both adapters exist
- Budget overflow
- Router cases listed in the acceptance criteria
- Ledger totals
- Stream assembly
- Structured-output success and failure
- Optional live test skipped without `RUN_LIVE_LLM`

Use fakes. Do not mock the router in the router tests.
