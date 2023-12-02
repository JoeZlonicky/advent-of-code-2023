def get_lines_from_text_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        return [line for line in lines if line != '']


# Expects line in the format of: Game #: # color, # color2; # color, # color2, # color3; ...
# Return a tuple in the format of: (game_idx, [{'color': n, 'color2': n, ...}, ...])
def parse_game_from_line(line):
    game_label, rounds_list = line.split(':')
    game_idx = int(game_label.split(' ')[1])

    rounds_list = rounds_list.split(';')
    new_list = []
    for round_data in rounds_list:
        color_dict = {}
        for color_count in round_data.split(','):
            color_count = color_count.strip().split(' ')
            color_dict[color_count[1]] = int(color_count[0])
        new_list.append(color_dict)

    return game_idx, new_list
