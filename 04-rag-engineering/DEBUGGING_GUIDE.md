# Stage 04 Debugging

| Symptom | Look at |
|---------|---------|
| Words from the source disappear | Chunk loop drops a tail or an overlap |
| Irrelevant chunk always wins | Threshold comparison is reversed, or the fake embedder ignores the text |
| Filter does nothing | Filter applied after you already truncated to k |
| Citations point at the wrong id | Context builder reorders and the ids stay in the old order |
| Postgres test hangs | No skip, and Docker is not running |
| Answer ignores the question | The prompt never received the chunk text |

Write the chunk ids you expected before you change the generator.
