# Stage 13 Testing

- Assert on event fields, not on log prose.
- Inject the clock. Do not sleep to measure latency.
- A redaction test puts a fake secret in a payload and asserts it is absent from the stored JSON.
- A diagnosis test loads a fixture trace and names the slowest operation.
- No live tracing vendor.
