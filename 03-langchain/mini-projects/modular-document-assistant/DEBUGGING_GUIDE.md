# Project Debugging

| Symptom | Check |
|---------|--------|
| Missing variable exception | Invoke keys versus template |
| Empty summary that still counts as success | Parser swallowed the error |
| Test called the network | Factory default constructs `init_chat_model` |
| Whole file in the log | Info log includes the excerpt |
| Stage 04 comparison feels identical | You added embeddings. Remove them from this project. |
