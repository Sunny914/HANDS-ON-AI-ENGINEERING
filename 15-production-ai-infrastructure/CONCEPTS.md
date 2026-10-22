# Stage 15 Concepts

## A service boundary

The process that speaks HTTP is not the place that decides tool authorization or metric math. Those stay in modules you can test without a socket. The service loads config, assigns a request id, calls those modules, and maps errors to responses.

Startup should fail if required configuration is missing. Shutdown should stop accepting work and finish or cancel in-flight calls within a bound you choose. Document which.

## Configuration

Read settings from the environment in the service. Validate them into a typed object once. `APP_MODE=fake` runs the deterministic adapter and must not require an API key. `APP_MODE=live` requires a key and is optional. A missing mode fails startup. Do not commit a real key. A `.env.example` may list names with empty values.

Secret rotation means you can change the key without a code change. You do not have to implement a vault. You do have to show that the key is not hard-coded and not logged.

## Timeouts and retries

Every outbound call, including a fake adapter, has a timeout. A retry needs a limit, and only for errors you marked retryable. Backoff increases the wait. Jitter randomizes it so many clients do not retry together. Tests inject the sleeper and do not wait on a wall clock.

A circuit breaker stops calling a dependency after repeated failures and tries again later. You may implement a tiny counter version or document it as a later control. Do not add one that hides the error from the caller with a success status.

Idempotency keys still matter when a retry might have succeeded on the first attempt. Stage 05 and Stage 11 already require this for side effects.

## Load

A concurrency limit caps how many model or tool calls are in flight. When the cap is hit, reject or queue. Pick one and test it. Backpressure means saying no before the process runs out of memory. A connection pool is relevant if you open a database. A single SQLite file does not need a pool tutorial.

## Health

`/health/live` returns success when the process can answer. `/health/ready` returns failure when a required dependency is marked down, such as the store or the fake provider flag. Do not use the live route to mean ready.

## Degradation

If the model adapter is down, a read of local data may still succeed. A tool that was going to send or deploy does not get a quieter policy. Skipping approval because the model is down is a safety change. Fail closed on those actions and return a clear error.

Provider fallback to a second model is optional. If the fallback uses a weaker policy, do not call it equivalent.

## Release

Keep a small offline suite: config validation, health, one authorized call, one denied call, and one dependency failure. An evaluation gate from Stage 12 can be a command that runs before you tag a release. It is not a live canary in this stage.

A rollback plan says how you return to the previous image and how you know the bad one is no longer taking traffic. Locally, that can be a previous image tag and a smoke command.

## Containers

A Dockerfile should copy the app, install dependencies, run as a non-root user, and not bake secrets into the image. Configuration arrives at runtime. A smoke test starts the container, checks readiness, and stops it. Kubernetes is an optional extension after this works on one machine. Do not start there.

Queues, Redis, and Celery are concepts until a milestone needs them. The core project can finish in-process.

## Migrations

If you store pending approvals or traces, a schema version belongs in the file or database. Startup refuses a version it cannot read. Backup and recovery, here, means you can name the file you would copy. You do not have to operate a replica.
