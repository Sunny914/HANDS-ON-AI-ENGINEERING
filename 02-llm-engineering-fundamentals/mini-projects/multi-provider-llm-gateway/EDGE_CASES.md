# Edge Cases

| Case | Behavior |
|------|----------|
| Empty messages | Validation error, no call |
| Window overflow | Reject locally |
| Temperature out of range | Validation error |
| Primary 429 then success | Retry primary, no fallback if retry succeeds |
| Both providers time out | Typed error, ledger shows both |
| Usage missing on an otherwise good body | Parse error |
| Stream with only usage | Empty text, usage present |
| Same idempotent request id retried by caller | Document whether you dedupe. Deduping is optional. |
