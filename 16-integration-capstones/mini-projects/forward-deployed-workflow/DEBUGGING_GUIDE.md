# Project Debugging


| Symptom | Check |
|---------|--------|
| Queue follows the model | Assignment reads the draft |
| Mail grows on draft | Draft module imports the mail simulator |
| Phantom ticket after timeout | Write happens before the simulator returns |
| Customer B sees A's body | List endpoint skips the owner filter |
| Eval and app disagree | Two different keyword tables |
