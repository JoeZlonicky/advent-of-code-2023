from part_one import get_outer_digit_characters


def test_only_numbers():
    assert get_outer_digit_characters('12') == ('1', '2')


def test_long_number():
    assert get_outer_digit_characters('23431231231231235234239') == ('2', '9')


def test_numbers_and_letters():
    assert get_outer_digit_characters('a0b2c') == ('0', '2')


def test_only_one_number():
    assert get_outer_digit_characters('1abc') == ('1', '1')


def test_empty_string():
    assert get_outer_digit_characters('') == ('', '')


def test_no_numbers():
    assert get_outer_digit_characters('abcdefaasda') == ('', '')
