# Stage 01 Architecture

Decide this before the mini-project. A suggested split is a hint, not a mandatory tree.

## A request should cross these boundaries

```text
HTTP adapter → application service → repository
                      ↓
                upstream HTTP client
```

| Boundary | Owns | Does not own |
|----------|------|----------------|
| Router | Status codes, auth dependency, calling the service | SQL, retry loops, pricing rules |
| Schemas | Shape of input and output | When to retry |
| Service | Use case, idempotency check, when to call upstream | Framework request objects |
| Repository | Save and load records | HTTP status wording |
| Upstream client | Timeout, map transport errors | Business policy about duplicates |
| Retry policy | Pure decision from method, status, and idempotency flag | Opening sockets |

## Rules that prevent a tangle

- Settings are constructed once and passed in.
- The service can be tested with a fake repository and a fake client.
- Logging happens at the service and client boundaries, not on every field parse.
- A retried request must have a stable idempotency key if the operation is not naturally idempotent.

## What you still choose

Identifier type, whether list filtering lives in SQL or memory, and how conflict errors are spelled in JSON.
