from collections import defaultdict
from grid import Grid

WALL_CHAR = '#'
OPEN_CHAR = '.'
NORTH_SLOPE_CHAR = '^'
EAST_SLOPE_CHAR = '>'
SOUTH_SLOPE_CHAR = 'v'
WEST_SLOPE_CHAR = '<'

type Pos = tuple[int, int]


class Path:
    def __init__(self, positions: list[Pos], previous):
        self.positions = positions
        self.previous = previous


def find_longest_path(grid: Grid, start_position: Pos, end_position: Pos):
    stack = [(start_position, None)]  # Position and previous so we don't double back
    distances = defaultdict(lambda: -1)
    distances[start_position] = 0

    while stack:
        pos, prev = stack.pop()
        distance_to_next = distances[pos] + 1
        next_positions = grid.get_adjacent_positions(pos[0], pos[1])
        next_positions = [p for p in next_positions if can_traverse_to_pos(pos, p, grid.get_cell(p[0], p[1]))]
        next_positions = [p for p in next_positions if p != prev and distance_to_next > distances[p]]

        for next_pos in next_positions:
            distances[next_pos] = distance_to_next
            pos_pair = (next_pos, pos)
            if pos_pair not in stack:
                stack.append(pos_pair)

    return distances[end_position]


def can_traverse_to_pos(from_pos: Pos, to_pos: Pos, to_char: str):
    if to_char == WALL_CHAR:
        return False
    if to_char == OPEN_CHAR:
        return True

    dx = to_pos[0] - from_pos[0]
    if dx == 1 and to_char == EAST_SLOPE_CHAR:
        return True
    if dx == -1 and to_char == WEST_SLOPE_CHAR:
        return True

    dy = to_pos[1] - from_pos[1]
    if dy == 1 and to_char == SOUTH_SLOPE_CHAR:
        return True
    if dy == -1 and to_char == NORTH_SLOPE_CHAR:
        return True

    return False
