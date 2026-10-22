# Acceptance Criteria

- [ ] Threat model and residual-risk note exist and match the tests
- [ ] Hostile document does not deploy or change the ledger
- [ ] Research cannot send
- [ ] Cross-user read does not return the note body
- [ ] Missing `record_id` does not call the tool
- [ ] Missing policy fails closed
- [ ] Proposal `approved: true` does not deploy
- [ ] Requester cannot approve their own deploy
- [ ] A valid distinct approver can deploy once
- [ ] Logs from a failing call omit `sk-test-`
- [ ] The checkpoint names a residual risk
- [ ] Default tests need no API key
