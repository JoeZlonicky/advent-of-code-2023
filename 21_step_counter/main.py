from garden_map import GardenMap
from pathing import n_garden_plots_in_exact_steps, solve_quadratic_for_exact_steps

INPUT_FILE_PATH = './inputs/puzzle.txt'
PART_ONE_STEPS = 64
PART_TWO_STEPS = 26501365


def main():
    garden_map = GardenMap.from_file(INPUT_FILE_PATH)

    part_one(garden_map)
    part_two(garden_map)


def part_one(garden_map: GardenMap):
    n = n_garden_plots_in_exact_steps(garden_map, PART_ONE_STEPS)
    print(f'(Part 1) N garden plots in exactly {PART_ONE_STEPS} steps: {n}')


def part_two(garden_map: GardenMap):
    garden_map.infinite_bounds = True
    n = solve_quadratic_for_exact_steps(garden_map, PART_TWO_STEPS)
    print(f'(Part 2) N garden plots in exactly {PART_TWO_STEPS} steps: {n}')


if __name__ == '__main__':
    main()
