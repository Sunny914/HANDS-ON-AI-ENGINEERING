# Stage 09 Architecture

```text
service → orchestration → tools
              ↓
           memory policy → store
              ↓
           trace and step log
```

Orchestration may be the Stage 07 loop or a Stage 08 graph. It does not open files itself. The service does not parse vendor JSON.

An ADR answers: why one agent, why this orchestration, what you will not add.
