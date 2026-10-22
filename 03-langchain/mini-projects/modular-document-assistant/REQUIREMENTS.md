# Requirements

- Input: filesystem path, question, and settings (tone, max excerpt characters, model alias).
- Load UTF-8 text. Reject missing files and binary-looking decode errors.
- Select an excerpt without embeddings. Allowed methods: whole file under the cap, or paragraphs that contain a query term. Document the method.
- If the selection is empty, do not call the model.
- Chain: `ChatPromptTemplate` piped to an injected chat model piped to a parser for `{summary: str, confidence: float, used_excerpt: bool}`.
- Confidence is between 0 and 1.
- Public function returns your type, not a raw `AIMessage`.
- Async entry point uses `ainvoke`.
- Tests inject a fake model. Live model is optional behind `RUN_LIVE_LLM`.
- Logs include path and latency, not the full document, at info level.

LCEL only. Do not use `LLMChain`.
