VALUE_MULTIPLIER = 17
VALUE_MODULO = 256


def hash_and_sum(values: list[str]) -> int:
    hash_sum = 0
    for value in values:
        hash_sum += hash_string(value)
    return hash_sum


def hash_string(s: str) -> int:
    current_value = 0
    for char in s:
        current_value += get_ascii_code(char)
        current_value *= VALUE_MULTIPLIER
        current_value %= VALUE_MODULO
    return current_value


def get_ascii_code(char: str) -> int:
    return ord(char)
