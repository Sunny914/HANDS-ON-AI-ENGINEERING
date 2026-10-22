# Stage 16 Concepts

## What a capstone is

A capstone reuses earlier stages on a problem that is larger than any one of them. The new work is the integration: one contract, one threat model, one eval set, one way to see a failed request, and one way to run it locally.

A baseline is the smallest path that a test can call. It is not a stub that returns "TODO" at the HTTP edge while the real design exists only in a diagram. For these projects the baseline is offline and uses fakes.

## Which earlier stages are mandatory

| Option | Do not skip |
|--------|-------------|
| A Knowledge | Stage 04 retrieval, Stage 12 groundedness versus retrieval, Stage 13 traces, Stage 14 tenant and untrusted documents, Stage 15 local service |
| B Operations | Stage 11 approval and idempotency, Stage 05 tools, Stage 13 audit-friendly events, Stage 14 fail closed, Stage 12 approval-compliance cases, Stage 15 service |
| C Workflow | Stage 01 API and validation, Stage 07 decision of when not to use an agent, Stage 12 task completion, Stage 13 correlation, Stage 14 allow-list, Stage 15 timeouts and health |

Stages you do not need for that option stay out of the design. Say so in the ADR.

## Rubric

Use the same three bars in the project checkpoint.

- **Basic:** the baseline milestone is runnable offline, with tests for the happy path and one serious failure.
- **Solid:** the security, evaluation, and observability requirements for that option are implemented and explained. The ADR matches the code.
- **Production-oriented:** local deploy or container smoke, a runbook, a regression gate, residual risk, and a rollback or recovery step.

A basic capstone can be an honest finish if you record the bar. Do not label a baseline as production-oriented.

## Incremental shape

1. Contract and non-goals.
2. Baseline behavior with fakes.
3. The failure and security tests that define the option.
4. Evaluation cases and a trace.
5. Health, config, and a local run story.

Starting with a cluster, a live model, or a second agent is a scope error.
