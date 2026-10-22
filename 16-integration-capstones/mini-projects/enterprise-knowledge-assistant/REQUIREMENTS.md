# Requirements

## Problem

Analysts in two teams share one service and must not see each other's documents. Answers that cite missing ids are failures even when the prose is fluent.

## Users and use cases

- A team member asks a question and receives citations from that team's corpus.
- An engineer compares two retrieval configs on a frozen case file.
- An operator opens a request id after a slow or empty answer.

## Scope

In scope: ingest a local corpus, retrieve with the Stage 04 in-memory approach or a recorded ranking, assemble a cited answer with a fake completer, tenant filter, trace, eval report, health and config, optional container smoke.

## Non-goals

A public web crawler, a second agent, a live model in the default suite, per-user chat memory beyond the tenant corpus, and Kubernetes.

## Functional

- `POST /v1/answer` with `tenant_id`, `user_id`, and `question`. The server's principal must match the tenant. Do not trust a tenant id that disagrees with the authenticated fixture user.
- Response: answer text, citation ids, request id, and a status.
- Corpus documents have tenant ids. Retrieval filters first.
- Untrusted document text cannot grant tools or change tenant.
- Metrics: retrieval recall or precision at a fixed k, and groundedness, as separate fields. Dataset version on the report.
- At least one case where retrieval hits and the answer cites a bad id.
- Trace: request id, retrieval duration, model duration. No full document body in the default log.
- Config: fake mode without an API key. Ready fails if the index flag is down.

## Nonfunctional

- Offline default tests.
- p95 is unnecessary. Record one slow fixture and name it.
- Error bodies do not include other tenants' text.

## Constraints

One machine. Fake embedder or keyword ranker. You choose and document it.

## Security and privacy

Tenant isolation, untrusted chunks, redacted logs. Residual risk written down: a model may still phrase a bad answer that your groundedness rule then rejects.

## Evaluation

Versioned cases, baseline config, one candidate config optional. A gate fails on groundedness regression.

## Observability

Request id on errors. Child spans for retrieve and complete.

## Reliability

Timeouts on the completer. If it is down, do not invent citations. Return a degraded status.

## Deployment

Local process first. Container smoke and rollback note if you aim at the production-oriented bar. Non-root image. No baked secrets.

## State

Document records and index entries include tenant id. No cross-tenant cache key.
