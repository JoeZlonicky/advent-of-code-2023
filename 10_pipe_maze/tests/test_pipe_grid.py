from .grid_test_fixtures import example_1_grid


def test_find_char(example_1_grid):
    assert example_1_grid.find_char('S') == (1, 1)


def test_get_char(example_1_grid):
    assert example_1_grid.get_char((0, 3)) == '-'


def test_is_pos_in_grid(example_1_grid):
    assert not example_1_grid.is_pos_in_grid((-1, 0))
    assert example_1_grid.is_pos_in_grid((0, 0))
    assert not example_1_grid.is_pos_in_grid((2, example_1_grid.height))
    assert example_1_grid.is_pos_in_grid((example_1_grid.width - 1, example_1_grid.height - 1))


def test_from_file(example_1_grid):
    assert example_1_grid.rows[0] == list('-L|F7')
    assert len(example_1_grid.rows) == 5
    assert example_1_grid.start_pos == (1, 1)
