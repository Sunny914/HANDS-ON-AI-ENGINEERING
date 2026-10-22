# Stage 15 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** Invalid configuration is a startup bug, not a request bug.
- **H2:** Parse an env mapping into an object. `APP_MODE` must be `fake` or `live`. Live requires `API_KEY`. Fake must not.
- **H3:** A test passes a dict, not the real environment. Missing mode raises. Fake without a key returns the object. Assert the key value is not in the exception text.

## ex-02

- **H1:** Live means the process answers. Ready means dependencies are usable.
- **H2:** Two functions, or two routes, reading a dependency object with `up`.
- **H3:** When `store.up` is false, ready is false and live is true. When it is true, both are true.

## ex-03

- **H1:** A retry without a cap is a loop.
- **H2:** Retry timeout and 503 only, at most twice after the first try. Other errors return immediately. Pass a sleeper that records delays.
- **H3:** A stub that always times out is called three times and then returns a named error. A validation error is called once.

## ex-04

- **H1:** Degradation may change availability. It may not change authorization.
- **H2:** If the adapter raises unavailable, a local read can return a stored note. `deploy` still returns denied or unavailable and does not write the ledger.
- **H3:** Test both paths with the adapter forced down. The deploy counter stays 0.

## ex-05

- **H1:** The error body the client sees should carry the request id you logged.
- **H2:** Middleware or a wrapper assigns the id, puts it on the response, and passes it to the logger.
- **H3:** Raise inside the handler. Assert the response includes the same id the log event stored. Do not include the stack in the client body.

## ex-06

- **H1:** A limit is a counter or a semaphore around the adapter call.
- **H2:** When two calls are in flight, the third gets a named busy error or waits. Document which. Tests should not depend on wall-clock speed.
- **H3:** Use an async or threaded barrier only if you can join it. A simpler version: a fake adapter checks a counter you increment around the call and rejects when it would exceed 2.

## ex-07

- **H1:** Shutdown is a state the server checks between units of work.
- **H2:** A flag `draining` rejects new calls. An in-flight fake call is allowed to store its idempotent result, then the flag stops the next one.
- **H3:** Start one call, set draining, finish that call, assert the result was stored, and assert a new call is rejected.

## arch-01

- **H1:** A container is a packaging choice, not a quality proof.
- **H2:** Write what the image contains, what it refuses to contain, and how config arrives. Include a smoke command and a rollback step.
- **H3:** Non-root user. No `API_KEY` in the image. `APP_MODE=fake` for the smoke test. Previous tag is the rollback. Kubernetes stays in a "not now" sentence.

## dbg-01

- **H1:** Both routes should not share one boolean.
- **H2:** See what happens when the dependency flag is false.
- **H3:** Return ready false when the dependency is down. Leave live true.

## dbg-02

- **H1:** Count calls to the stub.
- **H2:** The loop has no attempt limit.
- **H3:** Stop after a fixed max. A test that always fails must return and must not call the stub more times than the max.
