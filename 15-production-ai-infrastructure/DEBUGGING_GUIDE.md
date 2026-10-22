# Stage 15 Debugging

| Symptom | Look at |
|---------|---------|
| Ready while the store is down | Live and ready share one handler |
| Requests hang | No timeout on the adapter |
| Retry storm | No max attempts, or non-retryable errors included |
| Key in the log | Settings object printed |
| Shutdown drops a finished write | Cancel runs before the idempotent record is stored |
| Container starts and immediately exits | Config required at runtime was baked as empty and not passed in |

Hypothesis first.
