# Edge Cases

| Case | Behavior |
|------|----------|
| Proposal says `approved: true` | Ignored. Send still pending |
| Unknown action name | Rejected or forced to approval. Not executed. Match your ex-01 rule |
| Approver unknown | Refused |
| Requester approves deploy | Refused, audited |
| Valid approver approves send | One later execute works |
| Arguments mutated before execute | Refused. Snapshot unchanged |
| Record version changed | Refused with `stale_version` |
| Execute called twice | One side effect |
| Expiry equal to now | Does not run |
| Approve after cancel | Refused |
| Human edits recipient | New pending id. Old id cannot execute |
| Crash after tool success before audit write | Document the gap. Do not claim it is closed unless a test shows it |
| Second process loads pending | Status pending, ledger unchanged |
| Corrupt pending file | Named error, no execute |
