# Project Debugging

| Symptom | Check |
|---------|--------|
| Read creates a pending row | Policy table marks low risk as pause |
| Send changes the ledger inside submit | Proposer or submit calls the tool |
| Executed recipient is not the preview | Live args used |
| Self-approved deploy runs | Approver id taken from the proposal or same-principal check missing |
| Two ledger lines | Idempotency key missing or keyed only by action name |
| Expired item runs | Clock not injected, or expiry compared as strings |
| Audit skips refusals | Log called only after success |
| Resume executes immediately | Loaded status is treated as approved |
