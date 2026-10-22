# Requirements

## Stories

- As an on-call engineer, I open one request id and see every operation.
- As a reviewer, I see a timeout that was later retried.
- As a security reviewer, I do not find a secret in the stored events.

## Functional

- Structured events with request id, operation id, parent id, name, status, and duration.
- Spans for retrieval, model, and tool. Agent step count on the root when the workflow is an agent loop.
- Retry attempts retained.
- Token fields on model events when the fake adapter supplies them. Cost, if present, is an estimate you document.
- Redaction before storage, matching `TELEMETRY.md`.
- A diagnosis function that names the slowest child and any error or timeout.
- One planted problem in a fixture: a slow dependency or a retry that would have been invisible without the trace. `DIAGNOSIS.md` cites event ids.
- File-backed or in-memory store. Tests can read it back.
- Optional export to a vendor is out of scope.

## Nonfunctional

- Injected clock and ids.
- No network in default tests.
- Default debug flag off.

## Non-goals

A hosted dashboard, OpenTelemetry compliance, and a quality score for the answer.
