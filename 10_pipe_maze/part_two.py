from functions import parse_grid_from_file, find_char_in_grid, determine_grid_loop, count_inner_tiles_in_grid

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    grid = parse_grid_from_file(INPUT_FILE_NAME)
    start_pos = find_char_in_grid(grid, 'S')
    loop = determine_grid_loop(grid, start_pos)
    inner_tiles = count_inner_tiles_in_grid(grid, loop)
    print(f'Inner tiles: {inner_tiles}')


if __name__ == '__main__':
    main()
