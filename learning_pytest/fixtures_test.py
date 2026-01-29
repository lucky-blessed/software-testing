from fixtures import sample_list, sample_dict # type: ignore

def test_list(sample_list):
    assert 5 in sample_list


def test_sample_dict(sample_dict):
    assert sample_dict["name"] == "Bryan"
    assert sample_dict["age"] == 30