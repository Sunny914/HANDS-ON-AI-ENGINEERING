# Stage 05 Debugging

| Symptom | Look at |
|---------|---------|
| A string reached a function that adds money | Validation was skipped or coerced |
| Second call charged again | Idempotency key ignored |
| A guest ran an admin tool | Policy checked a field the model supplied, not the principal |
| Unknown tool crashes the process | Registry miss is not a typed error |
| The model never sees the failure | You raised and dropped the tool result |

Debugging exercises are broken on purpose. Hypothesis before `MENTOR_NOTES.md`.
