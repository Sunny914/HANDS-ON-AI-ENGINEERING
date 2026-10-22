# Stage 11 — Human-in-the-Loop Automation

Some actions should pause until an authorized person approves the exact action. Approval is a workflow control. It does not authenticate the caller, and it does not replace validation.

## Objectives

- Classify actions by risk and decide which ones pause
- Persist a pending action that survives a process restart
- Separate the requester, the approver, and the executor
- Execute only the approved snapshot, after a fresh check
- Make execution idempotent and auditable
- Treat model output as a proposal, never as an approval

## Prerequisites

- Stage 05 tool authorization: [../05-tool-calling-structured-outputs/README.md](../05-tool-calling-structured-outputs/README.md)
- Stage 06 persistence and untrusted text: [../06-memory-state-management/README.md](../06-memory-state-management/README.md)
- Stage 08 interrupts, if you use a graph: [../08-langgraph/README.md](../08-langgraph/README.md). A plain state machine is enough for the exercises.
- Stage 09 budgets and traces: [../09-single-agent-engineering/README.md](../09-single-agent-engineering/README.md)
- [../LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md)

## Sequence

[ROADMAP.md](./ROADMAP.md). Read [CONCEPTS.md](./CONCEPTS.md) before ex-01. The project uses fake local tools only.

## What this stage does not do

No real email, no real deployment, no payment, and no production identity provider. Identity is a named principal in the request plus a role table you define. That is enough to test separation of duties.

## Next

Stage 12 is scaffolded as specifications. Those files are not finished work, and they do not mean this checkpoint is done. Open [../12-evaluation/README.md](../12-evaluation/README.md) only after these answers match code you wrote.
