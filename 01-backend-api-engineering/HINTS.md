# Stage 01 Hints

Stop at the first level that helps. H4 is a review of your code and is not written here.

## ex-01

- **H1:** The caller needs a machine-readable class, not only a message string.
- **H2:** A function from `(status_code, method)` to a small enum is enough.
- **H3:** Group 429 and 503 as temporary. Group 400, 401, 404, and 422 as caller errors. Leave 500 as unexpected.

## ex-02

- **H1:** A resource is a noun the client can point at later.
- **H2:** Write the path, method, status, and body for create, get, list, and conflict. Do not invent handlers yet.
- **H3:** Use `/sync-jobs` and `/sync-jobs/{id}` as the nouns if you are stuck naming them.

## ex-03

- **H1:** The route is an adapter over a dictionary or service.
- **H2:** One module for the app, one for the in-memory store, until ex-05 forces a split.
- **H3:** Return 201 on create and 404 from get when the id is absent. Keep the store behind a function the route calls.

## ex-04

- **H1:** Pydantic should reject the shape before your business rule runs.
- **H2:** Separate "malformed JSON" from "qty must be positive".
- **H3:** Put the positive-qty rule in a `field_validator` or in the service, and test both the model and the route once.

## ex-05

- **H1:** Settings and loggers are process-wide. Request data is not.
- **H2:** `APIRouter` for the resource. A `get_settings` dependency. Logging configured in the entry module.
- **H3:** Load a dataclass or Pydantic settings object from environment variables once, then `Depends` it.

## ex-06

- **H1:** A missing timeout makes the event loop wait on one peer.
- **H2:** Wrap `httpx.AsyncClient` in a small client object the service can receive.
- **H3:** Pass `timeout=` when constructing the client. Translate `httpx.TimeoutException` into an error your service already names.

## ex-07

- **H1:** Retry is a policy. Transport is something else.
- **H2:** Keep the decision function pure. The loop that sleeps can call it.
- **H3:** Signature idea: `should_retry(method, status, attempt, limit, idempotent) -> bool`. Default `idempotent` to false for POST.

## ex-08

- **H1:** Pagination is a contract about slices, not about dumping a table.
- **H2:** Compute offset from page and page size in one function. The repository applies it.
- **H3:** Reject page < 1 and page_size outside 1..100 with 422. An empty slice is 200 with an empty list.

## ex-09

- **H1:** The route should not know column names if the service speaks in records.
- **H2:** Repository methods: add, get, list. Service calls them. Tests can use a temporary SQLite file.
- **H3:** Open the connection in the repository, commit on success, and close it on the way out. Do not leave a connection on the app object without a lifecycle.

## ex-10

- **H1:** Authentication answers who is calling. Authorization answers what they may do. This exercise is only a shared-secret bearer check.
- **H2:** A dependency reads the `Authorization` header and compares it to settings. Routes opt in.
- **H3:** Missing header is 401. A unit test calls the dependency with a fake header. An API test uses `TestClient` and checks 401 versus 200.

## arch-01

- **H1:** Draw the request before you name files.
- **H2:** Four boxes are enough: HTTP, service, repository, upstream client.
- **H3:** Write the function names the service exposes. Stop before creating the files.

## arch-02

- **H1:** Idempotency is remembered work. Retry is a second attempt.
- **H2:** The key is checked in the service, before the upstream call. The retry policy never stores keys.
- **H3:** On a repeated key, return the stored result and do not call upstream again.

## dbg-01

- **H1:** Look at the status code the client receives, not only the message.
- **H2:** Find the handler that runs for every exception.
- **H3:** Expected HTTP failures need their own status. A catch-all that returns 200 hides them.

## dbg-02

- **H1:** Some failures are permanent for this request.
- **H2:** Compare the timeout argument with the `except` clause.
- **H3:** Stop retrying when the status is a caller error. Set a timeout on the client.

## dbg-03

- **H1:** Two requests should not share a shopping list.
- **H2:** Find an object created once and appended to on every call.
- **H3:** Create the per-request collection inside the request path, or store rows in the repository.
