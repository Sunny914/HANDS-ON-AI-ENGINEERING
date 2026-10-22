# Stage 08 Assumptions

Checked on 2026-10-21 against public LangGraph docs and the PyPI metadata for `langgraph`. LangGraph was not installed in that environment, so none of these names were imported. If an import fails on your machine, use the installed docs. Do not copy an old tutorial that builds the graph with a prebuilt ReAct helper as the only path.

## Confirmed from public docs, not from a local import

- `StateGraph`, `START`, and `END` are shown as imports from `langgraph.graph`. One interrupt example also imports `START` from `langgraph.constants`.
- `compile(checkpointer=...)` takes a checkpointer. A `thread_id` under `config["configurable"]` selects the thread.
- `InMemorySaver` is imported from `langgraph.checkpoint.memory` in the graph API docs. `MemorySaver` is imported from the same module in the checkpoint reference. This audit did not prove they are aliases.
- Both are in-memory. Process death drops them.
- `interrupt` and `Command` are in `langgraph.types`.
- Resume after `interrupt()` re-enters the node from the beginning. Code before `interrupt()` runs again. Resume that call with `Command(resume=...)`.
- `interrupt_before` and `interrupt_after` are documented on `compile`. The interrupts guide says to resume those static breakpoints with `invoke(None, config)`, not with `Command(resume=...)`. It also says static breakpoints are for debugging, and human approval should use `interrupt()`.
- `add_messages` is documented as `from langgraph.graph.message import add_messages`.

## PyPI metadata observed the same day

- Latest `langgraph` release reported by PyPI: 1.2.16.
- That release requires Python `>=3.10` and `langgraph-checkpoint>=4.3.0,<5.0.0`.
- `requirements.txt` allows `langgraph>=1,<2`, which includes 1.2.16. It does not pin 1.2.16.

## Still unverified here

- No package was installed or imported for this audit.
- `SqliteSaver` is documented in the separate distribution `langgraph-checkpoint-sqlite`, imported from `langgraph.checkpoint.sqlite`. PyPI showed 3.1.2 for that distribution, with a `langgraph-checkpoint` range that overlaps the range declared by `langgraph` 1.2.16. This audit did not install either package, so the optional SQLite exercise still starts by confirming the import locally. Postgres is not required.
- `create_react_agent` and similar prebuilt helpers are out of scope. You already built a loop in Stage 07.
