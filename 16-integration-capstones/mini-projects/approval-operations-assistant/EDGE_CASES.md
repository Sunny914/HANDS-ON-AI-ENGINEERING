# Edge Cases

| Case | Behavior |
|------|----------|
| Skip-approval flag | Ignored |
| Clock at expiry | No send |
| Approve after cancel | Refused |
| Policy missing | Fail closed |
| Stale record version | No send |
| Audit write fails | Do not claim success. Document the gap if the tool already ran |
| Second process | Pending still unexecuted |
