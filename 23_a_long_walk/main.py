from grid import Grid
from pathing import find_longest_path, part_1_can_traverse, part_2_can_traverse

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    map_grid = Grid.from_file(INPUT_FILE_PATH)
    start_pos = (1, 0)
    end_pos = (map_grid.width - 2, map_grid.height - 1)

    longest = find_longest_path(map_grid, start_pos, end_pos, part_1_can_traverse)
    print(f'(Part 1) Longest path: {longest}')

    longest = find_longest_path(map_grid, start_pos, end_pos, part_2_can_traverse)
    print(f'(Part 2) Longest path: {longest}')


if __name__ == '__main__':
    main()
