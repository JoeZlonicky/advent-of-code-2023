from functions import parse_puzzle_input, count_ghost_steps_to_destination

INPUT_FILE_NAME = 'inputs/puzzle.txt'


def main():
    instructions, nodes = parse_puzzle_input(INPUT_FILE_NAME)
    steps = count_ghost_steps_to_destination(instructions, nodes, 'A', 'Z')
    print(f'Steps: {steps}')


if __name__ == "__main__":
    main()
