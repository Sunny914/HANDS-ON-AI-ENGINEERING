# Requirements

- One request type: messages, model alias, sampling settings, timeout, metadata request id.
- Model alias `small` maps to a primary and a fallback provider name via configuration, not via `if vendor ==` scattered in callers.
- Normalized response: text, provider name, model name, token counts, latency, estimated cost.
- Streaming method that yields text deltas and finishes with usage. Fakes must be able to stream.
- Ledger of attempts, including failed ones.
- Retry temporary failures. Do not retry caller errors.
- Fallback only after the primary's retries are exhausted because of temporary failures.
- Structured-output helper reuses the Stage exercise idea: validate JSON into a caller-supplied Pydantic model. Invalid model output is an error, not a second silent call, unless you document one repair attempt.
- Configuration from the environment for any live key. Default tests pass with no keys.
- Logging of request id, provider, latency, and token counts. Do not log full prompts in the default info level.

Nonfunctional: no paid call in `pytest` by default. Document `RUN_LIVE_LLM` if you add an optional integration.
