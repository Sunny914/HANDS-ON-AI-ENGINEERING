# Edge Cases

| Case | Behavior |
|------|----------|
| Empty corpus | Partial, no fake citations |
| max steps 1 | At most one tool |
| Crash after read | Second run skips it |
| Same search, new task id | Runs again |
| Memory larger than budget | Omitted |
| Final with empty citations | Not `done` if your rule requires evidence |
| Corrupt step log | Named error |
