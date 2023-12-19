from accept_or_reject import count_distinct_combinations_of_accepted
from parse_input_file import parse_input_file

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    processors, _ = parse_input_file(INPUT_FILE_PATH)
    n_distinct = count_distinct_combinations_of_accepted(processors, 1, 4000)
    print(f'N distinct combinations: {n_distinct}')


if __name__ == '__main__':
    main()
