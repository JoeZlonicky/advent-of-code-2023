from pipe_grid import PipeGrid
from loop_functions import determine_grid_loop
from inner_tile_functions import count_inner_tiles_in_grid

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    grid = PipeGrid.from_file(INPUT_FILE_NAME)
    loop = determine_grid_loop(grid)
    inner_tiles = count_inner_tiles_in_grid(grid, loop)
    print(f'Inner tiles: {inner_tiles}')


if __name__ == '__main__':
    main()
