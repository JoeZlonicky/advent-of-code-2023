from loop_functions import determine_grid_loop, calculate_furthest_steps_of_loop
from pipe_grid import PipeGrid

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    grid = PipeGrid.from_file(INPUT_FILE_NAME)
    loop = determine_grid_loop(grid)
    furthest_steps = calculate_furthest_steps_of_loop(loop)
    print(f'Furthest steps: {furthest_steps}')


if __name__ == '__main__':
    main()
