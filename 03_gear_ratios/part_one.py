INPUT_FILE_NAME = 'inputs/puzzle.txt'
IGNORED_SYMBOLS = ['.']


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

    number_rects, symbol_rects = [], []
    for line_number, line in enumerate(lines):
        new_number_rects, new_symbol_rects = get_string_rects_from_line(line, line_number, line_number == n_lines - 1)
        number_rects += new_number_rects
        symbol_rects += new_symbol_rects

    parts = calculate_intersected(number_rects, symbol_rects)
    total_sum = 0
    for part in parts:
        total_sum += int(part.string)
    print(total_sum)


def get_lines_from_text_file(file_name):
    with open(file_name) as f:
        lines = [line.strip() for line in f]
        return [line for line in lines if line != '']


# Creates StringRectAreas of the exact size for consecutive numbers, nothing for IGNORED_SYMBOLS,
# and areas with +1 margin for all other symbols
# Returns a tuple in the format of: (number_rects, symbol_rects)
def get_string_rects_from_line(line, line_number, is_last_line=False):
    consecutive_number_characters = ''
    number_rects = []
    symbol_rects = []

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

        if char not in IGNORED_SYMBOLS:
            symbol_rects.append(create_symbol_rect(char, x, line_number, is_last_line, x == line_length - 1))

    return number_rects, symbol_rects


def create_number_rect(number_string, end_x, y):
    return StringRectArea(number_string,
                          (end_x - (len(number_string) - 1), y),
                          (end_x, y))


def create_symbol_rect(symbol_char, x, y, is_last_row=False, is_last_column=False):
    return StringRectArea(symbol_char,
                          (max(x - 1, 0), max(y - 1, 0)),
                          (x if is_last_column else x + 1, y if is_last_row else y + 1))


# Use 2D AABB to find intersections between StringRectArea
# Returns a list of all the first_rects that intersect with at least one of second_rects
def calculate_intersected(first_rects, second_rects):
    intersected = []
    for first in first_rects:
        for second in second_rects:
            is_to_right = first.start_pos[0] > second.end_pos[0]
            is_to_left = first.end_pos[0] < second.start_pos[0]
            is_above = first.end_pos[1] < second.start_pos[1]
            is_below = first.start_pos[1] > second.end_pos[1]
            if not (is_to_right or is_to_left or is_above or is_below):
                intersected.append(first)
                break
    return intersected


if __name__ == "__main__":
    main()
