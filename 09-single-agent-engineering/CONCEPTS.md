# Stage 09 Concepts

## Layers

| Layer | Changes when |
|-------|----------------|
| Tools | A corpus or API changes |
| Memory policy | What you store changes |
| Loop or graph | Control flow changes |
| Model adapter | The provider changes |
| Application service | The user-facing result changes |

Stage 07 proved a loop. Stage 08 proved a graph. This stage picks one orchestration style in an ADR and keeps the other pieces swappable.

## Budgets

A budget is an object with remaining steps, time, and tokens. The loop asks it before every model or tool call. Returning the budget in the result makes tests obvious.

## Recovery

A step log is a list of completed tool calls and observations. After a crash, a new process loads the log and does not repeat a call that already has a result, unless the result was a retryable failure you have not exhausted.

That is different from a LangGraph checkpoint, which restores graph state. You may use either. The requirement is: a second process can continue without repeating a successful read. Document which mechanism you used.

## Evidence

The analysis cites ids that tools returned. A fluent answer with no ids is a failed run, not a partial success, unless the stop reason says you never found evidence.

## Evaluation here

You are not building Stage 12's harness. You are checking one run: expected ids present, forbidden tools absent, stop reason correct, budget not exceeded.
