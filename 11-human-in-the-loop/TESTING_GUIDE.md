# Stage 11 Testing

- No network and no paid API.
- Clock is injected so expiry tests do not sleep.
- Restart tests use two store objects and one directory.
- Security tests: requester approves their own high-risk action, payload changes after approval, `skip_approval: true`, duplicate execute, expired approval, unknown approver.
- Assert on ledger counts. A send that happened twice fails the test even if the status string says executed.
