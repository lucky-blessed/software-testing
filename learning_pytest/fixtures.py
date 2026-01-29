import pytest


# This is a decorator
@pytest.fixture

def sample_list():
    return [1, 2, 3, 4, 5]


@pytest.fixture
def sample_dict():
    return {"name": "Bryan", "age": 30}
