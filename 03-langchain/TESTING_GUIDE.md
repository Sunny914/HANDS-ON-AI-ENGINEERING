# Stage 03 Testing

- Inject the model or the runnable. Do not construct a live chat model in the test that runs by default.
- Assert on the string or the parsed object your function returns.
- A prompt test can `invoke` the template alone and inspect message content. That does not need a model.
- Parser tests can feed an `AIMessage` you construct.
- One integration test should run prompt, fake model, and parser together.
- If you add a live test, gate it with `RUN_LIVE_LLM=1` and skip otherwise.
