from loop_functions import do_positions_connect, find_next_pipe_pos, calculate_loop_length, \
    calculate_furthest_steps_of_loop, determine_start_piece_shape
from .grid_test_fixtures import example_1_grid, example_2_grid, example_3_grid, example_4_grid, example_5_grid
from .loop_test_fixtures import example_1_loop, example_2_loop, example_3_loop, example_4_loop, example_5_loop


def test_determine_grid_loop(example_1_loop):
    assert example_1_loop[0] == (1, 1)
    assert example_1_loop[-1] == (1, 2)
    assert len(example_1_loop) == 8


def test_find_next_pipe_pos(example_1_grid):
    next_from_start = find_next_pipe_pos(example_1_grid, (1, 1))
    assert next_from_start in [(2, 1), (1, 2)]

    next_pos = find_next_pipe_pos(example_1_grid, (2, 1), (1, 1))
    assert next_pos == (3, 1)

    next_pos = find_next_pipe_pos(example_1_grid, (3, 2), (3, 1))
    assert next_pos == (3, 3)


def test_do_positions_connect(example_1_grid):
    # East to West
    assert do_positions_connect(example_1_grid, (1, 1), (2, 1))
    assert not do_positions_connect(example_1_grid, (3, 1), (4, 1))

    # North to South
    assert do_positions_connect(example_1_grid, (3, 1), (3, 2))
    assert not do_positions_connect(example_1_grid, (3, 3), (3, 4))

    # West to East
    assert do_positions_connect(example_1_grid, (2, 3), (1, 3))
    assert not do_positions_connect(example_1_grid, (1, 3), (0, 3))

    # South to north
    assert do_positions_connect(example_1_grid, (1, 2), (1, 1))
    assert not do_positions_connect(example_1_grid, (1, 1), (1, 0))


def test_do_positions_connect_with_bad_inputs(example_1_grid):
    assert not do_positions_connect(example_1_grid, (1, 1), (3, 3))
    assert not do_positions_connect(example_1_grid, (0, 0), (-1, 0))
    assert not do_positions_connect(example_1_grid, (4, 4), (4, example_1_grid.height))


def test_calculate_loop_length(example_1_loop, example_2_loop):
    assert calculate_loop_length(example_1_loop) == 9
    assert calculate_loop_length(example_2_loop) == 17


def test_calculate_furthest_steps_of_loop(example_1_loop, example_2_loop):
    assert calculate_furthest_steps_of_loop(example_1_loop) == 4
    assert calculate_furthest_steps_of_loop(example_2_loop) == 8


def test_determine_start_piece_shape(example_1_loop, example_2_loop, example_3_loop, example_4_loop, example_5_loop):
    assert determine_start_piece_shape(example_1_loop) == 'F'
    assert determine_start_piece_shape(example_2_loop) == 'F'
    assert determine_start_piece_shape(example_3_loop) == 'F'
    assert determine_start_piece_shape(example_4_loop) == 'F'
    assert determine_start_piece_shape(example_5_loop) == '7'
