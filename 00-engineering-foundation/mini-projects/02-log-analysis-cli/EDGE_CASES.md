# MP2 — Edge Cases

| Case | Guidance |
|------|----------|
| Empty file | Zero totals, no crash |
| Only malformed lines | total 0, error_rate defined |
| Duplicate lines | Count each line |
| Missing `ms` suffix | Malformed |
| Negative duration | Malformed or clamp—document |
| Status non-numeric | Malformed |
| Path with spaces | Out of scope unless you extend format |
| Files > 100MB | Streaming required; do not load all |
| Wrong timezone in timestamp | Reject or parse as UTC only—document |
| 4xx responses | Classify as success, warning, or own bucket—document in README |
