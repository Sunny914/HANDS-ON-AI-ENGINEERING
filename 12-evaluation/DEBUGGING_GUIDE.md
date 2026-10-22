# Stage 12 Debugging

| Symptom | Look at |
|---------|---------|
| Precision rises when results get worse | Hits counted from the non-relevant ids |
| Recall is 1.0 on a case with no relevant ids | Division by zero treated as success |
| Answer score reported as retrieval quality | One field reused for two questions |
| A failed citation still releases | Judge result replaced the rule |
| Two reports "regressed" after you edited labels | Dataset version was not changed |

Hypothesis first. `MENTOR_NOTES.md` is for after you have one.
