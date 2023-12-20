from count_pulses import count_pulses_n_times
from parse_input_file import parse_input_file

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    modules = parse_input_file(INPUT_FILE_PATH)
    low, high = count_pulses_n_times(modules, 1000)
    print(f'Low: {low}, High: {high}')
    print(f'Multiplied: {low * high}')


if __name__ == '__main__':
    main()
