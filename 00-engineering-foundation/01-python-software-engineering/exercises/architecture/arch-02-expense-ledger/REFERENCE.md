# arch-02 — Reference Architecture (after your design)

## Layers

| Layer | Role |
|-------|------|
| CLI | Parse subcommands, map errors to messages |
| Service | Add/list/summary/export use cases |
| Repository | JSON read/write, ID generation policy |
| Models | `Expense` dataclass + invariants |

## ID policy (example)

Monotonic int stored in metadata section of JSON or UUID string—pick one and document.

## Export

Service returns rows; CLI or `csv_writer` module writes CSV—keep CSV formatting out of service if possible.

## Error handling

| Error | Layer raises | CLI shows |
|-------|--------------|-----------|
| Duplicate id | `DuplicateExpense` | user message |
| Invalid date | `ValidationError` | user message |
| IO failure | `StorageError` | log + generic message |
