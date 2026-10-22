# Edge Cases

| Case | Behavior |
|------|----------|
| Empty corpus | Search returns no ids. Partial or a documented empty answer |
| Read unknown id | Not-found, no retry loop |
| Final before any tool | Reject or allow. Document it. A research answer with no evidence should not look successful if you required citations |
| max_steps 0 | No tool runs |
| Same search, different query | Not a repeat |
| Script shorter than the budget | `script_exhausted` or final, whichever happened |
