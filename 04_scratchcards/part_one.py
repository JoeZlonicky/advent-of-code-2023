from card import Card
from helper_functions import get_lines_from_text_file

INPUT_FILE_NAME = "input.txt"


def main():
    lines = get_lines_from_text_file(INPUT_FILE_NAME)
    cards = [Card.from_line(line) for line in lines]
    point_sum = 0
    for card in cards:
        point_sum += card.calculate_points()
    print(point_sum)


if __name__ == "__main__":
    main()
