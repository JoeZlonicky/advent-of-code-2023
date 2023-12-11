from functions import parse_grid_from_file, find_char_in_grid, determine_grid_loop, calculate_furthest_steps_of_loop

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    grid = parse_grid_from_file(INPUT_FILE_NAME)
    start_pos = find_char_in_grid(grid, 'S')
    loop = determine_grid_loop(grid, start_pos)
    furthest_steps = calculate_furthest_steps_of_loop(loop)
    print(f'Furthest steps: {furthest_steps}')


if __name__ == '__main__':
    main()
