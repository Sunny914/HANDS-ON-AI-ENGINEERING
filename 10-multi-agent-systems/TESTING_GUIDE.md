# Stage 10 Testing

- Workers are fakes that return fixtures. Default tests do not call a paid model.
- Assert hop counts, not prose quality.
- A delegation test fails if the hop counter can grow without a stop.
- A privilege test sends a handoff that asks for a forbidden tool and asserts the gateway refuses.
- A comparison test runs the same question through a one-agent script and a multi-agent script. Record both traces.
- Parallel tests must not depend on wall-clock order. Use a deterministic scheduler: run ready workers in name order, or inject an executor that records call order.
