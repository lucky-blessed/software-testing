import pytest
from functions import add, subtract # type: ignore

def test_add():
    result = add(2, 3)
    assert result == 5

def test_subtract():
    result = subtract(5, 3)
    assert result == 2