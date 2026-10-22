# Test Plan

- Schema unit tests
- Registry unknown name
- Policy matrix: guest and support, both tools, plus a poisoned role argument
- Idempotency and conflict
- Loop statuses for ok, invalid, denied, and tool_error
- Log test or a logger fake that does not receive a secret, if you introduce any secret-like field

Do not mock the policy inside the executor test. Use a real policy and a fake ledger.
