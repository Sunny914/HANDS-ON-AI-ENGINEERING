# Stage 14 — Security and Guardrails

Model output, retrieved text, tool arguments, and user text are data. This stage puts enforcement in application code. Prompt wording is not a security boundary, and prompt injection is not something you can claim to have eliminated.

## Objectives

- Write a small threat model before adding checks
- Keep untrusted documents from granting tools or roles
- Authorize actions in the application, with least privilege
- Validate tool arguments before execution
- Test injection, cross-user access, secret leakage, and approval bypass with fixtures
- Say which risks remain

## Prerequisites

- Stage 05 tool boundaries: [../05-tool-calling-structured-outputs/README.md](../05-tool-calling-structured-outputs/README.md)
- Stage 06 untrusted memory: [../06-memory-state-management/README.md](../06-memory-state-management/README.md)
- Stage 10 delegation and allow-lists: [../10-multi-agent-systems/README.md](../10-multi-agent-systems/README.md)
- Stage 11 approval is not authorization: [../11-human-in-the-loop/README.md](../11-human-in-the-loop/README.md)
- Stage 13 redaction: [../13-observability/README.md](../13-observability/README.md)
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

Read [CONCEPTS.md](./CONCEPTS.md) before ex-01. [ROADMAP.md](./ROADMAP.md).

## Safety of the exercises

Use synthetic secrets, fake tools, and local strings. Do not point tests at a real account, a real shell, or a network service you do not control.

## Next

[Stage 15](../15-production-ai-infrastructure/README.md) after the checkpoint.
