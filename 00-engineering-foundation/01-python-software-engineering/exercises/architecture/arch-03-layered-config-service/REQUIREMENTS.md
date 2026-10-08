# arch-03 — Requirements

## Input

CSV with header: `email,name,department`

## Behavior

1. Load settings (log level, paths) from env + optional config file.
2. Import CSV, skip malformed rows with warning logs.
3. Deduplicate by `email` (case-insensitive); keep last occurrence.
4. Write JSON report: `{ "count": N, "by_department": { ... } }` to configured output path.

## Engineering requirements

- Custom exception types for config and storage
- Logging configured once at startup
- No single file over ~400 lines (refactor if needed)

## Tests

- Dedupe logic unit tests
- Integration with tmp CSV + output JSON
