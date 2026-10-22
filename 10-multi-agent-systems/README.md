# Stage 10 — Multi-Agent Systems

Several model-backed workers are a coordination system. They add handoffs, duplicated context, and new ways to fail. This stage teaches you to build that system and to refuse it when a workflow or one agent is enough.

## Objectives

- Define roles, inputs, and outputs before anyone delegates
- Choose among a workflow, one agent, and several agents for a specific task
- Bound delegation so a worker cannot spawn workers forever
- Resolve conflicting specialist results with an explicit rule
- Keep tool permissions on the application, not inside a worker message
- Compare a multi-agent run with a single-agent baseline on the same fixtures

## Prerequisites

- Stage 09 layers, budgets, and evidence checks: [../09-single-agent-engineering/README.md](../09-single-agent-engineering/README.md)
- Stage 07 stopping conditions: [../07-agent-fundamentals/README.md](../07-agent-fundamentals/README.md)
- Stage 05 tool authorization: [../05-tool-calling-structured-outputs/README.md](../05-tool-calling-structured-outputs/README.md)
- Stage 06 memory is untrusted data: [../06-memory-state-management/README.md](../06-memory-state-management/README.md)
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read [CONCEPTS.md](./CONCEPTS.md) before ex-03. The architecture choice is part of the stage, not an afterthought.

## What this stage does not require

No extra agent framework. A supervisor can be ordinary Python plus scripted workers. LangGraph is allowed only if your design says a graph is the coordinator. Do not add a second SDK to look current.

## Next

[Stage 11](../11-human-in-the-loop/README.md) after the checkpoint.
