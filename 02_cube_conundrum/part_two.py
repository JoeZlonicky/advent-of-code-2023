import math

from shared_functions import get_lines_from_text_file, parse_game_from_line

INPUT_FILE = 'inputs/puzzle.txt'


def main():
    lines = get_lines_from_text_file(INPUT_FILE)
    power_sum = 0
    for line in lines:
        game_idx, game_data = parse_game_from_line(line)
        minimums = calculate_minimum_cubes_for_game(game_data)
        power_sum += calculate_power(minimums)
    print(power_sum)


# Expects game_data to be in the format of: [{'color': n, 'color2': n, ...}, ...]
# Returns in the format of: {'color': n, 'color2': n, ...}
def calculate_minimum_cubes_for_game(game_data):
    minimums = {}
    for round_data in game_data:
        for color in round_data:
            minimums[color] = max(minimums.get(color, 0), round_data[color])
    return minimums


# Expects color_counts to be in the format of: {'color': n, ...}
# Throws out counts of zero
def calculate_power(color_counts):
    counts = [n for n in color_counts.values() if n != 0]
    if len(counts) == 0:
        return 0

    return math.prod(counts)


if __name__ == '__main__':
    main()
