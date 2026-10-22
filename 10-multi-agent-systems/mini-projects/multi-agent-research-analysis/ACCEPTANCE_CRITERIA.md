# Acceptance Criteria

- [ ] ADR compares workflow, one agent, and multi-agent, and names a rollback
- [ ] A one-note lookup does not call every specialist
- [ ] A research question that needs verification runs verification and records its result
- [ ] Hop limit stops a worker that always asks for another hop
- [ ] Verification can mark a citation unsupported
- [ ] A handoff cannot grant `shell` or switch its own role
- [ ] Duplicate search text across two roles causes one tool side effect
- [ ] Budget exhaustion returns a partial result instead of hanging
- [ ] The same fixture is reported for the single-agent baseline and the multi-agent path
- [ ] The checkpoint states whether the multi-agent path earned its overhead on that fixture
- [ ] Default tests need no API key
