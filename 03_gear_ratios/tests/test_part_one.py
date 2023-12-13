from part_one import get_string_rects_from_line, StringRectArea, create_number_rect, create_symbol_rect, \
    calculate_intersected


def test_get_string_rects_from_line_with_numbers():
    number_rects, _ = get_string_rects_from_line('1.234..5', 2)

    assert number_rects[0] == StringRectArea('1', (0, 2), (0, 2))
    assert number_rects[1] == StringRectArea('234', (2, 2), (4, 2))
    assert number_rects[2] == StringRectArea('5', (7, 2), (7, 2))


def test_get_string_rects_from_line_with_symbols():
    _, symbol_rects = get_string_rects_from_line('&..*.@', 1)
    assert symbol_rects[0] == StringRectArea('&', (0, 0), (1, 2))
    assert symbol_rects[1] == StringRectArea('*', (2, 0), (4, 2))
    assert symbol_rects[2] == StringRectArea('@', (4, 0), (5, 2))


def test_get_string_rects_from_line_with_symbols_first_row():
    _, symbol_rects = get_string_rects_from_line('-../.!', 0)
    assert symbol_rects[0] == StringRectArea('-', (0, 0), (1, 1))
    assert symbol_rects[1] == StringRectArea('/', (2, 0), (4, 1))
    assert symbol_rects[2] == StringRectArea('!', (4, 0), (5, 1))


def test_get_string_rects_from_line_with_symbols_last_row():
    _, symbol_rects = get_string_rects_from_line('^..<.>', 1, True)
    assert symbol_rects[0] == StringRectArea('^', (0, 0), (1, 1))
    assert symbol_rects[1] == StringRectArea('<', (2, 0), (4, 1))
    assert symbol_rects[2] == StringRectArea('>', (4, 0), (5, 1))


def test_create_number_rect():
    assert create_number_rect('1', 2, 2) == StringRectArea('1', (2, 2), (2, 2))


def test_create_number_rect_long():
    assert create_number_rect('1234', 4, 1) == StringRectArea('1234', (1, 1), (4, 1))


def test_create_symbol_rect():
    assert create_symbol_rect('$', 1, 1) == StringRectArea('$', (0, 0), (2, 2))


def test_create_symbol_rect_top_left_corner():
    assert create_symbol_rect('@', 0, 0) == StringRectArea('@', (0, 0), (1, 1))


def test_create_symbol_rect_bottom_right_corner():
    assert create_symbol_rect('!', 2, 2, True, True) == StringRectArea('!', (1, 1), (2, 2))


def test_calculate_intersected():
    numbers = [StringRectArea('1', (1, 1), (1, 1)),
               StringRectArea('2', (3, 3), (3, 3))]
    symbols = [StringRectArea('!', (0, 0), (2, 2))]
    assert calculate_intersected(numbers, symbols) == [numbers[0]]


def test_calculate_intersected_edge():
    numbers = [StringRectArea('3', (1, 1), (1, 1)),
               StringRectArea('4', (3, 3), (3, 3))]
    symbols = [StringRectArea('@', (3, 3), (4, 4))]
    assert calculate_intersected(numbers, symbols) == [numbers[1]]
