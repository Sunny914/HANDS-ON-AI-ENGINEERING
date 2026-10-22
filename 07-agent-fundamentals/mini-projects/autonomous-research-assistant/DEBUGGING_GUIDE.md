# Project Debugging

| Symptom | Check |
|---------|--------|
| Trace longer than max_steps | Bound not applied |
| Hang | `while True` without a break you can hit in a test |
| Clean final with a made-up id | Citation check missing |
| Two reads after one timeout | Retry restarted the whole script |
| Send tool ran | You added a tool the principal does not have, or trusted `allow` |
