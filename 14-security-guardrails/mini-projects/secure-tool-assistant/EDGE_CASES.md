# Edge Cases

| Case | Behavior |
|------|----------|
| Document says `role=admin` | Research principal unchanged |
| `skip_approval: true` | Deploy still blocked |
| User B requests user A's id | Body absent |
| Unknown tool | Denied, ledger unchanged |
| Empty allow-list | Denied |
| Extra argument | Rejected if the schema is closed |
| Double deploy execute | One ledger row |
| Secret in nested args | Not in the log |
| Policy file missing | Fail closed |
