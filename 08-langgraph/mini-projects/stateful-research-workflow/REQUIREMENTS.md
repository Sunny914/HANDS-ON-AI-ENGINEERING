# Requirements

## Stories

- As a user, I submit a question and a thread id and later read the same run's state.
- As a user, I see a partial result when the collect loop hits its max.
- As a tester, I inject a failed collect and see a recorded failure instead of a hang.

## Functional

- Explicit state schema: question, evidence ids, loop count, status, errors, final summary.
- Nodes you justify. A starting set is validate, collect, assess, synthesize, finalize. Merge only with a reason.
- Conditional routing and a bounded cycle.
- Local corpus tools from Stage 07, called by nodes, not reimplemented as prompts.
- Fake model only where a node needs text. Most nodes should be deterministic.
- Checkpointer with thread ids. In-memory is required. Document that it is not durable. SQLite is optional.
- A failed collect is visible on state and routes to a failure or finalize path. One retry is allowed if you document it.
- Streaming or a list of step names is required so a test can see order. Use the library's stream API if you confirm it, or return the trace on state if you document why.
- No human approval in this project. Leave a comment in the design for where Stage 11 would interrupt.

## Nonfunctional

- Default tests do not need a paid API or Postgres.
- Node unit tests exist for scoring or validation.
- Graph tests use fresh thread ids except the resume test.

## Non-goals

Multi-agent handoffs, production Postgres, and approval UX.
