from hand import Hand
from parse_hands_from_file import parse_hands_from_file

INPUT_FILE_NAME = './inputs/full_input.txt'


def main():
    Hand.IS_JOKER_WILD = True
    hands = parse_hands_from_file(INPUT_FILE_NAME)
    hands.sort()

    winnings = 0
    for idx, hand in enumerate(hands):
        bid = hand.bid
        multiplier = idx + 1
        winnings += bid * multiplier
    print(winnings)


if __name__ == '__main__':
    main()