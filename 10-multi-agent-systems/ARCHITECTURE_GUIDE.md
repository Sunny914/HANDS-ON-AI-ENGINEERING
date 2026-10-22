# Stage 10 Architecture

```text
caller
  → coordinator (no tools, or only the delegate tool the application implements)
       → role runner (scripted model or live model)
            → tool gateway (allow-list by role)
       ← typed result
  → conflict rule
  → evidence check
  → trace
```

The coordinator is application code. It is not "whatever the model felt like doing." A role runner that can call the coordinator again will recurse. Default: workers return results and do not delegate.

Do not import Stage 09 as a library unless you deliberately version that boundary. Reusing the idea of a budget object and an evidence check is required. Copying a pile of classes is not.
