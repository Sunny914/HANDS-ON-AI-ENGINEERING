# Stage 08 Testing

- Call a node function with a state dict and assert the partial update. That does not require a graph.
- Compile a graph with `InMemorySaver` for routing and interrupt tests.
- Use a new `thread_id` per test unless the test is about resume.
- Assert the sequence of node updates or the final state, not a screenshot of logs.
- A cycle test must fail if the counter never increments.
- Do not call a paid model. Fake nodes return fixtures.
