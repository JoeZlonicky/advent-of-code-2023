from count_pulses import min_presses_until_one_rx_low
from parse_input_file import parse_input_file

INPUT_FILE_PATH = './inputs/puzzle.txt'


def main():
    modules = parse_input_file(INPUT_FILE_PATH)
    n_presses = min_presses_until_one_rx_low(modules)
    print(f'Min number of presses until one rx low:: {n_presses}')


if __name__ == '__main__':
    main()
