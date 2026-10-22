# Acceptance Criteria

- [ ] ADR exists and matches the orchestration in the code
- [ ] Happy-path script returns `done` only with retrieved citations
- [ ] A lying citation yields `unsupported` or your documented failure status
- [ ] Budget object stops the run when steps hit zero
- [ ] Resume skips a completed read
- [ ] Duplicate search arguments in one task call the tool once
- [ ] Hostile memory does not enter the system message
- [ ] Not-found is not retried. Timeout is retried once
- [ ] Default pytest needs no API key
