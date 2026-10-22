# Requirements

## Behavior

- `POST /sync-jobs` creates a job. Body includes a source URL and a product key.
- The caller may send an `Idempotency-Key` header. If they do, a repeat of that key returns the original job and does not call upstream again.
- The service GETs the source URL with a timeout.
- Temporary upstream failures use your retry policy. Caller errors do not.
- The stored job includes status: `succeeded` or `failed`, plus a short error class on failure. Do not store a stack trace as the client-visible error.
- `GET /sync-jobs/{id}` returns one job or 404.
- `GET /sync-jobs` is paginated.
- Mutating and creating routes require the bearer token from settings. Health, if present, does not.
- Settings include timeout seconds, retry limit, database path, and the token.
- Logs include job id and upstream status. Logs omit the bearer token.

## Nonfunctional

- Default tests make no real network call.
- SQLite file is configurable.
- One process is enough. Do not build a worker queue.

## API shape

You defined most of this in ex-02. If that sketch and this file disagree, this file wins, and you should note the change in the checkpoint.
