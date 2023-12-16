from grid import Grid

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    grid = Grid.from_file(INPUT_FILE_PATH)
    n_energized = grid.count_energized((0, 0), (1, 0))
    print(f'Energized: {n_energized}')


if __name__ == '__main__':
    main()
