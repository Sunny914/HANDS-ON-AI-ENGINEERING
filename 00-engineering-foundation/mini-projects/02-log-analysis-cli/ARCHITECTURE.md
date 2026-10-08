# MP2 — Architecture

## Part A — Design questions (before coding)

Answer all 12 questions in [checkpoint](../../checkpoints/architecture-before-mini-project-2.md). Save to `checkpoints/your-answers/mp2-architecture.md`.

Do not read Part B until your code works.

---

## Part B — Reference architecture (after implementation)

### Suggested components

| Module | Role |
|--------|------|
| `cli` | Args, invoke pipeline, write report |
| `parser` | Line → `LogRecord` or None (generator) |
| `models` | `LogRecord`, `Summary` dataclasses |
| `aggregator` | Consume records, compute metrics |
| `reporter` | Format summary for stdout/file |
| `config` | Thresholds, paths |
| `exceptions` | `ParseError` if you use explicit errors |

### Data flow

```text
file → iter_lines (generator) → parse_line → aggregator.consume → summary → reporter
```

### Why generators

Keeps memory stable; aggregator can run online (single pass) for many metrics.

### Test seams

- Pure `parse_line(line)`
- Pure `aggregate(records)` or incremental `Aggregator` class
- Reporter given frozen `Summary`

### Your decisions

- Whether 4xx counts as success or warnings
- Whether to keep slow request list capped (top N)
