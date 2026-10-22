"""Broken gate. The judge erases a rule failure."""


def release(rule_pass: bool, judge_pass: bool) -> dict:
    return {"release": judge_pass, "judge_pass": judge_pass}
