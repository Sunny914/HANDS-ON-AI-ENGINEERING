# Project Debugging

| Symptom | Check |
|---------|--------|
| Every change looks like a regression | Dataset version changed or case ids were rewritten |
| Means improved and a bad citation shipped | Gate reads only the mean |
| Recall is perfect on unlabeled cases | Empty relevant set became 1 |
| Judge-only runs pass CI | Rule result dropped from the report |
| Second process sees an empty report | Report path differs or the file is not flushed |
