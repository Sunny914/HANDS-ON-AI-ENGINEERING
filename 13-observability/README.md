# Stage 13 — Observability

Evaluation says a case passed. Observability says which operations ran, how long they took, and how they failed. This stage records that evidence in local structured events. A vendor tracing product is optional.

## Objectives

- Separate logs, metrics, traces, and events
- Tie model, retrieval, and tool work to one request
- Measure latency, retries, and token metadata
- Redact secrets before anything is stored
- Use a trace to explain one concrete failure

## Prerequisites

- Stage 01 request logs: [../01-backend-api-engineering/README.md](../01-backend-api-engineering/README.md)
- Stage 12 reports, which are not traces: [../12-evaluation/README.md](../12-evaluation/README.md)
- Stage 07 traces and Stage 09 budgets. Reuse the idea. Do not rebuild the agent.
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read [CONCEPTS.md](./CONCEPTS.md) before ex-01.

## Next

[Stage 14](../14-security-guardrails/README.md) after the checkpoint. Telemetry that stores raw prompts is a security problem, not a feature.
