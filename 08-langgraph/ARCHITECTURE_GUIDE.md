# Stage 08 Architecture

```text
validate → plan → collect ⇄ assess → synthesize → check → end
```

Not every arrow should exist on day one. A cycle needs a counter in state and an edge that leaves the cycle.

| Node kind | Belongs in the graph | Stays a plain function |
|-----------|----------------------|------------------------|
| Route on state | Yes | |
| Call a fake model | Thin node | The script itself |
| Parse a note file | | Yes, called by a node |
| Append evidence | Reducer or explicit list update | |
| Pause for a human | Interrupt node | The decision record |

Side effects sit after a decision, not before a pause.
