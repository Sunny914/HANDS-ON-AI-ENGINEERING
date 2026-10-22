# Mentor notes — dbg-03

`allowed` reads `args["role"]` and ignores the `principal` parameter. The guest passes `role=support` inside the model payload.
