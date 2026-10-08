# MP1 — Architecture

## Part A — Design questions (answer before coding)

Use [checkpoint template](../../checkpoints/architecture-before-mini-project-1.md). Do not read Part B until your implementation exists.

1. What is the entry point?
2. What are the main components?
3. What responsibility does each component have?
4. Which component reads data?
5. Which component validates data?
6. Where is business logic?
7. Where is persistence?
8. Where does error handling happen?
9. Where should logging happen?
10. How will the components communicate?
11. What should be tested independently?
12. What dependencies flow in which direction?

Record answers in `checkpoints/your-answers/mp1-architecture.md`.

---

## Part B — Reference architecture (after your implementation)

> One valid layout. Compare tradeoffs with yours.

### Suggested components

| Module | Responsibility |
|--------|----------------|
| `cli` | argparse/subcommands, user messages |
| `service` | Use cases: create/update/delete/list/filter |
| `repository` | Load/save JSON collection |
| `models` | `Task` entity, enums for status/priority |
| `validation` | Parse CLI payloads → models or errors |
| `exceptions` | `TaskNotFound`, `ValidationError`, `StorageError` |
| `config` | Paths, log level |
| `logging_config` | One-time setup |

### Data flow

```text
User → CLI → validation → service → repository → JSON file
                ↓ errors ↑ domain exceptions → CLI message + log
```

### Engineering decisions left to you

- ID type and generation
- Atomic write strategy (temp file + rename recommended)
- Whether repository returns dicts or models

### Dependency rule

`models` and `validation` should not import `cli` or `repository`.
