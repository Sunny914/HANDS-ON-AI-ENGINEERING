# Stage 07 Testing

- Script the model. Do not call a provider in the default suite.
- Assert on the trace: tool names, count, and stop reason.
- A test that would hang needs a step ceiling. If your code ignores it, the test should fail because the trace is too long, not because the test killed the process. Keep the broken examples finite.
- Repeat-action tests use the same arguments twice.
- Partial-result tests use a script that never says finish.
