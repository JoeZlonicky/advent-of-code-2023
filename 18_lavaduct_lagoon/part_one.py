from dig_plan import parse_dig_plan_from_file
from dig_map import DigMap

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    dig_plan = parse_dig_plan_from_file(INPUT_FILE_PATH)
    dig_map = DigMap.from_dig_plan(dig_plan)
    dig_map.span_fill((1, 1))  # There is no guarantee that is point is valid... but if it works then it works
    count = dig_map.count_marked_cells()
    print(f'N marked cells: {count}')


if __name__ == '__main__':
    main()
