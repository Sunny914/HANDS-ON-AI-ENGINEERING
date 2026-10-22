# Stage 10 Assumptions

- Python 3.10 or newer, same as earlier stages. The learner's machine may be 3.13.
- No agent framework is required. Do not invent CrewAI, AutoGen, or LangGraph APIs in your notes.
- If you host the coordinator as a LangGraph graph, use the Stage 08 assumptions and confirm any API you call against the installed package. This stage's exercises are plain Python so they stay testable without that package.
- Paid model APIs stay behind an explicit flag such as `RUN_LIVE_LLM=1`. Ordinary tests use scripted role outputs.
- No Redis, no extra database, and no vector store. A JSON or SQLite trace is enough if you need durability.
