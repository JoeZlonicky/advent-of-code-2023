from part_one import parse_hands_from_file


def test_parse_hands_from_file():
    hands = parse_hands_from_file('../inputs/example_input.txt')
    assert len(hands) == 5
