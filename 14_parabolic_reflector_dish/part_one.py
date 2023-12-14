from rock_grid import RockGrid, SlideDirection

INPUT_FILE_NAME = './inputs/puzzle.txt'


def main():
    grid = RockGrid.from_file(INPUT_FILE_NAME)
    grid.slide_round_rocks(SlideDirection.NORTH)
    total_load = grid.sum_round_rock_load(SlideDirection.NORTH)
    print(f'Total load: {total_load}')


if __name__ == '__main__':
    main()
