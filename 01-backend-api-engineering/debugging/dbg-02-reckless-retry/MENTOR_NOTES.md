# Mentor notes — dbg-02

- No timeout is passed to `httpx.AsyncClient`.
- The loop retries every exception, including HTTP 404.
- A new client is created per attempt, which is wasteful but secondary. The grading bugs are the missing timeout and the undiscriminating retry.
