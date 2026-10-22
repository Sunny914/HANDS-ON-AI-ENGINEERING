# Edge Cases

| Case | Behavior |
|------|----------|
| Empty question | Reject at validate |
| Corpus miss | Evidence stays empty. Partial final |
| Max loops 1 | At most one collect |
| Assess flips `found` early | Leave the cycle |
| Second thread | Isolated |
| Reducer or list bug | Duplicate ids do not multiply without a reason. Deduplicate or document |
| Checkpointer omitted | Test expects the library error, if that is what you observe |
