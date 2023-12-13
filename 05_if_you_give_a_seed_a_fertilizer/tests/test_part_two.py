from part_two import parse_seed_list


def test_parse_seed_list():
    line = 'seeds:  4  2 9 5  '
    assert parse_seed_list(line) == [(4, 5), (9, 13)]
