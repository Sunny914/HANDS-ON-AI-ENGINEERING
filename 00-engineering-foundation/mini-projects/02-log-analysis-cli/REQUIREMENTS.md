# MP2 — Requirements

## Log line format (canonical)

One log entry per line:

```text
<TIMESTAMP> <METHOD> <PATH> <STATUS> <DURATION_MS>ms
```

Example:

```text
2025-03-01T12:00:01Z GET /api/health 200 12ms
2025-03-01T12:00:02Z POST /api/orders 500 340ms
2025-03-01T12:00:03Z GET /api/orders 200 45ms
```

- `TIMESTAMP`: ISO-8601 UTC with `Z` suffix (parse accordingly)
- `STATUS`: integer HTTP status
- `DURATION_MS`: integer before literal `ms`

Malformed lines: skip and count; log warning at WARNING level.

## CLI

```text
logalyze --input path/to.log [--slow-threshold MS] [--output report.txt]
```

Default slow threshold: 300ms (configurable).

## Report metrics (minimum)

| Metric | Description |
|--------|-------------|
| total_requests | Parsed lines count |
| successful_requests | status 200–399 |
| error_requests | status >= 500 |
| warning_count | your app log warnings if present—**or** treat 4xx as warnings; document choice |
| status_distribution | count per status code |
| endpoint_frequency | count per PATH |
| average_response_time_ms | mean duration |
| slow_requests | count and list paths above threshold |
| error_rate | errors / total (define 0 total) |
| requests_per_minute | bucket by minute from timestamp |

## Engineering

- Use generators for line iteration where appropriate
- Type hints on public functions
- Tests per TEST_PLAN.md
- Logging for skipped lines and summary

## Sample data

Create `samples/access.log` yourself for manual testing (not provided intentionally).
