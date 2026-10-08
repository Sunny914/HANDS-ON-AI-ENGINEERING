"""Tests pass but do not match intended behavior — fix product and/or tests."""

from app.math_ops import divide


def test_divide():
    assert divide(10, 2) == 5


def test_divide_by_zero():
    assert divide(1, 0) == 0
