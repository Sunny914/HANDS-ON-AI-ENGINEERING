# MP1 — Test Plan (you implement tests)

## Unit tests

- Validation: invalid status, priority, empty title
- ID generation uniqueness (if applicable)
- Service logic without touching real filesystem (inject repository fake)

## Repository tests

- Round-trip save/load
- Missing file behavior
- Corrupt JSON raises expected domain/storage error

## Integration tests

- Full flow: create → list → update → delete using temporary data path
- Filter queries return correct counts

## CLI tests (optional but recommended)

- Invoke via subprocess with env var for data path
- Assert stdout contains task title or exit code on error

## Regression

- Add one test for a bug you fixed during development (comment which bug)

## Coverage goal

Not measured by tooling required—focus on seams between layers.
