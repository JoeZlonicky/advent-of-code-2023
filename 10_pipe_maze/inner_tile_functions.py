from pipe_grid import PipeGrid, GridPos
from loop_functions import determine_start_piece_shape, Loop


def count_inner_tiles_in_grid(grid: PipeGrid, loop: Loop) -> int:
    inner_tiles_in_rows = []
    for y in range(grid.height):
        inner_tiles_in_rows.extend(get_inner_tiles_in_row(grid, loop, y))

    inner_tiles = []
    for x in range(grid.width):
        inner_tiles_in_column = get_inner_tiles_in_column(grid, loop, x)
        inner_tiles.extend(tile for tile in inner_tiles_in_column if tile in inner_tiles_in_rows)

    return len(inner_tiles)


def get_inner_tiles_in_row(grid: PipeGrid, loop: Loop, y: int) -> list[GridPos]:
    intersections = 0
    row = grid.rows[y]
    loop_pieces_in_row = [piece for piece in loop if piece[1] == y]
    inner_tiles = []
    enter_i = -1
    last_vertical_char = ''
    for x in range(len(row)):
        pos = (x, y)
        if pos not in loop_pieces_in_row:
            continue

        char = grid.get_char(pos)
        if char == 'S':
            char = determine_start_piece_shape(loop)

        if char == '-':
            continue

        if char == '|':
            intersections += 1

        elif char == 'J' and last_vertical_char == 'F':
            intersections += 1
        elif char == '7' and last_vertical_char == 'L':
            intersections += 1

        if char != '|':
            last_vertical_char = char

        if char in ['|', 'J', '7'] and intersections % 2 != 0:
            enter_i = x
        elif enter_i > 0 and char in ['|', 'L', 'F']:
            for i in range(enter_i + 1, x):
                inner_tiles.append((i, y))
            enter_i = -1

    return inner_tiles


def get_inner_tiles_in_column(grid: PipeGrid, loop: Loop, x: int) -> list[GridPos]:
    intersections = 0
    loop_pieces_in_column = [piece for piece in loop if piece[0] == x]
    inner_tiles = []
    enter_i = -1
    last_horizontal_char = ''
    for y in range(grid.height):
        pos = (x, y)
        if pos not in loop_pieces_in_column:
            continue

        char = grid.get_char(pos)
        if char == 'S':
            char = determine_start_piece_shape(loop)

        if char == '|':
            continue

        if char == '-':
            intersections += 1

        elif char == 'J' and last_horizontal_char == 'F':
            intersections += 1
        elif char == 'L' and last_horizontal_char == '7':
            intersections += 1

        if char != '-':
            last_horizontal_char = char

        if char in ['-', 'J', 'L'] and intersections % 2 != 0:
            enter_i = y
        elif enter_i > 0 and char in ['-', 'F', '7']:
            for i in range(enter_i + 1, y):
                inner_tiles.append((x, i))
            enter_i = -1

    return inner_tiles
