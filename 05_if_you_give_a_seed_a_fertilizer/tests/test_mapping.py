import pytest
from mapping import Mapping


@pytest.fixture
def example_mapping():
    return Mapping(10, 20, 5)


def test_map(example_mapping):
    assert example_mapping.map((9, 9)) == ([], [(9, 9)])
    assert example_mapping.map((10, 10)) == ([(20, 20)], [])
    assert example_mapping.map((14, 14)) == ([(24, 24)], [])
    assert example_mapping.map((15, 15)) == ([], [(15, 15)])


def test_from_line():
    m = Mapping.from_line('50 98 2')
    assert m.dest_range_start == 50
    assert m.dest_range_end == 51
    assert m.src_range_start == 98
    assert m.src_range_end == 99
    assert m.range_length == 2
