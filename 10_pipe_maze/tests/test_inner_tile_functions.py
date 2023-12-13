from inner_tile_functions import get_inner_tiles_in_row, count_inner_tiles_in_grid

from .loop_test_fixtures import example_1_loop, example_3_loop, example_4_loop, example_5_loop
from .grid_test_fixtures import example_1_grid, example_3_grid, example_4_grid, example_5_grid


def test_get_inner_tiles_in_row(example_3_grid, example_3_loop):
    assert len(get_inner_tiles_in_row(example_3_grid, example_3_loop, 3)) == 0
    assert len(get_inner_tiles_in_row(example_3_grid, example_3_loop, 5)) == 0
    assert len(get_inner_tiles_in_row(example_3_grid, example_3_loop, 6)) == 4


def test_count_inner_tiles_in_grid_1(example_1_grid, example_1_loop):
    assert count_inner_tiles_in_grid(example_1_grid, example_1_loop) == 1


def test_count_inner_tiles_in_grid_3(example_3_grid, example_3_loop):
    assert count_inner_tiles_in_grid(example_3_grid, example_3_loop) == 4


def test_count_inner_tiles_in_grid_4(example_4_grid, example_4_loop):
    assert count_inner_tiles_in_grid(example_4_grid, example_4_loop) == 8


def test_count_inner_tiles_in_grid_5(example_5_grid, example_5_loop):
    assert count_inner_tiles_in_grid(example_5_grid, example_5_loop) == 10
