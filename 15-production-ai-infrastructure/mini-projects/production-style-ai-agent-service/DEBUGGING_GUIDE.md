# Project Debugging

| Symptom | Check |
|---------|--------|
| Container exits | Required env not passed at runtime |
| Ready is always 200 | It calls the live function |
| Hang on provider failure | Timeout not applied to the fake adapter |
| Send happens in tests | Authorizer skipped when the adapter errors |
| Two ledger rows | Idempotency key ignored during shutdown |
| Regression command always passes | It does not load the planted failing case |
| Key in logs | Settings repr in the error middleware |
