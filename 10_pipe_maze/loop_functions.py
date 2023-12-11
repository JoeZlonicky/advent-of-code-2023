import math
from pipe_grid import PipeGrid, GridPos

NON_PIPE_CHARS = ['.']
START_CHAR = 'S'
NORTH_PIPE_CHARS = ['S', '|', 'L', 'J']
EAST_PIPE_CHARS = ['S', '-', 'L', 'F']
SOUTH_PIPE_CHARS = ['S', '|', '7', 'F']
WEST_PIPE_CHARS = ['S', '-', 'J', '7']

type Loop = list[GridPos]


# Returns the loop of positions
# The start pos is only included once (at the start)
def determine_grid_loop(grid: PipeGrid) -> Loop:
    loop = [grid.start_pos]
    past_pos = grid.start_pos
    current_pos = find_next_pipe_pos(grid, grid.start_pos)
    while current_pos != grid.start_pos:
        loop.append(current_pos)
        current_pos_before = current_pos
        current_pos = find_next_pipe_pos(grid, current_pos, past_pos)
        past_pos = current_pos_before
    return loop


def find_next_pipe_pos(grid: PipeGrid, current_pos: GridPos, ignore_pos: GridPos = (-1, -1)) -> GridPos:
    x, y = current_pos
    potential_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]

    next_positions = [pos for pos in potential_positions if
                      pos != ignore_pos and do_positions_connect(grid, current_pos, pos)]

    assert len(next_positions) > 0
    if grid.get_char(current_pos) == START_CHAR:
        assert len(next_positions) == 2
    else:
        assert len(next_positions) == 1

    return next_positions[0]


# first_pos is expected to be a pipe in a valid position
# second_pos will be verified to be a valid pipe that connects
def do_positions_connect(grid: PipeGrid, first_pos: GridPos, second_pos: GridPos) -> bool:
    if not grid.is_pos_in_grid(second_pos):
        return False

    first_char = grid.get_char(first_pos)
    second_char = grid.get_char(second_pos)

    if second_char in NON_PIPE_CHARS:
        return False

    x1, y1 = first_pos
    x2, y2 = second_pos

    if x1 - x2 == 1:  # Left
        return first_char in WEST_PIPE_CHARS and second_char in EAST_PIPE_CHARS
    if x2 - x1 == 1:  # Right
        return first_char in EAST_PIPE_CHARS and second_char in WEST_PIPE_CHARS
    if y2 - y1 == 1:  # Down
        return first_char in SOUTH_PIPE_CHARS and second_char in NORTH_PIPE_CHARS
    if y1 - y2 == 1:  # Up
        return first_char in NORTH_PIPE_CHARS and second_char in SOUTH_PIPE_CHARS

    return False


def calculate_loop_length(loop) -> int:
    return len(loop) + 1


def calculate_furthest_steps_of_loop(loop: Loop) -> int:
    length = calculate_loop_length(loop)
    return int(math.ceil(length / 2) - 1)


def determine_start_piece_shape(loop: Loop) -> str:
    x1, y1 = loop[1]
    x2, y2 = loop[-1]
    if abs(x1 - x2) == 2:
        return '-'
    if abs(y1 - y2) == 2:
        return '|'
    if x1 > x2:
        return 'F' if y1 < y2 else 'L'
    return '7' if y1 < y2 else 'J'
