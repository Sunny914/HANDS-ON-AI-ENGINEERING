# Stage 02 Testing

- Fixtures are JSON files of provider responses. Parse them in tests.
- A fake provider returns a scripted response or raises a scripted timeout.
- Do not call a paid API from the default test command.
- Assert on your normalized response: text, finish reason, token counts. Do not assert on a vendor header unless the test is specifically for that adapter.
- For streams, feed a list of chunks. Assert the joined text and the usage event.
- A fallback test should show the primary was attempted and the secondary produced the text.

Optional live tests belong behind an environment variable such as `RUN_LIVE_LLM=1` and must skip when the key is absent.
