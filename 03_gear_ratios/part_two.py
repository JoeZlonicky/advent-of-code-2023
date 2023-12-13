INPUT_FILE_NAME = 'inputs/puzzle.txt'
GEAR_SYMBOL = '*'


class StringRectArea:
    def __init__(self, string, start_pos, end_pos):
        self.string = string
        self.start_pos = start_pos
        self.end_pos = end_pos

    def __eq__(self, other):
        if not isinstance(other, StringRectArea):
            return False
        return self.string == other.string and self.start_pos == other.start_pos and self.end_pos == other.end_pos

    def __str__(self):
        return f'{self.string}: {self.start_pos}, {self.end_pos}'


def main():
    lines = get_lines_from_text_file(INPUT_FILE_NAME)
    n_lines = len(lines)

    number_rects, gear_rects = [], []
    for line_number, line in enumerate(lines):
        new_number_rects, new_symbol_rects = get_string_rects_from_line(line, line_number, line_number == n_lines - 1)
        number_rects += new_number_rects
        gear_rects += new_symbol_rects

    intersection_groups = calculate_rect_intersections(number_rects, gear_rects)
    gear_ratio_sum = 0
    for group in intersection_groups:
        gear_ratio_sum += calc_gear_ratio(group)
    print(gear_ratio_sum)


def get_lines_from_text_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        return [line for line in lines if line != '']


# Creates StringRectAreas of the exact size for consecutive numbers and areas with +1 margin for GEAR_SYMBOL
# Returns a tuple in the format of: (number_rects, gear_rects)
def get_string_rects_from_line(line, line_number, is_last_line=False):
    consecutive_number_characters = ''
    number_rects = []
    gear_rects = []

    line_length = len(line)
    for x, char in enumerate(line):
        if '0' <= char <= '9':
            if x == line_length - 1:
                number_rects.append(create_number_rect(consecutive_number_characters + char, x, line_number))
            else:
                consecutive_number_characters += char
            continue

        if consecutive_number_characters:
            number_rects.append(create_number_rect(consecutive_number_characters, x - 1, line_number))
            consecutive_number_characters = ''

        if char == GEAR_SYMBOL:
            gear_rects.append(create_symbol_rect(char, x, line_number, is_last_line, x == line_length - 1))

    return number_rects, gear_rects


def create_number_rect(number_string, end_x, y):
    return StringRectArea(number_string,
                          (end_x - (len(number_string) - 1), y),
                          (end_x, y))


def create_symbol_rect(symbol_char, x, y, is_last_row=False, is_last_column=False):
    return StringRectArea(symbol_char,
                          (max(x - 1, 0), max(y - 1, 0)),
                          (x if is_last_column else x + 1, y if is_last_row else y + 1))


# Use 2D AABB to find intersections between StringRectArea
# Returns a 2D list, grouping first_rects by intersections of the same rect of second_rects
def calculate_rect_intersections(first_rects, second_rects):
    intersections = []
    for second in second_rects:
        intersection_group = []
        for first in first_rects:
            is_to_right = first.start_pos[0] > second.end_pos[0]
            is_to_left = first.end_pos[0] < second.start_pos[0]
            is_above = first.end_pos[1] < second.start_pos[1]
            is_below = first.start_pos[1] > second.end_pos[1]
            if not (is_to_right or is_to_left or is_above or is_below):
                intersection_group.append(first)

        if intersection_group:
            intersections.append(intersection_group)

    return intersections


def calc_gear_ratio(gear_intersections):
    if len(gear_intersections) != 2:
        return 0
    return int(gear_intersections[0].string) * int(gear_intersections[1].string)


if __name__ == "__main__":
    main()
