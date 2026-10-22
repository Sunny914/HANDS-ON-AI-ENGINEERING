# Stage 06 Testing

- Round-trip a record through a temp file or temp SQLite database and a new object.
- Restart means a second instance, not a second method call on the same object.
- Conflict tests name which row survives.
- Budget tests use a tiny limit so the drop is obvious.
- Injection tests put "ignore your instructions" in a memory and assert your builder still labels it as data.
- No paid model and no vector store in the default suite.
