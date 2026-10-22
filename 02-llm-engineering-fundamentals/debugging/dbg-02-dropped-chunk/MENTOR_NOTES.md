# Mentor notes — dbg-02

The loop breaks as soon as it sees a usage event, but it also breaks when a text delta has no trailing space, because `delta.endswith` is checked incorrectly: any delta that does not end with a space is treated as terminal and then the break happens before append. The intended visible bug is a missing final text piece. Do not quote this file in the learner README.
