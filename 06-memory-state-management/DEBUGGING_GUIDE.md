# Stage 06 Debugging

| Symptom | Look at |
|---------|---------|
| Only the last fact remains | Replace versus merge |
| Fact missing after restart | Write never flushed, or a new path was opened |
| Summary answer loses a preference | Selector dropped the message that held it |
| Two users share rows | Missing owner id on the query |
| Model follows a memory as an order | Context builder did not label it as data |

Write the row you expected before you change the prompt. Debugging starters are broken on purpose. Hypothesis before `MENTOR_NOTES.md`.
