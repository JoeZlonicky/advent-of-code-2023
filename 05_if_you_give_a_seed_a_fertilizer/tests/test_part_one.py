from part_one import parse_seed_list


def test_parse_seed_list():
    line = 'seeds:  12  34 56 78  '
    assert parse_seed_list(line) == [(12, 12), (34, 34), (56, 56), (78, 78)]
