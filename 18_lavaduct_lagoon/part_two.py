from dig_plan import parse_dig_plan_from_file

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    dig_plan = parse_dig_plan_from_file(INPUT_FILE_PATH, True)
    print(dig_plan.calculate_n_squares())


if __name__ == '__main__':
    main()
