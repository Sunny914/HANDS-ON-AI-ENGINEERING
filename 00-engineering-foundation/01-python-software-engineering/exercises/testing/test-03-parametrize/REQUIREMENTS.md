# test-03 — Test Requirements

Use your email validator from ex-01 (copy module or import if colocated).

## Parametrized cases (minimum)

| email | valid |
|-------|-------|
| user@example.com | true |
| missing-at.com | false |
| @no-local.com | false |
| empty string | false |
| user@host | your documented rule |

One parametrized test function; optional separate test for rule documentation in docstring.
