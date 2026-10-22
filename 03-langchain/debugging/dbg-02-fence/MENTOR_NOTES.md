# Mentor notes — dbg-02

`strip_fence` only removes a fence when the string starts with exactly ``` and the body is sliced poorly: it does not allow a language tag, and it searches for a closing fence with a condition that never strips the tag line. The sample begins with ```json.
