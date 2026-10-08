# test-02 — Test Requirements

Implement:

- `divide(a, b)` returns float; raises `ZeroDivisionError` when b is 0
- `parse_ratio(text)` expects `"num/denom"`; raises `ValueError` on bad format or zero denom

## Tests required

- Happy path divide
- divide by zero
- parse_ratio valid
- parse_ratio missing slash
- parse_ratio zero denominator
- parse_ratio non-numeric parts
