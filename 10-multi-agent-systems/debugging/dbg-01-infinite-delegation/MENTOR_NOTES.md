# Mentor notes — dbg-01

`next_worker` always returns `"research"`. `run` never reads `max_hops`. It stops at a hard-coded ceiling of 10000 and still reports `done`.

The repair belongs in the coordinator: stop at the hop limit even if the next-role function misbehaves. Changing only the script, or raising the ceiling, hides the missing guard.
