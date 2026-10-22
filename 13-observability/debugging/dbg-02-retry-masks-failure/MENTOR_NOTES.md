# Mentor notes — dbg-02

`summarize` keeps only `attempts[-1]`. Earlier timeouts disappear, so the retry count stays 0.

Keep the full list. `retry_count` is the number of attempts after the first, or the number of failed attempts that were retried. Pick one, document it, and test the timeout-then-ok case.
