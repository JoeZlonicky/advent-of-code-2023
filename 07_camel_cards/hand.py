from enum import IntEnum


class HandType(IntEnum):
    HIGH_CARD = 1
    ONE_PAIR = 2
    TWO_PAIR = 3
    THREE_OF_A_KIND = 4
    FULL_HOUSE = 5
    FOUR_OF_A_KIND = 6
    FIVE_OF_A_KIND = 7


class Hand:
    HAND_SIZE = 5
    IS_JOKER_WILD = False

    def __init__(self, cards: list[str], bid: int = 0):
        self.cards = cards
        self.bid = bid
        self.counts = self.count_cards(cards)
        self.type = self.determine_hand_type(self.counts)

    def __lt__(self, other):
        if self.type != other.type:
            return self.type < other.type

        for i in range(self.HAND_SIZE):
            card, other_card = self.cards[i], other.cards[i]
            worth, other_worth = self.get_card_worth(card), self.get_card_worth(other_card)
            if worth != other_worth:
                return worth < other_worth
        return False  # Value doesn't really matter because they are equivalent

    @classmethod
    def from_line(cls, line) -> 'Hand':
        hand, bid = line.split()
        return cls(list(hand), int(bid))

    @staticmethod
    def count_cards(cards: list[str]) -> dict[str, int]:
        counts = {}
        for card in cards:
            counts[card] = counts.get(card, 0) + 1
        return counts

    @staticmethod
    def determine_hand_type(counts: dict[str, int]) -> HandType:
        n_counts = len(counts)
        if n_counts == 1:
            return HandType.FIVE_OF_A_KIND

        if 'J' in counts and Hand.IS_JOKER_WILD:
            return Hand.determine_best_hand_type_with_joker_as_wild(counts)

        if n_counts == 4:
            return HandType.ONE_PAIR
        if n_counts == 5:
            return HandType.HIGH_CARD
        if n_counts == 2:
            first_card = next(iter(counts))
            first_count = counts[first_card]
            return HandType.FOUR_OF_A_KIND if first_count == 4 or first_count == 1 else HandType.FULL_HOUSE
        for card in counts:
            if counts[card] == 3:
                return HandType.THREE_OF_A_KIND
            if counts[card] == 2:
                return HandType.TWO_PAIR

    @staticmethod
    def determine_best_hand_type_with_joker_as_wild(counts: dict[str, int]) -> HandType:
        n_jokers = counts['J']
        if n_jokers == 0:
            return Hand.determine_hand_type(counts)

        counts_without_joker = {card: count for card, count in counts.items() if card != 'J'}
        hand_types = []
        for card in counts_without_joker:
            counts_with_wild_joker = {other_card: count + n_jokers if other_card == card else count for
                                      other_card, count in counts_without_joker.items()}
            hand_type_with_wild_joker = Hand.determine_hand_type(counts_with_wild_joker)
            hand_types.append(hand_type_with_wild_joker)
        hand_types.sort()
        return hand_types[-1]

    @staticmethod
    def get_card_worth(card):
        if card.isdigit():
            return int(card)

        if card == 'A':
            return 14
        if card == 'K':
            return 13
        if card == 'Q':
            return 12
        if card == 'J':
            return 1 if Hand.IS_JOKER_WILD else 11

        assert card == 'T'
        return 10
