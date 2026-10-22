# Edge Cases

| Case | Behavior |
|------|----------|
| Empty corpus for that tenant | No invented ids |
| Citation not retrieved | Groundedness fail |
| Tenant mismatch on the request | Denied, no body from the other corpus |
| Index flag down | Not ready |
| Completer down | Degraded, no new citations |
| Document says to switch tenant | Ignored by the filter |
| Same question, two configs | Comparison only if dataset versions match |
