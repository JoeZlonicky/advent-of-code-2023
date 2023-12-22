from collections import deque, defaultdict
from garden_map import GardenMap
from math import inf
import numpy as np

type Pos = tuple[int, int]


def n_garden_plots_in_exact_steps(garden_map: GardenMap, steps: int) -> int:
    start_pos = garden_map.start_pos

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


# This assumes that the plots follow a quadratic equation for the steps intervals of (i * MAP_SIZE) + START_OFFSET
# Shoutout to r/adventofcode for pointing in the direction of this solution
def solve_quadratic_for_exact_steps(garden_map: GardenMap, steps: int) -> int:
    def generate_ith_steps(i):
        return i * garden_map.width + garden_map.start_pos[0]

    a = []
    b = []
    for x in range(3):
        s = generate_ith_steps(x)
        n = n_garden_plots_in_exact_steps(garden_map, s)
        a.append([s * s, s, 1])
        b.append(n)

    coefficients = np.linalg.solve(np.array(a), np.array(b))
    solution = steps * steps * coefficients[0] + steps * coefficients[1] + coefficients[2]
    return round(solution.real)
