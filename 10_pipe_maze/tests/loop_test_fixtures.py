import pytest
from loop_functions import determine_grid_loop
from .grid_test_fixtures import example_1_grid, example_2_grid, example_3_grid, example_4_grid, example_5_grid


@pytest.fixture
def example_1_loop(example_1_grid):
    return determine_grid_loop(example_1_grid)


@pytest.fixture
def example_2_loop(example_2_grid):
    return determine_grid_loop(example_2_grid)


@pytest.fixture
def example_3_loop(example_3_grid):
    return determine_grid_loop(example_3_grid)


@pytest.fixture
def example_4_loop(example_4_grid):
    return determine_grid_loop(example_4_grid)


@pytest.fixture
def example_5_loop(example_5_grid):
    return determine_grid_loop(example_5_grid)
