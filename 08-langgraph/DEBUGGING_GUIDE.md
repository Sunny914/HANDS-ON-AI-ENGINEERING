# Stage 08 Debugging

| Symptom | Look at |
|---------|---------|
| Always the same node | Conditional function returns one name on every branch |
| List field keeps only the last write | Missing reducer, or you replaced the list |
| Resume lost the state | Different thread id, or no checkpointer |
| Ledger doubled after approval | Work ran before `interrupt` and the node restarted |
| Graph never ends | Cycle edge has no counter check |

`MENTOR_NOTES.md` comes after a hypothesis.
