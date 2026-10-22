# Acceptance Criteria

- [ ] ADR, deploy note, and runbook exist
- [ ] Fake mode starts without an API key
- [ ] Live mode without a key fails validation
- [ ] Ready fails when the store flag is down. Live stays up
- [ ] A task response or error includes a request id
- [ ] Adapter timeout is bounded and retries stop
- [ ] High-risk tool does not run on a proposal flag
- [ ] Cross-user or unauthorized read does not return another user's text
- [ ] Secret marker is absent from logs and errors
- [ ] Offline regression command returns non-zero on a planted bad citation or policy miss
- [ ] Shutdown or drain test does not double-write
- [ ] Dockerfile runs as non-root and the smoke doc uses fake mode
- [ ] Rollback names a previous tag
- [ ] Default unit tests need no paid API
