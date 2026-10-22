# Stage 02 Debugging

| Symptom | Look at |
|---------|---------|
| Cost is absurd or zero | Units: cents versus dollars, prompt versus completion tokens |
| Last word missing | Stream loop stopping before the final delta |
| Fallback never happens | Error type not translated, so the router does not see a retryable failure |
| Fallback calls the same name twice | Candidate list contains duplicates, or the index never advances |
| Tests hit the network | Adapter constructed inside the test instead of injected |

Debugging folders contain broken code. Write a hypothesis before `MENTOR_NOTES.md`.
