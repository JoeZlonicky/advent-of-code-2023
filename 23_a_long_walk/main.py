from grid import Grid
from pathing import find_longest_path

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    map_grid = Grid.from_file(INPUT_FILE_PATH)
    longest = find_longest_path(map_grid, (1, 0), (map_grid.width - 2, map_grid.height - 1))
    print(f'Longest path: {longest}')


if __name__ == '__main__':
    main()
