# arch-01 — Requirements

## Input JSON schema

Array of objects:

```json
{
  "id": "string",
  "category": "string",
  "amount": "number",
  "user": "string"
}
```

## Behavior

1. Load JSON from path provided via CLI argument.
2. Validate each record; invalid records collected with reasons (do not crash entire run unless configured—your choice, document it).
3. Compute:
   - Total amount per `category`
   - Top 3 users by total spend (tie-break by user name ascending)
4. Write human-readable report to stdout and optional `--output path`.

## Non-functional

- Tests for validation and aggregation logic
- Logging at INFO for skipped invalid records

## Acceptance table

| Scenario | Expected |
|----------|----------|
| Valid file | Report with category totals and top users |
| Empty array | Report shows zeros / empty sections clearly |
| Invalid amount type | Record skipped or run fails—document choice |
| Missing file | Non-zero exit, clear message |
