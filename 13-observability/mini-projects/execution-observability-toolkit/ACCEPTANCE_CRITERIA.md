# Acceptance Criteria

- [ ] One request id returns a tree that includes retrieval, model, and tool
- [ ] A second request id does not leak those events
- [ ] A timeout attempt remains after a later success
- [ ] A planted slow or failed operation is named from the trace
- [ ] `sk-test-` does not appear in the stored events
- [ ] Durations come from the injected clock
- [ ] `DIAGNOSIS.md` cites ids from the fixture
- [ ] Default tests need no API key and no vendor account
