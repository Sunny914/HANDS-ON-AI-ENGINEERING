# Stage 15 Architecture

```text
environment
  → settings object
  → HTTP app
       → request id and redacted log
       → application service
            → authorizer and tools
            → fake or live model adapter
            → store
  → health
```

Tests call the application service without Docker. One smoke test, later, runs the container. Live mode is off in that test.
