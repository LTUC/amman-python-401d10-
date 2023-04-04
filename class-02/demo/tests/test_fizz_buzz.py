import pytest
from fizz_buzz.fizz_buzz import fizz_buzz

'''
num = 6 -> 6/3 = "fizz"
num = 25 -> 25/5 = "buzz"
num=2 -> "2"
'''

def test_one():
    actual=fizz_buzz(1)
    expected="1"
    assert actual == expected

def test_two():
    actual=fizz_buzz(2)
    expected="2"
    assert actual == expected
    
def test_three():
    actual=fizz_buzz(3)
    expected = "fizz"
    assert actual == expected

def test_four():
    actual=fizz_buzz(4)
    expected= "4"
    assert actual == expected


def test_five():
    actual=fizz_buzz(5)
    expected= "buzz"
    assert actual == expected

def test_six():
    actual=fizz_buzz(6)
    expected= "fizz"
    assert actual == expected

def test_fifteen():
    actual=fizz_buzz(15)
    expected= "fizz buzz"
    assert actual == expected
