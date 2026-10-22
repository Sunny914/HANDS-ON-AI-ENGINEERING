# Acceptance Criteria

- [ ] Scripted finish returns the answer and only real citation ids
- [ ] Invented citation does not count as a clean final
- [ ] max_steps stops a script that never finishes
- [ ] Repeated identical search stops with `repeated_action`
- [ ] Timeout retries once; not-found does not
- [ ] Guest-style `allow: true` in the proposal does not add a tool
- [ ] Empty search does not crash
- [ ] Trace length and stop reason are asserted
- [ ] No network in default pytest
