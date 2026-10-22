# Edge Cases

| Case | Behavior |
|------|----------|
| Empty body | Rejected |
| Two keywords | Document which queue wins |
| Model returns a queue name | Ignored for assignment |
| Approval of a different hash | No send |
| CRM timeout then success | One ticket row |
| CRM timeout forever | Bounded attempts, no phantom row |
| Restart | Ticket and pending send still there, mail unchanged until execute |
