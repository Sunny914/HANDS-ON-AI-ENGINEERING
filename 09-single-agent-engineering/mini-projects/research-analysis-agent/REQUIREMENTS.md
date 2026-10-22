# Requirements

## Stories

- As a user, I ask a question and receive a structured analysis with evidence ids and a stop reason.
- As an operator, I rerun after a crash and successful reads are not repeated.
- As a reviewer, I can see why this is one agent.

## Functional

- Layers from ex-01. Names are yours.
- Tools: search, read, and a notes scratch that does not leave the task. No shell. No open web.
- Scripted model by default. Live model only behind `RUN_LIVE_LLM`.
- Memory: optional preferences through the Stage 06 policy. Research notes for the task are working state, not durable user memory, unless the user asked to remember them.
- Budget object: steps, time, tokens.
- Recovery via step log or a graph checkpoint. The ADR says which.
- Idempotent search and read within a task.
- Evidence check from ex-07.
- Trace includes tool name, status, and whether a call was skipped.
- Authorization: a fixed researcher principal. Proposal fields do not add tools.

## Nonfunctional

- Offline default tests.
- Info logs: task id, stop reason, tool names. Not full note text.
- One request at a time. Document concurrency as out of scope.

## Non-goals

A team of agents, human approval, and a public web crawler.
