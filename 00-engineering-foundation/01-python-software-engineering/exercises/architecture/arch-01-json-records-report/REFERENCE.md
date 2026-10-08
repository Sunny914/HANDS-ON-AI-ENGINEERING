# arch-01 — Reference Architecture (read after your design)

> Compare, do not copy blindly. Your design may be better if justified.

## Suggested components

| Component | Responsibility |
|-----------|----------------|
| `cli.py` / `__main__.py` | Args, exit codes, print/write report |
| `loader.py` | Read bytes/path → Python data |
| `validation.py` | Record → valid model or validation error |
| `models.py` | `Record` dataclass |
| `reporting.py` | Pure functions: aggregates, top users, format text |
| `service.py` (optional) | Orchestrate load → validate → report |

## Data flow

```text
CLI → loader → validator (per row) → reporting → stdout/file
```

## Dependency direction

`cli` → `service`/`reporting` → `models`  
`loader` → (no domain)  
`validation` → `models`

## Testing focus

- Pure reporting given list of `Record`
- Validation edge cases without filesystem
- One integration test with temp JSON file

## Common learner mistakes vs reference

- Putting JSON key strings inside reporting functions
- No distinction between parse errors and validation errors
