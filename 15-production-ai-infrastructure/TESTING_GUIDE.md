# Stage 15 Testing

- Config tests do not require a real key in fake mode.
- Health tests flip a dependency flag.
- Retry tests count adapter calls and use a fake sleeper.
- Concurrency tests use a barrier or a counter, not a timed sleep as the assertion.
- The default suite does not build a container. The project smoke milestone does, and it can be skipped with a documented env flag only if Docker is unavailable. Say so in the report. Do not skip it silently on a machine where Docker works.
