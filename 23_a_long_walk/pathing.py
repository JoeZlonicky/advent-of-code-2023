from collections import defaultdict
from dataclasses import dataclass
from grid import Grid

WALL_CHAR = '#'
OPEN_CHAR = '.'
NORTH_SLOPE_CHAR = '^'
EAST_SLOPE_CHAR = '>'
SOUTH_SLOPE_CHAR = 'v'
WEST_SLOPE_CHAR = '<'

type Pos = tuple[int, int]


@dataclass
class Path:
    start: Pos
    second: Pos
    end: Pos
    distance: int


def find_longest_path(grid: Grid, start_position: Pos, end_position: Pos, can_traverse_predicate):
    paths_to_explore: list[tuple[Pos, Pos]] = []  # Stores (prev, start) so goes in right direction
    explored_paths: dict[Pos, list[Path]] = defaultdict(lambda: [])
    current_path = [start_position, start_position]

    while True:
        pos = current_path[-1]
        next_positions = grid.get_adjacent_positions(pos[0], pos[1])
        next_positions = [p for p in next_positions if can_traverse_predicate(pos, p, grid.get_cell(p[0], p[1]))]
        next_positions = [p for p in next_positions if p not in current_path]

        if len(next_positions) == 0:
            # Dead-end
            if not paths_to_explore:
                break

            first, second = paths_to_explore.pop()
            current_path = [first, second]
            continue
        elif len(next_positions) == 1:
            next_pos = next_positions[0]
            current_path.append(next_pos)
            if next_pos == end_position:
                explored_paths[current_path[0]].append(
                    Path(current_path[0], current_path[1], current_path[-1], len(current_path) - 1))
                if not paths_to_explore:
                    break

                first, second = paths_to_explore.pop()
                current_path = [first, second]
            continue

        # Split in path
        for next_pos in next_positions:
            path_already_explored = False
            for path in explored_paths[pos]:
                if next_pos == path.second:
                    path_already_explored = True
                    break
            if path_already_explored:
                continue

            first_two = (pos, next_pos)
            if first_two in paths_to_explore:
                continue

            paths_to_explore.append(first_two)

        explored_paths[current_path[0]].append(
            Path(current_path[0], current_path[1], current_path[-1], len(current_path) - 1))
        if not paths_to_explore:
            break

        first, second = paths_to_explore.pop()
        current_path = [first, second]

    longest_distance = find_longest_path_combination(explored_paths, start_position, end_position)
    return longest_distance


def find_longest_path_combination(paths: dict[Pos, list[Path]], start_position: Pos, end_position: Pos,
                                  travelled=None) -> int:
    if travelled is None:
        travelled = [paths[start_position][0]]

    current_path = travelled[-1]
    if current_path.end == end_position:
        distance_sum = 0
        for path in travelled:
            distance_sum += path.distance
        return distance_sum

    longest_distance = -1
    for path in paths[current_path.end]:
        if path == current_path or path.start != current_path.end:
            continue

        is_looping = False
        for t_path in travelled[:-1]:
            if t_path.end == path.start:
                is_looping = True
                break
        if is_looping:
            continue

        path_distance = find_longest_path_combination(paths, start_position, end_position, travelled + [path])
        if path_distance > longest_distance:
            longest_distance = path_distance

    return longest_distance


def part_1_can_traverse(from_pos: Pos, to_pos: Pos, to_char: str):
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


def part_2_can_traverse(from_pos: Pos, to_pos: Pos, to_char: str):
    return to_char != WALL_CHAR
