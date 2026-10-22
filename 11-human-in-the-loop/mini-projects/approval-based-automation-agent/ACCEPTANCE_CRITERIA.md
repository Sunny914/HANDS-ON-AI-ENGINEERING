# Acceptance Criteria

- [ ] Threat model exists and names tests for swapped payloads, self-approval, replay, stale versions, and a model `approved` flag
- [ ] Read runs without a pending approval
- [ ] Send does not touch the ledger until a different, authorized approval exists
- [ ] `skip_approval: true` still pauses send
- [ ] Restart leaves a pending send unexecuted
- [ ] Approved arguments are the arguments the fake tool receives
- [ ] Changed arguments or a new hash are refused
- [ ] Stale record version is refused
- [ ] Requester cannot approve their own deploy
- [ ] Two executes produce one ledger append
- [ ] Expired and cancelled items do not run
- [ ] A modified preview is a new pending id
- [ ] Audit contains the refusal and the successful execution sequences
- [ ] A failed fake tool is not marked executed
- [ ] Default pytest needs no API key and opens no sockets
