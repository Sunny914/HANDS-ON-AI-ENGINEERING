# Stage 08 Concepts

## Before LangGraph

A graph is a set of nodes and a rule for which node runs next. The state is the only data they share. If you cannot write that rule as a function of state, the library will not invent a good one.

ex-01 is that function. Later exercises move the same idea into LangGraph.

## What the library is for

Checked against LangChain's LangGraph docs on 2026-10-21. Confirm imports in your install. See [ASSUMPTIONS.md](./ASSUMPTIONS.md).

- `StateGraph` holds nodes and edges.
- `START` is the entry. You add edges to an end name the docs call `END`.
- Conditional edges call your function and return the next node name.
- `compile(checkpointer=...)` turns the builder into a runnable graph.
- A `thread_id` in `config["configurable"]` selects which checkpoint to load.
- `InMemorySaver` or `MemorySaver` keeps checkpoints in RAM. They vanish when the process exits. A SQLite checkpointer is the local durable option. Do not require Postgres here.

This sketch is not an exercise solution. It only shows the objects:

```text
builder = StateGraph(YourState)
builder.add_node("step", step_fn)
builder.add_edge(START, "step")
graph = builder.compile(checkpointer=in_memory)
graph.invoke(initial, {"configurable": {"thread_id": "t1"}})
```

You still write `step_fn` and `YourState`.

## Reducers

If a node returns a list field, the default update may replace the list. A reducer, often an annotation on that field, says "append" or "add messages" instead. Docs fetched on 2026-10-21 show `from langgraph.graph.message import add_messages`. Confirm that import in your install. If it fails, record the import you tried and use a local reducer you understand.

## Interrupts

`interrupt(value)` from `langgraph.types` pauses the run. You need a checkpointer and a thread id. Resume with `Command(resume=...)` from `langgraph.types`, using the same thread id.

The node **starts again from the top** when you resume. Code before `interrupt` runs twice. Side effects such as charging, sending, or appending a ledger row do not belong before the interrupt. Put them after you have the human's decision, or make them idempotent.

Static `interrupt_before` / `interrupt_after` on `compile` pause at node boundaries. The interrupts guide shows those breakpoints resuming with another `invoke(None, config)` on the same thread. That path does not supply a return value for `interrupt()`. `Command(resume=...)` is the resume path for `interrupt()`. Prefer `interrupt()` when the human must approve an exact payload.

## What stays ordinary Python

Parsing files, scoring a fixture, and validating a schema can be plain functions a node calls. The node should be thin. A graph that exists only to call one function is ceremony.
