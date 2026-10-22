# Stage 15 — Production AI Infrastructure

Package an AI application as a local service: configuration, health, bounded failure, logs, and a container you can start and stop. Kubernetes and paid cloud accounts are not required.

## Objectives

- Validate configuration and keep secrets out of the repo
- Separate liveness from readiness
- Bound timeouts, retries, and concurrency
- Degrade when a model provider is down without weakening a safety check
- Ship a container smoke test and a rollback note

## Prerequisites

- Stage 01 HTTP service: [../01-backend-api-engineering/README.md](../01-backend-api-engineering/README.md)
- Stage 12 gates: [../12-evaluation/README.md](../12-evaluation/README.md)
- Stage 13 events: [../13-observability/README.md](../13-observability/README.md)
- Stage 14 authorization: [../14-security-guardrails/README.md](../14-security-guardrails/README.md)
- Stages 05 and 08–11 for tools, workflows, and approval. Use them. Do not rebuild them from scratch.
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read [CONCEPTS.md](./CONCEPTS.md) before ex-01. Docker is for the project smoke milestone, not for ex-01.

## Next

[Stage 16](../16-integration-capstones/README.md) after the checkpoint. This stage's project is the Production-Style AI Agent Service.
