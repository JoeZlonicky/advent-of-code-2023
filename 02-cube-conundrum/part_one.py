from shared_functions import get_lines_from_text_file, parse_game_from_line

INPUT_FILE = 'input.txt'
COLOR_RESTRICTIONS = {
    'red': 12,
    'green': 13,
    'blue': 14
}


def main():
    lines = get_lines_from_text_file(INPUT_FILE)
    game_idx_sum = 0
    for line in lines:
        game_idx, game_data = parse_game_from_line(line)
        if is_game_valid(game_data, COLOR_RESTRICTIONS):
            game_idx_sum += game_idx
    print(game_idx_sum)


# Expects game_data to be in the format of: [{'color': n, 'color2': n, ...}, ...]
# Expects color_restrictions to be in the format of: {'color': max_n, ...}
def is_game_valid(game_data, color_restrictions):
    for round_data in game_data:
        for color in round_data:
            if color in color_restrictions and round_data[color] > color_restrictions[color]:
                return False
    return True


if __name__ == '__main__':
    main()
