# MP2 — Acceptance Criteria

## Functional

- [ ] Correct totals on a hand-crafted log file (≥20 lines)
- [ ] Malformed lines skipped; warning logged; count visible in report or logs
- [ ] Status distribution sums to total_requests
- [ ] Slow request detection respects threshold flag
- [ ] error_rate matches documented formula
- [ ] Time bucketing groups by UTC minute

## Engineering

- [ ] Parser separated from aggregation/reporting
- [ ] Generator-based line reading (not `readlines()` on whole file required)
- [ ] pytest suite passes
- [ ] Typed public API for parser and summary model

## Documentation

- [ ] README: run command, assumptions, 4xx handling policy
- [ ] Architecture checkpoint completed and compared to Part B
