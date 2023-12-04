from card import Card
from helper_functions import get_lines_from_text_file

INPUT_FILE_NAME = "input.txt"


def main():
    lines = get_lines_from_text_file(INPUT_FILE_NAME)
    cards = [Card.from_line(line) for line in lines]

    number_of_cards = [1 for _ in cards]
    for idx, card in enumerate(cards):
        n_matching = len(card.get_matching_numbers())

        n_copies = number_of_cards[idx]
        for i in range(n_matching):
            k = idx + i + 1
            number_of_cards[k] += n_copies

    total_number_of_cards = sum(number_of_cards)
    print(total_number_of_cards)


if __name__ == "__main__":
    main()
