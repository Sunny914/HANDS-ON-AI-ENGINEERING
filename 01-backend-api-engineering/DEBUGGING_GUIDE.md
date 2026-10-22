# Stage 01 Debugging

Generic process: [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md).

## API-specific symptoms

| Symptom | Look at |
|---------|---------|
| Client sees 200 but the work failed | Exception handlers and status codes |
| Validation error is a 500 | Model not attached to the route, or a broad `except` |
| Handler never returns | Missing timeout on the outbound call |
| Retries multiply writes | Retrying a non-idempotent POST |
| Users see each other's data | Mutable object stored on the app or in a dependency default |
| Works in unit test, fails in the app | Test called the function directly and skipped dependencies |

Write the failing request and the status code before you change code. Debugging exercises in `debugging/` are broken on purpose. Do not open `MENTOR_NOTES.md` until you have a written hypothesis.
