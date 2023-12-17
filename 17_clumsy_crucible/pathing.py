from city_map import CityMap

type pos = tuple[int, int]

MAX_REPEAT_DIRECTION = 3


def find_min_path_cost(start: pos, end: pos, city_map: CityMap) -> int:
    search_list = [(start, None)]
    path_cost_and_straightness: dict[pos, tuple[int, tuple]] = {start: (city_map.get_value(start[0], start[1]), (0, 0))}

    while search_list:
        search_list.sort(key=lambda x: (end[0] - x[0][0]) ** 2 + (end[1] - x[0][1]) ** 2, reverse=True)
        current, previous = search_list.pop()
        if current == end:
            break

        current_straightness = path_cost_and_straightness[current][1]
        neighbors = city_map.get_surrounding_positions(current[0], current[1])
        for neighbor in neighbors:
            cost_to = path_cost_and_straightness[current][0] + city_map.get_value(neighbor[0], neighbor[1])
            # if neighbor in path_cost_and_straightness and path_cost_and_straightness[neighbor][0] <= cost_to:
            #     continue

            direction = (neighbor[0] - current[0], neighbor[1] - current[1])
            if not is_valid_direction(current_straightness, direction):
                continue

            if (current_straightness[0] != 0 and direction != 0) or (
                    current_straightness[1] != 0 and direction[1] != 0):
                neighbor_straightness = (current_straightness[0] + direction[0], 0)
            else:
                neighbor_straightness = direction

            path_cost_and_straightness[neighbor] = (cost_to, neighbor_straightness)
            choice = (neighbor, current)
            if choice not in search_list:
                search_list.append(choice)

    return path_cost_and_straightness.get(end, (-1,))[0]


def is_valid_direction(straightness, direction) -> bool:
    if (straightness[0] > 0 > direction[0]) or (straightness[0] < 0 < direction[0]):
        return False
    if (straightness[1] > 0 > direction[1]) or (straightness[1] < 0 < direction[1]):
        return False
    combined = (straightness[0] + direction[0], straightness[1] + direction[1])
    return combined[0] <= MAX_REPEAT_DIRECTION and combined[1] <= MAX_REPEAT_DIRECTION
