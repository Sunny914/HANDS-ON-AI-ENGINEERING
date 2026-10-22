# Stage 14 Debugging

| Symptom | Look at |
|---------|---------|
| A document changes the caller's role | Authorizer reads text from the chunk |
| A tool runs with a missing field | Executor called before validation |
| User B sees user A's note | Query has no tenant predicate |
| Deploy runs without approval | Proposal flag `approved` is trusted |
| Secret in the log file | Raw arguments logged after a failure |

Hypothesis first. `MENTOR_NOTES.md` is second.
