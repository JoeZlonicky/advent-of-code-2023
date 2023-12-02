INPUT_FILE = 'input.txt'


class NumberStringWindow:
    def __init__(self, string_name, corresponding_number):
        self.string_name = string_name
        self.string_length = len(self.string_name)
        self.corresponding_number = corresponding_number
        self.current_window = ''

    # Returns true when the window matches the number string
    def update(self, c):
        self.current_window += c
        self.current_window = self.current_window[-self.string_length:]
        return self.current_window == self.string_name

    def reverse_window(self):
        self.string_name = self.string_name[::-1]


def main():
    try:
        lines = parse_text_file(INPUT_FILE)
    except FileNotFoundError:
        print(f'File not found: {INPUT_FILE}')
        return

    total_sum = 0
    for line in lines:
        digits = get_outer_digits(line)
        if digits == (-1, -1):
            continue
        total_sum += int(str(digits[0]) + str(digits[1]))
    print(total_sum)


def parse_text_file(file_name):
    with open(file_name) as f:
        stripped_lines = [line.strip() for line in f]
        return [line for line in stripped_lines if line != '']


def get_outer_digits(text):
    leftmost = get_first_digit(text)
    rightmost = get_first_digit(text, True)
    return leftmost, rightmost


def get_first_digit(text, from_end=False):
    number_windows = [NumberStringWindow(name, number) for number, name in enumerate(
        ['zero', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'])]

    if from_end:
        for window in number_windows:
            window.reverse_window()
        text = reversed(text)

    for c in text:
        if '0' <= c <= '9':
            return int(c)
        for window in number_windows:
            if window.update(c):
                return window.corresponding_number

    return -1


if __name__ == '__main__':
    main()
