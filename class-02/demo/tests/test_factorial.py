import pytest
from recursion.factorial import factorial

def test_one():
    actual=factorial(1)
    expected=1
    assert actual == expected

def test_zero():
    actual=factorial(0)
    expected=1
    assert actual == expected

def test_five():
    actual=factorial(5)
    expected=120
    assert actual == expected