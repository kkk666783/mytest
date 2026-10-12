import pytest


@pytest.fixture
def fruit_basket():
    return ["apple", "banana", "cherry"]


@pytest.mark.parametrize(
    "fruit,expected",
    [
        ("apple", False),
        ("banana", True),
        ("grape", False),
    ],
)
def test_fruit_in_basket(fruit_basket, fruit, expected):
    assert (fruit in fruit_basket) == expected
