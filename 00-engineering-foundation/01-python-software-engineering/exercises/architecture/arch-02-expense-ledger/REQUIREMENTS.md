# arch-02 — Requirements

## Domain

Expense entries: `id`, `date` (ISO `YYYY-MM-DD`), `amount` (positive float), `category`, `note` (optional).

## CLI commands (minimum)

- `add --date --amount --category [--note]`
- `list [--category] [--month YYYY-MM]`
- `summary --month YYYY-MM` (totals per category)
- `export --output path.csv`

## Persistence

JSON file path from env `LEDGER_PATH` or default `./ledger.json`.

## Rules

- IDs unique; reject duplicate on add
- Amount must be > 0
- Dates must parse as ISO dates

## Tests

Repository tests with temp file; service tests with fake repo optional.
