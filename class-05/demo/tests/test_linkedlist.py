import pytest
from linkedlist import LinkedList

# Test empty linked list
def test_empty_ll():
    ll = LinkedList()
    expected = "Empty LinkeList"
    actual = str(ll)
    assert expected == actual

# Test appending 3 nodes
def test_append_three_nodes(ll):
    expected = "5 --> Roaa --> 2.5 -->  None"
    actual = str(ll)
    assert expected == actual

@pytest.fixture
def ll():
    ll = LinkedList()
    ll.append(5)
    ll.append("Roaa")
    ll.append(2.5)
    return ll