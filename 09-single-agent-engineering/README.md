# Stage 09 — Single-Agent Engineering

Put the loop, the tools, the memory policy, and the trace into one system with boundaries. A single agent is a product decision. You will write down why you are not using several agents yet.

## Objectives

- Separate application, loop, tools, memory, and storage
- Enforce a budget object the loop cannot ignore
- Resume from a step log after a crash
- Keep tool calls idempotent
- Judge a result by evidence, not by a fluent paragraph
- Write an architecture decision for staying with one agent

## Prerequisites

- Stage 06 memory policy
- Stage 07 loop and traces
- Stage 08 nodes, only where a graph helps. A plain loop is still allowed if the design says so.
- Stage 05 authorization
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). [arch-01](./architecture-exercises/arch-01-single-agent-adr/README.md) comes before the project.

## Next

[Stage 10](../10-multi-agent-systems/README.md).
