from functions import parse_ints_from_file, extrapolate_value_history

INPUT_FILE_NAME = './inputs/puzzle.txt'


def main():
    values = parse_ints_from_file(INPUT_FILE_NAME)
    extrapolated_value_sum = 0
    for history in values:
        extrapolated_value_sum += extrapolate_value_history(history, False)
    print(f'Sum of extrapolated values: {extrapolated_value_sum}')


if __name__ == '__main__':
    main()
