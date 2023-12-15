from hash_algorithm import hash_and_sum
from parse_input_file import parse_input_file_csv

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    values = parse_input_file_csv(INPUT_FILE_PATH)
    hash_sum = hash_and_sum(values)
    print(f'Sum: {hash_sum}')


if __name__ == '__main__':
    main()
