from collections import deque, defaultdict
from garden_map import GardenMap
from math import inf
from numpy import linalg

type Pos = tuple[int, int]


def n_garden_plots_in_exact_steps(garden_map: GardenMap, start_pos: Pos, steps: int) -> int:
    min_steps = defaultdict(lambda: inf)
    min_steps[start_pos] = 0

    reachable = {}
    parity = steps % 2
    if parity == 0:
        reachable[start_pos] = True

    q = deque()
    q.append(start_pos)
    while q:
        current_pos = q.popleft()
        current_distance = min_steps[current_pos]

        adjacent = [(current_pos[0] + 1, current_pos[1]), (current_pos[0] - 1, current_pos[1]),
                    (current_pos[0], current_pos[1] + 1), (current_pos[0], current_pos[1] - 1)]
        adjacent = [pos for pos in adjacent if garden_map.is_pos_passable(pos[0], pos[1])]

        distance_to_adjacent = current_distance + 1
        if distance_to_adjacent > steps:
            continue

        for adj in adjacent:
            if distance_to_adjacent < min_steps[adj]:
                min_steps[adj] = distance_to_adjacent
                q.append(adj)

            if adj not in reachable and (distance_to_adjacent % 2 == parity):
                reachable[adj] = True

    return len(reachable)
