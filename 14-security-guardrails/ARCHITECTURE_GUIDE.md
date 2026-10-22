# Stage 14 Architecture

```text
untrusted text and model proposal
  → schema validation
  → authorizer (principal, tool, resource)
  → policy (approval required?)
  → fake executor
  → audit and redacted log
```

The proposal has no function pointer to the executor. Retrieved documents are passed in as data and are not concatenated into the authorizer's rules.
