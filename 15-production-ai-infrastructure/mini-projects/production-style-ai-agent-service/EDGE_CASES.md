# Edge Cases

| Case | Behavior |
|------|----------|
| Missing `APP_MODE` | Process does not serve |
| Store down | Not ready |
| Adapter timeout | Bounded attempts, then an error id |
| Third in-flight call | Busy or queued, as documented |
| `approved: true` on send | Does not send |
| Other user's record | Body absent |
| Drain set | New call rejected. Finished in-flight write kept once |
| Bad image | Smoke fails. Rollback note says which tag is current |
| Docker missing | Unit tests still run. Smoke marked blocked |
