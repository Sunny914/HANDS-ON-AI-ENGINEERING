# Stage 16 Architecture

Each capstone README names the boundaries. Common shape:

```text
HTTP or CLI edge
  → application service
       → domain policy (authz, approval, or workflow rules)
       → adapters (corpus, tickets, model) behind fakes
  → trace and eval report
```

The edge does not import a vendor SDK. The policy does not trust model fields for roles or approval.
