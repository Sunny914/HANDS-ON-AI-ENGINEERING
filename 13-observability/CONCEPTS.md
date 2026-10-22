# Stage 13 Concepts

## Four words

| Word | What it is | What it is not |
|------|------------|----------------|
| Log | A record of something that happened, meant for a person or a search | A metric |
| Event | A structured log with a name and fields | A paragraph |
| Metric | A number you can aggregate: count, latency, tokens | One request's story |
| Trace | A tree of operations that share an id | A single log line |

Debugging is what you do with that evidence. Evaluation is a scored dataset. A trace can feed both. It does not replace either.

## Identifiers

A request id identifies the user-facing call. An operation id identifies one model call, retrieval, tool call, or agent step. `parent_id` points at the operation that started this one. The root has an empty parent.

If two operations share no id, you cannot honestly say they are the same request. Generating a new random id inside a tool without copying the parent is how traces fall apart.

## What to time

Record start and end, or a duration in milliseconds from an injected clock. Model latency, retrieval latency, and tool latency are different series. A retry is another operation linked to the same parent, with an attempt number. It is not a silent second try that overwrites the first error.

Token counts and a cost estimate are fields when you have them. A fake adapter can stamp fixture numbers. Do not invent a vendor price table. Document the formula if you estimate cost, and call it an estimate.

## Metrics worth plotting

Counts of requests, failures, model calls, tool calls, retries, and timeouts. Latency you can summarize later with min, max, and a simple percentile over the events you stored. Agent step count and budget exhaustion are labels on the root. Queue depth matters only if you have a queue. Do not add one so the dashboard looks finished.

## Health

Liveness means the process can answer. Readiness means it can do useful work, including reaching a dependency you care about. A live process with a dead database is not ready. Stage 15 uses this in an HTTP service. Here, a function that returns `live` or `ready` is enough.

## Privacy

Do not store raw secrets, full prompts, or document bodies by default. Store ids, lengths, statuses, and hashes if you need to correlate. Redact values that look like keys before write. A debug flag may keep a short excerpt in local development. Production-shaped tests keep the flag off.

Sampling means keeping only some traces. It saves cost and can hide the one failure you needed. For these exercises, keep every event. Mention sampling as a later trade-off.

## Diagnosis

A slow request is a tree. Add the durations. The largest child is the first place to look. A retry storm is many attempts with errors and a final status that might still say success. Read the attempts. Do not stop at the root status.

OpenTelemetry, Phoenix, or a vendor agent are optional exporters of the same events. This stage does not require their SDKs. If you adopt one later, map your event fields to it instead of rewriting the system around the product.
