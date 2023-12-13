import pytest
from pipe_grid import PipeGrid


@pytest.fixture
def example_1_grid():
    return PipeGrid.from_file('../inputs/example1.txt')


@pytest.fixture
def example_2_grid():
    return PipeGrid.from_file('../inputs/example2.txt')


@pytest.fixture
def example_3_grid():
    return PipeGrid.from_file('../inputs/example3.txt')


@pytest.fixture
def example_4_grid():
    return PipeGrid.from_file('../inputs/example4.txt')


@pytest.fixture
def example_5_grid():
    return PipeGrid.from_file('../inputs/example5.txt')
