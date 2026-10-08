# Module 01 — Python Software Engineering

Move from single-file scripts to **engineered** Python: packages, typing, advanced language features, configuration, logging, testing, architecture, and debugging.

## Concepts first

[CONCEPTS.md](../CONCEPTS.md) Module 01 section.

## Tracks

| Track | Path | Count |
|-------|------|-------|
| Core progression | [exercises/ex-01](./exercises/ex-01/README.md) → ex-12 | 12 |
| Architecture | [exercises/architecture/](./exercises/architecture/) | 3 |
| Testing | [exercises/testing/](./exercises/testing/) | 5 |
| Debugging | [exercises/debugging/](./exercises/debugging/) | 5 |

**Suggested order:** ex-01 → ex-09, then testing test-01 → test-03, ex-10 → ex-12, test-04 → test-05, architecture arch-01 → arch-03, debugging dbg-01 → dbg-05, finally ex-12 integration capstone reread.

## Core exercise index

| ID | Title |
|----|-------|
| ex-01 | Pure validation functions |
| ex-02 | Multi-function text utilities module |
| ex-03 | Package layout: `textstats` |
| ex-04 | Dataclass domain models |
| ex-05 | Type hints and static reasoning |
| ex-06 | Custom iterator |
| ex-07 | Generator-based line processing |
| ex-08 | Timing decorator |
| ex-09 | Context manager for temporary state |
| ex-10 | Configuration from env + file |
| ex-11 | Logging policy across modules |
| ex-12 | Custom exceptions + service boundary |

## Architecture exercises

| ID | Title |
|----|-------|
| arch-01 | JSON records → validated report |
| arch-02 | Expense ledger CLI |
| arch-03 | Layered service with config |

Each includes `REFERENCE.md` (unlock after your design).

## Testing exercises

Specifications only—you write tests under `tests/`. Implement minimal product code where the README requires it.

## Debugging exercises

Broken starters in `broken/` or `app/`. Read exercise README first; hints in local `HINTS.md` (H1/H2/H3).

## Progression goal

```text
single function → module → package → service/storage split → config → logging → tests → refactor
```

## Module exit

[CHECKPOINT.md](../CHECKPOINT.md) Module 01 gate before mini-projects (architecture checkpoints mandatory).
