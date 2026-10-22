# Stage 08 — LangGraph

A graph is the Stage 07 loop with named nodes, explicit state, and a place to pause. Learn the state machine before you learn the library, then use LangGraph for routing, loops, checkpoints, and interrupts.

## Objectives

- Model state and transitions without a framework
- Build a small `StateGraph` with conditional edges
- Keep reducers from surprising you
- Bound a cycle
- Resume a thread from a checkpoint
- Put side effects where a resume will not repeat them by accident
- Test a node without running the whole graph

## Prerequisites

- Stage 07 control loop and stop reasons
- Stage 06 state schemas
- [ASSUMPTIONS.md](./ASSUMPTIONS.md)
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). ex-01 is required before ex-02. The project starts after [arch-01](./architecture-exercises/arch-01-what-is-a-node/README.md).

## Next

[Stage 09](../09-single-agent-engineering/README.md).
