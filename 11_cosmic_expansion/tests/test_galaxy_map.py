import pytest
from galaxy_map import GalaxyMap


@pytest.fixture
def example_map():
    return GalaxyMap.from_file('../inputs/example.txt', 2)


@pytest.fixture
def large_expansion_example_map():
    return GalaxyMap.from_file('../inputs/example.txt', 1000000)


def test_distance_between_positions(example_map):
    assert example_map.distance_between_positions((1, 6), (5, 11)) == 9
    assert example_map.distance_between_positions((1, 1), (1, 1)) == 0
    assert example_map.distance_between_positions((1, 1), (5, 1)) == 4


def test_get_galaxy_pairs(example_map):
    pairs = example_map.get_galaxy_pairs()
    assert len(pairs) == 36


def test_from_file(example_map):
    assert example_map.width == 13
    assert example_map.height == 12
    assert len(example_map.galaxies) == 9
    assert example_map.galaxies[0] == (4, 0)
    assert example_map.galaxies[1] == (9, 1)


def test_from_file_with_greater_expansion(large_expansion_example_map):
    assert large_expansion_example_map.width == 10 + (1000000 - 1) * 3
    assert large_expansion_example_map.height == 10 + (1000000 - 1) * 2
    assert len(large_expansion_example_map.galaxies) == 9
    assert large_expansion_example_map.galaxies[0] == (3 + (1000000 - 1), 0)
    assert large_expansion_example_map.galaxies[1] == (7 + (1000000 - 1) * 2, 1)
