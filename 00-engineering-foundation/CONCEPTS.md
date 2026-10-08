# Stage 00 — Concepts to Understand

Use this as a **readiness checklist**, not a course catalog. If a concept is unfamiliar, study it briefly (official docs, REPL experiments), then attempt the linked exercises.

## Module 00 — Python engineering reset

Understand before starting `00-python-engineering-reset/`:

| Concept | Why it matters here |
|---------|---------------------|
| Values, types, operators | Correct modeling in ex-01–05 |
| Strings (immutable, methods, formatting) | Parsing and reporting |
| list, tuple, set, dict semantics | Choosing the right structure |
| Comprehensions | Clear transformations without noise |
| `if` / `for` / `while`, boolean logic | Control flow exercises |
| Functions, parameters, return | Decomposition |
| `*args`, `**kwargs`, defaults | API design mistakes in ex-08–09 |
| LEGB scope, `global`/`nonlocal` (sparingly) | Debugging scope bugs |
| Mutable vs immutable, references | Mutation exercises |
| `copy` vs deep copy | Shared state bugs |
| Exceptions: try/except/else/finally, raise | Robust I/O |
| Files: text mode, paths, `with` | ex-11–12 |
| `json.load` / `json.dump` | Config and persistence preview |
| `import`, packages, `__name__ == "__main__"` | ex-13+ |
| Classes, `__init__`, methods, `@staticmethod` | ex-21 |

## Module 01 — Python software engineering

Understand before starting `01-python-software-engineering/`:

| Concept | Why it matters here |
|---------|---------------------|
| Package layout, absolute vs relative imports | Multi-module exercises |
| Separation of concerns | Architecture exercises |
| When functions beat classes (and vice versa) | Design exercises |
| `@dataclass`, fields, defaults | Models |
| Type hints, `Optional`, collections | Contracts between modules |
| Protocols / structural subtyping (conceptual) | Testing with fakes |
| Iterator protocol, `yield` | Streaming data |
| Decorators (functions wrapping functions) | Cross-cutting behavior |
| Context managers and `contextlib` | Resource safety |
| Config: files + environment variables | 12-factor habits |
| `logging` levels, handlers, loggers | Operations |
| Custom exception hierarchies | API clarity |
| `venv`, `pip`, `requirements.txt` or `pyproject.toml` | Reproducible env |
| pytest: discovery, asserts, parametrize, fixtures | Testing track |
| Mocking: patch boundaries, not internals | test-05 |
| Git branches, commits, diff | [GIT_WORKFLOW.md](./GIT_WORKFLOW.md) |
| Debugger: breakpoints, watch, stack | [DEBUGGING_GUIDE.md](./DEBUGGING_GUIDE.md) |

## Module 02 — Async preview

Understand before starting `02-async-python-preview/`:

| Concept | Why it matters here |
|---------|---------------------|
| CPU-bound vs I/O-bound | Why threads/async differ (preview only) |
| Blocking call | ex-01 |
| `async def`, `await`, event loop | ex-02–04 |
| `asyncio.create_task`, `gather` | Concurrency |
| Timeouts and cancellation (intro) | ex-04 |
| Sequential vs concurrent wall-clock | ex-05–06 |

## Mini-projects

| Concept | Applied in |
|---------|------------|
| CLI design (args, subcommands) | MP1, MP2 |
| Persistence format and atomic writes | MP1 |
| Validation at boundaries | MP1 |
| Parsing pipelines, generators | MP2 |
| Aggregation and reporting | MP2 |
| Test pyramid for CLIs | Both |

## Depth standard

You are ready to leave Stage 0 when you can **explain** these without notes:

1. Where validation lives vs business logic vs I/O  
2. How an exception propagates from storage to CLI  
3. What your tests would break if you merged two modules blindly  

If not, repeat one architecture exercise and one debugging exercise before the final checkpoint.
