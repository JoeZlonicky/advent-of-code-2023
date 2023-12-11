import math

NON_PIPE_CHARS = ['.']
START_CHAR = 'S'
NORTH_PIPE_CHARS = ['S', '|', 'L', 'J']
EAST_PIPE_CHARS = ['S', '-', 'L', 'F']
SOUTH_PIPE_CHARS = ['S', '|', '7', 'F']
WEST_PIPE_CHARS = ['S', '-', 'J', '7']


def parse_grid_from_file(file_name) -> list[list[str]]:
    with open(file_name) as f:
        return [list(line.strip()) for line in f]


def find_char_in_grid(grid: list[list[str]], search_char: str) -> tuple[int, int]:
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == search_char:
                return x, y
    return -1, -1


# Returns the loop of positions
# The start pos is only included once (at the start)
def determine_grid_loop(grid: list[list[str]], start_pos: tuple[int, int]) -> list[tuple[int, int]]:
    loop = [start_pos]
    past_pos = start_pos
    current_pos = find_next_pipe_pos(grid, start_pos)
    while current_pos != start_pos:
        loop.append(current_pos)
        current_pos_before = current_pos
        current_pos = find_next_pipe_pos(grid, current_pos, past_pos)
        past_pos = current_pos_before
    return loop


def calculate_loop_length(loop) -> int:
    return len(loop) + 1


def find_next_pipe_pos(grid: list[list[str]], current_pos: tuple[int, int], ignore_pos: tuple[int, int] = (-1, -1)) -> \
        tuple[int, int]:
    x, y = current_pos
    potential_positions = [(x + 1, y), (x - 1, y), (x, y + 1), (x, y - 1)]
    potential_positions = [pos for pos in potential_positions if
                           pos != ignore_pos and do_positions_connect(grid, current_pos, pos)]

    assert len(potential_positions) > 0
    if grid[y][x] == START_CHAR:
        assert len(potential_positions) == 2
    else:
        assert len(potential_positions) == 1

    return potential_positions[0]


# first_pos is expected to be a pipe in a valid position
# second_pos will be verified to be a valid pipe that connects
def do_positions_connect(grid: list[list[str]], first_pos: tuple[int, int], second_pos: tuple[int, int]) -> bool:
    x1, y1 = first_pos
    x2, y2 = second_pos

    if y2 < 0 or y2 > len(grid) - 1:
        return False
    if x2 < 0 or x2 > len(grid[y2]) - 1:
        return False

    first_char = grid[y1][x1]
    second_char = grid[y2][x2]

    if second_char in NON_PIPE_CHARS:
        return False

    is_left = x1 - x2 == 1
    is_right = x2 - x1 == 1
    is_up = y1 - y2 == 1  # Y increases downwards
    is_down = y2 - y1 == 1
    is_horizontal = is_left or is_right
    is_vertical = is_up or is_down
    if not (is_horizontal or is_vertical) or (is_horizontal and is_vertical):
        return False

    if is_left:
        return first_char in WEST_PIPE_CHARS and second_char in EAST_PIPE_CHARS
    if is_right:
        return first_char in EAST_PIPE_CHARS and second_char in WEST_PIPE_CHARS
    if is_down:
        return first_char in SOUTH_PIPE_CHARS and second_char in NORTH_PIPE_CHARS
    if is_up:
        return first_char in NORTH_PIPE_CHARS and second_char in SOUTH_PIPE_CHARS

    return False


def calculate_furthest_steps_of_loop(loop: list[tuple[int, int]]) -> int:
    length = calculate_loop_length(loop)
    return int(math.ceil(length / 2) - 1)
