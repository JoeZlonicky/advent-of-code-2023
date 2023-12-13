from card import Card


def test_from_line():
    card = Card.from_line('Card  12: 3  23 4 | 9  7 23')
    assert card.number == 12
    assert card.winning_numbers == [3, 23, 4]
    assert card.numbers_in_possession == [9, 7, 23]


def test_get_matching_numbers():
    card = Card.from_line('Card  32: 1 2 3 | 4 5 2 6 1')
    matching = card.get_matching_numbers()
    assert set(matching) == {1, 2}


def test_calculate_points():
    card = Card.from_line('Card  32: 1 2 3 | 1 2 3')
    assert card.calculate_points() == 4


def test_calculate_points_when_no_matches():
    card = Card.from_line('Card  32: 1 2 3 | 4 5 6')
    assert card.calculate_points() == 0
