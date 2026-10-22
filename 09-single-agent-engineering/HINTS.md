# Stage 09 Hints

## ex-01

- **H1:** A layer owns one kind of change.
- **H2:** Write interfaces: `ToolRunner`, `MemoryStore`, `Orchestrator`, `Model`. They can be protocols or small classes with no bodies yet.
- **H3:** A test uses fakes for all four and asserts the orchestrator called the tool runner, not the store, for a search.

## ex-02

- **H1:** Memory rows enter through the Stage 06 builder, not through string pasting in the loop.
- **H2:** The loop asks a context function before each model step.
- **H3:** Pass a tiny budget and assert a memory id was omitted. The system text stays stable.

## ex-03

- **H1:** Remaining amounts live in one object.
- **H2:** `before_step()` raises or returns a reason when any remaining counter is zero.
- **H3:** Decrement steps in that object. The loop stops with the reason the object reports. A test spends steps and then time.

## ex-04

- **H1:** The log is the source of truth after a crash, not the in-memory trace that died.
- **H2:** Persist each successful tool result before the next step. On start, load it.
- **H3:** Second service instance skips a logged read. A logged timeout may retry. Test both.

## ex-05

- **H1:** The idempotency key is the tool name plus canonical arguments plus the task id.
- **H2:** Store the key next to the result.
- **H3:** Two calls return one side effect. A changed argument is a new key.

## ex-06

- **H1:** One test, one question, one script, one expected stop.
- **H2:** Build the service in a factory that takes the model script and the corpus.
- **H3:** Assert trace tool names and the final citation ids. No network.

## ex-07

- **H1:** Evidence is a set intersection.
- **H2:** Compare cited ids to ids observed in the trace.
- **H3:** If the model final cites an extra id, status is `unsupported`, not `done`.

## arch-01

- **H1:** Write the decision after you list two alternatives.
- **H2:** Alternatives: fixed workflow, one agent. Multi-agent is a future option you are rejecting for this corpus.
- **H3:** Consequences: one trace, one budget, no handoff schema. That is the point.

## arch-02

- **H1:** A graph is worth it when you need checkpoints or a cycle you want drawn.
- **H2:** Say which you pick for the project and what you lose.
- **H3:** If you pick the loop, say how you still persist the step log. If you pick the graph, say which nodes stay thin.

## dbg-01

- **H1:** Measure the context size after three steps.
- **H2:** The budget argument is unused.
- **H3:** Stop adding messages when the next one would exceed the budget. Keep the pinned system text.

## dbg-02

- **H1:** List the labels you expected for not-found and timeout.
- **H2:** The function ignores the status.
- **H3:** Return `retry` only for timeout. Return `stop` for not-found.
