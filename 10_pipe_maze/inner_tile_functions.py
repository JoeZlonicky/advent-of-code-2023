from pipe_grid import PipeGrid, GridPos
from loop_functions import determine_start_piece_shape, Loop


def count_inner_tiles_in_grid(grid: PipeGrid, loop: Loop) -> int:
    inner_tiles = []
    for y in range(grid.height):
        inner_tiles.extend(get_inner_tiles_in_row(grid, loop, y))

    return len(inner_tiles)


# Use scanline fill technique by keeping track of odd vs. even # of intersections
def get_inner_tiles_in_row(grid: PipeGrid, loop: Loop, y: int) -> list[GridPos]:
    start_shape = determine_start_piece_shape(loop)
    loop = [piece for piece in loop if piece[1] == y]  # Only look at pieces that matter

    intersections = 0
    inner_tiles = []
    enter_inner_x = -1
    last_vertical_char = ''

    for x in range(grid.width):
        pos = (x, y)
        if pos not in loop:
            continue

        char = grid.get_char(pos)
        if char == 'S':
            char = start_shape

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
            enter_inner_x = x
        elif enter_inner_x > 0 and char in ['|', 'L', 'F']:
            for i in range(enter_inner_x + 1, x):
                inner_tiles.append((i, y))
            enter_inner_x = -1

    return inner_tiles
