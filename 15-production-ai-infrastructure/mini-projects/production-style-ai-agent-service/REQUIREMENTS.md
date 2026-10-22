# Requirements

## Stories

- As a caller, I send one request and get a structured result or a structured error with a request id.
- As an operator, I can see whether the process is live and whether it is ready.
- As a reviewer, I can start the service in fake mode from a container and roll back to the previous image tag.

## Functional

- Service contract: `POST /v1/tasks` with a question and a user id. Response includes status, request id, and either a short answer with evidence ids or an error code.
- One fake model adapter. Live mode is optional and off in tests.
- One read tool and one high-risk tool such as send. Send requires the Stage 14 or Stage 11 rule: no self-approval, proposal flags ignored.
- Config validation from ex-01. Example env file has empty secrets.
- Timeouts and bounded retries on the adapter.
- A concurrency cap you can set in config.
- `/health/live` and `/health/ready`.
- Request ids, redacted events, and no secret in error bodies.
- An offline regression command with a handful of cases from Stage 12, or a documented subset. A failed gate is a non-zero exit.
- Dockerfile you write: non-root, no baked secret, fake mode smoke.
- Graceful shutdown behavior from ex-07, even if the HTTP server's signal handling is a thin wrapper.
- `DEPLOY.md` with smoke and rollback. `RUNBOOK.md` with one dependency-down incident and one bad-image incident.
- ADR for what you refused: Kubernetes, a second provider, and a live key in CI.

## Nonfunctional

- Default pytest does not need Docker or a network.
- The smoke milestone is a separate command.
- Startup fails on invalid config.

## Non-goals

A multi-node cluster, a paid provider in CI, Redis, and a general agent platform.
