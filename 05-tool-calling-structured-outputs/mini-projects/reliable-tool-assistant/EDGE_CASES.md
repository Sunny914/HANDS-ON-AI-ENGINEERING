# Edge Cases

| Case | Behavior |
|------|----------|
| Missing tool name | invalid or unknown, documented |
| Extra argument keys | Document ignore versus reject |
| Guest, own order | ok |
| Guest, other owner's order | denied |
| Support refund at the max | ok |
| Support refund above the max | denied |
| Repeat key | same receipt |
| Repeat key, new amount | conflict, original row remains |
| Tool raises RuntimeError | tool_error result |
| Empty idempotency key | invalid |
