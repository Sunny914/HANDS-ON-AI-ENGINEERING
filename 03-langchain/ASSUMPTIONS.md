# Stage 03 Assumptions

Checked on 2026-10-21:

- LangChain 1.x is the stable track. The changelog's then-current patch was 1.4.x. Minor versions may move. Stay on `langchain>=1,<2` and `langchain-core>=1,<2`.
- Python 3.10 or newer is required by current LangChain releases. 3.13 is fine if your pins install.
- `LLMChain` is deprecated and scheduled to leave in 2.0. Default instruction is LCEL.
- Fake chat model class names must be confirmed in your installed `langchain_core`. This scaffold does not pin one class name as eternal.
- No API key is required for the stage.
