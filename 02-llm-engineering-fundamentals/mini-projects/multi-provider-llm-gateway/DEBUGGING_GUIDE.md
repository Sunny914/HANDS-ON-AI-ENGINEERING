# Project Debugging

| Symptom | Check |
|---------|--------|
| Fallback on a 400 | Error class mapped as temporary |
| Zero cost | Usage not copied onto the normalized response |
| Test waits forever | Fake ignores the timeout argument |
| Prompt text in logs | Info log includes message content |
| Live test runs in CI | Missing skip when the env flag is unset |

Compare a ledger row to the fake script before changing the router.
