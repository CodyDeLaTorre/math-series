import pytest
from series import fibonacci, lucas, sum_series


def test_fib():
    actual = fibonacci(2)
    expected = 1
    assert actual == expected


def test_luc():
    actual = lucas(7)
    expected = 29
    assert actual == expected


def test_sum1():
    actual = sum_series(7, 2, 1)
    expected = 29
    assert actual == expected


def test_sum2():
    actual = sum_series(2)
    expected = 1
    assert actual == expected
