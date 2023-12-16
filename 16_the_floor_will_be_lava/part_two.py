from grid import Grid

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    grid = Grid.from_file(INPUT_FILE_PATH)
    highest_possible = grid.highest_energized_from_entering_edge()
    print(f'Highest energization possible: {highest_possible}')


if __name__ == '__main__':
    main()
