from galaxy_map import GalaxyMap

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    g_map = GalaxyMap.from_file(INPUT_FILE_NAME, 2)
    distance_sum = 0
    for pair in g_map.get_galaxy_pairs():
        distance_sum += g_map.distance_between_positions(pair[0], pair[1])
    print(f'Distance sum: {distance_sum}')


if __name__ == '__main__':
    main()
