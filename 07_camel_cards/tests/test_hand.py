from hand import Hand, HandType


def test_count_cards():
    assert Hand.count_cards(['A', '8', '8', '8', 'K']) == {'A': 1, '8': 3, 'K': 1}


def test_determine_hand_type_high_card():
    assert Hand.determine_hand_type({'A': 1, '8': 1, '7': 1, '2': 1, 'Q': 1}) == HandType.HIGH_CARD


def test_determine_hand_type_one_pair():
    assert Hand.determine_hand_type({'A': 2, '7': 1, '2': 1, 'Q': 1}) == HandType.ONE_PAIR


def test_determine_hand_type_two_pair():
    assert Hand.determine_hand_type({'A': 1, '8': 2, 'Q': 2}) == HandType.TWO_PAIR


def test_determine_hand_type_with_wild_joker():
    Hand.IS_JOKER_WILD = True
    assert Hand.determine_hand_type({'A': 1, 'J': 2, '8': 1, '9': 1}) == HandType.THREE_OF_A_KIND
    assert Hand.determine_hand_type({'A': 1, 'J': 1, '8': 1, '9': 1, 'T': 1}) == HandType.ONE_PAIR
    Hand.IS_JOKER_WILD = False


def test_determine_hand_type_three_of_a_kind():
    assert Hand.determine_hand_type({'A': 1, '7': 3, 'Q': 1}) == HandType.THREE_OF_A_KIND


def test_determine_hand_type_full_house():
    assert Hand.determine_hand_type({'K': 3, 'Q': 2}) == HandType.FULL_HOUSE


def test_determine_hand_type_four_of_a_kind():
    assert Hand.determine_hand_type({'A': 4, '2': 1}) == HandType.FOUR_OF_A_KIND


def test_determine_hand_type_five_of_a_kind():
    assert Hand.determine_hand_type({'Q': 5}) == HandType.FIVE_OF_A_KIND


def test_hand_evaluation():
    good_hand = Hand(['Q', 'Q', 'Q', '9', '9'])
    bad_hand = Hand(['K', 'Q', '2', '3', '7'])
    assert good_hand > bad_hand


def test_hand_evaluation_when_same_type():
    good_hand = Hand(['9', '9', '8', '8', '5'])
    bad_hand = Hand(['9', '9', '8', '8', '4'])
    assert good_hand > bad_hand


def test_from_line():
    hand = Hand.from_line('32T3K 765')
    assert hand.cards == ['3', '2', 'T', '3', 'K']
    assert hand.bid == 765
    assert hand.counts == {'3': 2, '2': 1, 'T': 1, 'K': 1}
