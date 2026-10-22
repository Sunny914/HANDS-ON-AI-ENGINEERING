# Mentor notes — dbg-01

`execute` passes the raw dict into `refund` and never constructs `RefundArgs`. The model exists and is unused. The learner instructions do not say that.
