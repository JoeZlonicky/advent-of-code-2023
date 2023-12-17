from city_map import CityMap
from pathing import find_min_path_cost

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    city_map = CityMap.from_file(INPUT_FILE_PATH)
    min_cost = find_min_path_cost((0, 0), (city_map.width - 1, city_map.height - 1), city_map, 4, 10)
    print(f'Min cost: {min_cost}')


if __name__ == '__main__':
    main()
