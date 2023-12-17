import heapq
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
    search_list = [start_node]

    path_cost: dict[Node, int] = {start_node: 0}

    while search_list:
        search_list.sort(key=lambda x: path_cost[x], reverse=True)
        current = search_list.pop()
        if current.pos == end:
            if current.history[0] < min_repeat and current.history[1] < min_repeat:
                continue
            return path_cost[current]

        neighbors = city_map.get_surrounding_positions(current.pos[0], current.pos[1])
        for neighbor in neighbors:
            direction_to = (neighbor[0] - current.pos[0], neighbor[1] - current.pos[1])

            if not is_valid_direction(direction_to, current.history, min_repeat, max_repeat):
                continue

            if direction_to[0] > 0 and current.history[0] > 0:
                history = (current.history[0] + 1, 0)
            elif direction_to[1] > 0 and current.history[1] > 0:
                history = (0, current.history[1] + 1)
            else:
                history = direction_to

            neighbor_node = Node(neighbor, history)
            cost_to = path_cost[current] + city_map.get_value(neighbor[0], neighbor[1])

            if neighbor_node in path_cost and path_cost[neighbor_node] < cost_to:
                continue

            path_cost[neighbor_node] = cost_to
            if neighbor_node not in search_list:
                search_list.append(neighbor_node)

    return -1


def is_valid_direction(direction, history, min_repeat=0, max_repeat=inf) -> bool:
    if history == (0, 0):
        return True

    if (direction[0] > 0 > history[0]) or (direction[0] < 0 < history[0]):
        return False
    if (direction[1] > 0 > history[1]) or (direction[1] < 0 < history[1]):
        return False

    combined = (history[0] + direction[0], history[1] + direction[1])
    if combined[0] != 0 and combined[1] != 0:  # Turning
        if abs(history[0]) < min_repeat and abs(history[1]) < min_repeat:
            return False
    return combined[0] <= max_repeat and combined[1] <= max_repeat
