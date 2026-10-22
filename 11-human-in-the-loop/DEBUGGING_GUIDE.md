# Stage 11 Debugging

| Symptom | Look at |
|---------|---------|
| Submit already changed the ledger | Executor called on the propose path |
| Approved text differs from executed text | Executor used a live object instead of the snapshot |
| Second click sends twice | Idempotency key not stored |
| Expired approval still runs | Clock not compared to expiry |
| Requester can approve a deploy | Same principal allowed on both sides |
| Audit has a proposal and no execution row | Log write skipped after the tool |
| Resume runs the tool before the human answers | Pending status not checked |

Hypothesis first. `MENTOR_NOTES.md` is for after you have one.
