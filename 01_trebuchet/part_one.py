INPUT_FILE = 'inputs/puzzle.txt'


def main():
    try:
        lines = parse_text_file(INPUT_FILE)
    except FileNotFoundError:
        print(f'File not found: {INPUT_FILE}')
        return

    total_sum = 0
    for line in lines:
        digit_characters = get_outer_digit_characters(line)
        if digit_characters == ('', ''):
            continue
        total_sum += int(digit_characters[0] + digit_characters[1])
    print(total_sum)


def parse_text_file(file_name):
    with open(file_name) as f:
        stripped_lines = [line.strip() for line in f]
        return [line for line in stripped_lines if line != '']


def get_outer_digit_characters(text):
    leftmost = next((c for c in text if '0' <= c <= '9'), '')
    rightmost = next((c for c in reversed(text) if '0' <= c <= '9'), '')
    return leftmost, rightmost


if __name__ == '__main__':
    main()
