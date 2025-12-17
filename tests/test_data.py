from baseml.data_loader import load_data


def test_load_data():
    assert load_data() is True