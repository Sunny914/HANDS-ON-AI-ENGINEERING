# MP2 — Test Plan

## Parser unit tests

- Valid line → structured record
- Each malformed variant (missing field, bad status, bad duration)
- Edge timestamp at minute boundary

## Aggregator unit tests

- Known small list of records → expected metrics
- error_rate when total=0
- slow threshold boundary (299 vs 300 ms)

## Integration

- Temp file with mixed valid/invalid lines → report sections match
- Generator memory: optional test with many lines (can mock iterator)

## Golden snippet

- Store a 5-line log fixture in `tests/fixtures/` you create; assert key numbers in report text or structured summary object

## Regression

- One test tied to a bug you fixed while building
