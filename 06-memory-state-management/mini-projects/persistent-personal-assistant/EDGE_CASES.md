# Edge Cases

| Case | Behavior |
|------|----------|
| Empty remember text | Reject |
| Duplicate forget | Documented no-op or not-found |
| Expired row | Not retrieved |
| Older write arrives late | Does not beat a newer preference |
| Budget smaller than one memory | Omit it. Do not slice the string into nonsense unless you document that |
| Clock moves backward | Do not crash. Document the timestamp you trust |
| Two processes | Out of scope. Say so |
