from functions import parse_puzzle_input, count_steps_to_destination

INPUT_FILE_NAME = './inputs/full_input.txt'


def main():
    instructions, nodes = parse_puzzle_input(INPUT_FILE_NAME)
    steps = count_steps_to_destination(instructions, nodes, 'AAA', lambda x: x == 'ZZZ')
    print(f'Steps: {steps}')


if __name__ == "__main__":
    main()
