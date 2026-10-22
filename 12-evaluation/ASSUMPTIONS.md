# Stage 12 Assumptions

- No eval vendor SDK is required. This file does not claim those products' APIs were checked.
- Precision@k, recall@k, and F1@k use the definitions in [CONCEPTS.md](./CONCEPTS.md). Other libraries sometimes divide precision by the number of returned ids instead of by k. Do not swap definitions silently.
- A live model judge is optional and stays behind a flag such as `RUN_LIVE_LLM=1`. Ordinary tests do not call it.
- Stage 04's hit@k remains valid. This stage does not replace that exercise.
