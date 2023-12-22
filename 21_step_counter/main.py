from garden_map import GardenMap
from pathing import n_garden_plots_in_exact_steps

INPUT_FILE_PATH = './inputs/puzzle.txt'
PART_ONE_STEPS = 64


def main():
    garden_map = GardenMap.from_file(INPUT_FILE_PATH)

    # part_one(garden_map)
    part_two(garden_map)


def part_one(garden_map: GardenMap):
    n = n_garden_plots_in_exact_steps(garden_map, garden_map.start_pos, PART_ONE_STEPS)
    print(f'(Part 1) N garden plots in exactly {PART_ONE_STEPS} steps: {n}')


def part_two(garden_map: GardenMap):
    garden_map.infinite_bounds = True

    def generate_ith_steps(i):
        return i * garden_map.width + garden_map.start_pos[0]

    for x in range(3):
        steps = generate_ith_steps(x)
        n = n_garden_plots_in_exact_steps(garden_map, garden_map.start_pos, steps)
        print(f'a{steps * steps} + b{steps} + c = {n}')

    # Put values into gauss jordan elimination solver
    # Use result to create a new quadratic equation
    # Enter exact steps of problem
    # Answer!


if __name__ == '__main__':
    main()
