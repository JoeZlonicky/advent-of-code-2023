from garden_map import GardenMap
from pathing import n_garden_plots_in_exact_steps

INPUT_FILE_PATH = './inputs/puzzle.txt'
PART_ONE_STEPS = 64


def main():
    garden_map = GardenMap.from_file(INPUT_FILE_PATH)

    part_one(garden_map)
    part_two(garden_map)


def part_one(garden_map):
    n = n_garden_plots_in_exact_steps(garden_map, PART_ONE_STEPS)
    print(f'N garden plots in exactly {PART_ONE_STEPS} steps: {n}')


def part_two(garden_map):
    pass


if __name__ == '__main__':
    main()
