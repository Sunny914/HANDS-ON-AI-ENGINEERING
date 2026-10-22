# Stage 13 Architecture

```text
clock and ids
  → tracer (start, finish, fail)
  → redactor
  → event store
  → query by request id
  → tiny aggregates
```

Application code calls the tracer. The tracer does not call the model. Tests inject the clock and the id generator so two runs match.

An exporter to a file is the default. A network exporter is out of scope unless you mark it optional and keep the file path tested.
