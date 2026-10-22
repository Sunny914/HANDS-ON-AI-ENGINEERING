# Stage 05 Testing

- Tool functions in unit tests should be fakes: a clock, a ledger, an in-memory charge.
- Pass raw dicts that look like model output, including wrong types and extra keys.
- A permission test uses two principals and one tool.
- An idempotency test calls execute twice with the same key and asserts one side effect.
- The loop test feeds a fixture proposal. It does not require a live model.
- Optional live tool-calling belongs behind `RUN_LIVE_LLM=1`.

Do not assert only that the model "would have" called a tool. Assert that your executor did or did not run.
