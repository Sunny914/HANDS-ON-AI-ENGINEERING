# Project Debugging

| Symptom | Check |
|---------|--------|
| Test hangs | Timeout not applied to the fake or the client |
| Two upstream calls for one key | Lookup happens after the call, or the key is not stored |
| 200 on invalid JSON | A catch-all handler from dbg-01 came back |
| 401 on health | Auth dependency mounted on the whole app |
| Empty database in the API test | Test and app opened different file paths |
| Flaky retry test | Retry sleeps on a real clock. Inject a clock or set the delay to zero |

Use the Stage 01 debugging guide for the general loop. Write the request, status, and one log line before editing.
