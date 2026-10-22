# Stage 01 Testing

Repo-wide habits: [LEARNING_PROTOCOL.md](../LEARNING_PROTOCOL.md).

## Two kinds of tests

| Kind | Use it for | Do not use it for |
|------|------------|-------------------|
| Unit | Retry decisions, pagination math, schema rules, services with fakes | Binding a real port every time |
| API | Status code, error body, auth rejection, one happy path through the app | Re-testing every branch of a pure function |

Use FastAPI's `TestClient` for API tests, or `httpx.ASGITransport` if you are already on an async test style. Either is acceptable. Document which you chose.

## Fakes

- Repository fake: dict in memory
- Upstream fake: function that returns a fixture or raises a timeout
- Do not mock the function you are testing

## Minimum for the mini-project

- Pure tests for retry and idempotency decisions
- One API test that a second request with the same idempotency key does not create a second upstream call
- One test that an upstream timeout becomes a controlled error, not a hang
