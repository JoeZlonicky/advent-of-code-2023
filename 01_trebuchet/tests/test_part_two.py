from part_two import NumberStringWindow, get_outer_digits, get_first_digit


def test_number_string_window_update():
    window = NumberStringWindow('two', 2)
    assert window.update('t') is False
    assert window.update('w') is False
    assert window.update('o') is True


def test_number_string_window_reverse_window():
    window = NumberStringWindow('nine', 9)
    window.reverse_window()
    assert window.update('e') is False
    assert window.update('n') is False
    assert window.update('i') is False
    assert window.update('n') is True


def test_get_outer_digits_with_number_digits():
    assert get_outer_digits('a1b2c3d') == (1, 3)


def test_get_outer_digits_with_number_digit_and_word():
    assert get_outer_digits('athreec9') == (3, 9)


def test_get_outer_digits_with_words():
    assert get_outer_digits('azerofoursevenabc') == (0, 7)


def test_get_first_digit_with_number():
    assert get_first_digit('a1bfsdfs') == 1


def test_get_first_digit_with_word():
    assert get_first_digit('aafouraasd') == 4


def test_get_first_digit_reversed_with_word():
    assert get_first_digit('aaseven3twonineaasd', True) == 9
