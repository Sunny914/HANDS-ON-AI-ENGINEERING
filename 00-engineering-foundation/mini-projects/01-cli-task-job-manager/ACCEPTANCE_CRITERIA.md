# MP1 — Acceptance Criteria

## Functional

- [ ] Create task returns id; list shows it after restart
- [ ] Update modifies `updated_at` and persisted fields
- [ ] Delete removes task; subsequent show/list reflects change
- [ ] Filters return correct subsets
- [ ] Invalid priority/status rejected with message, non-zero exit optional
- [ ] Missing task id handled gracefully

## Engineering

- [ ] At least 4 modules/packages beyond `tests/`
- [ ] No business rules embedded only in print statements
- [ ] Configuration for data file path and log level
- [ ] pytest suite passes locally
- [ ] README documents install/run/test commands

## Documentation

- [ ] You can answer all 12 architecture checkpoint questions for your implementation
- [ ] Part B comparison notes in ARCHITECTURE.md or separate file

## Quality bar

A reviewer can trace: CLI command → service → storage → file without you explaining line-by-line.
