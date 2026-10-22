# Stage 13 Debugging

| Symptom | Look at |
|---------|---------|
| Tool events cannot be joined to the request | Missing parent or a new request id |
| Success with errors underneath | Root status ignores child failures |
| Durations are zero | Clock not injected, start equals end by accident |
| Secret appears in the file | Redactor not on the write path |
| Retry count is zero while the tool ran twice | Second attempt overwrote the first event |

Hypothesis first. Then `MENTOR_NOTES.md`.
