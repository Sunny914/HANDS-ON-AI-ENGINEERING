# Stage 09 Debugging

| Symptom | Look at |
|---------|---------|
| Prompt grows every step | Context builder appends the full history and ignores the budget |
| Tool runs after a crash already recorded it | Resume does not read the log |
| Every error retries | Classifier returns one label |
| Answer cites a note you never read | Evidence check missing |
| Graph and loop both call the tool | Two orchestrators wired |

Hypothesis before `MENTOR_NOTES.md`.
