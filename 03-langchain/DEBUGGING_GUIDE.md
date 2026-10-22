# Stage 03 Debugging

| Symptom | Look at |
|---------|---------|
| `KeyError` or missing variable on invoke | Template variables versus the dict you passed |
| Empty completion | Fake model list is empty, or you invoked the prompt and forgot the model |
| Parser always fails | Fence handling, or the fake returns prose |
| Event loop error | Calling blocking `invoke` inside an `async def` that also awaits I/O |
| Import error for `LLMChain` | You followed an old tutorial. Switch to LCEL. |

`MENTOR_NOTES.md` in a debugging exercise is not the first file to open.
