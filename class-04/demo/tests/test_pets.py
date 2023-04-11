from pets import (Pet, Cat, Dog)
import pytest

# ptes count
def test_pets_count(data) :
    expected = 4
    actual = Pet.get_pets_count()
    assert expected == actual

#Cats are Purring
def test_cat_purr(data):
    expected = "cat is purring!!!"
    actual1 = data[0].purr()
    actual2 = data[1].purr()

    assert actual1 == expected
    assert actual2 == expected

#Dog age
def test_dog_age(data):
    assert data[2].age == 2
    assert data[3].age == 3

# python fixture
@pytest.fixture
def data():
    cat1 = Cat("cat1",1,"British","black")
    cat2 = Cat("cat2",2,"American", "white")
    dog1 = Dog("Dog1",2,"American")
    dog2 = Dog("Dog1",3,"American")
    return [cat1, cat2, dog1, dog2]
