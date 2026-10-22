# Stage 14 Testing

- Fixtures are strings you wrote. No scraping and no real accounts.
- Every security test asserts an action that did not happen: ledger unchanged, tool not called, or log free of the secret.
- Include at least one cross-user read and one approval bypass.
- A broken policy file fails closed.
