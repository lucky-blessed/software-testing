import pytest
from exception import divide

def test_divide():
    assert divide(10, 2) == 5

    with pytest.raises(ValueError):
        divide(10, 0)