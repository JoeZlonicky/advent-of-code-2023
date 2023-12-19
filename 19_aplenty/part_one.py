from accept_or_reject import sum_accepted
from parse_input_file import parse_input_file

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    processors, parts = parse_input_file(INPUT_FILE_PATH)
    accepted_rating_sum = sum_accepted(processors, parts)
    print(f'Accepted rating sum: {accepted_rating_sum}')


if __name__ == '__main__':
    main()
