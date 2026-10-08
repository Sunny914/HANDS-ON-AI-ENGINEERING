# Architecture Guide — Stage 00

This stage trains **architectural intuition**: given requirements, decide where code lives before you write it.

## Core question

> "Where should this code go?"

Wrong answers often "work" in a single file. The goal is a structure that stays clear at 500+ lines.

## Layers (conceptual)

Not every program needs every layer. Choose deliberately.

| Layer | Typical responsibility | Should not |
|-------|------------------------|------------|
| **Entry / CLI / main** | Parse user input, call services, format output | Contain business rules or SQL/file details |
| **Application / service** | Use cases, orchestration, transactions | Know about argparse details |
| **Domain / models** | Data shapes, invariants, pure logic | Read environment variables |
| **Infrastructure / storage** | Files, DB, HTTP, clocks | Encode business policy |
| **Validation** | Shape and constraint checks at boundaries | Hidden inside random helpers |

**Dependency direction:** outer layers depend inward; domain should not import CLI.

## Decision heuristics

### Function vs class

| Prefer functions when | Prefer classes when |
|----------------------|---------------------|
| Stateless transforms | Mutable identity over time |
| Pipeline steps | Multiple operations on same data bundle |
| Small script | Rich invariants on a struct |

### Module boundaries

Split when:

- Two reasons to change (different stakeholders)
- You want to test one part without I/O
- Imports start forming cycles

Keep together when:

- Splitting would require passing 10 parameters
- The code is <30 lines and unlikely to grow

### Configuration

- Load config **once** near entry
- Pass config or explicit dependencies into services
- Avoid `os.environ` scattered in domain logic

### Errors

- Define domain errors (subclass `Exception`) in a small module
- Catch at boundaries (CLI prints user message; logs detail)
- Let unexpected exceptions propagate during development; handle at top level in production-style CLIs

### Logging

- Log at **service** and **infrastructure** boundaries
- CLI may log invocations; avoid logging every line of parsing in hot loops

## Architecture exercise protocol

For `01-python-software-engineering/exercises/architecture/*`:

1. Read requirements only—**do not** open `REFERENCE.md`.
2. Write answers to the 12 checkpoint questions (see [checkpoints/](./checkpoints/) template).
3. Draw a diagram (paper or ASCII): boxes and arrows for data flow.
4. Create your directory structure and implement.
5. Open `REFERENCE.md` and compare—note differences, not "right/wrong" scores.

## Mini-project protocol

Same as above using project `ARCHITECTURE.md` Part A. Complete Part B comparison after implementation.

## Anti-patterns to notice in yourself

- **God module:** one file does everything
- **Utils dumping ground:** `helpers.py` with unrelated functions
- **Primitive obsession:** passing dicts everywhere instead of models
- **Leaky storage:** JSON keys known in CLI strings
- **Test impossible:** logic fused with `print` and `input`

## Review questions (peer or self)

1. Can I add a new command without editing storage code?
2. Can I swap JSON for SQLite later—what would change?
3. Which module would I open first to trace a bug report?

See [IMPLEMENTATION_WORKFLOW.md](./IMPLEMENTATION_WORKFLOW.md) for build order.
