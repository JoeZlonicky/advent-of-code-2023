from heapdict import heapdict
from collections import defaultdict
from dataclasses import dataclass
from math import inf
from city_map import CityMap


@dataclass(frozen=True)
class Node:
    pos: tuple[int, int]
    history: tuple[int, int]

    def __eq__(self, other):
        return self.pos == other.pos and self.history == other.history


def find_min_path_cost(start: tuple[int, int], end: tuple[int, int], city_map: CityMap, min_repeat=0,
                       max_repeat=inf) -> int:
    start_node = Node(start, (0, 0))
    hd = heapdict()
    hd[start_node] = 0

    path_cost = defaultdict(lambda: 1000000000)
    path_cost[start_node] = 0

    while hd:
        current, _ = hd.popitem()

        if current.pos == end and (abs(current.history[0]) >= min_repeat or abs(current.history[1]) >= min_repeat):
            return path_cost[current]

        neighbors = city_map.get_surrounding_positions(current.pos[0], current.pos[1])
        for neighbor in neighbors:
            direction_to = (neighbor[0] - current.pos[0], neighbor[1] - current.pos[1])

            if not is_valid_direction(direction_to, current.history, min_repeat, max_repeat):
                continue

            if abs(direction_to[0]) > 0 and abs(current.history[0]) > 0:
                history = (current.history[0] + direction_to[0], 0)
            elif abs(direction_to[1]) > 0 and abs(current.history[1]) > 0:
                history = (0, current.history[1] + direction_to[1])
            else:
                history = direction_to

            cost_to = path_cost[current] + city_map.get_value(neighbor[0], neighbor[1])
            neighbor_node = Node(neighbor, history)

            if cost_to < path_cost[neighbor_node]:
                path_cost[neighbor_node] = cost_to
                hd[neighbor_node] = cost_to

    return -1


def is_valid_direction(direction, history, min_repeat=0, max_repeat=inf) -> bool:
    if history == (0, 0):
        return True

    if (direction[0] > 0 > history[0]) or (direction[0] < 0 < history[0]):
        return False
    if (direction[1] > 0 > history[1]) or (direction[1] < 0 < history[1]):
        return False

    combined = (history[0] + direction[0], history[1] + direction[1])
    furthest = max(abs(combined[0]), abs(combined[1]))
    if combined[0] != 0 and combined[1] != 0:  # Turning
        if furthest < min_repeat:
            return False
    return furthest <= max_repeat
